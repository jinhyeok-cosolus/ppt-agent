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
-   공정 단계가 여러 단계에서 1\~2단계로 감소하는 경우 (→ Variant A)
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

------------------------------------------------------------------------

## 2. Reference Reproduction Principle

이 Layout Reference에는 실제 Reference PPT(`before-after.pptx`, DLE
공정 4단계→1단계 전환 사례)가 함께 등록되어 있다. 이 문서의 [4. Variant
A](#4-variant-a--process-transformation) 수치·영역 구조는 해당
Reference의 실측 좌표를 그대로 비율화한 것이다.

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
| "어떤 단계가 어떻게 줄어드는가"가 핵심 | **Variant A. Process Transformation** |
| "기존 대비 무엇이 얼마나 개선되는가"를 여러 기준으로 보여주는 것이 핵심 | **Variant B. Before/After Comparison Table** |

-   두 질문 모두에 해당하는 콘텐츠(공정 흐름도 보여줘야 하고, 동시에
    다수의 정량 기준으로도 비교해야 하는 경우)는 이 문서의 두 Variant를
    한 슬라이드에 억지로 합치지 않는다. 이런 경우 Process +
    Comparison Layout(`process-comparison.md`)이 더 적합한지 먼저
    검토한다.
-   단순히 표 형태로 정리할 수 있다는 이유만으로 Variant B를 선택하지
    않는다 — 공정 단계 자체의 변화가 메시지의 핵심이면 Variant A를
    우선한다.
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

### 4.1 Overall Region Map

Body Box(1152×474px)를 기준으로 한 영역 좌표다. 실제 좌표는
`64 + (X% × 11.52)`, `182 + (Y% × 4.74)`로 환산한다.

| 영역 | X 범위 (Body Box 기준) | Y 범위 (Body Box 기준) | 비고 |
|---|---|---|---|
| Existing(Left) Column | 0\~44% | 0\~100% | Improved와 동일한 내부 구조(4.2) 사용 |
| Transformation(Center) Column | 44\~54% | 0\~100% | 폭 8\~12%(기본 10%), 좌우 Column 폭에서 조정 |
| Improved(Right) Column | 54\~98% | 0\~100% | Existing과 동일한 내부 구조(4.2) 사용, 우측 2%는 여백 |
| Column Zone Label | 각 Column 폭 전체 | 0\~13% | 좌우 동일 Y, 상단 기준선 정렬 |
| Process Visual Area | 각 Column 폭의 80\~90%(Column 내 좌측 정렬, Number Badge+Box 구조, 4.2 참조) | 13\~97% | Column 가용 높이의 대부분을 사용 |

Column 폭(44:10:44)은 콘텐츠 복잡도에 따라 ±3%p까지 조정할 수 있으나,
어느 한쪽 Column이 다른 쪽보다 명백히 좁아 보이지 않도록 좌우
균형(대칭)을 기본으로 한다. 좌우 Process 중 하나만 강조가 필요한
경우에도 Column 폭이 아니라 4.6의 색상/정보 강조로 처리한다.

### 4.2 Process Column — 공통 내부 구조 (Existing / Improved 동일 적용)

Existing과 Improved는 아래 동일한 정보 위계와 구조를 공유한다.

**Zone Label** ↓ **(선택) Input / Starting Material** ↓ **Step Box +
Connector 시퀀스(단일 또는 분기)** ↓ **(선택, 실제 자산이 있을 때만)
Result / Output Visual**

-   Zone Label은 Column 폭 전체를 사용하는 얇은 라벨/배지이며, 좌우
    Column에서 동일한 높이(Y 0\~13%)와 스타일을 사용한다.
-   Process Visual Area(Y 13\~97%, 84%p)는 Column의 가용 높이 전체를
    적극적으로 사용한다. 상단에 내용이 몰리고 하단이 비어 보이는
    구성을 금지한다.
-   Step Box는 Column 폭의 약 65\~80%를 차지하도록 크게 배치한다
    (Number Badge를 위한 좌측 여백 약 8\~12%, 우측 여백 약 10\~15%
    제외). Column 폭의 15\~20%만 차지하는 작은 Box를 한쪽에 몰아
    배치하지 않는다.
-   Step Box는 그림자·큰 모서리 반경·넉넉한 내부 Padding을 가진 Web
    UI Card가 아니라, 얇은 Border 또는 옅은 배경 + 명확한 Number
    Badge + 얇은 Connector로 구성된 PPT형 Process Box로 표현한다
    (4.7 참조).
-   같은 종류의 정보(Step 이름, 부가 설명, Number Badge 등)는
    Existing과 Improved에서 동일한 시각적 표현 방식(같은 폰트 크기,
    같은 Badge 모양, 같은 Box 비례)을 사용해 가로로도 직접 비교되도록
    한다.

### 4.3 Step Box 크기 산정 — 공통 Pitch 규칙

두 Column의 Step Box는 **Step(노드) 수가 더 많은 Column을 기준으로
계산한 Pitch를 양쪽에 동일하게 적용**한다.

-   기준 Pitch = Process Visual Area 높이(84%p) ÷ (두 Column 중 더
    많은 Step 수). 예: 한쪽이 4 Step이면 Pitch ≈ 21%p.
-   Step Box 높이 = Pitch × 0.65\~0.75, 나머지(0.25\~0.35)는
    Connector가 차지한다. Box가 Connector보다 항상 크게 유지되어
    Process Box + Connector 리듬이 유지되도록 한다.
-   Step 수가 적은 Column(예: Improved 1\~2 Step)도 **동일한 Pitch와
    동일한 Box 높이**를 사용한다 — Step 수가 적다는 이유로 Box를 이
    비율 이상으로 확대해 하나의 거대한 색상 Box를 만들지 않는다.
-   Step 수가 적어 발생하는 남는 세로 공간은 다음 중 하나로만 채운다.
    1.  4.4의 분기(Branch) 구조로 자연스럽게 높이를 채우는 경우
    2.  실제로 제공된 Result/Output Visual(사진, 수치, 그래프 등,
        4.9 참조)
    3.  Connector 길이를 Pitch 범위 내에서 여유 있게 사용하는 것
        (단, Box보다 길어지지 않는 범위)
    실제 콘텐츠·자산이 없으면 억지로 채우지 않고 Process Visual Area
    내에서 Step 시퀀스를 수직 중앙에 배치해 남는 여백을 상하로
    분산시킨다.
-   임의의 Placeholder 이미지, 예시용 사진, 관련 없는 장식 Icon으로
    남는 공간을 채우지 않는다.

### 4.4 Branching Process (분기형 Improved)

개선 공정이 단일 경로가 아니라 2개 이상의 경로로 분리되는 경우(예:
하나의 기존 공정이 목적에 따라 서로 다른 길이의 2개 신규 공정으로
분리), 다음을 따른다.

-   분기점(Branch Point)은 Improved Column 상단, Input 또는 첫 Step
    직후에 배치한다.
-   각 분기 경로는 4.3의 공통 Pitch/Box 높이를 동일하게 사용한다 —
    경로별로 Box 크기를 다르게 만들지 않는다.
-   경로 길이가 서로 다르면(예: 2 Step vs 4 Step), 더 긴 경로가 Column
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

중앙은 Before에서 After로의 변화 방향을 간결한 Arrow로 표현한다.

-   Arrow는 Center Column 폭(8\~12%) 안에서 좌우 Process Box보다
    얇고 가벼운 형태를 유지한다 — 폭과 시각적 무게 모두 좌우 Step
    Box를 넘지 않는다.
-   Arrow 높이는 본문 높이의 약 25\~40%를 기본으로 하며, Process
    Visual Area의 수직 중앙에 배치한다. 본문 전체를 채우는 거대한
    세로 Bar로 확대하지 않는다.
-   Arrow 위·아래에 과도한 빈 여백을 만들지 않는다 — Arrow가 좌우
    Process의 시각적 흐름 사이에 자연스럽게 끼워지도록, 위아래 여백은
    좌우 Step Box의 Connector 간격과 비슷한 수준으로 유지한다.
-   Design System의 Main/Light Color를 활용할 수 있다.
-   텍스트는 최소화하고, 넣더라도 한 단어 수준으로 짧게 유지한다.

### 4.6 Improved 강조 방법 (크기가 아닌 색상/정보로 강조)

Improved Process가 Existing보다 시각적으로 더 크거나 진한 Box로
확대되어 강조되는 것을 금지한다. 대신 다음 방법만 사용한다.

-   Step Box의 배경색 또는 Border를 Brand Color(Cosolus Teal 계열)로
    채운다. Existing은 Neutral Gray 계열을 유지한다.
-   Number Badge, 핵심 수치, Step Count 라벨 등 핵심 정보에 Brand
    Color를 적용한다.
-   Typography Weight를 한 단계 높여(예: SemiBold→Bold) 정보 위계를
    강조할 수 있다. 단, Font Size 자체를 Existing보다 크게 키우지
    않는다.
-   Box 크기, Column 폭, Padding은 Existing과 동일하게 유지한다 —
    강조는 색과 정보 밀도로만 표현한다.

### 4.7 Process Step Style

-   Step은 얇은 Border 또는 옅은 배경의 Box + Number Badge +
    Connector 조합을 기본으로 한다.
-   그림자(Box Shadow), 큰 모서리 반경, 넉넉한 내부 Padding을 가진
    Web UI Card 스타일을 사용하지 않는다.
-   연결선/Arrow 스타일은 Existing과 Improved에서 동일하게 유지한다.
-   Step 이름은 짧고 명확하게 작성한다.
-   동일 레벨 Step은 Existing/Improved 관계없이 동일한 크기와
    Typography를 사용한다(4.3 참조).

### 4.8 Step Count Emphasis

공정 단수 감소가 핵심 메시지인 경우 단계 수를 적극적으로 보여준다.

예: `4 Steps → 2 Steps`, `4 Steps → 4 Steps(공정 분리)` 등 실제
콘텐츠에 근거해 표기한다.

-   단계 수 표시는 각 Column의 Process Box 시퀀스 바로 옆(Side
    Bracket 또는 인접 라벨)에 배치해, 두 Column을 눈으로 오가지 않고도
    단계 수 차이가 즉시 비교되도록 한다.
-   단계 수는 실제 콘텐츠에 근거할 때만 사용한다.

### 4.9 Input / Output / Result Visual

-   Input은 Process 시퀀스 시작점 위(Process Visual Area 상단)에
    배치한다.
-   Output/Result는 Process 시퀀스 끝(하단)에 배치하되, **실제로
    제공된 이미지·수치·그래프가 있을 때만** 배치한다.
-   실제 자산이 없는 경우 Result Visual 자리를 임의의 Placeholder나
    예시 이미지로 채우지 않는다 — 대신 4.3의 남는 공간 처리 규칙(분기
    구조, 여유 Connector, 또는 단순 여백)을 따른다.
-   Existing과 Improved 양쪽에 Result Visual을 둘 경우, 동일한 표현
    방식(예: 둘 다 사진, 둘 다 수치 카드)을 사용해 직접 비교 가능하게
    한다.

### 4.10 Visual Hierarchy

핵심 시선 흐름:

`Existing Process → Transformation Arrow → Improved Process → 핵심 개선 지표`

-   사용자가 3\~5초 내에 기존 대비 무엇이 달라졌는지 파악할 수 있어야
    한다.
-   Improved의 핵심 개선(단계 감소, 효율 등)이 가장 중요한 Visual
    Message가 되도록 색상·정보 강조(4.6)로 유도한다.
-   세부 설명은 Process 이해를 보조하는 수준으로 제한한다.

### 4.11 Density & Spacing

-   Existing/Improved 모두 Process Visual Area(Y 13\~97%)의 가용
    높이를 적극적으로 사용한다 — 어느 한쪽만 본문 상단에 작게 몰려
    있고 하단이 비는 구성을 금지한다.
-   좌우 Process의 실제 Visual 점유 높이와 시각적 무게(Box 개수 ×
    크기 + Result Visual)를 가능한 한 유사하게 맞춘다.
-   Step Box와 Connector 크기는 4.3의 공통 Pitch 규칙을 따른다.
-   중앙 Arrow는 4.5 기준을 넘어서는 여백을 만들지 않는다.

### 4.12 Alignment

-   Existing/Improved의 Zone Label 상단(Y 0%)과 하단(Y 13%)을 좌우
    동일하게 맞춘다.
-   두 Column은 동일한 Grid(Column 폭, 좌측 여백, Number Badge
    위치)를 사용한다.
-   Step Box의 좌측 시작 X는 각 Column 내에서 동일한 기준선을
    사용한다.
-   Process Visual Area의 상단(Y 13%)과 하단(Y 97%) 경계를 좌우
    동일하게 맞춘다.
-   중앙 Arrow(4.5)는 두 Column의 시각적 중심 사이, Process Visual
    Area 수직 중앙에 배치한다.

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

### 5.1 Overall Region Map

Body Box(1152×474px, Hard Rule §9 기준)를 기준으로 한다.

| 영역 | X 범위 | Y 범위 | 비고 |
|---|---|---|---|
| Criteria Column | 0\~20% | 0\~100% | `구분`/`비교 기준` 열 |
| Existing Column | 20\~59% | 0\~100% | 폭 약 39% |
| Improved Column | 59\~100% | 0\~100% | 폭 약 41%, 강조 시 최대 45%까지만 확장 |
| Header Row | 전체 폭 | 0\~14% | 3 Column 공통 높이 |
| Data Row(각 Row) | 전체 폭 | Header 이후 균등 분할 | 5.3 참조 |
| Vertical Divider | Column 경계 2곳(X 20%, X 59%) | Header 하단(Y 14%)\~마지막 Row 하단 | 1px, Line Color. Hard Rule §11에 따라 Header Row(Y 0\~14%) 영역은 침범하지 않는다 |
| Horizontal Divider | 전체 폭 | 각 Row 경계 | 1px, Row 수만큼 |

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
-   Header 색상과 Typography는 Claude PPT Design System을 따른다.
-   일반 표처럼 모든 셀에 강한 테두리를 사용하지 않는다 — Header
    하단에만 Divider(1\~2px, Main/Line Color)를 사용한다.

### 5.3 Row 개수와 높이

-   비교 기준(Row)은 3\~6개를 권장 범위로 한다. 6개를 초과하면
    한 Row의 높이가 지나치게 얇아져 Cell 내부 Visual을 배치하기
    어렵다 — 이 경우 우선순위가 낮은 기준을 줄이거나 Comparison
    Matrix Layout을 재검토한다.
-   각 Data Row의 높이는 `(100% - Header 14%) ÷ Row 개수`로 균등
    분할하는 것을 기본으로 한다. 단, 이미지/Diagram이 들어가는 Row는
    텍스트만 있는 Row보다 최대 1.5배까지 높게 배분할 수 있다 — 이
    경우 다른 Row를 그만큼 축소해 전체 합이 100%를 넘지 않게 한다.
-   Row 간 Horizontal Divider는 1px, Line Color(`#E1E7E5`)를 기본으로
    한다.

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
-   얇은 Horizontal Divider(1px)를 중심으로 Row를 구분한다.
-   Column 간 구분이 필요한 경우 최소한의 Vertical Divider(1px)만
    사용한다 — Criteria/Existing 경계, Existing/Improved 경계 총
    2개를 넘지 않는다.
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
    A는 좌우 Process 대비, Variant B는 Column 대비로 표현
-   기존 대비 개선이라는 핵심 메시지
-   Variant A: 중앙 Transformation Direction, 기존/개선 Process의
    단계 구조, [4.1](#41-overall-region-map) 영역 비율
-   Variant B: Criteria Row / Existing·Improved Column 구조, 동일
    기준 가로 비교, [5.1](#51-overall-region-map) 영역 비율

### May Adapt

-   Variant A: Step 개수(Region Map의 Pitch 비율은 유지한 채 비례
    조정), Vertical/Branch Process 형태, Step Count 강조 방식, Result
    Visual·Input/Output 이미지 사용 여부
-   Variant B: 비교 기준 개수(3\~6개 권장 범위 내), Cell 내부 Visual
    유형, Improved Column 강조 여부, Header 배경색 여부, Vertical
    Divider 사용 여부

## 7. Avoid (공통)

-   Existing과 Improved를 서로 다른 디자인 언어로 표현
-   (Variant A) 중앙 Arrow 없이 두 공정을 단순 병렬 배치
-   (Variant A) [2. Prohibited Reinterpretations](#2-reference-reproduction-principle)에
    나열된 Card/Placeholder Icon/균일 Grid/전체 높이 Arrow 등으로
    재해석
-   (Variant B) 모든 Cell에 강한 Box Border를 적용하는 Excel식 표
-   (Variant B) Cell을 개별 Card로 감싸 Divider 기반 표 구조를 깨는 것
-   Step 설명 또는 Cell 설명을 긴 문장으로 작성
-   단계 감소가 핵심인데(Variant A) Step Count를 숨김
-   불필요한 장식으로 Process Flow(Variant A) 또는 비교
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

-   "어떤 단계가 어떻게 줄어드는가"가 핵심 → **Variant A. Process
    Transformation**
-   "기존 대비 무엇이 얼마나 개선되는가"를 여러 기준으로 보여주는
    것이 핵심 → **Variant B. Before/After Comparison Table**

비교 대상이 3개 이상으로 늘어나면 Comparison Matrix
Layout(`comparison-matrix.md`)을 사용하고, 공정 흐름 하나만 필요하다면
일반 Process Layout을 우선한다. 단순히 장점이 여러 개 있다는 이유만으로
이 Layout(특히 Variant B)을 적용하지 않는다.
