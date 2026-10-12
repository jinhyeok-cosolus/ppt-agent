"""
web-ppt-generator / qa_render.py

생성 후 QA(Post-Generation QA)용 스크린샷 렌더러 + Typography/Layout 감사 도구.
web_ppt/v{N}/index.html을 Playwright/Chromium으로 실제 렌더링해, 지정한 슬라이드
(또는 전체 슬라이드)를 브라우저가 보여주는 그대로 PNG로 캡처한다. `--audit-fonts`를
같이 주면 각 텍스트 요소의 **실제 computed font-size**(코드의 선언값이 아니라
브라우저가 최종 계산한 값)를 pt 단위로 함께 추출한다. `--audit-layout`을 같이 주면
겹침(overlap)/캔버스 이탈(overflow)/텍스트 잘림(clipping)/Page Number 위치(Hard
Rule §9)/Bottom Safe Area 침범, 이미지 원본 비율 유지(늘림·콘텐츠 잘림)와 같은
data-visual-group 안의 배치 방향별 정렬(가로=높이, 세로=너비)처럼 좌표·CSS 값만으로
기계적으로 판정 가능한 항목을 함께 감사해 `layout-audit.json`으로 저장한다 — 이 결과는 어떤 슬라이드를 LLM이
스크린샷으로 직접 봐야 하는지 미리 걸러내기 위한 것이며, 응집도·시각적 균형·가독성
등 정성적 판단을 대체하지 않는다.

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
  //       <defs>/<marker> 안의 도형(화살촉 등)은 그 자체로 그려지지 않고 선 끝에만
  //       붙으므로 판정에서 제외한다 — 채워진 화살촉 marker 때문에 Connector 오버레이가
  //       장식용으로 분류되지 않아 내부 모든 요소와 겹침 오탐이 나던 원인. Connector와
  //       이미지·라벨·박스의 실제 충돌은 아래 7) Flow 기하 감사가 선분 단위로 검사한다.
  const isDecorativeSvg = (el) => {
    const shapes = Array.from(el.querySelectorAll('*')).filter(s => !s.closest('defs, marker'));
    if (shapes.length === 0) return false;
    for (const s of shapes) {
      const tag = s.tagName.toLowerCase();
      if (tag !== 'line' && tag !== 'path' && tag !== 'polyline') return false;
      const fill = window.getComputedStyle(s).fill;
      if (fill && fill !== 'none' && fill !== 'transparent') return false;
    }
    return true;
  };
  // data-visual-frame="panel": Layout이 명시한 Full-Bleed 사진 패널(예: 기업개요 우측 사진).
  // 공통 Header(Sub Message·구분선)가 의도적으로 위에 겹치고 슬라이드 끝까지 닿으므로
  // 겹침·Bottom Safe Area 판정에서 제외한다(비율·Crop은 아래 6)에서 참고 기록으로 검사).
  const isPanel = (el) => el.getAttribute && el.getAttribute('data-visual-frame') === 'panel';
  const graphics = [];
  for (const el of all) {
    const tag = el.tagName.toLowerCase();
    if (tag === 'img') {
      if (isBackgroundImage(el) || isPanel(el)) continue;
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

  // 4) 공통 Header System·좌측 Brand Line·페이지 번호·Deck Footnote·Bottom Safe Area
  //    (Hard Rule §9) — Single Source of Truth는 Hard Rule 문서와 templates/style.css이며,
  //    아래 상수는 그 값을 기계적으로 대조하기 위해 옮겨온 것이다(값이 바뀌면 함께 바꾼다).
  //    슬라이드 유형(class)별 적용 범위: 일반 본문은 전부 적용, 기업개요(slide--company-overview)는
  //    페이지 번호 미표시 + Sub Message White·구분선 #96A4A5, 표지·Closing은 공통 요소 미적용.
  const slideType = slide.classList.contains('slide--cover') ? 'cover'
    : slide.classList.contains('slide--closing') ? 'closing'
    : slide.classList.contains('slide--company-overview') ? 'company-overview' : 'body';
  const usesCommonHeader = slideType === 'body' || slideType === 'company-overview';
  const PAGE_NUMBER_SELECTOR = '.deck-page';
  const PAGE_NUMBER_RIGHT_EDGE_X = width - 32;   // Hard Rule §9: X=1248px(=1280-32)
  const PAGE_NUMBER_BOTTOM_EDGE_Y = height - 16; // Hard Rule §9: Y=704px(=720-16)
  const DECK_FOOTNOTE_SELECTOR = '.deck-footnote';
  const DECK_FOOTNOTE_LEFT_X = 64;               // Hard Rule §9: X=64px
  const DECK_FOOTNOTE_RIGHT_MAX_X = width - 128; // Hard Rule §9: 우측 경계 X=1152px(=1280-128)
  const DECK_FOOTNOTE_BOTTOM_EDGE_Y = height - 28; // Hard Rule §9: Y=692px(Footnote 영역 유지)
  const BOTTOM_SAFE_AREA_Y = 678;                // Hard Rule §9: Content 하단 경계
  const POS_EPS = 2; // px 허용 오차(안티에일리어싱/서브픽셀 반올림 대응)
  // Hard Rule §9 공통 Header 실측값(기업개요 Reference.pptx) — 요소 박스 기준
  const HEADER_SPEC = [
    { sel: '.header-ci', left: 46.5, top: 31.0, height: 17.5 },
    { sel: '.header-section-label', left: 46.9, top: 64.7 },
    { sel: '.header-main-title', left: 41.6, top: 83.2 },
    { sel: '.header-submessage', right: 1262.2, top: 28.5 },
    { sel: '.header-divider', left: 41.6, top: 57.6, right: width },
    { sel: '.deck-left-line', left: 0, top: 0, width: 13.9, height: height },
  ];
  const HEADER_COLORS = {
    body: { submessage: 'rgb(71, 134, 137)', divider: 'rgb(71, 134, 137)' },               // #478689
    'company-overview': { submessage: 'rgb(255, 255, 255)', divider: 'rgb(150, 164, 165)' }, // White / #96A4A5
  };
  const visible = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };

  const pageNumberIssues = [];
  const deckFootnoteIssues = [];
  const bottomSafeAreaViolations = [];
  const commonElementIssues = [];
  const pageNumberEl = slide.querySelector(PAGE_NUMBER_SELECTOR);
  const deckFootnoteEl = slide.querySelector(DECK_FOOTNOTE_SELECTOR);

  // 4-1) 혼용된 페이지 번호 클래스 — `.deck-page` 하나로 통일
  for (const el of slide.querySelectorAll('.page-number, .header-page-number')) {
    pageNumberIssues.push({ type: 'page-number-class-nonstandard', class: classOf(el), expected: 'deck-page' });
  }

  // 4-2) 페이지 번호 — 일반 본문만 표시·위치 검사, 그 외 유형은 표시되면 오류
  if (slideType === 'body') {
    if (!pageNumberEl || !visible(pageNumberEl)) {
      pageNumberIssues.push({ type: 'page-number-missing', expected: PAGE_NUMBER_SELECTOR });
    } else {
      const pr = pageNumberEl.getBoundingClientRect();
      if (Math.abs(pr.right - PAGE_NUMBER_RIGHT_EDGE_X) > POS_EPS) {
        pageNumberIssues.push({ type: 'x', expected: PAGE_NUMBER_RIGHT_EDGE_X, actual: Math.round(pr.right) });
      }
      if (Math.abs(pr.bottom - PAGE_NUMBER_BOTTOM_EDGE_Y) > POS_EPS) {
        pageNumberIssues.push({ type: 'y', expected: PAGE_NUMBER_BOTTOM_EDGE_Y, actual: Math.round(pr.bottom) });
      }
      if (pr.top < BOTTOM_SAFE_AREA_Y - POS_EPS) {
        pageNumberIssues.push({ type: 'page-number-invades-safe-area', boundary: BOTTOM_SAFE_AREA_Y, actual: Math.round(pr.top) });
      }
    }
  } else if (pageNumberEl && visible(pageNumberEl)) {
    pageNumberIssues.push({ type: 'page-number-not-allowed', slide_type: slideType });
  }

  // 4-3) 공통 Header·좌측 Brand Line — 적용 유형은 존재·위치·색, 미적용 유형은 표시되면 오류
  for (const spec of HEADER_SPEC) {
    const el = slide.querySelector(spec.sel);
    const shown = el && visible(el);
    if (!usesCommonHeader) {
      if (shown) commonElementIssues.push({ type: 'common-element-not-allowed', element: spec.sel, slide_type: slideType });
      continue;
    }
    if (!el || window.getComputedStyle(el).display === 'none') { commonElementIssues.push({ type: 'common-element-missing', element: spec.sel }); continue; }
    const r = el.getBoundingClientRect();
    const off = {};
    for (const k of ['left', 'top', 'right', 'width', 'height']) {
      if (spec[k] === undefined) continue;
      if (Math.abs(r[k] - spec[k]) > POS_EPS) off[k] = { expected: spec[k], actual: Math.round(r[k] * 10) / 10 };
    }
    if (Object.keys(off).length) commonElementIssues.push({ type: 'common-element-position', element: spec.sel, mismatch: off });
  }
  if (usesCommonHeader) {
    const want = HEADER_COLORS[slideType];
    const sub = slide.querySelector('.header-submessage');
    const div = slide.querySelector('.header-divider');
    if (sub && window.getComputedStyle(sub).color !== want.submessage) {
      commonElementIssues.push({ type: 'common-element-color', element: '.header-submessage', expected: want.submessage, actual: window.getComputedStyle(sub).color });
    }
    // 구분선 색은 화면 표시선(::after, 정확한 선 두께 요소) 기준 — 테두리는 변환용으로 투명하다
    const divColor = div ? window.getComputedStyle(div, '::after').backgroundColor : null;
    if (div && divColor !== want.divider) {
      commonElementIssues.push({ type: 'common-element-color', element: '.header-divider', expected: want.divider, actual: divColor });
    }
  }

  // 4-4) Deck Footnote(조건부) — 있을 때만 허용 영역 검사
  if (deckFootnoteEl && visible(deckFootnoteEl)) {
    const fr = deckFootnoteEl.getBoundingClientRect();
    if (Math.abs(fr.left - DECK_FOOTNOTE_LEFT_X) > POS_EPS) {
      deckFootnoteIssues.push({ type: 'x', expected: DECK_FOOTNOTE_LEFT_X, actual: Math.round(fr.left) });
    }
    if (fr.right > DECK_FOOTNOTE_RIGHT_MAX_X + POS_EPS) {
      deckFootnoteIssues.push({ type: 'invades-page-number-zone', boundary: DECK_FOOTNOTE_RIGHT_MAX_X, actual: Math.round(fr.right) });
    }
    if (Math.abs(fr.bottom - DECK_FOOTNOTE_BOTTOM_EDGE_Y) > POS_EPS) {
      deckFootnoteIssues.push({ type: 'y', expected: DECK_FOOTNOTE_BOTTOM_EDGE_Y, actual: Math.round(fr.bottom) });
    }
    if (fr.top < BOTTOM_SAFE_AREA_Y - POS_EPS) {
      deckFootnoteIssues.push({ type: 'deck-footnote-invades-safe-area', boundary: BOTTOM_SAFE_AREA_Y, actual: Math.round(fr.top) });
    }
  }

  // 4-5) Bottom Safe Area — 공통 Header 적용 유형(일반 본문·기업개요) 전체에 적용.
  //      페이지 번호·Deck Footnote·좌측 Brand Line·Full-Bleed 사진 패널은 고정 영역이라 제외한다.
  if (usesCommonHeader) {
    for (const el of [...leaves, ...graphics]) {
      if (pageNumberEl && (el === pageNumberEl || pageNumberEl.contains(el) || el.contains(pageNumberEl))) continue;
      if (deckFootnoteEl && (el === deckFootnoteEl || deckFootnoteEl.contains(el) || el.contains(deckFootnoteEl))) continue;
      if (el.closest('.deck-left-line') || isPanel(el)) continue;
      const r = el.getBoundingClientRect();
      if (r.height === 0) continue;
      if (r.bottom > BOTTOM_SAFE_AREA_Y + POS_EPS) {
        bottomSafeAreaViolations.push({
          tag: el.tagName.toLowerCase(), class: classOf(el),
          text: (el.textContent || '').trim().slice(0, 40),
          bottom: Math.round(r.bottom), boundary: BOTTOM_SAFE_AREA_Y,
        });
      }
    }
  }

  // 6) 이미지 표시 크기·비율 감사 (SKILL.md "이미지 표시 크기·시각적 위계" 참조)
  //    - 원본 비율 유지: object-fit을 반영해 브라우저가 실제로 그린 이미지 영역을 계산하고,
  //      늘림(fill 왜곡)·콘텐츠 이미지의 잘림(cover/none)을 issue로 기록한다.
  //      data-visual-role="decorative" 또는 슬라이드 면적 85% 이상(풀블리드 배경)은 잘림 검사에서 제외한다.
  //    - 배치 방향별 정렬: 같은 data-visual-group 안에서 가로로 나란한 이미지는 높이를,
  //      세로로 이어진 이미지는 너비를 비교한다(그룹 표기가 없는 이미지는 추정해서 묶지 않는다).
  //    - 역할(Main/Supporting) 간 크기 순서는 판정하지 않는다 — 판독성·정보 밀도에 따라
  //      Supporting이 더 클 수 있으므로 기계적으로 오류 처리하지 않는다.
  const ASPECT_EPS = 0.02;      // 박스 비율과 원본 비율 차이 2% 초과 시 왜곡
  const CROP_EPS = 0.02;        // 콘텐츠 이미지가 2% 넘게 잘리면 잘림
  const LETTERBOX_RATIO = 0.15; // contain 박스 중 15% 이상이 빈 여백이면 참고 기록
  const ALIGN_TOLERANCE = 0.10; // 같은 그룹 정렬 축 크기 차이 10% 초과 시 불일치
  const imageIssues = [];
  const imageAdvisories = [];
  const imgInfos = [];
  const posOffset = (token, free) => {
    const t = (token || '').trim().toLowerCase();
    const kw = { left: 0, top: 0, center: 50, right: 100, bottom: 100 };
    if (t in kw) return free * kw[t] / 100;
    if (t.endsWith('%')) return free * parseFloat(t) / 100;
    if (t.endsWith('px')) return parseFloat(t);
    return free / 2;
  };
  for (const el of slide.querySelectorAll('img')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0 || !el.naturalWidth || !el.naturalHeight) continue;
    const cs = window.getComputedStyle(el);
    const fit = cs.objectFit || 'fill';
    const nw = el.naturalWidth, nh = el.naturalHeight;
    const natAr = nw / nh, boxAr = r.width / r.height;
    const role = el.dataset.visualRole || '';
    const decorative = role === 'decorative' || isBackgroundImage(el);
    const src = (el.getAttribute('src') || '').split('/').pop();
    let scale = null;
    if (fit === 'contain') scale = Math.min(r.width / nw, r.height / nh);
    else if (fit === 'cover') scale = Math.max(r.width / nw, r.height / nh);
    else if (fit === 'none') scale = 1;
    else if (fit === 'scale-down') scale = Math.min(1, r.width / nw, r.height / nh);
    let content = { left: r.left, top: r.top, width: r.width, height: r.height };
    let visibleFraction = 1;
    if (scale !== null) {
      const cw = nw * scale, ch = nh * scale;
      const pos = (cs.objectPosition || '50% 50%').split(' ');
      const cx = posOffset(pos[0], r.width - cw), cy = posOffset(pos[1] || '50%', r.height - ch);
      const vx0 = Math.max(cx, 0), vy0 = Math.max(cy, 0);
      const vx1 = Math.min(cx + cw, r.width), vy1 = Math.min(cy + ch, r.height);
      content = { left: r.left + vx0, top: r.top + vy0, width: Math.max(vx1 - vx0, 0), height: Math.max(vy1 - vy0, 0) };
      visibleFraction = (content.width * content.height) / (cw * ch);
      const emptyRatio = 1 - (content.width * content.height) / (r.width * r.height);
      if (emptyRatio >= LETTERBOX_RATIO) {
        imageAdvisories.push({ type: 'letterboxed', src, class: classOf(el), empty_ratio: Math.round(emptyRatio * 100) / 100,
          note: '박스가 이미지보다 커서 빈 여백이 생김 — 동일 크기 박스 강제 여부 확인' });
      }
    } else if (Math.abs(boxAr / natAr - 1) > ASPECT_EPS) {
      imageIssues.push({ type: 'aspect-distorted', src, class: classOf(el),
        box_ratio: Math.round(boxAr * 1000) / 1000, natural_ratio: Math.round(natAr * 1000) / 1000 });
    }
    // 원형 프레임(Claude PPT Design System §6 "Ellipse/Arc — 원형 프레임(인물 사진 등)")은
    // 의도된 프레이밍 Crop이므로 issue가 아니라 참고 기록으로만 남긴다.
    const isCircular = (node) => {
      if (!node) return false;
      const br = window.getComputedStyle(node).borderRadius || '';
      const nr = node.getBoundingClientRect();
      if (br.includes('%')) return parseFloat(br) >= 40;
      const v = parseFloat(br);
      return v > 0 && v >= 0.42 * Math.min(nr.width, nr.height) && Math.abs(nr.width - nr.height) <= 0.15 * Math.max(nr.width, nr.height);
    };
    if (!decorative && visibleFraction < 1 - CROP_EPS) {
      if (isPanel(el)) {
        imageAdvisories.push({ type: 'panel-frame-crop', src, class: classOf(el),
          visible_ratio: Math.round(visibleFraction * 100) / 100, note: 'Layout이 정한 Full-Bleed 사진 패널의 의도된 Crop — 핵심 피사체가 잘리지 않았는지 육안 확인' });
      } else if (isCircular(el) || isCircular(el.parentElement)) {
        imageAdvisories.push({ type: 'circular-frame-crop', src, class: classOf(el),
          visible_ratio: Math.round(visibleFraction * 100) / 100, note: '원형 프레임 — 인물 등 핵심 대상이 잘리지 않았는지 육안 확인' });
      } else {
        imageIssues.push({ type: 'content-cropped', src, class: classOf(el), object_fit: fit,
          visible_ratio: Math.round(visibleFraction * 100) / 100 });
      }
    }
    imgInfos.push({ el, src, role, group: el.dataset.visualGroup || '', content });
  }
  const groups = {};
  for (const info of imgInfos) {
    if (!info.group) continue;
    (groups[info.group] = groups[info.group] || []).push(info);
  }
  for (const [group, items] of Object.entries(groups)) {
    for (let i = 0; i < items.length; i++) {
      for (let j = i + 1; j < items.length; j++) {
        const a = items[i].content, b = items[j].content;
        const vOverlap = Math.min(a.top + a.height, b.top + b.height) - Math.max(a.top, b.top);
        const hOverlap = Math.min(a.left + a.width, b.left + b.width) - Math.max(a.left, b.left);
        let axis = null, va = 0, vb = 0;
        if (vOverlap > 0.5 * Math.min(a.height, b.height)) { axis = 'height'; va = a.height; vb = b.height; }
        else if (hOverlap > 0.5 * Math.min(a.width, b.width)) { axis = 'width'; va = a.width; vb = b.width; }
        if (!axis) continue;
        const diff = Math.abs(va - vb) / Math.max(va, vb);
        if (diff > ALIGN_TOLERANCE) {
          imageIssues.push({ type: axis === 'height' ? 'row-height-mismatch' : 'column-width-mismatch', group,
            images: [items[i].src, items[j].src], values: [Math.round(va), Math.round(vb)], diff: Math.round(diff * 100) / 100 });
        }
      }
    }
  }
  const imageSizes = imgInfos.map(i => ({ src: i.src, role: i.role || null, group: i.group || null,
    rendered: { w: Math.round(i.content.width), h: Math.round(i.content.height) } }));

  // 7) Flow Diagram 기하 감사 (flow-diagram-rules.md "Visual Composition — Lane Band·연결점·구분선")
  //    `.flow-field`가 있는 슬라이드에서만 실행한다. SVG Connector를 선분 단위로 실제 화면
  //    좌표로 환산해 이미지(실제 그려진 영역)·라벨·카테고리 박스와의 충돌, 불필요한 꺾임,
  //    Process 소속 Lane과의 간격, 구분선·상단 콘텐츠와의 간격, Node 간 간격, 종료 단계
  //    공통 축을 검사한다. 기준값은 `.flow-field`의 CSS 변수(--flow-clearance,
  //    --flow-gap-process, --flow-node-gap, --flow-axis-tolerance)를 읽어 쓰므로 슬라이드의
  //    가용 공간에 맞춰 조정한 값이 그대로 반영된다(변수가 없으면 아래 초기 기준값).
  const flowIssues = [];
  const flowAdvisories = [];
  const R = (v) => Math.round(v);
  const rectGap = (a, b) => Math.hypot(
    Math.max(0, Math.max(a.left, b.left) - Math.min(a.right, b.right)),
    Math.max(0, Math.max(a.top, b.top) - Math.min(a.bottom, b.bottom)));
  const xOverlap = (a, b) => Math.min(a.right, b.right) - Math.max(a.left, b.left);
  const unionRect = (rs) => rs.length ? {
    left: Math.min(...rs.map(r => r.left)), top: Math.min(...rs.map(r => r.top)),
    right: Math.max(...rs.map(r => r.right)), bottom: Math.max(...rs.map(r => r.bottom)) } : null;
  const nameOf = (el) => ((el.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 30))
    || (el.getAttribute && (el.getAttribute('alt') || (el.getAttribute('src') || '').split('/').pop())) || classOf(el);
  const alphaCache = new Map();
  const alphaBox = (el) => {
    const key = el.currentSrc || el.src;
    if (alphaCache.has(key)) return alphaCache.get(key);
    let res = null;
    try {
      const k = Math.min(1, 256 / Math.max(el.naturalWidth, el.naturalHeight));
      const w = Math.max(1, Math.round(el.naturalWidth * k)), h = Math.max(1, Math.round(el.naturalHeight * k));
      const cv = document.createElement('canvas'); cv.width = w; cv.height = h;
      const ctx = cv.getContext('2d'); ctx.drawImage(el, 0, 0, w, h);
      const d = ctx.getImageData(0, 0, w, h).data;
      let x0 = w, y0 = h, x1 = -1, y1 = -1;
      for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
        if (d[(y * w + x) * 4 + 3] > 16) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
      }
      if (x1 >= x0) res = { l: x0 / w, t: y0 / h, r: (x1 + 1) / w, b: (y1 + 1) / h };
    } catch (e) { res = null; } // 캔버스 접근 불가 시 박스 기준으로 대체
    alphaCache.set(key, res);
    return res;
  };
  const imgContentRect = (el) => {
    const r = el.getBoundingClientRect();
    const cs = window.getComputedStyle(el);
    const nw = el.naturalWidth, nh = el.naturalHeight, fit = cs.objectFit || 'fill';
    let scale = null;
    if (nw && nh) {
      if (fit === 'contain') scale = Math.min(r.width / nw, r.height / nh);
      else if (fit === 'cover') scale = Math.max(r.width / nw, r.height / nh);
      else if (fit === 'none') scale = 1;
      else if (fit === 'scale-down') scale = Math.min(1, r.width / nw, r.height / nh);
    }
    let box;
    if (scale === null) box = { left: r.left, top: r.top, width: r.width, height: r.height };
    else {
      const cw = nw * scale, ch = nh * scale;
      const pos = (cs.objectPosition || '50% 50%').split(' ');
      box = { left: r.left + posOffset(pos[0], r.width - cw), top: r.top + posOffset(pos[1] || '50%', r.height - ch), width: cw, height: ch };
    }
    // 투명 여백(PNG alpha)을 제외한 실제로 보이는 영역 — 간격·연결점·충돌은 눈에 보이는 픽셀 기준이다.
    const a = alphaBox(el) || { l: 0, t: 0, r: 1, b: 1 };
    return { left: Math.max(box.left + box.width * a.l, r.left), top: Math.max(box.top + box.height * a.t, r.top),
             right: Math.min(box.left + box.width * a.r, r.right), bottom: Math.min(box.top + box.height * a.b, r.bottom) };
  };
  // path d(M/L/H/V, 절대·상대)·line·polyline만 해석한다 — L25 실측 Connector는 전부 직선이다.
  const parsePoints = (s) => {
    const tag = s.tagName.toLowerCase();
    const num = (n) => parseFloat(s.getAttribute(n) || '0');
    if (tag === 'line') return [[num('x1'), num('y1')], [num('x2'), num('y2')]];
    if (tag === 'polyline') {
      const v = (s.getAttribute('points') || '').trim().split(/[\\s,]+/).map(parseFloat);
      const pts = []; for (let i = 0; i + 1 < v.length; i += 2) pts.push([v[i], v[i + 1]]); return pts;
    }
    const toks = (s.getAttribute('d') || '').match(/[a-zA-Z]|-?\\d*\\.?\\d+(?:e[-+]?\\d+)?/g) || [];
    const pts = []; let cmd = null, x = 0, y = 0, sx = 0, sy = 0, i = 0;
    while (i < toks.length) {
      if (/[a-zA-Z]/.test(toks[i])) { cmd = toks[i++]; if (!/[MLHVZmlhvz]/.test(cmd)) return null; }
      if (cmd === 'Z' || cmd === 'z') { x = sx; y = sy; pts.push([x, y]); continue; }
      const rel = cmd === cmd.toLowerCase(), c = cmd.toUpperCase();
      const n = () => parseFloat(toks[i++]);
      if (c === 'M' || c === 'L') { const a = n(), b = n(); x = rel ? x + a : a; y = rel ? y + b : b; if (c === 'M') { sx = x; sy = y; cmd = rel ? 'l' : 'L'; } }
      else if (c === 'H') { const a = n(); x = rel ? x + a : a; }
      else if (c === 'V') { const b = n(); y = rel ? y + b : b; }
      if (isNaN(x) || isNaN(y)) return null;
      pts.push([x, y]);
    }
    return pts.length >= 2 ? pts : null;
  };
  // 선분과 사각형의 교차 구간(Liang-Barsky). 반환: [t0, t1] 또는 null
  const clipSeg = (a, b, r) => {
    let t0 = 0, t1 = 1; const dx = b.x - a.x, dy = b.y - a.y;
    const p = [-dx, dx, -dy, dy], q = [a.x - r.left, r.right - a.x, a.y - r.top, r.bottom - a.y];
    for (let k = 0; k < 4; k++) {
      if (Math.abs(p[k]) < 1e-9) { if (q[k] < 0) return null; continue; }
      const t = q[k] / p[k];
      if (p[k] < 0) { if (t > t1) return null; if (t > t0) t0 = t; }
      else { if (t < t0) return null; if (t < t1) t1 = t; }
    }
    return t1 > t0 ? [t0, t1] : null;
  };
  const cssPx = (el, name, fallback) => {
    const v = parseFloat(window.getComputedStyle(el).getPropertyValue(name));
    return isNaN(v) ? fallback : v;
  };

  for (const field of slide.querySelectorAll('.flow-field')) {
    const fr = field.getBoundingClientRect();
    const T = {
      clearance: cssPx(field, '--flow-clearance', 20),
      processGap: cssPx(field, '--flow-gap-process', 8),
      nodeGap: cssPx(field, '--flow-node-gap', 16),
      axisTol: cssPx(field, '--flow-axis-tolerance', 4),
    };
    const PEN = 4;    // Connector 끝점이 대상 경계에 닿거나 살짝 들어가는 정도(이미지 투명 여백·안티에일리어싱)는 정상 연결로 본다
    const LINE_HALF = 1; // stroke 두께 절반
    const NODE_SEL = '.flow-node, .flow-process, .flow-output-group, .flow-category-label';

    // 7-1) 콘텐츠 요소 수집: 이미지(object-fit 반영 실제 영역), 텍스트 라벨, 카테고리 박스
    const items = [];
    const ownerOf = (el) => el.closest(NODE_SEL) || el;
    for (const img of field.querySelectorAll('img')) {
      const r = img.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      items.push({ el: img, kind: 'image', owner: ownerOf(img), rect: imgContentRect(img) });
    }
    for (const el of field.querySelectorAll('*')) {
      if (el.closest('svg')) continue;
      if (el.classList.contains('flow-category-label')) {
        const r = el.getBoundingClientRect();
        items.push({ el, kind: 'box', owner: el, rect: { left: r.left, top: r.top, right: r.right, bottom: r.bottom } });
        continue;
      }
      if (el.closest('.flow-category-label')) continue;
      let direct = false;
      for (const c of el.childNodes) if (c.nodeType === 3 && c.textContent.trim()) { direct = true; break; }
      if (!direct) continue;
      const range = document.createRange();
      range.selectNodeContents(el);
      const tr = range.getBoundingClientRect();
      if (!tr.width || !tr.height) continue;
      items.push({ el, kind: 'text', owner: ownerOf(el), rect: { left: tr.left, top: tr.top, right: tr.right, bottom: tr.bottom } });
    }

    // 7-2) Connector 선분 수집
    const paths = [];
    for (const s of field.querySelectorAll('svg path, svg line, svg polyline')) {
      if (s.closest('defs, marker')) continue;
      const raw = parsePoints(s);
      if (!raw) { flowAdvisories.push({ type: 'connector-unparsed', class: classOf(s), note: '곡선 등 해석하지 않는 path — 충돌 여부 육안 확인' }); continue; }
      const m = s.getScreenCTM();
      if (!m) continue;
      const pts = raw.map(([x, y]) => { const p = new DOMPoint(x, y).matrixTransform(m); return { x: p.x, y: p.y }; });
      const me = s.getAttribute('marker-end') || window.getComputedStyle(s).markerEnd;
      paths.push({ el: s, index: paths.length, pts, arrow: !!me && me !== 'none' });
    }
    const segs = [];
    for (const p of paths) for (let i = 0; i + 1 < p.pts.length; i++) {
      const a = p.pts[i], b = p.pts[i + 1];
      if (Math.hypot(b.x - a.x, b.y - a.y) < 0.5) continue;
      const ori = Math.abs(a.y - b.y) < 0.5 ? 'h' : Math.abs(a.x - b.x) < 0.5 ? 'v' : 'd';
      segs.push({ path: p, a, b, ori, first: i === 0, last: i === p.pts.length - 2 });
    }
    const pathLabel = (p) => `path#${p.index}(${p.pts.map(q => `${R(q.x - fr.left)},${R(q.y - fr.top)}`).join(' ')})`;

    // 끝점 바로 앞(진행 방향)에 있는 대상 — 콘텐츠 요소 또는 다른 Connector(분기 브래킷)
    const findTarget = (p) => {
      const n = p.pts.length, end = p.pts[n - 1], prev = p.pts[n - 2];
      const dx = Math.sign(R(end.x - prev.x)), dy = Math.sign(R(end.y - prev.y));
      let best = null;
      for (const it of items) {
        const r = it.rect;
        const ahead = (dx > 0 && r.right > end.x) || (dx < 0 && r.left < end.x) || (dy > 0 && r.bottom > end.y) || (dy < 0 && r.top < end.y);
        if (!ahead) continue;
        const inLine = dx !== 0 ? (end.y >= r.top - 4 && end.y <= r.bottom + 4) : (end.x >= r.left - 4 && end.x <= r.right + 4);
        if (!inLine) continue;
        const g = rectGap({ left: end.x, right: end.x, top: end.y, bottom: end.y }, r);
        if (g <= 48 && (!best || g < best.gap)) best = { item: it, gap: g };
      }
      for (const s of segs) {
        if (s.path === p) continue;
        const r = { left: Math.min(s.a.x, s.b.x), right: Math.max(s.a.x, s.b.x), top: Math.min(s.a.y, s.b.y), bottom: Math.max(s.a.y, s.b.y) };
        const g = rectGap({ left: end.x, right: end.x, top: end.y, bottom: end.y }, r);
        if (g <= 12 && (!best || g < best.gap)) best = { connector: s, gap: g };
      }
      return best;
    };

    // 7-3) Connector × 이미지·라벨·카테고리 박스 충돌(끝점이 대상에 PEN 이내로 닿는 정상 연결은 제외)
    const seenCross = new Set();
    for (const s of segs) {
      const len = Math.hypot(s.b.x - s.a.x, s.b.y - s.a.y);
      for (const it of items) {
        const r = { left: it.rect.left - LINE_HALF, right: it.rect.right + LINE_HALF, top: it.rect.top - LINE_HALF, bottom: it.rect.bottom + LINE_HALF };
        const hit = clipSeg(s.a, s.b, r);
        if (!hit) continue;
        const depth = (hit[1] - hit[0]) * len;
        const touchesEnd = s.last && hit[1] >= 1 - 1e-6 && depth <= PEN;
        const touchesStart = s.first && hit[0] <= 1e-6 && depth <= PEN;
        if (touchesEnd || touchesStart) continue;
        const key = `${s.path.index}|${nameOf(it.owner)}|${it.kind}`;
        if (seenCross.has(key)) continue;
        seenCross.add(key);
        const tm = (hit[0] + hit[1]) / 2;
        flowIssues.push({ type: 'connector-crosses-element', element: nameOf(it.el), kind: it.kind, owner_class: classOf(it.owner),
          connector: pathLabel(s.path), at: { x: R(s.a.x + (s.b.x - s.a.x) * tm - fr.left), y: R(s.a.y + (s.b.y - s.a.y) * tm - fr.top) },
          depth_px: R(depth) });
      }
    }

    // 7-4) 불필요한 꺾임 — 꺾임 개수 자체는 제한하지 않는다. 같은 방향으로 되돌아가는 지그(Z)
    //      중, 첫 구간을 그대로 연장해도 아무 요소와 부딪히지 않는 것(장애물 회피가 아닌 것)만
    //      지적한다 — 이 지그는 분기 팔과 목적지 연결점의 높이(또는 X)가 어긋나 생긴 것이다.
    for (const p of paths) {
      const target = p.arrow ? findTarget(p) : null;
      const targetOwner = target && target.item ? target.item.owner : null;
      for (let i = 0; i + 3 < p.pts.length; i++) {
        const [a, b, c, d] = [p.pts[i], p.pts[i + 1], p.pts[i + 2], p.pts[i + 3]];
        const o1 = Math.abs(a.y - b.y) < 0.5 ? 'h' : Math.abs(a.x - b.x) < 0.5 ? 'v' : 'd';
        const o2 = Math.abs(b.y - c.y) < 0.5 ? 'h' : Math.abs(b.x - c.x) < 0.5 ? 'v' : 'd';
        const o3 = Math.abs(c.y - d.y) < 0.5 ? 'h' : Math.abs(c.x - d.x) < 0.5 ? 'v' : 'd';
        if (o1 === 'd' || o1 !== o3 || o2 === o1) continue;
        const sameDir = o1 === 'h' ? Math.sign(b.x - a.x) === Math.sign(d.x - c.x) : Math.sign(b.y - a.y) === Math.sign(d.y - c.y);
        if (!sameDir) continue;
        const ext = o1 === 'h' ? [b, { x: d.x, y: b.y }] : [b, { x: b.x, y: d.y }];
        const blocker = items.find(it => it.owner !== targetOwner && clipSeg(ext[0], ext[1], {
          left: it.rect.left - LINE_HALF, right: it.rect.right + LINE_HALF, top: it.rect.top - LINE_HALF, bottom: it.rect.bottom + LINE_HALF }));
        if (blocker) {
          flowAdvisories.push({ type: 'bend-for-avoidance', connector: pathLabel(p), avoids: nameOf(blocker.el) });
          continue;
        }
        flowIssues.push({ type: 'unnecessary-bend', connector: pathLabel(p),
          jog_px: R(o1 === 'h' ? Math.abs(c.y - b.y) : Math.abs(c.x - b.x)),
          target: targetOwner ? nameOf(targetOwner) : null,
          note: '장애물 회피가 아닌 지그 — 분기 팔과 목적지 연결점(이미지 중심)의 위치를 맞추면 제거 가능' });
      }
    }

    // 7-5) 화살표 끝 — 대상이 불명확하거나 대상과 지나치게 떨어진 경우(참고)
    for (const p of paths) {
      if (!p.arrow) continue;
      const t = findTarget(p);
      if (!t) flowAdvisories.push({ type: 'arrow-target-unclear', connector: pathLabel(p) });
      else if (t.item && t.gap > T.nodeGap * 1.5) flowAdvisories.push({ type: 'arrow-gap-large', connector: pathLabel(p), target: nameOf(t.item.owner), gap_px: R(t.gap) });
    }

    // Node 단위 시각 영역(이미지·라벨 합집합)
    const owners = new Map();
    for (const it of items) {
      if (it.owner === it.el && it.kind !== 'box') continue; // flow Node 밖의 개별 요소
      if (!owners.has(it.owner)) owners.set(it.owner, []);
      owners.get(it.owner).push(it);
    }
    const ownerRect = (o) => unionRect(owners.get(o).map(i => i.rect));
    const ownerImgRect = (o) => unionRect(owners.get(o).filter(i => i.kind === 'image').map(i => i.rect)) || ownerRect(o);
    // Node 간 거리는 합집합 사각형이 아니라 실제 구성 요소(이미지·라벨) 사이 최소 거리로 잰다 —
    // 이미지 여러 장이 가로로 놓인 Output Group의 합집합 사각형은 빈 모서리까지 덮어 오탐을 낸다.
    const ownerGap = (o, r) => Math.min(...owners.get(o).map(i => rectGap(i.rect, r)));
    const ownersGap = (a, b) => Math.min(...owners.get(a).map(i => ownerGap(b, i.rect)));
    const ownersOverlap = (a, b) => owners.get(a).some(i => owners.get(b).some(j =>
      xOverlap(i.rect, j.rect) > 0 && Math.min(i.rect.bottom, j.rect.bottom) - Math.max(i.rect.top, j.rect.top) > 0));
    const hSegRect = (s) => ({ left: Math.min(s.a.x, s.b.x), right: Math.max(s.a.x, s.b.x), top: s.a.y - LINE_HALF, bottom: s.a.y + LINE_HALF });

    // 7-5b) Flow 영역(Body Box) 이탈 — 캔버스 안이어도 Body Box 밖으로 나간 라벨·이미지
    for (const it of items) {
      const r = it.rect, out = Math.max(fr.left - r.left, r.right - fr.right, fr.top - r.top, r.bottom - fr.bottom);
      if (out > 1) flowIssues.push({ type: 'outside-flow-field', element: nameOf(it.el), kind: it.kind, overflow_px: R(out) });
    }

    // 7-6) Process — 소속 Lane Connector와의 간격·소속 명확성
    for (const proc of field.querySelectorAll('.flow-process')) {
      if (!owners.has(proc)) continue;
      const P = ownerRect(proc), I = ownerImgRect(proc);
      const cx = (I.left + I.right) / 2;
      let laneY = null;
      const attr = proc.getAttribute('data-flow-lane-y');
      if (attr !== null && !isNaN(parseFloat(attr))) laneY = fr.top + parseFloat(attr);
      else {
        for (const s of segs) {
          if (s.ori !== 'h') continue;
          const r = hSegRect(s);
          if (cx < r.left - 2 || cx > r.right + 2 || s.a.y < I.bottom - 2) continue;
          if (laneY === null || s.a.y < laneY) laneY = s.a.y;
        }
      }
      if (laneY !== null) flowAdvisories.push({ type: 'process-lane-gap', process: nameOf(proc), gap_px: R(laneY - I.bottom) });
      if (laneY === null) { flowIssues.push({ type: 'process-no-lane', process: nameOf(proc), note: 'Process 아래에 소속 Lane Connector가 없음' }); continue; }
      const gapOwn = laneY - I.bottom;
      if (gapOwn < T.processGap / 2) {
        flowIssues.push({ type: 'process-gap-tight', process: nameOf(proc), gap_px: R(gapOwn), expected_px: T.processGap });
      } else if (gapOwn > T.processGap * 2) {
        flowIssues.push({ type: 'process-detached', process: nameOf(proc), gap_px: R(gapOwn), expected_px: T.processGap,
          note: 'Process 이미지가 소속 Lane에서 떠 있어 어느 경로의 공정인지 불명확' });
      }
      // 위쪽(다른 Lane)의 요소가 자기 Lane보다 가까우면 소속이 모호하다
      let nearest = null;
      for (const [o, its] of owners) {
        if (o === proc) continue;
        if (ownerRect(o).bottom > P.top + 2) continue;
        const g = ownersGap(proc, o);
        if (!nearest || g < nearest.gap) nearest = { name: nameOf(o), gap: g };
      }
      for (const s of segs) {
        if (s.ori !== 'h' || Math.abs(s.a.y - laneY) < 1) continue;
        const r = hSegRect(s);
        if (r.bottom > P.top + 2) continue;
        const g = ownerGap(proc, r);
        if (!nearest || g < nearest.gap) nearest = { name: pathLabel(s.path), gap: g };
      }
      // Lane Band — 위쪽 경계(다른 Lane 요소·Connector)와 Process 블록 사이에도 --flow-clearance를 둔다
      if (nearest && nearest.gap > gapOwn && nearest.gap < T.clearance - T.axisTol) {
        flowIssues.push({ type: 'process-band-overflow', process: nameOf(proc), upper_element: nearest.name,
          gap_px: R(nearest.gap), expected_px: T.clearance, note: 'Process 블록이 Lane Band를 넘어 위쪽 Lane에 붙음 — Lane 재배분 → 이미지 공통 높이 → 간격 순으로 조정' });
      }
      if (nearest && nearest.gap <= gapOwn) {
        flowIssues.push({ type: 'process-lane-ambiguous', process: nameOf(proc), own_lane_gap_px: R(gapOwn),
          nearer_element: nearest.name, nearer_gap_px: R(nearest.gap) });
      }
    }

    // 7-7) 구간 구분선 — 위·아래 Lane 콘텐츠와의 관통·간격·균형
    for (const dv of field.querySelectorAll('.flow-section-divider')) {
      const dr = dv.getBoundingClientRect();
      if (!dr.width) continue;
      const y = dr.top;
      const span = { left: dr.left, right: dr.right };
      const content = [];
      for (const [o] of owners) for (const it of owners.get(o)) if (xOverlap(it.rect, span) > 0) content.push({ name: nameOf(o), rect: it.rect });
      for (const s of segs) if (s.ori === 'h') { const r = hSegRect(s); if (xOverlap(r, span) > 0) content.push({ name: pathLabel(s.path), rect: r }); }
      let above = null, below = null;
      for (const c of content) {
        if (c.rect.top < y - 0.5 && c.rect.bottom > y + 0.5) {
          flowIssues.push({ type: 'divider-crosses-element', element: c.name, divider_y: R(y - fr.top) });
          continue;
        }
        if (c.rect.bottom <= y + 0.5) { if (!above || c.rect.bottom > above.rect.bottom) above = c; }
        else if (!below || c.rect.top < below.rect.top) below = c;
      }
      if (!above || !below) continue;
      const gA = y - above.rect.bottom, gB = below.rect.top - y, total = gA + gB;
      flowAdvisories.push({ type: 'divider-gaps', divider_y: R(y - fr.top), gap_above_px: R(gA), gap_below_px: R(gB), nearest_above: above.name, nearest_below: below.name });
      if (Math.min(gA, gB) < T.clearance - T.axisTol) {
        flowIssues.push({ type: 'divider-clearance', divider_y: R(y - fr.top), gap_above_px: R(gA), gap_below_px: R(gB),
          nearest_above: above.name, nearest_below: below.name, expected_px: T.clearance,
          note: total < 2 * T.clearance ? '위·아래 Lane 사이 공간 자체가 부족 — Lane Band 재배분(Lane Y·이미지 공통 높이) 필요' : '구분선을 위·아래 콘텐츠 사이 중간으로 옮긴다' });
      } else if (Math.abs(gA - gB) > Math.max(T.clearance, 0.3 * total)) {
        flowIssues.push({ type: 'divider-off-center', divider_y: R(y - fr.top), gap_above_px: R(gA), gap_below_px: R(gB),
          nearest_above: above.name, nearest_below: below.name, suggested_y: R((above.rect.bottom + below.rect.top) / 2 - fr.top),
          note: '구분선을 위·아래 Lane 콘텐츠 사이 중간에 둔다' });
      }
    }

    // 7-8) 상단 비-Header 콘텐츠(Supporting Message·결론 헤드라인 등)와의 간격
    //      Header System(`header-*`)은 Hard Rule §9 Header Safe Area·Body Box가 이미 간격을 보장하므로 제외한다.
    const blocks = Array.from(slide.children).filter(b => b !== field && !b.contains(field) && !field.contains(b)
      && !/(^|\\s)(header-|page-number|deck-page|deck-footnote)/.test(classOf(b)));
    for (const b of blocks) {
      const br = b.getBoundingClientRect();
      if (!br.width || !br.height || br.bottom > fr.top + fr.height / 2) continue;
      for (const [o] of owners) {
        const r = ownerRect(o);
        if (xOverlap(r, br) <= 0 || r.top < br.top) continue;
        const g = r.top - br.bottom;
        if (g < T.clearance - 0.5) {
          flowIssues.push({ type: 'upper-content-clearance', element: nameOf(o), upper: classOf(b), gap_px: R(g), expected_px: T.clearance });
        }
      }
    }

    // 7-9) Node 간 간격(Occupied Area) — 같은 Output Group 내부는 하나의 Node라 제외
    const ownerList = Array.from(owners.keys());
    for (let i = 0; i < ownerList.length; i++) for (let j = i + 1; j < ownerList.length; j++) {
      const g = ownersGap(ownerList[i], ownerList[j]);
      const overlap = ownersOverlap(ownerList[i], ownerList[j]);
      if (overlap || g < T.nodeGap / 2) {
        flowIssues.push({ type: overlap ? 'node-overlap' : 'node-too-close', a: nameOf(ownerList[i]), b: nameOf(ownerList[j]), gap_px: R(g), expected_px: T.nodeGap });
      } else if (g < T.nodeGap) {
        flowAdvisories.push({ type: 'node-gap-narrow', a: nameOf(ownerList[i]), b: nameOf(ownerList[j]), gap_px: R(g), expected_px: T.nodeGap });
      }
    }

    // 7-10) 종료 단계 공통 축 — 생성 단계가 같은 data-flow-axis로 묶은 Node만 issue로 판정한다.
    //       표기가 없어도 같은 분기 브래킷에서 나와 더 이어지지 않는 종료 Node끼리 중심 X가
    //       다르면 후보로만 기록한다(모든 결과물을 같은 X에 두라는 규칙이 아님).
    const axisGroups = {};
    for (const o of ownerList) {
      const g = o.getAttribute && o.getAttribute('data-flow-axis');
      if (g) (axisGroups[g] = axisGroups[g] || []).push(o);
    }
    for (const [g, os] of Object.entries(axisGroups)) {
      const cxs = os.map(o => { const r = ownerImgRect(o); return (r.left + r.right) / 2; });
      const diff = Math.max(...cxs) - Math.min(...cxs);
      if (diff > T.axisTol) flowIssues.push({ type: 'end-axis-misaligned', group: g, nodes: os.map(nameOf), center_x: cxs.map(v => R(v - fr.left)), diff_px: R(diff) });
    }
    const brackets = segs.filter(s => s.ori === 'v');
    const byBracket = new Map();
    for (const p of paths) {
      if (!p.arrow) continue;
      const st = p.pts[0];
      const br = brackets.find(s => s.path !== p && Math.abs(s.a.x - st.x) <= 2 && st.y >= Math.min(s.a.y, s.b.y) - 2 && st.y <= Math.max(s.a.y, s.b.y) + 2);
      const t = findTarget(p);
      if (!br || !t || !t.item || t.item.owner === t.item.el) continue;
      const o = t.item.owner, r = ownerRect(o);
      const continues = paths.some(q => q !== p && rectGap({ left: q.pts[0].x, right: q.pts[0].x, top: q.pts[0].y, bottom: q.pts[0].y }, r) <= 24);
      if (continues || o.getAttribute('data-flow-axis')) continue;
      if (!byBracket.has(br)) byBracket.set(br, []);
      if (!byBracket.get(br).includes(o)) byBracket.get(br).push(o);
    }
    for (const os of byBracket.values()) {
      if (os.length < 2) continue;
      const cxs = os.map(o => { const r = ownerImgRect(o); return (r.left + r.right) / 2; });
      const diff = Math.max(...cxs) - Math.min(...cxs);
      if (diff > T.axisTol) flowAdvisories.push({ type: 'end-axis-candidate', nodes: os.map(nameOf), center_x: cxs.map(v => R(v - fr.left)), diff_px: R(diff),
        note: '같은 분기점의 종료 결과물 — 같은 종료 단계면 data-flow-axis로 묶고 중심 X를 맞춘다' });
    }
  }

  return {
    overflow, clipped, overlaps,
    page_number_issues: pageNumberIssues,
    deck_footnote_issues: deckFootnoteIssues,
    bottom_safe_area_violations: bottomSafeAreaViolations,
    common_element_issues: commonElementIssues,
    slide_type: slideType,
    image_issues: imageIssues,
    image_advisories: imageAdvisories,
    image_sizes: imageSizes,
    flow_issues: flowIssues,
    flow_advisories: flowAdvisories,
  };
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
            # file:// 이미지의 투명 여백(alpha)을 캔버스로 읽기 위해 로컬 파일을 같은 출처로 취급한다.
            browser = p.chromium.launch(args=["--allow-file-access-from-files"])
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
                flagged = bool(
                    result["overflow"] or result["clipped"] or result["overlaps"]
                    or result["page_number_issues"] or result["deck_footnote_issues"]
                    or result["bottom_safe_area_violations"] or result["image_issues"]
                    or result["common_element_issues"]
                    or result["flow_issues"]
                )
                result["flagged"] = flagged
                layout_audit[f"slide_{idx}"] = result
                if flagged:
                    print(
                        f"[qa_render] slide {idx}: LAYOUT AUDIT FLAGGED "
                        f"(overflow={len(result['overflow'])}, clipped={len(result['clipped'])}, "
                        f"overlaps={len(result['overlaps'])}, page_number_issues={len(result['page_number_issues'])}, "
                        f"deck_footnote_issues={len(result['deck_footnote_issues'])}, "
                        f"bottom_safe_area_violations={len(result['bottom_safe_area_violations'])}, "
                        f"common_element_issues={len(result['common_element_issues'])}, "
                        f"image_issues={len(result['image_issues'])}, "
                        f"flow_issues={len(result['flow_issues'])})"
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
