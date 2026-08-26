# 01. Cover

## Purpose

PPT의 첫인상을 형성하고, 발표 주제와 COSOLUS의 브랜드 이미지를 명확하게
전달하는 표지 슬라이드.

## Layout (Cover Composition)

> Primary Cover Design Reference: `docs/cover-reference/cosolus_cover_reference.png.png`.
> 아래 규칙은 이 Reference의 텍스트·이미지 내용이 아니라 배치 구조·비율·정렬·겹침
> 방식을 분석해 재사용 가능한 규칙으로 일반화한 것이다. 제목·배경 이미지가
> 달라져도 이 구조는 동일하게 유지한다.

> **Status: 확정(Default)**. 아래 Brand Block 구성, Sub Message 스타일, COSOLUS
> CI 위치·크기 및 Sub Message와의 관계, Main Title 위치·정렬·위계, Background
> Overlay 방식은 반복 테스트를 거쳐 COSOLUS 기본 Cover Style로 확정되었다.
> Background Image 자체(구체적인 이미지 파일)만 제외하고, 프로젝트마다 임의로
> 변경하지 않고 이 구조·수치를 기본값으로 적용한다. Background Image는 아래
> Soft Rules의 우선순위(사용자 제공 이미지 → Background Image Library → 단색
> 대체안)에 따라 매번 주제에 맞게 선택한다.

-   전체 슬라이드를 활용하는 Full Background Image 구조를 기본으로 한다.
-   배경 이미지와 그 위의 오버레이(Visual Style / Image Treatment 처리)는
    슬라이드 전체(가로·세로 100%)에 걸쳐 끊김 없이 이어지는 단일 레이어로
    적용한다. 특정 영역만 감싸는 별도의 사각 패널이나 카드형 반투명 박스로
    분리하지 않는다.
-   Brand Block(Sub Message + COSOLUS 로고)은 좌측 상단에 세로로 쌓인 구조로
    배치한다.
    -   Sub Message(브랜드 모토)를 위쪽, COSOLUS 워드마크를 그 바로 아래쪽에
        배치한다.
    -   표지의 Sub Message 문구는 "Small action, BIG DIFFERENCE"만 사용한다
        (COSOLUS 워드마크 로고가 바로 아래 있으므로 회사명 반복 없이 모토
        문구만 표기).
    -   Sub Message 색상은 COSOLUS CI(로고)와 동일한 White로 표현한다.
    -   Sub Message와 COSOLUS CI는 좌측 시작점을 정확히 맞추고, 우측 끝점은
        CI 가로폭과 완전히 동일할 필요 없이 비슷한 수준으로 맞춘다 — Sub
        Message 전체 가로폭이 CI 가로폭을 크게 넘지 않는 선에서 자연스러운
        정도면 충분하다.
    -   Sub Message의 Font Size는 판독성 있게 적절히 키우고, 자간은 넓게
        벌리지 않는다. 글자 수가 적어 목표 가로폭에 못 미치더라도 단어
        사이 여백(word-spacing)을 인위적으로 크게 벌려 강제로 채우지
        않는다 — 자연스러운 자간·단어 간격을 우선한다.
    -   기본값(1280×720px 슬라이드 기준): COSOLUS CI 로고 높이 36px(원본
        비율 399:62 유지, width는 auto로 비율 고정), Sub Message는
        Pretendard Medium 16px·letter-spacing normal·색상 White(#ffffff).
        이 조합에서 로고와 Sub Message의 좌측 시작점이 일치하고 가로폭이
        서로 비슷한 수준이 되는 것을 확인했다.
    -   Sub Message와 워드마크 사이 간격은 좁게 유지해 하나의 시각적 블록으로
        인식되게 한다.
    -   시각적 위계는 COSOLUS CI(로고) > Sub Message 순으로 유지한다. Sub
        Message는 CI보다 명확히 작고 보조적으로 보여야 하며, CI가 Brand
        Block의 주 시각 요소가 되도록 한다.
    -   Brand Block은 슬라이드 좌측 상단 모서리 여백(Grid/Spacing 마진) 안쪽에
        위치시키고, 다른 표지 요소보다 위 레이어에 그린다.
-   Main Title은 슬라이드의 가로 중심을 기준으로 정렬한다(각 줄의 중심이
    슬라이드 가로 중심에 오는 중앙 정렬 텍스트 블록).
    -   제목 블록은 수직으로는 정중앙보다 살짝 아래쪽에 위치시켜, 상단 Brand
        Block과 분리되어 보이게 하고 하단에 더 넓은 여백이 남도록 한다.
    -   제목이 2줄인 경우, 두 줄의 길이가 한쪽으로 크게 치우치지 않도록 의미
        단위로 줄바꿈한다.
    -   메인 제목은 1\~2줄 구성을 기본으로 한다.
    -   제목 블록의 가로 폭은 지나치게 좁게 제한하지 않는다. 제목이 길어지는
        경우 Title Area(제목 블록의 최대 가로 폭)를 충분히 넓게 확보해,
        불필요하게 잦은 줄바꿈 없이 의미 단위로 1\~2줄에 자연스럽게
        배치되도록 한다.
    -   기본값(1280×720px 슬라이드 기준): Title Area 최대 가로 폭 960px,
        제목 텍스트 Pretendard Bold 48px·White. 제목이 유독 길어 이 폭
        안에서 의미 단위 1\~2줄 구성이 어려운 경우에 한해 가독성을
        우선해 폭 또는 크기를 조정할 수 있다.
    -   제목 블록과 Brand Block 사이, 제목 블록과 하단 여백 사이에 각각
        독립적인 공간을 확보해 두 요소가 시각적으로 분리되어 보이게 한다.
-   전체 구성은 비대칭(asymmetric) Composition을 기본으로 한다: 정보 요소는
    좌측 상단(Brand Block)과 중앙(Main Title)에만 배치하고, 그 외 영역(특히
    우측·하단)은 배경 이미지가 주가 되는 넓은 Negative Space로 남긴다.
-   표지에서는 본문형 콘텐츠 영역을 별도로 구성하지 않는다.

## Visual Style

-   배경 이미지 위에 COSOLUS 브랜드 컬러 계열의 오버레이를 적용하되, 톤은
    Deep Pine 중심의 어둡고 짙은 표현이 아니라 밝고 저채도인 Teal/Blue-Green
    계열을 기본으로 한다.
-   오버레이를 적용한 뒤에도 배경 이미지의 형태와 디테일(피사체의 윤곽,
    질감 등)이 충분히 인식될 수 있는 노출도를 유지한다. 이미지가 오버레이에
    짙게 묻혀 실루엣 수준으로만 보이는 정도로 어두워지지 않도록 한다.
-   기본 오버레이 레시피: 160deg 방향 선형 그라디언트, Ocean Blue
    rgba(26,106,140,0.55) 0% → Mint rgba(127,200,190,0.30) 50% →
    Cosolus Teal rgba(15,101,91,0.50) 100%. 배경 이미지가 바뀌어도 이
    레시피를 기본값으로 사용하며, Soft Rules에 따라 이미지 밝기·복잡도에
    맞춰 알파값만 미세 조정한다.
-   제목은 배경과 충분한 명도 대비를 확보한다.
-   제목을 가장 강한 시각적 위계로 표현한다.
-   전체적으로 장식적인 요소를 최소화하고 이미지, 브랜드, 제목에
    집중한다.
-   Font Family는 Pretendard 단일 서체를 사용한다(Hard Rule 준수). Font
    Size·Weight·Color 등 세부 값은 `Claude_PPT_Design_System.md`의
    Typography System을 따른다.

## Soft Rules

-   배경 이미지는 다음 우선순위에 따라 확보한다.
    1.  사용자가 현재 작업에서 직접 제공한 이미지 (최우선 사용)
    2.  `docs/brand-assets/cover-images/`(COSOLUS 표지용 Background
        Image Library)에 등록된 이미지 중 발표 주제와 적합한 이미지
    3.  위 두 경우에 적합한 이미지가 없으면, `Claude_PPT_Design_System.md`
        기준에 따른 COSOLUS 브랜드 컬러 기반 단색 배경을 대체안으로
        사용한다.
    -   `docs/brand-assets/cover-images/`에서 이미지를 선택할 때는
        각 이미지 파일을 매번 전부 열어 분석하지 않고, 우선
        `docs/brand-assets/README.md`에 정리된 파일명·권장 사용
        주제 설명을 참고해 발표 주제와 가장 적합한 이미지를
        선택한다.
    -   웹 이미지 검색은 기본적으로 수행하지 않는다. 사용자가
        프롬프트에서 웹 이미지 검색을 명시적으로 요청한 경우에만
        예외적으로 사용하며, 이 경우 다음 기준을 적용한다: 발표
        주제와 직접적으로 관련된 이미지 우선, 기업·B2B·화학소재·기술
        발표에 적합한 전문적인 이미지, 충분한 해상도, 워터마크·타사
        로고·과도한 텍스트 없음, 제목·로고 배치 영역의 가독성 고려,
        `Claude_PPT_Design_System.md`의 Image Treatment 기준 적용.
-   이미지 밝기와 복잡도에 따라 오버레이의 농도를 유연하게 조절할 수
    있다. 다만 기본값은 Reference 수준의 밝고 저채도인 톤을 기준으로
    하며, Deep Pine 중심의 어둡고 짙은 오버레이를 기본값으로 사용하지
    않는다.
-   제목의 가독성이 최우선이며, 배경 이미지가 제목보다 강하게 보이지
    않도록 조정한다.
-   제목이 긴 경우 의미 단위를 기준으로 자연스럽게 줄바꿈한다.
-   제목은 가능하면 2줄 이내로 구성한다.
-   부제목은 필요한 경우에만 사용한다.
-   날짜, 발표자, 불필요한 설명 등은 목적상 필요한 경우에만 추가한다.
-   표지에 과도한 정보를 배치하지 않는다.
-   충분한 여백을 확보하여 간결하고 전문적인 인상을 유지한다.

## Additional Rules

-   표지에는 페이지 번호를 표시하지 않는다.
-   사용자 제공 이미지와 `docs/brand-assets/cover-images/` 모두에서
    적합한 배경 이미지를 확보하지 못한 경우(웹 검색을 명시적으로
    요청받아 사용한 경우 포함)에만 COSOLUS Brand Color 기반의 단색
    배경을 대체안으로 사용할 수 있다.

## Avoid

-   제목 뒤에 복잡한 이미지 요소가 직접 겹쳐 가독성을 떨어뜨리는 구성
-   제목을 3줄 이상으로 과도하게 분할하는 구성
-   여러 종류의 강조색을 동시에 사용하는 구성
-   불필요한 카드, 아이콘, 도형 등의 추가
-   PPT 주제와 관계없는 장식용 이미지 사용
