"""
web-ppt-generator / new_version.py

웹PPT 버전 스냅샷을 관리한다 (git이 아닌 단순 폴더 복사 방식).

사용법:
    # 최초 생성: templates/를 기반으로 v1 생성
    python new_version.py --project /output/{project-name} --scaffold

    # 수정: 최신 버전을 복사해 다음 번호로 새 버전 생성
    python new_version.py --project /output/{project-name} --from-latest

    # 롤백: 과거 버전(vK)을 복사해 최신 버전으로 승격 (vK 자체는 그대로 보존)
    python new_version.py --project /output/{project-name} --rollback-from v2
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"


def find_versions(web_ppt_dir: Path) -> list[int]:
    if not web_ppt_dir.exists():
        return []
    versions = []
    for p in web_ppt_dir.iterdir():
        if p.is_dir() and re.fullmatch(r"v\d+", p.name):
            versions.append(int(p.name[1:]))
    return sorted(versions)


def scaffold(project_dir: Path) -> Path:
    web_ppt_dir = project_dir / "web_ppt"
    web_ppt_dir.mkdir(parents=True, exist_ok=True)
    versions = find_versions(web_ppt_dir)
    if versions:
        raise SystemExit(f"이미 버전이 존재합니다({versions}). --from-latest 를 사용하세요.")

    target = web_ppt_dir / "v1"
    if not TEMPLATES_DIR.exists():
        raise SystemExit(f"템플릿 폴더가 없습니다: {TEMPLATES_DIR}")
    shutil.copytree(TEMPLATES_DIR, target)
    print(f"[web-ppt-generator] v1 생성 완료 -> {target}")
    return target


def from_latest(project_dir: Path) -> Path:
    web_ppt_dir = project_dir / "web_ppt"
    versions = find_versions(web_ppt_dir)
    if not versions:
        raise SystemExit("기존 버전이 없습니다. --scaffold 로 먼저 생성하세요.")
    latest = versions[-1]
    new_num = latest + 1
    src = web_ppt_dir / f"v{latest}"
    dst = web_ppt_dir / f"v{new_num}"
    shutil.copytree(src, dst)
    print(f"[web-ppt-generator] v{latest} -> v{new_num} 복사 완료 -> {dst}")
    return dst


def rollback_from(project_dir: Path, source_version: str) -> Path:
    web_ppt_dir = project_dir / "web_ppt"
    versions = find_versions(web_ppt_dir)
    if not versions:
        raise SystemExit("기존 버전이 없습니다.")
    src = web_ppt_dir / source_version
    if not src.exists():
        raise SystemExit(f"롤백 대상 버전을 찾을 수 없습니다: {src}")
    new_num = versions[-1] + 1
    dst = web_ppt_dir / f"v{new_num}"
    shutil.copytree(src, dst)
    print(f"[web-ppt-generator] {source_version} 롤백 -> v{new_num} 생성 완료 -> {dst} (기존 스냅샷은 보존됨)")
    return dst


def main() -> None:
    parser = argparse.ArgumentParser(description="웹PPT 버전 스냅샷 생성/롤백")
    parser.add_argument("--project", required=True, help="/output/{project-name} 경로")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scaffold", action="store_true", help="v1을 템플릿 기반으로 최초 생성")
    group.add_argument("--from-latest", action="store_true", help="최신 버전을 복사해 다음 버전 생성")
    group.add_argument("--rollback-from", metavar="vK", help="과거 버전(vK)을 복사해 최신 버전으로 승격")
    args = parser.parse_args()

    project_dir = Path(args.project)
    if not project_dir.exists():
        raise SystemExit(f"프로젝트 폴더가 없습니다: {project_dir}")

    if args.scaffold:
        scaffold(project_dir)
    elif args.from_latest:
        from_latest(project_dir)
    elif args.rollback_from:
        rollback_from(project_dir, args.rollback_from)


if __name__ == "__main__":
    main()
