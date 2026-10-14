# Table Comparison Layout Reference

> 2026-10-14 통합: 기존 Variant A(Data)/B(Visual)를 하나의 기본 표로 합치고,
> 기존 Comparison Matrix(`comparison-matrix.md`)를 이 문서의 **Visual
> Evidence 구성**으로 흡수했다. 표 계열 비교는 이 Layout 하나에서
> **구성**(기본 / Visual Evidence)과 **강조**(없음 / Text / Outline /
> Solid Card)만 골라 조합한다 — 이미지 유무나 강조 방식 차이로 별도
> Layout을 만들지 않는다.

## 1. Purpose

여러 대상(자사/경쟁사, 기술 방식 A/B/C, 제품 등)을 **공통 비교축(Row
또는 Column)** 으로 행·열이 구획된 표에 정리해 가로로 즉시 비교하게 하는
레이아웃이다.

### Use When

-   모든 비교 대상이 **같은 비교 기준**을 공유하고, 대상 3개 이상이거나
    대상 2개라도 비교 기준이 여러 개인 경우
-   Cell 콘텐츠가 텍스트·수치·등급·보조 이미지 등 무엇이든, 기준별로
    대상을 나란히 읽는 것이 핵심인 경우
-   사진·실험결과처럼 대상별 Visual Evidence를 같은 기준으로 나란히
    보여줘야 하는 경우(→ [7. 구성](#7-구성--기본--visual-evidence)의
    Visual Evidence 구성)

### Do Not Use When

-   비교 대상이 Existing/Improved 2개이고 변화·전환 자체가 핵심인 경우 →
    Before/After Layout(`before-after.md`)
-   하나의 기술을 정량 성능과 작동 원리 두 관점으로 함께 설명하는 경우 →
    Left-Right Tech Comparison(`014_left-right-tech-comparison.md`)
-   동일한 5~8개 평가축의 종합 Profile(강점/약점 Pattern)이 핵심인 경우 →
    Multi-Radar(`013_multi-radar-technology-comparison.md`)
-   하나의 솔루션이 만드는 정확히 2개의 병렬 효과를 보여주는 경우 →
    Benefit + Impact Layout(`benefit-impact.md`)
-   대상마다 항목 구성(종류·개수)이 달라 공통 비교축이 없는 경우 →
    Column/Card 계열(정량 항목이 많다는 이유만으로 표를 선택하지 않는다)

------------------------------------------------------------------------

## 2. Reference Reproduction Principle

이 Layout Reference는 통합 Layout Catalog PPT
(`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`, **17번
슬라이드 — Layout Catalog `L17. Table / Matrix`**)의 구조를 근거로 한다.
해당 슬라이드는 범용 Table Wireframe 템플릿이므로 다음만 재현한다.

1.  Column/Row가 **완전히 맞닿은 직각형 Grid**로 구성되고 카드형으로
    분리·이격되지 않는다는 점
2.  모든 Row에서 Column 경계 X 위치, 모든 Column에서 Row 경계 Y 위치가
    같은 하나의 정렬된 Grid 축 — 구체적 폭·높이는 [4](#4-grid-column--row-규칙)에
    따라 콘텐츠 분량 기준으로 정한다
3.  Table Title → 여백 → Grid → 여백 → (선택) Highlight/Footnote Band의
    세로 정보 흐름
4.  Cell 내부 텍스트의 수평·수직 중앙 정렬

Wireframe의 Cell Fill·Border 색, Placeholder 텍스트·폰트, 5열×5행 구성은
재현하지 않는다 — 색·선·Typography는 Hard Rule §10B를 따른다.

------------------------------------------------------------------------

## 3. Overall Structure

### Table 배치 원칙

-   **[우선조건] 다른 Slide Layout의 Content Area 내부에서 Table을
    부분 요소로 쓰는 경우**: 위치·크기는 해당 Slide Layout의 배치 규칙을
    우선하고, 이 문서는 행·열 구조와 디자인([4](#4-grid-column--row-규칙)~[9](#9-typography))만
    적용한다.
-   **Table이 슬라이드의 핵심 Visual인 경우**: 아래 Region Map대로 Body
    Box(폭 1152px 기준) 전체 폭을 사용한다.
-   **Chart/Image 등 다른 핵심 Visual과 함께 배치되는 경우**: 자신의
    Content Area 안에서만 축소 배치하며 다른 Visual 영역을 침범하지
    않는다. 축소해도 Header Row/Body Row 구분, Grid 정렬 축, Hard Rule
    §10B 디자인은 그대로 유지한다.
-   **Reference가 제공된 경우**, 위 판단보다 Reference의 Table 점유
    비율과 배치 위치를 우선 재현한다.

### Overall Region Map

본문 Safe Area(Hard Rule §9/§12의 `.body-box` 또는 `.body-box.with-support`)를
100% 기준으로 한다.

| 영역 | X 범위 | Y 범위(Body Box 기준) | 비고 |
|---|---|---|---|
| 그룹 Label(선택) | 강조 Group 폭 | Grid 바로 위 | Outline 강조의 그룹 Label을 쓸 때만([8](#8-강조-옵션)) |
| Table Title(선택) | 0~100% | 0~8% | 비교 대상·기준을 한 줄로 명시할 때만. Main Title과 별개 |
| 여백 | - | Title 사용 시 8~13%, 미사용 시 0~5% | |
| Grid (Header Row + Body Row × N) | 0~100% | 여백 하단 ~ Grid 하단 | [4](#4-grid-column--row-규칙). **이미지 Cell도 Grid 안의 일반 Cell이다** — 이미지용 별도 슬롯·영역을 Grid 밖에 만들지 않고, 이미지가 든 Row의 높이만 늘린다 |
| 여백 | - | Grid 하단 ~ +5% | Band 미사용 시 생략 |
| Footnote / Highlight Band(선택) | 0~100% | 하단 ~8% | 표 전체의 결론·출처. Deck Footnote(§9)와 겸용하지 않는다 |

Row가 많아지면 Title/Footnote Band를 줄이거나 생략해 Grid에 공간을
우선 배분한다.

------------------------------------------------------------------------

## 4. Grid Column / Row 규칙

### 비교축 선택 원칙

1.  **Reference가 있는 경우**, Reference의 Row/Column 구조를 최우선한다.
2.  Reference가 없으면 비교 대상과 비교 항목의 수·내용량을 보고 판단한다.
    -   비교 대상이 소수(예: 기존 vs COSOLUS 2개)이고 항목이 여러 개 →
        대상을 **Row**, 항목을 **Column**으로 우선 배치
    -   여러 기업/제품/방식 비교 → 대상을 **Column**으로 배치
    -   **Outline 강조(Column Group 포함)·Solid Card 강조·Visual Evidence
        구성은 대상이 Column일 때만 쓴다.**
3.  하나의 표 안에서는 하나의 축 구조만 사용한다.

대상이 Row에 배치되면 그리드의 구조적 최상단 Row(비교 항목명)가 Header
Row 스타일을 받고, 대상 이름이 놓이는 맨 왼쪽 Column은 일반 Criteria
Column으로 취급한다.

### Column 구조

-   1열은 **Criteria Column**(비교 기준/항목명), 그 뒤로 **Target
    Column**(비교 대상)이 2~4개 — 전체 2~5 Column 범위를 기본으로 한다.
-   Column 폭은 콘텐츠 분량에 맞추되 **같은 역할의 Column끼리는 같은
    폭**으로 통일한다(`colgroup` + `table-layout: fixed`, SKILL.md "Table
    동일 폭 Column").
-   대상이 5개를 넘어 판독성이 떨어지면 핵심 대상만 선별한다 — 폰트를
    줄여 욱여넣지 않는다.

### Row 구조

-   최상단 **Header Row** 1개, 그 아래 **Body Row**가 비교 기준 수만큼.
-   Row 높이는 Row별 콘텐츠 분량(줄 수, 이미지 포함 여부)에 맞춘다. 위계
    표현만을 위해 Header Row를 임의로 두껍게/얇게 하지 않는다.
-   Row 높이가 달라도 모든 Column의 경계선 Y 위치는 각 Row에서 같다.

------------------------------------------------------------------------

## 5. Cell 구성 (기존 Variant A/B 통합)

-   Header·Body Cell의 배경·Grid·Typography는 **Hard Rule §10B**를 따르며
    이 문서에서 재정의하지 않는다.
-   Target Cell은 콘텐츠에 맞게 아래를 자유롭게 쓴다 — 한 표 안에서
    섞어도 되며, 이 차이로 Variant를 나누지 않는다.
    -   단일 수치/값 텍스트
    -   짧은 보조 Label + 값(2줄, 예: `TRL 9` / `상용화 단계`)
    -   짧은 문장형 텍스트(1~3개 핵심 메시지)
    -   **보조 이미지/Diagram + 캡션** — Cell 내부에 함께 배치하고 그
        Row의 높이만 늘린다
-   **같은 Row 안에서는 모든 Target Cell이 같은 데이터 형식**(수치 vs
    텍스트 vs 이미지+캡션)을 유지한다.
-   Cell 내부는 수평·수직 중앙 정렬. 2줄 이상 문장형 캡션은 블록만 중앙에
    두고 줄 정렬은 좌측을 허용한다.
-   데이터가 없는 항목에 임의 수치·이미지를 만들어 채우지 않는다 — `-`
    또는 짧은 정성 텍스트로 표기한다.

------------------------------------------------------------------------

## 6. Header Row

-   Header Row에는 각 Column이 의미하는 대상/항목 이름을 표시한다. 1열
    Header는 `구분`, `비교 기준`, `항목` 등으로 표기한다.
-   색상·Typography·정렬은 **Hard Rule §10B**를 그대로 따른다(Header Row
    전체 동일 스타일).
-   Header 텍스트는 2줄을 넘기지 않는다.
-   이 Header는 "10. Content Region Header"가 아니다 — §10 Header Bar를
    적용하지 않는다.

------------------------------------------------------------------------

## 7. 구성 — 기본 / Visual Evidence

슬라이드마다 둘 중 하나를 고른다(`slide_outline.md`의 Layout Options
`구성`). 두 구성은 같은 Grid·Header·Typography를 쓰며 아래 차이만 있다.

**판단 질문: "이 Row의 이미지를 빼면 슬라이드의 주장이 성립하지
않는가?"** — 그렇다면 Visual Evidence, 아니면 기본(이미지가 있어도
기본).

### 기본 구성 (`standard`)

[5. Cell 구성](#5-cell-구성-기존-variant-ab-통합) 그대로. 이미지는 텍스트
판독을 돕는 보조 자료이며 Cell 안에 작게 둔다.

### Visual Evidence 구성 (`visual-evidence`, 구 Comparison Matrix)

사진·실험결과·그래프·Diagram 같은 면적 점유형 Visual Evidence가 핵심
주장을 직접 증명하는 Required Evidence일 때만 쓴다.

-   **Cell 귀속**: Visual Evidence는 그것이 증명하는 대상(Column) × 기준
    (Row) Cell **안에** 둔다. 여러 대상의 Visual을 표 밖의 공통 영역으로
    합치거나, 귀속 Cell과 분리해 표 옆·아래에 두지 않는다. 하나의 Visual이
    여러 Cell을 실제로 공동 증명하는 경우에만 예외로 하며 그 대응 범위를
    표시한다.
-   **배치**: Visual Evidence Row를 Header Row 바로 아래에 우선 배치한다.
-   **크기**: 모든 Target이 **같은 크기의 Image Frame**을 쓰고, 원본 비율을
    유지한 채 Crop/Contain으로 체감 크기를 맞춘다. Visual은 그 Row 높이의
    대부분을 차지하도록 크게 두되 원본 해상도 이상으로 확대하지 않는다.
-   **필수 검사**: Visual Evidence Row의 모든 Target Cell에 Visual이 있어야
    한다. 데이터가 없는 대상은 `-`로 두고 그 사실을 Structural Check에
    남긴다 — 다른 이미지로 채우지 않는다.
-   이미지에 결과 라벨이 이미 들어 있으면 같은 내용의 캡션을 중복해
    붙이지 않는다.
-   Before→After를 한 Cell에서 보여주면 모든 대상 Cell에 같은 Frame과 같은
    형태의 방향 화살표를 쓴다.
-   Visual Evidence가 없는 Row(텍스트·수치)는 기본 구성의 Cell 규칙을
    따른다.

------------------------------------------------------------------------

## 8. 강조 옵션

강조 방식의 시각 스펙(색·두께·배치)은 **Hard Rule §10B**에서 정의하며
여기서는 선택 기준만 정한다. **한 표에 하나의 방식만** 쓰고, 강조 대상이
분명하지 않으면 쓰지 않는다(`none`).

| 옵션 | 쓰는 경우 | 대상 범위 | 구성 |
|---|---|---|---|
| `none` | 강조할 자사/핵심 대상이 없음(예: 순수 기술 동향) | - | 기본·Visual Evidence |
| `text` | 가벼운 강조로 충분함 | 1개 Column 또는 1개 Row | 기본·Visual Evidence |
| `outline` | 자사/핵심 대상을 박스로 분명히 묶어야 함 — 특히 **연속된 여러 Column을 하나의 그룹**으로 묶거나, Visual Evidence 구성이거나, Header가 회사명이 아닌 경우 | 1개 Column 또는 연속 Column Group 1개 | 기본·Visual Evidence |
| `solid-card` | 경쟁사 대비 자사 우위를 강하게 대비시키는 경쟁사 비교표(대상 3~4개) | 자사 1개 Column | 기본만 |

-   **그룹 Label**(`outline` 전용): Group이 2개 Column 이상이거나 Header가
    회사명이 아닐 때만 그룹 위에 소유자(예: `COSOLUS`)를 표기한다.
-   **Solid Card**는 [`019_competitive-advantage-highlight.md`](019_competitive-advantage-highlight.md)가
    정의하는 별도 강조 유형이다 — Outline으로 대체하거나 Outline과
    섞지 않는다.
-   **금지 조합**: `solid-card` + Visual Evidence 구성 / `solid-card` 여러
    Column / `outline`으로 떨어진 Column 묶기 / 한 표에 강조 2종 이상 또는
    그룹 2개 이상 / 대상이 Row 축인데 `outline`·`solid-card` 사용.

### Layout Options 기록·전달 값

`slide-structuring`은 `slide_outline.md`의 **Layout Options**에 아래 값을
기록하고, `web-ppt-generator`는 같은 값을 `<table>`의 data 속성으로
옮긴다(값이 다르면 Layout Compliance 위반).

| 항목 | outline 값 | HTML 속성 |
|---|---|---|
| 구성 | `standard` / `visual-evidence` | `data-table-mode` |
| 강조 | `none` / `text` / `outline` / `solid-card` | `data-emphasis` |
| 강조 대상 | Column 번호(1부터, Criteria 포함) — 단일 `3`, Group `3-4` | `data-emphasis-cols` |
| 그룹 Label | 텍스트(없으면 생략) | `data-emphasis-label` |

------------------------------------------------------------------------

## 9. Typography

Header Row Label, Criteria Column Label, Body/Data Cell, Cell 캡션,
Footnote는 **Hard Rule §10B**를 따른다. 이 Layout 고유 요소만 아래와 같다.

| 역할 | Font Size | Weight |
|---|---|---|
| Main Title | 28pt | ExtraBold (Hard Rule §9, 참조만) |
| Table Title(선택) | 20pt | SemiBold |

------------------------------------------------------------------------

## 10. Flexibility

### Must Preserve

-   직각형 Grid, 모든 행·열 사이 Grid와 Header 틴팅(Hard Rule §10B)
-   Header Row + Body Row의 명확한 행·열 구조와 공통 Grid 정렬 축
-   Cell 내부 중앙 정렬, 같은 Row 안 데이터 형식 통일
-   Visual Evidence 구성의 Cell 귀속·동일 Frame

### May Adapt

-   Column 수(2~5), Row 수, Column 폭·Row 높이(콘텐츠 분량 기준)
-   Table Title / Footnote·Highlight Band 사용 여부
-   구성(기본 / Visual Evidence), 강조 옵션과 대상

------------------------------------------------------------------------

## 11. Avoid

-   Rounded Corner, Card 그림자, Cell 간 간격을 띄운 카드형 표(019 Solid
    Card 상단 모서리 제외)
-   표마다 Grid 일부 생략·행 교차 틴팅·열 틴팅 등 §10B와 다른 Grid/틴팅
-   콘텐츠 분량과 무관하게 특정 Column/Row만 넓히거나 좁혀 강조 효과 내기
-   같은 Row 안에서 Column마다 데이터 형식 섞기
-   데이터가 없는데 임의 수치·이미지 만들어 채우기
-   이미지를 Grid 밖 별도 영역으로 빼서 배치하기
-   [8](#8-강조-옵션)의 금지 조합
-   Hard Rule §10 Content Region Header를 이 Layout의 Header Row에 적용
-   Hard Rule 또는 Claude PPT Design System 변경

------------------------------------------------------------------------

## 12. Rule Priority

1.  Hard Rule(§10B 포함)
2.  본 문서(구조·구성·강조 선택)
3.  Layout Catalog `L17. Table / Matrix`(구조 근거, [2](#2-reference-reproduction-principle))
4.  Claude PPT Design System
5.  Content Visualization Freedom — Cell 내부 표현 방식 선택

## 13. Selection Rule

1.  **Layout**: [Do Not Use When](#do-not-use-when)의 전용 Layout(Before/After,
    Left-Right, Multi-Radar, Benefit+Impact)에 해당하지 않고, 모든 대상이
    공통 비교축을 공유하면 Table Comparison을 쓴다.
2.  **구성**: "이 Row의 이미지를 빼면 주장이 성립하지 않는가?" → 그렇다면
    `visual-evidence`, 아니면 `standard`.
3.  **강조**: [8. 강조 옵션](#8-강조-옵션) 표로 고른다.
