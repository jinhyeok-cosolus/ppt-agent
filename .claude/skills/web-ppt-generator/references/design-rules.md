# 디자인 규칙 (design-rules.md)

> 이 문서는 웹PPT/pptx 생성 시 항상 먼저 참조하는 디자인 규칙이다. **고정 규칙**과 **가변 규칙**으로 구분한다.
> 신규 규칙은 LLM이 스스로 "일반화 가능하다"고 판단하더라도 **사용자의 명시적 승인 없이는 본문에 반영하지 않는다.** 승인 전 후보는 하단 "검토 대기 후보" 섹션에만 기록한다.

## 적용 우선순위

아래 4개 문서는 각각 별도 원본 파일로 관리하며(본 문서에 내용을 복사하지 않고 경로만 참조), 충돌 시 다음 순서로 우선 적용한다.

| 우선순위 | 구분 | 원본 문서 | 역할 |
|---|---|---|---|
| 1 | Hard Rule | [`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`](../../../../docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md) | 규격·폰트·크기·컬러·로고 등 절대 변경 불가 규칙 |
| 2 | Claude PPT Design System | [`docs/design-system/Claude_PPT_Design_System.md`](../../../../docs/design-system/Claude_PPT_Design_System.md) | Hard Rule 범위 내에서 PPT 전체의 Visual Style, Color, Typography, Grid/Spacing, Component(Shape/Card/Line) Style, Image Treatment, Chart/Table/Diagram Style을 결정하는 공통 Design System |
| 3 | Content Visualization Freedom | [`docs/design-system/content-visualization-freedom.md`](../../../../docs/design-system/content-visualization-freedom.md) | 위 두 규칙을 준수하는 범위에서, 콘텐츠별 표현 방식(레이아웃·표/차트/이미지 선택 등)에 대한 AI 판단 허용/금지 경계 |
| 4 | Layout Reference | [`docs/layout-reference/2026.08.13_layout-catalog_V1.md`](../../../../docs/layout-reference/2026.08.13_layout-catalog_V1.md)(선택 인덱스) + [`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`](../../../../docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx)(시각적 구조 원본) + `docs/slide-design-rules/`의 콘텐츠 구조별 특수 Layout Reference(예: [`three-column.md`](../../../../docs/slide-design-rules/three-column.md)) | 위 세 규칙을 준수하는 범위에서, 콘텐츠 유형·정보 구조에 따라 적합한 레이아웃(L01~L33, 또는 조건에 맞는 구조별 특수 Layout Reference)을 고르기 위한 참고 자료. 디자인 고정 규칙이 아니며 가장 낮은 우선순위 |
| 표지 전용 | Slide-Type Rule — Cover | [`docs/slide-design-rules/01_cover_design_V2.md`](../../../../docs/slide-design-rules/01_cover_design_V2.md) | **표지(Cover) 슬라이드를 생성할 때만** 적용. Hard Rule·Claude PPT Design System을 준수하는 범위에서 표지의 레이아웃·비주얼 스타일을 구체적으로 지정한 문서. 표지 슬라이드에 한해 4번 범용 Layout Reference(L01~L33)보다 우선 적용하며, 표지 생성 시 L01~L33 카탈로그는 참고하지 않는다 |

상위 우선순위 문서와 충돌하는 내용은 하위 문서에서 적용하지 않는다. 아래 "고정 규칙" 섹션은 1번 문서를, "가변 규칙" 섹션은 레이아웃 등 프로젝트별 판단 대상을 다루며, 그 판단은 2번·3번·4번 문서의 기준을 따른다. "표지 전용" 문서는 슬라이드 유형이 표지일 때만 적용되는 예외이며, 그 외 슬라이드 유형에는 영향을 주지 않는다.

> **세션 내 원본 문서 재사용 원칙(공통)**: 위 우선순위 문서(Hard Rule, Layout MD 등 이 표가 가리키는 모든 원본)를 이번 실행 세션에서 이미 읽고 대조한 적이 있다면, 같은 세션 안에서는 다시 Read하지 않고 그때 확인한 내용을 재사용한다. 여러 슬라이드가 반복 참조하는 문서(대표적으로 Layout MD)는 최초 대조 시 필요한 항목만 발췌해 체크리스트로 남기고 이후에는 그 체크리스트와 대조하는 절차를 쓸 수 있다(구체 절차는 `SKILL.md`의 해당 QA 섹션 참조). 새 세션(새 서브에이전트 호출)에서는 각 문서를 다시 1회 읽는다 — 세션 간 캐시는 없다.

## 고정 규칙 — 1순위 · Hard Rule

> **Source of Truth**: [`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`](../../../../docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md) (사용자 제공, 2026-08-12 등록). 본 Hard Rule은 아래 "가변 규칙" 및 개별 레이아웃 문서보다, 그리고 아래 Claude PPT Design System·Content Visualization Freedom보다 **항상 우선 적용**한다.
> **이 절은 인덱스일 뿐이다** — Hard Rule의 실제 수치·색상값·좌표·문구는 여기 복사하지 않는다. 적용·QA 대조 시에는 항상 위 원본 문서를 § 번호로 직접 열어 확인한다(요약·재기억으로 대체하지 않는다). 세션 내 재사용은 위 "세션 내 원본 문서 재사용 원칙"을 따른다.

원본 문서의 절 구성(찾아볼 위치 안내용 — 필요한 §만 골라 확인한다):

| § | 항목 |
|---|---|
| §1 | 슬라이드 규격(16:9) |
| §2 | 폰트(Pretendard 단일 서체, Weight 자유) |
| §3 | 글씨 크기(구체적 크기는 Claude PPT Design System §3에서 정의) |
| §4 | 제목 및 부제목 |
| §5 | Brand Color(Primary/Secondary/Neutral 팔레트, Color Usage 원칙) |
| §6 | 전체 디자인 분위기 |
| §7 | 회사 로고 및 Motto(로고 파일 경로 포함) |
| §8 | 기본 디자인 품질(겹침·overflow·텍스트 초과·비율 왜곡 금지 체크리스트) |
| §9 | 공통 Header System(Section Label/Main Title/CI/Sub Message/구분선/페이지 번호의 정확한 좌표·색상) |
| §10 | Content Comparison Header(Before/After·Three-Column류 Header Bar 스타일) |
| §11 | Vertical Content Divider |
| §12 | Main Title Supporting Message |

## Claude PPT Design System — 2순위 · Hard Rule 다음 우선 적용

> PPT 전체가 하나의 프레젠테이션처럼 보이도록 하는 공통 Design System(Visual Style/무드, Color, Typography, Grid/Spacing, Component(Shape/Card/Line/Arrow/Connector) Style, Image Treatment, Chart/Table/Diagram Style). Hard Rule을 대체하지 않으며 그 범위 안에서만 적용한다.
> 원본 문서(항상 이 경로를 직접 참조 — 본 문서에 내용을 복사하지 않음): [`docs/design-system/Claude_PPT_Design_System.md`](../../../../docs/design-system/Claude_PPT_Design_System.md)
> Hard Rule과 충돌하는 부분은 적용하지 않는다. 아래 "가변 규칙"(레이아웃 선택 등)과 "콘텐츠 표현 자유도"(다음 섹션) 판단은 모두 이 Design System 범위 안에서 이루어져야 한다.

## 콘텐츠 표현 자유도 — 3순위 · Hard Rule·Claude PPT Design System 다음 우선 적용

> AI(content-designer)가 슬라이드별로 표, 그래프, 다이어그램, 이미지, 텍스트 중심 구성 등 콘텐츠 표현 방식을 스스로 판단할 수 있는 허용 범위와, 임의로 변경해서는 안 되는 금지 범위를 정의한다. "디자인 스타일 생성"이 아니라 "콘텐츠를 가장 효과적으로 전달하는 표현 방식 선택"에 한정된 자유도다.
> 원본 문서(항상 이 경로를 직접 참조 — 본 문서에 내용을 복사하지 않음): [`docs/design-system/content-visualization-freedom.md`](../../../../docs/design-system/content-visualization-freedom.md)
> Hard Rule, Claude PPT Design System과 충돌하는 판단(예: 고정 규칙의 폰트/컬러 변경, Design System과 다른 새 디자인 언어 생성)은 이 문서가 "Allowed"로 열어두는 범위에 포함되지 않는다 — 두 상위 문서가 항상 우선한다.

## 표지(Cover) 전용 규칙 — 표지 슬라이드에서만 적용, Layout Reference보다 우선

> 표지 슬라이드를 생성·수정할 때 **항상 자동으로 참조**한다(별도 지시나 `@` 지정 없이도 적용). Hard Rule·Claude PPT Design System·Content Visualization Freedom을 준수하는 범위 안에서만 적용되며, 상위 규칙과 충돌하는 부분은 적용하지 않는다. 표지가 아닌 슬라이드(본문, Section Divider, Closing 등)에는 적용하지 않는다.
> 원본 문서(항상 이 경로를 직접 참조 — 본 문서에 내용을 복사하지 않음): [`docs/slide-design-rules/01_cover_design_V2.md`](../../../../docs/slide-design-rules/01_cover_design_V2.md) (사용자 제공, 2026-08-13 등록)
> 표지 생성 시 이 문서가 4순위 범용 Layout Reference(L01~L33)를 대체한다 — 표지에는 L01 등 카탈로그를 참고하지 않고 이 문서의 Layout/Visual Style/Soft Rules/Additional Rules/Avoid를 따른다.

## 가변 규칙 (레퍼런스 참고, 목적에 맞게 구성)

> 슬라이드 레이아웃, 표/차트 스타일, 정보 시각화, 강조 방식 등. 레퍼런스 자료 분석 후 사용자 승인을 받아 이곳에 추가한다.

### 레이아웃 선택 기준 — 채택 (2026-08-13, 사용자 승인) · 4순위 Layout Reference

> 디자인 고정 규칙이 아니다. 콘텐츠 유형·정보 구조에 따라 적합한 레이아웃을 고르기 위한 참고 기준이며, Hard Rule·Claude PPT Design System·Content Visualization Freedom과 충돌하는 부분은 적용하지 않는다.

- **선택 인덱스**(레이아웃 판단 시 항상 먼저 참조): [`docs/layout-reference/2026.08.13_layout-catalog_V1.md`](../../../../docs/layout-reference/2026.08.13_layout-catalog_V1.md) — 콘텐츠 유형·정보 구조 기준으로 레이아웃 후보를 빠르게 선택하기 위한 33종(L01~L33) 인덱스. 원본 내용은 수정하지 않고 경로만 참조한다.
- **시각적 구조 원본**(카탈로그에서 후보를 고른 뒤, 실제 요소 배치·구조를 확인해야 할 때만 참고): [`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`](../../../../docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx) — 33종 레이아웃 와이어프레임 원본(L01~L33이 슬라이드 1~33번에 대응).
  - 색상·서체는 이 pptx에 플레이스홀더로만 표시되어 있으므로 **그대로 쓰지 않는다** — 실제 적용 시 항상 위 "고정 규칙"(Pretendard 단일 서체, Brand Color)과 "Claude PPT Design System"을 따른다.
- **콘텐츠 구조별 특수 Layout Reference**(L01~L33 일반 카탈로그보다 먼저 검토): `docs/slide-design-rules/` 폴더에는 특정 콘텐츠 구조에 최적화된 개별 Layout Reference 문서(각 300~480줄)가 누적된다(표지 전용 문서는 위 "표지 전용" 행에서 별도로 다룸). **경량 선택 인덱스**(레이아웃 판단 시 항상 먼저 참조 — 원본 17개 문서를 전부/다수 열지 않고 여기서 먼저 후보를 1~2개로 좁힌다): [`docs/layout-reference/2026.08.20_special-layout-index_V1.md`](../../../../docs/layout-reference/2026.08.20_special-layout-index_V1.md) — 각 문서의 Layout명/Category/Use When/Do Not Use When/원본 MD 경로만 정리한 표. 슬라이드 콘텐츠 구조가 이 인덱스의 Use When 조건에 해당하면 일반 카탈로그(L01~L33)보다 먼저 그 **후보로 좁혀진 원본 MD만** 상세 Read해 적용하고, 해당하지 않으면 기존 절차대로 L01~L33에서 선택한다. 이 인덱스 자체는 각 원본 MD의 Use When 절을 옮긴 것일 뿐 새 판단 기준이 아니며, 세부 스펙(비율·색상·Variant 규칙 등)은 후보 확정 후 원본 MD를 열어 확인한다.

  이 인덱스가 가리키는 문서들은 각자 "Hard Rule > Claude PPT Design System > 해당 Layout Reference"라는 자체 우선순위를 명시하며, 이는 본 design-rules.md의 전체 우선순위 체계(1~4순위)와 정합한다. Layout을 고를 때는 **콘텐츠 항목 개수보다 정보 관계(Relationship)를 우선 판단**한다 — 아래 "Layout Routing 판단 순서"를 따른다. 같은 개수의 요소라도 그 사이의 관계가 다르면 서로 다른 Layout 계열을 검토해야 한다(예: 3개 요소라도 서로 독립·대등한 관계면 Column/Card 계열을, 순서대로 이어지는 관계면 Process/Flow 계열을, 되먹임·순환 구조면 Cycle/Loop을 표현할 수 있는 Layout을 각각 검토 대상으로 삼는다 — 이는 형식 예시일 뿐 특정 개수를 특정 Layout에 고정하는 규칙이 아니다). Visual + Insight Layout은 인덱스의 다른 문서들보다 조건이 넓은 범용 Family이므로, 콘텐츠가 회사소개·정량 Benefit 비교·좌우 Table+Technology 비교 등 더 구체적인 전용 Layout의 조건에 먼저 해당하는지 확인한 뒤에만 후보로 선택한다.

### Layout Routing 판단 순서 — Relationship 우선

> `slide-structuring`(Phase B)의 출력(Claim → Evidence → **Relationship** → Required/Optional)과 `content-visualization-freedom.md`가 그 Relationship에 대해 판단한 **Visual Strategy 방향**을 입력으로 받아, 그 관계와 전략을 가장 잘 수용할 수 있는 Layout을 고른다. 판단 순서는 **Relationship/Visual Strategy → 정보 구조 → 항목 수** 순이며, 항목 수(개수)는 후보를 좁힌 뒤 참고하는 마지막 요소일 뿐 단독 결정 기준이 아니다.

1. **Relationship/Visual Strategy 확인** — `slide-structuring`(Phase B)이 식별한 Relationship 유형(단일 독립 근거 / 복수 비교 근거 / Before-After / 시간에 따른 변화·추세 / 단계별 변화 / 구성요소별 기여도 / 원인→결과 / 순환 관계 / 순차 공정·프로세스 / 기타)과, `content-visualization-freedom.md`가 그에 대해 제시한 Visual Strategy 방향을 확인한다.
2. **Relationship에 맞는 Layout 계열 우선 검토** — 아래는 Relationship이 어떤 Layout 계열을 우선 검토 대상으로 만드는지의 **방향**이며, 특정 Relationship을 특정 Layout 하나에 고정 매핑하지 않는다. 아래 목록에 없는 Relationship이나 계열은 위 "콘텐츠 구조별 특수 Layout Reference" 인덱스(`special-layout-index_V1.md`)와 `layout-catalog_V1.md`(L01~L33) 전체에서 실제 Use When 조건을 대조해 판단한다.
   - 독립·대등 항목(단일 독립 근거가 여러 개 병렬) → Column/Card 계열 검토 가능
   - 복수 비교 근거 → **모든 대상이 공유하는 동일한 Row/Column 비교축(공통 평가 기준)이 실제로 존재할 때만** Comparison 계열(표/매트릭스 등) 우선 검토한다. 그룹마다 항목 구성(종류·개수)이 달라 공통 비교축이 없으면 비교 관계가 아니라 독립·대등 항목 병렬 관계에 가까우므로 Column/Card 계열을 우선 검토한다 — 정량 데이터·수치 항목이 많다는 이유만으로 Table/Matrix를 선택하지 않는다
   - Before/After → Before-After 또는 Comparison 계열 우선 검토
   - 순환 관계 → 순환·되먹임 구조를 보존할 수 있는 Layout 우선 검토
   - 순차 관계/공정 → Process/Flow 계열 우선 검토
   - 원인→결과 → 방향성·인과관계가 시각적으로 드러나는 Layout 우선 검토
   - 단계별 변화 → 단계의 진행성이 드러나는 Layout 우선 검토
   - 구성요소별 기여도 → 기여 관계를 표현할 Visual 공간을 충분히 확보할 수 있는 Layout 우선 검토
3. **정보 구조 확인** — 2에서 좁혀진 후보군 안에서 [`Claude_PPT_Design_System.md`](../../../../docs/design-system/Claude_PPT_Design_System.md) §5 "Content Relationship / Region Composition 원칙"의 Primary/Dependent/Shared Supporting/Conclusion 역할 분류와 Region 구성 절차를 따라 실제 정보 구조(위계 동일성·병렬성 등)를 확인한다.
4. **항목 수 확인(참고용, 마지막)** — 위 1~3에서 후보가 여럿 남았을 때만 항목 수를 참고해 더 적합한 쪽을 고른다. 항목 수만으로 1~3의 판단을 뒤집지 않는다.
4.5. **Field Test Pattern Library 대조(참고용)** — [`docs/field-test-patterns/field-test-pattern-library.md`](../../../../docs/field-test-patterns/field-test-pattern-library.md)에서 이 슬라이드의 Relationship·Content Density·항목 수·Visual 유무/형태가 기존 Pattern과 충분히 유사한지 확인한다. 유사한 Pattern이 있으면 그 Use When/Avoid When과 실제 검증된 Variant를 5의 후보 선택·6의 호환성 판단에 참고한다. 충분히 유사하지 않으면 억지로 적용하지 말고 1~4의 판단만으로 진행한다 — 이 문서는 후보를 새로 만들지 않고 기존 판단을 보강하는 참고 자료일 뿐이다.
5. **후보 매칭** — `docs/slide-design-rules/`의 콘텐츠 구조별 특수 Layout Reference를 위 경량 인덱스(`special-layout-index_V1.md`)에서 먼저 Use When 조건에 맞는 문서가 있는지 확인 → 있으면 그 1~2개 후보의 원본 MD만 상세 Read해 우선 적용 → 없으면 `layout-catalog_V1.md`의 L01~L33 중 적합한 후보 선택. 실제 요소 배치 확인이 필요할 때만 V3 pptx에서 해당 슬라이드 번호를 열어 구조를 확인한다.
6. **Visual/Content Fit Compatibility 확인** — 5에서 좁혀진 후보의 원본 Region Map(해당 Layout MD 또는 V3 pptx 실측 구조)이 Main Visual/Chart/Image를 필수 구조로 요구하면, 이 슬라이드의 실제 Primary/Required Visual과 Supporting/Optional Visual의 **개수·역할**이 그 Main Visual Region·Supporting Visual Region·Chart Region 구조와 호환되는지 확인한다 — 단순히 이미지가 있는지 없는지만 보지 않는다. 예: 후보가 Main Visual 자리를 1개만 정의하는데 슬라이드에 Primary Visual 외 Supporting Visual까지 있어 그 자리가 없으면, 또는 후보가 Main Visual을 필수로 요구하는데 슬라이드에 그 자리를 채울 Visual Evidence 자체가 없으면 호환되지 않는 것으로 판단한다. 명확히 호환되지 않으면 그 후보를 좌우 반전·Primary Visual 축소·원본에 없는 새 Region 추가 등으로 억지로 변형해 맞추지 않는다 — 5로 돌아가 다른 후보를 재검토한다.
   - **Visual 크기 적합성**: Region 자리 자체는 구조적으로 호환되더라도, 그 Region의 크기 제약 때문에 실제로 중요한(Required/Primary) Visual이 내용을 식별할 수 없는 수준까지 축소돼야 한다면 이 역시 비호환으로 판단한다 — 크기를 강제로 줄여 자리에 끼워 맞추지 않고 5로 돌아가 그 Visual에 더 넓은 Region을 배정할 수 있는 다른 후보를 재검토한다.
   - **Optional Visual 배제**: Optional/Supporting Visual이 후보 구조 전체의 복잡도만 늘리고 실질적 정보 기여가 크지 않으면(SKILL.md의 "공용 컴포넌트 재사용 > Supporting Visual Value" 원칙과 동일 기준), 그 Visual을 억지로 수용하는 후보 대신 더 단순한 후보를 우선 검토하거나 해당 Visual 자체를 생략한다.
   - **Content Volume Fit(공백 회피)**: 후보의 Region/Column/Node 수 대비 실제 정보량이 현저히 적어 채울 수 없는 공백이 크게 발생하면, 내용을 임의로 늘려 채우지 않는다 — 5로 돌아가 Region/Column/Node 수가 더 적은 단순한 후보를 재검토한다.
7. **적합한 Layout이 없을 때** — 카탈로그·특수 Layout Reference 어디에도 위 Relationship/Visual Strategy(및 위 Visual Requirement Compatibility)를 제대로 수용할 구조가 없으면, 억지로 가장 가까운 기존 Layout에 끼워 맞추지 않는다. 먼저 기존 Layout의 조합·최소 변형(Hard Rule·Claude PPT Design System은 반드시 유지)으로 표현 가능한지 검토하고, 그것도 어려우면 "적합한 Layout Reference 없음"으로 판단해 `slide_outline.md`의 Structural Check에 그 사유(어떤 Relationship 또는 Visual 구조를 어떤 후보들이 왜 수용하지 못했는지)를 남기고 메인/사용자 확인으로 이관한다.
8. **Hard Rule·Design System 재해석** — 최종 선택된 Layout(또는 조합·변형)에 Hard Rule과 Claude PPT Design System을 적용해 재해석한다. 표/그래프/이미지 등 구체적 표현 방식은 Content Visualization Freedom 범위 안에서 판단한다.

### 폐기됨 — 참고하지 않음
- `docs/design-candidates/cosolus-v1/`(2026-08-11, 구 샘플 `레이아웃 샘플.pptx` 14슬라이드 기반 상세 스펙 14종)는 2026-08-12 사용자 승인으로 **폐기**되었다. 이후 아래 V2 레이아웃 세트로 대체되었으며, 더 이상 웹PPT 생성 시 참조하지 않는다. 파일은 기록 보존을 위해 삭제하지 않고 폴더에 `README.md`로 폐기 표시만 남겼다.
- 구조 전용 레이아웃 30종(2026-08-12 채택, 기준 자료 `docs/layout-reference/2026.08.12_ppt layout set_integrated_V2.pptx`)은 2026-08-13 사용자 지시로 **폐기**되었다. 위 "레이아웃 선택 기준"의 V1 카탈로그(33종)로 대체되었으며, 더 이상 웹PPT 생성 시 참조하지 않는다. 해당 V2 pptx 파일은 현재 `docs/layout-reference/` 폴더에서 확인되지 않는다(V3로 교체된 것으로 보임).

## 검토 대기 후보 (사용자 승인 대기)

> content-designer가 [9] 단계에서 "일반화 가능하다"고 판단했지만 아직 사용자 승인을 받지 못한 후보. 승인되면 위 섹션으로 이동하고 여기서 삭제, 거절되면 사유와 함께 여기 보존(재제안 방지).

| 날짜 | 프로젝트 | 후보 규칙 | 판단 사유 | 상태 |
|---|---|---|---|---|
| - | - | - | - | - |
