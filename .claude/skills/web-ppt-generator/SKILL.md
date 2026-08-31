---
name: web-ppt-generator
description: design-rules.md(고정 규칙 + 가변 규칙)를 기반으로 HTML/CSS 웹PPT 슬라이드를 생성·수정하고, 차트/표를 렌더링한다. content-designer가 워크플로우 [5][7](웹PPT 생성/수정) 및 [9](규칙 갱신)에서 사용한다.
---

# web-ppt-generator

## 언제 사용하는가
content-designer가 [5] 웹PPT 초안 생성, [7] 피드백 반영, [9] 디자인 규칙 갱신 단계에 진입했을 때.

## 이 문서의 성격
이 문서 전체는 새 디자인 값·판단 기준을 만들지 않는다 — Hard Rule/Claude PPT Design System/Layout MD/`content-visualization-freedom.md`/`slide-structuring`(Phase B)가 이미 결정한 값·구조가 [5]/[7] 생성 과정에서 새거나 재발명되지 않도록, 그것을 브라우저에서 안정적으로 재현·집행하는 방법만 규정한다(아래 각 섹션에서 이 전제를 반복 서술하지 않는다). 각 규칙이 실제로 어떤 회귀 사례에서 나왔는지는 `references/design-decisions-log.md`에 모아두었다 — 매 호출마다 읽을 필요는 없고, 규칙의 취지가 의심스러울 때만 참조한다.

## 핵심 산출물
- `/output/{project-name}/web_ppt/v{N}/index.html` — 슬라이드 전체를 담는 진입점(섹션별 슬라이드 또는 `slides/slide-01.html` 형태로 분리 후 include, 프로젝트 규모에 따라 LLM이 선택)
- `/output/{project-name}/web_ppt/v{N}/assets/` — 이미지, 차트 데이터, 로고 등 정적 자산
- `/output/{project-name}/web_ppt/v{N}/style.css` — 공통 스타일(디자인 규칙 반영)

## 버전 스냅샷
수정할 때마다 새 버전을 만든다. 기존 버전은 삭제하지 않는다.

```bash
python .claude/skills/web-ppt-generator/scripts/new_version.py \
  --project /output/{project-name} \
  --from-latest   # 직전 버전을 복사해 새 vN 폴더 생성 (최초 생성 시에는 --scaffold)
```

- `--scaffold`: `v1/`을 templates 기반으로 새로 생성 (최초 웹PPT 생성 시)
- `--from-latest`: 가장 번호가 높은 `vN/`을 복사해 `vN+1/` 생성 (수정 시) — LLM은 복사된 폴더 위에서 diff를 적용
- 롤백: 과거 `vK/`를 `--from-latest` 대신 `--rollback-from vK` 옵션으로 지정하면 해당 버전을 복사해 새 최신 버전으로 만든다(과거 스냅샷 자체는 그대로 보존).

## 디자인 규칙 적용 원칙
`references/design-rules.md`를 항상 먼저 읽는다. 이 문서가 Hard Rule/Claude PPT Design System/Content Visualization Freedom/Layout Reference/표지 전용 규칙의 원본 경로와 **적용 우선순위**(충돌 시 이 순서)를 정의하는 단일 기준이다 — 우선순위 설명은 여기서 반복하지 않는다.

> **세션 내 재사용(같은 content-designer 실행 안에서)**: 이번 프로젝트의 [3]에서 `slide-structuring`이 같은 세션 안에서 `design-rules.md`/`Claude_PPT_Design_System.md`/`content-visualization-freedom.md`를 이미 읽었고 그 내용이 지금 컨텍스트에 남아 있다면, [5]/[7] 진입 시 다시 Read하지 않고 그 내용을 그대로 재사용한다(design-rules.md L20 "세션 내 원본 문서 재사용 원칙"과 동일 원칙을 이 진입점에도 적용). 아래 중 하나라도 해당하면 그때만 다시 Read한다.
> - 해당 원본 파일이 마지막으로 읽은 이후 수정됐을 가능성이 있는 경우(예: [9] 디자인 규칙 갱신을 거쳤거나, 파일 변경이 확인/보고된 경우)
> - 컨텍스트 압축·요약 등으로 지금 컨텍스트에 그 내용이 실제로 남아 있지 않은 경우(불확실하면 안전하게 다시 Read한다)

- **고정 규칙**(로고, 브랜드 색상, 지정 표지 등, = Hard Rule): 그대로 준수한다. 변형·생략 금지. 자산 파일은 `/docs/brand-assets/`에서 참조(프로젝트 폴더로 복사하지 말고 상대/절대 경로로 참조하거나, 배포 편의를 위해 필요 시 `assets/`로 1회 복사 후 출처를 유지).
- PPT 전체의 Visual Style, Color, Typography, Grid/Spacing, Component Style, Image Treatment, Chart/Table/Diagram Style은 Claude PPT Design System 기준을 따른다. Hard Rule과 충돌하는 부분은 적용하지 않는다.
- **Font Size 단위 처리(중요)**: Hard Rule §9/§10/§12와 Claude PPT Design System §3 Typography 표의 모든 크기 값은 **pt** 단위로 정의돼 있다. HTML/CSS로 옮길 때 `font-size`는 **pt 단위 그대로**(`font-size: 16pt` 형태) 작성하는 것을 기본으로 한다. 다른 이유로 px 단위가 꼭 필요한 경우에만 **1pt = 1.3333px** 기준으로 정확히 환산해서 쓴다 — Typography 표의 pt 숫자를 그대로 px 숫자로 옮겨 적지 않는다(예: Body 16pt를 `font-size: 16px`로 쓰는 것은 오류다 — 16px는 12pt에 불과하다. 올바른 px 환산은 16pt→21.3px, 14pt→18.7px, 18pt→24px, 20pt→26.7px). 이 문서 다른 곳(padding/width/gap 등)이 대부분 px 단위라는 이유로 font-size도 습관적으로 px을 쓰지 않도록 특히 주의한다.
- 슬라이드별 표현 방식(레이아웃, 표/그래프/다이어그램/이미지/텍스트 선택 등) 판단은 Content Visualization Freedom의 Allowed/Not Allowed 범위 안에서만 이루어진다 — Hard Rule·Claude PPT Design System을 벗어나는 판단은 허용되지 않는다.
- **레이아웃 선택 절차**: design-rules.md "레이아웃 선택 기준 > Layout Routing 판단 순서"를 그대로 따른다 — 표지 슬라이드는 표지 전용 규칙을 우선 적용(L01~L33 미참고)하고, 그 외에는 Relationship/Visual Strategy 판단 → `special-layout-index_V1.md`로 후보 1~2개로 좁혀 원본 MD만 상세 Read → 해당 없으면 `layout-catalog_V1.md`(L01~L33) 순으로 진행한다. 여기서 절차를 다시 설명하지 않는다.
- **가변 규칙**(레이아웃, 표/차트 스타일, 정보 시각화, 강조 방식): 레퍼런스 자료에서 파악한 장점을 슬라이드 목적에 맞게 해석해 적용한다. 이 해석·선택은 위 Claude PPT Design System·Content Visualization Freedom·Layout Reference 기준을 벗어나지 않는 범위에서 이루어진다.
  - `design-rules.md`에 가변 규칙이 아직 없는 프로젝트(최초 사용)라면, 업로드된 레퍼런스 자료를 분석해 초안 규칙을 제안하고 content-designer가 메인을 통해 사용자 확인을 받는다. 확인 전까지는 `design-rules.md`에 반영하지 않고, 해당 세션 내에서만 임시로 적용한다.
  - 레퍼런스 간 스타일이 상충하면 임의 선택 금지 — 메인을 통해 사용자에게 선택지를 제시한다.
- 원본 이미지는 그대로 사용. 디자인 통일성을 위한 크롭·색보정만 허용, 합성·수치 변형 금지.
- 원본 수치·데이터는 `material_analysis.json`/`slide_outline.md`와 정확히 일치해야 한다. 임의로 반올림·재해석하지 않는다. `[확인필요]` 표시가 있는 값은 슬라이드에도 동일하게 `[확인필요]`로 노출한다.

## 생성 전 Implementation Contract 확인 (Pre-Generation Contract Check)
> HTML을 쓰기 전에 슬라이드마다 한 번 확인만 한다.

`slide_outline.md`에서 슬라이드마다 아래를 확인한다(이 문서에서 새로 판단하지 않고, 이미 기록된 내용을 그대로 가져온다):
- Core Claim(들)
- Required Evidence / Optional Evidence — 관계형이면 관계를 이루는 값 전체
- Relationship 유형
- Selected Layout
- (해당하면) 사용하기로 확정된 실제 Image/Asset

이어서 이 Relationship에 `content-visualization-freedom.md`의 Relationship → Visual Strategy 기준을 적용해, 이번 생성에서 취할 Visual Strategy 방향을 정한다(구체적 Chart/Diagram 형태는 여기서 고정하지 않음 — Relationship을 보존하는 범위 안에서 자유롭게 판단).

### Required Evidence 보존
- Required로 표시된 Evidence는 생성 과정에서 임의로 삭제·축약하지 않는다.
- 관계형 Evidence는 관계를 이루는 값 전체(예: 이전 상태·중간 상태·이후 상태, 또는 단계별/구성요소별 값)를 실제 HTML에 반영한다 — 대표값 하나만 남기는 것으로 대체하지 않는다.
- 공간이 부족해 Required Evidence를 모두 구현하기 어려우면 아래 순서로 처리하고, 임의로 생략하지 않는다.
  1. 같은 Selected Layout 안에서 배치·크기·밀도를 재구성해 공간을 확보한다(Layout 자체는 바꾸지 않음).
  2. 그래도 안 되면 Layout 자체가 이 Evidence를 수용하기 어렵다고 판단한 것이므로, 여기서 임의로 다른 Layout으로 바꾸지 않는다 — 아래 "생성 후 QA 절차"의 재검증·에스컬레이션 경로를 따라 Layout 재검토가 필요하다는 사실을 기록해 메인/사용자에게 이관한다.
  3. 그래도 처리되지 못한 경우 어떤 Required Evidence를 왜 구현하지 못했는지 `slide_outline.md`의 Structural Check 아래에 기록한다.
- Optional Evidence는 공간·정보 위계에 따라 생략할 수 있다.

### Visual Strategy 보존
- Relationship이 관계형이고 `content-visualization-freedom.md`가 그에 대해 Visual Strategy 방향(예: Comparison/Trend/Progression/Contribution/Cause-Effect/Cycle/Process 등)을 제시했다면, 구현 편의를 이유로 Large Number·단순 Text·균질한 Stat Grid로 임의 대체하지 않는다.
- Visual Strategy는 특정 Chart 하나를 강제하지 않는다 — 그 Relationship을 보존하는 범위 안에서는 구체적 표현 형태(Bar/Line/Diagram/이미지 페어 등)를 이 단계에서 자유롭게 선택한다.

### Image/Asset 보존
- Required Evidence Visual로 확정된 실제 이미지는 실제 HTML에서 사용됐는지 확인한다.
- Optional 이미지는 공간·정보 위계에 따라 생략할 수 있으나, 생략 대신 관련성이 낮은 다른 이미지를 빈 공간을 채우기 위해 임의로 쓰지 않는다(`content-visualization-freedom.md`의 이미지 자산 활용 기준과 동일한 원칙).
- **Supporting Visual Value**: Optional/Supporting Visual은 관련이 있더라도 "공간이 남아서"라는 이유만으로 넣지 않는다 — Primary Visual과 내용이 중복되거나, 있어도 핵심 메시지 이해를 실질적으로 높이지 못하면 생략한다. "Primary와 겹치지 않는 정보를 담고 있는가"만으로 유지 여부를 판단하지 않는다 — 그 추가 정보 가치가 슬라이드 전체 Composition의 복잡도 증가(Region 수·시각적 밀도 상승)보다 실질적으로 큰지까지 비교해서 판단한다. 이 판단은 위 "Required Evidence 보존"과 마찬가지로 Region 배치를 정하기 전에 하며, 생략 시에도 원본 Evidence 자체는 삭제하지 않고 텍스트로는 남길 수 있다.
- **Supporting Visual을 유지하기로 한 경우의 배치**: 남는 빈 공간에 끼워 넣는 방식으로 배치하지 않는다 — Primary Visual과 의미적으로 연결돼 있다면 Claude PPT Design System "Content Density / Content Group 원칙"(기존 규칙, 새로 만드는 것 아님)에 따라 두 Visual을 하나의 Content Group으로 묶어(간격을 좁게, 위·아래 등 자연스러운 배치로) 정보 구조상 더 응집되어 보이도록 구성할지 먼저 검토한 뒤 Region을 정한다. Primary Visual보다 작게 표시해 위계 차이는 유지한다.

### Layout 내부 Visual 구성의 다양성
- Selected Layout은 슬라이드 전체 구조를 결정할 뿐, Layout 내부 각 Region/Column의 표현 방식까지 하나로 통일하라는 의미가 아니다.
- 같은 Layout 안에서도 각 Region/Column은 자신에게 매핑된 Claim → Evidence → Relationship → Visual Strategy를 기준으로 표현 방식을 독립적으로 판단한다 — 예를 들어 같은 병렬 구조 안에서도 비교 데이터가 있는 Region은 비교 표현을, 단일 KPI뿐인 Region은 Large Number를, 실제 이미지가 Evidence인 Region은 이미지를, 순차 관계가 있는 Region은 작은 Process/Flow 표현을 각각 취할 수 있다.
- Layout MD가 내부 Visual 슬롯을 특정 표현 방식으로 이미 제한하고 있다면 그 제한을 그대로 따르고, 제한이 없는 자리는 해당 Region의 Visual Strategy를 우선 구현한다.
- 다양성 자체를 목적으로 표현 방식을 임의로 섞지 않는다 — 각 Region의 Evidence·Relationship이 실제로 다른 표현을 요구할 때만 다르게 한다. 동일한 역할·정보 구조의 병렬 Region은 여전히 기존 Parallel Layout Alignment 등 시각적 일관성 규칙을 지킨다.
- 구현 편의를 위해 모든 Region을 동일한 패턴(예: 전부 Icon+Text, 전부 Number+Text, 전부 Text Card)으로 단순화하지 않는다.

### 전용 Layout의 구조 규칙 우선 적용 (Dedicated Layout Structure Enforcement)
> [3]에서 이미 확정된 Selected Layout이 [5]/[7] 구현 단계에서 다른 구조로 새는 것을 막는 절차 규칙이다(사유: `references/design-decisions-log.md#flow-diagram-region-map-drift`).

- Selected Layout이 `docs/slide-design-rules/`의 전용 Layout Reference 문서(예: `flow-diagram-rules.md`, `before-after.md`, `020_organization.md` 등 — Reference-Locked 여부와 무관하게 특수 Layout Reference 전체에 적용)를 가리키면, 그 문서가 정의하는 **Region Map(좌표/비율)·방향(가로/세로)·Connector 처리 방식·Branch 구조**는 이번 슬라이드의 구현 명세로 취급한다 — 참고용 예시가 아니라 실제로 재현해야 하는 구조다.
- **L01~L33 카탈로그 Layout에도 동일 적용**: 이 원칙은 위와 같은 전용 MD가 없는 `layout-catalog_V1.md`(L01~L33) Layout에도 그대로 적용된다 — 전용 Must Preserve 문서가 없더라도, 원본 Reference(`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`의 해당 슬라이드)에서 명확히 확인되는 주요 Region의 역할과 좌우·상하 배치 관계(예: Main Visual Region ↔ Text/Insight Region)는 기본 구조로 그대로 보존한다.
- **Primary/Optional Visual의 Region 배치**: Required로 확정된 Primary Visual은 원본 Reference가 지정한 Main Visual Region에 우선 배치한다. Optional/Supporting Visual은 원본 Reference에 별도 Supporting Visual Region이 있거나, 기존 Region 구조를 변형하지 않고 배치할 수 있는 경우에만 추가한다 — 이를 위해 Main Region의 좌우 관계를 반전하거나, Primary Visual을 축소하거나, 원본에 없는 새 Column/Region을 임의로 만들지 않는다(사유: `references/design-decisions-log.md#l07-primary-visual-reversed`).
- **Image Legibility(반대 방향의 축소·확대 왜곡 금지)**: Region을 채우기 위해 Primary Visual을 원본 해상도·포함된 텍스트가 깨지는 수준까지 무리하게 확대하지 않는다 — Main Visual Region이라고 해서 반드시 그 공간을 가득 채워야 하는 것은 아니며, 원본 이미지의 실제 해상도와 이미지 안에 포함된 텍스트(도표 라벨 등)가 읽을 수 있는 크기를 유지하는 선에서 배치한다. 판단 기준은 "원본 픽셀 크기보다 확대했는가"라는 수치 비교 하나로 끝내지 않는다 — 실제 렌더링된 화면에서의 체감 화질(확대율이 낮아도 원본 이미지 자체의 정보 밀도가 높으면 체감상 흐려 보일 수 있음), 그리고 슬라이드 전체의 Visual Balance(다른 Region·텍스트와 비교한 상대적 크기가 과도하지 않은지)까지 함께 본다.
- **Supporting Visual과의 크기·배치 균형**: Primary Visual을 위 기준으로 조정할 때, Optional/Supporting Visual과 텍스트를 포함한 전체 배치 균형을 함께 재검토한다 — Primary와 Supporting의 상대적 중요도 차이(Required vs Optional)가 시각적 크기·비중 차이로도 유지되도록 조정한다.
- **Visual Region Utilization(과소 활용 금지 — 위 Image Legibility의 반대 방향)**: 이미지가 배치되는 Region은 위 Image Legibility 기준(원본 해상도·내부 텍스트 가독성, Visual Balance)을 지키는 범위 안에서 가용 공간을 최대한 채운다 — Region과 원본 종횡비가 다르다는 이유만으로 불필요한 배경색/회색 박스, 과도한 padding, 빈 wrapper 영역을 만들어 이미지를 실제보다 작게 표시하지 않는다. 이미지 주변을 박스로 채우는 것보다 이미지 자체를 충분히 크게 보여주는 쪽을 우선한다. 여러 이미지가 하나의 Visual Region을 공유할 때는(사유: `references/design-decisions-log.md#shared-visual-region-uneven-boxes`) 동일한 박스 크기를 기계적으로 강제하지 않는다 — 각 이미지의 원본 비율과 내부 가독성을 유지하면서 전체 Region이 안정적으로 차도록 크기·배치를 조정한다(단, Before/After Variant B 등 Layout MD가 동일 폭 Column을 명시적으로 요구하는 경우는 그 규칙이 우선한다 — 위 "Table 동일 폭 Column" 참조). 이 Region의 Caption/출처 표시는 위 "Caption/Source Annotation Tier의 배치" 기준대로 원본 이해·출처 표기에 실제로 필요한 경우에만 유지하고, 본문에서 이미 설명된 내용을 반복하거나 있음으로써 Visual 영역을 불필요하게 축소시킨다면 생략한다.
- 콘텐츠와 원본 Reference 구조가 명확히 충돌해 위 두 원칙을 지킬 수 없는 경우, 여기서 임의로 구조를 재설계하지 않는다 — 위 "생성 전 Implementation Contract 확인 > Required Evidence 보존"의 처리 순서(같은 Layout 안에서 재구성 → 안 되면 Layout 재검토 필요성 기록·이관)를 따라 Layout 재선택 대상으로 다룬다.
- **Must Preserve 체크리스트 사전 발췌(Structure Contract)**: 위 Layout MD(또는 Implementation Reference)에 "Must Preserve/필수 정보/Layout-Specific Hard Rules/필수 Region" 등의 이름으로 명시된 섹션이 있으면, 이 세션에서 해당 Layout을 처음 쓰는 슬라이드의 **HTML 작성 전에** 그 섹션 항목을 원문 그대로(요약·재해석 없이) `<프로젝트>/.qa/v{N}/layout-checklist/{layout-slug}.md`에 발췌해 저장한다 — 아래 "1. Layout Compliance Check > Layout MD 재독 최소화"가 QA에서 쓰는 것과 **동일한 파일**이며, 이 시점에 만든 파일을 QA가 그대로 재사용한다(중복 발췌 없음). 이 체크리스트에 적힌 항목은 이번 슬라이드 HTML의 **필수 구조 조건**이다 — 구현 편의를 위해 일반 Column/Card 구조로 단순화하며 생략하지 않는다. 콘텐츠상 그 항목을 그대로 구현하기 어려운 명확한 이유가 있는 경우에만 예외로 생략할 수 있으며, 이때는 어떤 항목을 왜 생략했는지 `slide_outline.md`의 Structural Check 아래에 기록한다(위 "Required Evidence 보존"의 처리 원칙과 동일). 이런 이름의 섹션이 없는 Layout MD는 기존대로 본문 서술만 참고한다(모든 특수 Layout에 이 체크리스트를 강제하지 않음).
- **Implementation Reference 우선 참조**: 위 Layout MD와 같은 폴더에 그 MD 전용 Implementation Reference 파일(원본 pptx/디자인 파일에서 실측한 좌표·도형 종류·Connector 형태를 일반화 없이 정리한 문서 — 예: Flow Diagram의 [`flow-diagram-implementation-reference.md`](../../../docs/slide-design-rules/flow-diagram-implementation-reference.md))이 등록되어 있으면, HTML 좌표를 계산할 때 Layout MD 본문의 비율 서술(Region Map 등)이 아니라 **이 Implementation Reference 파일을 1차 소스로 읽는다** — pptx 원본을 매 슬라이드마다 다시 열어 분석하지 않기 위해 이미 1회 추출·정리해 둔 결과물이다. 두 문서의 수치가 다르면 Implementation Reference 값을 따른다. 아직 이런 파일이 없는 Layout은 기존대로 Layout MD 본문만 따른다(모든 특수 Layout에 이 파일을 강제하지 않음).
- **구현 골격(Component Skeleton) 우선 재사용**: 같은 폴더(`scripts/templates/components/`)에 그 Layout 전용 HTML/CSS 골격 파일이 등록되어 있으면(예: Flow Diagram의 [`flow-diagram.css`](scripts/templates/components/flow-diagram.css) + [`flow-diagram.html`](scripts/templates/components/flow-diagram.html), Three-Column의 [`three-column.css`](scripts/templates/components/three-column.css) + [`three-column.html`](scripts/templates/components/three-column.html)), 반복되는 CSS 클래스·SVG/DOM 구조를 매번 새로 타이핑하지 않고 이 파일 내용을 그대로 복사해 시작한다 — Node/분기/Lane 개수, 실제 좌표(Implementation Reference 값), 콘텐츠·이미지는 이 골격이 정하지 않으므로 그대로 채워 넣는다. 골격이 커버하지 못하는 구조(예: 이 골격에 없는 새로운 Connector 패턴)는 위 Layout MD·Implementation Reference의 규칙에 따라 필요한 부분만 확장한다 — 골격에 맞추기 위해 Layout MD의 구조 규칙을 임의로 바꾸지 않는다. 아직 골격 파일이 없는 Layout은 기존대로 Layout MD/Implementation Reference만 보고 HTML/CSS를 작성한다.
- 다른 슬라이드/다른 Layout을 위해 이미 만들어 둔 공용 컴포넌트(예: Process+Comparison의 가로 Step Box+화살표, Before-After의 Step Box+Connector 시퀀스)를 겉모습이 비슷하다는 이유로 그대로 가져와 이번 Layout MD의 구조를 대신하지 않는다. 기존 컴포넌트를 재사용하려면, 그 컴포넌트의 방향·Connector 분절/연속 규칙·Branch 처리 방식이 이번에 적용할 Layout MD의 요구사항과 실제로 일치하는지 먼저 대조하고, 일치하지 않으면 재사용하지 않고 그 Layout MD의 규칙대로 새로 구현한다.
- 이 확인(Region Map 취급 + 위 Must Preserve 체크리스트 발췌)은 HTML 작성 **전에** 한다(위 "생성 전 Implementation Contract 확인"에서 Selected Layout을 확인하는 시점과 동일한 단계). 작성 후 QA(아래 "1. Layout Compliance Check")는 이 확인이 실제로 지켜졌는지 재검증하는 역할이며, 사전 확인을 대체하지 않는다.

## 구현 기준 (HTML/CSS Implementation Standards)
> Hard Rule/Claude PPT Design System/Layout MD가 이미 정한 값(색상·두께·비율·Font Size 등)은 그대로 유지하며, 아래는 그 값을 브라우저에서 안정적으로 재현하기 위한 구현 방식만 규정한다(사유: `references/design-decisions-log.md#html-css-implementation-defects`).

### 한글 줄바꿈
- 한국어 일반 본문(Body/Supporting Text/Evidence/Caption 등 모든 문장형 텍스트)에는 기본적으로 `word-break: keep-all;`을 적용해 단어(어절) 중간에서 부자연스럽게 끊기지 않도록 한다. 기본 템플릿(`scripts/templates/style.css`)의 `body`에 전역 기본값으로 설정돼 있으므로, 개별 컴포넌트 스타일에서 이를 덮어써 끄지 않는다.
- 줄바꿈으로 인한 레이아웃 문제를 Font Size 축소로 해결하지 않는다 — Claude PPT Design System §3 "Font Size 적용 원칙"의 해결 순서(문장 압축 → 불필요한 내용 제거 → 줄 수 조정 → Gap 조정 → Visual 크기 조정 → Layout 재검토)를 그대로 따른다.

### Divider 서브픽셀 렌더링
- Hard Rule §10/§11이 정의한 Divider 두께 값(예: §11 Vertical Content Divider 0.5pt)은 변경하지 않는다.
- 브라우저는 1px 미만 서브픽셀 두께를 안티앨리어싱으로 완전히 지워버리는 경우가 있다(예: 0.5pt ≈ 0.66px). **웹 렌더링(HTML/CSS)에 한해서만** 실제 스크린샷에서 보이지 않으면 최소 1px로 fallback한다 — 색상·Gradient·위치 등 그 외 스펙은 원래 값을 그대로 유지한다. pptx 변환은 벡터 기반이라 이 fallback을 적용하지 않고 Hard Rule 원래 pt 값을 그대로 사용한다.
- 아래 "생성 후 QA 절차"의 Visual Quality Check에서 Divider·구분선의 실제 가시성을 스크린샷으로 확인한다.

### Table 동일 폭 Column
- 동일 역할의 Target Column(예: Table Comparison의 여러 대상 Column, Before/After 표의 Existing/Improved 등 Layout MD가 "동일 폭"을 요구하는 Column)은 브라우저의 auto table layout에 맡기지 않는다.
- `<colgroup>` + `table-layout: fixed`로 각 Column에 명시적 `width`(%)를 지정해 콘텐츠 길이와 무관하게 폭이 고정되도록 구현한다.
- 구체적인 Column 비율(예: Criteria 20% : Target 39% : Target 41%)은 이 문서가 정의하지 않으며, 해당 Layout MD(`table-comparison.md`, `before-after.md` §5.1 등)의 값을 그대로 따른다.

### 아이콘 렌더링
- PPT용 아이콘에 Unicode 이모지 문자를 사용할 때, 브라우저가 컬러 이모지(예: 광택 있는 3D 구체)로 렌더링해 Design System의 Flat/브랜드 컬러 아이콘 톤과 어긋나는 경우가 있다.
- 적절한 SVG 아이콘 또는 브랜드 자산(`/docs/brand-assets/`)이 있으면 그것을 우선 사용한다.
- Unicode 심볼을 불가피하게 써야 하면 text presentation 선택자(VS15, `U+FE0E`)를 붙여 컬러 이모지 렌더링을 억제하고 지정된 브랜드 컬러를 그대로 적용한다.

### 공용 컴포넌트 재사용 (Shared Component Reuse)
> 이미 Hard Rule/Claude PPT Design System이 정한 값을 슬라이드마다 따로 재작성하지 않고 재사용하기 위한 구현 방식만 규정한다(사유: `references/design-decisions-log.md#shared-component-reinvention`).

- **동일 의미 역할 Box는 하나의 공용 클래스로 통합**: Insight Box·Conclusion/Takeaway Box·Key Message Box처럼 여러 슬라이드가 같은 의미 역할(Claude PPT Design System §2 Content Relationship의 Conclusion/Takeaway, Shared Supporting 등)로 쓰는 강조 박스는 슬라이드마다 `.sN-*` 접두사로 새로 스타일링하지 않고, 프로젝트 `style.css`에 공용 클래스(예: `.insight-box`) 하나로 정의해 재사용한다. 스타일 값은 새로 만들지 않고 Claude PPT Design System §6 "RoundRect Card/Tag" 스펙(라운드 radius 소–중, 배경 White 또는 Tint, 테두리 없음 또는 1px Neutral, 좌측 컬러 바 등 장식적 accent border 금지)을 그대로 적용한다.
- **Caption/Source Annotation Tier의 배치**: Claude PPT Design System §3 Typography Tier가 이미 정의한 "Source/Footnote/각주"(12pt Light, Deck 전체에서 가장 낮은 위계, 프로젝트 공용 클래스가 있으면 그것을 재사용 — 예: `.footnote-block`)에 해당하는 이미지 출처·자료 설명 등은 이미지 바로 아래처럼 Main Content Region 안에 본문처럼 배치하지 않는다 — 슬라이드 하단의 공통 Footnote/Source 영역에 배치하는 것을 우선 검토한다. Chart Axis Label/Legend 등 "Caption/Auxiliary" Tier(14pt)와는 의미가 다르므로 섞어 쓰지 않되, 시각적 위계는 둘 다 Main Content보다 낮은 공통 Annotation Tier로 유지한다.
- **Insight/Conclusion Box의 배치 범위**: 이 Box가 특정 Region/Column 하나만의 결론이 아니라 슬라이드의 여러 병렬 Region(예: 좌우 Main Visual+Text 두 영역)을 함께 종합하는 결론이면, 그중 한쪽 Column 내부에 임의로 끼워 넣지 않는다 — Claude PPT Design System §5 "Integrated Conclusion" 원칙(이미 정의된 규칙, 새로 만드는 것 아님)에 따라 특정 Column에 속하지 않고 전체 병렬 Content Group의 폭을 기준으로 하단에 배치한다.
- **역할이 다른 Box까지 억지로 통합하지 않는다**: Header Bar(Hard Rule §10), Table Header Row(§10B), Process/System Architecture의 Node, Layout MD가 고유하게 정의한 Box(예: Timeline Milestone Node)는 위 공용 Box와 의미 역할이 다르므로 통합 대상이 아니다 — "강조 박스처럼 보인다"는 이유만으로 하나의 클래스로 묶지 않는다.
- **Body Text는 Typography Tier 그대로 사용**: Claude PPT Design System §3 Typography Tier(Body 16pt 등)를 그대로 사용하고, 공간이 부족하다는 이유로 특정 슬라이드의 Body 텍스트만 14~15pt 등으로 임의 축소하지 않는다 — 공간 문제는 위 "한글 줄바꿈" 절이 가리키는 §3 "Font Size 적용 원칙"의 해결 순서(문장 압축 → 불필요한 내용 제거 → 줄 수 조정 → Gap 조정 → Visual 크기 조정 → Layout 재검토)를 따른다.
- **이미 있는 공용 클래스 우선 재사용**: 이번 프로젝트의 `style.css`에 이미 동일 역할의 공용 클래스(Typography/Stat/Box뿐 아니라 Divider(`.v-divider`), 공통 Header System 요소, Card 등 포함, 예: 강조 수치용 `.t-stat`류)가 정의돼 있다면, 슬라이드 전용 클래스를 새로 만들어 동일한 폰트·색상·크기·두께 값을 다시 타이핑하지 않고 그 공용 클래스를 그대로 재사용(마크업에 함께 지정하거나 상속)한다. 슬라이드 전용 클래스(`.sN-*`)는 그 슬라이드만의 고유한 배치(위치·간격·너비 등)에만 쓰고, 다른 슬라이드와 공유되는 시각 스펙(폰트·색상·Box 스타일·Divider 두께 등)을 다시 정의하는 용도로 쓰지 않는다.

## 상세 데이터 표 처리
원본 표가 수십 행 이상(`needs_appendix: true`)이면:
1. 슬라이드 본문에는 핵심 행·열만 선별해 표시 (선별 기준: 발표 스토리라인상 강조할 수치, 이상치, 요약 행 등 — content-designer가 [3] 단계에서 결정한 기준을 따름)
2. 전체 표는 별도 부록 슬라이드(`appendix`)로 추가
3. 선별 과정에서 표시되는 수치 자체는 변경하지 않는다.

## 차트 렌더링
- 웹PPT에서는 **Chart.js**로 인터랙티브 렌더링한다. `scripts/vendor/chart.min.js`를 로컬에 두고 `<script src="../../assets/vendor/chart.min.js">`로 참조한다 (CDN 미사용 — 오프라인·로컬 처리 원칙 준수). 최초 셋업 시 `scripts/vendor/`에 Chart.js 파일을 1회 내려받아 배치해야 한다(현재 리포지토리에는 포함되어 있지 않음 — README 참고).
- 차트에 쓰이는 수치는 `material_analysis.json`에서 추출된 원본 값을 그대로 사용한다. 원본 수치를 추출할 수 없는 차트(`charts_detected`)는 새 차트를 그리지 않고 원본 이미지를 `<img>`로 삽입한다.
- pptx 변환 단계에서 네이티브 차트/이미지 중 무엇으로 변환할지 판단할 수 있도록, 차트를 감싸는 요소에 `data-chart-mode="native|image"` 힌트 속성과 원본 데이터(`data-chart-json`)를 함께 남긴다.

## 생성 후 QA 절차 (Post-Generation QA)
> Hard Rule/Claude PPT Design System/Content Visualization Freedom/Layout Reference는 항상 원본 경로를 다시 읽어 대조하며, 규칙 본문을 이 문서에 복사하지 않는다. `slide-structuring`의 [3] 판단이나 `pptx-exporter`의 [8] 변환 검증(슬라이드 수·요소 일치·파일 무결성)과 역할이 겹치지 않도록, 이 절차는 [5]/[7]에서 HTML/CSS를 생성·수정한 직후에만 적용한다.

> **경량화 원칙(2026-08-24)**: 자동 QA는 **기계적으로 신뢰성 있게 판정 가능한 항목**(canvas overflow, text clipping, 최소 font size 위반, 명확한 object overlap, render/HTML 오류, broken image/resource, Layout MD 대비 수치 불일치)만 다룬다. **AI의 시각적·의미적 재판단이 필요한 항목**(전체 슬라이드 육안 재검토, screenshot 반복 Read, crop→확대→재판단, 디자인 균형/미관 판단, Layout Reference와의 육안 유사도, 이미지 의미 적합성 반복 Vision 검토, Content Fidelity uncertain/ambiguous flag의 추가 조사)은 자동 QA에서 수행하지 않고 Human Review ②([6])로 그대로 넘긴다. 실행 흐름은 **Web PPT 생성 → 기계적 QA 1회 → 확정 오류 수정 → 수정 슬라이드만 부분 QA → Human Review ②**로 고정하며, 부분 QA가 clean이면 그 시점에서 종료한다 — 통과를 재확인하기 위한 Final Full QA(전체 재렌더링·재감사)는 수행하지 않는다.

`v{N}`을 새로 만들거나 수정했으면, **그때 생성·수정된 슬라이드마다** 아래 순서로 QA를 수행한다. 단, [5] 최초 웹PPT 생성이 전체 슬라이드에 대해 처음 완료된 시점(v1)에는 아래 "0. 최초 생성 후 전체 QA"를 먼저 1회 수행한 뒤 슬라이드별 절차로 들어간다. [7] 이후의 수정 라운드에서는 이 전체 QA를 반복하지 않고 그때 변경된 슬라이드만 재검증하는 것이 기본이며, "0-b. 전체 QA 재실행이 필요한 경우"(공통 CSS/Template 등 전체 슬라이드에 영향을 주는 요소 변경)에 해당할 때만 예외적으로 전체 QA를 다시 수행한다.

### 0. 최초 생성 후 전체 기계적 QA (1회, [5] 최초 생성 직후에만)
> 아래 검출 항목(Layout/Overflow/Clipping/Typography/Overlap/Content Fidelity) 자체는 줄이지 않는다 — 이 절은 그 항목들을 **언제·몇 번** 전체 범위로 도는지만 규정하며, 전부 기계적 검사다(스크린샷 육안 검토 없음).

- `python scripts/qa_render.py --web-ppt <web_ppt/v1> --out <프로젝트>/.qa/v1 --audit-fonts --audit-layout`(`--slides` 생략 시 전체 슬라이드 대상)로 전체 슬라이드의 Typography(1-b)와 Layout/Overflow/Clipping/Overlap(2-a)을 한 번의 배치 호출로 함께 감사한다.
- `content_fidelity_qa.py`도 `--slides` 없이(전체 슬라이드 대상) 1회 실행해 Content Fidelity(1-d)를 함께 확인한다.
- 위반 판정 기준은 각각 아래 "1-b. Typography Compliance Check"/"2. Visual Quality Check"/"1-d. Content Fidelity QA"와 동일하다.
- 이 전체 감사에서 발견된 위반 중 **확정적으로 판정 가능한 것만** 아래 "3. 자동 수정 범위" 안에서 즉시 수정하고, **수정한 슬라이드에 한해서만** 1·1-b·1-c·1-d·2-a를 재수행한다 — 전체 슬라이드를 다시 렌더링·재감사하지 않는다.
- 이 최초 전체 패스 이후 부분 QA(변경된 슬라이드만)가 clean으로 통과하면 그 시점에서 해당 버전의 QA는 종료하고 Human Review ②로 넘긴다. 통과를 다시 확인하기 위한 별도의 "최종 전체 QA 재렌더링/재감사"는 추가로 수행하지 않는다.
- [7] 이후 부분 수정 라운드에서는 이 0번 단계(전체 범위 실행)를 원칙적으로 다시 수행하지 않는다 — 그때 생성·수정된 슬라이드 번호만 기존 1·1-b·1-c·2-a와 Content Fidelity QA(1-d) 대상으로 삼는다(단일 슬라이드 HTML/콘텐츠 수정은 해당 슬라이드만). 아래 0-b 예외에 해당하는 경우만 전체 범위로 되돌아간다.

#### 0-b. 전체 QA 재실행이 필요한 경우 (예외)
[7] 이후 라운드라도 아래에 해당하는 변경이면 이번에 손댄 슬라이드만이 아니라 **전체 슬라이드**를 대상으로 위 "0. 최초 생성 후 전체 QA"를 다시 1회 수행한다 — 여러 슬라이드가 공유하는 기반이 바뀐 것이므로 영향 범위를 변경된 슬라이드 번호만으로 좁힐 수 없기 때문이다.
- 여러 슬라이드가 함께 참조하는 `style.css`의 전역/공용 클래스(공통 컴포넌트, Header/Divider 등) 변경
- `scripts/templates/`의 공통 템플릿 변경
- Hard Rule/Claude PPT Design System/Layout Reference 등 design-rules.md가 참조하는 상위 규칙 문서 원본의 변경
- 그 외 다수 슬라이드가 공유하는 공통 컴포넌트·공통 Layout 구조의 변경

단일 슬라이드의 HTML/콘텐츠, 그 슬라이드 전용 인라인 스타일, 또는 다른 슬라이드가 참조하지 않는 로컬 CSS 클래스만의 수정은 이 예외에 해당하지 않는다 — 그 슬라이드 번호만 재QA한다.

### 1. Layout Compliance Check
1. `slide_outline.md`에서 해당 슬라이드의 **Selected Layout**을 확인하고, 실제 HTML의 구조(클래스명·요소 구성)가 그 Layout과 일치하는지 대조한다.
2. Selected Layout이 가리키는 Layout MD 원본(`docs/slide-design-rules/...` 또는 `layout-catalog_V1.md`)을 확인하고, 그 문서가 Must Preserve/Avoid로 명시한 핵심 규칙과 Divider·Column/Target 폭 비율·Alignment·Width/Height·Header·Visual 비중 관련 수치를 실제 CSS 값과 하나씩 대조한다 — **이번 세션에서 이미 이 Layout MD를 읽고 대조한 적이 있다면 다시 Read하지 않고, 아래 "Layout MD 재독 최소화" 절차에 따라 재사용한다.** **"이 요소가 존재하는가"가 아니라 "명시된 세부 스펙(예: Divider의 Gradient·inset%, 동일 역할 Column의 동일 폭, Header의 정확한 pt/색상)대로 구현됐는가"까지 확인한다** — 이미 규칙에 맞는 공용 CSS 클래스(예: `.v-divider`, `.content-header-bar`)가 파일에 정의돼 있다면, 슬라이드가 그 클래스를 실제로 참조하는지, 아니면 별도 인라인 스타일로 재구현해 스펙이 새어나가지 않았는지도 확인한다. 문서 전체를 옮겨 적지 않고, 이 슬라이드에 실제로 적용된 값(Fill 여부, 정렬, 폭 비율, Gap 등)만 확인한다.
3. 위 대조에서 Hard Rule 또는 Claude PPT Design System(특히 §5 Content Density/Parallel Layout Alignment 원칙, §8 Table Style)과 Layout MD의 세부값이 다르면, `design-rules.md`의 우선순위(Hard Rule > Design System > Content Visualization Freedom > Layout Reference)에 따라 상위 문서 값을 기준으로 판단한다.

#### Layout MD 재독 최소화 (세션 내 1회 원칙)
> design-rules.md "세션 내 원본 문서 재사용 원칙"을 Layout MD에 적용한 절차다. 매 슬라이드 QA마다 같은 Layout MD 원본을 통째로 다시 Read하지 않기 위해, 위 "전용 Layout의 구조 규칙 우선 적용 > Must Preserve 체크리스트 사전 발췌"에서 만든 `<프로젝트>/.qa/v{N}/layout-checklist/{layout-slug}.md`를 QA도 그대로 재사용해 실제 CSS 값과 대조한다(새로 만들지 않음). 그 파일이 아직 없는 경우(사전 발췌 대상이 아니었거나 도입 이전 슬라이드를 다시 QA하는 경우)에만 최초 대조 시 그 발췌 절차를 동일하게 수행한다.

- 체크리스트에 없는 항목을 새로 확인해야 하면 원본 Layout MD를 다시 연다 — 체크리스트에 없다고 임의로 판단하거나 생략하지 않는다.
- 체크리스트는 원본 Layout MD의 발췌본일 뿐 새로운 판단 기준이 아니다. 체크리스트 값과 원본이 어긋난다고 의심되면(발췌 누락·오기 가능성) 바로 원본을 다시 읽어 확인하고, 원본이 항상 우선한다.
- 새 실행 세션(새로운 content-designer 호출)에서는 과거 세션이 남긴 체크리스트를 그대로 신뢰하지 않는다 — 해당 Layout을 다시 쓰는 첫 슬라이드에서(생성 단계든 QA 단계든, 이번 세션에서 먼저 마주치는 시점에) 원본 Layout MD를 1회 다시 읽어 확인한 뒤, 필요하면 체크리스트를 갱신한다(세션 간 캐시 없음).

### 1-b. Typography Compliance Check
`scripts/qa_render.py --audit-fonts`로 대상 슬라이드의 **실제 computed font-size**(코드에 적힌 값이 아니라 브라우저가 최종 계산한 값)를 pt 단위로 추출한다: `python scripts/qa_render.py --web-ppt <web_ppt/vN> --out <프로젝트>/.qa/vN --slides <번호> --audit-fonts`(스크린샷과 함께 `<프로젝트>/.qa/vN/font-audit.json` 생성). 이 결과를 Hard Rule §9/§10/§12·Claude PPT Design System §3 Typography 표와 대조해 아래를 위반으로 판정한다 — 코드의 `font-size` 선언값이 아니라 이 audit의 실측 pt 값 기준으로 판단한다.
- Source/Footnote/각주 역할이 **아닌** 텍스트가 14pt 미만인 경우
- Body(일반 본문/Supporting Text/Evidence) 역할 텍스트가 16pt 미만인 경우
- Main Title Supporting Message가 20pt가 아닌 경우
- Content Comparison Header(Before/After·Three-Column·Benefit-Impact 분할 Header 등 Hard Rule §10 대상)가 20pt가 아닌 경우
- 동일 역할의 Stat Number가 슬라이드/컴포넌트마다 서로 다른 pt 값을 쓰는 경우(24~30pt 범위 자체를 벗어나는 것도 함께 확인)
- Source/Footnote/각주 역할 텍스트가 12pt 미만인 경우

위반이 발견되면 해당 CSS 값을 pt 단위 기준값으로 고친다(px를 써야 한다면 1pt=1.3333px로 정확히 환산) — 이 문서의 "Font Size 단위 처리" 원칙을 따른다.

### 1-c. 전달 보존 Check (Delivery Preservation Check)
> 기존 1(Layout Compliance)·1-b(Typography)·2(Visual Quality) 체크와 중복되지 않는, **콘텐츠 전달 보존 여부**만 확인하는 최소 절차다. 좌표·간격·색상·정렬 등은 여기서 다시 확인하지 않는다.

위 "생성 전 Implementation Contract 확인"과 실제 HTML을 대조해 아래만 확인한다.
- Required Evidence가 실제로 구현됐는가(관계형이면 관계를 이루는 값 전체가 남아 있는가, 대표값 하나로 축소되지 않았는가)
- Relationship이 실제 Visual에서 보존되는가
- Visual Strategy가 구현 편의로 Text/Large Number/균질 Stat Grid로 임의 축소되지 않았는가
- Required로 확정된 Image/Asset이 실제로 사용됐는가
- Selected Layout이 의도한 정보 관계를 그대로 유지하고 있는가(다른 구조로 바뀌지 않았는가)

위반이 발견되면 "생성 전 Implementation Contract 확인 > Required Evidence 보존"의 처리 순서(같은 Layout 안에서 재구성 → Layout 재검토가 필요하면 에스컬레이션 → 구현 불가 사유 기록)를 따른다. 이 체크만을 위한 별도 반복 횟수는 두지 않는다 — 아래 "4. 재검증"에 포함해 함께 확인한다.

### 1-d. Content Fidelity QA (1차 최소 검증)
> Typography/Layout/Visual QA와 분리된 결정론적 콘텐츠 검사다. 원본 PPT/PDF/DOCX를 다시 열거나 전체 내용을 LLM으로 의미 비교하지 않는다.

최초 생성 시에는 전체 슬라이드, [7] 수정 라운드에서는 **이번에 변경된 슬라이드만** 아래 Script를 한 번의 배치 호출로 검사한다(위 "0-b. 전체 QA 재실행이 필요한 경우"에 해당하면 이 단계도 전체 슬라이드로 되돌아간다). 입력은 기존 `material_analysis.json`, `slide_composition_map.json`, `slide_outline.md`만 재사용하며 동일 Source를 슬라이드별로 반복 Read하지 않는다.

```bash
python .claude/skills/web-ppt-generator/scripts/content_fidelity_qa.py \
  --material-analysis /output/{project-name}/material_analysis.json \
  --composition-map /output/{project-name}/slide_composition_map.json \
  --outline /output/{project-name}/slide_outline.md \
  --web-ppt /output/{project-name}/web_ppt/vN \
  --out /output/{project-name}/.qa/vN \
  --slides <이번에 생성·수정된 슬라이드 번호의 콤마 목록>
```

- 최초 생성에서 전체 슬라이드를 검사할 때는 `--slides`를 생략한다.
- 검사 범위는 (1) Grounding에 없는 명시적 수치·단위·연도 및 규칙으로 식별 가능한 회사명·제품명 후보, (2) `slide_outline.md`의 Required Evidence에서 결정론적으로 추출 가능한 수치·인용문·명시 필드·이미지 ref의 누락, (3) Data Pending·`[확인필요]` marker 유실이다.
- 결과는 `.qa/vN/content-fidelity-report.json`에 저장한다. 확정 위반인 `issues[]`가 있으면 종료 코드 1로 실패하며, **명확히 확정 가능한 오류만** 수정한 뒤 변경 슬라이드만 재검사한다.
- provenance 없이 사용 여부를 확정할 수 없는 uncertain 자산이나 결정론적 atom을 뽑을 수 없는 Required Evidence는 통과로 단정하지 않고 `unchecked[]`에 기록한다. **이 uncertain/ambiguous 항목을 원본과 다시 대조해 false positive 여부를 AI가 재판정하지 않는다** — 그대로 `qa_report.md`에 남겨 Human Review ②([6]) 대상으로 이관한다. 이 1차 검증을 이유로 LLM 전체 의미 검사를 추가하지도 않는다.
- Relationship Fidelity, Chart Series/Axis/Legend 비교, 세밀한 Claim 의미 검증, HTML→PPTX parity는 이 단계에서 검사하지 않는다.

### 2. Visual Quality Check
> 겹침·overflow·캔버스 이탈·Font Size처럼 좌표·CSS 값으로 기계적으로 판정 가능한 항목만 이 단계에서 자동 검사한다(2-a). 응집도·시각적 균형·가독성·이미지-캡션 의미 일치·Layout Reference와의 육안 유사도 등 **코드로 판정할 수 없는 정성적 기준은 삭제되지 않지만, 자동 QA의 책임이 아니다** — 스크린샷을 반복 Read하거나 crop해 확대·재판단하는 과정 없이, 아래 2-a만 수행하고 나머지 정성적 판단은 전부 Human Review ②([6])로 이관한다. 사용자가 브라우저로 직접 열어 이 항목들을 판단한다.

#### 2-a. 자동 검사
1. `scripts/qa_render.py`로 대상 슬라이드를 렌더링하면서 Font Size와 겹침/overflow/텍스트 잘림, render/HTML 오류, broken image/resource를 함께 감사한다(1-b와 한 번에 실행 가능): `python scripts/qa_render.py --web-ppt <web_ppt/vN> --out <프로젝트>/.qa/vN --slides <이번에 만든/고친 슬라이드 번호> --audit-fonts --audit-layout`.
   - **배치 호출 원칙**: 이번 라운드에 대상이 되는 슬라이드가 여러 장이면(예: 최초 생성 후 발견된 문제 슬라이드가 3, 6, 8, 19번처럼 여러 개) 슬라이드마다 따로 호출하지 않고 `--slides 3,6,8,19`처럼 **하나의 호출에 콤마로 묶어** 실행한다 — `qa_render.py`는 한 번의 실행으로 여러 슬라이드를 순회하며 렌더링·감사하도록 이미 설계돼 있다. 슬라이드를 분리 호출하는 것은 아래 두 경우로 한정한다.
     1. 한 슬라이드의 수정 결과가 다른 슬라이드의 수정 여부·내용에 영향을 줘서 순서대로 처리해야 하는 경우(순서 의존성이 실제로 있는 경우만 — 단지 같은 라운드에서 발견됐다는 이유만으로는 해당하지 않는다)
     2. 특정 슬라이드 하나만 별도로 재검증해야 하는 경우(예: 다른 슬라이드는 이미 통과했고 이 슬라이드만 추가 수정·재확인이 필요할 때)
2. `<프로젝트>/.qa/vN/layout-audit.json`(겹침/overflow/clipping)과 `font-audit.json`(Typography 위반)을 읽고 어떤 슬라이드에서 위반이 탐지됐는지 확인한다 — 이 두 파일의 판정은 스크린샷을 열지 않아도 코드 결과로 확정할 수 있다.
3. 2-a에서 이상이 탐지되지 않으면 이 슬라이드의 Visual Quality Check는 그것으로 종료한다 — 스크린샷을 열어 육안으로 재확인하지 않는다.

#### 2-b. Human Review ②로 이관되는 항목 (자동 QA 미수행)
아래는 자동 QA에서 판단하지 않는다. QA 스크립트가 스크린샷을 남기더라도 그것을 열어 아래 항목을 재판단하는 절차는 수행하지 않으며, 그대로 [6] Human Review ②에서 사람이 확인한다.
- Content Area 여백·쏠림·응집도, 병렬 Region 간 시각적 비중 균형, sibling Content Group 간 시각적 무게 균형
- Container 대비 실제 Visual/텍스트 크기, Main Visual/Evidence/Table/Image의 콘텐츠량 대비 크기
- 아이콘/도형/이미지의 의미 전달 적합성, 이미지·캡션 의미 일치
- 고정 `max-width`/폭 값으로 인한 부자연스러운 줄바꿈
- Divider/구분선의 실제 가시성(서브픽셀 렌더링으로 사라져 보이는지) — 보이지 않는다고 확인되면 위 "구현 기준 > Divider 서브픽셀 렌더링" 기준에 따라 1px fallback 적용
- 컬러 이모지 아이콘의 브랜드 톤 이탈 — 위 "구현 기준 > 아이콘 렌더링" 기준에 따라 VS15 또는 SVG/브랜드 자산으로 교체
- Selected Layout이 의도한 시각적 구성·Layout Reference와의 유사도가 실제로 구현됐는지

Human Review ②에서 위 항목에 대한 수정 요청이 오면 [7] 피드백 반영 절차를 그대로 따른다 — 이 문서의 자동 QA 재검증 루프에는 포함하지 않는다. 단, 위 항목 중 문구 변경·Text/Image 좌표(X/Y)·크기·이미지 교체류의 최종 미세 조정은 Human Fine Editing 도구(`scripts/fine_editor/`, CLAUDE.md "Human Fine Editing" 절)로 사람이 직접 처리하며 이 스킬(web-ppt-generator)이 다시 호출되지 않는다 — 응집도·시각적 균형·이미지 의미 적합성 등 구조 판단이 필요한 나머지 피드백만 [7] 경로로 들어온다.

### 3. 자동 수정 범위
1·1-b·1-c·1-d·2-a에서 **기계적으로 확정 가능한** 문제가 발견되면 아래 범위 안에서만 수정한다. 2-b로 이관된 정성적 항목(응집도·균형·의미 적합성 등)은 여기서 다루지 않는다 — Human Review ②에서 수정 요청이 오면 그때 [7]로 처리한다.
- Visual/Image/Table/Chart의 크기 조정(overflow/clipping 해소 목적)
- 내부 Gap 조정(overlap 해소 목적)
- 사용 가능한 실제 이미지 자산 활용(1-c/1-d에서 누락으로 확정된 경우)
- Layout MD에 명시된 비율/정렬/Fill/Alignment 복원(1의 수치 불일치로 확정된 경우)
- Typography 기준(Hard Rule §9/§10/§12, Design System §3)에 맞는 Font Size 복원 — pt 단위로 수정하며, px가 필요하면 1pt=1.3333px로 정확히 환산한다
- 동일 역할 Table Target Column을 `colgroup` + `table-layout: fixed`로 명시적 폭 지정(비율은 해당 Layout MD 값 유지)
- 1-c/1-d에서 확정된 Required Evidence/Relationship/Visual Strategy 누락을 같은 Selected Layout 안에서 복원(배치·크기·밀도 재구성)

슬라이드의 핵심 메시지나 `slide_outline.md`의 **Selected Layout 자체는 변경하지 않는다.** Layout을 바꿔야 해결되는 문제로 판단되면(1-c에서 Required Evidence가 같은 Layout 안에서 도저히 수용되지 않는 경우 포함) 자동 수정하지 않고 아래 4번의 에스컬레이션 경로를 따른다.

### 4. 재검증
수정한 슬라이드만 대상으로 1·1-b·1-c·1-d·2-a를 다시 실행한다(동일한 `--slides` 범위, 배치 호출 원칙 동일 — 여러 슬라이드를 동시에 고쳤다면 한 번의 `--slides` 콤마 리스트로 묶어 재렌더링한다). 스크린샷을 다시 열어 확인하는 절차는 없다 — 2-a 결과(`layout-audit.json`/`font-audit.json`)와 1-d 결과(`content-fidelity-report.json`)가 clean이면 그 슬라이드의 재검증은 통과다. **최대 2회까지만** 반복한다. 2회 후에도 기계적 QA가 clean하게 통과하지 않으면(또는 애초에 Layout 변경이 필요하다고 판단되면) 슬라이드 번호와 미해결 문제를 `<프로젝트>/.qa/vN/qa_report.md`에 기록하고, content-designer는 이를 메인에게 보고해 Human Review ②([6]) 대상으로 표시한다.

## 스크립트
- `scripts/new_version.py` — 버전 스냅샷 생성/롤백
- `scripts/qa_render.py` — 생성 후 QA용 슬라이드 스크린샷 렌더링(Playwright, [5]/[7] 직후 사용). `--audit-fonts`는 Typography 위반을, `--audit-layout`은 겹침/캔버스 이탈(overflow)/텍스트 잘림을 좌표·computed style로 감사해 각각 `font-audit.json`/`layout-audit.json`으로 저장한다 — "2. Visual Quality Check > 2-a"의 기계적 판정에 그대로 사용하며, 이 결과가 clean이면 스크린샷을 열어 육안으로 재확인하지 않는다. 응집도 등 정성적 판단은 2-b에 따라 자동 QA 범위 밖이며 Human Review ②로 이관된다.
- `scripts/content_fidelity_qa.py` — 기존 분석 산출물과 HTML을 한 번씩 읽어 명시적 사실 추가, Required Evidence atom 누락, uncertainty marker 유실만 검사하는 비-LLM 경량 QA. 최초 생성 또는 변경 슬라이드에만 실행한다.
- `scripts/bundle_for_share.py` — 확정된 `vN/` 버전을 외부 공유용 단일 self-contained HTML(`shared.html`)로 번들링(CSS·이미지·로컬 스크립트 인라인, 원본 `index.html`/`style.css`/`assets/`는 읽기 전용). 메인 에이전트가 CLAUDE.md [6] "확정 웹PPT 공유용 HTML 자동 생성" 절차에 따라 **모든 `v{N}` 확정 시 기본으로** 직접 실행하는 LLM 판단 불필요 스크립트이며(사용자의 별도 공유 요청과 무관), [5]/[7] 생성·수정이나 위 QA 절차와 무관한 별도 후처리 단계다. 인라인 처리 후에도 로컬 파일 참조가 남아 있으면(예: 찾을 수 없는 이미지, `file:///` 절대경로) 스크립트가 종료 코드 1로 실패하고 `shared.html`을 쓰지 않는다 — 원본 파일은 이 스크립트가 애초에 읽기만 하므로 실패해도 훼손되지 않는다. content-designer가 직접 호출할 일은 없다.
- `scripts/templates/` — 슬라이드 기본 HTML/CSS 템플릿 (표지, 본문, 표, 차트, 부록 레이아웃)
- `scripts/templates/components/` — Layout별 재사용 HTML/CSS 구현 골격(위 "전용 Layout의 구조 규칙 우선 적용 > 구현 골격 우선 재사용" 참조). 현재 `flow-diagram.css`/`flow-diagram.html`(Flow Diagram Layout, Node/분기/Lane 개수·좌표·콘텐츠는 비워둔 채 구조만 제공)과 `three-column.css`/`three-column.html`(Three-Column Insight Layout, Header 행과 Body 행을 분리된 두 트랙으로 구성해 Header Gap과 Body Vertical Divider가 서로 다른 값을 갖도록 보장하는 구조만 제공)이 등록돼 있다. 다른 Layout으로 확장할 때도 이 폴더에 같은 이름 규칙(`{layout-slug}.css`/`.html`)으로 추가한다.
- `scripts/vendor/` — 로컬 번들 JS 라이브러리 배치 위치 (Chart.js 등)
- `scripts/fine_editor/` — Human Fine Editing용 독립 경량 Editor(문구 변경·Text/Image X/Y 이동·Image 크기 조절/교체, 순수 HTML/CSS/JS + 표준 라이브러리 Python 서버, 추가 패키지 없음). Agent가 호출하지 않는 사람 전용 도구이며 [5]/[7] 생성 로직을 재사용하지 않고 완전히 별도로 동작한다. 사용법은 CLAUDE.md "Human Fine Editing" 절 참조.

## references
> 우선순위(Hard Rule > Design System > Content Visualization Freedom > Layout Reference)와 각 문서의 관계는 `references/design-rules.md`가 정의하는 단일 기준이다 — 아래는 경로와 용도만 요약하며, 전부 수정 금지(design-rules.md에서 참조만).

- `references/design-rules.md` — 위 우선순위·가변 규칙·검토 대기 후보를 링크하는 허브 문서(누적 갱신, 가변 규칙 본문 반영은 사용자 명시 승인 후에만)
- `docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md` — Hard Rule 원본
- `docs/design-system/Claude_PPT_Design_System.md` — Claude PPT Design System 원본
- `docs/design-system/visual-style.md` — 기존 Visual Style 원본(참고용 보존, design-rules.md가 대체 관계 정의)
- `docs/design-system/content-visualization-freedom.md` — 콘텐츠 표현 자유도 원본
- `docs/layout-reference/2026.08.13_layout-catalog_V1.md` — Layout Reference 선택 인덱스 원본(L01~L33, 콘텐츠 유형·정보 구조 기준)
- `docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx` — 위 카탈로그가 가리키는 33종 레이아웃의 시각적 구조 원본. 카탈로그에서 후보를 고른 뒤 실제 요소 배치를 확인할 때만 참고한다.
- `docs/layout-reference/2026.08.20_special-layout-index_V1.md` — `docs/slide-design-rules/`의 특수 Layout Reference 17종에 대한 경량 선택 인덱스(Layout명/Category/Use When/Do Not Use When/원본 MD 경로)
- `docs/slide-design-rules/` — 콘텐츠 유형·구조별 특수 Layout Reference 원본 폴더. 표지 전용 `01_cover_design_V2.md`와 구조별 참고 `three-column.md`, `process-comparison.md`, `comparison-matrix.md`, `benefit-impact.md`, `before-after.md`(Variant A/B 체계), `table-comparison.md`, `013_multi-radar-technology-comparison.md`, `014_left-right-tech-comparison.md`, `019_competitive-advantage-highlight.md`, `020_organization.md`, `021_business-site-map.md`, `02_instruction_design_V1.md`(Company Introduction), `timeline-company-milestone.md`, `process-system-architecture-layout.md`(공정/시스템 구성 요소를 좌→우 선형 구조로 순차 설명, 사진 유무에 따른 Layout A/B), `product-application-layout.md`(대표 제품과 적용 분야를 Card형 또는 방사형 Hub-and-Spoke로 연결), `visual-insight/visual-insight.md`(범용 2분할 Family)를 포함하며 계속 추가될 수 있다. 원본 17개 문서를 전부 열지 않고 위 경량 인덱스로 먼저 1~2개 후보로 좁힌 뒤 그 후보만 상세 Read한다(레이아웃 선택 절차 자체는 위 "디자인 규칙 적용 원칙"에서 이미 정의).
- `references/design-decisions-log.md` — 위 규칙들의 근거가 된 과거 Field Test 회귀 사례 로그(매 호출마다 읽을 필요 없음, 규칙 취지가 의심스러울 때만 참조)
