# Comparison Matrix Layout Reference

## 1. Purpose

여러 개의 제품, 기술, 경쟁사, 공정 방식 또는 솔루션을 **동일한 비교 기준(Row)** 으로 병렬 비교할 때 사용하는 Presentation형 Comparison Matrix 레이아웃이다.

단순 표를 만드는 것이 아니라, 각 비교 대상의 차이와 핵심 강점을 한눈에 파악할 수 있도록 **텍스트 + 이미지 + Diagram + 수치 + 강조 요소**를 함께 사용하는 시각적 비교 레이아웃이다.

### Use When
- 자사와 경쟁사 제품/기술을 비교할 때
- 3개 이상의 기술 방식을 동일 기준으로 비교할 때
- 제품 A/B/C 또는 솔루션 A/B/C의 특징을 비교할 때
- 작동원리, 성능, TRL, 장점, 단점 등 동일한 평가 기준을 여러 대상에 반복 적용할 때
- 특정 대상 또는 자사 기술의 차별점을 강조하면서 객관적으로 비교할 때

### Do Not Use When
- 비교 대상이 2개뿐이고 Before/After 구조가 더 적합한 경우
- 시간 흐름이나 단계 진행이 핵심인 경우
- 각 항목의 중요도가 독립적이고 병렬 메시지 전달이 핵심인 경우
- 비교 기준이 대상마다 달라 동일한 행 구조를 만들기 어려운 경우

---

## 2. Overall Structure

기본 구조는 다음과 같다.

`Comparison Criteria | Target A | Target B | Target C | Target D ...`

- 첫 번째 열은 **비교 기준**을 표시한다.
- 나머지 열은 **비교 대상**을 표시한다.
- 동일한 비교 기준의 정보는 같은 Y축 위치에 배치하여 가로 방향으로 즉시 비교 가능해야 한다.
- 비교 대상 수에 따라 3~5개 Column을 기본 범위로 사용한다.
- 비교 대상이 많아질수록 텍스트를 무리하게 축소하지 말고 핵심 정보만 남긴다.

---

## 3. Header Row

각 비교 대상의 이름은 상단 Header Row에 배치한다.

- Header의 높이와 Y 위치는 모든 Column에서 동일하게 유지한다.
- 첫 번째 Header는 `구분`, `비교 기준`, `항목` 등 비교 기준 영역임을 나타낸다.
- 비교 대상 Header는 중앙 정렬을 기본으로 한다.
- Header 색상과 Typography는 Claude PPT Design System을 따른다.
- Header Row는 본문과 명확히 구분되도록 배경색, 선 또는 강조색을 사용할 수 있다.
- 일반 표처럼 모든 셀에 강한 테두리를 사용하지 않는다.

---

## 4. Criteria Column

첫 번째 열은 각 Row의 비교 기준을 표시한다.

예:
- 작동원리
- 공정시간
- 첨가제 사용량
- 기술성숙도(TRL)
- 장점
- 단점
- 성능
- 비용
- 효율
- 적용 분야

### Rules
- 비교 기준은 짧고 명확하게 작성한다.
- 모든 비교 기준은 동일한 X축 정렬과 텍스트 위계를 유지한다.
- 각 Row의 중앙 높이에 정렬하여 해당 행과 자연스럽게 연결되도록 한다.
- 필요 시 기준명 아래에 단위 또는 짧은 설명을 추가할 수 있다.

---

## 5. Comparison Cells

각 비교 대상의 Cell은 단순 텍스트만 사용하지 않고, 정보 특성에 따라 적합한 표현 방식을 선택한다.

사용 가능한 표현 방식:
- Short Text
- Key Number / KPI
- Photo
- Diagram
- Icon
- Chemical Structure
- Mini Chart
- Before/After Image
- Process Image
- Short Bullet
- Badge / Label

같은 Row에서는 가능한 한 **동일한 정보 유형과 정보량**을 사용하여 비교가 쉬워야 한다.

예:
- 작동원리 Row → 각 대상별 Diagram
- 성능 Row → 각 대상별 수치 또는 Mini Chart
- 장점 Row → 각 대상별 1~2개 핵심 문장
- 공정시간 Row → 각 대상별 이미지 + 결과 시간

---

## 6. Presentation Matrix Style

이 레이아웃은 일반적인 표(Table)보다 **Presentation형 비교 Matrix**를 우선한다.

### Must
- 모든 Cell에 사각 테두리를 넣지 않는다.
- 얇은 Horizontal Divider를 중심으로 Row를 구분한다.
- Column 간 구분이 필요한 경우 최소한의 Vertical Divider를 사용한다.
- 충분한 White Space를 확보하되 정보가 지나치게 비어 보이지 않도록 한다.
- 이미지/Diagram이 있는 Row는 해당 Visual을 충분히 크게 사용한다.
- 가로 방향으로 읽었을 때 차이가 즉시 비교되도록 한다.

### Avoid
- Excel처럼 모든 Cell에 Box Border 적용
- 과도한 배경색 사용
- 동일한 내용을 긴 문장으로 반복
- 비교 대상별로 서로 다른 Typography 사용
- 각 Column이 별도의 카드처럼 분리되어 Matrix 비교성이 약해지는 구성

---

## 7. Highlighted Target / Preferred Option

자사, 핵심 기술, 추천안, 우선 제안 등 **강조해야 할 비교 대상이 명확한 경우** 특정 Column 또는 Column Group을 강조할 수 있다.

### Highlight Method
- Main Color의 굵은 Outline
- Header 색상 강조
- Column 상단에 회사명 또는 Preferred Label 배치
- 중요 문구에 Main Color 적용
- 다른 대상보다 시각적 대비를 약간 높임

### Rules
- 강조 대상은 최대 1개 또는 하나의 연속된 Column Group을 기본으로 한다.
- 강조 때문에 비교 구조 자체가 무너지지 않도록 한다.
- 강조 대상의 Column Width를 과도하게 넓히지 않는다.
- `COSOLUS` 등 특정 회사명은 Layout Rule로 고정하지 않는다.
- 실제 콘텐츠에서 자사/핵심 대상이 명확한 경우에만 적용한다.

---

## 8. Visual Comparison Row

이미지 또는 Diagram을 사용하는 Row는 다음 원칙을 따른다.

- 각 대상의 Main Visual 크기를 가능한 한 유사하게 맞춘다.
- 서로 다른 이미지 비율은 Crop 또는 Contain 방식을 적절히 사용해 균형을 맞춘다.
- 이미지 아래 짧은 Result Label 또는 Key Message를 배치할 수 있다.
- 변화 전/후를 보여주는 경우 Cell 내부에 `Before → After` 구조를 사용할 수 있다.
- Arrow 및 강조 요소의 스타일은 모든 대상에서 동일하게 유지한다.

---

## 9. Text Comparison Row

장점, 단점, 특징, 적용성 등 텍스트 중심 Row는 다음을 따른다.

- 한 Cell당 핵심 메시지 1~3개 이내
- 긴 문단 금지
- 동일 Row에서는 문장 길이와 정보량을 가능한 한 유사하게 조정
- 핵심 키워드는 Bold 또는 Main Color로 강조 가능
- 여러 대상에 동일한 표현을 반복하지 말고 차이를 중심으로 작성

---

## 10. Information Hierarchy

기본 정보 위계:

**Slide Main Title**
↓
**Optional Key Message / Comparison Insight**
↓
**Target Header Row**
↓
**Comparison Matrix**
↓
**Optional Source / Footnote**

- 필요 시 Main Title 아래에 한 줄의 핵심 메시지를 추가할 수 있다.
- 핵심 메시지는 Matrix가 전달하려는 결론을 먼저 보여주는 역할을 한다.
- Matrix 내부에서는 Header → Visual/Value → Supporting Text 순으로 읽히도록 한다.

---

## 11. Density & Spacing

Reference와 유사한 **중간~높은 정보 밀도**를 유지한다.

- 비교 대상과 기준이 충분한 경우 본문 영역을 적극적으로 사용한다.
- 이미지가 작고 여백만 큰 형태를 피한다.
- Row 간 간격은 비교 가독성을 해치지 않는 범위에서 최소화한다.
- Header Row와 첫 번째 Data Row 사이 간격을 일정하게 유지한다.
- Source/Footnote는 하단 Safe Area 내에서 최소한의 크기로 배치한다.

---

## 12. Alignment

- 동일 Row의 콘텐츠는 동일한 수직 기준선에 맞춘다.
- 동일 Column의 콘텐츠는 동일한 중심축을 유지한다.
- Header와 Data Cell의 Column Center를 일치시킨다.
- Row Label은 일정한 좌측 또는 중앙 정렬 기준을 사용한다.
- Highlighted Column이 있어도 전체 Grid Alignment는 유지한다.

---

## 13. Flexibility

### Must Preserve
- 비교 기준 Row + 비교 대상 Column 구조
- 동일 Row 기준으로 가로 비교 가능한 정렬
- Presentation형 Matrix의 시각적 구조
- 비교 대상 간 균형
- 필요 시 특정 대상 강조 기능

### May Adapt
- 비교 대상 개수
- 비교 기준 개수
- Cell 내부의 Visual 유형
- Highlight 여부
- Header 배경색 여부
- Vertical Divider 사용 여부
- Key Message 사용 여부

---

## 14. Avoid

- 단순 표 데이터처럼 모든 정보를 텍스트로만 표현
- 모든 Cell에 강한 Border 적용
- 비교 대상마다 Visual 크기가 지나치게 다른 구성
- 특정 Column만 과도하게 많은 내용을 포함
- 비교 기준 순서가 논리 없이 배치되는 것
- 자사 강조가 객관적 비교를 방해할 정도로 과도한 것
- Layout을 맞추기 위해 콘텐츠를 임의 축약하거나 왜곡하는 것
- Hard Rule 또는 Design System을 덮어쓰는 것

---

## 15. Rule Priority

적용 우선순위:

1. **Hard Rule**
   - CI
   - Sub Message
   - Divider
   - Section Label
   - Main Title
   - Page Number
   - 기타 공통 고정 요소

2. **Claude PPT Design System**
   - Color
   - Typography
   - Chart Style
   - Image Style
   - Visual Language

3. **Comparison Matrix Layout Reference**
   - Criteria Row / Target Column 구조
   - Matrix Alignment
   - Presentation형 비교 방식
   - Highlighted Target 표현

본 Layout Reference는 Hard Rule과 Claude PPT Design System을 변경하거나 대체하지 않는다.

---

## 16. Selection Rule

다음 조건을 만족할 때 이 Layout을 우선 고려한다.

1. 비교 대상이 3개 이상이거나, 2개 이상이라도 여러 개의 동일한 비교 기준이 존재함
2. 각 대상을 동일한 기준으로 가로 방향 비교하는 것이 정보 이해에 가장 효과적임
3. 텍스트뿐 아니라 이미지, Diagram, 수치 등 다양한 정보 형식을 하나의 Matrix 안에서 정렬할 필요가 있음

단순히 표 형태의 데이터가 있다는 이유만으로 자동 적용하지 않는다.

비교 기준보다 각 대상의 독립적인 설명이 더 중요한 경우에는 Multi-column Layout을 우선 고려한다.
