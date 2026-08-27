#!/usr/bin/env python3
"""
web-ppt-generator / fine_editor / server.py

Human Fine Editing 전용 경량 로컬 에디터 서버 (표준 라이브러리만 사용, 추가 패키지 설치 없음).
확정된 web_ppt/v{N}/을 읽기 전용으로 두고, 별도 v{N}-fine/ 폴더를 새로 만들어 그 위에서만
브라우저 기반으로 문구·Text/Image 위치·크기·이미지 교체 같은 최종 미세 수정을 한다.
content-designer/web-ppt-generator의 생성 로직을 재사용하지 않는 완전히 별도의 Utility다
(CLAUDE.md "Human Fine Editing" 절 참조). Agent가 호출하지 않으며, 사람이 터미널에서 직접
실행한다.

사용법:
    python server.py --project-dir /output/{project}/web_ppt/v{N} [--port 8765] [--no-browser]

엔드포인트:
    GET  /                    에디터 UI
    GET  /edit/<path>         fine 폴더 내 파일 (iframe 미리보기 겸 편집 대상)
    GET  /static/<path>       에디터 자체 정적 리소스(JS/CSS)
    GET  /api/info            현재 세션 정보(원본 경로, fine 폴더 경로)
    POST /api/save            {html} -> fine 폴더 index.html 덮어쓰기
    POST /api/upload-image    {filename, dataUrl} -> fine 폴더 assets/fine-uploads/에 저장
    POST /api/bundle          기존 bundle_for_share.py를 fine 폴더에 대해 실행 (shared.html 생성)
    POST /api/qa              기존 qa_render.py --audit-layout을 fine 폴더에 대해 실행 (구조 QA 재검증)
    POST /api/finalize        저장 -> 전체 슬라이드 구조 QA -> shared.html 번들을 한 번에 실행
                               (사용자가 index.html을 직접 열거나 관리할 필요 없이, Editor 안에서
                               "최종 확정" 한 번으로 공유용 산출물까지 끝내기 위한 진입점)
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
import shutil
import subprocess
import sys
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

TOOL_DIR = Path(__file__).parent
SCRIPTS_DIR = TOOL_DIR.parent  # .../web-ppt-generator/scripts

SOURCE_DIR: Path
FINE_DIR: Path


def next_fine_dir(source_dir: Path) -> Path:
    """원본 v{N}과 나란히, 원본을 건드리지 않는 새 편집용 폴더 경로를 정한다."""
    parent = source_dir.parent
    base = source_dir.name  # 예: "v3"
    candidate = parent / f"{base}-fine"
    if not candidate.exists():
        return candidate
    n = 2
    while (parent / f"{base}-fine{n}").exists():
        n += 1
    return parent / f"{base}-fine{n}"


def safe_join(root: Path, rel: str) -> Path:
    """root 하위로만 접근을 제한한다 (경로 탈출 방지)."""
    rel = unquote(rel).lstrip("/")
    root_resolved = root.resolve()
    target = (root_resolved / rel).resolve()
    if target != root_resolved and root_resolved not in target.parents:
        raise PermissionError(f"허용 범위 밖 경로: {rel}")
    return target


class EditorHandler(BaseHTTPRequestHandler):
    server_version = "FineEditor/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("[fine-editor] " + (fmt % args) + "\n")

    # ---- 공통 응답 헬퍼 ----
    def _send_bytes(self, data: bytes, content_type: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, obj, status: int = 200) -> None:
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self._send_bytes(data, "application/json; charset=utf-8", status)

    def _send_file(self, path: Path) -> None:
        if not path.is_file():
            self._send_json({"error": f"파일을 찾을 수 없음: {path.name}"}, 404)
            return
        mime, _ = mimetypes.guess_type(str(path))
        mime = mime or "application/octet-stream"
        self._send_bytes(path.read_bytes(), mime)

    def _read_json_body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length) if length else b"{}"
        return json.loads(raw.decode("utf-8"))

    # ---- GET ----
    def do_GET(self) -> None:
        path = urlparse(self.path).path
        try:
            if path == "/":
                self._send_file(TOOL_DIR / "editor_ui.html")
            elif path.startswith("/static/"):
                self._send_file(safe_join(TOOL_DIR, path[len("/static/"):]))
            elif path.startswith("/edit/"):
                sub = path[len("/edit/"):] or "index.html"
                self._send_file(safe_join(FINE_DIR, sub))
            elif path == "/api/info":
                self._send_json({
                    "source_dir": str(SOURCE_DIR),
                    "fine_dir": str(FINE_DIR),
                    "fine_dir_name": FINE_DIR.name,
                })
            else:
                self._send_json({"error": "not found"}, 404)
        except PermissionError as e:
            self._send_json({"error": str(e)}, 403)
        except Exception as e:  # noqa: BLE001 - 로컬 도구 최상위 에러 응답
            self._send_json({"error": str(e)}, 500)

    # ---- POST ----
    def do_POST(self) -> None:
        path = urlparse(self.path).path
        try:
            if path == "/api/save":
                self._handle_save()
            elif path == "/api/upload-image":
                self._handle_upload_image()
            elif path == "/api/bundle":
                self._handle_bundle()
            elif path == "/api/qa":
                self._handle_qa()
            elif path == "/api/finalize":
                self._handle_finalize()
            else:
                self._send_json({"error": "not found"}, 404)
        except Exception as e:  # noqa: BLE001
            self._send_json({"error": str(e)}, 500)

    def _handle_save(self) -> None:
        body = self._read_json_body()
        html = body.get("html", "")
        if not html.strip():
            self._send_json({"error": "빈 HTML은 저장하지 않습니다."}, 400)
            return
        target = FINE_DIR / "index.html"
        target.write_text(html, encoding="utf-8")
        self._send_json({"ok": True, "path": str(target)})

    def _handle_upload_image(self) -> None:
        body = self._read_json_body()
        filename = re.sub(r"[^A-Za-z0-9._-]", "_", body.get("filename") or "image.png")
        data_url = body.get("dataUrl") or ""
        m = re.match(r"^data:([^;]+);base64,(.+)$", data_url, re.DOTALL)
        if not m:
            self._send_json({"error": "잘못된 이미지 데이터"}, 400)
            return
        raw = base64.b64decode(m.group(2))
        dest_dir = FINE_DIR / "assets" / "fine-uploads"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_name = f"{int(time.time() * 1000)}_{filename}"
        (dest_dir / dest_name).write_bytes(raw)
        self._send_json({"ok": True, "path": f"assets/fine-uploads/{dest_name}"})

    def _handle_bundle(self) -> None:
        script = SCRIPTS_DIR / "bundle_for_share.py"
        proc = subprocess.run(
            [sys.executable, str(script), "--project-dir", str(FINE_DIR)],
            capture_output=True, text=True,
        )
        shared_path = FINE_DIR / "shared.html"
        self._send_json({
            "ok": proc.returncode == 0,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "shared_html_path": str(shared_path) if (proc.returncode == 0 and shared_path.is_file()) else None,
        })

    def _handle_finalize(self) -> None:
        """저장 -> 전체 슬라이드 구조 QA -> shared.html 번들을 한 번의 요청으로 묶어 처리한다.
        기존 /api/save, /api/qa, /api/bundle이 이미 각각 호출하던 스크립트(qa_render.py,
        bundle_for_share.py)를 그대로 순서대로 재사용할 뿐, 새 로직을 추가하지 않는다."""
        body = self._read_json_body()
        html = body.get("html", "")
        if not html.strip():
            self._send_json({"error": "빈 HTML은 저장하지 않습니다."}, 400)
            return

        save_path = FINE_DIR / "index.html"
        save_path.write_text(html, encoding="utf-8")

        qa_script = SCRIPTS_DIR / "qa_render.py"
        qa_out = FINE_DIR / ".qa" / "fine"
        qa_proc = subprocess.run(
            [sys.executable, str(qa_script), "--web-ppt", str(FINE_DIR), "--out", str(qa_out), "--audit-layout"],
            capture_output=True, text=True,
        )
        layout_audit = {}
        audit_path = qa_out / "layout-audit.json"
        if audit_path.is_file():
            layout_audit = json.loads(audit_path.read_text(encoding="utf-8"))
        flagged_slides = [k for k, v in layout_audit.items() if v.get("flagged")]

        bundle_script = SCRIPTS_DIR / "bundle_for_share.py"
        bundle_proc = subprocess.run(
            [sys.executable, str(bundle_script), "--project-dir", str(FINE_DIR)],
            capture_output=True, text=True,
        )
        shared_path = FINE_DIR / "shared.html"
        bundle_ok = bundle_proc.returncode == 0 and shared_path.is_file()

        self._send_json({
            "ok": bundle_ok,
            "save_path": str(save_path),
            "qa_ok": qa_proc.returncode == 0,
            "qa_stderr": qa_proc.stderr,
            "flagged_slides": flagged_slides,
            "layout_audit": layout_audit,
            "bundle_stdout": bundle_proc.stdout,
            "bundle_stderr": bundle_proc.stderr,
            "shared_html_path": str(shared_path) if bundle_ok else None,
        })

    def _handle_qa(self) -> None:
        body = self._read_json_body()
        slides = str(body.get("slides") or "").strip()
        script = SCRIPTS_DIR / "qa_render.py"
        out_dir = FINE_DIR / ".qa" / "fine"
        args = [sys.executable, str(script), "--web-ppt", str(FINE_DIR), "--out", str(out_dir), "--audit-layout"]
        if slides:
            args += ["--slides", slides]
        proc = subprocess.run(args, capture_output=True, text=True)
        report = {}
        audit_path = out_dir / "layout-audit.json"
        if audit_path.is_file():
            report = json.loads(audit_path.read_text(encoding="utf-8"))
        self._send_json({
            "ok": proc.returncode == 0,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "layout_audit": report,
        })


def main() -> None:
    global SOURCE_DIR, FINE_DIR
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project-dir", required=True, help="확정된 web_ppt/v{N} 폴더 경로 (읽기 전용으로만 사용)")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true", help="자동으로 브라우저를 열지 않음")
    args = ap.parse_args()

    SOURCE_DIR = Path(args.project_dir).resolve()
    if not (SOURCE_DIR / "index.html").is_file():
        raise SystemExit(f"index.html을 찾을 수 없습니다: {SOURCE_DIR}")

    FINE_DIR = next_fine_dir(SOURCE_DIR)
    shutil.copytree(SOURCE_DIR, FINE_DIR)
    print(f"[fine-editor] 원본(읽기 전용, 수정하지 않음): {SOURCE_DIR}")
    print(f"[fine-editor] 편집용 버전 생성: {FINE_DIR}")

    port = args.port
    httpd = None
    for _ in range(10):
        try:
            httpd = ThreadingHTTPServer(("127.0.0.1", port), EditorHandler)
            break
        except OSError:
            port += 1
    if httpd is None:
        raise SystemExit("사용 가능한 포트를 찾지 못했습니다.")

    url = f"http://127.0.0.1:{port}/"
    print(f"[fine-editor] 서버 시작: {url}")
    print("[fine-editor] Ctrl+C로 종료하세요.")
    if not args.no_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[fine-editor] 종료합니다.")


if __name__ == "__main__":
    main()
