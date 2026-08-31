# Product / Application Layout

> teammate-version(`product-application-layout.md`)을 원본으로 검토 후,
> 이 프로젝트에서 확정된 Hard Rule §9/§12·Claude PPT Design System §3/§5 기준에
> 맞춰 보정해 등록한다(2026-08-19). 원본에 있던 공통 Header 수치 중복 정의를
> 제거하고 참조로 전환했으며, Typography·Main Title Supporting Message·Content
> Relationship/Region Composition·Parallel Layout Alignment 항목을 추가로
> 반영했다. Layout A/B 선택 로직, 방사형 좌표 값 등 이 레이아웃 고유의 구조적
> 판단은 원본 그대로 유지한다.

대표 제품 또는 솔루션과 적용 분야를 한 페이지에서 설명하기 위한 Layout
MD다. 동일한 콘텐츠 유형에 대해 아래 두 가지 레이아웃을 지원한다.

- Layout A --- Grid형: 제품과 복수의 적용 사례를 정돈된 목록으로 제시
- Layout B --- 방사형: 하나의 핵심 제품이 여러 산업·용도로 확장되는
  관계를 시각화

### Use When

- 대표 제품/소재/플랫폼/기술과 그 적용 분야·고객군·Use Case를 한 슬라이드
  에서 `제품 → 적용처` 관계로 보여줘야 하는 경우

### Do Not Use When

- 제품 자체의 세부 성능·스펙 비교가 핵심인 경우 → Table Comparison
  (`table-comparison.md`) 또는 Comparison Matrix
  (`comparison-matrix.md`)
- 적용처 사이에 단계·시간 순서·인과관계가 있는 경우 → Process / System
  Architecture Layout(`process-system-architecture-layout.md`) 또는
  `timeline-company-milestone.md`

---

## 0. 적용 원칙

- 공통 Header, Logo, 브랜드 컬러, 기본 폰트 패밀리, 페이지 번호 등은 Hard
  Rule([`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`](../design-hard-rules/2026.08.12_design_hard-rules_V2.md))을
  그대로 따른다. 본 문서는 위치·색상 수치를 재정의하지 않는다.
- **Main Title Supporting Message(Hard Rule §12)**: 이 Layout은 자체
  부제목 요소를 두지 않으므로 §12의 기본 적용 규칙을 그대로 따른다 —
  원본 콘텐츠에 근거한 1~2줄 Supporting Message를 기본 배치하고, §12의
  예외 조건에 해당할 때만 생략한다. Supporting Message 사용 시 본문 시작
  Y는 §12 기준(`.body-box.with-support`)으로 확장된다.
- 색상 값(Primary/Dark·Main/Secondary/Light, Ink/Slate/Gray, Line, Mist
  등)은 Hard Rule §5 Brand Color 및
  [`docs/design-system/Claude_PPT_Design_System.md`](../design-system/Claude_PPT_Design_System.md)
  §2 Color System을 그대로 따른다. 본 문서에서는 값을 재정의하지 않으며,
  이 Layout에서만 적용되는 사용 규칙만 아래에 남긴다.
  - 핵심 제품 및 자사 요소는 Primary 계열을, 일반 제목·본문은 Ink를,
    보조 설명은 Slate 또는 Gray를 사용한다.
  - 강조는 Font Weight를 먼저 적용하고 필요한 경우 Main Color를
    추가한다(Hard Rule §5 강조 우선순위).
  - 산업마다 임의로 서로 다른 색을 부여하지 않는다.
  - 방사형 연결선은 Primary 또는 Secondary 계열 한 가지 색으로
    통일한다.

### 이미지 및 품질

- 모든 이미지의 비율을 유지하고 각 프레임 안에서 Crop한다(Design System
  §7 Image Treatment).
- 같은 슬라이드의 적용 분야 이미지는 유사한 밝기, 채도, 촬영 톤으로
  통일한다.
- 제품과 적용처를 혼동할 수 있는 장식용 이미지는 사용하지 않는다.
- 텍스트, 이미지, 연결선 간 의도하지 않은 겹침을 금지한다(Hard Rule §8).
- 연결선은 이미지와 텍스트보다 뒤에 배치한다.
- 요소가 슬라이드 밖으로 잘리거나 텍스트가 박스를 초과하지 않도록 한다.

---

## 1. Layout 목적

다음 콘텐츠를 시각적으로 연결한다.

- 중심 대상: 대표 제품, 소재, 플랫폼, 기술 또는 솔루션
- 외부 대상: 산업 분야, 고객군, 사용 환경, 응용 제품 또는 Use Case
- 핵심 메시지: 제품이 무엇인지와 실제로 어디에 활용되는지를 한눈에 전달

이 Layout은 제품 자체의 세부 성능 비교보다 `제품 → 적용처` 관계를
보여주는 데 적합하다.

---

## 2. Content Relationship / Region Composition 매핑

Claude_PPT_Design_System.md §5의 "Content Relationship / Region
Composition 원칙"을 이 Layout의 콘텐츠에 적용하면 다음과 같다.

- **Primary Content**: 중심 제품(하나의 대표 대상) — Layout A의 Product
  Hero, Layout B의 중앙 Product Hub.
- **Dependent Content**: 각 적용 분야 Item/Node — 중심 제품 하나를
  보완·확장 설명하는 정보이므로 별도 Supporting Region으로 분리하지
  않고, 중심 제품과 같은 Main Content Group 안에서 대등한 반복 요소로
  배치한다.
- 이 Layout에는 별도의 Conclusion/Takeaway 통합 영역을 기본으로 두지
  않는다 — `제품 → 적용처` 관계 자체가 메시지이며, 필요한 경우에만 §5.5·
  §6.7의 시선 흐름 마지막에 짧은 요약을 덧붙일 수 있다.

Application Item(Layout A) / Application Node(Layout B)는 동일 계층의
병렬 반복 요소이므로, 아래 §5·§6의 "모든 항목/원의 폭·높이·이미지 비율
동일" 규칙은 Design System §5 "Parallel Layout Alignment 원칙"(동일
Width/Height, 동일 Gap, 대응 요소 정렬)을 이 Layout에 적용한 것이다.

---

## 3. 레이아웃 자동 선택 규칙

레이아웃은 항목 수가 아니라 `중심 대상과 적용처 사이의 의미 관계`를
우선 기준으로 선택한다.

### 3.1 Layout B --- 방사형을 선택하는 경우

다음 조건 중 하나 이상이 명확하면 방사형을 우선 선택한다.

- 하나의 제품·소재·기술이 여러 산업 분야로 파생되거나 확장되는 구조
- 동일한 핵심 소재가 서로 다른 최종 제품에 공통으로 도입되는 구조
- 중심 기술 또는 플랫폼에서 여러 Use Case가 발생하는 Hub-and-Spoke 관계
- `기반`, `확장`, `파생`, `적용 분야`, `다양한 산업에 적용`, `산업
  전반으로 확대`가 핵심 메시지인 경우
- 모든 적용처가 하나의 중심 제품과 직접 연결되며 적용처끼리는 상하
  관계가 없는 경우

예시:

- 난연 마스터배치 → 전기·전자 / 자동차 / 건축자재 / 배터리 부품
- 핵심 분리 소재 → 양극재 회수 / 음극재 회수 / 폐수 처리 / 공정 재사용
- 분석 플랫폼 → 품질관리 / 공정 최적화 / 연구개발 / 고객 대응

### 3.2 Layout A --- Grid형을 선택하는 경우

다음 조건에서는 Grid형을 우선 선택한다.

- 제품과 각 적용 사례를 개별적으로 자세히 소개해야 하는 경우
- 적용처별로 이미지와 1~2줄 설명을 안정적으로 읽게 하는 것이 중요한 경우
- 적용 분야가 서로 독립적인 사례 목록이며 확산 관계를 강조할 필요가
  없는 경우
- 특정 고객, 프로젝트, 산업, 사용 시나리오별 차이를 비교하거나 나열하는
  경우
- 중심 제품보다 적용 사례의 정보량과 가독성이 더 중요한 경우

예시:

- 대표 장비 1종 + 고객 적용 사례 4건
- 플랫폼 소개 + 산업별 도입 사례와 성과
- 제품 사진 + 사용 환경별 간단한 설명

### 3.3 선택 우선순위

1. `하나의 중심 제품에서 여러 산업으로 뻗어나가는 의미`가 있으면 방사형을
   선택한다.
2. 의미 관계가 불분명하고 사례를 균등하게 나열해야 하면 Grid형을
   선택한다.
3. 적용처별 설명이 길어 방사형에서 가독성이 떨어지면 Grid형으로
   전환한다.
4. 사용자가 특정 구조를 명시하면 해당 구조를 우선한다.
5. 두 구조가 모두 가능하지만 목적이 불명확하면 기본값은 Grid형으로
   한다.

### 3.4 선택 금지 사례

- 제품이 여러 개이고 각각 별도의 적용 분야를 갖는 경우 방사형 하나에
  모두 넣지 않는다.
- 적용처 사이에 단계, 시간 순서 또는 인과관계가 있으면 방사형 대신
  Process/Flow Layout을 사용한다.
- 적용처별 정량 비교가 목적이면 Comparison/Table/Chart Layout을
  사용한다.
- 중심 대상 없이 독립 항목만 존재하면 방사형을 사용하지 않는다.

---

## 4. 공통 콘텐츠 구조

### 필수 정보

- Section Label: 기본값 `PRODUCT`(값·위치는 Hard Rule §9 고정)
- Main Title: 슬라이드 내용을 직접 설명하는 1줄 제목(Hard Rule §9)
- (기본 적용) Main Title Supporting Message: §0 참조
- 중심 제품명 또는 솔루션명
- 중심 제품 이미지 1개
- 적용 분야 3~6개
- 적용 분야별 대표 이미지 1개
- 적용 분야별 제목

### 선택 정보

- 중심 제품 한 줄 설명
- 적용 분야별 짧은 보조 설명
- 소재 종류, 대상 수지, 핵심 기능 등의 짧은 Spec Line

### 4-1. Typography

새 Font Size를 정의하지 않고 Claude PPT Design System §3 Typography
표의 기존 역할을 그대로 매핑한다(Weight는 Hard Rule §2에 따라 자유롭게
조정 가능, 아래 표는 최소 크기 기준).

| 요소 | Design System 역할 | 크기 |
|---|---|---|
| 중심 제품명 | Content Header (H2) | 20pt |
| 중심 제품 보조 설명 | Explanation | 18pt |
| 적용 분야 제목(Item/Node) | Body | 16pt |
| 적용 분야 보조 설명 | Body | 16pt(공간 부족을 이유로 14pt 미만으로 축소 금지) |
| Spec Line(선택) | Caption / Auxiliary | 14pt |

### 텍스트 제한

- 중심 제품명: 1줄 권장, 최대 2줄
- 중심 제품 보조 설명: 1줄
- 적용 분야 제목: 1줄 권장
- 적용 분야 보조 설명: 1줄 권장, 최대 2줄
- 긴 문장, 문단, 세부 수치 표는 사용하지 않는다.
- 텍스트가 많아지면 폰트를 축소하지 말고(§4-1 Typography 최소 크기 유지)
  Grid형으로 전환하거나 내용을 줄인다.

---

## 5. Layout A --- Grid형

> **Design System §6 준수**: `Claude_PPT_Design_System.md` §6은 Card(배경
> Fill·Border·Rounded Corner로 감싸는 컨테이너) 사용을 원칙적으로 금지하며,
> Named Exception은 `021_business-site-map.md`의 단일 Pin 부속 Card,
> `019_competitive-advantage-highlight.md`의 자사 열 강조 Card 2개뿐이다
> (2026-08-21 개정 — 이전에는 이 문서(Layout A)도 예외로 인정됐으나, 병렬
> Region 구분에 Card 자체를 쓰지 않는 쪽으로 정책이 바뀌면서 예외에서
> 제외됨). 따라서 이 Layout도 다른 Layout과 동일하게 Card 없이 구성하며,
> 적용 분야 항목 간 구분은 [5.4](#54-application-item-parallel-layout-alignment-적용)의
> 얇은 Line(0.5~1px)과 Gap만으로 표현한다.

### 5.1 사용 목적

좌측에서 대표 제품을 먼저 인지시킨 뒤, 우측에서 여러 적용 사례를
순서대로 탐색하게 하는 구성이다. 적용 사례별 이미지와 설명의 독립적인
가독성을 확보하는 데 유리하다.

### 5.2 기본 구성

- Content Area 시작 Y는 Hard Rule §9(Supporting Message 미사용 시
  Y=135px) 또는 §12(`with-support`, 사용 시 확장)를 따르며, 이 Layout은
  그 아래 약 10~15px의 여유를 추가로 둘 수 있다. X 범위는 Hard Rule
  §9와 동일하게 X=64~1216px를 사용한다.
- 좌측 Product Hero 영역: 전체 본문 폭의 약 34~38%
- 우측 Application 영역: 전체 본문 폭의 약 58~62%
- 두 영역 사이 Gap: 약 32~44px
- 좌측에는 큰 제품 이미지 1개와 제품명·보조 설명을 배치한다.
- 우측에는 적용 분야를 2×2 Grid로 배치한다.
- 적용 분야가 3개이면 1×3 또는 균형 잡힌 삼각 배치를 사용할 수 있으나
  항목 크기는 동일하게 유지한다.
- 적용 분야가 5~6개이면 3×2 Grid를 사용하고 텍스트를 축약한다.

### 5.3 Product Hero

- 시각적 우선순위가 가장 높아야 한다.
- 세로형 또는 정방형에 가까운 큰 이미지 프레임을 사용한다.
- 제품 이미지가 프레임의 중심을 차지하도록 Crop한다.
- 제품명은 이미지 하단 또는 프레임 바로 아래에 배치한다.
- 제품명은 §4-1 Typography(Content Header 20pt) 기준, Weight는 Bold~
  ExtraBold, 색상은 Ink 또는 Dark/Main을 사용한다.
- 보조 설명은 제품명 아래 1줄로 배치하고 §4-1 Typography(Explanation
  18pt) 기준, Primary 또는 Slate 색상을 사용한다.

### 5.4 Application Item (Parallel Layout Alignment 적용)

- 모든 항목의 폭, 높이, 이미지 비율, 제목 위치를 동일하게 한다(동일
  Width/Height, 동일 Top Line).
- 각 Item은 `대표 이미지 → 적용 분야 제목 → 짧은 보조 설명` 순서로
  구성한다.
- 항목 간 Gap을 명확히 확보하며 서로 맞닿지 않게 한다(Gap/Padding 통일).
- Card 컨테이너(배경 Fill·Border·Rounded Corner·그림자로 항목을 감싸는
  것)를 사용하지 않는다(Design System §6 — Card는 Named Exception 2개
  외에는 사용하지 않음).
- White Background 위에 이미지와 텍스트를 직접 정렬하는 Flat 구조를
  사용한다.
- 항목 간 구분은 Line 색상의 0.5~1px 경계만 사용한다(Tint/배경색 Fill로
  구분하지 않음) — 충분한 Gap과 이 얇은 Line만으로 항목 경계를
  표현한다.

### 5.5 시선 흐름

`Main Title → 좌측 핵심 제품 → 우측 상단에서 우측 하단 순서의 적용 분야`

---

## 6. Layout B --- 방사형

### 6.1 사용 목적

하나의 핵심 제품·소재·기술이 여러 산업 또는 사용처로 확장되는 관계를
직관적으로 보여준다. 중심성과 확장성이 핵심 메시지일 때 사용한다.

### 6.2 기본 구성

- Content Area 시작 Y는 §5.2와 동일한 기준(Hard Rule §9 또는 §12)을
  따른다. X 범위는 X=64~1216px.
- 중앙에 가장 큰 원형 Product Hero를 배치한다.
- 적용 분야는 중앙을 둘러싸는 동일 크기의 원형 이미지로 배치한다.
- 중앙 원과 외곽 원을 가는 Solid Line으로 직접 연결한다.
- 연결선은 중앙에서 외곽으로 뻗는 구조여야 하며, 적용처끼리 연결하지
  않는다.
- 중앙 원의 지름은 외곽 원 지름의 약 1.5~1.8배로 설정한다.
- 모든 외곽 원은 중앙에서 시각적으로 동일한 거리감을 유지한다.

### 6.3 적용 분야 개수별 배치

- 3개: 중앙 기준 약 120° 간격의 삼각 방사형
- 4개: 좌상 / 우상 / 좌하 / 우하의 대칭 방사형 --- 권장 기본값
- 5개: 중앙을 둘러싼 오각형 배치
- 6개: 중앙을 둘러싼 육각형 배치
- 7개 이상: 방사형을 사용하지 않고 Grid형 또는 별도 Portfolio Layout으로
  전환

### 6.4 중앙 Product Hero

- 제품 또는 소재를 명확히 식별할 수 있는 실사 이미지를 원형 Crop한다.
- 중앙 원은 슬라이드의 시각적 중심에 배치하되 Header Safe Area와 하단
  캡션 영역을 고려해 수직 위치를 미세 조정할 수 있다.
- 중심 제품명은 중앙 원 바로 아래에 배치한다.
- 제품명은 §4-1 Typography(Content Header 20pt) 기준, Weight는 Bold~
  ExtraBold, 색상은 Ink 또는 Dark/Main을 사용한다.
- Spec Line 또는 한 줄 설명은 제품명 아래에 배치하며 §4-1
  Typography(Explanation 18pt) 기준, Primary 또는 Secondary 색상을
  사용한다.
- 중앙 원에 과도한 다중 테두리나 장식용 Glow를 사용하지 않는다.

### 6.5 외곽 Application Node (Parallel Layout Alignment 적용)

- 모든 외곽 원은 동일한 크기와 동일한 이미지 처리 방식을 사용한다(동일
  Width/Height).
- 각 원 아래에 `적용 분야 제목 → 보조 설명` 순서로 배치한다(§4-1
  Typography: 제목·보조 설명 모두 Body 16pt).
- 제목은 Weight SemiBold~Bold, Ink 색상을 사용한다.
- 보조 설명은 Slate 또는 Primary 색상을 사용한다.
- 원형 이미지와 캡션은 하나의 시각 Group으로 취급한다(Content Density —
  Group 내부는 좁게).
- 상단 Node의 캡션이 중앙 원 또는 연결선을 침범하지 않도록 충분한 간격을
  확보한다.
- 하단 Node의 캡션이 페이지 번호 또는 하단 Safe Margin을 침범하지
  않도록 한다.

### 6.6 연결선

- Color: Primary 또는 Secondary 중 한 가지(값은 Hard Rule §5 팔레트
  참조).
- Width: 약 1~1.5px
- Style: Solid
- Arrowhead: 기본적으로 사용하지 않는다.
- 방향성을 반드시 강조해야 할 때만 중앙에서 외곽을 향하는 작은
  Arrowhead를 허용한다.
- 선은 각 원의 중심점이 아니라 원의 외곽 경계에서 끝나는 것처럼 보이게
  한다.
- 연결선은 모든 원형 이미지와 텍스트 뒤에 배치한다.
- 선이 캡션을 가로지르지 않도록 한다.

### 6.7 시선 흐름

`Main Title → 중앙 핵심 제품 → 연결선 → 주변 산업별 적용 분야`

### 6.8 방사형 금지 표현

- 외곽 Node마다 무관한 색상을 부여하는 표현
- 중앙 원과 외곽 원의 크기 차이가 거의 없는 표현
- 연결선이 서로 교차하거나 적용처끼리 연결되는 표현
- 원형 이미지 주변에 두꺼운 장식 Ring을 반복하는 표현
- 중앙 제품보다 외곽 이미지가 더 강하게 보이는 표현
- 단순 장식 목적으로 불필요한 아이콘, 화살표, 점선을 추가하는 표현

### 6.9 검증된 기본 좌표 (4개 Node 기준, 1280×720)

아래 좌표는 원본(teammate-version)에서 실제 HTML 렌더링으로 겹침·여백을
검증한 기본값이며, Content Area(X=64~1216, Y=145~670) 내부 상대 좌표
(원점 X=64, Y=145) 기준이다. Supporting Message(Hard Rule §12) 사용
여부에 따라 Content Area의 실제 시작 Y는 §6.2 기준대로 조정되므로, 이
좌표는 원점(§6.2에서 정한 실제 Y 시작값) 기준 상대 오프셋으로 재해석해
사용한다. 항목 수·텍스트 길이가 달라지면 비율(§6.2~§6.3)을 유지한 채 이
값을 기준으로 조정한다.

- 중앙 Hub: 지름 180px, 중심 좌표 (576, 205) --- 슬라이드 절대 좌표로는
  (640, 350)
- 외곽 Node: 지름 108px(중앙 대비 1.67배), 중심에서 가로 ±270px·세로
  ±135px 대칭 배치
  - 좌상 중심 (306, 70) / 우상 중심 (846, 70)
  - 좌하 중심 (306, 340) / 우하 중심 (846, 340)
- Hub 하단 캡션(제품명+보조설명) 박스: 폭 360px, 상단 Y=301(Hub 하단
  경계에서 6px 아래)
- Node 하단 캡션(제목+보조설명 2줄) 박스: Node 하단 경계에서 10px 아래,
  폭 170px(2줄 텍스트 줄바꿈 여유 확보를 위해 Node 지름보다 넉넉하게)
- 연결선: Hub 중심 → 각 Node 중심을 직선으로 연결하고 z-index를 원·
  텍스트보다 아래에 둔다(원이 선 끝을 가려 외곽 경계에서 끝나는 것처럼
  보이게 하는 방식)
- 핵심 메시지/Insight 한 줄을 하단에 추가할 경우, 가장 아래 Node
  캡션의 최대(줄바꿈 포함) 예상 높이 기준으로 최소 70~90px 아래에
  배치해 겹침을 방지한다

**주의**: 좌표는 반드시 Content Area 원점(§6.2에서 정한 X, Y) 기준
상대값으로 계산한다. 슬라이드 절대 중심(X=640)을 그대로 쓰면 Header/
여백 offset만큼 우측으로 쏠린다.

---

## 7. 이미지 선택 규칙

- 중심 이미지는 원료·제품·소재의 실물을 우선 사용한다.
- 적용 분야 이미지는 제품이 실제로 사용되는 부품, 설비, 환경을 보여준다.
- 지나치게 넓은 산업 전경보다 적용 위치를 인지할 수 있는 중근거리
  이미지를 우선한다.
- 적용 분야 이미지가 제품의 실제 적용을 오해하게 만들 수 있으면 상징
  이미지 대신 정확한 부품 이미지를 사용한다.
- 등록된 공식 제품 사진이 있으면 생성 이미지보다 공식 사진을 우선한다.
- 실제 고객사, 실제 제품 또는 공식 인증을 암시하는 가짜 이미지·로고·UI를
  생성하지 않는다.

---

## 8. 콘텐츠 변환 예시

### 입력 콘텐츠

- 중심 제품: 할로겐프리 난연 마스터배치
- 대상 수지: PA6, PP, PE
- 적용 분야: 전기·전자 부품, 자동차 부품, 건축·산업 자재, 배터리 부품
- 전달 의도: 하나의 난연 소재가 여러 산업 분야에 공통 적용됨

### 자동 판단

- 중심 대상이 1개다.
- 4개 산업이 중심 제품에서 직접 파생된다.
- 산업 간 순서나 비교 관계가 없다.
- 핵심 메시지가 확장성과 범용성이다.

따라서 `Layout B --- 방사형`을 선택한다.

### Grid형으로 전환되는 예

각 산업별 적용 제품명, 고객 요구사항, 적용 효과 등 별도 설명이 2줄
이상 필요하면 방사형의 가독성이 저하된다. 이 경우 동일 콘텐츠라도
`Layout A --- Grid형`으로 전환한다.

---

## 9. AI 제작 지시문

```text
입력된 제품과 적용 분야의 의미 관계를 먼저 분석한다.

하나의 제품·소재·기술이 여러 산업 또는 사용처로 파생·확장되는 Hub-and-Spoke 관계라면 Layout B(방사형)를 사용한다. 중앙에 핵심 제품을 배치하고, 동일 크기의 적용 분야 Node를 주변에 배치한 뒤 중앙에서 각 Node로 연결선을 뻗는다.

적용 사례를 독립적으로 나열하거나 사례별 이미지와 설명의 가독성이 더 중요하다면 Layout A(Grid형)를 사용한다. 좌측에 핵심 제품을 크게 배치하고 우측에 적용 분야를 균등한 Grid로 배치한다.

관계가 불분명하면 Grid형을 기본값으로 사용한다. 적용 분야별 설명이 길어 방사형에서 가독성이 저하되면 Grid형으로 전환한다. 두 Layout을 한 슬라이드 안에 혼합하지 않는다.

Main Title 아래에는 Hard Rule §12 기준 Supporting Message를 기본 배치하고(예외 조건에 해당할 때만 생략), 텍스트 크기는 이 문서 §4-1 Typography 표를 따른다.

모든 경우 공통 Header System, Pretendard Font, Brand Color, Safe Area 및 이미지 비율 규칙은 Hard Rule을 우선 적용한다.
```

---

## 10. 최종 검수 체크리스트

- [ ] 중심 대상이 제품·소재·기술 중 하나로 명확한가?
- [ ] 제품과 적용처의 의미 관계에 따라 Grid형 또는 방사형을 선택했는가?
- [ ] 중심에서 여러 산업으로 확장되는 관계라면 방사형을 우선 적용했는가?
- [ ] 적용처별 설명이 길면 Grid형으로 전환했는가?
- [ ] 두 Layout을 한 슬라이드 안에 혼합하지 않았는가?
- [ ] 공통 Header System의 위치·크기·색상을 유지했는가?
- [ ] 모든 본문 요소가 Hard Rule §9(또는 Supporting Message 사용 시 §12)
      기준 Header Safe Area 아래에 있는가?
- [ ] Main Title Supporting Message(Hard Rule §12)를 기본 적용했거나,
      예외 조건에 해당함을 확인했는가?
- [ ] §4-1 Typography 표의 최소 크기(Body 16pt 등)를 지켰는가?
- [ ] Pretendard 외 폰트를 사용하지 않았는가?
- [ ] Brand Color 외 임의 색상 사용을 최소화했는가?
- [ ] 중심 제품의 시각적 우선순위가 가장 높은가?
- [ ] 이미지 비율 왜곡, 텍스트 Overflow, 의도하지 않은 겹침이 없는가?
- [ ] 연결선이 이미지와 텍스트 뒤에 있으며 캡션을 가로지르지 않는가?
- [ ] 공식 CI를 텍스트로 재현하거나 변형하지 않았는가?
- [ ] 페이지 번호가 단독 숫자 형식으로 표시되었는가?
