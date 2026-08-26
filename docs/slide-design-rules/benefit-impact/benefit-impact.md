# Benefit + Impact Layout Reference

## 1. Purpose

하나의 기술·솔루션·제품이 만들어내는 **좌/우 2개의 핵심 개선 효과와 그
비즈니스/공정 Impact**를 한 장에서 병렬적으로 설명할 때 사용하는
레이아웃이다.

단순 장점 나열이 아니라
`Core Technology / Solution → Improvement → Quantified Impact`의 논리
흐름이 보여야 한다. Core Technology/Solution 자체는 Hard Rule §9
공통 Header System의 Main Title에서 이미 전달되므로, 본 Layout의
본문(Header 이하)은 그 기술이 만드는 2개의 Benefit을 증명하는 데
집중한다.

### Use When

-   기술 적용으로 CAPEX/OPEX, 공정시간, 수율, 사용량 등이 개선되는
    효과가 **정확히 2개**인 경우
-   하나의 솔루션이 2개의 정량적 효과를 만드는 경우
-   성능 개선과 경제적 효과를 함께 제시하는 경우
-   그래프, 표, Diagram 등 서로 다른 Evidence로 동일 솔루션의 2개
    효과를 증명하는 경우

### Do Not Use When

-   핵심 효과(Benefit)가 1개뿐이거나 3개 이상인 경우 → 3개 이상은
    Three-Column Layout(`three-column.md`) 또는 Comparison Matrix
    Layout(`comparison-matrix.md`)을 우선 검토
-   여러 경쟁 대상을 동일 기준으로 비교하는 경우 → Comparison Matrix
    Layout(`comparison-matrix.md`)
-   단계별 공정 흐름 자체가 핵심인 경우
-   Before/After 공정 단계 변화 자체가 핵심인 경우 →
    Before/After Layout(`before-after.md`)

------------------------------------------------------------------------

## 2. Reference Reproduction Principle

이 Layout Reference에는 실제 Reference PPT(`benefit-impact.pptx`,
추출제 CAPEX/OPEX 개선 사례)가 함께 등록되어 있다. 이 문서의 수치·비율은
해당 Reference의 실측 좌표를 근거로 도출한 참고값이며, Reference가
제공된 경우 다음 우선순위를 지킨다.

1.  Reference의 공간 분할(좌:우 폭 비율 — 실측 약 **54:46**) — 일반적인
    50:50 Grid, Card Grid 같은 통상적 Web/AI UI 관습보다 우선
2.  Reference의 Evidence Visual 점유율(Benefit Area 본문 높이의 약
    **60~70%**) — "여백을 넉넉히 준다"는 일반 디자인 관습보다 우선
3.  Reference의 정보 밀도 — Benefit Message, Evidence Visual, Supporting
    Text, Footnote가 촘촘히 이어지는 중~높은 밀도 구성이며, Dashboard형
    여백 중심 구성보다 우선
4.  Reference의 정렬 패턴 — 좌우 Benefit Message의 Y 시작선 정렬,
    Evidence Visual 시작선 정렬
5.  콘텐츠(텍스트/수치/이미지)만 새 프로젝트 내용으로 치환한다 —
    Reference의 특정 수치·문구·이미지 자체는 복제하지 않는다
    ([13. Avoid](#13-avoid) 참조)
6.  Evidence Visual의 구체적 형식(Chart/Table 등)도 Reference PPT가
    실제로 사용한 형식에 고정되지 않는다 — 입력 콘텐츠의 특성과 전달
    목적을 분석해 [7. Evidence Visual](#7-evidence-visual) 중 가장
    적합한 형식을 매번 새로 선택한다. 유지되는 것은 형식이 아니라
    위 1~4번의 공간 분할·점유율·밀도·정렬 구조다.

## 3. Overall Structure

본문은 Hard Rule §9/§12의 본문 Safe Area(**X 64~1216px**, Y·높이는 Main
Title Supporting Message 사용 여부에 따라 둘 중 하나 — 미사용 시 §9 기준
**Y 135~656px, 1152×521px Body Box**(`.body-box`), 사용 시 §12 기준
**Y 178~656px, 1152×478px Body Box**(`.body-box.with-support`))를 100%
기준으로 아래 구조를 따른다. 실제 좌표는 `64 + (X% × 11.52)`,
`(135 또는 178) + (Y% × (5.21 또는 4.78))`로 환산한다(해당 슬라이드가
어느 Body Box를 쓰는지에 맞춰 괄호 안 값 중 하나를 선택).

1.  **Benefit Area Header** (통합 1개 또는 좌/우 분할 2개 — 콘텐츠
    구조에 따라 판단, Hard Rule §10 적용 — [4](#4-benefit-area-header-hard-rule-10-적용) 참조)
2.  **좌/우 2개의 Benefit Area** (Header 아래 본문 분할, Hard Rule §11
    Vertical Divider로 구분 — [5](#5-vertical-divider-hard-rule-11-적용) 참조).
    **두 Benefit Area 사이의 시각적 구분은 오직 (1)Header Bar와
    (2)Vertical Divider 두 가지로만 표현한다.** 각 Benefit Area 전체를
    감싸는 배경색 Box(Tint Fill), Border, Rounded Corner 같은 별도의
    "카드형" 컨테이너를 추가로 씌우지 않는다 — Header Bar와 Divider만으로
    이미 두 영역이 충분히 구분되므로 그 위에 카드 껍데기를 덧대는 것은
    중복 구현이며 [13. Avoid](#13-avoid)가 명시적으로 금지하는 패턴이다.
3.  각 Benefit Area 내부: **Benefit Message → Evidence Visual →
    (필요 시) Supporting Text** ([6](#6-benefit-area-내부-구조) 참조)

### Overall Region Map

Header를 통합 1개로 쓸지 좌/우 분할 2개로 쓸지는
[4](#4-benefit-area-header-hard-rule-10-적용)의 판단 기준에 따라
결정한다. 아래 표는 **분할 Header** 기준이며, **통합 Header**를
사용하는 경우 좌/우 Header 두 행이 "Benefit Area Header (통합)" 한
행(X: 0~100%, Y: 0~11%, 본문 전체 폭)으로 대체된다. 그 외 행(Benefit
Area Body, Vertical Divider)은 두 경우 모두 동일하다.

| 영역 | X 범위 (Body Box 기준) | Y 범위 (Body Box 기준) | 비고 |
|---|---|---|---|
| Benefit Area Header (좌, 분할 시) | 0 ~ (D-G/2)% | 0 ~ 11% | Hard Rule §10 고정 Height(0.561in≈54px) 적용. 우측 Header와 완전히 분리된 독립 Bar — 바깥쪽(X=0%) 경계는 좌측 Benefit Area와 동일, 안쪽 경계만 Header Gap(G)의 절반만큼 D%에서 물러남 |
| Header Gap | (D-G/2) ~ (D+G/2)% | 0 ~ 11% | 좌/우 Header Bar를 시각적으로 분리하는 여백. 이 구간에는 어떤 요소도 채우지 않는다(Fill 없음) — 두 Header가 맞닿아 하나로 보이는 것을 방지하는 것이 목적 |
| Benefit Area Header (우, 분할 시) | (D+G/2) ~ 100% | 0 ~ 11% | 좌측과 동일한 높이·Typography·정렬(§10). 바깥쪽(X=100%) 경계는 우측 Benefit Area와 동일, 안쪽 경계만 Gap의 절반만큼 D%에서 물러남 |
| Benefit Area Header (통합 시) | 0 ~ 100% | 0 ~ 11% | 좌/우 Benefit Area를 합친 본문 전체 폭, 높이·Typography·정렬은 §10 그대로. 통합 Header는 1개 Bar이므로 Header Gap이 적용되지 않는다 |
| Left Benefit Area Body | 0 ~ D% | 11 ~ 100% | Header 하단부터 본문 하단까지(통합/분할 무관 동일) |
| Right Benefit Area Body | D% ~ 100% | 11 ~ 100% | 위와 동일 |
| Vertical Divider (§11) | D% 지점(= Header Gap의 정중앙과 동일 좌표) | Benefit Area Body(Content Area) 내부, Hard Rule §11 "Content Region 범위 기준" 원칙에 따라 실제 콘텐츠 배치에 맞춰 자연스럽게 판단(세로 중심은 Content Area 중심과 일치) | Header 영역(Header Gap 포함) 비침범, Footnote가 있으면 그 상단까지의 Content Area 기준([5](#5-vertical-divider-hard-rule-11-적용) 참조) |

`D`(좌우 분할 지점)는 기본 50%이며, 콘텐츠 중요도에 따라 최대 55%까지
조정할 수 있다(Reference 실측 비율은 약 54%). 좌측이 항상 더 넓어야
하는 것은 아니며, 콘텐츠 비중에 따라 우측을 더 넓게 조정할 수도 있다
(그 경우 D는 45~50% 범위로 조정).

`G`(분할 Header 사용 시 좌/우 Header Bar 사이 Gap)는 두 Header가 맞닿아
하나의 통합 Header처럼 보이지 않도록 분리하는 간격이다. Gap의 시각적
일관성은 **Hard Rule §10**이 관리한다 — 이 문서는 별도의 고정 %/px
Gap 값을 정의하지 않으며, 좌/우 Gap을 서로 동일하게 유지하고 Benefit
Area Grid 기준에 맞춰 자연스럽게 배치한다. Gap은 두 Header가 서로
마주보는 **안쪽 경계에서만** 차감하며, 바깥쪽 경계(좌측 Header의
X=0%, 우측 Header의 X=100%)는 그대로 유지해 Benefit Area Body 및
Hard Rule Safe Area 여백과 어긋나지 않게 한다 — 그 결과 좌/우 Header는
Gap만큼을 제외하면 각각 자신이 속한 Benefit Area와 동일한 폭·중심축을
유지한다. 통합 Header(1개)에는 G가 적용되지 않는다.

## 4. Benefit Area Header (Hard Rule §10 적용)

Main Title Safe Area(Hard Rule §9, Y=135px) 바로 아래, 본문 상단에는
Hard Rule **§10 Content Comparison Header** 스타일을 적용한 Header를
배치한다. Header를 **통합 1개**로 배치할지 **좌/우 분할 2개**로
배치할지는 아래 [Header 판단 기준](#header-판단-기준)에 따라 결정하며,
어느 경우든 Header의 높이·Y 위치·Typography·정렬 구조 자체는 Hard
Rule §10 원 스펙을 그대로 따르고 이 문서에서 재정의하지 않는다.

### Header 판단 기준

**Header 선택 조건**: Header 형태는 스타일 취향이 아니라 콘텐츠의
의미 구조(좌/우 Benefit이 서로 독립적인지, 하나의 메시지로 묶이는지)를
먼저 판단해 선택한다.

| 콘텐츠 의미 구조 | 선택 Header 형태 |
|---|---|
| 좌/우 Benefit이 서로 독립된 2개의 개선 효과 | **분할 Header** — 독립 Header Bar 2개 |
| 좌/우 Benefit을 하나의 동일한 대표 메시지가 포괄 | **통합 Header** — Header Bar 1개 |

구체적 판정 기준(분할 Header 필수 조건, 통합 Header 예외 조건, 판단
절차)은 아래 내용을 따른다.

기본값은 **분할 Header**다 — 본 Layout의 좌/우 Benefit은 원칙적으로
서로 독립적인 2개의 개선 효과이므로, 별다른 판단 없이는 분할 Header를
사용한다. 즉 Benefit Area가 좌/우 2개로 구성되는 이 Layout에서는
Header도 원칙적으로 동일하게 좌/우 2개 영역으로 분할된다. **통합
Header**는 그 중 하나의 메시지가 전체를 대표할 수 있다고 판단되는
예외적인 경우에만 선택한다.

-   **분할 Header 필수 조건**: 좌/우 Benefit의 주제·핵심 메시지가 서로
    다르면 **반드시 분할 Header(2개)를 사용한다.** 예: 현재 QA
    테스트의 "OPEX 절감" vs "수율 향상"처럼 대상 지표(비용/수율 등)나
    개선 방향 자체가 성격이 다른 경우가 여기 해당한다. 이런 경우
    통합 Header로 묶으면 서로 다른 두 메시지 중 하나가 희석되거나
    표현이 모호해지므로 선택지에서 제외한다.
-   **통합 Header 예외 조건**: 좌/우 2개의 Benefit을 **하나의 동일한
    대표 메시지**로 자연스럽게 묶을 수 있는 경우에만 예외적으로
    통합 Header(1개)를 사용한다 — 즉 두 Benefit이 별개 주제가 아니라
    같은 개선 방향을 수치·관점만 달리 보여주는 관계일 때만 해당한다.
-   분할 Header는 하나의 Bar를 선(Divider 등)으로 나눈 형태가 아니라
    완전히 분리된 **독립 Header Bar 2개**로 생성한다. 동일한 Fill·상하
    Divider 스타일의 두 Bar가 Gap 없이 맞닿으면 시각적으로 하나의
    통합 Header처럼 보이므로, 두 Bar 사이에는 반드시
    [Overall Region Map](#overall-region-map)에서 정의한 Header
    Gap(G)을 적용해 명확히 분리한다.
-   각 Header는 자신이 속한 Content Group(Benefit Area)의 폭과 가로
    방향 중심축(center)에 맞추는 것을 원칙으로 하되, Header Gap(G)만큼은
    예외로 허용한다 — 바깥쪽 경계(좌측 Header의 X=0%, 우측 Header의
    X=100%)는 좌/우 Benefit Area의 바깥쪽 경계와 정확히 일치시키고,
    서로 마주보는 안쪽 경계만 Gap의 절반만큼 물러난다. 두 Header의
    높이·Y 위치·Typography·정렬 구조는 동일하게 유지한다. Header는
    아래 Benefit Area보다 (Gap을 제외하고) 넓거나 좁게, 또는 좌우로
    치우쳐 배치되지 않는다([11. Alignment](#11-alignment) 참조).
-   통합 Header(1개, 본문 전체 폭 사용)를 선택하는 경우, Header는
    좌측 Benefit Area 시작점부터 우측 Benefit Area 끝점까지 본문 전체
    폭(좌우 Benefit Area를 합친 폭)을 차지하는 1개 텍스트로 배치한다.
-   판단 절차: 먼저 "좌/우 Benefit의 주제·핵심 메시지가 서로 다른가"를
    확인한다 — 다르면 분할 Header로 확정하고 그 이상 고민하지 않는다.
    같지 않다고 단정하기 어려운 경우에만 "두 Benefit이 동일한 Core
    Technology/Solution을 설명하는 한 문장으로 자연스럽게 요약되는가"를
    추가로 검토해 통합 여부를 예외적으로 결정한다. 억지로 묶으면
    의미가 흐려지는 경우 기본값인 분할을 유지한다.

두 경우 모두 Header의 구체적인 치수·폰트 크기·색상·Divider 스펙은 이
문서에서 재정의하지 않으며, Hard Rule §10 원 스펙을 그대로 따른다.
분할 Header를 사용하는 경우 좌/우 Header의 경계 X 위치는
[3. Overall Structure](#3-overall-structure)의 분할 지점(D)과 항상
동일하며, 이 D% 값은 [5. Vertical Divider](#5-vertical-divider-hard-rule-11-적용)의
Divider X 위치와도 반드시 일치한다 — 두 값은 별도로 관리되지 않고
하나의 D%를 공유한다. Vertical Divider(§11, [5])의 세로 배치 범위는
통합/분할 여부와 무관하게 동일하게 적용된다([5] 참조).

-   Header 텍스트에는 각 Benefit Area의 핵심 구분/카테고리를 짧게
    표기한다(예: `CAPEX 절감` / `OPEX 절감` 등 실제 콘텐츠의 Benefit
    구분 명, 통합 Header의 경우 두 Benefit을 아우르는 한 문장).
-   본 Layout의 좌/우 Benefit은 Before/After처럼 기존 대비 개선을
    대립적으로 비교하는 관계가 아니라, 하나의 솔루션이 만드는 **2개의
    병렬적 긍정 효과**다. 따라서 분할 Header를 사용하는 경우 좌우
    Header는 Hard Rule §10의 **Parallel Variant**를 양쪽에 동일하게
    적용한다(Contrast Variant는 사용하지 않는다). 한쪽에만 다른
    스타일을 부여해 두 Benefit 사이에 우열이 있는 것처럼 보이게 하지
    않는다.

## 5. Vertical Divider (Hard Rule §11 적용)

두 Benefit Area 사이에는 Hard Rule **§11 Vertical Content Divider**를
적용한다. 두께·색상·Gradient 처리는 Hard Rule §11 원 스펙을 그대로
따르며 이 문서에서 재정의하지 않는다.

-   Divider의 X 위치는 [3. Overall Structure](#3-overall-structure)의
    분할 지점(D)에 맞춰 배치한다. 분할 Header를 사용하는 경우 이 D%는
    좌/우 Header Bar 사이 **Header Gap(G)의 정중앙**과 항상 일치한다
    (좌측 Header 안쪽 경계 D-G/2%, 우측 Header 안쪽 경계 D+G/2%의
    중간점) — D%는 별도로 관리되지 않고 Header Gap 중심·Divider
    위치가 하나의 값을 공유한다. Divider와 Header Gap은 같은
    X좌표(D%)를 공유하되 Y축 구간은 겹치지 않는다 — Gap은 Header
    높이(Y 0~11%) 구간에, Divider는 그 아래 Content Area 구간에만
    나타난다.
-   Divider는 Header 영역(Header Gap 포함)에 바로 붙여서 시작하지
    않는다. Header 영역(통합/분할 무관)과 완전히 분리된, Header 아래
    실제 Benefit Content Area(Header를 제외한 본문 영역, [3. Overall
    Region Map](#overall-region-map)의 Benefit Area Body) **내부**에서
    시작·종료한다.
-   Divider는 Content Area의 세로 중앙 범위를 중심으로 배치하며, 좌우
    Benefit 본문을 충분히 구분할 수 있도록 본문 높이의 대부분을
    커버한다. 정확한 상·하단 여백은 고정 % 수치가 아니라 **Hard Rule
    §11**의 "Content Region 범위 기준" 원칙에 따라, 실제 좌우 Benefit
    콘텐츠(Benefit Message~Evidence Visual~Supporting Text)의 배치에
    맞춰 자연스럽게 판단한다 — 인접 콘텐츠에 바로 닿지 않으면서도
    "좌우 Benefit이 충분히 구분되어 보인다"는 목적을 만족하는 범위를
    콘텐츠 구성에 따라 판단하며, Divider의 세로 중심은 Content Area의
    세로 중심과 일치시킨다.
-   Divider의 상·하단은 Hard Rule §11 자체의 Gradient 설계(양 끝
    White Fade-out)에 따라 Content Area 내부에서 자연스럽게
    Fade-out되며, 어떤 경우에도 Header 영역을 침범하지 않는다.
-   Footnote가 있는 경우, Content Area는 Footnote 영역 상단까지로
    계산되며 Divider 하단은 Footnote 영역을 침범하지 않는다.
-   이 세로 배치 규칙은 Header가 통합 1개이든 좌/우 분할 2개이든
    동일하게 적용된다([4](#4-benefit-area-header-hard-rule-10-적용)
    참조).

## 6. Benefit Area 내부 구조

각 Header(§10, [4](#4-benefit-area-header-hard-rule-10-적용)) 바로
아래, 각 Benefit Area는 다음 정보 위계를 기본으로 한다.

**Benefit Message** ↓ **Evidence Visual(Chart/Table/Diagram 등)** ↓
**(필요 시) Supporting Text**

Benefit Message는 해당 Benefit Area가 증명하려는 핵심 개선 효과를
짧고 강하게 전달하는 문장이다(예: `추출 효율 2~5% 개선 → 추출 단수
1단 저감(CAPEX 경제성 확보)`). Evidence Visual은 이 메시지를 뒷받침하는
증거이며, Supporting Text는 이제 Evidence Visual **아래**에 위치해
보조 설명·비교를 덧붙인다. 기존에 Headline과 Evidence Visual 사이에
두던 "영역 내부 소규모 비교"(Comparison Sub-block)는 별도 블록으로
분리하지 않고, Supporting Text 또는 Evidence Visual 자체(예:
Comparison Chart/Bar)로 흡수해 표현한다
([9](#9-comparison-inside-benefit-area) 참조).

예: `공정 단수 감소 → CAPEX 절감` ↓ `추출 효율 비교 차트` ↓ `기존 4단
vs COSOLUS 5단 비교 텍스트`
`부산물 감소 → OPEX 절감` ↓ `기존 대비 비교 표` ↓ `연간 절감량
하이라이트 수치`

Reference pptx 실측 기준 대략적인 비율(참고용, 콘텐츠에 따라 조정
가능. 아래 %는 Header 하단 이후 Benefit Area 본문 높이 기준):

-   Benefit Message: 약 15~20%
-   Evidence Visual: 약 55~70%(가장 넓은 비중, 축 라벨 등 부속 요소
    포함)
-   (필요 시) Supporting Text: 나머지 — 사용하지 않으면 그만큼
    Evidence Visual에 배분
-   (선택) Footnote: 최소 높이

-   Benefit Message는 짧고 강하게 작성한다.
-   정량 효과가 있으면 수치를 Benefit Message 또는 Evidence Visual
    가까이에 적극적으로 노출한다.
-   `CAPEX`, `OPEX`, 생산성, 환경성 등 비즈니스 의미가 있으면 보조
    Label로 명확히 연결한다.
-   Benefit Message → Evidence Visual → Supporting Text는 요소 간
    간격을 좁혀 하나의 시각적 그룹으로 인식되도록 배치한다. 그룹
    내부 요소 간 간격은 좌우 Benefit Area 사이의 간격(Divider
    여백)보다 항상 작게 유지한다.
-   **정렬 기준은 좌측 정렬이 아니라 Center Align이다.** Benefit
    Message, Evidence Visual, Supporting Text는 각각 좌측 끝에 맞춰
    쌓지 않고, 자신이 속한 Content Group(해당 Benefit Area)의 폭을
    기준으로 수평 중심을 맞춰 배치한다. Evidence Visual 자체가
    Chart/Table 등으로 내부 구성 요소가 좌우 비대칭인 경우, 그 내부
    구성 요소 하나하나의 배치까지 강제하지는 않는다 — 다만 Evidence
    Visual 블록 전체와 Benefit Message/Supporting Text 같은 텍스트
    요소는 모두 Content Group 중심을 기준으로 수평 정렬한다
    ([11. Alignment](#11-alignment) 참조). **단, Supporting Text가
    여러 줄로 구성되는 경우** 이 Center Align은 텍스트 블록 자체의
    수평 위치(블록을 Content Group 중심에 놓는 것)에만 적용되며,
    블록 **내부** 줄들의 정렬까지 강제하지 않는다 — 자연스러운 문장
    흐름을 위해 블록 내부 텍스트는 Left Align을 허용한다(아래
    "Supporting Text 작성 규칙" 참조).

### Supporting Text 작성 규칙

Supporting Text(및 그 밖의 세부 설명 텍스트)는 아래 규칙을 따라
작성한다.

-   긴 설명을 한 줄로 길게 이어 쓰지 않는다.
-   의미 단위, 문장 단위, 조건/결과 단위로 자연스럽게 줄바꿈한다.
-   한 줄 길이가 과도하게 길어지지 않도록 2~3줄 내에서 읽기 좋게
    구성한다.
-   텍스트가 박스를 벗어날 것 같을 때, 폰트를 강제로 축소하기보다
    **줄바꿈과 텍스트 박스 폭 조정을 우선** 적용한다 — Typography(§16)
    범위를 벗어나는 임의 축소로 회피하지 않는다.
-   텍스트 블록 자체(블록 전체의 위치)는 Content Group 기준 Center
    Align을 유지한다. 다만 여러 줄로 구성된 설명은 자연스러운 문장
    흐름을 위해 텍스트 블록 **내부**에서는 필요 시 Left Align을
    허용한다 — 즉 블록의 수평 위치는 가운데, 블록 안 각 줄의 정렬은
    좌측 정렬이 가능하다.

## 7. Evidence Visual

Benefit을 증명하는 자료 유형은 Reference PPT가 사용한 특정 형식에
고정하지 않고, 입력 콘텐츠의 특성과 전달 목적을 분석해 아래 중 가장
적합한 형식을 자동으로 선택한다.

-   Line / Bar Chart
-   Comparison Chart / Comparison Visual
-   Compact Table
-   Before/After Visual
-   Diagram
-   Calculation Result
-   Image / Photo + Result
-   기타 정량적 Evidence

좌우 Evidence가 서로 다른 Visual 유형이어도 된다(예: 좌측은 Chart,
우측은 Table). 단, 전체 시각적 무게와 영역 밀도는 균형을 유지한다.
하나의 Benefit Area 안에 관련된 Evidence Visual을 2개(예: 비교되는
2개의 Chart)까지 나란히 배치할 수 있다.

-   **정량 데이터가 없는 콘텐츠는 임의의 수치나 그래프를 새로 만들지
    않는다.** Chart/Table 등 정량 시각화는 실제 입력 데이터가 있을
    때만 사용하고, 정량 데이터가 없으면 Diagram/Image/정성적 설명 등
    데이터를 꾸며내지 않는 형식을 사용한다.
-   Evidence Visual은 해당 Benefit Area가 가진 가용 폭과 높이를
    적극적으로 사용해 충분히 크게 배치한다([6](#6-benefit-area-내부-구조)의
    약 55~70% 기준). 여백을 남기기 위해 임의로 축소하지 않는다.
-   단순 KPI/Large Number 하나만 있는 경우에도 숫자를 넓은 빈 공간에
    단독 배치하지 않는다. Before/After 비교, Mini Chart, Comparison
    Bar 등 수치를 뒷받침하는 시각화와 함께 구성한다. **큰 KPI 숫자 +
    넓은 여백, Card/Badge/Dashboard형 재해석은 금지한다.**
-   좌우 Benefit Area의 Evidence Visual은 시작 위치(상단 기준선)와
    시각적 중심을 가능한 한 정렬한다.

## 8. Quantitative Emphasis

-   개선율, 감소율, 비용, 공정단수, 수율 등 핵심 수치를 우선적으로
    시각화한다.
-   수치는 Supporting Text 안에 묻히지 않도록 한다.
-   핵심 수치와 비교 기준이 무엇인지 명확하게 표시한다.
-   과도한 장식보다 Evidence 자체가 중심이 되도록 한다.

## 9. Comparison Inside Benefit Area

한 Benefit Area 내부에서 기존 대비 개선을 보여줄 필요가 있는 경우,
별도의 Comparison Sub-block을 추가하지 않고
[6](#6-benefit-area-내부-구조)의 **Supporting Text** 또는 **Evidence
Visual 자체**(예: Comparison Chart/Bar, Before/After Visual)로 비교를
표현한다.

예: `Existing vs New` `Before → After` `Competitor vs Our Solution`

단, 전체 슬라이드를 Comparison Matrix로 바꾸지 않는다. 비교는 해당
Benefit을 증명하기 위한 하위 표현으로 사용한다.

## 10. Density & Spacing

-   Reference와 유사한 중간~높은 정보 밀도를 유지한다. 큰 숫자 하나와
    과도한 White Space 중심의 KPI Dashboard 스타일은 지양한다.
-   Evidence Visual은 Benefit Area 내에서 가장 넓은 면적을 차지하도록
    충분히 크게 사용한다([6](#6-benefit-area-내부-구조) 참조).
-   Benefit Area 상단에 텍스트만 몰리고 하단이 비는 구성을 피한다.
-   본문 중앙 및 하단에 콘텐츠 없이 비어 보이는 영역이 발생하지 않도록
    Evidence Visual 크기와 요소 배치를 조정한다.
-   좌우 영역의 Visual 크기와 텍스트 양을 균형 있게 조절한다.
-   불필요한 Card UI를 반복하지 않는다.

## 11. Alignment

-   좌우 Benefit Area Header(§10)의 높이·Y 위치를 동일하게 맞춘다.
-   분할 Header 사용 시, 각 Header의 **폭과 가로 방향 중심축은 자신이
    속한 Benefit Area(Content Group)와 정확히 일치**시킨다([4. Header
    판단 기준](#header-판단-기준) 참조).
-   각 Benefit Area 내부의 Benefit Message, Evidence Visual,
    Supporting Text는 좌측 정렬이 아니라 **해당 Content Group(Benefit
    Area) 기준 Center Align**을 사용한다 — 요소들의 수평 중심을 자신이
    속한 Benefit Area 폭의 중심에 맞춘다. Evidence Visual 내부의 개별
    구성 요소 배치까지 강제하지는 않되, Evidence Visual 블록 전체와
    텍스트 요소(Benefit Message/Supporting Text)의 수평 중심은 동일한
    기준을 따른다([6. Benefit Area 내부 구조](#6-benefit-area-내부-구조)
    참조).
-   Benefit Message의 Y 위치(Header 하단 기준 상대 위치)를 좌우
    동일하게 맞춘다.
-   좌우 Benefit Area의 시작점(X, Header 하단 Y)과 하단 기준선을
    가능한 한 정렬한다.
-   Evidence Visual의 시각적 중심을 맞춘다.
-   Vertical Divider(§11)는 두 Benefit Area의 경계(D%)에 정확히
    배치하며, 세로 방향으로는 Header를 침범하지 않고 Content Area
    내부에서 inset되어 배치된다([5. Vertical Divider](#5-vertical-divider-hard-rule-11-적용)
    참조).

## 12. Flexibility

### Must Preserve

-   하나의 Core Technology/Solution (Main Title에서 전달)
-   좌/우 **정확히 2개**의 핵심 Benefit/Impact
-   Benefit Area Header(Hard Rule §10)와 Vertical Divider(Hard Rule
    §11) 구조 — Benefit Area를 구분하는 시각 장치는 이 두 가지뿐이며,
    배경 Fill/Border/Rounded Corner로 감싼 카드형 컨테이너를 추가하지
    않는다([13. Avoid](#13-avoid) 참조)
-   각 Benefit을 뒷받침하는 Evidence
-   Technology → Improvement → Impact의 논리 흐름

### May Adapt

-   Evidence 유형(Chart/Table/Diagram 등)
-   좌우 영역 비율(D, 50~55% 범위)
-   분할 Header 사용 시 Header Gap(G) — 값은 Hard Rule §10이 관리(좌우
    동일 유지, 이 문서에서 별도 수치를 정의하지 않음)
-   Header 구성 — 통합 1개 / 분할 2개 중 콘텐츠 구조에 따라
    [4. Header 판단 기준](#header-판단-기준)을 적용해 결정
-   분할 Header 사용 시에도 Header(§10)는 항상 **Parallel Variant**를
    좌우 공통으로 사용한다(§4의 병렬 Benefit 원칙 참조 — 대립 비교가
    아니므로 Contrast Variant는 사용하지 않는다)
-   Benefit Area 내부 Supporting Text 사용 여부, Evidence Visual
    내부 비교 표현 방식
-   Footnote 사용 여부

## 13. Avoid

-   단순 장점 Bullet 2개만 나열
-   Evidence 없이 효과를 주장
-   정량 데이터가 없는 상태에서 임의의 수치·그래프를 새로 만들어
    Evidence Visual에 사용(데이터가 없으면 Diagram/Image/정성적 설명
    사용, [7. Evidence Visual](#7-evidence-visual) 참조)
-   좌우 Benefit Area 간 정보 위계가 서로 다른 구성
-   그래프/표를 지나치게 작게 배치
-   모든 내용을 카드 안에 넣는 구성 — 구체적으로, 각 Benefit Area
    전체(Benefit Message~Evidence Visual~Supporting Text)를 하나의
    Div/Shape로 묶어 **배경색 Fill(Tint 등) + Border + Rounded Corner**를
    적용하는 것(웹 UI의 통상적인 "Card" 컴포넌트 관습). 이 조합 중
    하나만 있어도(예: Border-radius 없이 배경 Tint + Border만 있는
    경우도) 카드형 재해석으로 간주해 금지한다 — "그림자가 없으니
    카드가 아니다" 같은 자의적 예외를 허용하지 않는다. 두 Benefit
    Area를 나누는 시각적 장치는 [3. Overall Structure](#3-overall-structure)가
    명시하는 Header Bar(§4)와 Vertical Divider(§5) 두 가지뿐이다.
-   Evidence를 큰 KPI 숫자 + 넓은 여백, Card/Badge/Dashboard형으로
    재해석
-   Benefit Area Header(§10) 스타일(치수·색상·Typography 등)을 임의로
    변형
-   좌우 Header에 서로 다른 스타일(Before/After식 대립 구도)을 차등
    적용
-   분할 Header를 Gap 없이 맞닿은 하나의 Bar로 만들고 그 경계에 세로
    선(Divider 등)만 그어 "분할된 것처럼" 표현 — 반드시 Header Gap(G)으로
    물리적으로 분리된 독립 Bar 2개로 렌더링한다
-   Vertical Divider(§11) 스타일(두께·색상·Gradient)을 임의로 변형
-   핵심 Benefit을 3개 이상으로 늘려 배치(→ 다른 Layout 사용)
-   Reference의 특정 데이터나 문구 복제
-   Hard Rule 또는 Claude PPT Design System 변경

## 14. Rule Priority

1.  Hard Rule (§9 공통 Header System, §10 Content Comparison Header,
    §11 Vertical Content Divider 포함)
2.  Claude PPT Design System
3.  Reference PPT(`benefit-impact.pptx`) 실측 비율
    ([2. Reference Reproduction Principle](#2-reference-reproduction-principle),
    [3. Overall Region Map](#overall-region-map) 기준)
4.  Benefit + Impact Layout Reference 서술 규칙

본 Layout Reference는 Hard Rule 및 Design System을 변경하거나 대체하지
않는다.

## 15. Selection Rule

다음 조건을 만족할 때 우선 고려한다.

1.  하나의 기술·솔루션이 중심에 있음
2.  그 기술로 인해 발생하는 **정확히 2개**의 명확한 개선 효과가 있음
3.  각 효과를 수치, 그래프, 표, 이미지 등 Evidence로 증명할 수 있음

단순히 장점이 여러 개 있다는 이유만으로 적용하지 않는다. 핵심 효과가
1개뿐이거나 3개 이상이면 [Do Not Use When](#do-not-use-when)의 대안
Layout을 검토한다.

## 16. Typography (Reference PPT 실측 기반)

Reference PPT(`benefit-impact.pptx`)의 텍스트 run 단위 실측(`a:rPr
sz`, Bold 여부 등)을 근거로 이 Layout에서 사용하는 Font Size/Weight
범위를 아래와 같이 고정한다. 이 범위를 벗어난 임의의 Font Size나
Weight를 이 Layout에서 새로 만들지 않는다. Benefit Message는
`Claude_PPT_Design_System.md` §3의 Key Message/Explanation 역할에
해당하므로 Header Bar(Hard Rule §10 고정값)와 같은 행으로 묶지 않고
Explanation Tier(18pt)를 별도로 적용한다.

| 역할 | Font Size | Weight |
|---|---|---|
| Main Title | 28pt | ExtraBold (Hard Rule §9, 참조만 — 본 문서에서 재정의하지 않음) |
| Benefit Area Header(Hard Rule §10 Header Bar) | 20pt | SemiBold (Hard Rule §10 고정값, 참조만 — 본 문서에서 재정의하지 않음) |
| Benefit Message(Key Message) | 18pt | SemiBold (Design System §3 Explanation Tier) |
| Body / Supporting Text | 16pt | Light |
| Chart·Table Label | 14pt | SemiBold |
| Footnote / Source | 14pt | Light |

Font Weight는 Pretendard **ExtraBold**(최상위 강조) / **SemiBold**
(핵심 메시지·Header) / **Light**(보조·Footnote) 체계 안에서만 정보
위계에 따라 적용하고, 이 범위를 벗어난 임의의 Weight나 Font Size를
생성하지 않는다.
