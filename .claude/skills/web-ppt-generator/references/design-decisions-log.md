# Design Decisions Log

이 문서는 `web-ppt-generator/SKILL.md`의 특정 규칙이 왜 생겼는지 근거가 된 과거 Field Test 회귀 사례를 모아둔 곳이다. **판단 기준 자체는 SKILL.md 본문에 그대로 있다** — 이 로그는 그 판단 기준을 매 [5]/[7] 호출마다 다시 읽을 필요가 없는 배경 설명으로 분리한 것뿐이며, 규칙을 이해하거나 실행하는 데 필수는 아니다. 규칙의 적용 방식 자체가 의심스럽거나("왜 이렇게까지 엄격한가") 새 사례를 이 문서에 추가할지 판단해야 할 때만 참조한다.

각 항목은 SKILL.md 본문에서 `(사유: design-decisions-log.md#앵커)` 형태로 역참조된다.

---

## flow-diagram-region-map-drift
**관련 규칙**: "전용 Layout의 구조 규칙 우선 적용 (Dedicated Layout Structure Enforcement)"

2026-08-24, `cosolus-ir-deck-F` Slide 16에서 Selected Layout은 정확히 Flow Diagram(L25)이었으나 실제 HTML은 그 문서의 Region Map·Connector 규칙 대신 다른 Layout용 범용 컴포넌트를 그대로 가져다 쓴 사례가 있었다. Selected Layout이 전용 Layout Reference 문서를 가리킬 때 그 문서의 Region Map·Connector 처리 방식을 "참고용 예시"가 아니라 "구현 명세"로 취급하도록 규칙을 강화한 계기다.

## l07-primary-visual-reversed
**관련 규칙**: "Primary/Optional Visual의 Region 배치"

2026-08-25, `cosolus-business-plan-2026` Slide 3에서 L07의 좌=Main Visual/우=Text 구조가 반전되고, Optional 보조 이미지를 넣기 위해 Primary Visual까지 축소된 사례가 있었다. Optional/Supporting Visual을 위해 원본 Reference의 Main Region 좌우 관계를 반전하거나 Primary Visual을 축소하지 않도록 규칙을 강화한 계기다.

## shared-visual-region-uneven-boxes
**관련 규칙**: "이미지 표시 크기·시각적 위계 > 과소 활용 금지(Visual Region Utilization)"

2026-08-25, `cosolus-business-plan-2026` Slide 11에서 그림6·7을 균등 폭 회색 박스에 강제로 맞춰 실제 이미지가 절반 이하 크기로 줄어든 사례가 있었다. 여러 이미지가 하나의 Visual Region을 공유할 때 동일한 박스 크기를 기계적으로 강제하지 않도록 규칙을 강화한 계기다.

## html-css-implementation-defects
**관련 규칙**: "구현 기준 (HTML/CSS Implementation Standards)" 전체(한글 줄바꿈/Divider 서브픽셀/Table 동일 폭 Column/아이콘 렌더링)

2026-08-19, C 테스트 `cosolus-ir-deck-C`에서 여러 슬라이드·레이아웃에 걸쳐 반복 발생한 구현 결함(단어 중간 줄바꿈, 서브픽셀 Divider 소실, Table Column 폭 불일치, 컬러 이모지 렌더링 등)을 공통 기준으로 정리해 이 섹션이 만들어졌다.

## shared-component-reinvention
**관련 규칙**: "공용 컴포넌트 재사용 (Shared Component Reuse)" 전체

2026-08-25, `cosolus-business-plan-2026` Field Test에서 아래 세 가지가 반복 확인됐다:
- Insight/Conclusion Box가 슬라이드마다 다른 border 방식으로 재발명됨
- Body 텍스트가 슬라이드별로 14~15pt로 임의 축소됨
- 이미 있는 Stat Number 공용 클래스를 두고도 슬라이드 전용 클래스로 동일 값이 중복 재정의됨

이 세 가지 재발명·중복·임의 축소를 막기 위해 "공용 클래스 통합", "Body Text는 Typography Tier 그대로 사용", "이미 있는 공용 클래스 우선 재사용" 규칙이 만들어졌다.

## image-display-size-by-role
**관련 규칙**: "이미지 표시 크기·시각적 위계(Image Display Size)" 전체, `flow-diagram-rules.md` "구조 정렬과 이미지 표시 크기의 구분", slide-structuring 2단계 "이미지별 시각 역할"

2026-10-08, `cosolus-ir-deck-G` Slide 1(공정 흐름도)에서 Node 종류별 고정 `max-width`×`max-height` 박스(예: Process 72×46px) 때문에 여러 단계가 담긴 가로형 공정 도해(유도가열 3단계 등)가 정사각형 시료 사진과 같은 크기로 축소돼 단계를 식별하기 어려웠다. 규칙상 "동일 위계 Node 유사 체감 크기"가 Node 종류 기준으로 해석됐고, 이미지별 시각 역할·정보 밀도는 [3] 산출물에 기록되지 않아 [5]에서 구분할 근거가 없었다. 같은 조사에서 `object-fit: cover`로 콘텐츠 사진이 최대 47% 잘리고, pptx 변환기가 `object-fit`을 무시해 그 이미지들을 최대 88% 늘려 넣던 사례(`cosolus-ir-deck-B` final.pptx)도 확인됐다. 이미지 중요도를 원본 크기·비율이 아니라 역할·정보 밀도·판독성으로 판단하고, 컨테이너 정렬과 이미지 표시 크기를 분리하며, 원본 비율 유지를 QA·pptx 변환까지 일관되게 적용하도록 정리한 계기다.

## flow-visual-composition
**관련 규칙**: `flow-diagram-rules.md` "Visual Composition — Lane Band·연결점·구분선", qa_render.py `flow_issues`

2026-10-12, `cosolus-ir-deck-G` Slide 1에서 이미지 크기만 역할별로 조정하자 배치 문제가 드러났다. 폐흑연 화살표의 불필요한 Z자 꺾임, 건식환원 이미지를 가로지르는 구분선, 소속 Lane이 모호한 유도가열 이미지, COSOLUS(2세대) 박스와 분기 브래킷의 겹침, 상단 결론 헤드라인에 가까운 Lane A 콘텐츠, 회수 화합물·폐흑연의 서로 다른 중심축이다. 원인은 다섯 가지였다. (1) Process가 연결선 위로만 쌓이는데 위쪽 공간 한도가 없었다. (2) Material Node는 이미지+라벨 블록 중심을 Lane에 맞춰서 이미지 높이가 바뀌면 연결점이 어긋났다. (3) 구분선이 고정 좌표였다. (4) PNG 투명 여백 때문에 박스 기준 간격과 보이는 간격이 달랐다(유도가열 이미지 하단 26%가 투명). (5) QA가 화살촉 marker 때문에 Connector 오버레이를 장식으로 판정하지 못해 오탐 32건만 내고 실제 충돌은 잡지 못했다. 그래서 가용 공간 → 이미지 크기 → Node 위치 → Connector → 구분선을 한 절차로 계산하도록 정리했다.
