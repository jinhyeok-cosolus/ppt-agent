# Visual + Insight Layout Reference

## 1. Purpose

하나의 **Main Visual**(이미지 / Chart / 기술·공정 Diagram / 핵심 Data
Visualization)과, 그 Visual이 왜 중요한지·무엇을 의미하는지·어떤
시사점이 있는지를 설명하는 **Supporting Insight**를 좌/우로 배치해
하나의 메시지로 전달하는 범용 2분할 Layout Reference다.

`docs/layout-reference/2026.08.13_layout-catalog_V1.md`의 아래 5개
카탈로그 항목은 콘텐츠 성격은 다르지만 실제 배치 구조가 공통적으로
"한쪽 Main Visual + 반대쪽 Supporting Insight"이므로, 개별 Layout MD를
따로 만들지 않고 이 문서 하나로 통합 관리한다. 각 항목은 아래
[6. Content Variants](#6-content-variants)의 Variant에 대응한다.

| Layout Catalog | 대응 Variant |
|---|---|
| L06. Image + Text | Variant A |
| L07. Market / Problem | Variant B |
| L09. Technology / Principle | Variant C |
| L24. Message + Evidence | Variant D |
| L15. Financial / Growth | Variant E |

### Use When

- 하나의 Main Visual이 슬라이드 메시지의 중심이고, 그 Visual을
  설명·해석·뒷받침하는 텍스트가 반대편에 필요한 경우
- 이미지, Chart, 기술/공정 Diagram, 핵심 주장, 성장 전망 Chart 등
  서로 다른 성격의 콘텐츠이지만 "Main Visual 1개 + Supporting Insight
  1개"의 2분할 구조로 표현 가능한 경우

### Do Not Use When

- 비교 대상이 명확히 2개 이상이고 대등하게 병렬 비교해야 하는 경우 →
  Before/After(`before-after.md`), Comparison Matrix
  (`comparison-matrix.md`), Three-Column(`three-column.md`)
- 하나의 솔루션이 만드는 정확히 2개의 정량 Benefit을 증명하는 것이
  핵심인 경우 → Benefit + Impact(`benefit-impact.md`)
- 공정 흐름을 먼저 보여준 뒤 하단에서 문제/비교를 연결해야 하는 경우 →
  Process + Comparison(`process-comparison.md`)
- 여러 대상을 동일 기준 Row/Column으로 촘촘히 비교해야 하는 경우 →
  Table Comparison(`table-comparison.md`)
- 3개 이상의 독립적인 병렬 메시지를 동일 위계로 나열해야 하는 경우 →
  Three-Column(`three-column.md`)

---

## 2. Relationship to Existing Layout MD (기능 중복 확인용, 삭제 없음)

이번 통합 대상은 아직 전용 Layout MD가 없던 L06/L07/L09/L15/L24
카탈로그 항목이다. 아래 기존 Layout MD는 이 문서와 부분적으로 유사한
"한쪽 Visual + 반대쪽 설명" 구조를 갖지만, 각자 더 구체적이고 이미
확정된 고유 규칙(필수 요소, Reference 실측 좌표 등)을 가지고 있어 이번
작업에서 통합하거나 삭제하지 않는다 — 아래는 참고용 매핑 기록이며 판단은
사용자 확인 후 별도로 진행한다.

- **`02_instruction_design_V1.md`(회사소개)**: 좌측 정보 + 우측 이미지의
  2단 구조가 Variant A(Image + Explanation)와 유사하다. 다만
  회사소개 전용 정보 구조(Company Facts, 이미지 자산 탐색 규칙 등)가
  이미 확정되어 있어 별도 유지.
- **`014_left-right-tech-comparison.md`(14페이지)**: 우측 Process /
  Technology Diagram이 Variant C(Technology / Principle)와 유사하다.
  다만 필수 Summary Bar + 좌측 정량 Table이라는 이 페이지 고유의
  확정 Identity가 있어 별도 유지.
- **`benefit-impact.md`**: 좌/우 2 Area + Evidence 구조가 부분적으로
  유사하다. 다만 "정확히 2개의 정량 Benefit"이라는 이 Layout 고유의
  엄격한 선택 조건과 Reference 실측 규칙이 있어 별도 유지.

---

## 3. Overall Structure

슬라이드는 Hard Rule §9 공통 Header System 아래, 크게 두 영역으로
구성한다.

1. **Main Visual Area**
2. **Supporting Insight Area**

두 영역은 좌/우로 나란히 배치하며, 하나의 **Content Group**으로
인식되어야 한다 — 서로 다른 슬라이드를 이어 붙인 것처럼 분리되어
보이지 않도록 한다(Design System §5 Content Density / Content Group
원칙 참조, 본 문서에서 재정의하지 않음).

### Region Map (가이드값)

본문은 Hard Rule §9의 본문 Safe Area(X 64~1216px, Y 135~656px 기준,
Main Title Supporting Message 사용 시 §12에 따라 Y 시작점이 아래로
조정됨)를 100% 기준으로 한다. 이 Layout은 특정 Reference PPT의 실측
좌표를 근거로 하지 않으므로, 아래 수치는 고정값이 아니라 콘텐츠에 따라
조정 가능한 **가이드값**이다.

| 영역 | 폭 비율(가이드) | 비고 |
|---|---|---|
| Main Visual Area | 50~60% | Main Visual의 정보량이 많을수록 최대 60%까지 확대 가능 |
| Supporting Insight Area | 40~50% | Main Visual이 확대되는 만큼 상대적으로 축소 |

- 기본 비율은 50:50이며, [7. Common Placement
  Principles](#7-common-placement-principles)에 따라 Main Visual의
  정보량이 많은 경우 최대 60:40까지 Main Visual 쪽으로 조정할 수 있다.
  Supporting Insight Area가 이 범위보다 더 좁아져 텍스트가 읽기 어려운
  수준까지 축소되지 않도록 한다.
- 두 영역의 세로 시작점(Top Y)과 높이는 동일하게 맞춘다(Design System
  §5 Parallel Layout Alignment 원칙 참조, 본 문서에서 재정의하지 않음).

---

## 4. Left/Right Placement

- 기본은 **Main Visual을 좌측, Supporting Insight를 우측**에 두는
  구조를 우선 검토하되, 콘텐츠 성격·제공된 이미지 방향·기존 자료의
  흐름에 따라 Main Visual을 우측, Supporting Insight를 좌측에 배치할
  수도 있다.
- 좌우 배치를 바꾸더라도 정보 위계([6. Content
  Variants](#6-content-variants), [8. Supporting Insight
  Area](#8-supporting-insight-area))와 두 영역의 폭 비율 원칙(§3)은
  동일하게 유지한다 — 좌우 반전이 정보 구조 자체를 바꾸지 않는다.
- 한 슬라이드 내에서 Main Visual 위치는 하나로 확정하며, 같은 슬라이드
  안에서 다시 좌우를 뒤섞지 않는다.

---

## 5. Main Title Supporting Message

이 Layout은 Main Title 아래 부제목/설명 요소를 별도로 정의하지 않는다.
필요한 경우 **Hard Rule §12 Main Title Supporting Message**를 그대로
적용한다 — 사용 조건(실제 콘텐츠에 설명이 있을 때만), 위치(Main Title과
Main Content 사이), 분량(1~2줄), Font Size(Design System §3 Explanation
Tier, 18pt)는 모두 §12를 따른다. 사용하는 경우 Main Visual Area와
Supporting Insight Area(§3의 Content Start Y) 전체를 §12 기준대로 함께
아래로 조정한다.

---

## 6. Content Variants

동일한 기본 골격(Main Visual Area + Supporting Insight Area) 안에서
콘텐츠 성격에 따라 아래 Variant 중 하나를 선택한다. Variant는 서로
다른 고정 Template이 아니라, **Main Visual의 종류와 Supporting Insight의
역할 조합**을 콘텐츠에 맞게 고르는 선택지다.

### Variant A — Image + Explanation

- **Main Visual**: 제품, 사업장, 설비, 기술 이미지 등 대표 이미지
- **Supporting Insight**: 핵심 특징과 설명(어떤 이미지인지, 무엇을
  보여주는지, 왜 중요한지)
- 적용 예: 제품/설비/기술 소개, 시설 사진 기반 슬라이드

### Variant B — Chart + Insight

- **Main Visual**: 시장 규모, 실적, 성능, 성장률 등의 Chart / Data
  Visualization
- **Supporting Insight**: 핵심 수치 해석, 원인, 시사점
- 적용 예: 시장 데이터, 문제 정의를 뒷받침하는 근거 Chart

### Variant C — Technology / Principle

- **Main Visual**: 기술 구조도, 공정도, 원리 Diagram
- **Supporting Insight**: 작동 원리, 기술 특징, 핵심 장점
- 적용 예: 단일 기술/공정의 구조·원리 설명(비교가 아닌 단독 설명)

### Variant D — Message + Evidence

- **Main Visual 또는 주요 영역**: 핵심 주장 또는 결론(Large Statement,
  Quote, Key Number 등)
- **Supporting Insight/Evidence 영역**: 사례, 데이터, 이미지 등
  Supporting Evidence
- 적용 예: 하나의 결론을 먼저 제시하고 근거로 뒷받침하는 슬라이드
- 참고: 이 Variant는 주장 쪽이 반드시 "이미지/Chart"일 필요는 없다 —
  주장 자체가 주 영역(Main Visual Area 자리)을 차지하는 짧은 텍스트/
  숫자일 수 있다는 점에서 Variant A/B/C와 다르다.

### Variant E — Growth / Driver

- **Main Visual**: 성장 전망 또는 Financial Chart(매출, 투자, 성장률
  등)
- **Supporting Insight**: Growth Driver, Assumption, 사업 전략 등의
  설명
- 적용 예: 재무 전망, 투자 계획, 성장 스토리 슬라이드

### Selection Guide

| 콘텐츠 특징 | 우선 Variant |
|---|---|
| 제품/사업장/설비/기술 이미지가 핵심이고, 이를 설명하는 텍스트가 필요함 | **A. Image + Explanation** |
| 시장 규모·실적·성능 등 Chart/데이터가 핵심이고, 그 의미·원인 해석이 필요함 | **B. Chart + Insight** |
| 하나의 기술/공정의 구조·작동 원리 자체를 설명해야 함(비교 대상 없음) | **C. Technology / Principle** |
| 결론/주장을 먼저 던지고 그 근거(사례·데이터·이미지)로 뒷받침해야 함 | **D. Message + Evidence** |
| 성장 전망·재무 Chart가 핵심이고, 그 성장의 동인·전제·전략 설명이 필요함 | **E. Growth / Driver** |

콘텐츠가 위 다섯 특징 중 여러 개에 걸쳐 있는 경우, 슬라이드의 **1차
목적**(무엇을 증명/설명하려는 슬라이드인가)을 기준으로 Variant 하나를
선택한다. 어떤 Variant를 선택했는지도 다른 Layout과 동일하게
`slide_outline.md`에 기록한다.

---

## 7. Common Placement Principles

- Main Visual과 Supporting Insight가 서로 다른 슬라이드처럼 분리되어
  보이지 않고 하나의 메시지를 구성하도록 배치한다.
- Supporting Insight는 Main Visual을 단순 반복 설명하지 않는다 — 왜
  그런지 / 무엇을 의미하는지 / 어떤 시사점이 있는지를 전달한다.
- Main Visual의 특정 부분에 직접 대응하는 Explanation은 Visual과
  가까운 관계로 배치해(같은 Content Group 내 좁은 간격) 대응 관계가
  즉시 인식되게 한다.
- Main Visual이 충분한 정보량을 가진 경우 [3. Region
  Map](#region-map-가이드값)의 범위 안에서 Visual 영역을 더 크게 사용할
  수 있도록 좌우 비율을 유연하게 허용한다.
- 기본은 Visual 중심 구조이지만, 콘텐츠 특성에 따라 [4. Left/Right
  Placement](#4-leftright-placement)에 따라 Visual을 좌측 또는 우측에
  배치할 수 있다.
- 좌우 배치를 바꾸더라도 정보 위계와 전체 균형은 동일하게 유지한다.
- 특정 요소(Supporting Header, Key Message, Explanation, Supporting
  Evidence/Detail 등)가 콘텐츠에 없다고 해서 그 자리를 임의의 빈
  영역이나 장식으로 채우지 않는다 — 없는 요소는 생략하고 남는 공간은
  나머지 요소의 여백으로 자연스럽게 흡수한다.

---

## 8. Supporting Insight Area

Supporting Insight Area는 아래 요소 중 **실제 콘텐츠에 필요한 것만**
선택적으로 구성한다. 모든 요소를 항상 다 채울 필요는 없다.

**Supporting Header** ↓ **Key Message** ↓ **Explanation** ↓
**Supporting Evidence / Detail**

- **Supporting Header**: Supporting Insight Area의 주제를 짧게 나타내는
  소제목(예: `핵심 특징`, `시사점`, `작동 원리`). Main Visual Area에는
  대응하는 Header Bar가 없으므로, 좌우 대칭 Header Bar가 필요한
  Before/After·Three-Column·Benefit+Impact와 달리 Hard Rule §10 Content
  Comparison Header(Bar 스타일)를 적용하지 않는다 — 일반 텍스트
  소제목으로 표현한다.
- **Key Message**: Main Visual이 전달하는 핵심을 한 문장으로 요약한다.
- **Explanation**: Key Message를 뒷받침하는 설명(원인, 배경, 작동
  방식 등).
- **Supporting Evidence / Detail**: 세부 수치, 사례, 목록 등 근거·
  상세 정보.

이 네 요소는 항상 이 순서·전부를 강제하는 고정 Template이 아니다 —
콘텐츠에 필요한 요소만 선택하고, 필요하면 순서를 조정할 수 있다. 다만
선택된 요소끼리는 위 정보 위계(Header → Key Message → Explanation →
Evidence/Detail)를 벗어나지 않는다.

### Typography (참조만, 재정의하지 않음)

Font Size는 `Claude_PPT_Design_System.md` §3 Typography System을
그대로 따른다. 아래는 위 요소가 어느 Tier에 대응하는지 매핑만 표시하며,
이 문서가 새로운 Font Size를 정의하지 않는다.

| 요소 | 대응 Tier(Design System §3) |
|---|---|
| Supporting Header | Content Header Tier(20pt, SemiBold) |
| Key Message | Explanation Tier(18pt) |
| Explanation | Explanation Tier(18pt) |
| Supporting Evidence / Detail | Body Tier(16pt) — 16pt 미만으로 축소하지 않음 |
| Main Visual 내부 축 Label / Legend / Source / Footnote | Caption·Auxiliary Tier(14pt) |
| (선택) Conclusion / Key Takeaway | Explanation Tier(18pt) |

---

## 9. Optional Vertical Divider

Main Visual Area와 Supporting Insight Area 사이에 구분선이 필요한
경우, **Hard Rule §11 Vertical Content Divider**를 그대로 적용한다.
두께·색상·Gradient 처리는 §11 원 스펙을 그대로 따르며 이 문서에서
재정의하지 않는다. Divider 사용 여부 자체는 선택 사항이며, 두 영역이
이미지/Chart의 여백만으로 충분히 구분되는 경우 생략할 수 있다.

---

## 10. Optional Conclusion / Key Takeaway

필요한 경우 하단에 Main Visual Area + Supporting Insight Area 전체를
종합하는 Conclusion / Key Takeaway를 Optional로 추가할 수 있다.

- 좌우(또는 Main Visual/Supporting Insight) 내용을 단순 반복하거나
  요약 재진술하지 않는다 — 두 영역을 종합했을 때 도출되는 결론만
  담는다.
- Conclusion은 특정 영역에 속하지 않고 전체 Content Group의 폭과
  중심축을 기준으로 배치한다(Design System §5 Parallel Layout
  Alignment의 Integrated Conclusion 원칙 참조).
- 실제로 종합할 결론이 있는 경우에만 사용하며, 단순 나열형 콘텐츠에는
  강제하지 않는다.

---

## 11. Density & Spacing

- Main Visual은 충분한 크기로 배치한다 — 여백을 남기기 위해 임의로
  축소하지 않는다.
- Supporting Insight Area 내부에서 선택된 요소들은 하나의 Content
  Group으로 촘촘하게 묶고, Main Visual Area와의 사이(또는 Divider
  간격)는 그보다 상대적으로 넓게 유지한다(Design System §5 Content
  Density 원칙).
- Supporting Insight Area 상단에 요소가 몰리고 하단이 비어 보이는
  구성을 피한다 — 콘텐츠가 적으면 두 영역을 세로 중앙 정렬해 여백을
  상하로 분산시킨다.

---

## 12. Alignment

- Main Visual Area와 Supporting Insight Area는 동일한 Top Y에서
  시작하고, 가능한 한 동일한 Height를 사용한다.
- Supporting Header를 사용하는 경우, Main Visual Area 상단 요소와 Y
  위치를 맞춘다.
- Main Visual의 특정 부분과 직접 대응하는 Explanation이 있는 경우, 그
  대응 관계가 시각적으로도 드러나도록 가능한 한 유사한 Y 위치에
  배치한다.
- Optional Conclusion을 사용하는 경우, 본문(Main Visual Area +
  Supporting Insight Area)의 좌우 정렬 기준과 어긋나지 않게 배치한다.

---

## 13. Flexibility

### Must Preserve

- Main Visual Area + Supporting Insight Area의 2분할 구조
- Main Visual과 Supporting Insight가 하나의 Content Group으로 읽히는
  밀착 배치
- Supporting Insight가 Main Visual의 단순 반복이 아니라 해석/시사점을
  전달한다는 원칙
- 선택된 Variant(§6)의 Main Visual 종류·Supporting Insight 역할 조합

### May Adapt

- 좌우 비율(50:50 ~ 60:40, §3 Region Map 가이드 범위 내)
- Main Visual의 좌/우 위치(§4)
- Supporting Insight Area 내부 요소(Supporting Header / Key Message /
  Explanation / Supporting Evidence·Detail) 중 실제로 사용할 요소와
  순서
- Vertical Divider 사용 여부(§9)
- Conclusion / Key Takeaway 사용 여부(§10)
- Main Title Supporting Message 사용 여부(§5, Hard Rule §12 기준)

---

## 14. Avoid

- 5개 Variant를 하나의 고정 Template으로 강제해 콘텐츠와 무관하게
  기계적으로 채우는 것
- Supporting Insight가 Main Visual의 내용을 그대로 반복 서술하는 것
- 콘텐츠에 없는 요소(Supporting Header, Key Message 등)를 형식을
  맞추기 위해 임의로 만들어 채우는 것
- Main Visual을 여백 확보를 이유로 과도하게 축소하는 것
- 정량 데이터가 없는 Chart(Variant B/E)를 임의의 수치로 채우는 것 —
  데이터가 없으면 Diagram/정성적 설명 등 다른 표현으로 대체한다
- 공통 Typography, Main Title Supporting Message(Hard Rule §12),
  Header/Footer(Hard Rule §9) 등을 이 문서에서 중복 재정의하는 것
- Hard Rule 또는 Claude PPT Design System을 이 Layout Reference가
  덮어쓰는 것

---

## 15. Rule Priority

적용 우선순위:

1. **Hard Rule** — CI, Sub Message, Divider, Section Label, Main
   Title, Main Title Supporting Message(§12), Page Number 등 공통
   고정 요소
2. **Claude PPT Design System** — Color, Typography, Chart Style,
   Image Style, Visual Language
3. **Visual + Insight Layout Reference** — Main Visual Area /
   Supporting Insight Area 구조, Variant 선택, 배치 원칙(본 문서)

본 Layout Reference는 Hard Rule과 Claude PPT Design System을 변경하거나
대체하지 않는다.

---

## 16. Selection Rule

다음 조건을 만족할 때 이 Layout을 우선 고려한다.

1. 슬라이드의 콘텐츠가 "하나의 Main Visual + 그것을 설명/해석하는
   Supporting Insight"의 2분할 구조로 자연스럽게 표현됨
2. 비교 대상이 2개 이상 대등하게 병렬 비교되는 구조가 아님(비교가
   핵심이면 [Do Not Use When](#do-not-use-when)의 다른 Layout을 검토)

만족하면 [6. Content Variants](#6-content-variants)의 Selection Guide에
따라 Main Visual의 종류와 Supporting Insight의 역할을 기준으로 Variant
A~E 중 하나를 선택한다.
