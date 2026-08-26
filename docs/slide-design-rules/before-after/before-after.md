# Before + After Process Layout Reference

## 1. Purpose

기존 방식(Existing/Current)과 개선 방식(Improved/New)을 비교해 그
변화와 개선을 보여주는 **Before/After 계열의 범용 Layout
Reference**다.

Before/After 콘텐츠를 항상 공정 Diagram으로 표현하지 않는다. 콘텐츠
구조에 따라 아래 2가지 Layout Variant 중 적합한 것을 선택해 적용한다.

-   **Variant A — Process Transformation** — 기존/개선 방식의 공정
    단계 자체(단계 수, 순서, 분기, 단순화 등)가 핵심일 때, 좌측
    Existing Process / 중앙 Transformation Arrow / 우측 Improved
    Process 구조와 실제 공정 Step·Connector·Image/Diagram으로 표현
-   **Variant B — Before/After Comparison Table** — 기존/개선 방식을
    여러 동일 기준으로 비교하는 것이 핵심일 때, 비교 기준을 Row,
    Existing/Improved를 Column으로 구성한 Presentation형 비교표로 표현

두 Variant의 선택 기준은 [3. Variant Selection
Rule](#3-variant-selection-rule)을 따른다.

### Use When

-   기존 방식과 개선 방식, 단 2개를 직접 비교할 때
-   기존 방식의 복잡성/한계를 개선 방식이 어떻게 해소하는지 보여줄
    때
-   공정 단계의 수·순서·분기·통합·단순화 등 **Process 구조 자체가
    달라지는** 경우 (→ Variant A) — 단계 수가 줄어드는 경우뿐 아니라,
    단계가 재구성되거나 분기되어 늘어나는 경우도 포함한다
-   공정단수, 공정시간, 비용, 효율, 부산물, 성능 등 동일 기준으로
    기존 대비 개선 정도를 보여줄 때 (→ Variant B)
-   기존 기술 → 신규 솔루션의 Transformation 또는 정량적 개선이 핵심
    메시지일 때

### Do Not Use When

-   비교 대상이 기존/개선 2개가 아니라 3개 이상일 때 → Comparison
    Matrix Layout(`comparison-matrix.md`)을 사용
-   서로 독립적인 배경/요인 3개를 동일 위계로 병렬 제시할 때 →
    Three-Column Layout(`three-column.md`)을 사용
-   공정 흐름을 먼저 보여준 뒤 그 흐름과 연결된 문제점/비교를 하단에서
    함께 전달해야 할 때 → Process + Comparison
    Layout(`process-comparison.md`)을 사용
-   하나의 솔루션이 만드는 정량적 Impact를 Evidence(그래프·KPI 등)로
    증명하는 것이 핵심(비교보다 효과 증명이 목적)일 때 → Benefit +
    Impact Layout(`benefit-impact.md`)을 사용
-   시간축 기반 로드맵/연혁인 경우
-   비교 대상(Existing vs Improved)이 없고 **단일 Process 흐름 하나만
    설명**하면 충분할 때 → Process / System Architecture
    Layout(`process-system-architecture-layout.md`)을 사용
-   **Process 흐름(단계·순서·분기) 자체가 없이** 속성·스펙·평가
    항목만 비교할 때 → Table Comparison
    Layout(`table-comparison.md`) 또는 Comparison Matrix
    Layout(`comparison-matrix.md`)을 사용

------------------------------------------------------------------------

## 2. Reference Reproduction Principle

Variant A는 `docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`의
28번 슬라이드(L28, 최신 수정판)를 기준 Reference로 사용한다. 이전에는
별도 파일 `before-after.pptx`(분기 없는 단일 사례)를 참조했으나, 분기
구조를 포함한 L28로 기준을 교체한다. 이 문서의 [4. Variant
A](#4-variant-a--process-transformation) 수치·영역 구조는 L28의 실측
좌표를 그대로 비율화한 것이다.

**Reference가 제공된 경우 다음 우선순위를 지킨다.**

1.  Reference의 공간 분할(영역 비율) — 일반적인 3-Column Grid, Card
    Grid 같은 통상적 Web/AI UI 관습보다 우선
2.  Reference의 Visual 크기/점유 범위 — "여백을 넉넉히 준다"는 일반
    디자인 관습보다 우선
3.  Reference의 정보 밀도 — Dashboard형 여백 중심 구성보다 우선
4.  Reference의 정렬·배치 패턴(기준선, Y축 정렬 등)
5.  콘텐츠(텍스트/수치/이미지)만 새 프로젝트 내용으로 치환한다 —
    Reference의 특정 공정명·회사명·이미지·수치 자체는 복제하지 않는다
    ([6. Avoid](#6-avoid-공통) 참조)

**Prohibited Reinterpretations (공통, Variant A/B 모두 적용)**

다음은 이 Layout을 "일반적인 AI/Web UI 스타일"로 되돌리는 대표적인
실패 패턴이다. 명시적으로 금지한다.

-   Step/Cell을 모두 동일한 `border-radius` + `box-shadow` Card로
    감싸는 것 (Reference는 얇은 Box/Divider 중심, 그림자 없는 평면
    구성)
-   비어 있는 Placeholder Icon(원형 배경 + 단색 Line Icon)을 실제
    Diagram/Photo 대신 채워 넣는 것
-   Step 수와 무관하게 3\~4개의 균일한 폭의 Column/Grid로 기계적으로
    나누는 것 (Existing/Improved 두 Column으로 나누는 것은 예외 —
    좌우 Column 폭 비율 기준은 §4.1을 따른다)
-   중앙 Transformation 요소를 본문 높이 전체를 채우는 큰 세로 Bar로
    만드는 것 — Arrow 크기·비례 기준은 §4.5를 따른다
-   KPI/숫자 하나를 큰 여백 중심의 Dashboard Tile로 단독 배치하는 것
-   Step Box 사이 간격을 Box 자체 높이보다 크게 벌려 카드처럼 분리시키는
    것 — Box:간격 비율 기준은 §4.3을 따른다
-   좌우 Process 중 한쪽(특히 Improved)을 다른 쪽보다 큰 Box 크기나
    넓은 Column 폭으로 확대해 강조하는 것 — 강조는 §4.6의 색상/정보
    방식만 사용한다
-   Step 수가 적은 쪽의 남는 공간을 임의의 Placeholder 이미지나 예시
    사진으로 채우는 것 — §4.3·§4.9 기준을 따른다
-   Existing/Improved 두 영역의 디자인 언어(Box 스타일, Typography,
    Depth)를 다르게 표현하는 것

------------------------------------------------------------------------

## 3. Variant Selection Rule

다음 핵심 질문을 기준으로 표현 방식을 선택한다.

| 핵심 질문 | 선택 Variant |
|---|---|
| "단계 수·순서·분기·통합 등 Process 구조가 어떻게 달라지는가"가 핵심 | **Variant A. Process Transformation** |
| "기존 대비 무엇이 얼마나 개선되는가"를 여러 기준으로 보여주는 것이 핵심 | **Variant B. Before/After Comparison Table** |

-   두 질문 모두에 해당하는 콘텐츠(공정 흐름도 보여줘야 하고, 동시에
    다수의 정량 기준으로도 비교해야 하는 경우)는 이 문서의 두 Variant를
    한 슬라이드에 억지로 합치지 않는다. 이런 경우 Process +
    Comparison Layout(`process-comparison.md`)이 더 적합한지 먼저
    검토한다.
-   단순히 표 형태로 정리할 수 있다는 이유만으로 Variant B를 선택하지
    않는다 — 공정 단계 자체의 변화가 메시지의 핵심이면 Variant A를
    우선한다.
-   [2026-08-25 추가] 공통 비교 기준(Criteria)이 **명확히 존재하지
    않고**, 공정 단계 변화도 핵심이 아니며, 단순히 기존 상태 하나와
    개선 상태 하나를 직접 대비하는 것이 목적인 경우에는 Variant A를
    선택하되 §4의 **Process/Step Sequence 전용 조건부 규칙(4.2~4.4,
    4.7~4.9, 4.13)은 적용하지 않고** Comparison Frame(Header Bar,
    좌우 대비 구조)만 사용한다 — Main Visual이 Chart/Image/KPI 등
    비-Process 콘텐츠인 경우와 동일하게 취급한다(§4 서두 참조). 비교
    기준(Criteria)이 여러 개이고 각 기준이 Existing/Improved 양쪽에
    1:1로 대응되면 이 경우가 아니라 Variant B를 우선한다(아래
    참조).
-   선택 결과(Variant A / Variant B)는 `slide_outline.md`에 함께
    기록한다.

------------------------------------------------------------------------

## 4. Variant A — Process Transformation

기존 방식의 복잡한 공정과 개선 방식의 단순화(또는 재구성)된 공정을
좌→우로 직접 비교하여 단계 감소, 효율 개선 또는 프로세스 혁신을
직관적으로 보여주는 표현 방식이다. 본문은 Hard Rule §9의 본문 Safe
Area(**X 64\~1216px, Y 182\~656px, 즉 1152×474px Body Box**)를 100%
기준으로 아래 구조를 따른다.

**총괄 원칙**: 좌우 Process는 Header 아래 본문 전체 폭을 적극적으로
사용하는 두 개의 대칭적인 Column이며, 중앙에 작게 모여 떠 있는 형태를
금지한다. Existing과 Improved는 동일한 Grid, Box Style, Typography
Hierarchy, Alignment 체계를 공유하는 하나의 시스템으로 설계하고, 서로
다른 디자인 언어로 표현하지 않는다.

단, 이 대칭은 Column의 위치·폭 등 **Frame 차원의 대칭**이며, 그 안에서
흐르는 실제 Step Flow의 형태(단일 경로 vs 분기, Step 수)까지 좌우가
같아야 한다는 뜻은 아니다 — Existing과 Improved 중 한쪽만 분기하거나
서로 다른 Step 수를 가질 수 있다(4.2, 4.3, 4.4 참조).

**Comparison Frame과 Main Visual**: 이 Variant는 항상 유지되는 **공통
Comparison Frame**과, 콘텐츠 성격에 따라 달라질 수 있는 **Main
Visual**을 구분한다.

-   **Comparison Frame(Main Visual 유형과 무관하게 항상 적용)**: 4.1의
    영역 비율(Existing/Transformation/Improved Column 배치), Header
    Bar의 역할·배치·독립된 Bar 구조(4.2 Header Bar 부분), 중앙
    Before→After Arrow(4.5), 좌우 Main Visual이 서로 비교 가능한
    위치·크기·정렬을 이루도록 하는 배치 원칙(4.10\~4.12).
-   **Process/Step Sequence 전용 조건부 규칙**: Main Visual이 실제
    공정·단계 흐름(Process/Step Sequence)일 때만 4.2의 Step Box 내부
    구조, 4.3 Pitch 규칙, 4.4 Branching, 4.7 Step Style, 4.8 Step Box
    Sizing & Alignment, 4.9 Input/Outcome·Result 영역, 4.13 Connector
    Line이 추가로 적용된다. 단순 속성을 나열·
    비교하는 Before/After(Chart·Image·KPI 등 비-Process Main Visual)에는
    이 조건부 규칙(특히 4.13 Connector)을 강제하지 않는다.
-   **Conclusion(4.14, Optional)**: Main Visual 유형과 무관하게, 하단
    Conclusion을 실제로 사용하기로 선택한 경우에만 적용된다.

Main Visual은 콘텐츠 성격에 따라 Process ↔ Process, Diagram ↔
Diagram, Chart ↔ Chart, Image ↔ Image, KPI ↔ KPI 등으로 달라질 수
있다 — 단, Existing과 Improved 양쪽은 항상 **동일한 Main Visual
유형**을 사용해야 직접 비교가 성립한다(예: 한쪽은 Chart, 다른 쪽은
Photo로 표현하지 않는다). Main Visual 유형 선택 자체는 이 문서가
규정하지 않으며 `content-visualization-freedom.md`의 Main Visual
선택 기준을 따른다.

### 4.1 Overall Region Map

Body Box(1152×474px)를 기준으로 한 영역 좌표다. 실제 좌표는
`64 + (X% × 11.52)`, `182 + (Y% × 4.74)`로 환산한다.

| 영역 | X 범위 (Body Box 기준) | Y 범위 (Body Box 기준) | 비고 |
|---|---|---|---|
| Existing(Left) Column | 0\~44% | 0\~100% | Improved와 동일한 내부 구조(4.2) 사용 |
| Transformation(Center) Column | 44\~54% | 0\~100% | 폭 8\~12%(기본 10%), 좌우 Column 폭에서 조정 |
| Improved(Right) Column | 54\~98% | 0\~100% | Existing과 동일한 내부 구조(4.2) 사용, 우측 2%는 여백 |
| Header Bar (Zone Label) | 각 Column 폭 전체 | 0\~13% | 좌우 동일 Y, 상단 기준선 정렬. 시각 스펙은 Hard Rule §10 참조(4.2 Header Bar 부분) |
| Process Visual Area | 각 Column 폭의 80\~90%(Column 내 가운데 정렬) | 13\~97% | Column 가용 높이의 대부분을 사용. 세부 구조는 Main Visual 유형에 따라 다름(Process/Step Sequence는 4.2 이하 참조, 그 외에는 `content-visualization-freedom.md` 기준) |

Column 폭(44:10:44)은 콘텐츠 복잡도에 따라 ±3%p까지 조정할 수 있으나,
어느 한쪽 Column이 다른 쪽보다 명백히 좁아 보이지 않도록 좌우
균형(대칭)을 기본으로 한다. 좌우 Process 중 하나만 강조가 필요한
경우에도 Column 폭이 아니라 4.6의 색상/정보 강조로 처리한다.

### 4.2 Process Column — 공통 내부 구조 (Existing / Improved 동일 적용)

*이 절의 Header Bar(Zone Label) 규칙은 Main Visual 유형과 무관하게
항상 적용되는 Comparison Frame의 일부다. 그 아래 Input/Step
Box/Connector/Output 구조는 Main Visual이 Process/Step Sequence일
때만 적용되는 조건부 규칙이다.*

Existing과 Improved는 아래 동일한 정보 위계와 구조를 공유한다.

**Header Bar(Zone Label)** ↓ **(선택) Input / Starting Material** ↓
**Step Box + Connector 시퀀스(단일 또는 분기)** ↓ **(선택, 실제
자산이 있을 때만) Result / Output Visual**

Existing과 Improved(또는 Improved 내부의 각 분기 경로)는 이 정보
위계 순서만 동일하게 따르면 되며, 시퀀스가 단일 경로인지 분기인지,
Step 수가 몇 개인지는 Flow마다 독립적으로 결정된다 — 좌우가 같은
내부 구조(단계 수·분기 여부)를 가져야 한다는 제약은 아니다.

-   Header Bar(Zone Label)는 Column 폭 전체를 사용하며, 좌우 Column
    에서 동일한 높이(Y 0\~13%)를 사용해 두 비교 대상을 명확히 구분
    하는 독립적인 Bar로 인식되어야 한다. Header Bar 자체의 시각
    스펙(Height·Font·Color·Letter Spacing·Padding·Corner·Fill·
    Divider·Gap 등)은 이 문서에서 새로 정의하지 않으며 **Hard Rule §10
    Content Region Header**를 그대로 따른다 — Existing/Improved처럼
    의미적으로 명확한 대립 구조이므로 Hard Rule §10의 **Contrast
    Variant**를 적용해 대비를 표현한다(Existing 측/Improved 측 배정은
    Hard Rule §10 Contrast Variant 정의를 그대로 따른다). 두
    Header Bar는 중앙 Transformation Column(4.5)을 사이에 두고 있어
    Hard Rule §10의 Header Bar 간 Gap 확보 요건을 이미 충족한다.
-   Header Bar는 **본문(Flow 설명 Text, Step Box 등)의 콘텐츠 변경에
    영향받지 않는 고정 영역**이다 — Header Bar와 본문이 같은 상위
    Container를 공유하더라도, 본문 콘텐츠가 늘어나거나 줄어든다는
    이유로 Header Bar의 폭·높이·Padding·Text 정렬·구분선이 압축되거나
    변형되어서는 안 된다. 구현 시 Header Bar 치수를 본문과 독립적으로
    고정해 이를 보장한다.
-   Header Bar와 Step Box 시퀀스 사이에 Flow를 설명하는 짧은 텍스트
    (Zone 이름, Input 설명 등)를 두는 경우, 이 텍스트도 해당 Flow
    영역(Column) 폭 기준으로 가운데 정렬하며 Font Size는 Step Box
    내부 Text와 동일하게 16pt를 사용한다(4.7 참조) — 좌측 정렬하지
    않는다.
-   Flow 설명 Text와 그 아래 첫 Step Box 사이에는 서로 붙어 보이지
    않도록 **충분한 세로 Gap**을 둔다 — Existing과 Improved 모두 동일한
    Gap 기준을 적용한다.
-   Process Visual Area(Y 13\~97%, 84%p)는 Column의 가용 높이 전체를
    적극적으로 사용한다. 상단에 내용이 몰리고 하단이 비어 보이는
    구성을 금지한다.
-   Step Box는 콘텐츠 양에 맞는 폭으로 배치하고(4.8 참조), 그 Flow
    영역(Column 또는 분기 경로 폭) 안에서 좌우 여백이 같도록 가운데
    정렬한다 — 내용에 비해 불필요하게 넓게 늘리지 않는다.
-   Step Box는 그림자·큰 모서리 반경·넉넉한 내부 Padding을 가진 Web
    UI Card가 아니라, 얇은 Border 또는 옅은 배경 + 얇은 Connector로
    구성된 PPT형 Process Box로 표현한다(4.7 참조).
-   같은 종류의 정보(Step 이름, 부가 설명 등)는 Existing과 Improved에서
    동일한 시각적 표현 방식(같은 폰트 크기, 같은 Box 비례)을 사용해
    가로로도 직접 비교되도록 한다.

### 4.3 Step Box 크기 산정 — 공통 Pitch 규칙

*Main Visual이 Process/Step Sequence일 때 적용되는 조건부 규칙이다.*

이 슬라이드에 존재하는 **모든 개별 Step Flow**(Existing의 흐름,
Improved의 흐름 — Improved가 분기되는 경우 각 분기 경로도 하나의
개별 Flow로 취급한다)는 그중 **Step(노드) 수가 가장 많은 Flow를
기준으로 계산한 Pitch를 모든 Flow에 동일하게 적용**한다.

-   기준 Pitch = Process Visual Area 높이(84%p) ÷ (모든 Flow 중 가장
    많은 Step 수). 예: 가장 긴 Flow의 Step 수가 N이면 Pitch ≈ 84%p ÷ N.
-   Step Box 높이 = Pitch × 0.65\~0.75, 나머지(0.25\~0.35)는
    Connector가 차지한다. Box가 Connector보다 항상 크게 유지되어
    Process Box + Connector 리듬이 유지되도록 한다.
-   Step 수가 적은 Flow(예: 특정 분기 경로의 짧은 Step 수)도 **동일한
    Pitch와 동일한 Box 높이**를 사용한다 — Step 수가 적다는 이유로
    Box를 이 비율 이상으로 확대해 하나의 거대한 색상 Box를 만들지
    않는다.
-   Step 수가 적어 발생하는 남는 세로 공간은 다음 중 하나로만 채운다.
    1.  4.4의 분기(Branch) 구조로 자연스럽게 높이를 채우는 경우
    2.  실제로 제공된 Result/Output Visual(사진, 수치, 그래프 등,
        4.9 참조)
    3.  Connector 길이를 Pitch 범위 내에서 여유 있게 사용하는 것
        (단, Box보다 길어지지 않는 범위)
    실제 콘텐츠·자산이 없으면 억지로 채우지 않는다. 이때 Step 시퀀스는
    Process Visual Area 상단(Pitch 그리드의 시작 지점)에서 다른
    Flow와 동일하게 시작하고 남는 여백은 하단에 남긴다 — 병렬 분기
    경로가 있는 경우 각 경로를 개별적으로 수직 중앙 정렬하지 않는다
    (모든 병렬 Flow가 동일한 Y 시작점·그리드를 공유해야 하므로, 4.4
    참조).
-   임의의 Placeholder 이미지, 예시용 사진, 관련 없는 장식 Icon으로
    남는 공간을 채우지 않는다.

### 4.4 Branching Process (Flow 분기)

*Main Visual이 Process/Step Sequence일 때 적용되는 조건부 규칙이다.*

개선 공정이 단일 경로가 아니라 2개 이상의 경로로 분리되는 경우(예:
하나의 기존 공정이 목적에 따라 서로 다른 길이의 2개 신규 공정으로
분리), 다음을 따른다.

-   Existing과 Improved가 좌우 대칭일 필요는 없다 — 한쪽(전형적으로
    Improved)만 분기하고 다른 쪽은 단일 경로를 유지하는 구성이 기본
    형태이며, 대칭을 맞추기 위해 분기하지 않는 쪽을 억지로 나누거나
    분기한 쪽을 억지로 합치지 않는다.
-   분기된 각 경로는 §4.3의 공통 Pitch를 다른 모든 Flow와 함께
    공유하며, **동일한 Y 시작점(공통 Pitch 그리드의 최상단)에서 함께
    출발**한다 — 경로마다 다른 시작 위치나 개별적인 상하 중앙 정렬을
    적용하지 않는다. 경로 길이가 서로 달라 발생하는 세로 범위 차이는
    자연스럽게 허용하되(경로가 짧으면 더 일찍 끝날 뿐), 시작 지점과
    Y 그리드 자체는 항상 모든 경로가 공유한다.
-   분기점(Branch Point)은 Improved Column 상단, Input 또는 첫 Step
    직후에 배치한다.
-   각 분기 경로는 4.3의 공통 Pitch/Box 높이를 동일하게 사용한다 —
    경로별로 Box 크기를 다르게 만들지 않는다.
-   경로 길이가 서로 다르면(예: 짧은 경로 vs 긴 경로), 더 긴 경로가 Column
    가용 높이를 채우는 기준이 되고, 짧은 경로는 남는 공간을 4.3의
    남는 공간 처리 규칙(분기 구조 자체, 실제 Output Visual, 여유
    Connector)으로 채운다.
-   두 경로를 나란히 배치할 경우 Column 폭을 균등 분할하되, 각 경로의
    Step Box 폭이 Web UI의 좁은 Sub-card처럼 보이지 않도록 경로당
    최소 Column 폭의 28\~35%를 유지한다.
-   분기형 구조를 사용하는 경우에도 Existing 대비 총 공정 효율(단계
    수 합, 처리 시간 등)이 개선되었다는 메시지가 명확히 드러나야
    한다 — 분기 자체가 목적이 되지 않게 한다.

### 4.5 Transformation Area (Center Column)

중앙은 Before에서 After로의 변화 방향을 표현하는 Arrow 요소로
구성한다.

-   Arrow는 **Reference(§2, L28)에 등록된 겹친 Chevron(») 원본 이미지
    Asset을 그대로 사용**한다 — CSS 도형(clip-path/polygon 등)이나
    SVG로 새로 그려 재구성하지 않으며, 단일 화살표·굵은 화살촉 등 다른
    Arrow 형태로 임의 대체하지 않는다. 여러 개의 방향 요소가 겹쳐
    하나의 전환 방향을 표현하는 구성 자체가 이 Layout의 구조적
    특징이다.
-   Arrow 원본의 가로세로 비율은 그대로 유지한다 — 폭과 높이를 각각
    다른 비율로 눌러 늘리거나 압축하지 않는다(비율 고정, 크기만
    조정).
-   Arrow의 크기는 **Step Box 1개와 비슷한 체감 크기**를 기준으로
    조정한다 — 본문 전체를 채우는 거대한 세로 Bar로 확대하지 않으며,
    반대로 존재감이 거의 없을 만큼 축소하지도 않는다. Center Column
    폭(8\~12%) 안에서 좌우 Process Box보다 얇고 가벼운 형태를
    유지한다.
-   Arrow의 수직 중심은 **Main Process Flow 영역**(각 Column 또는
    분기 경로의 Step 시퀀스가 실제로 차지하는 구간) 기준으로
    정렬한다. Outcome/Result 영역(§4.9)이 별도로 존재해 특정 Flow의
    전체 높이가 더 길어지더라도, 그 Outcome/Result 확장분은 Arrow
    중심 계산에 포함하지 않는다.
-   Arrow 위·아래에 과도한 빈 여백을 만들지 않는다 — Arrow가 좌우
    Process의 시각적 흐름 사이에 자연스럽게 끼워지도록, 위아래 여백은
    좌우 Step Box의 Connector 간격과 비슷한 수준으로 유지한다.
-   중앙 영역에는 **Arrow 이미지만 배치**하고 "Redesign" 등 어떤
    설명 Caption·라벨 텍스트도 추가하지 않는다. Arrow는 Existing→
    Improved **전환 관계 자체만** 표현하는 상징 요소다 — 수치, 부가
    설명, Arrow 위에 얹은 라벨 등 전환 관계 외의 추가 정보를 담지
    않는다.

### 4.6 Improved 강조 방법 (크기가 아닌 색상/정보로 강조)

Improved Process가 Existing보다 시각적으로 더 크거나 진한 Box로
확대되어 강조되는 것을 금지한다. 대신 다음 방법만 사용한다.

-   Step Box의 배경색 또는 Border를 Brand Color(Cosolus Teal 계열)로
    채운다. Existing은 Neutral Gray 계열을 유지한다.
-   핵심 수치 등 핵심 정보 텍스트에 Brand Color를 적용한다.
-   Typography Weight를 한 단계 높여(예: SemiBold→Bold) 정보 위계를
    강조할 수 있다. 단, Font Size 자체를 Existing보다 크게 키우지
    않는다.
-   Box 크기, Column 폭, Padding은 Existing과 동일하게 유지한다 —
    강조는 색과 정보 밀도로만 표현한다.

### 4.7 Process Step Style

*Main Visual이 Process/Step Sequence일 때 적용되는 조건부 규칙이다.*

-   Step Box 내부 Label(Step 이름, 부가 설명 등)은 **가로·세로 중앙
    정렬을 기본**으로 한다 — 이는 Design System §5의 일반 본문 좌측
    정렬 기본값에 대한 예외다. Step Box는 일반 본문 텍스트가 아니라
    하나의 노드처럼 인식되어야 하는 **Process Node 컴포넌트**이므로,
    이 Layout Reference가 Step Box에 한해 별도로 정의하는 정렬
    규칙이다.
-   Step은 얇은 Border 또는 옅은 배경의 Box + Connector 조합을
    기본으로 한다.
-   그림자(Box Shadow), 큰 모서리 반경, 넉넉한 내부 Padding을 가진
    Web UI Card 스타일을 사용하지 않는다.
-   연결선/Arrow 스타일은 Existing과 Improved에서 동일하게 유지한다.
-   Step 이름은 짧고 명확하게 작성한다.
-   Step Box 내부 Text(Step 이름, 부가 설명 등)의 **Font Size는
    16pt로 고정**한다. Font Weight·Color는 Hard Rule/Design System
    값(4.6의 강조 규칙 포함)을 그대로 따르며 이 문서가 재정의하지
    않는다.
-   동일 레벨 Step은 Existing/Improved 관계없이 동일한 크기와
    Typography를 사용한다(4.3 참조).

### 4.8 Step Box Sizing & Alignment (동일 크기·가운데 정렬)

*Main Visual이 Process/Step Sequence일 때 적용되는 조건부 규칙이다.*

이 Variant는 Number Badge, Side Bracket, 단계 수 Label 등 별도
Comparison Marker 요소를 사용하지 않는다 — Existing 대비 Improved의
변화(단계 감소, 분기 등)는 Process 자체의 구조(Step 개수·배치·중앙
Arrow, 4.10 참조)만으로 전달하며, 그 위에 강조용 장식 요소를 얹지
않는다.

-   같은 위계의 Step Box(예: 한 Flow 안의 모든 Step, 또는 병렬 분기
    경로 사이의 대응되는 Step)는 콘텐츠 분량이 조금씩 달라도 **동일한
    폭·높이**를 사용한다 — Step마다 제각각 크기를 다시 정하지 않는다.
-   Step Box는 자신이 속한 Flow 영역(Column 또는 분기 경로 폭) 안에서
    좌우 여백이 같도록 **가운데 정렬**한다.
-   텍스트가 길어 한 줄에 다 들어가지 않는 경우, Box 크기를 늘려서
    맞추지 않고 **줄바꿈(Wrapping)**으로 처리한다 — Box 크기는 같은
    위계의 다른 Box들과 동일하게 유지한다.
-   Step Box 내부 Label(Step 이름, 부가 설명 등)은 4.7에 따라 가로·
    세로 중앙 정렬한다.

### 4.9 Input / Outcome·Result 영역

*Main Visual이 Process/Step Sequence일 때 적용되는 조건부 규칙이다.*

-   Input은 Process 시퀀스 시작점 위(Process Visual Area 상단)에
    배치한다.
-   공정의 최종 결과값(Outcome/Result)이 **다른 Step과 동일하게 짧은
    텍스트 노드로 표현될 수 있는 경우**, 별도의 Card 스타일이나
    구분선·여백·Typography 차이를 얹어 "결과값임을 강조"하지 않고
    **같은 Flow의 다른 Step Box와 완전히 동일한 스타일(크기·Font
    Size·Weight·Color·정렬, 4.7\~4.8 참조)**을 그대로 적용한다 —
    Process 시퀀스의 자연스러운 마지막 노드로 표현하며, 4.13에 따라
    Connector로 이어 시퀀스가 끊기지 않게 한다.
-   Outcome/Result가 사진·그래프·Diagram 등 **Step Box와 다른 종류의
    Main Visual**로 표현되는 경우에만, 그 Visual 형식 자체의 차이로
    자연스럽게 구분된다(예: 텍스트 Box 사이에 놓인 이미지) — 이 경우
    에도 인위적인 장식(Card 테두리 강조, 별도 배경색 등)을 추가로
    덧붙이지는 않는다. Process 시퀀스 끝(하단)에 배치하되, **실제로
    제공된 이미지·수치·그래프가 있을 때만** 배치한다.
-   실제 자산이 없는 경우 Outcome/Result 영역을 임의의 Placeholder나
    예시 이미지로 채우지 않는다 — 대신 4.3의 남는 공간 처리 규칙(분기
    구조, 여유 Connector, 또는 단순 여백)을 따른다.
-   Outcome/Result의 표현 방식(Text/Key Number/Image/Diagram 등)은
    Flow의 콘텐츠 성격에 따라 Flow마다 다르게 선택할 수 있다 —
    Existing과 Improved(또는 분기 경로별)가 반드시 동일한 표현
    유형일 필요는 없다. 단, 같은 Flow 내부에서는 일관된 표현을
    유지하고, 어떤 Flow의 결과인지 위치·정렬(4.12 참조)로 즉시
    알아볼 수 있게 한다.
-   Improved가 여러 경로로 분기되는 경우, 분기 경로마다 독립적인
    Outcome/Result 영역을 가질 수 있다.

### 4.10 Visual Hierarchy & Comparison Composition 우선순위

개별 요소(Header/Arrow/Step/Y축 정렬)가 각각 규칙대로 구현되어도,
요소끼리 상충할 때 무엇을 우선할지가 없으면 좌우가 하나의 비교
Composition으로 읽히지 않는다. 요소 간 조율이 필요한 경우 다음
우선순위를 따른다. *이 우선순위 프레임 자체는 Main Visual 유형과
무관한 일반 원칙이다.*

1.  **핵심 변화의 즉시 비교** — Multi-step → Simplified Process처럼
    Existing과 Improved의 Step 개수·배치·분기 여부 차이 자체가 한눈에
    대비되어 읽히는 것. 별도 Badge/Bracket/Label 없이, 동일한 Box
    표현 방식·읽기 흐름·Process 형태 대비(4.8 참조)만으로 달성한다.
2.  **좌우 Main Visual 전체의 Visual Balance** — 좌우가 하나의
    Composition으로 인식될 정도의 균형. 이는 좌우 Bounding Box를
    기계적으로 동일하게 맞추는 것이 아니라, Process 고유의 자연스러운
    Flow와 분기 구조(4.4)를 그대로 유지한 상태에서 실제로 관련성
    있는 콘텐츠가 있을 때 그것으로 보완하는 원칙이다(4.11 참조). 이
    균형을 이유로 Process/Branch의 시작 위치나 내부 배치를 인위적으로
    이동시키지 않는다.
3.  **공통/대응 요소 Y축 정렬** — 이름·성격이 같은 Step을 동일 Y축에
    배치하는 것(4.12 참조). Branch 구조에서는 각 Path가 분기 원점을
    공유하며 분기 직후 자연스럽게 시작하는 것 자체가 이 정렬의 기본
    형태다.
4.  **개별 Step의 기계적 위치 일치** — 그 외 세부 요소를 Pitch 격자에
    기계적으로 맞추는 것

위 우선순위는 요소 간 판단 기준일 뿐, 상위 항목을 달성한다는 이유로
Process/Branch의 자연스러운 연결 관계(4.4, 4.13)를 깨거나 4.1의 전체
영역 비율·4.3의 공통 Pitch 규칙을 벗어나는 것은 허용하지 않는다.

핵심 시선 흐름:

`Existing Process → Transformation Arrow → Improved Process → 핵심 개선 지표`

-   사용자가 3\~5초 내에 기존 대비 무엇이 달라졌는지 파악할 수 있어야
    한다.
-   Improved의 핵심 개선(단계 감소, 효율 등)이 가장 중요한 Visual
    Message가 되도록 색상·정보 강조(4.6)로 유도한다.
-   세부 설명은 Process 이해를 보조하는 수준으로 제한한다.

### 4.11 Density & Spacing / Main Visual Balance

-   Existing/Improved 모두 Process Visual Area(Y 13\~97%)의 가용
    높이를 적극적으로 사용한다 — 어느 한쪽만 본문 상단에 작게 몰려
    있고 하단이 비는 구성을 금지한다.
-   Process/Branch 구조는 Visual Balance보다 **자연스러운 Flow와
    연결 관계를 우선**한다. 하나의 Input에서 여러 Path가 분기되는
    경우, 각 Path는 동일한 Branch Origin을 공유하며 분기 직후
    자연스럽게 시작해야 한다 — Visual Balance를 이유로 특정 Path나
    Process Group 전체를 분기 원점에서 떼어내 아래로(또는 다른
    위치로) 이동시키지 않는다.
-   좌우 Process의 실제 Visual 점유 높이와 시각적 무게(Box 개수 ×
    크기 + Outcome/Result 영역)를 가능한 한 유사하게 맞추는 것은
    바람직하지만(4.10의 우선순위 2), **Process 자체의 위치를 옮기거나
    내부 Gap을 인위적으로 늘려 Bounding Box를 기계적으로 맞추지
    않는다** — 실제로 근거 있는 하단 보완 콘텐츠가 있을 때 그것으로
    자연스럽게 달성한다.
-   실제로 제공된 관련 Image/Photo/Outcome·Result/Supporting
    Evidence가 있는 경우, 그 콘텐츠를 하단 보완 요소로 활용해 좌우
    Visual Weight를 보완할 수 있다(4.9 참조).
-   실제로 근거 있는 보완 콘텐츠가 없는 경우 Placeholder나 임의
    Visual을 만들지 않는다 — 콘텐츠량 차이에 따른 자연스러운 비대칭과
    여백을 그대로 허용한다(무자산 시 남는 공간 처리는 4.3 기준을
    따른다). 균형을 맞추기 위해 Step Box를 4.3의 공통 Pitch·Box 높이
    이상으로 확대하거나, 의미적으로 연결된 Step 사이의 간격을
    인위적으로 벌리지 않는다 — Step Box 크기·Pitch 자체는 4.3을 그대로
    따른다.
-   Step Box와 Connector 크기는 4.3의 공통 Pitch 규칙을 따른다.
-   중앙 Arrow는 4.5 기준을 넘어서는 여백을 만들지 않는다.

### 4.12 Alignment

-   Existing/Improved의 Zone Label 상단(Y 0%)과 하단(Y 13%)을 좌우
    동일하게 맞춘다.
-   두 Column은 동일한 Grid(Column 폭, Pitch 그리드)를 사용한다.
-   Step Box는 4.8에 따라 각 Flow 영역 안에서 가운데 정렬하며, 같은
    Flow 안의 모든 Step Box는 동일한 좌우 기준선(중심축)을 공유한다.
-   Process Visual Area의 상단(Y 13%)과 하단(Y 97%) 경계를 좌우
    동일하게 맞춘다.
-   중앙 Arrow(4.5)는 두 Column의 시각적 중심 사이, §4.5의 Main
    Process Flow 영역 기준 수직 중앙에 배치한다.
-   Existing과 Improved(분기 경로 포함) 양쪽에 **이름·성격이 동일
    하거나 대응되는 요소**가 존재하면, 가능한 한 **동일한 Y축(또는
    대응되는 시각적 위치)**에 배치한다 — 이를 통해 두 흐름 사이에서
    **유지되는 요소**와 **변경되는 요소**가 즉시 구분되도록 한다. 이
    원칙은 Main Visual 유형과 무관하게 적용되는 Comparison Frame의
    일부다.
-   단, 콘텐츠 구조상 억지로 동일 위치에 맞추면 오히려 비교 흐름이
    왜곡되는 경우(예: 대응 요소의 순서 자체가 달라지는 경우)에는 이
    Y축 정렬을 예외로 허용한다 — 이 경우에도 4.1\~4.3의 전체 영역
    비율과 Pitch 규칙은 그대로 유지한다.

### 4.13 Connector Line

*Main Visual이 Process/Step Sequence일 때만 적용되는 조건부 규칙이다.
단순 속성을 나열·비교하는 Before/After(Chart·Image·KPI 등 비-Process
Main Visual)에는 이 절의 Connector를 강제하지 않는다 — Connector는
Sequential/Process Variant에서만 필수 적용한다.*

Sequential/Process Main Visual에서는 각 Step Box가 하나의 흐름으로
읽히도록 Connector Line을 필수로 적용한다.

-   세로로 진행하는 공정은 각 Step Box의 **실제 가로 중심(수직
    중심축)을 정확히 지나는 Vertical Connector**를 사용한다 — Box가
    4.8에 따라 가운데 정렬되므로 이 중심축은 곧 Flow 영역의 가로
    중심과도 일치한다. Badge 등 다른 요소가 있던 자리에 맞춘 고정
    오프셋이나 Box 좌측 등 임의 지점을 잇는 연결선을 사용하지 않으며,
    좌표 계산상으로만이 아니라 **최종 렌더링 화면에서 Connector가
    Box 중심과 실제로 겹치는지 확인**한다.
-   Connector는 Step Box보다 **뒤(Behind)에 배치**한다(z-index/그리기
    순서상 Box 아래) — Box가 Connector 선 위에 얹힌 것처럼 보이도록
    하고, Connector가 Box 테두리 위로 겹쳐 보이지 않게 한다.
-   Connector 두께·색상은 Existing/Improved에서 동일하게 유지한다
    (4.7 참조). 굵기는 Step Box Border보다 얇게 유지해 Box가 항상
    시각적으로 주된 요소가 되도록 한다.
-   분기되는 공정(4.4 Branching)은 **부모 Step → Branch Connector →
    각 하위 경로**의 관계가 하나의 연결된 구조로 보이도록 한다 —
    Branch Connector는 부모 Step의 중앙 하단에서 시작해 각 경로 Step의
    중앙 상단으로 갈라져 이어져야 하며, 각 경로가 부모와 무관하게
    따로 떠 있는 것처럼 보이지 않아야 한다.
-   Connector 길이·간격은 4.3의 공통 Pitch 규칙(Box:Connector ≈
    0.7:0.3)을 따른다.
-   Outcome/Result가 4.9에 따라 다른 Step Box와 동일한 스타일의
    텍스트 노드로 표현되는 경우, 그 노드도 앞 Step과 Connector로 이어
    같은 세로 흐름 안에서 끊기지 않게 한다.

### 4.14 Conclusion (Optional)

*Main Visual 유형과 무관하게, 하단 Conclusion을 사용하기로 선택한
경우에만 적용되는 조건부 규칙이다.*

Before/After 슬라이드 하단에 별도 Conclusion 영역을 두는 경우, 좌우
Column의 내용을 단순 반복하거나 요약 재진술하지 않는다.

-   Conclusion은 **Before→After 사이에 실제로 일어난 변화의 결과**
    (예: 단계 감소, 공정 단순화, 처리시간·수율 등 성능 개선)를 한두
    문장 또는 핵심 수치로 요약한다.
-   좌측(Existing) 또는 우측(Improved) 내용을 그대로 옮겨 적거나, 두
    Column의 설명을 나열식으로 다시 나열하지 않는다.
-   Conclusion에서 사용하는 수치·주장은 실제 콘텐츠에 근거해야 하며,
    임의로 만들어내지 않는다.
-   Conclusion 영역이 본문 Comparison Frame(4.1)의 좌우 비율·정렬을
    침범하지 않도록, 본문 아래 별도 영역으로 배치한다.

------------------------------------------------------------------------

## 5. Variant B — Before/After Comparison Table

기존 방식(Existing)과 개선 방식(Improved)을 **동일한 비교 기준(Row)**
으로 나란히 비교하는 Presentation형 비교표다. 여러 대상을 비교하는
Comparison Matrix Layout(`comparison-matrix.md`)과 원칙은 유사하되,
비교 대상이 **Existing / Improved 2개로 고정**된다는 점이 다르다.

> 현재 `before-after.pptx` Reference는 Variant A(Process Transformation)
> 사례만 포함한다. 아래 수치는 Reference 실측값이 아니라 Hard Rule
> Body Box(1152×474px) 및 `comparison-matrix.md`의 Presentation형 표
> 관습에서 도출한 권장값이다. Variant B의 실제 Reference PPT가 추가로
> 제공되면 그 실측 좌표가 아래 권장값보다 우선한다.

> **Table을 Main Visual로 단독 사용(2026-08-25 추가)**: Variant B는
> 그 자체로 Comparison Table이 슬라이드의 Main Visual Structure다 —
> 이미지가 비교 내용 이해에 실질적으로 기여하지 않으면 별도 이미지나
> Supporting Visual을 추가로 요구하지 않는다(공간이 남는다는 이유로
> 무관한 이미지를 끼워 넣지 않는다는 SKILL.md Supporting Visual Value
> 원칙과 동일). 이미지가 실제로 필요한 경우(예: 구조 단면도처럼 텍스트로
> 대체 불가능한 근거)에는 기존처럼 Table 하단 Supporting Visual로
> 추가할 수 있다.

### 5.1 Overall Region Map

Body Box(1152×474px, Hard Rule §9 기준)를 기준으로 한다.

| 영역 | X 범위 | Y 범위 | 비고 |
|---|---|---|---|
| Criteria Column | 0\~20% | 0\~100% | `구분`/`비교 기준` 열 |
| Existing Column | 20\~59% | 0\~100% | 폭 약 39% |
| Improved Column | 59\~100% | 0\~100% | 폭 약 41%, 강조 시 최대 45%까지만 확장 |
| Header Row | 전체 폭 | 0\~14% | 3 Column 공통 높이 |
| Data Row(각 Row) | 전체 폭 | Header 이후 균등 분할 | 5.3 참조 |
| Vertical Divider | Column 경계 2곳(X 20%, X 59%) | Header 하단(Y 14%)\~마지막 Row 하단 | Table Grid — Hard Rule §10B Table Header Row 참조. Header Row(Y 0\~14%) 영역은 침범하지 않는다 |
| Horizontal Divider | 전체 폭 | 각 Row 경계 | Table Grid — Hard Rule §10B Table Header Row 참조 |

`Comparison Criteria | Existing Process | Improved Process` 구조를
기본으로 하며, 첫 번째 열은 비교 기준, 나머지 두 열은 각각 기존
방식과 개선 방식을 표시한다. 동일한 비교 기준의 정보는 같은 Y축
위치에 배치해 가로 방향으로 즉시 비교 가능해야 한다.

### 5.2 Header Row

-   각 방식의 이름(예: `기존 공정`/`개선 공정`, 또는 실제 공정명·자사
    기술명)을 Header Row(Y 0\~14%)에 배치한다.
-   첫 번째 Header는 `구분`, `비교 기준` 등 비교 기준 영역임을
    나타낸다.
-   Header의 높이와 Y 위치는 3개 Column에서 동일하게 유지한다.
-   Existing/Improved Header는 각 Column 폭 중앙 정렬을 기본으로
    한다.
-   Header 색상·Typography·Divider는 **Hard Rule §10B Table Header
    Row**를 따른다(이 문서에서 재정의하지 않음).
-   일반 표처럼 모든 셀에 강한 테두리를 사용하지 않는다.

### 5.3 Row 개수와 높이

-   비교 기준(Row)은 3\~6개를 권장 범위로 한다. 6개를 초과하면
    한 Row의 높이가 지나치게 얇아져 Cell 내부 Visual을 배치하기
    어렵다 — 이 경우 우선순위가 낮은 기준을 줄이거나 Comparison
    Matrix Layout을 재검토한다.
-   각 Data Row의 높이는 `(100% - Header 14%) ÷ Row 개수`로 균등
    분할하는 것을 기본으로 한다. 단, 이미지/Diagram이 들어가는 Row는
    텍스트만 있는 Row보다 최대 1.5배까지 높게 배분할 수 있다 — 이
    경우 다른 Row를 그만큼 축소해 전체 합이 100%를 넘지 않게 한다.
-   Row 간 Horizontal Divider(Table Grid)는 **Hard Rule §10B Table
    Header Row**를 그대로 따른다.

### 5.4 Criteria Column

비교 기준 예시: 공정단수, 공정시간, 비용, 효율, 부산물, 성능, 수율,
사용량 등.

-   비교 기준은 짧고 명확하게 작성한다.
-   모든 비교 기준은 Column 폭(0\~20%) 내 동일한 X축 정렬(좌측
    정렬 기본)과 텍스트 위계를 유지한다.
-   각 Row의 중앙 높이에 정렬하여 해당 행과 자연스럽게 연결되도록
    한다.
-   필요 시 기준명 아래에 단위 또는 짧은 설명(Sub Label)을 추가할 수
    있다.

### 5.5 Comparison Cells

각 방식의 Cell은 단순 텍스트만 사용하지 않고, 정보 특성에 따라 적합한
표현 방식을 선택한다.

사용 가능한 표현 방식: Short Text, Key Number/KPI, Photo, Diagram,
Icon, Mini Chart, Badge/Label, Short Bullet 등.

-   같은 Row에서는 Existing/Improved 두 Cell이 가능한 한 동일한 정보
    유형과 정보량을 사용해 비교가 쉬워야 한다.
-   Visual이 있는 Cell은 해당 Row 높이의 **약 70\~80%를 Visual이
    차지**하도록 크게 배치한다. 나머지 20\~30%는 짧은 Label/수치용
    여백이다 — Visual을 Row 높이의 40% 이하로 축소하지 않는다.
-   필요 시 사진, Diagram, 수치, 짧은 설명을 Cell 내부에 함께 배치할
    수 있다.
-   한 Cell당 핵심 메시지는 1\~3개 이내로 제한하고 긴 문단은 사용하지
    않는다.

### 5.6 Presentation Table Style

이 Variant는 일반적인 표(Table)보다 **Presentation형 비교표**를
우선한다.

-   모든 Cell에 사각 테두리를 넣지 않는다.
-   Row/Column 구분은 **Hard Rule §10B Table Header Row**의 Table
    Grid 규칙(얇은 직선)을 따른다 — Column 간 구분이 필요한 경우
    Criteria/Existing 경계, Existing/Improved 경계 총 2개를 넘지 않는다.
-   Excel처럼 모든 Cell에 Box Border를 적용하지 않는다.
-   Cell을 개별 Card(둥근 모서리+그림자)로 감싸지 않는다 — Divider로만
    구분되는 연속된 표 형태를 유지한다.
-   과도한 배경색 사용을 피한다.

### 5.7 Improved / 자사 Column 강조

개선안(Improved) 또는 자사 기술 Column을 강조해야 하는 경우:

-   Main Color의 Header 색상 강조
-   Main Color의 굵은 Outline(Column 전체 또는 Header만)
-   핵심 수치에 Main Color 적용
-   다른 Column보다 시각적 대비를 약간 높임

[2026-08-25 추가] "Main Color의 Header 색상 강조"는 §5.2의 Header Row
전체 동일 Fill(Hard Rule §10B) 기본값 대신, **Existing/Criteria
Header는 White(Fill 없음) 유지 + Improved Header만 Light Tint 배경
(`--c-tint-lightest`)·Main Color Text·Main Color Bottom Border**로
차등 적용하는 형태로 구현해도 된다 — 이 경우 Row/Column Divider는
5.9와 같이 얇고 연하게(§8 Hard Rule §11 색상), 표 외곽 전체를 두르는
Border는 사용하지 않는다(§5.6 Excel식 표 금지 원칙과 일관).

Rules:

-   강조는 최대 1개 Column(Improved)을 기본으로 한다.
-   강조해도 Improved Column 폭은 5.1 기준(41%, 최대 45%)을 넘지
    않는다.
-   강조 때문에 비교 구조 자체가 무너지지 않도록 한다.
-   실제 콘텐츠에서 개선안/자사 기술이 명확한 경우에만 적용한다.

### 5.8 Density & Spacing

-   Reference와 유사한 중간\~높은 정보 밀도를 유지한다.
-   Row 간 간격은 비교 가독성을 해치지 않는 범위에서 최소화한다 —
    Row 사이 여백을 Row 내부 Cell 여백보다 크게 만들지 않는다.
-   이미지/Diagram이 있는 Row는 해당 Visual을 5.5 기준대로 충분히
    크게 사용한다.
-   Header Row와 첫 번째 Data Row 사이 간격을 일정하게 유지한다.

### 5.9 Alignment

-   동일 Row의 콘텐츠는 동일한 수직 기준선(Row 중앙)에 맞춘다.
-   동일 Column의 콘텐츠는 동일한 중심축(Column 중앙)을 유지한다.
-   Header와 Data Cell의 Column Center를 일치시킨다.
-   Improved Column이 강조되어도 전체 Grid Alignment는 유지한다.

------------------------------------------------------------------------

## 6. Flexibility (공통)

### Must Preserve

-   Existing(Before) vs Improved(After)의 명확한 대비 구조 — Variant
    A는 좌우 Main Visual 대비, Variant B는 Column 대비로 표현
-   기존 대비 개선이라는 핵심 메시지
-   Variant A: 중앙 Transformation 표현(§4.5 — Reference 원본 Chevron
    이미지를 그대로, 비율 유지, Step Box 1개와 비슷한 체감 크기, 별도
    Caption 없음), [4.1](#41-overall-region-map) 영역 비율, 좌우 Main
    Visual의 비교 가능한 위치·크기·정렬(Comparison Frame). Main
    Visual이 Process/Step Sequence일 때는 각 Flow의 단계 구조도
    포함(단, Flow 간 대칭은 요구하지 않는다 — 4.2/4.4 참조), 같은
    위계 Step Box의 동일 크기·가운데 정렬(§4.8), Comparison Marker
    (Badge/Bracket/Label) 미사용, 병렬 분기 Flow의 동일 Y 시작점(§4.4),
    본문 콘텐츠 변경에 영향받지 않는 고정 Header Bar(§4.2), Step Box
    내부 Text와 Flow 설명 Text의 16pt·가운데 정렬(§4.2/4.7), Flow
    설명 Text와 첫 Step Box 사이 세로 Gap(§4.2), 텍스트 노드로 표현되는
    Outcome/Result의 동일 Step Box 스타일·Connector 연결(§4.9/4.13)
-   Variant B: Criteria Row / Existing·Improved Column 구조, 동일
    기준 가로 비교, [5.1](#51-overall-region-map) 영역 비율

### May Adapt

-   Variant A: **Main Visual 유형**(Process/Diagram/Chart/Image/KPI
    중 콘텐츠에 맞게 선택, 단 Existing·Improved 동일 유형 유지),
    Main Visual이 Process/Step Sequence일 때의 Step 개수(Region Map의
    Pitch 비율은 유지한 채 비례 조정), Vertical/Branch Process 형태,
    Existing/Improved 각 Flow의 분기 여부·Step 수(좌우 대칭 불필요),
    Flow별 Outcome/Result 표현 방식(§4.9), Result Visual·Input/Output
    이미지 사용 여부, 같은 위계 Step Box의 구체적 크기 값(단, 같은
    Flow·같은 위계 내에서는 동일 크기 유지)
-   Variant B: 비교 기준 개수(3\~6개 권장 범위 내), Cell 내부 Visual
    유형, Improved Column 강조 여부, Header 배경색 여부, Vertical
    Divider 사용 여부

## 7. Avoid (공통)

-   Existing과 Improved를 서로 다른 디자인 언어로 표현
-   (Variant A) 중앙 Arrow 없이 좌우 Main Visual을 단순 병렬 배치
-   (Variant A) 겹친 Chevron(§4.5) 원본 이미지를 CSS 도형으로 재구성
    하거나 단일 화살표·다른 Arrow 아이콘으로 임의 대체하는 것, 또는
    원본 비율을 무시하고 늘리거나 눌러 압축하는 것
-   (Variant A) 중앙 Arrow 아래·주변에 "Redesign" 등 설명 Caption을
    추가하는 것 — 중앙에는 Arrow만 둔다
-   (Variant A) Number Badge/Side Bracket/단계 수 Label 등 Comparison
    Marker를 추가하는 것(§4.8) — 변화는 Process 구조 자체로 전달한다
-   (Variant A) 같은 위계의 Step Box를 Flow마다 다른 크기로 만들거나,
    텍스트가 길다는 이유로 Box를 키우는 것(§4.8) — Box 크기는 통일하고
    긴 텍스트는 줄바꿈으로 처리한다
-   (Variant A) 병렬 분기 경로마다 다른 Y 시작점을 사용하거나 각
    경로를 개별적으로 수직 중앙 정렬해 서로 다른 세로 범위에서
    시작하게 만드는 것(§4.4)
-   (Variant A) [2. Prohibited Reinterpretations](#2-reference-reproduction-principle)에
    나열된 Card/Placeholder Icon/균일 Grid/전체 높이 Arrow 등으로
    재해석
-   (Variant B) 모든 Cell에 강한 Box Border를 적용하는 Excel식 표
-   (Variant B) Cell을 개별 Card로 감싸 Divider 기반 표 구조를 깨는 것
-   Step 설명 또는 Cell 설명을 긴 문장으로 작성
-   단계 감소가 핵심인데(Variant A) Existing/Improved의 실제 Step
    개수·배치를 왜곡해 변화가 한눈에 읽히지 않게 만드는 것
-   불필요한 장식으로 Main Visual 전달력(Variant A) 또는 비교
    가독성(Variant B)을 방해
-   Existing보다 Improved가 더 복잡하거나 불리하게 보이는 잘못된 정보
    위계
-   Reference의 특정 공정명/회사명/이미지/수치 복제
-   Hard Rule 또는 Claude PPT Design System 변경

## 8. Rule Priority

적용 우선순위:

1.  **Hard Rule**
2.  **Claude PPT Design System**
3.  **Reference PPT 실측 비율** ([2. Reference Reproduction
    Principle](#2-reference-reproduction-principle), Variant A는
    [4.1](#41-overall-region-map) 기준)
4.  **Before + After Layout Reference** 서술 규칙(Variant A. Process
    Transformation 또는 Variant B. Before/After Comparison Table)

본 Layout Reference는 Hard Rule 및 Claude PPT Design System을
변경하거나 대체하지 않는다.

## 9. Selection Rule

다음 조건을 만족할 때 이 Layout(Before/After 계열)을 우선 고려한다.

1.  비교 대상이 기존(Existing) 1개와 개선(Improved) 1개로 명확히
    구분됨
2.  그 변화를 통해 개선·단순화·효율화를 전달하는 것이 핵심 메시지임

조건을 만족하면 다음 기준으로 Variant를 선택한다.

-   "단계 수·순서·분기·통합 등 Process 구조가 어떻게 달라지는가"가
    핵심 → **Variant A. Process Transformation**
-   "기존 대비 무엇이 얼마나 개선되는가"를 여러 기준으로 보여주는
    것이 핵심 → **Variant B. Before/After Comparison Table**

비교 대상이 3개 이상으로 늘어나면 Comparison Matrix
Layout(`comparison-matrix.md`)을 사용한다. 비교 대상(Existing vs
Improved) 없이 공정 흐름 하나만 설명하면 된다면 Process / System
Architecture Layout(`process-system-architecture-layout.md`)을
우선하고, Process 흐름 없이 속성·스펙·평가 항목만 비교한다면 Table
Comparison Layout(`table-comparison.md`) 또는 Comparison Matrix
Layout을 우선한다(§1 Do Not Use When 참조). 단순히 장점이 여러 개
있다는 이유만으로 이 Layout(특히 Variant B)을 적용하지 않는다.
