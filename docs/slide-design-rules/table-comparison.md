# Table Comparison Layout Reference

## 1. Purpose

여러 대상(자사/경쟁사, 제품 A/B/C, 스펙 항목 등)을 **직각형 Data Table
구조**로 병렬 비교할 때 사용하는 레이아웃이다. Diagram·Icon·자유
배치 중심의 시각적 비교가 아니라, 실제 스펙시트·데이터시트처럼 행·열이
명확히 구획된 표 형태로 정보를 빽빽하게 정리해 보여주는 데 목적이
있다.

### Use When

-   제품/기술 스펙을 항목별로 표 형태로 나열해야 하는 경우
-   자사와 경쟁사(또는 여러 대상)를 동일 기준의 행으로 촘촘히 비교해야
    하는 경우
-   수치·데이터 중심이라 Diagram보다 표가 더 정확하고 신뢰도 있게
    전달되는 경우
-   비교 항목(Row) 수가 많아 Card/Diagram형 배치로는 밀도를 감당하기
    어려운 경우
-   Cell의 지배적 콘텐츠가 텍스트·수치·기호·등급 등이며, Visual을 보는
    것보다 **평가값을 정확히 읽는 것이 핵심**인 경우. 텍스트와 Visual이
    함께 있어도 Visual이 보조이고 평가값 판독이 핵심이면 본 Layout을
    우선한다.

### Do Not Use When

-   비교 대상이 2개뿐이고 Before/After처럼 변화·전환 자체가 핵심인
    경우 → Before/After Layout(`before-after.md`)
-   비교 항목마다 Icon/Diagram/이미지·강조 배지 등을 자유롭게 배치해
    항목별로 다른 시각적 구성을 허용해야 하는 경우 → Comparison
    Matrix Layout(`comparison-matrix.md`). **Table Comparison과
    Comparison Matrix는 서로 다른 별도 Layout이다** — 둘 다 "여러
    대상을 비교"하지만, Comparison Matrix는 Cell마다 자유로운 시각적
    구성을 허용하는 반면, 본 Layout은 직각형 Grid에 갇힌 정형화된
    Table Cell 구조를 강제한다는 점에서 명확히 구분한다. 두 Layout을
    혼용하거나 서로의 규칙을 가져와 섞지 않는다.
-   사진·실험결과·그래프·Diagram 등 면적 점유형 Visual Evidence가
    핵심 주장을 직접 증명하는 Required Evidence인 경우 → Comparison
    Matrix Layout(`comparison-matrix.md`)
-   하나의 솔루션이 만드는 정확히 2개의 병렬 효과를 보여주는 경우 →
    Benefit + Impact Layout(`benefit-impact.md`)

------------------------------------------------------------------------

## 2. Reference Reproduction Principle

이 Layout Reference는 통합 Layout Catalog PPT
(`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`, **17번
슬라이드 — Layout Catalog `L17. Table / Matrix`**)의 실측 좌표를
근거로 한다. 해당 슬라이드는 특정 사례가 아니라 범용 Table Wireframe
템플릿이므로, 다음을 구분해서 적용한다.

**재현 대상 (구조·비율)**

1.  Column/Row가 **완전히 맞닿은 직각형 Grid**로 구성되고, 카드형으로
    분리·이격되지 않는다는 점
2.  Column/Row가 임의로 들쭉날쭉 배치되지 않고 하나의 정렬된 Grid
    축을 공유한다는 점(모든 Row에서 Column 경계 X 위치 동일, 모든
    Column에서 Row 경계 Y 위치 동일) — Reference의 구체적 폭·높이
    수치(5 Column/5 Row 균등 20%)는 재현 대상이 아니며, 실제 폭·
    높이는 [4](#4-grid-column--row-규칙)에 따라 콘텐츠 분량 기준으로
    정한다
3.  Table Title → 여백 → Grid → 여백 → (선택) Highlight/Footnote
    Band로 이어지는 세로 정보 흐름과 그 사이 여백 리듬
4.  Cell 내부 텍스트가 수평·수직 모두 중앙 정렬된다는 배치 원칙

**재현하지 않는 대상 (Wireframe placeholder이므로 무시)**

-   Cell Fill 색상(`#E7EAED`), Border 색상(`#C6CBD0`), Header/Body
    동일 회색조 — 실제 색상은 Hard Rule §5 Color Usage 및 Visual
    Style(Claude PPT Design System)을 따른다
-   `TABLE TITLE`/`HEADER`/`ITEM`/`DATA` 같은 Placeholder 텍스트,
    Arial 폰트, 9~21pt 임의 크기 — 실제 Typography는
    [10. Typography](#10-typography)를 따른다
-   Reference의 5열(기준 1 + 대상 4) × 5행(Header 1 + Body 4) 구성
    자체는 예시 값일 뿐 고정 값이 아니다 — 실제 Column/Row 수는
    콘텐츠에 맞게 [4](#4-grid-column--row-규칙)의 범위 내에서 정한다

------------------------------------------------------------------------

## 3. Overall Structure

### Table 배치 원칙

Table의 크기와 위치는 고정 좌표로 못박지 않는다 — 슬라이드 안에서
Table이 다른 콘텐츠와 어떤 관계로 구성되는지에 따라 매번 달라진다.

-   **[우선조건] 다른 Slide Layout의 Content Area 내부에서 Table을
    사용하는 경우**(예: 다른 Layout Reference의 Evidence Visual/Cell
    등 하위 영역 안에 Table을 부분 요소로 넣는 경우): Table의 위치·
    크기는 **해당 Slide Layout의 배치 규칙을 우선 적용**한다. 이때
    table-comparison.md는 Table 자체의 행·열 구조와 디자인
    ([4](#4-grid-column--row-규칙)~[10](#10-typography))만 적용하고,
    배치(크기·위치)에는 관여하지 않는다.
-   아래 배치 유연성 규칙(핵심 Visual 여부에 따른 확대/축소 판단,
    Overall Region Map)은 **Table 자체가 슬라이드의 핵심 Layout일
    때만** 적용한다.
-   **Table이 슬라이드의 핵심 Visual인 경우**(다른 Chart/Image 없이
    비교 자체가 메시지의 중심): 아래 [Overall Region Map](#overall-region-map)의
    기본값대로 Body Box(폭 1152px 기준) 전체 폭을 넓게 사용한다.
-   **Chart/Image 등 다른 핵심 Visual과 함께 배치되는 경우**: Table을
    Body Box 전체에 펼치지 않고, 그 다른 Visual과 나란히 구성된 자신의
    **Content Area(할당된 하위 영역) 안에서만** 축소 배치한다 — Table이
    다른 핵심 Visual 영역을 침범하거나 겹치지 않는다.
-   **축소 배치 시에도** [4. Grid Column / Row 규칙](#4-grid-column--row-규칙)의
    행·열 구조(Header Row + Body Row 구분, Column/Row 경계 정렬 축)와
    [5. Cell 구조](#5-cell-구조-공통-variant-ab-공통-적용)의 디자인
    비율(테두리 굵기, Cell 내부 정렬·여백 비율 등)은 그대로 유지한다 —
    폭이 좁아졌다고 임의로 Column을 합치거나, 정렬 기준을 바꾸거나,
    테두리를 생략하지 않는다. Column/Row 각각의 구체적 폭·높이는
    [4](#4-grid-column--row-규칙)에 따라 축소된 Content Area 안에서도
    콘텐츠 분량 기준으로 다시 배분하되, Grid 정렬 축은 Full-width
    배치와 동일한 원칙을 따른다.
-   **Reference가 제공된 경우**, 위 판단보다 Reference의 실제 Table
    점유 비율(슬라이드/Content Area 대비 Table이 차지하는 폭·높이
    비율)과 배치 위치(중앙/좌/우, 다른 요소와의 상하좌우 관계)를
    우선 재현한다 — Reference 없이 새로 구성하는 경우에만 위 두
    판단 기준(핵심 Visual 여부)으로 크기를 정한다.

### Overall Region Map

아래 표는 **Table이 슬라이드의 핵심 Visual인 경우**(Body Box 전체 폭
사용)의 기본값이다. Chart/Image와 함께 축소 배치되는 경우, 이 표의
비율(Title/여백/Grid/Footnote 사이 비율 관계)은 유지하되 전체
기준값이 Body Box가 아니라 Table에 할당된 Content Area로 바뀐다.

본문은 Hard Rule §9/§12의 본문 Safe Area(**X 64~1216px**, Y·높이는
Main Title Supporting Message 사용 여부에 따라 둘 중 하나 — 미사용 시
§9 기준 **Y 135~656px, 1152×521px Body Box**(`.body-box`), 사용 시
§12 기준 **Y 178~656px, 1152×478px Body Box**(`.body-box.with-support`))를
100% 기준으로 아래 구조를 따른다. 아래 표의 %는 두 경우 모두 그대로
적용하고, 실제 px 환산 시에만 해당 슬라이드의 Y 시작점·높이를 사용한다.

| 영역 | X 범위 | Y 범위(Body Box 기준) | 비고 |
|---|---|---|---|
| Table Title(선택) | 0~100% | 0~8% | 표 제목/부제. Hard Rule §9 Main Title과는 별개의 보조 요소이며, 표가 다루는 비교 대상·기준을 한 줄로 명시할 때만 사용(예: `주요 스펙 비교`) |
| 여백 | - | Title 사용 시 8~13%, 미사용 시 0~5% | Title(또는 Body Box 상단)과 Grid 사이 여백 |
| Grid (Header Row + Body Row × N) | 0~100% | 여백 하단 ~ Grid 하단 | [4](#4-grid-column--row-규칙) 참조. Row별 높이는 콘텐츠 분량에 따라 조정(균등 고정 아님) |
| 여백 | - | Grid 하단 ~ +5% | Grid와 Footnote/Highlight Band 사이 여백(Band 미사용 시 생략) |
| Footnote / Highlight Band(선택) | 0~100% | 하단 ~8% | 표 전체에 대한 결론·강조 문구. Reference의 `Highlight / conclusion / footnote` 요소에 대응. Hard Rule 공통 Deck Footnote(페이지 하단 disclaimer)와는 별개이며 둘을 겸용하지 않는다 |

Grid가 차지하는 실제 세로 폭은 Row 수(N)와 Row당 높이에 따라
가변적이다 — Row가 많아지면 Title/Footnote Band를 줄이거나 생략해
Grid에 공간을 우선 배분한다([4](#4-grid-column--row-규칙) 참조).

------------------------------------------------------------------------

## 4. Grid Column / Row 규칙

### 비교축 선택 원칙

Table의 Row/Column 방향(어느 축에 비교 대상을, 어느 축에 비교 항목을
배치할지)은 특정 구조로 모든 Table에 고정하지 않는다. 아래 우선순위로
매번 판단한다.

1.  **Reference가 있는 경우**, Reference의 Row/Column 구조를 최우선
    적용한다 — 아래 2~3번 판단보다 우선한다.
2.  Reference가 없는 경우, 비교 대상과 비교 항목의 **수·내용량**을
    함께 보고 판단한다.
    -   **비교 대상이 소수(예: 기존 vs COSOLUS 2개)이고 비교 항목이
        여러 개인 경우**: 비교 대상을 **Row**, 비교 항목을
        **Column**으로 배치하는 것을 우선한다.
    -   **여러 기업/제품을 비교하는 경우**: 비교 대상을 **Column**으로
        배치할 수 있다.
3.  하나의 표 안에서는 하나의 축 구조만 사용한다 — 일부 대상은 Row,
    일부는 Column으로 섞지 않는다.

아래 [Column 구조](#column-구조), [Row 구조](#row-구조),
[6. Header Row](#6-header-row), [9. 자사 강조](#9-자사-강조)는
**비교 대상이 Column에 배치되는 경우**(여러 기업/제품 비교 등)를
기준으로 서술한다. 위 판단에 따라 **비교 대상이 Row에 배치되는
경우**에는 "Criteria Column"(비교 항목명 표시)이 "Criteria Header
Row"(비교 항목이 최상단 Row에 표기)로 역할이 바뀐다 — 이때 그리드의
**구조적 최상단 Row**(= Criteria Header Row)가 [6. Header Row](#6-header-row)의
Header Row Fill 규칙을 그대로 받는다. 대상 이름(예: 기존/COSOLUS)이
표시되는 맨 왼쪽 Column은 별도 Header Fill 없이 일반 Column과 동일하게
취급하며, 대상 강조는 [9. 자사 강조](#9-자사-강조)에 따라 텍스트로만
표현한다. 동일 역할 축끼리 폭/높이 통일, 콘텐츠 기반 크기 조정, 중앙
정렬, [5. Cell 구조](#5-cell-구조-공통-variant-ab-공통-적용) 등
나머지 원칙은 축이 바뀌어도 그대로 적용된다.

### Column 구조

-   1열은 **Criteria Column**(비교 기준/항목명)이며, 그 뒤로
    **Target Column**(비교 대상)이 2~4개 이어진다 — 전체 2~5 Column
    범위를 기본으로 한다.
-   **기존 방식 vs COSOLUS 2자 비교를 Column 축으로 배치하는 경우**
    ([비교축 선택 원칙](#비교축-선택-원칙)에 따라 Reference가 이
    구조를 지정하거나, 비교 항목 수가 적어 Column 배치가 더 적합하다고
    판단되는 경우): 기존/COSOLUS를 각각 하나의 Target Column으로
    구성한다. 색상 처리는 Claude PPT Design System §8 Table Style을
    따른다([9. 자사 강조](#9-자사-강조) 참조). 비교 항목이 여러 개인
    일반적인 2자 비교는 [비교축 선택 원칙](#비교축-선택-원칙)의
    기본값대로 대상을 Row로 배치하는 쪽을 우선 검토한다.
-   **Column 폭은 균등 고정이 아니라 콘텐츠 분량에 맞춰 조정하되,
    같은 역할의 Column끼리는 폭을 통일한다.** 서로 다른 역할의
    Column(Criteria Column vs Target Column)은 각자의 콘텐츠 분량에
    따라 폭이 달라질 수 있다 — Criteria Column의 항목명이 길면
    그만큼 넓게, Target Column들의 값이 짧은 수치·단어 위주면
    그만큼 좁게 배분한다. 반면 **같은 역할의 Column(예: 여러 Target
    Column)끼리는 서로 동일한 폭을 유지**한다 — 특정 Target Column
    하나만 콘텐츠가 짧다고 그 Column만 따로 좁히지 않는다(Reference
    실측값 — 5 Column 정확히 20%씩 균등 분할 — 은 Wireframe
    Placeholder의 예시일 뿐 고정 비율이 아니다, [2. Reference
    Reproduction Principle](#2-reference-reproduction-principle) 참조).
    Column끼리 폭 차이가 나더라도 전체 Grid의 가로 정렬 기준(각
    Column의 좌우 경계선이 모든 Row에서 동일한 X 위치를 유지하는
    것)은 그대로 지킨다 — Row마다 Column 경계가 어긋나지 않는다.
-   비교 대상이 5개를 초과해 Column이 좁아져 판독성이 떨어지면 Column
    수를 줄이거나(핵심 대상만 선별) [Comparison Matrix
    Layout](comparison-matrix.md) 등 다른 구조를 검토한다 — 폰트를
    과도하게 축소해 욱여넣지 않는다.

### Row 구조

-   최상단은 **Header Row** 1개, 그 아래 **Body Row**가 비교 기준
    수만큼 이어진다.
-   **Row 높이는 Column 폭과 동일한 원칙**으로 균등 고정이 아니라
    Row별 콘텐츠 분량(텍스트 줄 수, Variant B의 이미지/Diagram 포함
    여부 등)에 맞춰 조정한다 — 내용이 짧은 Row는 낮게, 긴 텍스트나
    Visual이 들어가는 Row는 그만큼 높게 확보한다(Reference 실측값 —
    5개 Row 정확히 20%씩 균등 분할 — 은 Wireframe Placeholder 예시일
    뿐 고정 비율이 아니다). Header Row와 Body Row의 구분은 원칙적으로
    높이 차이가 아니라 [6. Header Row](#6-header-row)의 색상·
    Typography Weight로 표현하되, Row 자체의 콘텐츠 분량 차이로 높이가
    달라지는 것은 허용한다 — 다만 위계를 표현하려는 목적만으로 임의
    확대하지 않는다([12. Avoid](#12-avoid) 참조).
-   Row마다 높이가 달라져도 모든 Column의 상하 경계선은 각 Row에서
    동일한 Y 위치를 유지한다 — Grid 전체의 세로 정렬 기준은 Row 높이
    차이와 무관하게 깨지지 않는다.
-   Body Row 수(N)는 비교 기준 개수만큼 자유롭게 늘어난다. Row가
    많아질수록 [3](#3-overall-structure)의 Title/Footnote Band를
    줄이거나 생략해 Grid 영역을 우선 확보한다.

------------------------------------------------------------------------

## 5. Cell 구조 (공통, Variant A/B 공통 적용)

Cell의 직각형 Grid 구조, Table Grid(Cell 구분선) 두께·색상, Padding은
**Hard Rule §10B Table Header Row**를 따르며 이 문서에서 재정의하지
않는다. 이 문서가 정의하는 것은 아래와 같은 이 Layout 고유의 배치
예외뿐이다.

-   Cell 내부 텍스트는 **수평·수직 모두 중앙 정렬**을 기본으로 한다
    (Reference 실측 원칙). 다만 Variant B의 설명 캡션처럼 문장형
    텍스트가 2줄 이상으로 길어지는 경우, 블록 자체는 Cell 중앙에
    두되 내부 줄 정렬만 좌측 정렬을 허용한다(다른 Layout Reference의
    Supporting Text 규칙과 동일한 예외).

------------------------------------------------------------------------

## 6. Header Row

> 아래는 그리드의 **구조적 최상단 Row**를 기준으로 한 서술이다.
> [비교축 선택 원칙](#비교축-선택-원칙)에 따라 비교 대상이 Row에
> 배치되는 경우, 이 최상단 Row에는 대상 이름 대신 비교 항목명이
> 표시된다(= Criteria Header Row). 어느 경우든 최상단 Row가 아래
> Header Row 스타일을 받으며, 대상 이름이 맨 왼쪽 Column에 표시되는
> 경우 그 Column은 별도 Header 스타일 없이 일반 Column과 동일하게
> 취급한다 — 대상(COSOLUS 등) 강조는 [9. 자사 강조](#9-자사-강조)에
> 따라 텍스트로만 표현한다.

-   Header Row에는 각 Column이 의미하는 항목/대상 이름을 표시한다.
    1열 Header는 `구분`, `비교 기준`, `항목` 등으로 표기한다.
-   Header Row의 색상·Typography·정렬은 **Hard Rule §10B Table Header
    Row**를 그대로 따르며 이 문서에서 재정의하지 않는다(비교 대상
    개수와 무관하게 Header Row 전체를 동일 스타일로 통일하고,
    Column/대상 단위로 나눠 일부만 다르게 처리하지 않는다).
-   **Reference가 있는 경우**, 위 기본값보다 Reference가 실제로 사용한
    Header 강조 방식을 우선 적용한다(§10B Reference 예외 조항 참조).
-   콘텐츠 분량에 따라 Row 높이 자체가 달라지는 것은
    [4. Row 구조](#4-grid-column--row-규칙)를 따른 것이며 위 색상
    통일 규칙과는 별개다.
-   본 Layout은 "10. Content Region Header"(2~3개 병렬 Content
    Region이 각자 갖는 독립 Header Bar)가 아니라 **Hard Rule §10B
    Table Header Row**를 따른다 — N개 Column(가변)으로 구성되는
    Table Header는 §10과 적용 범위가 다르다.
-   Header Row 텍스트는 Column 폭 안에서 중앙 정렬하며, 2줄을
    넘기지 않는다.

------------------------------------------------------------------------

## 7. Variant A — Data Comparison Table

텍스트·수치 중심의 비교표. Reference(`L17`)의 `ITEM`/`DATA` Cell
구성과 가장 가까운 기본형이다.

-   Criteria Column Cell: 비교 기준명(짧은 명사구, 1줄 권장)
-   Target Column Cell: 아래 중 콘텐츠에 맞는 구성을 사용
    -   단일 수치/값 텍스트(가장 단순한 형태)
    -   짧은 보조 Label + 값(2줄 구성, 예: `TRL` 위 · `7` 아래)
-   정량 데이터가 없는 항목에 임의의 수치를 만들어 채우지 않는다 —
    데이터가 없으면 `-` 또는 정성적 짧은 텍스트로 표기한다.
-   같은 Row(동일 비교 기준) 안에서는 모든 Target Column이 동일한
    데이터 형식(수치 vs 텍스트)을 유지해야 가로 비교가 즉시
    가능하다 — 한 Row 안에서 한쪽은 수치, 다른 쪽은 긴 문장으로
    섞어 쓰지 않는다.

------------------------------------------------------------------------

## 8. Variant B — Visual Comparison Table

이미지/Diagram과 설명·수치를 Cell 내부에서 함께 비교하는 표.

-   Table 기본 구조·디자인 규칙은 Variant A([7](#7-variant-a--data-comparison-table))를
    그대로 사용한다 — Variant B를 위한 별도 Grid/Layout을 새로 만들지
    않는다.
-   Body Cell에는 Image/Diagram + Text/Number를 함께 배치할 수 있다.
-   이미지/Diagram이 들어가는 Row는 콘텐츠에 맞게 Row Height를
    조정한다([4](#4-grid-column--row-규칙) Row 구조 원칙과 동일).
-   여러 기업/제품을 비교하는 경우 비교 대상은 Column(가로축)에
    배치한다.
-   Column Header는 Main Color Fill + White Bold Text로
    통일한다([6](#6-header-row) 기본값과 동일).
-   COSOLUS를 포함한 모든 비교 대상 Header는 동일한 Header Style을
    사용한다 — COSOLUS만 별도 Header 스타일을 두지 않는다.
-   Body에서 COSOLUS 데이터 강조가 필요하면 Main Color Text +
    Bold로 표현한다([9](#9-자사-강조) 원칙과 동일).
-   여러 기업을 비교하는 경우 COSOLUS는 Criteria Column(구분) 바로
    다음 Column에 우선 배치한다.
-   모든 기업 Header는 COSOLUS를 포함해 예외 없이 Main Color Fill +
    White Bold Text를 동일하게 유지한다.
-   COSOLUS Column 전체(Header ~ 마지막 Row)는 진한 Main Color
    Border로 하나의 영역처럼 감싸 강조한다.
-   이 Border는 좌·우 세로선뿐 아니라 상·하단까지 포함한 전체 외곽
    Border로 적용한다.
-   COSOLUS Column 내부의 Cell Border/구조는 기존 Table 규칙([5](#5-cell-구조-공통-variant-ab-공통-적용))을
    그대로 유지한다.
-   COSOLUS 전체를 별도 Background Fill로 강조하지 않는다 — 강조는
    외곽 Border만으로 표현한다.

------------------------------------------------------------------------

## 9. 자사 강조

이 문서(일반 Table)의 자사 강조는 **Hard Rule §10B Table Header Row**의
강조 기본값(Body Fill 아닌 Main Color Text + Bold, 최대 1개
Column/Row)을 그대로 따르며 이 문서에서 재정의하지 않는다.
[비교축 선택 원칙](#비교축-선택-원칙)에 따라 COSOLUS가 Row에 배치되든
Column에 배치되든 이 원칙은 동일하게 적용된다. **Reference가 있는
경우**, 위 기본 강조 방식보다 Reference가 실제로 사용한 강조 방식을
우선 적용한다(§10B Reference 예외 조항 참조). 이 문서는 자사 Column
전체를 Solid Fill로 강조하는 것과 같은 별도의 Layout-specific Emphasis
Variant를 정의하지 않는다 — 그러한 강조가 필요한 경우(예: 경쟁사 비교
우위를 시각적으로 강하게 대비시켜야 하는 콘텐츠)는
`019_competitive-advantage-highlight.md`처럼 Hard Rule §10B가 허용하는
Layout-specific Emphasis 예외를 그 Layout MD에서 별도로 정의한다.

------------------------------------------------------------------------

## 10. Typography

Header Row Label/Criteria Column Label, Body/Data Cell, Cell 설명 캡션,
Footnote의 Font Size/Weight는 **Hard Rule §10B Table Header Row**를
그대로 따르며 이 문서에서 재정의하지 않는다. 아래는 §10B가 다루지 않는
이 Layout 고유 요소(Main Title, Table Title)만 정리한 것이다.

| 역할 | Font Size | Weight |
|---|---|---|
| Main Title | 28pt | ExtraBold (Hard Rule §9, 참조만) |
| Table Title(선택, 표 제목/부제) | 20pt | SemiBold |

------------------------------------------------------------------------

## 11. Flexibility

### Must Preserve

-   직각형 Grid 구조(Rounded/Card/Shadow 금지)
-   Header Row + Body Row의 명확한 행·열 구조
-   모든 Row/Column에서 동일하게 유지되는 Grid 정렬 축(Column 경계
    X 위치, Row 경계 Y 위치) — 개별 Column 폭·Row 높이 값 자체는
    콘텐츠 분량에 따라 달라질 수 있음
-   얇은 직선 Cell 구분, 최소한의 Fill/장식
-   Cell 내부 중앙 정렬 기본 원칙
-   같은 Row 안 데이터 형식 통일(Variant A), 표 전체 Variant A/B 통일

### May Adapt

-   Column 수(2~5 범위), Row 수(콘텐츠의 비교 기준 개수에 따라 가변)
-   Column 폭 / Row 높이 — 콘텐츠 분량(텍스트 길이·Visual 크기 등)에
    맞춰 조정(다만 Grid 정렬 축은 유지, [4](#4-grid-column--row-규칙)
    참조)
-   Table Title / Footnote·Highlight Band 사용 여부
-   Variant A/B 선택 — 콘텐츠에 이미지/Diagram 자산이 있으면 B, 텍스트·
    수치 중심이면 A
-   Header Row 스타일 — 기본값은 Main Color Fill + White Bold Text로
    통일하되, Reference에 명확히 다른 Table Header Style이 있는
    경우에는 Reference를 우선 적용한다([6. Header Row](#6-header-row)
    참조)
-   자사 강조 대상(Column 또는 Row 중 콘텐츠에 맞는 쪽 선택)

------------------------------------------------------------------------

## 12. Avoid

-   Rounded Corner, Card 그림자, Cell 간 간격을 띄운 카드형 표 재해석
-   콘텐츠 분량과 무관하게 Header Row를 Body Row보다 임의로 두껍게/
    얇게 만들어 높이만으로 위계를 표현
-   콘텐츠 분량과 무관하게 특정 Column/Row만 임의로 넓히거나 좁혀
    강조 효과를 내기(Column/Row 폭·높이 조정은 반드시 실제 콘텐츠
    분량에 근거해야 한다, [4. Grid Column / Row 규칙](#4-grid-column--row-규칙)
    참조)
-   같은 Row 안에서 Column마다 데이터 형식(수치/텍스트)을 다르게 섞기
-   정량 데이터가 없는데 임의 수치·이미지를 새로 만들어 채우기
-   2개 이상 Column/Row를 동시에 자사 강조로 처리
-   Hard Rule §10 Content Region Header(2~3개 병렬 Content Region용
    Header Bar)를 이 Layout의 Header Row에 그대로 적용
-   Comparison Matrix Layout(`comparison-matrix.md`)의 자유 배치형
    Cell 규칙을 가져와 섞어 쓰기
-   Hard Rule 또는 Claude PPT Design System 변경

------------------------------------------------------------------------

## 13. Rule Priority

1.  Hard Rule
2.  Slide-specific Design Rule (본 문서 — Grid/Cell 서술 규칙)
3.  Layout Catalog / Selected Layout Reference (`L17. Table / Matrix`
    실측 구조·비율, [2](#2-reference-reproduction-principle) 기준)
4.  Visual Style(Claude PPT Design System) — 색상·Typography·장식
    처리
5.  Content Visualization Freedom — Variant B의 Cell 내부 이미지
    구성 등 Reference에 실측 사례가 없는 부분

본 Layout Reference는 Hard Rule 및 Design System을 변경하거나 대체하지
않는다.

## 14. Selection Rule

다음 조건을 만족할 때 우선 고려한다.

1.  비교 대상이 3개 이상이거나, 비교 기준(Row)이 여러 개라 표 형태의
    밀도 있는 정리가 필요함
2.  대상별로 서로 다른 자유 시각 구성이 아니라, 동일한 행·열 격자
    안에서 정확히 대응되는 비교가 필요함(→ 아니라면
    `comparison-matrix.md` 검토)
3.  Before/After식 변화·전환이 아니라 다수 대상의 정적 스펙/데이터
    비교가 핵심임(→ 아니라면 `before-after.md` 검토)
