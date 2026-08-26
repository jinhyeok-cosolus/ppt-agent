# 14페이지 --- 핵심기술 좌우 비교형 레이아웃

> 핵심 소재/제품의 정량 성능과 후속 공정·시스템 기술을 한 화면에서
> 병렬로 설명하는 기술 슬라이드. 이 레이아웃의 가장 중요한 시각적 특징은
> 제목 바로 아래에 배치되는 **전폭 Summary Bar**와, 그 아래 좌·우 기술
> 영역을 동일한 컬러 체계로 묶는 구조이다.

------------------------------------------------------------------------

## 0. 적용 원칙

-   공통 Header, Logo, 제목 위치, 기본 폰트 패밀리, 페이지 번호 등은
    Hard Rule을 따른다.
-   본 MD는 14페이지 고유의 콘텐츠 구조와 시각적 표현 방식을 정의한다.
-   기본 구조는
    `상단 Summary Bar → 좌/우 Section Title → 좌측 정량 Table → 우측 Process Diagram`
    순서이다.
-   좌측과 우측은 표현 형식이 달라도 동일한 슬라이드 안의 하나의 기술
    체계로 보이도록 색상과 정렬 기준을 통일한다.

------------------------------------------------------------------------

## 1. 핵심 Layout Identity

이 레이아웃의 핵심 조합은 다음과 같다.

`Full-width Summary Bar + Two Technology Sections + Table/Data + Process Diagram`

특히 **Summary Bar는 선택 요소가 아니라 이 레이아웃의 필수 요소**이다.

Summary Bar가 누락되거나 일반 텍스트 한 줄로 대체되면 본 레이아웃의
디자인 Identity가 훼손된 것으로 판단한다.

------------------------------------------------------------------------

## 2. 상단 Summary Bar --- 필수

### 구조

메인 제목 바로 아래에 슬라이드 콘텐츠 폭을 거의 전부 사용하는 가로형
Bar를 배치한다.

원본 기준 위치 비율: - X: 약 3.2% - Y: 약 19.9% - W: 약 94.1% - H: 약
7.5%

Bar 내부에는 슬라이드 전체의 핵심 결론 또는 성과를 한 문장으로 배치한다.

예:
`COSOLUS 화학구조 설계, 정제, 공정 기술 → 재자원화율(>90%), 공정비용(<5,500원/kg)`

### Bar Color

-   Fill: `#F4FAFA`
-   Border / Rule: `#478689`
-   Text: 기본 Ink 계열을 사용하되 핵심 기술·수치는 Hard Rule의 강조
    체계를 따른다.

### 형태

-   직사각형
-   둥근 모서리 사용 금지
-   Shadow 금지
-   Gradient 금지
-   과도한 테두리 금지
-   상·하단의 얇은 Teal Rule을 사용하여 Bar 영역을 명확하게 구분한다.

### Hard Requirement

-   Summary Bar는 반드시 메인 제목과 본문 영역 사이에 위치한다.
-   Bar는 좌측 Table 영역에만 걸치지 않고 **좌·우 콘텐츠 전체를 하나로
    묶는 전폭 요소**로 사용한다.
-   Bar Fill은 반드시 `#F4FAFA`를 사용한다.
-   Bar 경계선은 `#478689` 계열을 사용한다.
-   유사한 회색·민트색으로 임의 변경하지 않는다.

------------------------------------------------------------------------

## 3. Two-Section Composition

Summary Bar 아래 콘텐츠를 좌측과 우측 두 영역으로 나눈다.

### 좌측

정량 성능 / 제품 / 소재 / 실험 결과

### 우측

공정 / 시스템 / 센서 / AI / 작동 원리

두 영역의 폭은 콘텐츠에 따라 소폭 조정할 수 있으나 기본적으로 균형 있는
2-column 구성을 유지한다.

원본처럼 중앙에 얇은 Vertical Divider를 사용할 수 있다.

Divider: - Thin Line - Teal 계열 - 장식적 강조 금지

### 좌우 모듈 하단 인사이트 (선택)

콘텐츠 분량에 따라 좌·우 모듈 하단에 각각 1~2줄의 짧은 분석/인사이트
문장을 추가할 수 있다.

-   좌측 모듈: `Section Title → Table/Data → 인사이트 1~2줄`
-   우측 모듈: `Section Title → Diagram → 인사이트 1~2줄`
-   좌·우가 동일한 3단 구조(제목 → 핵심 콘텐츠 → 인사이트)를 따르면,
    두 영역이 표현 형식은 달라도 유사한 성질의 것을 나란히 비교하는
    한 쌍의 패널로 읽힌다.
-   인사이트 문장은 이미 제시된 수치·데이터를 해석한 결론이며, 새로운
    수치나 사실을 임의로 추가하지 않는다.
-   Summary Bar와 달리 필수 요소는 아니다 — 인사이트가 불필요한
    콘텐츠라면 생략한다.

------------------------------------------------------------------------

## 4. Section Title

좌·우 영역 상단에는 각각 독립적인 Section Title을 배치한다.

예:

`핵심소재 (재자원화율 3% → 50%)`

`분리막 & THz 기술 (리튬 재자원화율 3% → 90%)`

### Color

Section Title의 기본 색상은 원본과 동일하게:

`#034443`

을 사용한다.

-   좌측과 우측 제목은 동일 색상 사용
-   한쪽만 임의로 다른 Accent Color 사용 금지
-   핵심 수치도 동일한 Title Color 체계 안에서 표현한다.

### 배치

-   좌·우 Section Title의 수직 시작점을 최대한 일치시킨다.
-   각 제목은 자신이 담당하는 콘텐츠 영역의 중심 또는 좌측 기준에 맞춰
    정렬할 수 있다.
-   제목과 실제 Table/Diagram 사이에는 충분한 White Space를 확보한다.

------------------------------------------------------------------------

## 5. Left Module --- Quantitative Table

좌측은 정량적 성능 또는 제품 데이터를 보여주는 Table/Data 영역을
기본으로 한다.

### 기본 구조

  구분       제품/기술명
  ---------- ----------------------
  평가항목   Chart / Image / Data

원본처럼 첫 번째 열은 항목명, 두 번째 열은 실제 제품·데이터 영역으로
사용한다.

### Table Style

-   White Background
-   불필요한 Cell Fill 최소화
-   외곽선과 주요 구분선 중심의 Minimal Table
-   굵고 복잡한 Grid 사용 금지
-   데이터 시각화가 있는 경우 Table 내부에 Chart/Image 삽입 가능

### Table Header

중요: Table Header 자체를 강한 색상 박스로 만들지 않는다.

상단 Summary Bar가 이미 슬라이드의 주요 강조 요소이므로, Table은 최대한
절제된 선형 구조로 유지한다.

### 콘텐츠

다음 요소를 삽입할 수 있다.

-   Line Chart
-   Scatter Plot
-   성능 그래프
-   실험 결과 이미지
-   제품 이미지
-   정량 수치

표 내부 시각자료가 핵심 정보일 경우 충분한 크기를 확보한다.

------------------------------------------------------------------------

## 6. Right Module --- Process / Technology Diagram

우측은 기술 작동 원리 또는 공정 흐름을 설명하는 Diagram 영역이다.

기본 흐름:

`Input → Separation / Core Technology → Output → Diagnosis / AI`

### 구성 원칙

-   프로세스는 좌 → 우 방향으로 읽히도록 구성
-   Input과 Output 영역은 명확하게 구분
-   핵심 기술 영역은 중앙에 배치
-   최종 진단/AI 영역은 우측 끝에 배치
-   화살표 또는 이온 이동 등 필요한 정보만 표시

### Diagram Color Palette

원본 14페이지의 Process Diagram은 다음 색상 계열을 사용한다.

Primary / Structural: - Deep Teal: `#034443` - Teal: `#478689` - Green:
`#43A047`, `#4CAF50`

Blue System: - Blue: `#42A5F5` - Dark Blue: `#1565C0` - Light Blue
Background: `#E3F2FD` - Indigo: `#3F51B5` - Violet: `#5E35B1`

Neutral: - Dark: `#263238` - Gray: `#78909C` - Light Gray: `#B0BEC5`,
`#CFD8DC`

필요한 물질 또는 상태 구분에 한해 Orange/Purple 등 보조색을 제한적으로
사용할 수 있다.

색상은 의미 없이 장식적으로 추가하지 않는다.

------------------------------------------------------------------------

## 7. Color Consistency Rule

이 레이아웃에서는 색상 일치가 중요하다.

### 반드시 유지할 색상

  Element                     Color
  --------------------------- -----------------------
  Summary Bar Fill            `#F4FAFA`
  Summary Bar Border / Rule   `#478689`
  Section Title               `#034443`
  Main Teal Diagram Element   `#478689`
  Primary Blue Data Element   `#42A5F5`
  Dark Blue Highlight         `#1565C0`
  Dark Process Panel          `#263238`
  Positive/Active Status      `#43A047` / `#4CAF50`

AI가 임의로 새로운 메인 컬러 팔레트를 생성하지 않는다.

콘텐츠 특성상 추가 색상이 필요한 경우에도 기존 Teal / Blue / Green
체계를 우선 사용한다.

------------------------------------------------------------------------

## 8. Visual Hierarchy

시각적 우선순위는 다음과 같다.

1.  Main Title
2.  Full-width Summary Bar
3.  Left / Right Section Title
4.  핵심 Chart 또는 Process Diagram
5.  Table Label / Diagram Label
6.  Footnote / Source

Summary Bar는 제목 다음으로 강한 정보 계층을 갖는다.

단, Bar 자체를 진한 색으로 채우기보다 밝은 Mint Background + Teal Rule을
사용하여 절제된 강조를 유지한다.

------------------------------------------------------------------------

## 9. Content Adaptation

좌측과 우측 콘텐츠는 반드시 원본과 동일한 종류일 필요는 없다.

### 좌측 대체 가능 콘텐츠

-   제품 비교 Table
-   성능 Chart
-   실험 결과
-   KPI
-   Before / After Data

### 우측 대체 가능 콘텐츠

-   Process Diagram
-   Technology Mechanism
-   Workflow
-   System Architecture
-   단계별 공정
-   AI / Sensor Monitoring Panel

즉, 구체적인 콘텐츠 표현 방식에는 자율성을 허용한다.

단 다음 구조는 유지한다.

`Summary Bar → Two Section Titles → Left Data Module + Right Visual Module`

------------------------------------------------------------------------

## 10. Density Adaptation

콘텐츠가 많을 경우 다음 순서로 조정한다.

1.  부가 설명 축약
2.  Footnote 최소화
3.  Diagram 내부 Label 축약
4.  Table 행 수 조정
5.  좌·우 Column 폭 조정
6.  Chart / Diagram 크기 재조정

Summary Bar를 삭제하거나 축소하여 공간을 확보하지 않는다.

본문을 억지로 삽입하기 위해 전체 글자 크기를 과도하게 축소하지 않는다.

------------------------------------------------------------------------

## 11. Avoid

-   Summary Bar 삭제
-   Summary Bar를 일반 텍스트로 대체
-   Summary Bar 색상을 진한 Teal로 변경
-   Section Title마다 서로 다른 색 사용
-   Table Header에 과도한 Fill 사용
-   좌우 영역을 각각 독립적인 Card Box로 감싸는 구성
-   과도한 Rounded Rectangle
-   Shadow 남용
-   Gradient 남용
-   Diagram 색상을 임의의 Rainbow Palette로 변경
-   중앙 Divider보다 강한 장식선 사용

------------------------------------------------------------------------

## 12. Soft Rule

하나의 핵심기술을 `정량적 성능 + 작동 원리/공정`의 두 관점으로 동시에
설명해야 할 경우 이 레이아웃을 우선적으로 검토한다.

좌측과 우측의 구체적인 시각화 방식은 콘텐츠 전달 효과에 따라 자유롭게
선택할 수 있다.

단, 상단 Summary Bar와 좌·우 Section 구조는 유지하여 원본 슬라이드의
시각적 정체성을 보존한다.

------------------------------------------------------------------------

## 13. Layout Identity

이 레이아웃의 핵심 Identity:

`Full-width Pale Mint Summary Bar + Dark Teal Section Titles + Minimal Data Table + Technical Process Diagram`

특히 다음 두 요소는 최우선 보존 대상이다.

1.  제목 아래 전폭 Summary Bar
2.  `#F4FAFA / #478689 / #034443` 기반의 색상 일치

이 두 요소가 유지되지 않으면 다른 레이아웃으로 판단한다.
