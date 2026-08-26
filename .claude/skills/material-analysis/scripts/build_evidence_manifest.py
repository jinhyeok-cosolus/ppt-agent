"""Build a deterministic, non-authoritative Evidence Manifest.

The manifest is embedded in material_analysis.json for cheap downstream
lookup.  The rest of that file remains the canonical source of truth.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


MANIFEST_KEY = "evidence_manifest"
MANIFEST_VERSION = "1.0"


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _summary(value: Any, limit: int = 180) -> str:
    if isinstance(value, dict):
        value = value.get("title") or value.get("label") or value.get("description") or value.get("text") or ""
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else ([] if value is None else [value])


def _citation(container: dict[str, Any], group: dict[str, Any]) -> Any:
    return container.get("source_citation", group.get("source_citation"))


def _text_metadata(container: dict[str, Any]) -> list[dict[str, Any]]:
    metadata = container.get("text_evidence_metadata", [])
    return metadata if isinstance(metadata, list) else []


def _metadata_for_text(metadata: list[dict[str, Any]], index: int) -> dict[str, Any]:
    for item in metadata:
        if isinstance(item, dict) and item.get("text_index") == index:
            return item
    return {}


def _entry(
    evidence_id: str,
    group_id: str,
    subtopic_id: str | None,
    source_order: int,
    evidence_type: str,
    summary: Any,
    canonical_ref: str,
    *,
    source_ref: Any = None,
    source_type: str | None = None,
    content_match_confidence: str | None = None,
    relation_confidence: str | None = None,
    cross_group_ref: Any = None,
    data_pending: bool = False,
    production_directive_refs: list[str] | None = None,
    visual_placeholder_refs: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "evidence_id": evidence_id,
        "group_id": group_id,
        "subtopic_id": subtopic_id,
        "source_order": source_order,
        "evidence_type": evidence_type,
        "summary": _summary(summary),
        "canonical_ref": canonical_ref,
        "source_ref": source_ref,
        "source_type": source_type,
        "content_match_confidence": content_match_confidence,
        "relation_confidence": relation_confidence,
        "cross_group_ref": cross_group_ref,
        "data_pending": data_pending,
        "production_directive_refs": production_directive_refs or [],
        "visual_placeholder_refs": visual_placeholder_refs or [],
    }


def _container_entries(
    container: dict[str, Any],
    group: dict[str, Any],
    group_id: str,
    subtopic_id: str | None,
    canonical_ref: str,
) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    metadata = _text_metadata(container)
    directive_refs = [f"{subtopic_id or group_id}-PD{i:02d}" for i, _ in enumerate(_as_list(container.get("production_directives")), 1)]
    placeholder_refs = [f"{subtopic_id or group_id}-VP{i:02d}" for i, _ in enumerate(_as_list(container.get("visual_placeholders")), 1)]
    citation = _citation(container, group)
    prefix = subtopic_id or group_id

    for i, item in enumerate(_as_list(container.get("confirmed_text")), 1):
        item_dict = item if isinstance(item, dict) else {}
        meta = _metadata_for_text(metadata, i)
        entries.append(_entry(
            f"{prefix}-TXT{i:02d}", group_id, subtopic_id,
            int(meta.get("source_order", item_dict.get("order", i))), "text", item,
            f"{canonical_ref}/confirmed_text/{i - 1}", source_ref=citation,
            source_type=meta.get("source_type", item_dict.get("source_type", "text")),
            relation_confidence=item_dict.get("relation_confidence"),
            cross_group_ref=item_dict.get("cross_group_ref"),
            production_directive_refs=directive_refs, visual_placeholder_refs=placeholder_refs,
        ))

    for i, item in enumerate(_as_list(container.get("metrics")), 1):
        item_dict = item if isinstance(item, dict) else {}
        entries.append(_entry(
            f"{prefix}-MET{i:02d}", group_id, subtopic_id, int(item_dict.get("order", i)), "metric", item,
            f"{canonical_ref}/metrics/{i - 1}", source_ref=item_dict.get("source_citation", citation),
            source_type=item_dict.get("source_type"), relation_confidence=item_dict.get("relation_confidence"),
            cross_group_ref=item_dict.get("cross_group_ref"), production_directive_refs=directive_refs,
            visual_placeholder_refs=placeholder_refs,
        ))

    for i, item in enumerate(_as_list(container.get("tables")), 1):
        item_dict = item if isinstance(item, dict) else {}
        entries.append(_entry(
            f"{prefix}-TBL{i:02d}", group_id, subtopic_id, int(item_dict.get("order", i)), "table", item,
            f"{canonical_ref}/tables/{i - 1}", source_ref=item_dict.get("source_citation", citation),
            source_type=item_dict.get("source_type"), relation_confidence=item_dict.get("relation_confidence"),
            cross_group_ref=item_dict.get("cross_group_ref"), production_directive_refs=directive_refs,
            visual_placeholder_refs=placeholder_refs,
        ))

    for i, item in enumerate(_as_list(container.get("images_available")), 1):
        item_dict = item if isinstance(item, dict) else {}
        entries.append(_entry(
            f"{prefix}-IMG{i:02d}", group_id, subtopic_id, int(item_dict.get("order", i)), "image", item,
            f"{canonical_ref}/images_available/{i - 1}", source_ref=item_dict.get("path", citation),
            source_type=item_dict.get("source_type"),
            content_match_confidence=item_dict.get("content_match_confidence"),
            relation_confidence=item_dict.get("relation_confidence"),
            cross_group_ref=item_dict.get("cross_group_ref"), production_directive_refs=directive_refs,
            visual_placeholder_refs=placeholder_refs,
        ))

    for i, item in enumerate(_as_list(container.get("production_directives")), 1):
        item_dict = item if isinstance(item, dict) else {}
        entries.append(_entry(
            directive_refs[i - 1], group_id, subtopic_id, int(item_dict.get("order", i)), "production_directive", item,
            f"{canonical_ref}/production_directives/{i - 1}", source_ref=citation,
            source_type=item_dict.get("source_type"), cross_group_ref=item_dict.get("cross_group_ref"),
            production_directive_refs=[directive_refs[i - 1]], visual_placeholder_refs=placeholder_refs,
        ))

    for i, item in enumerate(_as_list(container.get("visual_placeholders")), 1):
        item_dict = item if isinstance(item, dict) else {}
        data_pending = item_dict.get("data_status") == "data_pending"
        entries.append(_entry(
            placeholder_refs[i - 1], group_id, subtopic_id, int(item_dict.get("order", i)), "visual_placeholder", item,
            f"{canonical_ref}/visual_placeholders/{i - 1}", source_ref=item_dict.get("source_citation", citation),
            source_type=item_dict.get("source_type"), relation_confidence=item_dict.get("relation_confidence"),
            cross_group_ref=item_dict.get("cross_group_ref"), data_pending=data_pending,
            production_directive_refs=directive_refs, visual_placeholder_refs=[placeholder_refs[i - 1]],
        ))

    for i, item in enumerate(_as_list(container.get("source_citation")), 1):
        entries.append(_entry(
            f"{prefix}-SRC{i:02d}", group_id, subtopic_id, i, "source_reference", item,
            f"{canonical_ref}/source_citation/{i - 1}", source_ref=item,
            production_directive_refs=directive_refs, visual_placeholder_refs=placeholder_refs,
        ))
    return entries


def build_manifest(document: dict[str, Any]) -> dict[str, Any]:
    canonical = copy.deepcopy(document)
    canonical.pop(MANIFEST_KEY, None)
    digest = hashlib.sha256(_canonical_json(canonical).encode("utf-8")).hexdigest()
    entries: list[dict[str, Any]] = []

    for g_idx, group in enumerate(_as_list(document.get("content_groups")), 1):
        if not isinstance(group, dict):
            continue
        group_id = str(group.get("id") or f"CG{g_idx:02d}")
        group_ref = f"/content_groups/{g_idx - 1}"
        for s_idx, subtopic in enumerate(_as_list(group.get("subtopics")), 1):
            if not isinstance(subtopic, dict):
                continue
            subtopic_id = str(subtopic.get("id") or f"{group_id}-ST{s_idx:02d}")
            entries.extend(_container_entries(subtopic, group, group_id, subtopic_id, f"{group_ref}/subtopics/{s_idx - 1}"))
        direct = group.get("direct_evidence")
        if isinstance(direct, dict):
            entries.extend(_container_entries(direct, group, group_id, None, f"{group_ref}/direct_evidence"))
        for c_idx, citation in enumerate(_as_list(group.get("source_citation")), 1):
            entries.append(_entry(
                f"{group_id}-SRC{c_idx:02d}", group_id, None, c_idx, "source_reference", citation,
                f"{group_ref}/source_citation/{c_idx - 1}", source_ref=citation,
            ))

    return {
        "manifest_version": MANIFEST_VERSION,
        "canonical_content_sha256": digest,
        "non_authoritative": True,
        "evidence_count": len(entries),
        "entries": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="material_analysis.json path; updated in place")
    args = parser.parse_args()
    path = Path(args.input)
    document = json.loads(path.read_text(encoding="utf-8"))
    document[MANIFEST_KEY] = build_manifest(document)
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
