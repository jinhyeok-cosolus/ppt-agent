#!/usr/bin/env python3
"""Deterministic Content Fidelity QA using existing analysis artifacts only."""

from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from typing import Any


SLIDE_RE = re.compile(r"^##\s+Slide\s+(\d+)\.", re.M)
NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:\d{4}\s*년|\d+(?:\.\d+)?\s*(?:%|％|명|개|건|곳|원|달러|억원|만원|톤|kg|g|km|m|배|년|월|일|단계|개국))(?![A-Za-z0-9])",
    re.I,
)
MODEL_RE = re.compile(r"\b(?=[A-Za-z0-9-]*[A-Za-z])(?=[A-Za-z0-9-]*\d)[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+\b")
EN_ENTITY_RE = re.compile(r"\b(?:[A-Z][A-Za-z0-9&.-]+|[A-Z]{2,})(?:\s+(?:[A-Z][A-Za-z0-9&.-]+|[A-Z]{2,})){0,3}\b")
KO_COMPANY_RE = re.compile(r"(?:주식회사\s*[가-힣A-Za-z0-9&.-]+|[가-힣A-Za-z0-9&.-]+\s*\(주\)|[가-힣A-Za-z0-9&.-]+(?:사|그룹))")
MARKER_RE = re.compile(r"Data\s*Pending|데이터\s*(?:미제공|준비\s*중|확인\s*필요)|\[확인필요\]|uncertain|불확실|확인\s*필요", re.I)
IGNORE_ENTITIES = {"HTML", "CSS", "PPT", "PPTX", "IR", "KPI", "ESG", "R&D", "CEO", "Before", "After", "Data Pending", "Required", "Optional", "Source"}


def norm(value: str) -> str:
    return re.sub(r"[\s\u00a0,]+", "", html.unescape(value)).lower()


def strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            if key not in {"path", "source_file"}:
                yield from strings(item)


def uncertainty_indicators(value: Any, refs: set[str]) -> set[str]:
    """Find stable ref/path tokens for uncertain evidence already carried by mapping."""
    found: set[str] = set()
    if isinstance(value, list):
        for item in value:
            found.update(uncertainty_indicators(item, refs))
    elif isinstance(value, dict):
        identifiers = {str(value.get(key, "")) for key in ("id", "ref")}
        if identifiers & refs:
            found.update(x for x in identifiers if x)
            if value.get("path"):
                found.add(Path(str(value["path"])).name)
        for item in value.values():
            found.update(uncertainty_indicators(item, refs))
    return found


class SlideHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[list[str]] = []
        self.depth = 0
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "section" and "slide" in (attrs_dict.get("class") or "").split():
            self.slides.append([])
            self.depth = 1
        elif self.depth:
            self.depth += 1
        if self.depth and tag in {"script", "style"}:
            self.skip_depth = self.depth
        if self.depth and self.slides:
            for key in ("src", "alt", "title", "data-chart-json"):
                if attrs_dict.get(key):
                    self.slides[-1].append(str(attrs_dict[key]))

    def handle_endtag(self, tag: str) -> None:
        if self.depth:
            if self.skip_depth == self.depth:
                self.skip_depth = 0
            self.depth -= 1

    def handle_data(self, data: str) -> None:
        if self.depth and not self.skip_depth and self.slides:
            self.slides[-1].append(data)


def outline_blocks(text: str) -> dict[int, str]:
    matches = list(SLIDE_RE.finditer(text))
    return {int(m.group(1)): text[m.start() : matches[i + 1].start() if i + 1 < len(matches) else len(text)] for i, m in enumerate(matches)}


def required_evidence(block: str) -> list[str]:
    found: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("- Evidence:"):
            current = [stripped.split(":", 1)[1].strip()]
        elif current and stripped.startswith("- Required/Optional:"):
            if "Required" in stripped:
                found.append(" ".join(current))
            current = []
        elif current and stripped and not stripped.startswith(("- Claim:", "- Relationship:")):
            current.append(stripped.lstrip("- "))
    return found


def evidence_atoms(evidence: str) -> list[str]:
    atoms = re.findall(r'["“](.*?)["”]', evidence)
    atoms += NUMBER_RE.findall(evidence)
    atoms += re.findall(r"(?:기업명|대표자|임직원|소재지|제품명|회사명)\s*\(([^)]+)\)", evidence)
    atoms += re.findall(r"\bimg\d+\b", evidence, re.I)
    return list(dict.fromkeys(x.strip() for x in atoms if len(norm(x)) >= 2))


def fact_candidates(text: str) -> list[tuple[str, str]]:
    candidates = [("numeric", x) for x in NUMBER_RE.findall(text)]
    candidates += [("model", x) for x in MODEL_RE.findall(text)]
    candidates += [("company", x) for x in KO_COMPANY_RE.findall(text)]
    candidates += [("entity", x) for x in EN_ENTITY_RE.findall(text)]
    result: list[tuple[str, str]] = []
    seen: set[str] = set()
    for kind, value in candidates:
        value = value.strip(" .,:;()[]")
        key = f"{kind}:{norm(value)}"
        if value in IGNORE_ENTITIES or len(norm(value)) < 2 or key in seen:
            continue
        seen.add(key)
        result.append((kind, value))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--material-analysis", required=True)
    parser.add_argument("--composition-map", required=True)
    parser.add_argument("--outline", required=True)
    parser.add_argument("--web-ppt", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--slides", help="comma-separated slide numbers; omit for all")
    args = parser.parse_args()

    material = json.loads(Path(args.material_analysis).read_text(encoding="utf-8"))
    composition = json.loads(Path(args.composition_map).read_text(encoding="utf-8"))
    outline_text = Path(args.outline).read_text(encoding="utf-8")
    blocks = outline_blocks(outline_text)
    html_parser = SlideHTMLParser()
    html_parser.feed((Path(args.web_ppt) / "index.html").read_text(encoding="utf-8"))
    slide_text = {i + 1: " ".join(parts) for i, parts in enumerate(html_parser.slides)}
    selected = set(blocks) if not args.slides else {int(x.strip()) for x in args.slides.split(",") if x.strip()}
    grounding_norm = norm(" ".join(strings(material)) + " " + outline_text)
    map_slides = {int(s["slide_number"]): s for s in composition.get("slides", [])}
    report: dict[str, Any] = {"status": "pass", "scope": sorted(selected), "slides": {}}

    for number in sorted(selected):
        rendered = slide_text.get(number, "")
        rendered_norm = norm(rendered)
        block = blocks.get(number, "")
        issues: list[dict[str, Any]] = []
        unchecked: list[dict[str, Any]] = []
        for kind, fact in fact_candidates(rendered):
            if norm(fact) not in grounding_norm:
                issues.append({"type": "ungrounded_explicit_fact", "kind": kind, "value": fact})
        for evidence in required_evidence(block):
            atoms = evidence_atoms(evidence)
            if not atoms:
                unchecked.append({"type": "required_evidence_without_deterministic_atom", "evidence": evidence})
                continue
            missing = [atom for atom in atoms if norm(atom) not in rendered_norm]
            if len(missing) == len(atoms):
                issues.append({"type": "required_evidence_missing", "evidence": evidence, "checked_atoms": atoms})
            elif missing:
                issues.append({"type": "required_evidence_partially_missing", "evidence": evidence, "missing_atoms": missing})
        pending = "Data Pending" in block or bool(map_slides.get(number, {}).get("data_pending_carried"))
        confirmation = "[확인필요]" in block
        uncertain_refs = {str(x) for x in map_slides.get(number, {}).get("uncertain_evidence_carried", [])}
        uncertain = bool(uncertain_refs) or bool(re.search(r"uncertain(?:보류)?\s*[1-9]", block, re.I))
        if pending and not MARKER_RE.search(rendered):
            issues.append({"type": "data_pending_marker_missing"})
        if confirmation and "[확인필요]" not in rendered:
            issues.append({"type": "confirmation_marker_missing"})
        if uncertain:
            indicators = uncertainty_indicators(material, uncertain_refs)
            used = [x for x in indicators if norm(x) and norm(x) in rendered_norm]
            if used and not MARKER_RE.search(rendered):
                issues.append({"type": "uncertain_state_marker_missing", "matched_assets": used})
            elif not used:
                unchecked.append({"type": "uncertain_usage_not_traceable_without_provenance", "known_refs": sorted(uncertain_refs)})
        report["slides"][str(number)] = {"issues": issues, "unchecked": unchecked}
        if issues:
            report["status"] = "fail"

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "content-fidelity-report.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    issue_count = sum(len(s["issues"]) for s in report["slides"].values())
    unchecked_count = sum(len(s["unchecked"]) for s in report["slides"].values())
    print(f"[content-fidelity] {report['status']}: {issue_count} issue(s), {unchecked_count} unchecked item(s) -> {out_path}")
    return 1 if issue_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
