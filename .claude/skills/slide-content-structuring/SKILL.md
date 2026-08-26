---
name: slide-content-structuring
description: 슬라이드 구성 설계 단계에서 콘텐츠의 핵심 메시지·역할·관계를 분석해 Content Region과 Layout을 판단하고 구조화된 slide_outline.md를 생성한다. content-designer가 워크플로우 [3]에서 material-analysis 이후, web-ppt-generator 이전에 사용한다.
---

# slide-content-structuring

## 언제 사용하는가
content-designer가 [3] 슬라이드 구성 설계 단계에서 `content-grouping`이 `slide_composition_map.json`으로 슬라이드 경계를 확정한 이후, `web-ppt-generator`([5])를 호출하기 전에 사용한다.

## 역할과 범위
이 Skill은 **판단 Skill**이다. 실제 웹PPT(HTML/CSS)를 디자인하거나 생성하지 않는다. 입력된 콘텐츠를 슬라이드 단위로 분석해 구조화된 `slide_outline.md`를 만드는 것까지가 책임 범위다. 실제 좌표·정렬·간격·타이포그래피 등 디자인 구현은 `web-ppt-generator`가 담당한다.

Hard Rule / Claude PPT Design System / Content Visualization Freedom / Layout Reference의 세부 규칙은 이 문서에 복사하지 않는다 — 판단이 필요할 때 항상 원본 문서를 직접 참조한다.

## 입력
- `material_analysis.json` 경로 (`evidence_manifest`가 포함되어 있으면(material-analysis 4-1) 아래 1/1-b/1-c 단계에서 그 인덱스를 1차 참조로 사용한다)
- `slide_composition_map.json` 경로 — `content-grouping` 스킬이 이미 확정한 슬라이드 경계(각 슬라이드에 배정된 Content Group/Subtopic/evidence_cluster)와 그 배정 근거. 이 스킬은 여기 기록된 슬라이드 경계·Source Material 배정을 다시 판단하지 않고, 그 배정에 해당하는 `material_analysis.json`의 실제 내용을 바탕으로 1단계 이하 작업을 수행한다.
- 청중 유형, 발표 언어, 발표 시간, 목표 슬라이드 수
- (선택) 레퍼런스 자료 경로
- content-designer가 이미 정한 스토리라인 순서(슬라이드 배치 흐름)

## 처리 흐름

1. **핵심 메시지 파악** — `slide_composition_map.json`에서 이 슬라이드에 배정된 Source Material(Content Group/Subtopic/evidence_cluster ID)을 확인하고, 그에 해당하는 `material_analysis.json`의 텍스트/표/차트/이미지를 바탕으로 슬라이드별 핵심 메시지(Core Message)를 정한다.
   - **Manifest 우선 조회**: `evidence_manifest`가 있으면(최신 여부는 material-analysis SKILL.md 기준 — `material_analysis.json`이 마지막 확정 이후 재수정됐는데 Manifest가 재생성되지 않았다면 최신이 아니므로 원본 배열을 직접 확인) 배정된 Source Material 범위의 Manifest entry(ID·`evidence_type`·`source_type`(text_box 등 세부 출처 구분 포함)·summary·상태)를 먼저 확인해 무엇이 있는지 파악한다. 배정 범위 전체의 원문을 먼저 통째로 읽지 않는다.

1-b. **핵심 주장별 Evidence 확인 및 관계 유지** — Core Message, 그리고 Core Message 안에 개별 주장이 여러 개 있으면 그 각각(예: "서로 다른 두 근거로 뒷받침되는 두 개의 하위 주장")에 대해 `material_analysis.json`에서 이를 **직접** 뒷받침하는 근거(수치·표·이미지·서술·출처)를 확인한다. 이 단계는 아직 어떤 Visual Type(Chart/Bar/Table 등)으로 표현할지는 정하지 않는다 — "어떤 근거가 있고 그 근거들 사이에 어떤 관계가 있는지"까지만 명시한다(표현 방식은 3단계 이후 `content-visualization-freedom.md`·Layout Routing이 판단).
   - **관계 유형 확인** — 확인된 근거가 아래 유형 중 무엇에 해당하는지 판단한다(콘텐츠 형식이나 산업 분야와 무관하게, 어떤 입력 자료에도 동일하게 적용되는 일반 분류다. 아래는 각 유형의 이름일 뿐 특정 수치·업종 예시가 아니다):
     - 단일 독립 근거 (다른 값과 비교·연결되지 않는 값 하나)
     - 복수 비교 근거 (여러 대상·항목을 같은 기준으로 나란히 비교)
     - Before / After (전환 전후 두 상태)
     - 시간에 따른 변화·추세 (3개 이상 시점의 시계열)
     - 단계별 변화 (공정·단계를 거치며 값이 바뀌는 경우)
     - 구성요소별 기여도 (여러 요소가 하나의 결과에 각각 얼마나 기여하는지의 분해)
     - 원인 → 결과 (인과 관계)
     - 순환 관계 (되먹임·순환 구조)
     - 순차 공정/프로세스 (여러 단계가 순서대로 이어지는 흐름)
     - 병렬 동등 항목 (Parallel/Peer Items) — 서로 비교·인과·시계열 관계가 없이, 하나의 상위 범주(예: 기업 프로필, 인물 소개) 아래 동등한 자격으로 나열되는 개별 항목들(예: 임직원 수·소재지·사업장·비전처럼 서로 다른 속성을 나열하는 경우, 여러 인물의 학력·경력을 각각 나열하는 경우). "복수 비교 근거"와는 목적이 다르다 — 복수 비교 근거는 같은 기준으로 값을 견주는 것이 목적이지만, 병렬 동등 항목은 비교가 목적이 아니라 서로 다른 개별 사실을 함께 제시하는 것이 목적이다.
     - 위 어디에도 해당하지 않는 기타 관계
     
     관계형(단일 독립 근거가 아닌 모든 유형)이면 그중 대표값(예: 최종 결과 수치)만 남기지 않고 관계를 이루는 **값 전체**(예: 이전 상태·중간 상태·이후 상태, 또는 단계별 값)를 근거로 유지한다. 병렬 동등 항목은 값 사이에 순서·인과가 없으므로 "관계를 이루는 값 전체" 대신 나열된 개별 항목 전체를 근거로 유지한다(일부만 대표로 골라 축약하지 않는다). 어떤 값을 남길지는 그때그때 입력 자료의 실제 관계 구조를 따르며, 여기서 특정 산업·특정 수치를 규칙으로 고정하지 않는다.
   - **Required/Optional 구분**: 그 근거 없이는 핵심 주장이 성립하지 않거나 신뢰도가 크게 떨어지면 Required, 있으면 이해를 돕지만 없어도 주장이 성립하면 Optional로 표시한다. `content_match_confidence: uncertain`으로 표시된 근거(주로 이미지)는 그 중요도와 무관하게 Required로 표시하지 않는다(Optional 상한) — 정체가 불확실한 근거를 핵심 주장의 필수 근거로 올리지 않는다.
   - **Data Pending 근거의 Required/Optional**: `visual_placeholders`(`data_status: "data_pending"`)로 표시된 근거는 데이터가 아직 없다는 이유로 자동으로 Optional 처리하거나 슬라이드에서 제외하지 않는다 — 원래 그 자리가 뒷받침하려던 주장이 핵심 주장이면 그대로 Required로 표시하고 Evidence 칸에 "Data Pending(원본에 데이터 미제공, material_analysis.json 참조)"처럼 상태를 명시한다. 대표 수치가 없다고 해서 주장 자체를 삭제하거나 근거 없는 서술로 조용히 대체하지 않는다.
   - **근거-주장 매핑(Evidence-Claim 구조 확인)**: 아래 두 경우를 구분한다.
     - 상위 주장 하나를 뒷받침하는 복수 Evidence — 여러 근거가 같은 주장 하나를 함께 뒷받침하면 하나의 근거 그룹으로 묶는다.
     - 서로 다른 주장을 각각 뒷받침하는 Evidence Group — 근거(특히 Shared Supporting Content)가 **서로 다른 상위 주장 여러 개**를 뒷받침하면, 그 근거가 어느 주장에 연결되는지 각각 명시하고 이 시점에 하나의 균질한 그룹으로 합치지 않는다(구체적으로 어떻게 묶거나 나눌지는 4단계 Content Region 설계에서 반영).
   - **제작 지시문 우선 적용**: 이 슬라이드의 Source Material에 딸린 `production_directives` 중 `directive_type`이 `placement`/`visualization`/`emphasis`인 항목은 이 스킬 자체 판단보다 우선한다 — 예를 들어 "표로 구성"/"이미지와 함께 배치"라는 지시가 있으면 표현 방식·배치 의도로 우선 반영하고, 이 스킬이 임의로 다른 표현 방식을 판단하지 않는다(단, 색상·서체·여백 등 실제 시각 스타일은 항상 Hard Rule/Design System을 따르며 지시문이 이를 대체하지 않는다). 지시가 이미 확정된 슬라이드 경계·근거 구조와 모순되거나 실행 불가능하면 임의로 무시하지 않고 `needs_confirmation`으로 남긴다.
   - `material_analysis.json`에 실제로 존재하는 근거만 사용한다 — 원본에 없는 수치·관계를 새로 만들지 않는다. 근거가 없으면 해당 주장은 Evidence 없이 `N/A`로 남긴다(추정으로 채우지 않음). 단, Data Pending으로 이미 알려진 자리는 `N/A`가 아니라 위 Data Pending 표기를 따른다.
   - **원문 지연 조회**: Evidence 후보 스크리닝은 Manifest entry(요약·상태)로 먼저 한다. 다만 최종적으로 슬라이드 문구·Evidence 칸에 옮길 항목, 그리고 `uncertain`/Data Pending/`cross_group_ref`/관계형(비교·Before-After·추세·단계별·기여도·인과·순환·공정) Evidence는 반드시 해당 항목의 `canonical_ref`로 원문을 확인해 실제 값·범위·조건을 그대로 옮긴다 — Manifest의 `summary`(최대 180자 절삭)를 최종 Evidence 문구로 그대로 쓰지 않는다.

1-c. **Backward Completeness Check(완결성 역검증)** — 1-b로 Claim/Evidence를 구성한 직후, 2단계(Content Role 분류)로 넘어가기 전에 수행한다. 목적은 `slide_composition_map.json`이 이 슬라이드에 배정한 원본 내용이 1-b의 재구성 과정에서 판단 없이 빠지지 않았는지 확인하는 것이다 — **원본 문장을 전부 슬라이드에 욱여넣기 위한 절차가 아니라, 정보적으로 중요한 내용이 의도 없이 사라지는 것을 막기 위한 절차**다.
   - **항상 수행: 경량 추적** — 모든 슬라이드에서 `slide_composition_map.json`의 Source Material ID와 안정적으로 참조 가능한 Evidence ID/원본 항목 키를 1-b의 Claim/Evidence 참조와 대조한다. 이때 원문을 다시 의미적으로 분류하지 않고 아래만 확인한다. `evidence_manifest`가 있으면 이 대조는 그 entry(ID·유형·개수·상태)를 기준으로 수행하며 원문을 다시 읽지 않는다 — Manifest가 없거나 최신이 아니면(위 "Manifest 우선 조회" 판단 기준과 동일) 원본 배열에서 직접 개수·ID·상태를 확인한다.
     1. Source Material과 Evidence ID/원본 항목 키가 보존됐는지
     2. Evidence의 개수와 유형(일반 텍스트 / 수치 / 표 / 차트 / 이미지)이 배정 결과와 일치하는지
     3. `content_match_confidence: uncertain` 및 `data_status: data_pending` 상태가 유실·격상·삭제되지 않았는지
     - ID·개수·유형·상태에 불일치가 하나라도 있으면 경량 체크를 통과로 처리하지 않고, 그 슬라이드(또는 불일치 항목)를 아래 **상세 의미 검증** 대상으로 즉시 승격한다.
   - **상세 의미 검증 대상** — 아래 중 하나라도 있으면, 해당 위험 항목과 그 항목이 속한 Source Material 범위에 대해 `canonical_ref`로 원문을 지연 조회해 기존 수준의 원문 대조·6분류를 수행한다.
     - `uncertain` 근거 또는 Data Pending 근거
     - 병합/분할된 Source Material, 여러 Source Material이 한 슬라이드에 배정된 경우, 또는 `cross_group_ref`
     - `content-grouping`의 Coverage Check에 기록된 제외/미배정 처리의 사유·상태가 없거나 불일치해, 원래 배정 범위의 재구성이 필요한 경우
     - 표·차트 또는 복수 비교, 단계·순차, 인과, 종속 등 관계형 Evidence
     - 핵심 수치가 요약·선별·대표값화되어 원래 범위·조건·비교 관계의 손실 가능성이 있는 경우
     - 프레이밍/목표/조건 문장처럼 evidence_cluster 밖에 남아 1-b의 Claim/Evidence에 흡수·누락될 가능성이 있는 경우
   - **미배정 항목 처리** — 슬라이드별 BCC에서 미배정 원본 전체를 다시 읽거나 6분류하지 않는다. `content-grouping`의 `coverage_check`에서 해당 항목의 명시적 제외/미배정 사유와 추적 상태가 존재하는지만 확인한다. 사유·상태가 없거나 불일치하면 해당 항목을 content-designer에게 반환해 `content-grouping`에서 해결한다.
   - **상세 분류** — 상세 의미 검증 대상으로 승격된 원본 항목 하나하나를 아래 6개 범주 중 정확히 하나로 분류한다:
     1. Claim/Evidence에 명시적으로 반영됨
     2. Core Message/Supporting Message에 반영됨(개별 Evidence로 남지 않고 요약문에 흡수됨)
     3. 다른 Evidence와 중복되어 의도적으로 통합됨
     4. 정보량 없는 제목/라벨이라 의도적으로 제외됨(그 자체로 새로운 사실을 담지 않는 헤딩·구획 텍스트 등)
     5. `content_match_confidence: uncertain`이라 보류됨(1-b의 Required 승격 금지 규칙을 그대로 따름)
     6. 중요 내용인데 미반영됨 → 재구성 필요
     - 판단 기준: 그 항목이 새로운 사실(수치·관계·범위·조건·대상·근거)을 담고 있는데 위 1~5 어디에도 해당하지 않으면 6으로 분류한다. 단순 재진술이나 라벨이면 4로 분류하고 6으로 넘기지 않는다.
   - **상세 검증에서 반드시 점검할 두 패턴** (반복적으로 유실이 확인된 유형):
     - 특정 evidence_cluster에 속하지 않고 Subtopic 최상위에 남아있는 프레이밍/목표/조건 문장 — 여러 Claim에 공통되지만 어느 한 Claim의 typed relationship 틀에도 깔끔히 안 들어가 Core Message 요약에만 흡수되고 Evidence에서 빠지기 쉽다.
     - 여러 Content Group을 병합한 경우, 이미 완결된 서사를 가진 한쪽 소스가 대표 텍스트로 채택되면서 병합 상대 쪽의 세부 내용(범위·산출물·조건 등)이 반영 여부 확인 없이 조용히 빠지기 쉽다.
   - **6(미반영)으로 분류된 항목의 재구성** — 아래 순서로 판단한다:
     1. 기존 Claim의 Evidence에 편입 가능한지 먼저 검토한다(가장 우선).
     2. 편입이 어색하면 그 Claim(또는 슬라이드 전체)의 별도 Supporting Evidence로 유지한다.
     3. 그래도 넣기 부적절하면 슬라이드에서 제외하되, 제외 사유를 명시적으로 남긴다(추정으로 채우거나 침묵 처리하지 않는다).
     - 재구성 결과 슬라이드 병합/유지/분할 자체를 다시 판단해야 할 정도로 큰 누락이면(예: Evidence만으로는 도저히 한 슬라이드에 담기지 않음), 6단계와 동일하게 content-designer에게 알려 `content-grouping`을 재호출하게 한다 — 이 스킬 자신이 슬라이드 경계를 바꾸지 않는다.
   - **기록**: 모든 슬라이드에 경량 추적 결과(Source Material/Evidence ID 보존 여부, 유형별 개수, uncertain/Data Pending 개수, 불일치 여부)를 `slide_outline.md`의 "Backward Completeness Check" 항목에 기록한다. 상세 의미 검증을 수행한 경우에만 범주별 개수와 6으로 분류돼 재구성된 항목의 처리 결과를 추가 기록한다.
   - 이 체크는 6단계 "구조적 사전 점검"의 "1-b에서 Required로 표시한 Evidence가 Content Region에 빠짐없이 반영되어 있는가"와 방향이 다르다 — 6단계는 **1-b가 이미 고른 Evidence**가 이후 Region에서 유실되지 않는지 보는 전방(forward) 체크이고, 이 1-c는 **원본 전체 대비 1-b가 무엇을 빠뜨렸는지** 보는 후방(backward) 체크다. 두 체크는 서로 대체하지 않으며 둘 다 수행한다.

2. **Content Role 분류** — 슬라이드 내 각 콘텐츠 요소를 Primary / Dependent / Shared Supporting / Conclusion 중 필요한 역할로 분류한다. 역할 정의는 새로 쓰지 않고 [`Claude_PPT_Design_System.md`](../../../docs/design-system/Claude_PPT_Design_System.md) §5 "Content Relationship / Region Composition 원칙"을 그대로 따른다.
   - 모든 역할을 채울 필요는 없다. 해당 역할의 콘텐츠가 없으면 `N/A`로 표기한다.
   - 단일 콘텐츠 중심 슬라이드나 자유 형식 콘텐츠를 억지로 4개 역할에 끼워 맞추지 않는다.

3. **정보 관계 분석** — 콘텐츠 간 관계를 아래 중 필요한 유형으로 판단한다: 병렬 / 비교 / 순차 / 인과 / 종속 / 전체-부분 / 단일 콘텐츠 / 기타·복합. 판단 기준은 콘텐츠 형식(표/차트/이미지/텍스트)이 아니라 정보의 의미와 관계다.
   - **Dominant Relationship 판단(슬라이드에 Claim이 여러 개이고 그 Relationship이 서로 다를 때)**: 이 항목의 Relationship 값은 슬라이드 전체를 대표하는 **Dominant Relationship**이다 — 여러 Claim 중 하나의 Evidence 내부에만 존재하는 부분적 인과·순차 관계를, 그 이유만으로 슬라이드 전체의 Relationship으로 승격하지 않는다. Core Message가 실제로 요약하는 범위와 각 Claim의 비중(몇 개 Claim이 해당 관계를 공유하는지)을 기준으로 슬라이드 전체에 공통되는 관계를 판단한다. Claim들의 관계 유형이 서로 달라 하나로 대표하기 어려우면 억지로 인과·순차 중 하나를 고르지 않고 **기타·복합**으로 표기한다.
   - **순차/인과 관계 성립 여부 검증(Claim이 하나뿐이어도 적용)**: 여러 항목을 시간순으로 나열할 수 있다는 이유만으로 순차·인과 관계로 판단하지 않는다. 각 항목이 실제로 앞 항목의 결과에 기능적으로 의존하는지 원문 근거로 확인하고, 항목 순서를 바꾸거나 각 항목을 독립적으로 제시해도 핵심 메시지가 유지되면 병렬(또는 전체-부분)에 더 가깝다 — 이 경우 순차/Flow 계열 대신 병렬 계열로 재판단한다.

4. **Content Region 설계** — 좌표·세부 디자인을 정하기 전에 큰 Content Region부터 설계한다(위 §5 원칙의 Region 구성 절차를 따름).
   - 대등한 Primary Content가 여러 개면 병렬 Region으로 묶는 것을 고려한다.
   - Dependent Content는 대응하는 Primary Content와 같은 Region(Group)에 둔다.
   - Shared Supporting Content는 특정 Column/Region에 임의로 귀속시키지 않고, 공통 Supporting Region을 우선 검토한다.
   - 1-b에서 서로 다른 상위 주장에 매핑된 근거들이 있으면, 그 근거들을 하나의 균질한 Region/그룹으로 뭉뚱그리지 않고 매핑된 주장 단위로 구분한다(예: 근거 A·B·C가 주장①을, 근거 D가 주장②를 뒷받침하면 최소한 서로 다른 근거 그룹으로 인지되도록 Region을 나누거나 구획한다 — 구체적 시각적 표현은 이후 단계 몫).
   - Conclusion/Takeaway가 필요하면 전체 내용을 종합하는 별도 Region을 고려한다.
   - **Data Pending Region 예약**: `visual_placeholders`(`data_status: "data_pending"`)로 표시된 근거가 배정된 Claim이 있으면, 데이터가 없다는 이유로 그 Region을 생략하거나 일반 텍스트 서술로 대체하지 않는다 — 원래 지시된 표현 방식(표/차트/도식, `instructed_visual_type`)에 맞는 Region 자리를 그대로 설계하고, Region 설명에 "Data Pending" 상태를 명시한다. 이렇게 하면 이후 실제 데이터가 채워질 때 Region 구조 전체를 다시 설계하지 않고 그 Region의 내용만 채울 수 있다. 실제 Data Pending 상태의 시각적 표현(예: "데이터 준비 중" 플레이스홀더 스타일)은 web-ppt-generator 구현 몫이며, 이 스킬은 자리와 의도된 Visual Type까지만 확정한다.
   - **제작 지시문 우선 적용**: 이 슬라이드에 딸린 `production_directives` 중 `directive_type`이 `placement`(좌우·상하 배치 등)인 항목은 Region 배치를 정할 때 이 스킬 자체 판단보다 우선한다(예: "박스 2개 위아래 배치"는 좌우 병렬이 아니라 상하 배치 Region으로 반영). Content Regions 기술에 어떤 지시(id)를 반영했는지 남긴다.
   - 각 Region의 콘텐츠 표현 방식(표/차트/이미지/텍스트 등)은 [`content-visualization-freedom.md`](../../../docs/design-system/content-visualization-freedom.md)의 Main Visual 선택 기준을 따라 함께 판단한다(면적 점유형/압축형 Visual 여부는 Region 크기 판단에 영향을 준다). `production_directives`(`visualization` 유형)로 표현 방식이 이미 지시된 경우 그 지시를 우선 적용한다.
   - Region의 정확한 Alignment/Gap/Typography 등 세부 디자인 규칙은 여기서 정의하지 않는다 — `Claude_PPT_Design_System.md` §5의 Content Density·Parallel Layout Alignment 원칙을 따르며, 실제 적용은 web-ppt-generator 단계에서 이루어진다.
   - Region을 설계할 때 원본 표/도식/이미지의 시각적 레이아웃(셀 배치, 색상, 아이콘 형태 등)을 그대로 옮겨 그리지 않는다 — 원본은 콘텐츠·관계·제작 의도(위 제작 지시문 포함)를 파악하는 근거일 뿐이며, 실제 Region 구성과 표현은 항상 Hard Rule/Claude PPT Design System/Layout Reference를 따라 새로 설계한다(자세한 원칙은 `material-analysis` SKILL.md "'원문 그대로 반영' 원칙의 적용 범위" 참조).

5. **Layout Routing** — `.claude/skills/web-ppt-generator/references/design-rules.md`의 "레이아웃 선택 기준"을 그대로 사용해 가장 적합한 Layout을 고른다.
   - 표지 슬라이드는 `01_cover_design_V2.md`를 우선 적용(L01~L33 미참고).
   - 표지가 아니면 먼저 [`docs/layout-reference/2026.08.20_special-layout-index_V1.md`](../../../docs/layout-reference/2026.08.20_special-layout-index_V1.md)(콘텐츠 구조별 특수 Layout Reference 17종의 경량 인덱스 — Layout명/Category/Use When/Do Not Use When/원본 경로)에서 이번 슬라이드의 Relationship·콘텐츠 구조에 맞는 Use When 조건에 해당하는 후보가 있는지 확인한다. 이 인덱스만으로 1~2개 후보로 좁혀지면 그 후보의 원본 Layout MD만 상세 Read해 세부 스펙(구조·비율·Variant 등)을 확인하고 우선 적용한다 — 후보가 아닌 나머지 특수 Layout 문서는 열지 않는다.
   - 인덱스의 어떤 Use When에도 해당하지 않으면 `layout-catalog_V1.md`(L01~L33)에서 후보를 고른다.
   - Data Pending Region이 있다는 이유로 Layout 후보에서 제외하지 않는다 — 실제 데이터가 없어도 그 Region이 차지할 자리(표/차트 영역)를 감안해 Layout을 고른다.
   - 이 Skill은 후보 목록이나 개별 Layout의 세부 규칙(색상·서체·정렬 수치 등)을 다시 정의하지 않는다 — design-rules.md와 선택된 Layout Reference 문서를 참조만 한다.

6. **구조적 균형 사전 점검 (Pre-Design Structural Check)** — 실제 HTML 생성 전, 콘텐츠 구조 수준에서만 아래를 점검한다. 좌표·Overflow 등 렌더링 수준 검사는 하지 않는다(web-ppt-generator의 자기 검증이 담당).
   - 특정 Region에 콘텐츠가 과도하게 몰려 있지 않은가
   - 대등한 병렬 Region 간 예상 정보량·시각적 비중이 지나치게 불균형하지 않은가
   - Shared Supporting Content가 특정 Primary Region에 잘못 귀속되지 않았는가
   - **1-b에서 Required로 표시한 Evidence가 Content Region에 빠짐없이 반영되어 있는가** — 핵심 메시지(대표 수치·결론)만 남고 그것을 뒷받침하는 비교·Before-After·추세·단계별 변화·기여도·인과·순환·공정 관계가 유실되지 않았는지 확인한다. 유실됐다면 4단계로 돌아가 해당 Region에 되살린다. (이 항목은 1-b가 이미 고른 Evidence의 이후 유실만 본다 — 원본 전체 대비 1-b가 무엇을 놓쳤는지는 1-c Backward Completeness Check가 별도로 담당하며, 이 6단계에서 새로 하지 않는다.)
   - 서로 다른 상위 주장을 뒷받침하는 근거들이 하나의 균질한 그룹으로 뭉뚱그려지지 않았는가
   - Data Pending으로 표시된 Region이 삭제되거나 일반 텍스트로 조용히 대체되지 않고 자리와 의도된 Visual Type을 유지하고 있는가
   - Conclusion이 특정 Region 안에 묻혀 있지 않은가
   - 현재 구조로 한 슬라이드에 담기 어려운 콘텐츠량이면 요약 또는 슬라이드 분할이 필요한가(`content-visualization-freedom.md`의 "내용 과다 시 요약/슬라이드 분할 제안" 범위에서 판단)
   - 문제가 발견되면 2~5단계로 돌아가 재조정한다. 슬라이드 병합/유지/분할 자체를 다시 판단해야 하면(Content Region 설계만으로 해결되지 않으면) content-designer에게 알려 `content-grouping`을 재호출해 `slide_composition_map.json`을 재조정하게 한다 — 이 스킬 자신은 슬라이드 경계를 바꾸지 않는다.

7. **`slide_outline.md` 기록** — 아래 스키마로 `/output/{project-name}/slide_outline.md`에 기록한다.

## 출력 스키마 (`slide_outline.md`)
각 슬라이드마다 최소 아래 항목을 포함한다. 판단할 근거가 없거나 해당 사항이 없으면 `N/A`로 표기한다 — 형식을 맞추기 위해 값을 억지로 채우지 않는다.

```markdown
## Slide {N}. {슬라이드 제목}

- **Source Material**: (`slide_composition_map.json`에서 이 슬라이드에 배정된 source_material ID 목록을 그대로 옮겨 적는다 — 예: "CG02(entire), CG03-ST01-EC1(partial)". 이 스킬이 새로 판단하지 않는다.)
- **Core Message**:
- **Core Claims & Evidence**: (1-b의 결과 — 슬라이드 안의 핵심 주장마다 하나씩. 주장이 하나뿐이면 항목도 하나)
  - Claim: (구체적 주장)
    - Evidence: (원본 자료의 구체적 근거 — 수치/표/이미지/서술, 출처 포함. 없으면 `N/A`. `visual_placeholders`(data_status: data_pending)에 해당하면 "Data Pending(원본에 데이터 미제공)"으로 표기)
    - Relationship: (단일 독립 근거 / 복수 비교 근거 / Before-After / 시간에 따른 변화·추세 / 단계별 변화 / 구성요소별 기여도 / 원인→결과 / 순환 관계 / 순차 공정·프로세스 / 병렬 동등 항목(Parallel/Peer Items) / 기타 중 해당하는 것 — 관계형이면 대표값 하나가 아니라 관계를 이루는 값 전체(이전 상태·중간 상태·이후 상태, 또는 단계별 값)를 기재한다. 병렬 동등 항목이면 나열된 개별 항목 전체를 기재한다. 아래는 형식 예시일 뿐 특정 자료의 실제 값이 아니다: "이전 상태 A → 이후 상태 B", "1단계 X / 2단계 Y / 3단계 Z", "항목 a / 항목 b / 항목 c(비교 아닌 나열)")
    - Required/Optional:
  - Claim: (두 번째 주장이 있으면 반복, 서로 다른 근거 그룹을 여기서 분리)
- **Backward Completeness Check**: (1-c의 결과 — 모든 슬라이드에 `경량` 또는 `상세` 모드를 명시한다. 경량이면 Source Material/Evidence ID 보존 여부, 유형별 개수, uncertain/Data Pending 개수, 불일치 여부를 기록한다. 상세이면 추가로 범주별 개수(예: "명시반영 6 / Core Message반영 2 / 중복통합 1 / 라벨제외 3 / uncertain보류 2 / 미반영 0")와 재구성된 미반영 항목의 처리 결과(편입/Supporting Evidence로 유지/제외 사유)를 기록한다. 미반영 항목이 없었으면 "미반영 항목 없음"으로 명시한다.)
- **Content Roles**:
  - Primary:
  - Dependent:
  - Shared Supporting:
  - Conclusion/Takeaway:
- **Relationship**: (병렬 / 비교 / 순차 / 인과 / 종속 / 전체-부분 / 단일 콘텐츠 / 기타·복합 중 해당하는 것)
- **Content Regions**: (설계된 Region 목록과 각 Region이 대응하는 역할·표현 방식, 예: "Region A(병렬 Primary #1, Chart) / Region B(병렬 Primary #2, Chart) / Supporting Region(공통, Text)" — 위 Core Claims & Evidence의 Required 항목이 어느 Region에 반영됐는지 알 수 있게 기술. Data Pending Region이 있으면 "Region B(Primary #2, Chart, Data Pending)"처럼 상태를 함께 표기)
- **Selected Layout**: (구조별 특수 Layout Reference 문서명 또는 L01~L33 번호)
- **Layout Selection Reason**: (Use When 조건 충족 여부 등 선택 근거)
- **Structural Check**: (사전 점검 결과 요약 — 문제 없음 / 발견된 이슈와 조치)
```

이 스키마는 `web-ppt-generator`([5]/[7])가 HTML/CSS를 구성할 때 그대로 소비하는 입력이 된다. 이후 단계는 여기 기록된 Content Region·역할·관계·Layout을 다시 판단하지 않고, 그 결과를 바탕으로 실제 배치·정렬·크기를 구현한다. 특히 Core Claims & Evidence의 **Required** 항목은 web-ppt-generator가 실제 표현 방식(Chart/Table/Diagram/Image/Text 등, `content-visualization-freedom.md` 판단 범위)을 고르더라도 그 관계 전체가 드러나야 하는 근거이며, 대표 수치 하나로 축약해도 되는 항목이 아니다.

## 하지 않는 것
- 슬라이드 병합/유지/분할, Content Group/Subtopic/evidence_cluster 단위의 Source Material Mapping 결정 → `content-grouping` 스킬이 이 단계 이전에 이미 확정(`slide_composition_map.json`)
- HTML/CSS 생성, 실제 좌표·정렬·간격·타이포그래피 결정 → `web-ppt-generator` 담당
- 렌더링 결과의 Overflow·요소 겹침 등 시각적 QA → `web-ppt-generator`의 자기 검증 담당
- Hard Rule / Claude PPT Design System / Content Visualization Freedom / Layout Reference의 세부 규칙 재정의 — 항상 원본 문서를 참조
- Evidence의 구체적 Visual Type(Chart/Bar/Waterfall/Table/Diagram 등 형태 확정) 결정 — 1-b는 "어떤 근거가 필요하고 근거들 사이에 어떤 관계가 있는지"까지만 명시하며, 그 근거를 무엇으로 그릴지는 `content-visualization-freedom.md`와 5단계 Layout Routing의 판단 범위다

## 판단 기준 원본 문서 (참조만, 복사 금지)
- 슬라이드 경계·Source Material 배정: `content-grouping` 스킬이 생성하는 `slide_composition_map.json` — 재판단하지 않고 그대로 소비
- 역할 분류·Region 구성: [`docs/design-system/Claude_PPT_Design_System.md`](../../../docs/design-system/Claude_PPT_Design_System.md) §5 "Content Relationship / Region Composition 원칙"
- Layout Routing: [`.claude/skills/web-ppt-generator/references/design-rules.md`](../web-ppt-generator/references/design-rules.md) "레이아웃 선택 기준" (내부 4.5단계에서 [`docs/field-test-patterns/field-test-pattern-library.md`](../../../docs/field-test-patterns/field-test-pattern-library.md)를 참고용으로 대조)
- 콘텐츠 표현 방식·요약/분할 판단: [`docs/design-system/content-visualization-freedom.md`](../../../docs/design-system/content-visualization-freedom.md)
- 제작 지시문(`production_directives`)·Data Pending 근거(`visual_placeholders`)의 스키마와 식별 방식: `material-analysis` SKILL.md — 이 스킬은 두 필드를 새로 만들지 않고 `material_analysis.json`에 이미 기록된 것을 그대로 소비한다

## 향후 보완 여지
이번 버전은 Field Test를 위한 최소 골격이다. 구조적 사전 점검(6단계)의 판단 기준(예: 정보량 불균형의 구체적 임계치)은 아직 정성적 판단에 의존하며, 실제 프로젝트에서 반복 사용하며 필요 시 보완한다. 지금 단계에서는 세부 기준을 과도하게 경직시키지 않는다.
