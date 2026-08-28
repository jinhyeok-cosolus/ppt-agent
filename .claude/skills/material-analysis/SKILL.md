---
name: material-analysis
description: 원본 자료(docx/pdf/xlsx/csv/이미지)에서 텍스트·표·차트·이미지를 추출하고, 원본에 존재하는 상위 주제-하위 주제-근거 계층을 보존해 Content Group 구조로 정리한다. content-designer가 워크플로우 [2] 자료 분석 단계에서 사용한다.
---

# material-analysis

## 언제 사용하는가
content-designer가 [2] 자료 분석 단계에 진입했을 때. 원본 자료 파일 경로 목록을 입력받아 `material_analysis.json`을 만든다.

## 이 개정의 목적 (2026-08-19)
이전 버전은 원본의 텍스트·표·이미지를 슬라이드/파일 단위의 flat한 배열(`confirmed_text[]`, `images_available[]`)로만 정리했다. 이 방식은 **원본에 실제로 존재하던 "무엇이 어느 상위 주제 아래에 속하는가"라는 계층 정보를 이 단계에서 이미 지워버린다** — 그 결과 이후 [3] `content-designer`/`slide-structuring` 단계는 이미 평평해진 텍스트 뭉치에서 계층을 다시 추측해야 했고, 어떤 근거가 어떤 하위 주제를 뒷받침하는지, 어떤 이미지가 어떤 설명과 실제로 짝지어지는지가 구조적으로 보장되지 않았다(회귀 테스트 cosolus-ir-deck-D에서 이미지 라벨 오류·근거 뭉뚱그림으로 반복 확인됨).

이번 개정은 **원본에서 실제로 확인 가능한 구조 신호가 있을 때만** 그 신호를 그대로 살려 `Content Group → Subtopic → Evidence` 계층으로 추출한다. 확인할 수 없는 계층·관계는 추정해서 만들지 않는다 — 신호가 없으면 `structure_signal: "none_detected"`로 명시하고 flat 구조로 남긴다.

이 개정은 **material-analysis([2])까지만** 적용된다. `slide-structuring`의 Phase A 슬라이드 병합/분할 판단과 Phase B의 Claim→Evidence→Relationship 판단(1-b)은 이 문서의 범위가 아니며 수정하지 않았다 — 이 둘은 이제 더 풍부하고 계층이 보존된 입력을 받게 될 뿐, 그 자체의 판단 로직은 그대로다.

## 처리 흐름

### 1. 기계적 추출 (`scripts/extract.py`)
형식별로 **원본에서 실제로 확인 가능한 구조 신호**를 이용해 `Content Group → Subtopic` 골격과 그 안에 속한 문단/표/이미지를 추출한다. 신호는 형식마다 다르며, 하나의 신호(예: 특정 Word 스타일 이름 하나)에만 의존하지 않는다:

| 형식 | 1차 구조 신호 | 신뢰도 |
|---|---|---|
| docx | 문단 스타일 이름의 "Heading N"/"제목 N" 패턴(영문·국문 템플릿 모두 인식) — 가장 얕은 헤딩 레벨이 Content Group 경계, 그 다음 깊이가 Subtopic 경계 | 확정 신호(문서 자체가 명시한 구조) |
| pdf | 페이지 경계(항상 사용 가능, Content Group 경계로 사용) | 확정 신호 |
| pdf | 페이지 내 폰트 크기 이상치(본문 대비 눈에 띄게 큰 줄) → Subtopic 후보 | **휴리스틱** — `signal_detail: "font_size_heuristic"`로 명시, 확정 신호로 취급하지 않음 |
| xlsx | 시트 경계 | 확정 신호 |
| csv / 단일 이미지 파일 | 없음 | `structure_signal: "none_detected"` — 계층을 임의로 만들지 않음 |

- docx는 `document.xml` body를 실제 XML 순서 그대로(문단·표가 섞인 원래 순서) 순회한다 — `document.paragraphs`/`document.tables`처럼 종류별로 나뉜 컬렉션을 따로 순회하면 "이 표/이미지가 어느 제목 바로 다음에 있었는가"라는 인접성 정보 자체가 사라지기 때문이다.
- 이미지 relationship id는 문서 순서대로(`doc.part.rels` 딕셔너리 순서가 아니라 실제로 문단에 등장하는 순서로) 추출한다. **이전 버전은 `doc.part.rels` 순회로 이미지를 뽑아 실제 문서 순서와 어긋날 수 있었고, cosolus-ir-deck-D 회귀 테스트에서 실제로 로고 이미지가 한 칸씩 밀려 매칭되는 결함(SWAP/MUKTI/eCoNiL/IBC/HLI)의 원인이었다.** 이번 개정으로 이 결함 유형은 구조적으로 해소된다.
- 변환 도구(PPT→docx 등)가 이미지 한 장을 셀 1개짜리 표로 감싸는 경우가 흔하다(cosolus 원본 문서에서 실제로 확인됨). 모든 셀의 텍스트가 비어 있는 표는 "이미지 컨테이너"로 판단해 표가 아니라 이미지로 추출한다 — 그렇지 않으면 이미지가 빈 표로 오분류되어 유실된다.
- 상세 데이터 표(수십 행 이상, `needs_appendix: true`)는 추출 단계에서 걸러내지 않는다(선별은 [3] 이후 담당).
- 스캔 PDF(텍스트 레이어 없음) 등 자동 판독 불가 시 OCR을 임의로 시도하지 않고 `needs_manual_review: true`로 표시한다.
- 원본에 구조 신호가 전혀 없으면(`structure_signal: "none_detected"`) `needs_confirmation`에 "이 파일은 구조 신호가 없어 이후 단계가 주제 그룹핑을 수동 판단에 의존하게 됨"을 자동 기록한다(스크립트가 자동으로 남김 — LLM이 뒤늦게 발견하는 게 아니라 추출 시점에 바로 드러나도록).

```bash
python .claude/skills/material-analysis/scripts/extract.py \
  --input <원본파일 또는 폴더> \
  --output /output/{project-name}/material_analysis.json
```

### 2. 의미 구조화 (LLM)
1번의 기계적 추출 결과(raw, `content_groups[] → subtopics[] → {text_blocks, tables, images}`)를 LLM이 검토해 최종 `material_analysis.json`(아래 출력 스키마)을 작성한다. 이 단계에서 하는 일은 **1번이 이미 확정한 Content Group/Subtopic 경계를 재해석하지 않고**, 그 안에서:

- **Evidence 식별**: 각 Subtopic의 본문 텍스트에서 수치·KPI·주장을 뽑아 `metrics[]`로 정리한다. 수치는 원본 값을 그대로 사용 — 재계산·추정 금지.
- **텍스트 출처 메타데이터 보존**: `confirmed_text`의 기존 문자열 배열은 호환성을 위해 유지하되, raw의 각 텍스트 블록 순서와 `source_type`(특히 `text_box`)을 `text_evidence_metadata[]`에 `text_index`(1부터 시작), `source_order`, `source_type`으로 함께 기록한다. 원문 텍스트를 이 메타데이터에 복제하지 않는다.
- **표/이미지-주제 관계 확정**: 1번이 이미 구조적으로 소속을 확정한 표·이미지(같은 Subtopic 안에 있었던 것)는 `relation_confidence: "structural"`로 표시한다. **이미지·표의 소속 Subtopic은 1번의 문서 순서·인접성으로 이미 결정돼 있으므로 이 단계에서 다시 추정하지 않는다.**
- **이미지 검증 라우팅(구조 우선, Vision 보수적 승격)**: 이미지마다 먼저 기계 추출 결과와 인접 원문만으로 아래 **자동 structural 매핑 조건을 모두** 확인한다. 하나라도 확인할 수 없거나 애매하면 토큰 절약을 위해 추정하지 말고 반드시 Vision 검토 대상으로 보낸다.
  - Word/XML 문서 순서상 Content Group/Subtopic 소속이 명확하다.
  - 인접 캡션 또는 이미지 삽입/제작 지시문이 정확히 1개이며 이미지 1개와 1:1로 대응한다.
  - 같은 설명 구간에 다른 이미지 후보가 없고, 다른 Content Group 참조·재사용(`cross_group_ref`)이 없다.
  - 캡션/지시문이 사진·로고 등 비데이터 시각 자산임을 명시하며, 차트·그래프·표·도표·공정도처럼 이미지 내용을 읽어야만 수치·관계·주장이 성립하는 자산이 아니다.
  - 인접 텍스트만으로 그 이미지의 사용 목적과 주장 근거가 충분히 보존되고, 이미지 내용과 충돌할 합리적 징후가 없다.
  - 모든 조건을 만족하면 이미지를 열어 보지 않고 `content_match_confidence: "structural"`로 기록한다. 이는 **구조적 소속과 1:1 대응이 확인됐음**을 뜻하며, 이미지의 시각적 내용을 LLM이 확정했다는 뜻은 아니다.
  - 위 조건 중 하나라도 불명확하면 LLM이 이미지를 직접 검토한다. 구조적 소속이 불명확함, 캡션/지시문 부재·모호성, 다수 이미지-다수 설명 관계, 다른 Group 참조·재사용, 차트/그래프/표/도표, 인접 텍스트와의 충돌 가능성은 모두 Vision 검토 사유다. Vision으로 일치가 분명하면 `content_match_confidence: "confirmed"`, 판단이 어렵거나 어긋나 보이면 **임의로 확정하지 말고 `content_match_confidence: "uncertain"`으로 표시**한다.
- **Content Group 간 참조**: 어느 Subtopic의 Evidence가 다른 Content Group(예: 별도 부록/보조자료 섹션)에서 가져온 것이면, 그 사실을 `cross_group_ref`로 명시한다 — 구조적으로 다른 곳에 있던 자료를 이 Subtopic에 슬쩍 섞어 넣지 않는다.
- **출처/각주 연결**: 원문에서 특정 수치·서술 바로 옆에 출처 표기가 있으면 그 Evidence 항목에 직접 `source_citation`으로 붙인다. 출처가 Content Group 전체에 걸쳐 있고 특정 Evidence를 콕 집어 가리키지 않으면 Group 레벨 `source_citation`으로 남긴다 — 근거 하나하나에 억지로 짝짓지 않는다.
- **누락/제외 추적**: 1번의 원재료 중 최종 구조에 반영하지 못한 내용(예: 원본 레이아웃 유실로 재구성 불가능한 표, 캡션 없어 매칭 불가능한 인물 사진)이 있으면 버리지 말고 `unassigned_or_dropped_content[]`에 사유와 함께 남긴다.
- **제작 지시문 식별·분리**: 원본 문서에는 실제 슬라이드 콘텐츠(사실·수치·주장)와 문서 작성자가 남긴 제작/편집 지시문이 섞여 있을 수 있다(예: "프롬프트:", "제작 지시:", "배치:", "표로 구성", "이미지와 함께 배치", "~해줘", "~할 것" 같은 marker나 2인칭 명령형으로 대상 구성·배치·표현 방식을 지시하는 문장). LLM이 이 단계에서 각 문장이 (a) 실제 콘텐츠인지 (b) 콘텐츠의 구성·배치·표현 방식에 대한 지시인지 자동 판별한다 — 사람이 사전 분류할 필요 없다.
  - 지시문으로 판별된 문장은 `confirmed_text`에 섞어 넣지 않고, 해당 Subtopic(또는 `direct_evidence`)의 `production_directives[]`에 원문 그대로 별도 보존한다(삭제 금지, 최종 슬라이드 본문 텍스트로 출력되지 않도록 콘텐츠 배열과 분리만 한다).
  - 판별이 애매한 경우(지시문인지 실제 콘텐츠인지 확신할 수 없는 경우)는 임의로 한쪽으로 단정하지 않고 `confirmed_text`에 남긴 채 `needs_confirmation`에 사유를 기록한다.
  - 이 필드의 우선 적용(병합/분리/배치 판단에 지시 내용을 우선 반영하는 것)은 이 스킬의 책임이 아니다 — `slide-structuring`의 Phase A(그룹핑)와 Phase B(1-b/4/5)가 소비 주체이며, 해당 스킬 문서에 소비 방식이 명시돼 있다. 이 스킬은 지시문을 유실 없이 식별·보존해 넘기는 데까지만 책임진다.
- **Data Pending 처리(차트/표 삽입 지시는 있으나 데이터 자체가 없음)**: 원본에 "차트 삽입 예정", "표 삽입 예정" 같은 지시(위 `production_directives`로 분류됨)만 있고 그 차트/표가 담아야 할 수치 데이터 자체가 원본 어디에도 없는 경우, 그 자리를 삭제하거나 일반 텍스트로 뭉뚱그려 대체하지 않는다 — 나중에 실제 데이터가 채워질 자리로 보고 구조를 유지한다.
  - 해당 Subtopic(또는 `direct_evidence`)의 `visual_placeholders[]`에 `data_status: "data_pending"`으로 명시적으로 기록한다(아래 스키마 참조). 눈대중으로 값을 추정해 채우지 않는다.
  - 이 Data Pending 근거가 핵심 주장(발표 논거)을 뒷받침하는 자리이면 `escalations`에도 함께 기록해 즉시 후속 작업을 중단하고 사용자 확인을 받는다(아래 참조). 부가적인 자리이면 `needs_confirmation`에만 기록하고 계속 진행한다.
- 수치·실험 결과·기술적 의미는 원본을 그대로 반영하며 임의로 생성·추정하지 않는다(기존 원칙 유지).
  - 핵심 수치(발표 주장의 근거)를 확인할 수 없으면 → `escalations`에 기록하고 **즉시 이 수치를 다루는 후속 작업을 중단**, content-designer가 메인에게 보고.
  - 부가 수치를 확인할 수 없으면 → `needs_confirmation`에 기록하고 나머지 작업은 계속 진행.
  - 차트 원본 수치를 추출할 수 없는 경우는 두 가지를 구분해서 기록한다(둘 다 눈대중 추정으로 새 차트를 만들지 않는다는 원칙은 동일):
    - **이미 존재하는 차트/표에서 수치를 못 읽어내는 경우**(스캔 손상, 이미지 해상도 부족 등) → 해당 항목을 `escalations`(핵심 근거) 또는 `needs_confirmation`(부가 근거)에 `type: "core_claim_extraction_failed"`로 기록하고, 원본 차트 이미지를 그대로 슬라이드에 활용하는 방향을 권장한다.
    - **차트/표를 만들라는 지시만 있고 데이터 자체가 원본에 없는 경우** → 위 "Data Pending 처리" 절차를 따르고, `escalations`/`needs_confirmation`에는 `type: "core_claim_data_missing"`으로 기록한다. 이 둘은 원인이 다르므로(추출 실패 vs 데이터 미제공) 같은 유형으로 뭉뚱그리지 않는다.
- 자기 검증: 최종 구조를 원본과 재대조해 텍스트·수치·이미지 개수가 1번의 raw 추출과 어긋나지 않는지 확인한다(예: 어느 Subtopic이 "이미지 4개"라는 제목을 달고 있는데 실제로는 3개만 옮겨졌다면 재확인). 제작 지시문이 `confirmed_text`에 섞여 남아있지 않은지도 함께 확인한다.

### 3. Evidence Manifest 생성 (결정론적 후처리)
LLM이 최종 `material_analysis.json`을 작성한 뒤, 아래 스크립트를 **한 번** 실행해 정본 내부의 `evidence_manifest`를 생성한다. 이 Manifest는 조회 최적화용 인덱스이며, 원문·상태·수치의 정본은 항상 같은 파일의 기존 Content Group/Subtopic/Evidence 필드다.

```bash
python .claude/skills/material-analysis/scripts/build_evidence_manifest.py \
  --input /output/{project-name}/material_analysis.json
```

- 스크립트는 정본에서 Manifest 자체를 제외한 콘텐츠의 SHA-256을 `canonical_content_sha256`으로 기록한다. 해시가 다르면 Manifest를 독립 정본으로 사용하지 말고 다시 생성한다.
- Evidence ID는 `CGxx[-STxx]-(TXT|MET|TBL|IMG|SRC|PD|VP)xx` 형식으로, Content Group/Subtopic 위치와 해당 배열의 원본 순서로 결정론적으로 만든다. 기존 필드의 표현을 바꾸지 않으며 ID와 정본 위치는 Manifest의 `evidence_id`/`canonical_ref`로 연결한다.
- 모든 entry에는 Evidence 유형·짧은 요약·원본 순서·출처 참조·상태를 기록한다. `text_box`, `structural|confirmed|uncertain`, `cross_group_ref`, Data Pending, production directive, visual placeholder 참조는 축약·누락하지 않는다.

## "원문 그대로 반영" 원칙의 적용 범위
위 원칙들이 말하는 "원문 그대로"는 **콘텐츠(수치·사실·관계·제작 의도)**에 대한 것이지, **원본 표·도식·그림의 시각적 디자인·배치**를 그대로 복제하라는 뜻이 아니다.
- 원본의 표/도식/그림(레이아웃, 색상, 셀 배치, 아이콘 형태 등)은 이 단계에서 콘텐츠·데이터·관계·제작 의도를 파악하는 **근거로만** 사용한다.
- 실제 슬라이드에서 이를 어떻게 시각적으로 표현할지는 이 스킬의 책임이 아니며, 항상 이후 단계가 확정하는 Hard Rule/Claude PPT Design System/Content Visualization Freedom/Layout Reference를 따라 새로 구현된다(`slide-structuring`(Phase B)의 Layout Routing, `web-ppt-generator`의 실제 구현).
- 원본 자체의 결함(표의 레이블-데이터 불일치, 도식 내 빈 placeholder 등)을 이 단계에서 임의로 추정해 채우지 않는다는 원칙(콘텐츠 보존 원칙)과, 원본의 시각 디자인을 복제하지 않는다는 원칙(표현 방식 원칙)은 서로 다른 층위이며 둘 다 지킨다.

## 출력 스키마 (`material_analysis.json`)

```json
{
  "project": "...",
  "source_file": "...",
  "extraction_note": "...",
  "content_groups": [
    {
      "id": "CG01",
      "title": "...",
      "structure_signal": {"type": "heading_style|page_boundary|font_size_heuristic|sheet_boundary|none_detected", "detail": "예: Heading 1, Page 3"},
      "subtopics": [
        {
          "id": "CG01-ST01",
          "title": "...",
          "structure_signal": {"type": "...", "detail": "..."},
          "confirmed_text": ["...", "..."],
          "text_evidence_metadata": [
            {"text_index": 1, "source_order": 1, "source_type": "text"}
          ],
          "metrics": [
            {"label": "...", "value": "...", "source_citation": "있으면 기재, 없으면 null"}
          ],
          "tables": [
            {"table_ref": "table_1", "headers": [...], "rows": [...], "needs_appendix": false, "relation_confidence": "structural"}
          ],
          "images_available": [
            {
              "ref": "img3",
              "path": "...",
              "description": "구조적 1:1 매핑 근거 또는 Vision 검토로 확인한 내용",
              "relation_confidence": "structural",
              "content_match_confidence": "structural|confirmed|uncertain",
              "cross_group_ref": null
            }
          ],
          "production_directives": [
            {
              "id": "CG01-ST01-PD01",
              "raw_text": "원문 그대로 (예: \"프롬프트: 다음 내용을 3 BOX 구조로 만들고, 내용에 맞는 아이콘 삽입\")",
              "directive_type": "merge|split|order|placement|visualization|emphasis|other",
              "target_scope": "이 지시가 적용되는 대상 (예: 이 Subtopic 전체, 특정 evidence/문단)",
              "applicability": "auto_applicable|ambiguous"
            }
          ],
          "visual_placeholders": [
            {
              "id": "CG01-ST01-VP1",
              "instructed_visual_type": "table|chart|diagram",
              "intended_subject": "지시문/문맥상 이 자리가 다뤄야 할 주제 (예: 글로벌 양극재(리튬) 수요-공급 전망)",
              "data_status": "data_pending",
              "production_directive_ref": "CG01-ST01-PD01",
              "note": "원본에 제목만 있고 수치 데이터가 없음 등 구체적 상태"
            }
          ],
          "source_citation": "이 Subtopic 전체에 걸리는 출처가 있으면 기재"
        }
      ],
      "direct_evidence": {
        "confirmed_text": [], "metrics": [], "tables": [], "images_available": [],
        "production_directives": [], "visual_placeholders": []
      }
    }
  ],
  "unassigned_or_dropped_content": [
    {"content": "...", "reason": "...", "source_location": "CG10"}
  ],
  "escalations": [
    {"id": "ESC-01", "type": "core_claim_data_missing|core_claim_extraction_failed|other", "detail": "...", "source": "CG04"}
  ],
  "needs_confirmation": [
    {"id": "NC-01", "detail": "...", "source": "CG04"}
  ],
  "evidence_manifest": {
    "manifest_version": "1.0",
    "canonical_content_sha256": "...",
    "non_authoritative": true,
    "evidence_count": 0,
    "entries": [
      {"evidence_id": "CG01-ST01-TXT01", "canonical_ref": "/content_groups/0/subtopics/0/confirmed_text/0", "evidence_type": "text"}
    ]
  }
}
```

### 기존 스키마와의 호환성
- `confirmed_text`, `images_available`, `source_citation`, `escalations`, `needs_confirmation` **필드 이름은 그대로 유지**한다 — 다만 이전에는 Content Bundle(=슬라이드 후보) 레벨의 flat 배열이었던 것을, 이번에는 **Subtopic 레벨**로 한 단계 더 들어가 배치한다. 기존에 이 필드들을 읽던 판단(slide-structuring Phase A의 슬라이드 분할, Phase B의 1-b)은 필드 이름이 같으므로 계속 읽을 수 있으며, 이제 그 필드들이 어느 상위 Content Group의 어느 Subtopic에 속하는지도 함께 알 수 있다.
- Content Group 자체는 기존 "Content Bundle"(B01~B22 형태)과 대응한다 — 다만 이번에는 `structure_signal`로 그 경계가 실제 원본의 어떤 신호에 근거했는지(추정이 아닌지)를 함께 기록한다.
- `direct_evidence`는 Subtopic 헤딩 없이 Content Group 헤딩 바로 아래에 본문이 오는 경우(원본에 하위 제목이 없는 경우)를 위한 필드다 — 이 경우 억지로 Subtopic을 만들지 않는다.
- `production_directives`/`visual_placeholders`는 이번 개정에서 새로 추가된 필드다. 지시문이나 Data Pending 자리가 없는 Subtopic은 빈 배열로 둔다 — 기존에 이 필드를 모르는 소비자가 있더라도(빈 배열이므로) 동작에 영향이 없다. `escalations`의 `type`도 이번에 새로 명시했으며, 기존에 `type` 없이 `{id, detail, source}`만 쓰던 방식과도 호환된다(`type`이 없으면 `other`로 간주).

## 하지 않는 것
- 원본에 없는 상위 주제-하위 주제 관계를 추정해서 만들지 않는다. 구조 신호가 없으면 `structure_signal: "none_detected"`로 명시하고 flat하게 둔다.
- Subtopic보다 더 깊은 원본 계층(예: docx의 3번째 헤딩 레벨)은 별도 3번째 구조 레이어로 만들지 않는다 — 해당 Subtopic의 `confirmed_text` 안에 `[하위 제목]` 형태로 유실 없이 남긴다(향후 필요성이 확인되면 계층을 확장할 수 있다).
- 이미지·표가 "어느 Subtopic에 속하는가"(구조적 소속)는 1번(기계적 추출)이 이미 확정하며, 2번(LLM)이 이를 다시 추정하지 않는다. 이미지는 위 자동 structural 매핑 조건을 모두 만족할 때만 시각 검토 없이 `content_match_confidence: structural`로 보존하고, 그 외에는 Vision으로 내용-설명 일치 여부를 판단한다. 불확실한 이미지를 structural로 격상하지 않는다.
- 슬라이드 분할·병합, Claim/Evidence/Relationship 분류, Layout 선택은 이 스킬의 범위가 아니다 — 각각 `slide-structuring`의 Phase A / Phase B(1-b) / Phase B Layout Routing이 담당한다. 이 스킬은 그 판단들이 딛고 설 **계층이 보존된 입력**을 만드는 데까지만 책임진다.
- `production_directives`에 담긴 배치·구성 의도를 실제로 어떻게 적용할지(병합/분리/좌우 배치 등)는 이 스킬이 판단하지 않는다 — 식별·보존만 하며, 적용은 `slide-structuring`(Phase A/Phase B)이 담당한다.
- `visual_placeholders`(Data Pending)에 눈대중 수치나 가짜 그래프를 채워 넣지 않는다 — 데이터가 실제로 확보되기 전까지는 항상 `data_status: "data_pending"`으로 남긴다.

## 스크립트 사용법

```bash
python .claude/skills/material-analysis/scripts/extract.py \
  --input <원본파일 또는 폴더> \
  --output /output/{project-name}/material_analysis.json
```

- 여러 파일을 한 번에 넘기면 파일별 결과가 `sources` 배열에 누적된다(각 소스가 위 `content_groups` 구조를 가진다 — main() 레벨 래퍼는 `{"sources": [...], "escalations": [...], "needs_confirmation": [...]}`이며, 2단계 LLM이 이를 읽어 최종 `material_analysis.json`의 통합된 `content_groups[]`로 재정리한다).
- docx: `document.xml` body를 순서대로 순회해 헤딩 스타일로 Content Group/Subtopic 경계를 잡고, 문단/표/이미지를 그 경계 안에 순서대로 배치. 이미지 1장을 담은 셀-표는 표가 아닌 이미지로 처리.
- pdf: 페이지 경계를 Content Group으로, 폰트 크기 이상치를 Subtopic 후보로(휴리스틱, 확정 아님) 사용.
- xlsx/csv: 시트/파일을 Content Group으로. 임베드 차트는 "차트 감지됨 — 원본 수치 추출 불가"로만 표시.
- 이미지: 파일 경로만 등록(내용 판단은 2단계 LLM이 이미지를 직접 보고 수행).

## references
- `references/` : 형식별 파싱 시 주의사항(병합 셀, 각주, 다단 레이아웃 등)을 프로젝트 경험이 쌓이며 축적하는 공간. 현재는 비어 있음.
- 이번 개정은 `cosolus-ir-deck-D` 원본 docx에 새 extract.py를 재실행하는 회귀 테스트로 검증됐다(기존 프로젝트 산출물은 건드리지 않음). 검증에 쓰인 임시 산출물(`output/_material-analysis-regression/`)은 용량 정리 차원에서 삭제됐으며, 이 개정 배경은 위 "이 개정의 목적" 절에 그대로 남아 있다.
