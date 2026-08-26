"""
web-ppt-generator / qa_render.py

생성 후 QA(Post-Generation QA)용 스크린샷 렌더러 + Typography/Layout 감사 도구.
web_ppt/v{N}/index.html을 Playwright/Chromium으로 실제 렌더링해, 지정한 슬라이드
(또는 전체 슬라이드)를 브라우저가 보여주는 그대로 PNG로 캡처한다. `--audit-fonts`를
같이 주면 각 텍스트 요소의 **실제 computed font-size**(코드의 선언값이 아니라
브라우저가 최종 계산한 값)를 pt 단위로 함께 추출한다. `--audit-layout`을 같이 주면
겹침(overlap)/캔버스 이탈(overflow)/텍스트 잘림(clipping)처럼 좌표·CSS 값만으로
기계적으로 판정 가능한 항목을 함께 감사해 `layout-audit.json`으로 저장한다 — 이
결과는 어떤 슬라이드를 LLM이 스크린샷으로 직접 봐야 하는지 미리 걸러내기 위한
것이며, 응집도·시각적 균형·가독성 등 정성적 판단을 대체하지 않는다.

이 스크립트는 pptx 변환(pptx-exporter/scripts/export_pptx.py)과 역할이 다르다 —
좌표를 추출해 pptx 네이티브 요소로 재구성하지 않고, content-designer가 눈으로
검토(Visual Quality Check)하거나 수치로 대조(Typography/Layout Compliance Check)할
수 있는 원시 자료만 만든다. 디자인 규칙을 판단하거나 수정하지 않는다.

사용:
    python qa_render.py --web-ppt /output/{project-name}/web_ppt/v{N} \
        --out /output/{project-name}/.qa/v{N} [--slides 4,7,10,13] \
        [--audit-fonts] [--audit-layout]

설치(최초 1회, pptx-exporter와 공유): pip install playwright && playwright install chromium
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SLIDE_WIDTH_PX = 1280
SLIDE_HEIGHT_PX = 720

# Hard Rule §9: 1pt = 1.3333px(96dpi) — 이 스크립트가 되돌려주는 pt 값도 동일 기준.
PX_PER_PT = 1.3333

FONT_AUDIT_JS = """
() => {
  const slide = document.querySelector('.slide.is-active');
  if (!slide) return [];
  const results = [];
  const all = slide.querySelectorAll('*');
  for (const node of all) {
    let hasDirectText = false;
    for (const child of node.childNodes) {
      if (child.nodeType === 3 && child.textContent.trim().length > 0) {
        hasDirectText = true;
        break;
      }
    }
    if (!hasDirectText) continue;
    const cs = window.getComputedStyle(node);
    const fontSizePx = parseFloat(cs.fontSize);
    if (!fontSizePx) continue;
    const cls = (typeof node.className === 'string') ? node.className : '';
    results.push({
      tag: node.tagName.toLowerCase(),
      class: cls,
      text: node.textContent.trim().slice(0, 60),
      font_weight: cs.fontWeight,
      font_size_px: Math.round(fontSizePx * 100) / 100,
    });
  }
  return results;
}
"""

# 겹침(overlap)/캔버스 이탈(overflow)/텍스트 잘림(clipping)을 좌표·computed style만으로
# 기계적으로 판정한다. 응집도·시각적 균형·이미지-캡션 의미 일치 등 정성적 항목은
# 여기서 판정하지 않는다(여전히 스크린샷 육안 검토가 필요) — SKILL.md "2. Visual
# Quality Check" 참조.
LAYOUT_AUDIT_JS = """
({ width, height }) => {
  const slide = document.querySelector('.slide.is-active');
  if (!slide) return { overflow: [], clipped: [], overlaps: [] };
  const EPS = 1; // px 오차 허용
  const OVERLAP_RATIO_THRESHOLD = 0.3; // 두 텍스트 요소 중 작은 쪽 면적의 30% 이상 겹치면 flag

  const all = Array.from(slide.querySelectorAll('*'));
  const classOf = (el) => el.getAttribute('class') || '';

  // 1) 캔버스(슬라이드 영역) 밖으로 나간 요소
  const overflow = [];
  for (const el of all) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if (r.left < -EPS || r.top < -EPS || r.right > width + EPS || r.bottom > height + EPS) {
      overflow.push({
        tag: el.tagName.toLowerCase(),
        class: classOf(el),
        rect: { left: Math.round(r.left), top: Math.round(r.top), right: Math.round(r.right), bottom: Math.round(r.bottom) },
      });
    }
  }

  // 2) overflow:hidden 등으로 실제 내용이 잘린 요소(스크롤 크기 > 표시 크기)
  const clipped = [];
  for (const el of all) {
    const cs = window.getComputedStyle(el);
    const hides = cs.overflow === 'hidden' || cs.overflowY === 'hidden' || cs.overflowX === 'hidden';
    if (!hides) continue;
    if (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2) {
      clipped.push({ tag: el.tagName.toLowerCase(), class: classOf(el), text: el.textContent.trim().slice(0, 60) });
    }
  }

  // 3) 직접 텍스트를 가진 leaf 요소끼리의 의도치 않은 겹침
  const leaves = [];
  for (const el of all) {
    let hasDirectText = false;
    for (const child of el.childNodes) {
      if (child.nodeType === 3 && child.textContent.trim().length > 0) { hasDirectText = true; break; }
    }
    if (hasDirectText) leaves.push(el);
  }

  // 3b) img/svg 그래픽 요소 — text-leaf 판정(직접 텍스트 자식 유무)만으로는 img처럼
  //     텍스트 자식이 없는 요소가 통째로 검사 대상에서 빠진다(예: Step Box 텍스트와
  //     실제로 겹친 <img> 사진이 지금까지 감지되지 않던 원인). 아래 두 종류를
  //     "그래픽 요소"로 추가하되, 의도된 배경/장식 요소는 false positive를 피하기
  //     위해 제외한다.
  //     - img: 슬라이드 면적의 85% 이상을 덮는 경우(표지 풀블리드 배경 이미지 등)
  //       텍스트를 덮는 것이 설계 의도이므로 제외한다.
  //     - svg: 채워진 도형(fill) 없이 line/path/polyline(fill:none)만으로 구성된
  //       경우 Connector·화살표 등 장식용 선으로 간주해 제외한다 — 이런 svg는
  //       실제 잉크는 얇은 선뿐인데 bounding box는 컨테이너 전체를 덮게 배치되는
  //       경우가 흔해(예: 전체 영역을 덮는 Flow Connector 오버레이), 그대로 겹침
  //       판정에 쓰면 그 안의 모든 텍스트 요소와 false positive를 일으킨다.
  const slideArea = width * height;
  const isBackgroundImage = (el) => {
    const r = el.getBoundingClientRect();
    return slideArea > 0 && (r.width * r.height) / slideArea >= 0.85;
  };
  const isDecorativeSvg = (el) => {
    const shapes = el.querySelectorAll('*');
    if (shapes.length === 0) return false;
    for (const s of shapes) {
      const tag = s.tagName.toLowerCase();
      if (tag !== 'line' && tag !== 'path' && tag !== 'polyline') return false;
      const fill = window.getComputedStyle(s).fill;
      if (fill && fill !== 'none' && fill !== 'transparent') return false;
    }
    return true;
  };
  const graphics = [];
  for (const el of all) {
    const tag = el.tagName.toLowerCase();
    if (tag === 'img') {
      if (isBackgroundImage(el)) continue;
      graphics.push(el);
    } else if (tag === 'svg') {
      if (isDecorativeSvg(el)) continue;
      graphics.push(el);
    }
  }

  // 같은 부모 아래 두 요소가 모두 position:absolute/fixed로 겹쳐 쌓이도록 배치된
  // 경우(예: 겹친 Chevron 화살표 2장처럼 의도적으로 레이어링된 그래픽)는 우연한
  // 충돌이 아니라 설계된 합성이므로 겹침 판정에서 제외한다.
  const isIntentionalStack = (a, b) => {
    if (a.parentElement !== b.parentElement) return false;
    const posOf = (el) => window.getComputedStyle(el).position;
    const pa = posOf(a), pb = posOf(b);
    const isAbs = (p) => p === 'absolute' || p === 'fixed';
    return isAbs(pa) && isAbs(pb);
  };

  const describe = (el) => {
    const d = { tag: el.tagName.toLowerCase(), class: classOf(el), text: (el.textContent || '').trim().slice(0, 40) };
    if (d.tag === 'img') d.src = el.getAttribute('src') || '';
    return d;
  };
  const rectOverlapRatio = (ra, rb) => {
    const ix = Math.max(0, Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left));
    const iy = Math.max(0, Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top));
    const interArea = ix * iy;
    if (interArea <= 0) return 0;
    const minArea = Math.min(ra.width * ra.height, rb.width * rb.height);
    return minArea > 0 ? interArea / minArea : 0;
  };
  const overlaps = [];
  const pushOverlap = (a, b, ratio, pairType) => {
    overlaps.push({ a: describe(a), b: describe(b), overlap_ratio: Math.round(ratio * 100) / 100, pair_type: pairType });
  };

  // text × text (기존 로직 그대로 유지)
  for (let i = 0; i < leaves.length; i++) {
    for (let j = i + 1; j < leaves.length; j++) {
      const a = leaves[i], b = leaves[j];
      if (a.contains(b) || b.contains(a)) continue; // 조상-자손 관계는 겹침이 아님
      const ratio = rectOverlapRatio(a.getBoundingClientRect(), b.getBoundingClientRect());
      if (ratio > OVERLAP_RATIO_THRESHOLD) pushOverlap(a, b, ratio, 'text-text');
    }
  }

  // text × image, text × svg(비장식 그래픽)
  for (const t of leaves) {
    for (const g of graphics) {
      if (t.contains(g) || g.contains(t)) continue;
      if (isIntentionalStack(t, g)) continue;
      const ratio = rectOverlapRatio(t.getBoundingClientRect(), g.getBoundingClientRect());
      if (ratio > OVERLAP_RATIO_THRESHOLD) pushOverlap(t, g, ratio, `text-${g.tagName.toLowerCase()}`);
    }
  }

  // image × image (그래픽 요소끼리, img-svg/svg-svg 조합 포함)
  for (let i = 0; i < graphics.length; i++) {
    for (let j = i + 1; j < graphics.length; j++) {
      const a = graphics[i], b = graphics[j];
      if (a.contains(b) || b.contains(a)) continue;
      if (isIntentionalStack(a, b)) continue;
      const ratio = rectOverlapRatio(a.getBoundingClientRect(), b.getBoundingClientRect());
      if (ratio > OVERLAP_RATIO_THRESHOLD) pushOverlap(a, b, ratio, `${a.tagName.toLowerCase()}-${b.tagName.toLowerCase()}`);
    }
  }

  return { overflow, clipped, overlaps };
}
"""


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except Exception as e:
        raise SystemExit(
            "Playwright가 필요합니다.\n"
            "  pip install playwright\n"
            "  playwright install chromium\n"
            f"원인: {e}"
        )


def render(
    web_ppt_dir: Path,
    out_dir: Path,
    slide_indices: list[int] | None,
    audit_fonts: bool = False,
    audit_layout: bool = False,
) -> tuple[list[Path], dict[str, list[dict]], dict[str, dict]]:
    index_path = (web_ppt_dir / "index.html").resolve()
    if not index_path.exists():
        raise SystemExit(f"index.html을 찾을 수 없습니다: {index_path}")

    sync_playwright = ensure_playwright()
    out_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []
    font_audit: dict[str, list[dict]] = {}
    layout_audit: dict[str, dict] = {}

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception as e:
            raise SystemExit(
                "Chromium을 실행하지 못했습니다. 다음 명령을 먼저 실행하세요:\n"
                "  playwright install chromium\n"
                f"원인: {e}"
            )

        page = browser.new_page(
            viewport={"width": SLIDE_WIDTH_PX, "height": SLIDE_HEIGHT_PX},
            device_scale_factor=2,
        )
        page.goto(index_path.as_uri(), wait_until="load")
        page.evaluate("() => document.fonts.ready")

        total = page.evaluate("() => document.querySelectorAll('.slide').length")
        if total == 0:
            raise SystemExit("`.slide` 요소를 찾지 못했습니다 — index.html 구조를 확인하세요.")

        targets = slide_indices if slide_indices else list(range(1, total + 1))

        # 이 웹PPT는 SPA 방식으로 `.slide.is-active` 한 장만 화면에 보인다.
        # index.html 자체의 탐색 스크립트와 동일한 방식(is-active 토글)으로
        # 슬라이드를 하나씩 활성화해, 실제 브라우저에서 보는 화면 그대로 캡처한다.
        for idx in targets:
            found = page.evaluate(
                """(i) => {
                  const slides = Array.from(document.querySelectorAll('.slide'));
                  slides.forEach(s => s.classList.remove('is-active'));
                  const target = slides.find(s => s.dataset.index === String(i)) || slides[i - 1];
                  if (!target) return false;
                  target.classList.add('is-active');
                  return true;
                }""",
                idx,
            )
            if not found:
                print(f"[qa_render] slide {idx}: 찾지 못해 건너뜀")
                continue
            page.wait_for_timeout(150)  # Chart.js 등 마지막 프레임 렌더링 대기

            out_path = out_dir / f"slide-{idx:02d}.png"
            page.locator(".slide.is-active").screenshot(path=str(out_path))
            saved.append(out_path)
            print(f"[qa_render] slide {idx} -> {out_path}")

            if audit_fonts:
                raw = page.evaluate(FONT_AUDIT_JS)
                for item in raw:
                    # device_scale_factor=2로 스크린샷을 찍지만 getComputedStyle은
                    # CSS px(스케일 무관) 기준이므로 별도 보정 없이 그대로 pt 환산한다.
                    item["font_size_pt"] = round(item["font_size_px"] / PX_PER_PT, 2)
                font_audit[f"slide_{idx}"] = raw

            if audit_layout:
                result = page.evaluate(LAYOUT_AUDIT_JS, {"width": SLIDE_WIDTH_PX, "height": SLIDE_HEIGHT_PX})
                flagged = bool(result["overflow"] or result["clipped"] or result["overlaps"])
                result["flagged"] = flagged
                layout_audit[f"slide_{idx}"] = result
                if flagged:
                    print(
                        f"[qa_render] slide {idx}: LAYOUT AUDIT FLAGGED "
                        f"(overflow={len(result['overflow'])}, clipped={len(result['clipped'])}, "
                        f"overlaps={len(result['overlaps'])})"
                    )
                else:
                    print(f"[qa_render] slide {idx}: layout audit clean")

        browser.close()

    if audit_fonts:
        audit_path = out_dir / "font-audit.json"
        audit_path.write_text(
            json.dumps(font_audit, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"[qa_render] font-audit -> {audit_path}")

    if audit_layout:
        layout_audit_path = out_dir / "layout-audit.json"
        layout_audit_path.write_text(
            json.dumps(layout_audit, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        flagged_slides = [k for k, v in layout_audit.items() if v["flagged"]]
        print(f"[qa_render] layout-audit -> {layout_audit_path} (flagged: {flagged_slides or 'none'})")

    return saved, font_audit, layout_audit


def main() -> None:
    parser = argparse.ArgumentParser(description="생성 후 QA용 슬라이드 스크린샷 렌더링 + Typography 감사")
    parser.add_argument("--web-ppt", required=True, help="web_ppt/vN 폴더 경로")
    parser.add_argument("--out", required=True, help="스크린샷/감사 결과 저장 폴더 (예: /output/{project}/.qa/vN)")
    parser.add_argument("--slides", help="쉼표로 구분된 슬라이드 번호(예: 4,7,10,13). 생략 시 전체 슬라이드")
    parser.add_argument(
        "--audit-fonts",
        action="store_true",
        help="각 텍스트 요소의 실제 computed font-size(pt 환산 포함)를 <out>/font-audit.json으로 함께 저장",
    )
    parser.add_argument(
        "--audit-layout",
        action="store_true",
        help="겹침/캔버스 이탈(overflow)/텍스트 잘림을 좌표·computed style로 감사해 <out>/layout-audit.json으로 저장 "
        "(응집도·시각적 균형 등 정성적 판단은 대체하지 않음 — 어떤 슬라이드를 육안으로 봐야 하는지 미리 걸러내는 용도)",
    )
    args = parser.parse_args()

    slide_indices = None
    if args.slides:
        slide_indices = [int(x.strip()) for x in args.slides.split(",") if x.strip()]

    saved, _, _ = render(
        Path(args.web_ppt),
        Path(args.out),
        slide_indices,
        audit_fonts=args.audit_fonts,
        audit_layout=args.audit_layout,
    )
    if not saved:
        raise SystemExit("생성된 스크린샷이 없습니다.")
    print(f"[qa_render] 완료: {len(saved)}개 슬라이드")


if __name__ == "__main__":
    main()
