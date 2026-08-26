# Content Visualization Freedom

> AI에게 부여하는 자유도는 '디자인 스타일 생성'이 아니라 '콘텐츠를 가장 효과적으로 전달하는 표현 방식 선택'에 한정한다.

## Allowed Freedom
AI는 다음 범위에서 콘텐츠에 따라 판단할 수 있다.

- 콘텐츠에 적합한 레이아웃 선택
- 표, 그래프, 다이어그램, 이미지, 텍스트 중심 구성 중 적합한 표현 방식 선택
- 이미지 사용 여부 및 이미지 수 결정
- 콘텐츠 양에 따른 좌우/상하 영역 비율 조정
- 완성된 원본 Graph/Chart가 없고 Raw Data만 존재하는 경우, 표와 그래프 중 더 적합한 방식 선택
- 핵심 수치의 강조 위치 조정(원본의 값·단위·대응관계 및 기존 Visual의 의미 구조를 변경하지 않는 범위)
- 내용이 과도할 경우 요약 또는 슬라이드 분할 제안
- 동일한 레이아웃 계열 내에서 콘텐츠 밀도에 맞춘 미세 조정

## Graph / Chart / Table 적용 우선순위
Content Visualization Freedom은 아래 우선순위에 따라 적용한다.

1. **완성된 원본 Graph/Chart가 존재하는 경우 → 원본 이미지 재사용**
   - 원본 Graph/Chart 이미지를 최우선으로 사용한다.
   - AI가 데이터를 다시 해석해 새로운 Graph/Chart로 재구성하거나 재디자인하지 않으며, Graph ↔ Table 등 다른 표현 방식으로 임의 변환하지 않는다.
   - 원본의 수치, Series, Category, Axis, Unit, Label, 범례 및 비교 관계를 그대로 보존한다.
   - Layout에 맞춘 크기·위치 및 Crop/Contain 등 배치 조정만 허용한다.
2. **완성된 Graph/Chart가 없고 Raw Data만 존재하는 경우 → AI 시각화 허용**
   - 이 경우에만 데이터 시각화에 대한 Content Visualization Freedom을 적용한다.
   - 원본 데이터의 값·단위·관계를 변경하지 않는 범위에서 Graph/Chart/Table/KPI 중 적절한 표현 방식을 선택할 수 있다.
   - 위 Allowed Freedom의 "표와 그래프 중 더 적합한 방식 선택"도 이 경우에만 적용한다.
3. **일반 콘텐츠 → 기존 Visualization Freedom 유지**
   - 사진, Diagram, Icon, Map, KPI 등 일반 콘텐츠에는 기존 자유도를 그대로 적용하며 전체적인 디자인 자유도를 축소하지 않는다.

원본 Visual의 품질이 사용하기 어려울 정도로 낮거나 사용자가 명시적으로 재디자인을 요청한 경우에만 예외를 허용한다. 예외 적용 여부가 불명확하면 임의로 재생성하지 않는다.

## Evidence Relationship 기반 Visual 판단 (1차 기준)
Visual Type은 근거의 **개수**가 아니라 `slide-content-structuring`이 산출한 **Claim → Evidence → Relationship → Required/Optional** 구조의 **Relationship 유형**을 1차 기준으로 판단한다. 값이 여러 개라도 서로 무관한 독립 값이면 단일 독립 근거로, 값이 하나뿐이어도 그 안에 비교·변화 구조가 내포돼 있으면 관계형으로 다룬다.

단, 완성된 원본 Graph/Chart가 존재하면 위 "Graph / Chart / Table 적용 우선순위"가 이 판단보다 우선하며, Relationship 기반 판단은 원본 Visual을 다른 형식으로 재구성하는 근거가 되지 않는다.

### Relationship → Visual Strategy 후보군
아래는 각 Relationship 유형에 대해 우선 검토할 Visual Strategy의 **방향(후보군)**이다. 특정 Relationship을 특정 Chart 하나에 고정 매핑하지 않는다 — 실제 표현 형태(Bar/Line/Waterfall/Diagram/이미지 페어 등)는 콘텐츠와 Design System(§6 Shape 컴포넌트, §8 Chart/Table/Diagram Style)이 허용하는 범위 안에서 그때그때 판단한다.

| Evidence Relationship | 우선 검토할 Visual Strategy 방향 |
|---|---|
| 단일 독립 근거 | Large Number / Key Stat — 비교·추세 대상이 없으므로 이 자체로 충분 |
| 복수 비교 근거 | Comparison Visual — 여러 대상·항목을 나란히 대조해 차이가 드러나는 표현 |
| Before / After | 전후 차이가 직접 드러나는 Visual — 두 상태를 나란히 배치하거나 변화량 자체를 강조하는 표현 |
| 시간에 따른 변화·추세 | Trend Visual — 시점 흐름에 따른 값 변화가 이어져 보이는 표현 |
| 단계별 변화 | Progression Visual — 단계를 거치며 값이 달라지는 과정이 순서대로 드러나는 표현 |
| 구성요소별 기여도 | Contribution Visual — 여러 요소가 결과에 기여하는 비중·증분이 분해되어 보이는 표현 |
| 원인 → 결과 | Cause-Effect Visual — 원인에서 결과로 이어지는 방향성이 드러나는 표현 |
| 순환 관계 | Cycle/Loop Visual — 되먹임·순환 구조가 닫힌 흐름으로 보이는 표현 |
| 순차 공정/프로세스 | Process/Flow Visual — 여러 단계가 순서대로 이어지는 흐름이 드러나는 표현 |
| 기타 관계 | 관계의 성격에 가장 가까운 표현을 판단하거나, 적합한 Visual이 없으면 Text 중심 |

### Relationship 보존 우선 원칙 (시각적 강조보다 우선)
- Evidence가 관계형(단일 독립 근거가 아닌 모든 유형)이고 Required로 표시돼 있다면, 대표값 하나만 Large Number로 떼어내 강조하고 나머지 관계 값(이전 상태·중간 값·구성요소별 값 등)을 생략하지 않는다 — **관계를 이루는 값 전체가 Visual에 남아 있어야 한다.** 대표값을 시각적으로 더 크게·진하게 강조하는 것은 허용되지만, 그 강조가 나머지 관계 값을 지우는 방식이어서는 안 된다.
- 반대로 원본 자료에 실제로 단일 수치만 있고 비교·추세 등 관계형 데이터가 없다면(Relationship이 "단일 독립 근거"인 경우), 관계를 억지로 만들어내지 않고 Large Number/Text 표현을 그대로 허용한다 — 시각화를 위해 원본에 없는 비교값·추세를 임의로 추정하지 않는다(아래 데이터 정확성 원칙과 동일).

### Evidence-Claim 구조와 시각적 그룹화
- 상위 주장 하나를 뒷받침하는 복수 Evidence는 하나의 의미 그룹(공통 스타일·인접 배치 등)으로 연결해 표현한다.
- 서로 다른 주장을 각각 뒷받침하는 Evidence Group은 겉보기 형식이 같다는 이유만으로(예: 숫자가 여러 개라서) 하나의 동일한 Stat Grid 등으로 무조건 합치지 않는다 — 어느 근거가 어느 주장을 뒷받침하는지 시각적으로 구분되게 표현한다. 구체적 좌표·간격 수치는 여기서 정의하지 않는다.

## 콘텐츠 성격에 따른 보조 판단 (2차 기준)
위 Relationship 기준으로 Visual Strategy 방향을 정한 뒤, 그 방향 안에서 구체적 형식을 고를 때 아래 콘텐츠 성격도 함께 판단한다.

- 개념·기능·효과·추상적 메시지 → Icon
- 국가·지역·거점·공급망 → Map
- 제품·설비·공정·현장·결과 등 **실제 모습 자체가 Claim을 직접 뒷받침하는 콘텐츠** → Photo/Image를 정식 Evidence Visual 후보로 판단(아래 "이미지 자산 활용 기준" 참조)
- 위 어디에도 해당하지 않고 적합한 Visual이 없거나 시각화가 의미를 왜곡할 가능성이 있는 경우 → Text 중심

## 이미지 자산 활용 기준
- 입력 자료 또는 별도로 제공된 이미지 자산이 있는 경우, Claim을 직접 뒷받침하는 이미지가 존재하는지 먼저 확인한다.
- 이미지가 Claim을 직접 뒷받침하는 Evidence(Required 또는 Optional)인 경우에만 Evidence Visual 후보로 사용한다 — 근거와 무관하게 단순히 빈 공간을 채우기 위한 이미지는 사용하지 않는다.
- 이미지가 제공되었다는 이유만으로 무조건 사용하지 않는다 — 해당 슬라이드의 핵심 메시지와 직접 관련된 경우에만 사용한다.
- 관련 이미지가 없으면 Photo 영역을 억지로 만들지 않고, 위 Relationship → Visual Strategy 기준에 따라 다른 적절한 표현을 선택한다.
- 제공된 원본 이미지의 의미·내용·수치 등을 임의로 변형하지 않는다(기존 원칙 유지).
- 원본에 없는 수치나 데이터를 추정하여 Chart를 생성하지 않는다(기존 데이터 정확성 원칙 유지).

## Not Allowed
AI는 다음 사항을 임의로 변경하지 않는다.

- Hard Rule의 폰트, 폰트 크기, 컬러 등 고정 규칙 변경
- 기존 Visual Style과 다른 새로운 디자인 언어 생성
- 슬라이드마다 서로 다른 카드, 아이콘, 선, 장식 스타일 사용
- 브랜드 컬러 체계 외의 임의 색상 체계 생성
- 단순히 공간을 채우기 위한 장식 요소 추가
- 사용자 자료에 없는 수치, 사실, 성과를 임의로 생성
- 레이아웃 Reference의 목적과 무관한 구조를 임의로 선택

## Decision Principle
- 디자인을 바꾸기보다 콘텐츠 표현 방식을 바꾼다.
- 가독성과 정보 전달을 최우선으로 한다.
- 가장 단순한 표현으로 메시지가 전달되면 복잡한 시각화를 추가하지 않는다.
- 여러 표현 방식이 모두 가능한 경우 Deck 전체의 일관성이 높은 방식을 우선한다.
- Relationship 보존을 단순 시각적 강조보다 우선한다 — 관계형 Required Evidence를 대표값 하나로 축약해 나머지 관계가 사라지게 하지 않는다.
- 특정 Relationship 유형을 특정 Chart 형태 하나에 고정 매핑하지 않는다 — Relationship → Visual Strategy 표는 방향성 후보군이며, 실제 형태는 콘텐츠와 Design System이 허용하는 범위에서 자유롭게 판단한다.
