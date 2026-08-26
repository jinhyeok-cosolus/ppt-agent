# Flow Diagram 공통 규칙 (COSOLUS PPT)

이 문서는 공정도/flow diagram 형태의 슬라이드를 만들 때 항상 적용되는 **반복 표현 규칙**입니다.
슬라이드마다 달라지는 내용(어떤 단계가 있고 어떻게 분기하는지, 어떤 이미지를 쓰는지)은
이 문서에 넣지 않고 슬라이드별 구조 프롬프트(input)에 따로 작성합니다. 이 문서도 특정
슬라이드의 단계명·이미지 파일명을 예시로 하드코딩하지 않는다 — 모든 예시는 원칙 설명용이다.

## 0. 역할 구분과 적용 우선순위

- **전체 배치·공간 구조(Region Map)의 원본 기준**은 `docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`의 **L25 Symmetric Two-Split**(슬라이드 25~26, `layout-catalog_V1.md`의 L25 항목)이다. 아래 "Region Map(비율 기준)"은 이 pptx의 실제 도형 좌표를 분석해 **재사용 가능한 비율로 일반화**한 것이며, **Flow Diagram Routing이 선택되면(위 Use When 충족 시) 공간 배치의 필수 기준으로 적용한다** — 표현 규칙(화살표/색상/Typography 등)만 지키고 이 Region Map을 참고하지 않은 채 임의의 좌·우 컬럼 비율이나 임의의 분기 위치를 사용하지 않는다.
- **실제 좌표 산출 시 1차 소스**: [`flow-diagram-implementation-reference.md`](flow-diagram-implementation-reference.md)에 위 pptx 슬라이드 25~26의 도형 좌표·크기·Connector 형태를 실측 그대로(일반화 없이) 정리해 두었다. HTML 좌표를 계산할 때는 아래 Region Map(비율 범위, 참고 설명)이 아니라 **이 Implementation Reference 파일의 실측값을 1차 소스로 사용**한다 — 두 문서의 수치가 다르면 Implementation Reference가 우선한다(2026-08-24, `cosolus-ir-deck-F` Slide 16에서 Region Map 비율표만으로 재구현한 결과가 실제 pptx 구조와 어긋난 사례를 반영).
- **이 문서(flow-diagram-rules.md)**는 그 공간 구조 위에서 매 슬라이드 반복되는 **표현 규칙**(화살표 형태, 라벨 박스 배치, 아이콘 처리, 색상 대비 적용 방식, 밀도, 대칭, 라벨 텍스트 위치)도 함께 정의한다.
- **실제 단계·분기 관계·텍스트·사용 이미지**는 슬라이드별 input 지시서가 결정한다. 이 문서는 그 내용을 받아 어떻게 "표현"할지만 규정한다.
- 우선순위는 프로젝트 전체 체계를 그대로 따른다: **Hard Rule(`design-hard-rules`) > Claude PPT Design System > Content Visualization Freedom > L25 Layout Reference(pptx 슬라이드 25~26, 아래 Region Map 포함) > 이 문서**. 아래 각 규칙은 상위 문서와 충돌하지 않는 범위 안에서만 적용되며, 상위 문서와 다르게 읽히는 표현이 있다면 항상 상위 문서가 우선한다.
- **Header/공통 고정 영역 불가침**: Section Label·Main Title·좌측 상단 CI·우측 상단 Sub Message·상단 구분선·우측 하단 페이지 번호(Hard Rule §9)와 Main Title Supporting Message(§12)는 이 문서가 다루는 범위가 아니다. 이 문서의 "제목과 도식 사이 여백" 규칙은 Header Safe Area(§9/§12)를 침범하지 않는다는 기존 원칙을 Flow Diagram 맥락에서 재확인하는 것일 뿐, 별도 예외나 새 좌표를 만들지 않는다.

### Region Map (비율 기준, L25 실측을 일반화 — Hard Rule §9 Body Box 폭·높이 기준 %)

> 아래 %는 Body Box(Hard Rule §9 Safe Area, 콘텐츠가 실제로 그려지는 영역) 폭·높이를 각각 100%로 두고 L25(슬라이드 25~26) 도형 좌표를 분석해 도출한 **범위**다. 특정 슬라이드의 좌표를 그대로 고정한 값이 아니라, 콘텐츠 분량에 따라 이 범위 안에서 조정 가능한 가이드라인이다. 좌→우 흐름, 상단=1차 분기 후 첫 번째 갈래, 하단=두 번째 갈래를 기준으로 표기한다(실제로는 좌/우 배치로 응용할 수도 있다 — 그 경우 축만 바꿔 동일 비율을 적용한다).

| 영역 | 비율 범위 | 비고 |
|---|---|---|
| 공통 시작 영역(Shared Intake) 가로 폭 | 0% ~ 약 35% | Body Box 좌측 끝부터 1차 분기점 직전까지. 공유 시작 노드(들)와 그 사이 연결 화살표가 이 구간 안에 위치 |
| 1차 분기점(브래킷) X 위치 | 약 33% ~ 38% | 공통 시작 영역이 끝나고 상/하 Lane으로 갈라지는 지점. 브래킷의 상/하 색 분할 경계도 이 X선상에 위치 |
| 상단 Lane 세로 영역 | 약 상위 45%p ~ 50%p | 1차 분기점의 Y 위치(약 45~50%)를 상/하 Lane의 경계로 삼아 대칭 배치 |
| 하단 Lane 세로 영역 | 약 하위 50%p ~ 55%p | 위와 동일한 경계 기준. 두 Lane의 세로 폭 차이가 크게 벌어지지 않도록 대칭을 우선한다(분기 구조 대칭 규칙과 동일 원칙) |
| 2세대(하단 Lane) 내부 재분기점 X 위치 | 약 48% ~ 55% | 1차 분기점(33~38%) 이후, 하단 Lane 안에서 다시 위/아래로 갈라지는 두 번째 브래킷의 X 위치. 1차 분기점보다 오른쪽이며 결과물 영역보다는 왼쪽 |
| 라벨 영역(카테고리 라벨 박스 사용 시) 위치/폭 | X 약 20% ~ 35% (폭 약 10~14%p) | 1차 분기점(33~38%)보다 왼쪽 또는 그 직전 구간에 위치해, 화살표 흐름을 가리지 않고 그 위쪽에 뜬다(위 "라벨 박스 규칙" 참조). 세로 위치는 자신이 설명하는 Lane의 세로 영역 안에 둔다 |
| 결과물(Result) 영역 시작 위치와 가로 점유 | 약 68% ~ 76%에서 시작, 100%(Body Box 우측 끝)까지 점유 | 폭 약 24~32%p. 1세대·2세대·재분기 하위 갈래의 최종 결과물 모두 이 대역 안에서 시작해 우측 끝까지 사용 |

**영역 간 최소 Gap/정렬 원칙**
- 공통 시작 영역과 1차 분기점 사이, 1차 분기점과 각 Lane의 첫 요소 사이에는 서로 맞닿지 않는 최소 여백을 둔다 — 브래킷 선과 다음 요소가 겹치거나 즉시 붙지 않게 한다.
- 상단/하단 Lane은 서로 다른 좌우 시작 X(1차 분기점 X)와 종료 X(결과물 영역 끝)를 동일하게 공유한다 — Lane마다 좌우 시작·종료 위치가 달라지지 않는다.
- 2세대 내부 재분기의 두 하위 갈래(위/아래)도 같은 원칙으로 좌우 시작·종료 X를 서로 동일하게 맞춘다.
- 라벨 영역은 자신이 속한 Lane의 세로 영역 범위를 벗어나지 않는다(위 Lane 세로 영역 비율 참조) — 다른 Lane의 세로 영역을 침범하지 않는다.
- 1세대/2세대 사이 가로 점선 구분선(위 "구간 구분선 규칙")은 1차 분기점의 Y 위치(상/하 Lane 경계)와 같은 높이에 배치한다.

## Use When / Do Not Use When (Layout Routing 참고)

- **Use When**: 하나의 공통 시작점(또는 공통 자재/공정)에서 2개 이상의 갈래로 분기하는 공정·흐름을 보여줘야 하고, 각 갈래(또는 카테고리)를 색상 등으로 뚜렷하게 대비시켜야 할 때. 갈래가 다시 하위 갈래로 재분기하는 구조를 포함할 수 있다.
- **Do Not Use When**:
  - 분기 없이 기존(Existing)-개선(Improved) **정확히 2개**를 **좌우 Column**으로 나란히 비교하는 것이 핵심이면 → `before-after.md`(Variant A, Comparison Frame이 좌우 Column 기준)를 우선 검토한다. 공유 시작점에서 위/아래(또는 좌/우)로 분기하는 **하나의 트리 구조**로 표현해야 한다면 이 문서(L25)를 우선한다.
  - 공정 흐름을 먼저 보여준 뒤 그 흐름과 연결된 비교/문제점을 슬라이드 **하단**에서 별도로 다뤄야 하면 → `process-comparison.md`를 우선 검토한다.
  - 분기 없는 **단일 선형 흐름**만 설명하면 충분하면 → `process-system-architecture-layout.md`를 우선 검토한다.
  - 비교 대상이 3개 이상이면 → `comparison-matrix.md`를 우선 검토한다.

## Flow Graph 선해석 및 Connector 생성 원칙 (배치보다 선행)

> 아래 원칙은 좌표·스타일을 정하기 **이전에** 적용되는 절차 규칙이다 — 먼저 이 절차를 따라 Flow Graph를
> 확정한 뒤에만 Region Map(§0)과 이 문서의 나머지 표현 규칙(화살표/라벨/색상 등)을 적용해 실제 좌표를
> 계산한다. 순서를 바꿔 좌표부터 잡고 화면상 가까운 요소끼리 연결하지 않는다.

### 1. Flow 관계 선해석 원칙
- 레이아웃을 배치하기 전에, input의 각 요소를 **Material/Input, Process, Intermediate, Output** 중 하나로
  분류하고, 요소 간 선후 관계를 먼저 **Flow Graph**(무엇이 무엇으로 이어지는지)로 확정한다.
- 시각적 배치(좌표)를 먼저 만든 뒤 화면상 가까운 요소끼리 임의로 Connector를 연결하지 않는다 — Connector는
  항상 이 Flow Graph에 실제로 존재가 확인된 관계에만 그린다.
- 동일 Material이 이전 Process의 Output이면서 동시에 다음 Process의 Input인 경우, 두 개의 별도 노드로
  중복 생성하지 않고 하나의 **Intermediate Node**로 취급해 Flow가 끊기지 않고 연속되게 한다.
- 이 분류 결과에 따라 Connector 처리 방식도 함께 결정한다 — **Process는 Connector를 연속 유지**하고
  **Material/Input/Intermediate/Output은 Connector를 분절**하는 것이 원칙이며(각각 아래 "공정(Process)
  라벨·이미지와 Connector의 수직 배치 규칙", "Material/Intermediate/Output Node 라벨 배치 규칙" 참조),
  두 처리 방식을 서로 혼용하지 않는다(Process를 분절 방식으로 그리거나 Material류를 연속 통과시키지 않는다).

### 2. Material → Process → Material Connector 연속성
- `Material A → Process → Material B` 관계에서는, Process 이미지/라벨이 "공정(Process) 라벨·이미지와
  Connector의 수직 배치 규칙"에 따라 Connector 위쪽에 떠 있더라도, **A→Process 구간과 Process→B 구간의
  Connector를 모두 표현**한다.
- Process를 Connector 위에 띄워 배치한다는 이유로 Process 전후 두 구간 중 하나를 생략하거나, Process
  노드와 그 지점의 Trunk Line 사이의 시각적 연관성을 없애지 않는다 — Process 노드가 흐름과 무관하게 떠
  있는 독립 라벨처럼 보이지 않아야 한다.
- 결과적으로 하나의 Process를 통과하는 Flow가 시각적으로 끊겨 보이면(전후 어느 한쪽이라도 Connector가
  없거나 Process와 Trunk Line의 연결이 드러나지 않으면) 규칙 위반으로 판정한다.
- 여기서 "A→Process 구간"과 "Process→B 구간"은 물리적으로 끊어 그리는 두 개의 별도 선이 아니라, Process
  이미지 아래를 지나가는 **하나의 연속된 Connector 선**의 앞/뒤 구간을 가리키는 개념적 구분이다 — Process
  지점에서 Connector를 실제로 끊어 그리지 않는다(아래 "공정(Process) 라벨·이미지와 Connector의 수직 배치
  규칙" 및 "Node와 Connector 완전 비중첩"의 Process 처리 방식과 동일).

### 3. Branch Point 구조 보존
- 하나의 Node에서 여러 경로로 분기되는 경우, 반드시 **공통 Trunk → 단일 Branch Point → 복수 Branch**
  구조로 생성한다(위 "복수 결과물 분기 규칙(Sibling Outputs)"이 Process 단위 분기에 요구하는 것과 같은
  구조를, Branch Point가 등장하는 모든 경우—Region Map의 1차/2차 분기점 포함—에 일관되게 적용한다).
- 각 Branch Connector를 서로 독립된 선처럼(Branch Point와 시각적으로 이어지지 않은 채) 생성하거나, Branch
  마다 시작 지점이 서로 어긋나게(예: 한쪽 Branch만 Branch Point에서 뻗어 나가고 다른 쪽은 별도 지점에서
  갑자기 시작) 만들지 않는다 — Branch가 N개면 Branch Point에서 N개 모두로 뻗어나가는 선이 실제로
  그려져야 하며, 일부만 그려지고 나머지가 누락되지 않는다.
- Branch Point에서 각 Branch가 갈라져 나가는 시작 X/Y 좌표를 공유하도록 해, 여러 개의 개별 선이 아니라
  **하나의 Fork 구조**로 인식되게 한다.
- Region Map(§0)은 Branch Point의 **대략적인 위치**(X/Y 비율)를 결정하는 역할이고, 이 규칙은 그 위치에서
  Branch 자체가 어떻게 **연결 구조**를 이루는지를 강제하는 역할이다 — 서로 다른 층위의 규칙이며 충돌하지
  않는다.

### 4. Node와 Connector 완전 비중첩 (공통 원칙, Process/Material 처리 방식 구분)
- Process뿐 아니라 Material/Input/Intermediate/Output 노드의 **이미지와 텍스트 라벨 모두**, Connector를
  가리거나 관통하지 않는 것을 **공통 기본 원칙**으로 한다 — 위 "공정 라벨·이미지와 Connector의 수직 배치
  규칙", "Material/Intermediate/Output Node 라벨 배치 규칙"은 이 공통 원칙을 각 Node 유형에 맞게
  구체화한 것이다. 다만 이 원칙을 지키는 **방식**은 두 유형이 서로 다르다 — 하나의 방식으로 혼용하지 않는다.
  - **Process**: Connector 자체를 구성하는 Node가 아니라 Flow 위에 표시되는 공정 정보로 취급한다.
    공정명+이미지 전체를 수평 Connector보다 Y축상 위쪽에 배치해 애초에 Connector와 물리적으로 겹치는
    지점을 만들지 않는다 — Connector는 Process 이미지 아래에서 **끊기지 않고 하나의 연속된 선**으로
    유지한다. 즉 Process는 아래 "Bounding Box 외곽에서 종료 후 재시작" 방식의 적용 대상이 아니다.
  - **Material/Input/Intermediate/Output**: 실제 Flow 경로를 구성하는 Node로 취급한다. 이미지가 있는
    구간에서는 Connector를 **반드시 분절**한다 — 기본 표현은 **Connector → Node Image → Connector**다.
    이미지 뒤/아래로 Connector를 끊지 않고 연속 통과시키는 표현은 금지한다.
- **이미지 Bounding Box도 텍스트와 동일하게 비관통 대상이다** — Material/Intermediate/Process/Output
  이미지 중 어느 것도 Connector 위에 겹쳐 놓지 않는다(과거 "Connector가 Material 이미지 중심을 지나가도
  된다"는 예외는 더 이상 적용하지 않는다). Process는 위쪽 배치로, Material/Input/Intermediate/Output은
  아래 분절 방식으로 각각 이 비관통 원칙을 지킨다.
- Material/Input/Intermediate/Output에서 Connector는 Node의 Bounding Box(이미지+라벨을 포함한 실제
  렌더링 영역) **외곽에서 종료**하고, 다음 구간은 그 Bounding Box 외곽 **이후부터** 시작한다 — Node를
  사이에 둔 두 Connector 구간은 Node의 폭만큼 끊어 그리며, Node 내부를 관통해 하나의 선처럼 그리지 않는다.
  (Process에는 이 분절이 적용되지 않는다 — 위 Process 항목 참조.)
- Node와 Connector 사이에는 항상 명확한 Gap을 확보한다. Process가 Connector보다 위쪽에 뜨는 경우에도
  이미지 하단과 Connector 사이에 이 Gap을 동일하게 유지한다.
- **검증 기준**: 최종 렌더링에서 Connector가 이미지 또는 텍스트 영역을 **조금이라도** 관통하면 위반으로
  판정한다(이미지 관통도 이제 텍스트 관통과 동일하게 위반이다 — 위 "Material/Intermediate/Output Node
  라벨 배치 규칙"에 남아 있던 이미지 중심 통과 허용 문구도 이 강화된 기준을 따른다). 추가로, **Process인데
  Connector가 물리적으로 끊겨 있거나(Connector → Process Image → Connector 형태), Material/Input/
  Intermediate/Output인데 Connector가 끊기지 않고 이미지 뒤로 그대로 통과하는 경우**도 각각 위반으로
  판정한다.

### 5. 생성 전 Flow Graph 검증
- HTML/PPT 배치 전에, `Node → Process → Node → Branch → ...`로 이어지는 관계가 input이 설명하는 실제
  공정 순서와 일치하는지 먼저 확인한 뒤에 Connector를 생성한다.
- 화면상 가까운 요소를 단순히 연결하지 않는다 — 모든 Connector는 1번의 Flow Graph에서 실제로 존재가
  확인된 관계에만 그린다.

### 6. 생성 전 Output 관계 판별 (Output Group vs Sibling Outputs Branch)
- Flow Graph 선해석 단계(1번)에서 복수 결과물을 발견하면, Connector를 생성하기 전에 그 결과물들이
  **Output Group**인지 **Sibling Outputs Branch**인지 먼저 판별한다(판별 기준은 아래 "Output Group /
  Sibling Outputs Branch 판별 규칙" 참조).
- 이 관계를 확정한 뒤에만 Branch 여부(Branch Point를 만들지, 단일 Connector로 묶을지)를 결정한다 —
  복수 결과물을 발견했다는 사실만으로 곧바로 Branch Point부터 그리지 않는다.

## 화살표 / 연결선 규칙
- 모든 단계 연결은 반드시 화살표 도형으로만 표시한다. 하이픈(-)이나 대시로 대체하지 않는다.
- 분기선(브래킷)도 화살표와 동일한 선 규칙을 따른다.

## 공정(Process) 라벨·이미지와 Connector의 수직 배치 규칙
- **Process는 Connector 자체를 구성하는 Node가 아니라 Flow 위에 표시되는 공정 정보로 취급한다** — 아래
  Material/Input/Intermediate/Output Node(위 "Node와 Connector 완전 비중첩" 참조)처럼 Connector를 끊는
  대상이 아니다.
- 공정명(Process Label)과 공정 이미지/아이콘은 그 공정을 지나가는 **수평 Connector의 Y축상 위쪽 영역**에 배치한다.
- 기본 수직 순서는 **공정명 → 공정 이미지 → 수평 Connector**다.
- 공정명과 이미지는 Connector의 진행 경로를 가리거나 끊지 않는다. 수평 Connector는 공정 이미지 뒤를 통과하거나
  이미지에 의해 분절되지 않고 **하나의 연속된 Flow Line**으로 유지한다 — 즉 `Connector → Process Image →
  Connector`처럼 공정 이미지가 Connector의 중심축 위에 직접 놓이는 구조로 만들지 않는다.
- 공정명과 이미지는 해당 공정이 위치하는 X축 지점을 중심으로 정렬하되, Connector와 적절한 세로 Gap을 유지한다
  (위 "라벨 박스 규칙"이 카테고리 라벨 박스에 요구하는 것과 같은 방향 — Connector를 관통하지 않고 그 위에 뜬다).
- 이 규칙은 **공정(Process) 노드 전용**이며, 시작물질·중간물질·결과물 등 Material/Output Node에는 강제하지
  않는다(Material/Intermediate/Output Node의 배치는 아래 "Material/Intermediate/Output Node 라벨 배치
  규칙"과 "라벨 텍스트 위치 규칙"을 따른다).

## Material / Intermediate / Output Node 라벨 배치 규칙 (이미지·라벨 모두 비관통)
- **Material/Input/Intermediate/Output은 Process와 달리 실제 Flow 경로를 구성하는 Node로 취급한다** —
  이미지가 있는 구간에서는 Connector를 반드시 분절하며, 기본 표현은 **Connector → Node Image →
  Connector** 구조다(위 "Node와 Connector 완전 비중첩" 참조).
- 시작물질·중간물질·결과물 등 **Connector가 지나가는 지점에 놓이는 Node**(Material/Input/Intermediate/
  Output)는 위 Process 규칙처럼 Connector 위로 완전히 띄우지 않아도 되지만, 그렇다고 이미지+텍스트 라벨을
  **하나의 블록으로 묶어 그 블록 전체의 중심을 Connector에 맞추지 않는다** — 이 경우 라벨 텍스트 절반이
  Connector 선과 겹치게 된다.
- **Connector는 해당 Node의 이미지도 관통하지 않는다**(위 "Node와 Connector 완전 비중첩" 참조 — 과거
  "이미지 중심은 통과 가능"이라는 예외는 더 이상 적용하지 않는다) — Connector는 이미지 Bounding Box
  직전에서 종료하고, 이미지 폭만큼 공백을 둔 뒤 이미지 Bounding Box 다음 지점부터 다시 시작한다. **텍스트
  라벨 역시 Connector와 겹치지 않는 별도 영역**(이미지 기준 Connector 반대쪽)에 배치한다.
- 기본 배치는 **이미지 → 라벨** 또는 **라벨 → 이미지** 중 콘텐츠 구조에 맞게 선택하되, 어느 쪽을 선택하든
  **라벨의 Bounding Box와 Connector 사이에 명확한 세로 Gap**을 확보한다 — 라벨을 이미지 반대쪽으로
  밀어내는 것만으로 Gap이 저절로 생기지 않으면 여백을 추가한다.
- 라벨이 2줄 이상으로 줄바꿈되는 경우에도 그 전체 텍스트 영역이 Connector를 관통하지 않아야 한다 —
  줄 수가 늘어난 만큼 라벨 영역과 Connector 사이 Gap도 함께 확보한다(줄 수 증가를 이유로 Gap을 줄이지
  않는다).
- 동일 위계의 Material Node(예: 같은 Lane·같은 단계에 있는 여러 중간물질)는 라벨 위치(이미지 위/아래
  또는 좌/우) 규칙을 서로 일관되게 적용한다 — 노드마다 라벨 위치를 다르게 섞지 않는다.
- **검증 기준**: 최종 렌더링에서 Connector 선이 이미지 또는 라벨 텍스트 영역을 조금이라도 가로지르면
  위반으로 판정한다(이미지·텍스트 모두 대상 — 위 "Node와 Connector 완전 비중첩" 기준과 동일하다).

## 라벨 박스 규칙
- 구간을 표시하는 라벨 박스(예: "기존공정(1세대)", "COSOLUS(2세대)")는 화살표 흐름 바깥(위쪽)에
  별도로 띄워서 배치한다.
- 라벨 박스는 화살표 선 위에 겹치거나 화살표를 관통해서는 안 된다. 화살표는 박스 아래를
  깨끗하게 그대로 지나가야 한다.
- 각 라벨 박스는 자신이 설명하는 구간/분기와 같은 높이(수평선상)에 배치한다.

## 아이콘 / 이미지 규칙
- 아이콘·이미지에는 어떠한 테두리나 박스도 넣지 않는다. 이미지만 자연스럽게 배치한다.
- 이미지는 반드시 첨부된 파일 그대로 사용한다. 새로 검색하거나 대체 이미지를 만들지 않는다.
- 슬라이드별 프롬프트에는 반드시 "이미지 파일명 = 어떤 단계/라벨" 매칭표를 함께 제공한다.

## 색상 대비 규칙 (Flow Diagram 내부 표현 규칙 중 최우선 순위)
- 서로 다른 카테고리(예: 1세대/2세대, A안/B안)를 비교하는 도식에서는, 각 카테고리에 지정된 색을
  해당 구간의 모든 화살표·연결선·분기선에 예외 없이 적용한다.
- **이 색상 규칙은 "Flow Diagram 내부의 다른 표현 규칙"(예: 특정 요소를 브랜드 Teal 단색으로 통일하려는 관성 등) 사이에서만 최우선이라는 뜻이다.** Hard Rule §5 Color Usage(Red/Blue는 명확한 의미가 필요한 예외적 경우에만 제한적으로 사용, Orange/Amber 등 Secondary Color는 강조에 사용 금지, 강조는 Font Weight → Main Color 순으로 적용)와 Claude PPT Design System의 색상 규정이 이 규칙보다 항상 우선한다. 카테고리 색으로 Red/Blue 등 Hard Rule상 "예외적" 색을 쓰는 경우, 그 자체가 Hard Rule이 말하는 "명확한 의미가 필요한 예외적 경우"에 해당하는지 먼저 확인한다(카테고리 대비처럼 의미가 명확하면 해당).

## 밀도 / 크기 규칙
- 요소 간 여백을 최소화하고 슬라이드 가로 폭을 꽉 채우도록 배치한다.
- 아이콘 크기는 여백 대비 큼직하게 한다.
- 라벨 텍스트는 굵게(bold)로 강조하되, **구체적 pt 값은 Claude PPT Design System §3 Typography Tier를 그대로 따른다 — Source/Footnote/각주 역할이 아닌 모든 텍스트는 14pt 미만으로 축소하지 않는다(2026-08-19 확정 사항, 공간·밀도 부족을 이유로 한 예외 없음).** 노드 수가 많아 공간이 부족한 경우에도 라벨 폰트를 14pt 미만으로 줄이는 방식으로 밀도를 확보하지 않는다 — 대신 아이콘 크기 축소, 텍스트 줄바꿈, 여백 최소화, 슬라이드 폭 활용(가로 채움)을 먼저 사용하고, 그래도 부족하면 단계 수 자체나 표현 구조를 메인/사용자와 재검토한다.
- 제목(슬라이드 상단)과 도식 사이에는 충분한 여백을 두어 겹치지 않게 한다(Hard Rule §9 Header Safe Area, §12 Supporting Message 영역 침범 금지).

## Node 이미지 최소 크기 및 공간 확보 규칙 (Occupied Area 포함)
- **Occupied Area 정의**: 각 Node의 Bounding Box는 이미지 자체의 크기만으로 판단하지 않는다 — 이미지
  주변에 확보해야 하는 최소 Safety Gap까지 포함한 **Occupied Area**를 그 Node의 실제 점유 영역으로
  본다. 배치·간격 계산은 이미지 원본 크기가 아니라 이 Occupied Area를 기준으로 한다.
- 다른 Node(이미지+라벨)나 Connector는 이 Occupied Area 안으로 들어오지 않도록 배치한다 — 이미지끼리
  시각적으로 겹치지 않는 것만으로는 충분하지 않고, Safety Gap을 포함한 Occupied Area 전체를 침범하지
  않아야 한다.
- 서로 다른 Process/Material/Output 이미지는 각자의 Occupied Area가 맞닿거나 거의 붙어 두 개의 개별
  Node가 하나의 요소처럼 보이지 않도록, 명확한 시각적 Gap을 확보한다(단, 의도적으로 하나의 Node로
  묶이는 Output Group 내부는 예외 — 아래 Output Group 항목의 내부 간격 규칙을 따른다).
- Process가 Connector 위에 뜨는 구조(위 "공정 라벨·이미지와 Connector의 수직 배치 규칙" 참조)에서는,
  Connector와 Process Image 사이, 그리고 Process Image와 Process Label 사이 **각각**에 충분한 세로
  Gap을 확보한다 — 두 구간의 Gap을 하나로 합쳐 어느 한쪽에만 여백을 몰아주지 않는다.
- Flow를 설명하는 주요 Material/Process/Output 이미지는 가독 가능한 최소 크기를 확보한다 — 공간이
  부족하다는 이유로 이미지를 과도하게 축소하지 않는다. Layout Reference(L25, 위 "0. 역할 구분" 참조)에서
  확인되는 이미지-대비-영역 상대 크기를 기준으로 삼아, 그보다 눈에 띄게 작아져 시각적 존재감이 약해지지
  않도록 한다.
- 동일 위계의 Node 이미지(예: 같은 Lane 안의 여러 Process 아이콘, 같은 Output Group의 개별 이미지)는
  서로 유사한 체감 크기를 유지한다 — 같은 위계인데 노드마다 크기가 들쭉날쭉하지 않게 한다.
- 여러 항목으로 구성된 Output Group은 개별 이미지를 나란히 배치하되, 그룹 전체가 **하나의 Node**로
  인식되도록 항목 간 간격과 정렬을 통일한다(개별 이미지 간 간격이 Node와 Node 사이 간격만큼 벌어지지
  않게 한다 — Output Group 내부 간격은 서로 다른 Node 사이 Gap보다 눈에 띄게 좁아야 그룹으로 인식된다).
- **공간 부족 시 우선순위**: 공간이 부족한 경우 **이미지 크기를 먼저 줄이지 않는다** — Node 간 X/Y
  간격 및 사용 가능한 Body 공간(Region Map §0 범위 안에서의 여백 재배분)을 먼저 조정하고, 그래도
  부족하면 위 "밀도/크기 규칙"의 순서(텍스트 줄바꿈 → 여백 최소화 → 슬라이드 폭 활용)를 따르며, 라벨
  텍스트를 14pt 미만으로 줄이지 않는 원칙(위 "밀도/크기 규칙" 참조)과 동일하게 이미지도 가독성 최소
  기준 아래로 줄이지 않는다.
- 구체적인 이미지 크기는 px 고정값으로 강제하지 않는다 — Region Map(§0)이 정의하는 각 영역의 폭·높이
  대비 이미지가 차지하는 비율을 기준으로 콘텐츠 분량에 맞게 범용적으로 판단한다.
- **검증 기준**: 최종 렌더링 QA에서는 실제 Bounding Box(Occupied Area 기준)가 겹치는 경우뿐 아니라,
  겹치지는 않아도 서로 다른 Node가 지나치게 가까워 하나의 요소처럼 보이는 경우도 위반으로 판정한다
  (단, 의도적으로 하나의 Node로 묶이는 Output Group 내부는 제외).

## 구간 구분선 규칙
- 카테고리(예: 1세대/2세대) 구간 사이를 가로로 구분해야 하는 경우, 얇고 중립적인 톤(Neutral Gray/Slate 계열)의
  점선을 사용한다.
- Hard Rule §11 Vertical Content Divider는 **세로** Divider 전용 규정이므로, 이 가로 구분선을 §11의
  컴포넌트로 간주하거나 §11이 정의하는 세로 Divider 색상(#034443 Gradient)을 그대로 가져오지 않는다 —
  성격이 다른 별도 요소다. 두께감·절제된 톤이라는 방향성만 §11의 취지와 맞춘다.

## 분기 구조 대칭 규칙
- 하나의 공통 시작점에서 여러 갈래로 분기하는 구조라면, 공통 시작점을 기준으로 각 갈래는
  대칭적인 간격을 두고 배치한다. 한쪽으로 치우치지 않도록 한다.
- 구체적인 대칭 배치(Lane 높이 비율, 분기 지점의 좌우/상하 위치 등)는 L25 Layout Reference(위 "0. 역할
  구분" 참조)의 공간 구조를 비례 기준으로 삼는다.

## Output Group / Sibling Outputs Branch 판별 규칙
- 하나의 Process에서 결과물이 2개 이상 나온다고 해서 **항상 각각을 Branch로 분리하지 않는다** — 복수
  Output = 자동 Branch로 판단하지 않는다. Branch를 만들기 전에 먼저 아래 기준으로 관계를 판별한다.
- **Output Group**(단일 Connector로 그룹 전체를 하나의 목적지로 연결): 여러 결과물이 서로 **동일
  카테고리·동일 위계**이고, 그중 어느 것도 **별도의 후속 Process로 이어지지 않는** 경우. 이 경우 Output
  Group 내부의 개별 항목 사이에는 Branch Connector를 만들지 않는다 — 하나의 Connector가 그룹 전체를
  하나의 목적지로 연결하고, 그룹 내부는 위 "Node 이미지 최소 크기 및 공간 확보 규칙 (Occupied Area 포함)"에
  따라 나란히 배치해 하나의 Node처럼 인식되게 한다.
- **Sibling Outputs Branch**(아래 "복수 결과물 분기 규칙" 적용): 결과물들이 서로 **다른 후속 경로**를
  갖거나(하나는 여기서 끝나고 다른 하나는 다음 Process로 이어지는 등) **의미적으로 독립된 별개의 결과**로
  구분되는 경우에만 사용한다.
- 이 판별은 Flow Graph 선해석 단계(위 "생성 전 Output 관계 판별")에서 Branch Point를 그리기 전에
  먼저 끝낸다 — 판별 없이 결과물이 여럿이라는 이유만으로 곧바로 Branch Point부터 그리지 않는다.

## 복수 결과물 분기 규칙 (Sibling Outputs)
- 위 판별 결과 **Sibling Outputs Branch**로 확정된 경우에만 아래를 적용한다 — Output Group으로 판별된
  결과물에는 이 절의 Branch 구조를 적용하지 않는다(바로 위 "Output Group / Sibling Outputs Branch
  판별 규칙" 참조).
- 하나의 Process에서 2개 이상의 결과물이 발생하는 경우, 결과물끼리 `Process → Output A → Output B`처럼
  **순차적으로 연결하지 않는다.**
- 대신 해당 Process 이후 **하나의 공통 Branch Point**에서 Connector를 분기해 각 결과물로 독립적으로
  연결한다 — `Process → Branch Point → Output A / Output B` 형태를 사용한다.
- 각 Output은 동일한 Process에서 발생한 **병렬 결과물(Sibling Outputs)**로 취급한다 — 서로 우선순위나
  순서 관계가 있는 것처럼 표현하지 않는다.
- 이 규칙은 위 Region Map의 "결과물(Result) 영역" 안에서 그 영역에 여러 결과물을 배치할 때 적용되는
  세부 Connector 구조이며, Region Map의 영역 비율 자체를 변경하지 않는다. 1차 분기점·2세대 내부 재분기점
  (Region Map, 카테고리/갈래 단위 분기)과는 별개의, **Process 단위의 소규모 분기**다 — 동일한 "공통
  Branch Point에서 분기" 원칙을 더 작은 스케일로 적용한 것뿐이며 서로 충돌하지 않는다.

## 라벨 텍스트 위치 규칙
- 각 결과물/그룹의 공통 라벨은 해당 아이콘(들) 아래쪽에 배치하는 것을 기본으로 한다.
  (프롬프트에서 별도로 위/아래를 지정하지 않은 경우 아래쪽 배치가 기본값)

## 구현 골격 (Implementation Skeleton, 참고용)
> 이 골격은 위 규칙들을 코드 구조로 옮기는 방식을 보여주는 참고용 예시일 뿐, 특정 슬라이드의 단계명·이미지를 하드코딩하지 않는다(문서 서두 원칙과 동일). Process+Comparison(`process-stage`/`process-arrow`)이나 Before-After(`ba-step-box`/`ba-connector`)의 기존 컴포넌트를 이 골격 대신 가져다 쓰지 않는다 — 이 문서의 Connector 연속성·Branch Point·Process/Material 구분 규칙은 그 컴포넌트들의 구조(고정 폭 chip을 화살표 사이에 끼워 넣는 방식)와 다르다.

핵심 구조는 세 레이어로 분리한다.
1. **Connector 레이어(SVG, 단일)**: `viewBox="0 0 100 100" preserveAspectRatio="none"`로 Body Box 전체를 덮는 SVG 하나에 모든 Trunk/Branch/Lane Connector를 그린다. 좌표는 위 Region Map의 %를 그대로 0~100 값으로 사용하므로, 아래 Node 레이어의 `left`/`top` %와 동일한 좌표계를 공유한다(별도 환산 불필요).
   - Trunk: 공통 시작 Node의 오른쪽 끝 X부터 Branch Point 직전까지만 그린다(Node를 관통하지 않음).
   - Branch: 정확히 하나의 Branch Point 좌표에서 각 Lane으로 향하는 곡선을 각각 그리되, 모든 곡선이 같은 시작점(X/Y)을 공유하게 한다(Branch Point 구조 보존 규칙).
   - Lane 내부: 해당 Lane의 시작 Material Node 오른쪽 끝부터 결과물(Output) Node 왼쪽 끝까지 **하나의 끊기지 않는 선**으로 그린다 — 그 사이에 있는 Process는 이 선을 끊지 않는다(Process 처리 방식).
2. **Material/Intermediate/Output Node 레이어**: 텍스트 라벨(+이미지가 있으면 이미지)을 절대좌표 `div`로 배치한다. 이 Node의 Bounding Box는 위 Connector 레이어가 지나가지 않는 지점에 위치해야 한다 — Connector 좌표를 계산할 때 이 Node의 좌우 경계를 기준으로 선을 끊는다.
3. **Process Node 레이어**: 해당 Lane의 Connector Y좌표보다 **위쪽**(Y값이 더 작은 위치)에 절대좌표로 배치한다. Connector 선과 겹치지 않도록 세로 Gap을 확보한다. 이미지가 있으면 라벨 위/아래에 함께 배치하되 순서는 "공정명 → 이미지 → (Connector)"를 따른다.

```html
<div class="flow-field" style="position:relative;">
  <svg class="flow-connectors" viewBox="0 0 100 100" preserveAspectRatio="none"
       style="position:absolute; inset:0; width:100%; height:100%;">
    <!-- Trunk: 공통 시작 Node 오른쪽 끝 → Branch Point 직전 -->
    <path d="M{trunkStartX},{trunkY} L{branchX},{trunkY}" class="flow-connector-line"/>
    <!-- Branch: 동일한 Branch Point에서 각 Lane으로 -->
    <path d="M{branchX},{trunkY} C ... {laneAStartX},{laneAY}" class="flow-connector-line"/>
    <path d="M{branchX},{trunkY} C ... {laneBStartX},{laneBY}" class="flow-connector-line"/>
    <circle cx="{branchX}" cy="{trunkY}" r="1.2" class="flow-branch-point"/>
    <!-- Lane 내부: Material 오른쪽 끝 → Output 왼쪽 끝, Process로 끊지 않음 -->
    <path d="M{laneAMaterialEndX},{laneAY} L{laneAOutputStartX},{laneAY}" class="flow-connector-line"/>
  </svg>

  <!-- Material/Output Node: Connector가 지나가지 않는 자리에 배치 -->
  <div class="flow-node-label" style="position:absolute; left:{laneAMaterialX}%; top:{laneAY}%; transform:translateY(-50%);">라벨</div>

  <!-- Process Node: Connector보다 위쪽, 화살표 chip으로 끼워 넣지 않는다 -->
  <div class="flow-process-box" style="position:absolute; left:{processX}%; top:{laneAY - gap}%; transform:translate(-50%,-100%);">공정명</div>
</div>
```

- `{}`로 표시된 값은 실제 구현 시 이 문서의 Region Map(§0)과 슬라이드별 input에 따라 계산한다 — 하드코딩된 예시 수치가 아니다.
- `.flow-connector-line`/`.flow-branch-point`/`.flow-process-box`는 `style.css`에 프로젝트 공통 클래스로 이미 정의되어 있으면 재사용하고, 없으면 Hard Rule·Claude PPT Design System의 색상/두께 토큰을 그대로 적용해 새로 추가한다 — 색상·두께 자체를 이 문서가 새로 정의하지 않는다(위 "색상 대비 규칙"·Design System 우선).
