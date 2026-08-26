---
name: content-grouping
description: material-analysis의 Content Group → Subtopic → Evidence 계층을 의미적 관계 기준으로 재판단해 슬라이드 병합/유지/분할을 결정하고, Source Material Mapping과 Coverage Check 결과를 생성한다. content-designer가 워크플로우 [3]에서 material-analysis 이후, slide-content-structuring 이전에 사용한다.
---

# content-grouping

## 언제 사용하는가
content-designer가 [3] 슬라이드 구성 설계 단계에 진입했을 때 — `material-analysis`([2])가 만든 `material_analysis.json` 산출 직후, `slide-content-structuring`을 호출하기 전에 사용한다.

## 역할과 범위
이 Skill은 **슬라이드 경계를 정하는 판단 Skill**이다 — "무엇을 같은 슬라이드에 배치할지, 몇 장으로 나눌지"만 결정한다. 그 경계 안에서 Claim/Evidence/Relationship을 분석하거나 Required/Optional을 확정하는 일, Content Role·Region·Layout을 정하는 일은 하지 않는다 — 전부 `slide-content-structuring`(1단계 이하)의 책임이며 여기서 중복 판단하지 않는다. HTML/CSS 생성도 하지 않는다.

material-analysis가 원본에서 실제로 확인 가능한 구조 신호(헤딩 스타일, 페이지 경계, 시트 경계 등)로 만든 Content Group/Subtopic 경계는 **원본 문서의 구조**를 보존한 것이지 **슬라이드 경계**가 아니다. 이 둘을 동일시하지 않는 것이 이 Skill이 존재하는 이유다.

## 입력
- `material_analysis.json` 경로 (Content Group → Subtopic → Evidence 계층 전체 — `evidence_manifest`가 포함되어 있으면(material-analysis 4-1) 아래 1~2단계에서 그 인덱스를 1차 참조로 사용한다)
- 청중 유형, 발표 언어, 발표 시간, 목표 슬라이드 수
- (선택) 레퍼런스 자료 경로 — 스토리라인 순서·구성 관례 참고용

## 처리 흐름

1. **원본 계층 전체 확인** — 아직 어떤 병합·분할 판단도 하지 않은 채, `material_analysis.json`의 모든 Content Group/Subtopic과 그 안의 `confirmed_text`/`metrics`/`tables`/`images_available`/`evidence_clusters`/`direct_evidence`, 그리고 `cross_group_ref`·`content_match_confidence`가 붙은 항목, 그리고 `production_directives[]`·`visual_placeholders[]`(Data Pending 자리 포함)를 빠짐없이 목록화한다. `unassigned_or_dropped_content[]`에 이미 제외 사유가 기록된 항목은 배정 대상에서 제외하되 그 사실을 유지한다.
   - **목록화 방식**: `evidence_manifest`가 있으면 이 목록화는 그 entry(`evidence_id`·`evidence_type`·`source_type`(text_box 등 세부 출처 구분 포함)·`summary`·`source_order`·`content_match_confidence`·`relation_confidence`·`cross_group_ref`·`data_pending`·`production_directive_refs`·`visual_placeholder_refs`)를 1차로 사용한다 — 이 시점에는 각 항목의 원문 전체를 다시 읽지 않는다. Manifest는 조회 인덱스일 뿐 정본이 아니다(material-analysis SKILL.md 참조) — `material_analysis.json`이 마지막 확정 이후 다시 수정됐는데 `build_evidence_manifest.py`가 재실행되지 않았다면 그 Manifest는 최신이 아니므로 신뢰하지 않고 원본 배열을 직접 읽어 목록화한다.

2. **의미 단위(Semantic Unit) 식별** — Content Group/Subtopic의 원본 경계와 무관하게, "하나의 완결된 메시지를 전달하는 데 필요한 최소 콘텐츠 집합"이 무엇인지 판단한다. 하나의 의미 단위는 Subtopic 하나보다 작을 수도(evidence_cluster 단위), Content Group 하나와 같을 수도, 여러 Content Group에 걸칠 수도 있다.
   - **원문 조회 시점**: 의미 단위 판단이 Manifest의 `summary`(최대 180자 절삭)만으로 명확하면 원문을 추가로 읽지 않는다. summary가 판단에 부족하거나(절삭으로 핵심이 잘림, 애매함) 아래 3단계 병합/분리 후보 신호 판단에 필요하면, 그 항목의 `canonical_ref`로 `material_analysis.json` 원문을 지연 조회한다 — 판단에 필요한 항목만 읽고 Content Group 전체를 다시 처음부터 읽지 않는다.

3. **병합/유지/분할 결정** — 식별된 의미 단위를 슬라이드로 매핑한다.
   - **제작 지시문 우선 적용**: 그 의미 단위에 속한 `production_directives` 중 `directive_type`이 `merge`/`split`/`order`(병합/분리/순서 관련)인 항목이 있으면, 아래 의미적 판단 신호보다 **그 지시를 우선 적용**한다(예: "A와 B를 한 페이지에"는 병합 신호로, "이 둘은 각각 다른 페이지로"는 분리 신호로 우선 반영). 지시가 서로 충돌하거나, 실제 콘텐츠 구조와 명백히 모순되거나, 필요한 정보가 없어 지금 판단할 수 없는 경우에만 임의로 따르지 않고 `needs_confirmation` 사유로 남긴다(판단 가능한 명확한 지시는 항상 자동 적용). 지시를 적용해 병합/분할을 결정했으면 4단계 근거 기록에 `production_directive_applied`로 어떤 지시(id)를 따랐는지 남긴다.
   - **함께 배치할 후보** (제작 지시문이 없거나 지시문이 명시하지 않는 부분에 한해, 아래 중 하나 이상 해당하면 병합을 검토한다):
     - 하나의 상위 메시지를 공동으로 구성
     - 문제와 해결
     - 원인과 결과
     - 개념과 이를 뒷받침하는 근거
     - 기술과 그 효과
     - 동일 대상의 서로 다른 측면
     - 함께 제시해야 의미가 완성되는 하위 주제
   - **분리할 후보** (아래 중 하나 이상 해당하면 분할을 검토한다):
     - 독립적인 핵심 메시지가 여러 개 존재
     - 서로 다른 목적의 내용이 혼재
     - 각각 독립적인 Evidence가 충분함
     - 한 슬라이드에 합치면 핵심 메시지가 불명확해짐
   - **항상 원문을 확인하는 경우(위험 항목)**: `cross_group_ref`가 있는 항목, `content_match_confidence: "uncertain"`인 항목, `production_directives`가 딸린 항목, `visual_placeholders`(Data Pending)가 딸린 항목은 Manifest summary만으로 병합/분할을 확정하지 않고 해당 항목의 원문을 반드시 `canonical_ref`로 확인한 뒤 판단한다.
   - **금지**: 원본 페이지가 같음 / Content Group이 같음 / 항목 수가 적음 / 공간이 남음 — 이런 이유만으로 병합하지 않는다. 반대로 하나의 Content Group이라는 이유만으로 반드시 한 슬라이드로 유지하지도 않는다.
   - 발표 시간·목표 슬라이드 수는 제약 조건으로 고려하되 위 의미적 판단보다 우선하지 않는다. 슬라이드 수가 부족하면 콘텐츠 요약·부록 이관을 먼저 검토하고, 의미적으로 분리해야 하는 내용을 억지로 합치지 않는다. 요약·부록 이관으로도 목표를 맞출 수 없으면 content-designer가 메인을 통해 사용자에게 알린다 — 임의로 강행하지 않는다.
   - `cross_group_ref`가 있는 항목(다른 Content Group, 예: 부록 성격의 보조 자료 섹션에서 가져오는 근거)은 이 단계에서 실제로 어느 슬라이드가 그 근거를 사용할지 확정한다.
   - `content_match_confidence: "uncertain"`인 이미지·근거는 슬라이드에 배정하더라도 uncertain 표시를 그대로 유지해 다음 단계(`slide-content-structuring` 1-b)에 전달한다 — 이 단계에서 임의로 confirmed로 격상하지 않는다.
   - `visual_placeholders`(`data_status: "data_pending"`)가 딸린 콘텐츠는 데이터가 없다는 이유로 배정에서 제외하거나 다른 콘텐츠에 흡수시켜 지우지 않는다 — 그 자리가 속한 의미 단위와 함께 그대로 슬라이드에 배정하고, 배정된 사실을 Source Material Mapping에 남긴다(자리 자체는 다음 단계가 유지한다).

4. **결정 근거 기록** — 각 병합·유지·분할 결정마다 3단계의 어떤 신호(제작 지시문 우선 적용 / 함께 배치 후보 / 분리 후보 중 무엇)에 해당해 그렇게 판단했는지 기록한다. 근거 없는 병합·분할은 남기지 않는다.

5. **Source Material Mapping 생성** — 슬라이드별로 배정된 Content Group/Subtopic/evidence_cluster ID, 결정 유형(병합/유지/분할), 근거를 아래 출력 스키마에 따라 `/output/{project-name}/slide_composition_map.json`에 기록한다.

6. **Coverage Check** — Mapping이 완성되면 `material_analysis.json`과 다시 대조해 아래를 확인한다.
   - 중요한 Content Group/Subtopic이 어느 슬라이드에도 배정되지 않았는지
   - 하나의 상위 메시지를 구성하는 내용이 이유 없이 분리되지 않았는지
   - 서로 다른 주제가 부적절하게 한 슬라이드에 섞이지 않았는지
   - 일부 Evidence(metrics/tables/images_available/evidence_clusters)가 슬라이드 배정 과정에서 유실되지 않았는지
   - `cross_group_ref`가 사용됐다면 출처 Group과 실제 사용 Slide를 추적할 수 있는지
   - `content_match_confidence: "uncertain"` Evidence가 확정 Evidence처럼 취급되지 않았는지
   - `visual_placeholders`(Data Pending)가 슬라이드 배정 과정에서 삭제되거나 조용히 누락되지 않았는지
   - 제작 지시문(`production_directives`) 중 병합/분리/순서 지시가 있었다면 실제 결정에 반영됐는지, 반영하지 못했다면(충돌·모순·판단 불가) `needs_confirmation`으로 남아있는지
   - 문제가 발견되면 3단계로 돌아가 재조정한다(자동 1회). 재조정 후에도 해결되지 않으면 CLAUDE.md §4 "실패/에스컬레이션 처리 원칙"을 따른다 — 핵심 메시지의 근거가 유실된 경우는 즉시 작업을 멈추고 메인을 통해 사용자에게 확인을 요청하고, 부가적인 문제는 `coverage_check.issues_found[]`에 남긴 채 다음 단계로 진행한다.
   - 결과는 `slide_composition_map.json`의 `coverage_check` 항목에 기록한다.

7. **`slide_composition_map.json` 확정** — Coverage Check까지 통과한(또는 남은 이슈를 기록한) 최종 결과를 저장한다.

## 출력 스키마 (`slide_composition_map.json`)

```json
{
  "project": "...",
  "slides": [
    {
      "slide_number": 1,
      "working_title": "...",
      "source_material": [
        {"id": "CG02", "scope": "entire"},
        {"id": "CG03-ST01-EC1", "scope": "partial", "parent": "CG03-ST01"}
      ],
      "decision": "merge | keep | split",
      "rationale": "3단계 신호 중 해당하는 것과 구체적 판단 근거",
      "production_directive_applied": ["병합/분리/순서 판단에 실제로 우선 적용된 production_directive id (없으면 빈 배열)"],
      "cross_group_ref_resolved": [
        {"content_id": "예: CG23-ST08의 이미지 하나", "source_group": "CG23", "used_in_slide": 1}
      ],
      "uncertain_evidence_carried": ["여기 배정됐지만 아직 content_match_confidence: uncertain인 근거 ID"],
      "data_pending_carried": ["여기 배정된 visual_placeholder 중 data_status: data_pending인 항목 ID"]
    }
  ],
  "coverage_check": {
    "unassigned_content_groups": [],
    "unassigned_subtopics": [],
    "evidence_reconciliation": [
      {"source_id": "CG02-ST02", "source_count": 5, "mapped_count": 5, "match": true}
    ],
    "cross_group_ref_trace_complete": true,
    "uncertain_evidence_flagged": ["..."],
    "data_pending_flagged": ["슬라이드에 배정됐지만 아직 data_status: data_pending인 visual_placeholder ID"],
    "unresolved_production_directives": ["충돌·모순·판단 불가로 이번 단계에서 적용하지 못하고 needs_confirmation으로 남긴 production_directive id"],
    "issues_found": [],
    "status": "pass | issues_resolved | escalated"
  }
}
```

이 스키마는 `slide-content-structuring`이 소비하는 입력이다. 이후 단계는 여기 기록된 슬라이드 경계·Source Material 배정을 다시 판단하지 않고, 그 배정에 해당하는 `material_analysis.json`의 실제 내용을 바탕으로 Claim/Evidence/Relationship·Content Role·Region·Layout을 판단한다.

## 하지 않는 것
- Claim/Evidence/Relationship 분석, Required/Optional 확정, Content Role(Primary/Dependent/Shared Supporting/Conclusion) 분류, Content Region 설계, Layout 선택 → `slide-content-structuring` 담당
- Visual Type(Chart/Table/Diagram/Image/Text 등) 확정, HTML/CSS 생성 → `web-ppt-generator` 담당
- 원본에 없는 근거·관계를 새로 만드는 것 — 여기서 판단하는 것은 항상 원본에 이미 존재하는 콘텐츠를 어떻게 슬라이드로 묶을지이지, 새 콘텐츠를 만드는 것이 아니다.
- `material_analysis.json`을 만드는 방식(구조 신호 추출 등) 자체 — `material-analysis` 담당, 이 Skill은 그 산출물을 입력으로만 받는다.

## 판단 기준
- 3단계의 병합/분리 신호는 콘텐츠 형식·업종과 무관한 일반 원칙이며, 특정 프로젝트의 가변 규칙(`design-rules.md`)이나 레퍼런스 스타일을 참조하지 않는다 — 어떤 입력 자료(회사소개서/IR/사업계획서/기술소개서 등)에도 동일하게 적용한다.
- 발표 시간·목표 슬라이드 수 제약과 사용자 에스컬레이션 원칙: `CLAUDE.md` §4 "실패/에스컬레이션 처리 원칙"

## 향후 보완 여지
이번 버전은 최소 골격이다. 의미 단위 판단(2단계)의 구체적 임계치(예: "충분한 독립적 Evidence"의 기준)는 아직 정성적 판단에 의존하며, 실제 프로젝트에서 반복 사용하며 필요 시 보완한다.
