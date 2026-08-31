# Three-Column Insight Layout

## 1. Purpose

서로 구분되는 **3개의 핵심 요인, 이슈, 근거, 특징 또는 비교 항목을 한
슬라이드에서 병렬적으로 설명**할 때 사용하는 3분할 레이아웃이다.

이 레이아웃은 각 항목의 중요도가 유사하고, 3개의 메시지를 독립적인 정보
단위로 동시에 보여줄 필요가 있을 때 사용한다.

### Use When

-   산업적 요인 또는 배경 3가지를 설명할 때
-   문제점 또는 이슈 3가지를 병렬적으로 제시할 때
-   핵심 경쟁력 또는 특징 3가지를 설명할 때
-   시장·기술·환경 등의 변화 요인 3가지를 제시할 때
-   서로 독립적이지만 동일한 위계의 근거 3가지를 비교·설명할 때

### Do Not Use When

-   3개 항목이 순차적으로 이어지는 프로세스인 경우
-   시간의 흐름이 중요한 경우
-   하나의 항목이 나머지보다 현저히 중요한 경우
-   두 대상의 직접 비교가 핵심인 경우
-   3개로 나누는 것이 콘텐츠 의미상 부자연스러운 경우

------------------------------------------------------------------------

> **Reference 출처**: 이 문서의 §3~§7에 명시된 영역 비율·간격·정렬
> 수치는 `3 column_reference.pptx`(3분할 Reference 슬라이드 3장) 분석에서
> 콘텐츠가 아닌 **레이아웃 구조만** 추출해 반영한 것이다(분석 결과는
> 이 문서에 모두 반영되어 있으며 원본 pptx는 별도로 보관하지 않는다).
> 실제 웹PPT/pptx 생성 시에는 pptx 원본을 열어볼 필요 없이 **이
> 문서(three-column.md)만 기준으로 적용**한다.
> Reference의 좌측 세로 브랜드 스트라이프(다크+옅은 틴트 컬러 바)는
> 해당 Reference 자체의 고유 표지 요소이며 3분할 구조와 무관한
> 장식이므로 반영 대상에서 제외했다 — 이미 확정된 Hard Rule 공통
> Header System(CI/Sub Message/구분선/Section Label/Main Title/페이지
> 번호)과 별개로 새로운 브랜드 장식을 추가하지 않는다.

## 2. Basic Structure

본문 콘텐츠 영역을 **동일한 비중의 3개 Column**으로 구성한다.

기본 구조:

`Column 1 | Column 2 | Column 3`

각 Column은 기본적으로 다음 정보 위계를 따른다.

1.  Column Header (Header Bar)
2.  Key Message
3.  Main Visual
4.  Supporting Information / Evidence (필요한 경우에만)

Column 내부는 여백보다 정보 밀도를 우선한다 — 4개 요소 사이 간격은
필요한 최소 수준으로 유지하고, 콘텐츠 특성에 따라 3\~4번 요소의 조합과
순서는 유연하게 조정할 수 있다.

------------------------------------------------------------------------

## 3. Column Header (Header Bar)

각 Column 상단에는 **Hard Rule §10 Content Region Header** 스타일을
그대로 적용한 Header Bar를 사용한다. Height·Font·Font Color·Letter
Spacing·정렬·Padding·Corner·Fill·Divider·Gap 등 Header Bar 자체의 시각
스펙은 이 문서에서 재정의하지 않으며, Hard Rule §10 원 스펙을 그대로
따른다. 이 문서(Layout MD)가 결정하는 것은 Header의 **개수(3개)·폭·
Content Group 대응 관계**, 그리고 Hard Rule §10이 정의하는 두 Named
Variant 중 어느 것을 쓸지뿐이다.

-   3개 Header Bar는 서로 맞닿지 않고 시각적으로 구분되는 **Gap을 두고
    배치**한다 — Header Bar끼리 이어 붙어 하나의 긴 Header처럼 보이지
    않아야 한다. Gap의 시각적 일관성(3개 Gap을 서로 동일하게 유지하고
    Column Grid 기준에 맞춰 자연스럽게 배치하는 것)은 **Hard Rule §10**이
    관리한다. 각 Header Bar 내부에는 해당 Column의 핵심 주제를 짧고
    명확하게 표기한다.
-   3개 Header Bar의 **X/Y 위치, 폭(Gap 제외), 높이를 모두 동일하게
    유지**한다.
-   3개 Column은 Before/After처럼 대립하는 두 대상이 아니라 대등하고
    독립적인 병렬 항목이므로, Hard Rule §10의 **Parallel Variant**를
    3개 Header Bar 모두에 동일하게 적용한다 — Column마다 다른 Variant를
    섞어 쓰지 않는다.
-   Header 텍스트는 중앙 정렬(Hard Rule §10 기준)을 유지하며, 3개
    항목이 동일한 정보 위계로 인식되도록 한다.

------------------------------------------------------------------------

## 4. Key Message

Header Bar 바로 아래에는 해당 Column의 핵심 메시지를 배치한다.

-   **간격**: Header Bar와 Key Message 사이 간격은 좁게 유지해(Header
    Bar 높이의 약 1/3 수준) 두 요소가 하나의 상단 블록처럼 응집되어
    보이도록 한다.
-   **가로 배치**: Header Bar와 달리 Column 폭 전체를 채우지 않는다.
    좌우에 여백을 두어 Column 폭의 약 **70~85%** 수준으로 좁게
    배치해, 옅은 배경의 Header Bar와 구분되는 헤드라인처럼 보이도록
    한다.
-   폰트/스타일: **Pretendard ExtraBold, 18pt**, 컬러는 **회사 Main
    Color**(Hard Rule Brand Color 표의 Primary 컬러)를 사용한다.
-   **길이**: 1~2줄 이내로 간결하게 구성한다. 문장을 길게 늘여쓰지
    않는다.
-   **밑줄 강조**: 메시지 내 핵심 키워드 또는 핵심 문장 일부에 한해
    밑줄 강조를 적용할 수 있다.
    -   밑줄 색상은 Key Message와 동일한 회사 Main Color를 사용한다.
    -   밑줄은 **장식 목적이 아니라 핵심 키워드·핵심 문장을 강조하는
        용도로만** 사용한다.
    -   메시지 전체 문장에 밑줄을 긋거나, 강조 대상이 불분명한 채로
        남용하지 않는다.
-   3개 Column의 Key Message는 폰트·크기·컬러·정렬 방식을 동일하게
    유지하고, 각 Column의 내용에 따라 텍스트와 밑줄 강조 위치만
    달라진다.

------------------------------------------------------------------------

## 5. Main Visual

Key Message 아래에는 해당 내용을 뒷받침하는 **Main Visual**을
배치한다.

-   Main Visual을 정하기 전, 각 Column의 콘텐츠 성격을
    [`content-visualization-freedom.md`](../design-system/content-visualization-freedom.md)의
    "Main Visual 선택 기준"에 따라 먼저 판단한 뒤 Chart / Large
    Number / Icon·Diagram / Map / Photo·Image / Text 중 적합한
    표현을 고른다.
-   Key Message와 Main Visual 사이 간격은 최소화한다 — 거의 붙듯이
    배치해 Key Message가 Main Visual의 캡션처럼 곧바로 이어지는
    느낌을 준다.
-   Main Visual은 각 Column에서 **가장 크고 적극적으로 활용되는
    시각적 핵심 요소**여야 한다 — Header Bar·Key Message를 제외한
    Column 콘텐츠 영역에서 **세로 기준 약 55~65%**를 Main Visual이
    차지하도록 충분한 영역을 확보한다. Supporting Evidence를 포함해도
    이 비중을 훼손하지 않는다.
-   Column 콘텐츠 하단(Main Visual 또는 Supporting Evidence의 마지막
    요소)과 슬라이드 하단(출처 표기 등)의 경계 사이에는 내용이 하단에
    바짝 붙지 않도록 작은 여백을 남긴다.
-   표현 방식은 콘텐츠 성격에 따라 자유롭게 선택한다. 사용 가능한
    표현 방식의 예:
    -   Chart / Graph
    -   Image / Photo
    -   Map
    -   Diagram
    -   Process Graphic
    -   Large Number / KPI
    -   Icon + Message
    -   Quote / Key Statement
    -   Comparison Graphic
    -   기타 콘텐츠 이해에 적합한 시각적 표현
-   **세 Column에 반드시 동일한 종류의 시각자료를 사용할 필요는
    없다.** 각 Column의 콘텐츠 성격이 서로 다르면 `Image | Chart |
    Map`, `Chart | Chart | Key Statement`, `KPI | Diagram | Image`
    처럼 Photo/Chart/Diagram/Map/Large Number/Icon 등 서로 다른
    표현 방식을 조합할 수 있다. 반대로 세 Column의 콘텐츠 성격이
    실제로 동일하다면 동일한 Visual Type을 사용하는 것도 허용된다 —
    Visual Type을 억지로 다르게 만드는 것이 목적이 아니라, 콘텐츠
    성격이 다른데도 편의상 동일한 표현 방식으로 통일하는 것을
    방지하는 것이 목적이다.
-   제공된 이미지 자산 중 특정 Column의 콘텐츠와 직접 관련된 이미지가
    있다면(`content-visualization-freedom.md`의 "이미지 자산 활용
    기준" 참고), 해당 Column의 Main Visual 후보로 우선 검토한다.
-   표현 방식이 다르더라도 3개 Column의 **전체적인 시각적 무게와 정보
    밀도는 균형을 유지**해야 한다.
-   3개 Main Visual은 Visual Type이나 내부 형태가 다르더라도 **Visual
    영역의 시작 위치와 높이를 동일하게 맞추고**, 실제 도형·이미지가
    차지하는 체감 크기와 시각적 무게가 균형을 이루도록 조정한다. 단순히
    동일한 width/height 값을 부여하는 것만으로 균형을 판단하지 않는다.
-   Supporting Information/Evidence를 덧붙일 때도 Main Visual을
    보조하는 수준으로 제한하고, Main Visual의 면적을 잠식하지 않는다.
-   Supporting Information/Evidence가 3개 Column에 모두 있다면 각
    Visual 영역의 높이를 맞춰 **Supporting Text의 시작 Y를 동일하게
    정렬**하고, Main Visual과 Supporting Text 사이의 간격도 Column마다
    동일하게 유지한다.

------------------------------------------------------------------------

## 6. Visual Hierarchy

각 Column 내부의 기본 정보 위계는 다음을 따른다.

**Header Bar → Key Message → Main Visual → Supporting Evidence**

-   Main Visual이 각 Column에서 가장 넓은 면적을 차지하는 핵심 시각
    요소가 되도록 한다.
-   Key Message는 짧고 빠르게 이해할 수 있도록 표현한다.
-   Supporting Evidence(세부 설명)는 Main Visual을 보조하는 수준으로
    제한한다.
-   텍스트만으로 공간을 채우기보다 데이터, 이미지, 차트, 지도, 아이콘
    등 콘텐츠에 적합한 시각적 표현을 우선 고려한다.
-   단, 시각자료가 정보 전달에 도움이 되지 않는 경우 억지로 추가하지
    않는다.
-   각 Column은 Header Bar부터 Main Visual까지 하나로 응집된 **독립적
    정보 블록**으로 인식되어야 한다.

------------------------------------------------------------------------

## 7. Alignment & Balance

-   3개 Column의 기본 폭은 동일하게 구성한다.
-   Column의 Main Visual/Supporting Evidence 영역 사이에는 별도의 넓은
    여백(gutter)을 두지 않는다 — 얇은 Vertical Divider가 경계선
    역할을 하며, Main Visual은 이 경계까지 채운다. 단, Header Bar
    영역만 위 §3의 Hard Rule §10 Gap 규정에 따라 예외적으로 Gap을
    둔다.
-   Vertical Divider의 두께·색상·Gradient 등 시각 스펙은 이 문서에서
    재정의하지 않으며, **Hard Rule §11 Vertical Content Divider**
    스펙을 그대로 따른다.
-   3개 Column 사이에 Divider를 사용하는 경우 두 Divider를 각각
    **인접 Column 사이 Gap의 중앙**에 배치한다. 어느 한 Divider가
    Column 경계나 콘텐츠 뒤에 가려지지 않도록 하며, 두 Divider 모두
    실제 렌더링 결과에서 명확히 보이는지 확인한다. DOM/CSS에 요소와
    선언이 존재하는지만으로 표시 여부를 판정하지 않는다.
-   Divider는 Header Bar 바로 아래에 붙여서 시작하지 않는다. Header
    Bar를 침범하지 않는 것만으로는 충분하지 않으며, Header Bar와
    이어진 선처럼 보이지 않도록 Header Bar를 제외한 Column Content
    영역(Key Message~Supporting Evidence, §5~§6 참조) **내부에서만
    시작·종료**한다 — Divider는 Header가 아니라 본문 Content Group을
    구분하는 요소로 인식되어야 한다. 정확한 상·하단 여백은 고정 % 수치가
    아니라 **Hard Rule §11**의 "Content Region 범위 기준" 원칙에 따라,
    실제 Key Message~Supporting Evidence 배치에 맞춰 Key Message 등
    상단 요소와 겹치지 않는 범위에서 자연스럽게 판단한다.
-   Divider의 세로 중심은 Column Content 영역의 세로 중심과 대략
    일치시킨다. Divider 상·하단은 Hard Rule §11 Gradient 설계(양 끝
    Fade-out)에 따라 Content 영역 내부에서 자연스럽게 사라지며,
    슬라이드 상단(Header)부터 하단까지를 그대로 가로지르는 절단선
    처럼 보이지 않아야 한다(Header Bar 자체 및 슬라이드 하단 출처
    영역은 Divider 범위에서 제외).
-   3개 Header Bar의 위치·폭·높이·배경색·스타일을 정렬·통일한다.
-   각 Column의 Main Visual 영역은 가능한 한 유사한 시각적 무게와
    크기를 갖도록 구성한다.
-   본문 Visual만 조정할 때는 기존 Header Bar와 Column 공통 Container의
    구조·Gap·Padding·크기·위치를 유지하고, 조정 범위를 각 Column의
    Visual 전용 영역과 그 내부 요소로 제한한다.
-   Column 내부 요소가 다른 Column 영역을 침범하지 않도록 한다.
-   Column 내부의 불필요한 상하 여백을 줄이고, Reference 수준의 정보
    밀도를 유지한다 — 특정 Column만 지나치게 비거나 과도하게
    복잡해 보이지 않도록 조절한다.
-   불필요한 카드, 테두리 또는 장식 박스를 반복적으로 추가하지 않는다.

------------------------------------------------------------------------

## 8. Content Adaptation

AI는 콘텐츠의 성격을 분석하여 각 Column에 적합한 Main Visual 표현
방식을 선택한다.

### Data-focused

`Header Bar → Key Message → Chart → Source/Supporting Data`

### Image-focused

`Header Bar → Key Message → Image → Supporting Text`

### Message-focused

`Header Bar → Key Message → Large Number/Icon → Supporting Statement`

### Map / Supply Chain-focused

`Header Bar → Key Message → Map → Key Data`

위 유형을 기계적으로 적용하지 말고, **각 Column의 핵심 내용을 가장
빠르고 명확하게 전달할 수 있는 표현 방식**을 우선한다.

------------------------------------------------------------------------

## 9. Layout Flexibility

이 문서는 고정 템플릿이 아니라 **Layout Reference**이다.

반드시 유지해야 하는 핵심 구조: - 3개의 병렬 정보 영역 - 동일하거나
유사한 정보 위계 - 3개 Column 간 시각적 균형 - 공통된 Header Bar 체계
(위치·높이·배경색·스타일 통일) - Header Bar → Key Message → Main
Visual 순서

유연하게 변경할 수 있는 요소: - 각 Column 내부(Main Visual)의
시각화 방식 - 이미지, 차트, 지도, 숫자, 인용문 등의 조합 - Key
Message의 밑줄 강조 위치 - 콘텐츠별 내부 간격 - Supporting Evidence의
포함 여부·양과 위치 - 필요에 따른 Divider 사용 여부

------------------------------------------------------------------------

## 10. Avoid

다음과 같은 구성은 피한다.

-   3개 Column의 폭이나 중요도가 이유 없이 크게 다른 구성
-   3개 Header Bar의 위치·높이·배경색·스타일이 서로 다른 구성
-   Header Bar를 Column 경계까지 채우지 않고 좌우에 불필요한 여백을
    남기는 것 (Header Bar는 edge-to-edge가 기본)
-   반대로 Key Message를 Header Bar처럼 Column 폭 전체로 늘려 여백
    없이 배치하는 것 (Key Message는 좌우 여백을 둔 좁은 배치가 기본)
-   Key Message를 2줄을 초과해 장황하게 작성하는 것
-   Key Message 밑줄을 강조 목적이 아닌 장식으로 남용하거나, 문장
    전체에 밑줄을 긋는 것
-   Main Visual을 작게 축소해 Column 내부에 불필요한 여백을 과도하게
    남기는 것
-   콘텐츠가 적다는 이유로 의미 없는 장식 요소를 추가하는 것
-   모든 Column을 무조건 동일한 Chart 또는 Card 형식으로 만드는 것
-   하나의 Column에 지나치게 많은 텍스트를 배치하는 것
-   시각자료의 크기 차이가 지나쳐 전체 균형이 무너지는 것
-   콘텐츠 특성과 관계없이 Reference Slide의 시각자료 종류를 그대로
    복제하는 것
-   Layout Reference 때문에 Hard Rule 또는 Design System을 변경하는 것

------------------------------------------------------------------------

## 11. Rule Priority

이 문서는 **Slide Layout Reference**이며 Hard Rule이 아니다.

적용 우선순위:

1.  **Hard Rule**
    -   CI
    -   Sub Message
    -   Divider
    -   Section Label
    -   Main Title
    -   Page Number
    -   기타 공통 고정 요소
2.  **Claude PPT Design System**
    -   Color
    -   Typography
    -   Chart Style
    -   Image Style
    -   Visual Language
    -   기타 공통 디자인 기준
3.  **Three-Column Insight Layout**
    -   3분할 콘텐츠 구조
    -   Header Bar(Hard Rule §10 스펙 적용) / Key Message 스타일
        (ExtraBold 18pt·회사 Main Color, 밑줄 강조 규칙 등)
    -   Header Bar/Key Message/Main Visual의 상대적 크기 비율과 간격
        (§3~§5, Reference 분석 기반)
    -   Column 간 정보 위계 및 정보 밀도
    -   콘텐츠 배치 및 시각적 균형

본 Layout Reference는 Hard Rule과 Claude PPT Design System을 변경하거나
대체하지 않는다. Key Message의 색상(회사 Main Color)과 폰트(Pretendard
ExtraBold)는 Hard Rule·Design System이 정의하는 브랜드 컬러·서체
범위 안에서 지정된 것이며, 이를 벗어나는 값으로 임의 변경하지 않는다.

------------------------------------------------------------------------

## 12. Selection Rule

슬라이드 콘텐츠를 분석했을 때 **동일하거나 유사한 중요도를 가진 3개의
독립적인 핵심 메시지를 병렬적으로 전달하는 것이 가장 적합한 경우** 이
Layout Reference를 우선적으로 고려한다.

단순히 콘텐츠 항목이 3개라는 이유만으로 자동 적용하지 않는다.

프로세스, 시간 흐름, 직접 비교 등 다른 정보 구조가 더 적합한 경우 해당
목적에 맞는 다른 Layout Reference를 선택한다.
