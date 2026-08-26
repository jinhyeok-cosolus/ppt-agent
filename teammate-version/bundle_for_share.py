#!/usr/bin/env python3
"""
web_ppt/v{N}/ 폴더(index.html + style.css + assets/...)를 외부 공유가 가능한
단일 self-contained HTML 파일로 번들링한다.

- style.css → <style> 인라인
- 로컬 <script src="..."> (vendor JS 등) → <script> 인라인
- 로컬 <img src="..."> → base64 data URI
- style.css 안의 url(...) 참조(배경 이미지 등)도 base64 data URI로 치환

외부(http/https) 링크나 data: URI는 건드리지 않는다.
LLM 판단이 필요 없는 순수 파일 조작이며, 원본 vN/ 폴더는 수정하지 않고
같은 폴더에 별도 산출물(기본 shared.html)로 저장한다.

사용법:
  python bundle_for_share.py --project-dir /output/{project-name}/web_ppt/v{N} [--entry index.html] [--output shared.html]
"""

import argparse
import base64
import mimetypes
import re
import sys
from pathlib import Path

LOCAL_REF_SKIP_PREFIXES = ("http://", "https://", "data:", "//", "#")

WARN_SIZE_BYTES = 12 * 1024 * 1024  # Artifact 16MB 한도 대비 경고 임계치


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


def bundle(project_dir: Path, entry: str, output: str) -> Path:
    entry_path = project_dir / entry
    if not entry_path.is_file():
        raise FileNotFoundError(f"entry 파일을 찾을 수 없음: {entry_path}")

    html = entry_path.read_text(encoding="utf-8")
    html = inline_stylesheets(html, project_dir)
    html = inline_scripts(html, project_dir)
    html = inline_images(html, project_dir)

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

    bundle(project_dir, args.entry, args.output)


if __name__ == "__main__":
    main()
