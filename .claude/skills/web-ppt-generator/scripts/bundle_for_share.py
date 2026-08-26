#!/usr/bin/env python3
"""
web_ppt/v{N}/ 폴더(index.html + style.css + assets/...)를 외부 공유가 가능한
단일 self-contained HTML 파일로 번들링한다.

- style.css → <style> 인라인
- 로컬 <script src="..."> (vendor JS 등) → <script> 인라인
- 로컬 <img src="..."> → base64 data URI
- style.css 안의 url(...) 참조(배경 이미지 등)도 base64 data URI로 치환

외부(http/https) 링크나 data: URI는 건드리지 않는다.
LLM 판단이 필요 없는 순수 파일 조작이며, 원본 vN/ 폴더는 **읽기 전용으로만**
사용한다 — index.html/style.css/assets는 절대 수정하지 않고, 결과는 같은
폴더에 별도 산출물(기본 shared.html)로만 저장한다. 인라인 처리 후 로컬 참조
(상대경로·`file:///` 절대경로 등)가 하나라도 남아 있으면 다른 PC에서 열리지
않는 깨진 결과물이므로, 이 경우 shared.html을 쓰지 않고 실패로 종료한다
(원본 vN/ 폴더는 어떤 경우에도 건드리지 않으므로 이 실패가 원본이나 이미
끝난 QA 결과물을 훼손하지 않는다).

사용법:
  python bundle_for_share.py --project-dir /output/{project-name}/web_ppt/v{N} [--entry index.html] [--output shared.html]

종료 코드: 0=성공, 1=실패(entry 없음/미해결 로컬 참조 잔존 등, stderr에 상세 사유 출력).
"""

import argparse
import base64
import mimetypes
import re
import sys
from pathlib import Path

LOCAL_REF_SKIP_PREFIXES = ("http://", "https://", "data:", "//", "#", "mailto:", "tel:")

WARN_SIZE_BYTES = 12 * 1024 * 1024  # Artifact 16MB 한도 대비 경고 임계치


class BundleValidationError(Exception):
    """인라인 처리 후에도 로컬 파일 의존성(상대경로, file:/// 절대경로 등)이
    남아 있어 다른 PC에서 열 수 없다고 판단될 때 발생시킨다."""


def is_local_ref(url: str) -> bool:
    url = url.strip()
    if not url:
        return False
    return not url.lower().startswith(LOCAL_REF_SKIP_PREFIXES)


def to_data_uri(file_path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(file_path))
    if mime is None:
        mime = "application/octet-stream"
    data = file_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"


def inline_css_urls(css_text: str, base_dir: Path) -> str:
    pattern = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)")

    def repl(m):
        quote, ref = m.group(1), m.group(2)
        if not is_local_ref(ref):
            return m.group(0)
        target = (base_dir / ref).resolve()
        if not target.is_file():
            print(f"  [경고] CSS 참조 파일을 찾을 수 없음, 건너뜀: {ref}", file=sys.stderr)
            return m.group(0)
        data_uri = to_data_uri(target)
        return f"url({quote}{data_uri}{quote})"

    return pattern.sub(repl, css_text)


def inline_stylesheets(html: str, base_dir: Path) -> str:
    pattern = re.compile(
        r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*>'
        r'|<link\s+[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']stylesheet["\'][^>]*>'
    )

    def repl(m):
        href = m.group(1) or m.group(2)
        if not is_local_ref(href):
            return m.group(0)
        target = (base_dir / href).resolve()
        if not target.is_file():
            print(f"  [경고] 스타일시트를 찾을 수 없음, 건너뜀: {href}", file=sys.stderr)
            return m.group(0)
        css_text = target.read_text(encoding="utf-8")
        css_text = inline_css_urls(css_text, target.parent)
        return f"<style>\n{css_text}\n</style>"

    return pattern.sub(repl, html)


def inline_scripts(html: str, base_dir: Path) -> str:
    pattern = re.compile(r'<script\s+([^>]*?)src=["\']([^"\']+)["\']([^>]*)>\s*</script>')

    def repl(m):
        pre_attrs, src, post_attrs = m.group(1), m.group(2), m.group(3)
        if not is_local_ref(src):
            return m.group(0)
        target = (base_dir / src).resolve()
        if not target.is_file():
            print(f"  [경고] 스크립트를 찾을 수 없음, 건너뜀: {src}", file=sys.stderr)
            return m.group(0)
        js_text = target.read_text(encoding="utf-8")
        attrs = (pre_attrs + post_attrs).strip()
        attrs = " " + attrs if attrs else ""
        return f"<script{attrs}>\n{js_text}\n</script>"

    return pattern.sub(repl, html)


def inline_images(html: str, base_dir: Path) -> str:
    pattern = re.compile(r'(<img\s+[^>]*?src=["\'])([^"\']+)(["\'])')

    def repl(m):
        pre, src, post = m.group(1), m.group(2), m.group(3)
        if not is_local_ref(src):
            return m.group(0)
        target = (base_dir / src).resolve()
        if not target.is_file():
            print(f"  [경고] 이미지를 찾을 수 없음, 건너뜀: {src}", file=sys.stderr)
            return m.group(0)
        return pre + to_data_uri(target) + post

    return pattern.sub(repl, html)


def inline_inline_style_urls(html: str, base_dir: Path) -> str:
    """HTML 태그의 style="..." 속성 안에 직접 적힌 url(...) 참조(예:
    <div style="background-image:url('assets/images/x.png')">)를 인라인
    처리한다. style.css 파일 안의 url(...)은 inline_stylesheets가 이미
    처리하므로, 이 함수는 HTML 문서에 인라인으로 박힌 style 속성만 대상으로
    한다."""
    pattern = re.compile(r'style\s*=\s*(["\'])(.*?)\1', re.DOTALL)

    def repl(m):
        quote, style_text = m.group(1), m.group(2)
        new_style = inline_css_urls(style_text, base_dir)
        return f'style={quote}{new_style}{quote}'

    return pattern.sub(repl, html)


def validate_no_local_refs(html: str) -> list[str]:
    """인라인 처리가 끝난 최종 HTML 문자열에서 여전히 로컬 파일에 의존하는
    참조(상대경로, `file:///C:/...` 같은 현재 PC 절대경로 등)가 남아 있는지
    검사한다. 비어 있지 않은 리스트를 반환하면 그 자체로 실패 사유 목록이다."""
    offenders: list[str] = []

    attr_pattern = re.compile(r'(?:src|href)\s*=\s*["\']([^"\']+)["\']')
    for ref in attr_pattern.findall(html):
        if is_local_ref(ref):
            offenders.append(ref)

    url_pattern = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)")
    for _, ref in url_pattern.findall(html):
        if is_local_ref(ref):
            offenders.append(ref)

    # is_local_ref 판정과 별개로, file:// 절대경로는 그 자체로 명백한 현재 PC
    # 의존성이므로(다른 PC에는 같은 경로에 파일이 없음) 별도로도 잡아낸다.
    for m in re.finditer(r"file://\S+", html, flags=re.IGNORECASE):
        offenders.append(m.group(0))

    # 중복 제거, 순서 유지
    seen: set[str] = set()
    unique_offenders = []
    for o in offenders:
        if o not in seen:
            seen.add(o)
            unique_offenders.append(o)
    return unique_offenders


def bundle(project_dir: Path, entry: str, output: str) -> Path:
    entry_path = project_dir / entry
    if not entry_path.is_file():
        raise FileNotFoundError(f"entry 파일을 찾을 수 없음: {entry_path}")

    html = entry_path.read_text(encoding="utf-8")
    html = inline_stylesheets(html, project_dir)
    html = inline_scripts(html, project_dir)
    html = inline_images(html, project_dir)
    html = inline_inline_style_urls(html, project_dir)

    offenders = validate_no_local_refs(html)
    if offenders:
        detail = "\n".join(f"  - {o}" for o in offenders)
        raise BundleValidationError(
            "인라인 처리 후에도 로컬 파일 의존성이 남아 있어 다른 PC에서 열 수 없습니다 "
            f"(shared.html을 쓰지 않고 중단합니다, 원본 vN/ 폴더는 변경되지 않았습니다):\n{detail}"
        )

    out_path = project_dir / output
    out_path.write_text(html, encoding="utf-8")

    size = out_path.stat().st_size
    print(f"번들 완료: {out_path} ({size / 1024:.0f} KB)")
    if size > WARN_SIZE_BYTES:
        print(
            f"  [경고] 파일 크기가 {WARN_SIZE_BYTES / 1024 / 1024:.0f}MB를 초과했습니다. "
            "Artifact 게시 한도(16MB)에 근접하니 이미지 용량을 줄이는 것을 검토하세요.",
            file=sys.stderr,
        )
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project-dir", required=True, help="web_ppt/v{N} 폴더 경로")
    ap.add_argument("--entry", default="index.html", help="번들링 시작 HTML 파일명 (기본: index.html)")
    ap.add_argument("--output", default="shared.html", help="산출물 파일명 (기본: shared.html, project-dir 내부에 저장)")
    args = ap.parse_args()

    project_dir = Path(args.project_dir).resolve()
    if not project_dir.is_dir():
        print(f"프로젝트 폴더가 존재하지 않음: {project_dir}", file=sys.stderr)
        sys.exit(1)

    try:
        bundle(project_dir, args.entry, args.output)
    except (FileNotFoundError, BundleValidationError) as e:
        print(f"번들링 실패: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
