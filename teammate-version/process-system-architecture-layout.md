# Process / System Architecture Layout

공정, 시스템 구성, 기술 단계 또는 구성요소 간 연결 관계를 한 페이지에서 설명하기 위한 Layout MD다.

동일한 Process / System Architecture 콘텐츠에 대해 다음 두 가지 조건부 레이아웃을 지원한다.

- Layout A — 이미지 없음: 기존 Component 중심의 수평 프로세스 구조 유지
- Layout B — 이미지 있음: Component 박스 높이를 축소하고 동일 폭·동일 높이의 사진 박스를 추가

본 문서는 개별 Layout 규칙이며, `2026.08.12_design_hard-rules_V2(1).md`의 모든 Hard Rule을 우선 적용한다. 두 문서가 충돌하면 Hard Rule을 따른다.

---

## 1. Layout 목적

다음과 같은 콘텐츠를 순차적으로 설명한다.

- 공정 단계와 단계별 역할
- 시스템을 구성하는 주요 Component
- 기술 또는 데이터의 전달 흐름
- 각 단계의 기능과 짧은 설명
- 전체 시스템이 만들어내는 최종 Output, Insight, Customer Value 또는 Final Result

이 Layout은 `Component 01 → Component 02 → Component 03 ...`처럼 좌측에서 우측으로 진행되는 선형 구조를 기본으로 한다.

---

## 2. 공통 Hard Rule 연동

### 2.1 슬라이드 및 폰트

- 슬라이드 비율: 16:9
- 기준 캔버스: 1280×720px
- Font Family: Pretendard만 사용
- White 또는 밝은 Neutral Background를 기본으로 한다.
- 기술 기반 소재·화학 기업의 전문성, 신뢰성, 정돈된 이미지를 유지한다.

### 2.2 공통 Header System

표지를 제외한 일반 콘텐츠 슬라이드이므로 아래 요소를 반드시 유지한다.

- COSOLUS CI: X=64px, Y=25px, H=20px, 원본 비율 유지
- 우측 상단 Sub Message: `We promise tomorrow`, 우측 끝 X=1216px, Y=25px, 14pt, `#478689`
- 상단 구분선: X=64~1216px, Y=56px, 1px, `#478689`
- Section Label: X=68px, Y=62px, Pretendard Light 12pt, `#8C9694`
- Main Title: X=64px, Y=83px, Pretendard ExtraBold 28pt, 1줄 원칙
- Header Safe Area 하단: Y=135px
- 페이지 번호: 우측 하단에 현재 페이지 숫자만 표시

본문의 Process Title, Component, Image, Arrow, Function Text 및 Insight Box는 Y=135px 아래에 배치한다.

### 2.3 색상

- 핵심 공정·자사 기술·최종 성과: Primary `#067875`, Dark/Main `#034443`, Secondary `#349887`
- 일반 제목 및 본문: Ink `#162B1F`
- 보조 설명: Slate `#5A6664` 또는 Gray `#8C9694`
- 박스 경계: Line `#E1E7E5`
- Component 및 Insight의 약한 배경: Mist `#F3F6F5` 또는 `#F4FAFA`
- Arrow는 Dark/Main 또는 Primary 계열 한 가지 색으로 통일한다.
- Component별 임의 색상 구분을 금지한다.

### 2.4 공통 품질

- 모든 Component 박스의 폭, 높이, 정렬 기준을 동일하게 유지한다.
- 모든 Arrow의 크기, 색상, 선 두께 및 수직 위치를 동일하게 유지한다.
- 텍스트, 이미지, 박스, Arrow 간 의도하지 않은 겹침을 허용하지 않는다.
- 이미지 비율을 왜곡하지 않고 지정 프레임 안에서 Crop한다.
- 텍스트가 박스를 초과하면 폰트를 임의로 축소하지 않고 문구를 줄인다.
- 모든 요소가 슬라이드 밖으로 잘리지 않도록 한다.

---

## 3. 레이아웃 자동 선택 규칙

### 3.1 Layout A — 이미지 없음

다음 조건에서는 기존 Component 중심 레이아웃을 유지한다.

- 입력 콘텐츠에 단계별 사진 또는 대표 이미지가 없는 경우
- 공정명, 기능, 역할, 짧은 설명만으로 구조를 충분히 이해할 수 있는 경우
- 추상적 시스템, 데이터 흐름, 소프트웨어 모듈처럼 사진이 의미를 추가하지 못하는 경우
- 사진보다 단계 명칭과 연결 순서가 더 중요한 경우

### 3.2 Layout B — 이미지 있음

다음 조건에서는 Component 상단 또는 하단에 사진 영역을 추가한다.

- 각 단계별 설비, 시료, 부품, 공정 상태 또는 결과물을 보여줄 사진이 있는 경우
- 사진이 Component 간 차이를 빠르게 식별하는 데 실질적으로 도움이 되는 경우
- 실제 공정이나 장비의 신뢰성을 시각적으로 보여주는 것이 중요한 경우
- 사용자가 단계별 사진 삽입을 명시한 경우

### 3.3 선택 우선순위

1. 단계마다 대응되는 이미지가 충분히 제공되면 Layout B를 선택한다.
2. 일부 단계에만 이미지가 있으면 임의로 빈 이미지 박스를 혼용하지 않는다.
3. 전체 단계 중 사진 확보 비율이 80% 미만이면 기본적으로 Layout A를 선택한다.
4. 핵심 단계만 사진으로 강조해야 한다면 본 Layout을 혼합하지 말고 별도 Key Process Layout을 사용한다.
5. 이미지가 장식적 의미만 갖는다면 Layout A를 유지한다.
6. 사용자가 사진 포함 또는 미포함을 명시하면 해당 지시를 우선한다.

---

## 4. 공통 콘텐츠 구조

### 필수 정보

- Section Label: 기본값 `TECHNOLOGY` 또는 `PROCESS`
- Main Title: 슬라이드 내용을 직접 설명하는 1줄 제목
- System / Process Title: 공정 또는 시스템 전체 명칭
- Component: 3~6개 권장
- Component Name 또는 단계명
- 단계별 Function / Role
- 단계별 Short Detail
- 최종 Insight / Output / Customer Value / Final Result

### 선택 정보

- 단계별 대표 사진
- 단계 번호
- 짧은 조건, 투입물, 산출물 또는 핵심 Spec

### 텍스트 제한

- System / Process Title: 1줄
- Component Name: 1~2줄
- Function / Role: 1줄
- Short Detail: 1줄 권장, 최대 2줄
- Insight 문구: 1줄 권장, 최대 2줄
- 긴 설명은 별도 상세 슬라이드로 분리한다.

---

## 5. 공통 기본 구조

### 5.1 Content Area

- 전체 본문 권장 범위: X=64~1216px, Y=145~665px
- System / Process Title은 본문 상단 좌측에 배치한다.
- 단계 그룹은 System / Process Title 아래에서 수평으로 배열한다.
- 단계 그룹 사이에는 동일한 크기의 Arrow를 배치한다.
- Insight Box는 단계 그룹 전체를 시각적으로 묶는 폭으로 하단에 배치한다.

### 5.2 단계 수

- 기본값: 5개
- 권장 범위: 3~6개
- 3~4개: 단계 폭을 넓혀 시각적 안정감을 확보한다.
- 5개: 기준 레이아웃을 사용한다.
- 6개: Component명과 Detail을 축약하고 Gap을 조정한다.
- 7개 이상: 한 페이지에 강제로 배치하지 않고 슬라이드를 분리하거나 Timeline/Flow Layout을 사용한다.

### 5.3 수평 정렬

- 모든 단계 그룹은 동일한 폭을 사용한다.
- 첫 번째와 마지막 단계의 외곽선은 Content Area 좌우 기준선에 맞춘다.
- 단계 간 Gap과 Arrow 영역은 동일하게 반복한다.
- Arrow는 앞 Component의 우측 중앙과 다음 Component의 좌측 중앙을 연결하는 위치에 둔다.

---

## 6. Layout A — 이미지 없음

### 6.1 기본 원칙

사진이 없으면 Reference의 현재 레이아웃을 유지한다. Component 박스의 크기, 단계별 텍스트 구조, Arrow 위치 및 Insight Box의 기본 수직 위치를 임의로 변경하지 않는다.

### 6.2 단계 그룹 구조

각 단계는 아래 순서로 구성한다.

1. Component Box
2. Function / Role
3. Short Detail

### 6.3 Component Box

- 모든 Component Box는 동일한 폭과 동일한 높이를 사용한다.
- 기준 비율은 가로가 세로보다 넓은 직사각형이다.
- Background: Mist 또는 매우 밝은 Neutral
- Border: Line `#E1E7E5`, 약 0.5~1px
- Corner: Sharp Corner를 기본으로 하며 과도한 Rounded Corner를 사용하지 않는다.
- Component Name은 박스 중앙에 수평·수직 정렬한다.
- 단계 번호가 있으면 Component Name과 하나의 텍스트 Group으로 구성한다.

### 6.4 Function / Role 및 Short Detail

- Function / Role은 Component Box 아래에 배치한다.
- Function / Role은 Pretendard SemiBold~Bold, Ink를 사용한다.
- Short Detail은 그 아래에 배치하고 Slate 또는 Gray를 사용한다.
- 모든 단계에서 두 텍스트의 Y 위치와 간격을 동일하게 유지한다.

### 6.5 Insight Box

- 이미지가 없는 경우 Reference의 현재 위치를 유지한다.
- 단계별 Short Detail과 충분한 간격을 둔다.
- 단계 그룹 전체 폭의 약 70~80%를 사용하고 슬라이드 중앙에 정렬한다.
- Background는 Mist 또는 `#F4FAFA`를 사용한다.
- Border는 Line 또는 Primary 계열의 얇은 선을 사용한다.
- Insight 문구는 중앙 정렬한다.
- 핵심 단어는 Font Weight 또는 Primary Color로 제한적으로 강조한다.

---

## 7. Layout B — 이미지 있음

### 7.1 변환 원칙

사진을 삽입할 때는 기존 수평 프로세스 구조를 유지하면서 각 Component Group 내부만 세로로 확장한다. 축소된 Component Box(텍스트 박스)를 위에, Photo Box(사진 박스)를 그 아래에 배치한다.

기존 Component Box의 높이를 `H`, Photo Box의 폭(= 축소 Component Box 폭)을 `W`라고 정의하면 다음과 같이 변환한다.

- 축소 Component Box 높이: `2H/3`
- Photo Box 폭: 축소 Component Box와 동일(`W`)
- Photo Box 높이: `W`를 기준으로 4:3 비율로 계산한다(`0.75 × W`). Component Box보다 세로로 큰 비중을 차지한다.
- Component Box와 Photo Box 사이 Gap: 약 6~10px
- 변환 후 단계별 시각 블록 높이: `2H/3 + Gap + 0.75W`

즉 사진을 넣더라도 기존 Component Box의 폭과 단계별 X 위치는 유지하며, 높이만 2/3로 축소한다. 새로 추가되는 Photo Box는 축소된 Component Box와 폭은 같지만, 높이는 4:3 비율에 따라 별도로 계산한다.

### 7.2 단계 그룹 구조

각 단계는 아래 순서로 구성한다.

1. 축소 Component Box
2. Photo Box
3. Function / Role
4. Short Detail

기본값은 `Component(텍스트) → 사진 → 기능 → 설명` 순서다. Component Box를 상단에 두어 단계 명칭과 흐름을 먼저 인지시키고, Photo Box는 그 아래에서 내용을 보강한다. 사진이 Component의 결과물보다 공정 투입물을 의미하는 경우에도 전체 슬라이드에서 순서를 통일한다.

### 7.3 Photo Box

- 폭: 축소 Component Box와 동일
- 높이: 폭 기준 4:3 비율로 계산한다(`높이 = 폭 × 0.75`). 축소 Component Box보다 세로로 크다.
- 위치: 축소 Component Box 아래, Function / Role보다 위에 배치한다.
- 모든 Photo Box는 동일한 비율과 크기를 사용한다.
- 사진은 프레임에 꽉 차게 Crop하되 핵심 피사체가 잘리지 않도록 한다.
- 이미지의 밝기, 채도, 색온도는 가능한 범위에서 통일한다.
- Photo Box에 별도의 제목이나 긴 캡션을 중복 삽입하지 않는다.
- Border가 필요하면 Component Box와 동일한 Line 색상을 사용한다.
- 사진과 Component Box가 하나의 카드처럼 지나치게 합쳐져 보이지 않도록 6~10px Gap을 유지한다.

### 7.4 축소 Component Box

- 기존 Component Box의 폭은 변경하지 않는다.
- 기존 Component Box의 높이만 정확히 약 2/3로 줄인다.
- 모든 단계에 동일한 축소 비율을 적용한다.
- Component Name은 축소된 높이 안에서 수직 중앙 정렬한다.
- 텍스트가 들어가지 않으면 폰트를 크게 줄이지 말고 Component Name을 축약한다.
- Background, Border, Font Color 등 시각 스타일은 이미지 없는 Layout과 동일하게 유지한다.

### 7.5 Arrow 위치

- Arrow는 Component Box끼리 연결한다.
- Photo Box의 중앙을 연결하지 않는다.
- Component Box 높이가 축소되므로 Arrow의 Y 위치도 축소 Component Box의 수직 중앙에 맞춰 조정한다.
- Component Box가 단계 그룹 상단에 위치하므로, Arrow는 전체 시각 블록의 상단부에 정렬된다(하단의 Photo Box와는 무관하다).
- 모든 Arrow는 동일한 Y축에 정렬한다.
- Arrow가 Photo Box 또는 Function Text와 겹치지 않도록 한다.

### 7.6 Function / Role 및 Short Detail

- Photo Box 아래에 배치한다.
- 사진 추가로 단계 그룹의 높이가 크게 증가하므로 기존보다 상당히 아래쪽으로 이동한다.
- 모든 단계에서 Function / Role과 Short Detail의 기준선은 동일해야 한다.
- 텍스트 스타일은 이미지 없는 Layout과 동일하게 유지한다.

### 7.7 Insight Box 하향 조정

- 사진이 없는 Layout의 Insight Box 위치를 기준 위치 `Y₀`로 정의한다.
- 사진이 추가되면 늘어난 단계 그룹의 높이만큼 Insight Box를 아래쪽으로 이동한다. Photo Box가 4:3 비율로 세로가 크므로 이동량도 함께 커진다.
- 권장 이동량: 약 `Photo Box 높이 - H/3 + Gap`, 일반적인 5단계·1280×720 기준 대략 90~130px 범위
- Insight Box의 폭과 높이는 원칙적으로 유지한다.
- Insight Box를 축소하여 억지로 맞추지 않는다.
- 페이지 번호 및 하단 Safe Margin을 침범하지 않는 범위에서만 이동한다.
- 이동량이 커서 하단 공간이 부족하면, 이동량을 줄이기 전에 상단 System / Process Title과 단계 그룹 사이 여백을 먼저 소폭 조정한다.
- 그래도 공간이 부족하면 Short Detail을 축약한다. 폰트 크기 축소는 최후 수단으로도 사용하지 않는다.
- 그래도 부족하면 Photo Box의 4:3 비율은 유지한 채 Component Box 폭(= Photo Box 폭) 자체를 줄여 세로 크기를 함께 낮추는 것을 검토한다(비율을 임의로 축소하지 않는다).

### 7.8 사진형에서 유지해야 할 요소

- Component의 X 위치와 폭
- Component 간 Gap
- Arrow의 좌우 연결 관계
- Function / Role 및 Short Detail의 정보 위계
- Insight Box의 폭, 높이 및 스타일
- 전체 수평 프로세스 흐름

---

## 8. 사진 삽입 예외 규칙

- 모든 단계에 사진을 넣는 것이 기본이다.
- 사진이 없는 단계에 임의의 아이콘, 그라데이션 또는 장식 이미지를 채워 넣지 않는다.
- 일부 단계의 사진이 확보되지 않으면 전체를 이미지 없는 Layout으로 전환한다.
- 동일한 사진을 여러 단계에 반복 사용하지 않는다.
- 실제 설비, 실제 제품, 실제 고객사 또는 인증을 암시하는 가짜 이미지를 생성하지 않는다.
- 공정 사진의 방향이나 피사체 크기가 크게 다르면 Crop 기준을 조정해 시각적 무게를 맞춘다.
- 단계별 사진보다 하나의 대형 공정 사진이 더 적절하면 본 Layout 대신 Photo + Process Overlay Layout을 사용한다.

---

## 9. 콘텐츠 변환 예시

### 입력 콘텐츠

- Process Title: 사용 후 배터리 핵심광물 회수 공정
- Component 01: 전처리
- Component 02: 선택적 침출
- Component 03: 불순물 제거
- Component 04: 분리·정제
- Component 05: 제품화
- Insight: 고순도 핵심광물 회수와 공정 폐수 저감

### 이미지가 없는 경우

- Component Box 5개를 기존 높이로 유지한다.
- 각 박스 아래에 Function / Role과 Short Detail을 배치한다.
- Insight Box는 Reference의 기본 위치를 유지한다.

### 단계별 사진이 있는 경우

- 각 Component Box의 폭과 X 위치를 유지한다.
- Component Box 높이만 기존의 2/3로 줄이고, 단계 그룹 상단에 배치한다.
- 각 Component 아래에 동일한 폭을 갖고 4:3 비율로 높이를 계산한 Photo Box를 추가한다.
- Arrow는 축소 Component Box의 수직 중앙을 기준으로 배치한다.
- Function / Role과 Short Detail은 Photo Box 아래, 전체 단계에서 동일한 Y축을 유지한다.
- Insight Box는 기존보다 약 90~130px 아래로 이동한다.

---

## 10. AI 제작 지시문

```text
입력 콘텐츠에 각 Component와 직접 대응되는 단계별 사진이 있는지 먼저 확인한다.

사진이 없거나 사진이 공정 이해에 실질적인 정보를 추가하지 않으면 Layout A를 사용한다. 기존 Component Box의 크기, 수평 단계 구조, Function / Role, Short Detail 및 Insight Box 위치를 유지한다.

모든 단계에 대응되는 사진이 있으면 Layout B를 사용한다. 기존 Component Box의 폭과 X 위치는 유지하고 높이만 기존의 2/3로 줄인 뒤 단계 그룹 상단에 배치한다. 그 아래에 동일한 폭을 갖고 4:3 비율(높이 = 폭×0.75)로 세로가 큰 Photo Box를 추가한다. Photo Box와 Component Box 사이에는 6~10px Gap을 둔다.

Arrow는 Photo Box가 아니라 축소 Component Box의 수직 중앙을 연결한다. 사진 추가로 단계 그룹 높이가 크게 늘어나므로 Insight Box를 기존 위치보다 약 90~130px 아래로 이동한다. Insight Box의 폭과 높이는 유지한다.

일부 단계에만 사진이 있으면 사진형과 비사진형을 혼합하지 않는다. 전체 사진 확보 비율이 충분하지 않으면 Layout A를 사용한다.

모든 경우 공통 Header System, Pretendard Font, Brand Color, Safe Area, 이미지 비율 및 Overlap 금지 규칙은 Hard Rule을 우선 적용한다.
```

---

## 11. 최종 검수 체크리스트

- [ ] 공정 또는 시스템이 좌측에서 우측으로 명확하게 진행되는가?
- [ ] 단계 수가 3~6개 범위인가?
- [ ] 사진 유무에 따라 Layout A 또는 Layout B를 일관되게 적용했는가?
- [ ] 일부 단계만 사진형으로 혼합하지 않았는가?
- [ ] 사진형에서 Component Box의 폭과 X 위치를 유지했는가?
- [ ] 사진형에서 Component Box 높이를 기존의 약 2/3로 줄이고 단계 그룹 상단에 배치했는가?
- [ ] Photo Box가 축소 Component Box와 동일한 폭을 가지며, 높이가 4:3 비율(폭×0.75)로 계산되었는가?
- [ ] Photo Box가 Component Box 아래, Function/Role 위에 위치하는가?
- [ ] Photo Box와 Component Box 사이에 6~10px Gap이 있는가?
- [ ] Arrow가 축소 Component Box의 수직 중앙에 정렬되었는가?
- [ ] 모든 단계의 Function / Role 및 Short Detail 기준선이 동일한가?
- [ ] 사진형에서 Insight Box를 약 90~130px 아래로 이동했는가?
- [ ] Insight Box의 폭과 높이, 스타일을 유지했는가?
- [ ] Insight Box와 페이지 번호 또는 하단 여백이 충돌하지 않는가?
- [ ] 모든 본문 요소가 Header Safe Area Y=135px 아래에 있는가?
- [ ] Pretendard 외 폰트를 사용하지 않았는가?
- [ ] 이미지 비율 왜곡, 텍스트 Overflow, 의도하지 않은 겹침이 없는가?
- [ ] 공식 CI 및 공통 Header System이 정확히 유지되었는가?
