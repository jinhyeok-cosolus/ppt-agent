# Field Test Pattern Library

> 이 문서는 과거 `output/`의 Field Test(실제 생성·검토·확정 이력)를 근거로 "이런 콘텐츠 구조·분량이면 과거에 어떤 Layout/Variant가 실제로 잘 작동했는가"를 정리한 참고 자료다.
>
> **역할 분리**(CLAUDE.md 2장 참조):
> - **Pattern Library(이 문서)** = 과거 근거로 무엇을 선택할지 참고
> - **Layout MD**(`docs/slide-design-rules/*.md`) = 선택한 Layout을 어떻게 구현할지
> - **Hard Rule**(`docs/design-hard-rules/`) = 모든 슬라이드가 반드시 지킬 기준
>
> 이 문서는 Layout MD를 대체하지 않는다. Layout MD에 이미 있는 구현 규칙(색상·좌표·타이포)은 반복하지 않고, Layout MD가 다루지 않는 **"왜 이 Variant를 골랐는가"**·**"비슷해 보이지만 실패한 시도"**만 기록한다.
>
> **적용 원칙**: 과거 사례와 충분히 유사하지 않은 콘텐츠에는 아래 Pattern을 억지로 적용하지 않는다. 그런 경우 `.claude/skills/web-ppt-generator/references/design-rules.md`의 기존 Layout Selection Logic(Relationship → 정보 구조 → 항목 수 → 후보 매칭)을 그대로 사용한다. 이 문서는 그 절차 중 "후보가 여럿 남았을 때의 참고 근거"로만 개입한다.

## 신뢰도 표기 기준

| 표기 | 의미 |
|---|---|
| **높음** | `final.pptx` 도달 또는 사용자가 명시적으로 확정(Human Review 승인)한 버전에서 관찰됨 |
| **중간** | 사용자가 확정했으나 pptx 미변환, 또는 회귀 테스트/재검증에서 반복 확인됨 |
| **낮음(추정)** | `state.json`/Human Review 기록이 없어 최종본을 확정할 수 없음 — 파일명 순서·최신 수정 시점 등 정황 증거만 있음. 참고는 하되 단독 근거로 확정 판단하지 않는다 |

---

## 1. Three-Column — 3개 대등 병렬 항목

- **Content Relationship**: 병렬(대등한 위계, 순서 강제 불필요)
- **Content Density**: 항목당 짧은 메시지(수치 근거 없어도 됨)
- **항목 수**: 정확히 3
- **Visual**: Icon + Message (원문에 세부 이미지 없을 때도 성립)
- **강조 정보**: 3개 항목이 완전히 동등한 위계라는 것
- **최종 확정 Layout/Variant**: `three-column/three-column.md` — Header Bar 48px edge-to-edge, Key Message 78% 폭, Divider는 Body 영역에만 적용
- **Use When**: 병렬 항목이 정확히 3개이고 순차/인과 관계가 아님
- **Avoid When**: 실제로는 2-Column 비교인데 항목을 억지로 3개로 쪼개거나, 4개 이상을 3개로 합쳐 정보 손실 발생
- **Field Test 근거**: `cosolus-ir-deck` A/B/C 3개 프로젝트가 같은 슬라이드(비즈니스 모델 3축)에서 독립적으로 동일 선택 수렴 — **높음**. `cosolus-business-plan-2026`에서 Header/Body 간 gap 공유로 Divider가 누락되는 구조적 버그 발견 → Header/Body 행 분리로 재작성 후 공용 컴포넌트화 — **높음**(구현 결함이지 Variant 선택 오류 아님, 참고용).

---

## 2. Before-After — Variant A(공정/구조 변화 자체가 메시지)

### 2-A. 단일 경로형 (Existing 1개 흐름 → Improved 1개 흐름)

- **Content Relationship**: 비교(정확히 2개: 기존 vs 개선), 공정 단계 수·구성 자체가 핵심
- **Content Density**: 정성 설명 위주, 정량 수치 없어도 사용 가능
- **항목 수**: 2 Column, 각 Column 내부 단계 수는 자유(비대칭 허용 — 예: 4단계 vs 1단계)
- **Visual**: Image↔Image(화학구조식 등) 또는 Process/Step Sequence 다이어그램, 중앙 Transformation은 실제 2-layer Chevron 이미지 자산 사용(CSS로 그리지 않음)
- **강조 정보**: 단계 수/복잡도 차이(Comparison Marker Pair)
- **최종 확정 Layout/Variant**: `before-after/before-after.md` Variant A
- **Use When**: 비교 대상이 정확히 2개이고, 메시지의 핵심이 "무엇이 얼마나"가 아니라 "구성 자체가 어떻게 달라졌는가"일 때
- **Avoid When**: 순수 텍스트 화살표(`→`/`↓`)로 대체하거나 Chevron 이미지 자산을 생략하는 초기 방식 — 이후 Reference 기반 이미지 방식으로 전면 교체됨
- **Field Test 근거**: `cosolus-ir-deck` A/B/C가 Slide 6(추출제)/8(DLE)/11(2세대 공정)에서 3개 프로젝트 독립 판단 수렴, `final.pptx` 도달 — **높음**. `cosolus-before-after-process-test`(4단계→1단계, 텍스트 화살표)는 최초 시도로, 이후 이미지 기반 방식에 완전히 대체된 초기 실험 — **낮음(추정), 참고용 avoid 사례로만 사용**.

### 2-B. 분기형 (Existing 1개 흐름 → Improved 내부에서 비대칭 2경로로 분기)

- **Content Relationship**: 비교(기존 vs 개선)이되, 개선 쪽이 하나의 분기 원점에서 서로 다른 길이의 두 경로로 갈라짐(예: 고순도 등급 2-step / 범용 등급 4-step)
- **Content Density**: 단계별 이름 + 선택적 1줄 보조 라벨
- **항목 수**: Existing 4~5단계(단일 흐름) vs Improved 2경로(길이 비대칭, 가장 긴 흐름 기준 Pitch Grid 계산)
- **Visual**: 텍스트/보더 박스 + 커넥터 라인, 두 경로는 동일 Y 시작점(분기 원점) 공유
- **강조 정보**: 분기해도 총 복잡도 대비 개선이라는 점, 두 경로가 같은 원점에서 시작한다는 것
- **최종 확정 Layout/Variant**: `before-after/before-after.md` §4.3(Pitch)/§4.4(분기)
- **Use When**: 개선안이 조건별로 두 갈래 이상의 대응을 요구할 때(예: 원료 등급별 분리 처리)
- **Avoid When**: **두 분기의 Comparison Marker(Bracket 등)를 시각적 정렬을 위해 임의로 Y-위치를 맞추지 않는다** — 원본 Reference 측정값(예: 51px 오프셋)이 애초에 정렬을 의도하지 않았다면, 억지 정렬이 "분기 원점 공유" 원칙을 깨뜨림. 실제로 시도했다가 되돌린 사례 있음.
- **Field Test 근거**: `cosolus-before-after-variant-a-test/quick-test.html`(배터리 금속 회수, COSOLUS 실도메인) — `quick-test-priority-recheck.html`에서 우선순위 규칙 변경 후에도 구조 변경 없이 재검증 통과 — **중간**. `cosolus-before-after-rule-update-test`에서 Bracket 정렬 시도 → 4차 수정에서 명시적으로 되돌림(avoid 사례) — **중간**.

---

## 3. Before-After — Variant B(다수 공유 기준 정량 비교)

- **Content Relationship**: 비교(정확히 2개 대상)이지만 3~7개의 **공유 비교 기준(criteria)**으로 반복 비교
- **Content Density**: 기준당 1개 수치
- **항목 수**: Criteria Column + Existing/Improved 2 Column = 사실상 3열 Comparison Table. 기준 수 3~6개 권장, 7개는 상한 근접 위험(우선순위 낮은 기준 통합 검토)
- **Visual**: Table 형태 Comparison Frame, Criteria Row 필수
- **강조 정보**: "무엇이 얼마나 개선되는가"를 항목별로
- **최종 확정 Layout/Variant**: `before-after/before-after.md` Variant B
- **Use When**: 비교 대상이 정확히 2개 + 다수 동일 기준. 대상이 3개 이상이면 §4(Table Comparison/Comparison Matrix)로 분기
- **Avoid When**:
  - 원문에 없는 경쟁사명/수치를 다른 참고자료의 예시(예: BTR/Vianode)에서 그대로 가져오지 않는다.
  - Selected Layout 문서에는 Variant B로 기록해놓고 실제 HTML은 Criteria Row 없는 임의 2-Column으로 구현하는 괴리를 만들지 않는다 — 전용 Layout의 Must Preserve 체크리스트는 **HTML 생성 이전에** 발췌해 반영해야 하며, QA 시점에야 발견하면 늦다.
- **Field Test 근거**: `cosolus-ir-deck` A/B/C Slide 13(경쟁력—가격·기술 우위), `final.pptx` 도달 — **높음**. `cosolus-business-plan-2026` Slide 7에서 위 avoid 사례(Criteria Row 누락) 발생 → §5.1 Region Map대로 3-Column `<table>`로 재구현, 6차 수정 끝에 확정 — **중간**(사용자 확정, pptx 미변환).

---

## 4. Comparison Matrix / Table Comparison — 3개 이상 대상 × 공유 기준

### 4-A. Comparison Matrix (Visual/근거 중심, 혼합 셀 타입)

- **Content Relationship**: 복수 비교 근거, 자사 vs 경쟁사 N개(3~4개 권장)
- **Content Density**: 기준별로 셀 표현 타입이 다를 수 있음(문단/KPI 수치/뱃지/불릿 등 혼재 가능, 단 같은 Row 안에서는 열 간 타입 일관 유지)
- **항목 수**: 3~4 대상 × 4~5 기준
- **Visual**: 이미지/다이어그램 없이 텍스트·KPI·뱃지 중심, 자사 열은 아웃라인+하이라이트 배경(공용 컴포넌트 `019_competitive-advantage-highlight.md`)으로 강조
- **강조 정보**: 자사 기술의 전 지표 우위 — 단, 열세인 지표(예: 낮은 TRL)도 숨기지 않고 그대로 유지
- **최종 확정 Layout/Variant**: `comparison-matrix/comparison-matrix.md`
- **Use When**: 정성 설명·주석이 많아 정확한 문장/수치를 있는 그대로 읽어야 할 때(Multi-Radar 등 시각 압축형 Layout은 이런 경우 Do Not Use)
- **Avoid When**: 데이터 양이 많다는 이유만으로 자동으로 Matrix/Table을 선택하지 않는다 — **모든 대상이 공유하는 공통 Row/Column 비교축이 실제로 존재할 때만** 이 계열을 선택한다. 비교축이 없는데 표로 강제하면 정보를 왜곡한다.
- **Field Test 근거**: `cosolus-comparison-matrix-test/quick-test.html`(COSOLUS vs 경쟁사 A/B/C, 5기준×4열, 혼합 셀 타입) — 단일 인스턴스, `state.json` 없음 — **낮음(추정)**. `cosolus-ir-deck` A/B/C Slide 7/9(3사/4방식 비교), 열 폭 불일치 결함 발견 후 `colgroup`+`table-layout:fixed`를 공통 규칙으로 승격, D-test 회귀 검증 완료 — **높음**.

### 4-B. Table Comparison (값 읽기 중심, Visual 최소)

- **Content Relationship**: 복수 비교 근거지만 Visual이 보조이고 텍스트·수치·평가값을 "읽는 것" 자체가 핵심
- **Content Density**: 셀당 하나의 짧은 값(문단/이미지 없음)
- **항목 수**: 3개 대상 × 4개 기준 예시 확인(1px hairline divider, 자사 열은 좌측 보더+미세 틴트+볼드로만 구분, 카드/그림자 없음)
- **최종 확정 Layout/Variant**: `table-comparison.md`
- **Use When**: Comparison Matrix와의 경계 — 값 읽기가 핵심이면 Table Comparison, Visual 근거(차트/뱃지 등)가 필요하면 Comparison Matrix
- **Avoid When**: 세대 비교처럼 비교축이 다른 데이터(예: 기존 5단→COSOLUS 4단)를 억지로 같은 표의 4번째 열로 합치지 않는다 — Highlight Band 등으로 분리
- **Field Test 근거**: `cosolus-table-comparison-test/quick-test.html` — 단일 인스턴스, `state.json` 없음 — **낮음(추정)**. 경계 판단 규칙 자체는 `cosolus-business-plan-2026` 조사에서 보강 확인 — **중간**.

---

## 5. Benefit-Impact — 하나의 기술 → 정확히 2개의 정량 개선 효과

- **Content Relationship**: 인과(Core Technology → Improvement → Quantified Impact) + 병렬(정확히 2개 효과)
- **Content Density**: 상단 강점 요약(3~4개, 선택) + 좌우 각각 Before/After 수치
- **항목 수**: **정확히 2** — 3개 이상이면 이 Layout에 적합하지 않음(§8 참조, 미해결 공백)
- **Visual**: Large Number Before→After. Evidence 형식은 고정하지 않고 콘텐츠에 따라 매번 선택:
  - Chart(막대+화살표) ↔ Compare-Bars(가로 이중 바 + delta 라벨, 예: 94%→99% "+5%p 향상") 조합이 실제 검증된 조합
  - 한쪽 효과에 정성 지표(예: 공정 안정성: 보통→우수)가 섞여 있으면 그 쪽만 Compact Table(2~3열)로 교체 가능
- **강조 정보**: 두 정량 효과 모두 하나의 대표값으로 뭉개지 않고 동일 비중으로 보존
- **최종 확정 Layout/Variant**: `benefit-impact/benefit-impact.md`
- **Use When**: 하나의 기술이 만드는 정확히 2개의 정량 개선 효과
- **Avoid When**: **두 기여 요소 중 하나만 대표 Large Number로 강조하고 나머지를 하단 보조 문장 한 줄로 축소하지 않는다** — 실제로 이 실수가 발생했다가(v1) Claim→Evidence→Relationship 구조화 단계 도입 후 두 값 모두 동일 비중의 2-bar Contribution 시각으로 재구성된 사례(v2) 있음.
- **Field Test 근거**: `cosolus-ir-deck` A/B/C Slide 10, `final.pptx` 도달 — **높음**. `cosolus-ir-deck-D` v1→v2 회귀 비교 문서가 위 avoid 사례를 정확히 기록 — **중간**(회귀 테스트, Human Review 미완료이나 진단 신뢰도 높음). `cosolus-benefit-impact-test`의 Chart+Compare-Bars 조합(`quick-test.html`, priority-recheck에서 재확인) — **중간**. Compact Table 대체(`quick-test-table-evidence.html`)는 병행 탐색 버전으로 우열 미확정 — **낮음(추정)**.

**미해결 공백(§8)**: "구성요소별 기여도(3개 이상)"나 "순환 관계"가 슬라이드 **전체**의 Primary Content인 경우를 위한 전용 Layout이 카탈로그에 없음이 D-test에서 확인됨. 국소 영역(Column 1개 등)에 한정된 기여도/순환 구조는 기존 Layout 내부 재구성(SVG cycle diagram, contribution bar)으로 해결 가능했으나, 전체 슬라이드 단위는 미검증 — 이런 콘텐츠를 만나면 이 Pattern Library를 억지로 적용하지 말고 기존 Layout Selection Logic으로 판단할 것.

---

## 6. Process + Comparison / Process-System-Architecture — 공정 흐름 → 하단 Insight로 수렴

- **Content Relationship**: 순차(공정 흐름) + 인과(공정→성과)
- **Content Density**: 상단 다단계 프로세스(3~7단계, 각 단계 아이콘/다이어그램 + 이름 + 짧은 보조 라벨) + 하단 1~2개 핵심 성과 수치 또는 2-Side 비교
- **항목 수**: 상단 단계 수 가변, 하단 결론/비교는 통상 1~2개. 상하 비율 예시: 56:44 또는 60:40
- **Visual**: 상단 Process Flow(실사진 있으면 우선 사용, 없으면 SVG Icon/Diagram — 원 번호 아이콘보다 Icon/Diagram이 더 검증됨) + 하단 Insight Box(배경·테두리 있는 종합 결론) 또는 Flat/Open 2-Column 비교(Rounded Card 스타일보다 우선)
- **강조 정보**: 특정 단계(Process Callout — 강조색+밑줄)가 하단 비교/Insight의 직접적 원인임을 시각적으로 연결
- **최종 확정 Layout/Variant**: `process-comparison/process-comparison.md`, `process-system-architecture-layout.md`
- **Use When**: 여러 단계 공정이 하단 핵심 Insight/비교와 직접 연결될 때. 실사진 커버리지가 낮으면(80% 미만) 이미지 없는 변형 채택
- **Avoid When**:
  - 하단 Insight Box(배경·테두리, Output/Customer Value 종합)를 얇은 텍스트 라벨로 축소하지 않는다 — 실제 이탈 사례 있음(원인: 전용 Layout Must Preserve 체크리스트를 생성 *이후* QA에서야 확인해 조용히 단순화되는 경로가 있었음. → 체크리스트를 생성 *이전*에 사전 발췌하는 규칙으로 보완됨)
  - 의미가 불명확한 장식적 화살표/역방향 피드백 커넥터는 정보 전달에 기여하지 않으면 제거한다
  - 하단 비교를 Rounded Card로 감싸는 "일반적 웹 UI"식 처리보다 Flat/Open(중앙 divider) 스타일이 더 검증됨 — 상단 원 번호 아이콘도 Icon/Diagram 방식으로 대체된 이력 있음
- **Field Test 근거**: `cosolus-ir-deck` A/B/C Slide 5, 12, `final.pptx` 도달 — **높음**. `cosolus-business-plan-2026` Slide 12 Insight Box 이탈→수정 사례 — **중간**. `cosolus-process-comparison-test/quick-test.html`(4단계 흐름 + 강조 단계 + 하단 2-Side 비교, v1→v2 파일 내 주석으로 리비전 기록) — **중간**(단일 파일이나 개선 근거가 명확히 문서화됨).

---

## 7. 병렬 배경 설명 (Market/Problem) — 정보량 비대칭 허용

- **Content Relationship**: 병렬(2개의 독립적 배경 요인) — Before/After 대립도 아니고 정확히 3개 병렬도 아님
- **Content Density**: 한쪽은 다수 수치(예: 4개 통계), 다른 쪽은 단일 스탯만 있는 비대칭이 흔함
- **항목 수**: 좌우 2 Region
- **Visual**: 좌측 수치+지도/이미지, 우측 Large Number 단일 스탯 + 문장 (또는 그 반대 — 원본 Reference의 좌우 방향을 그대로 따른다)
- **강조 정보**: 정보량이 적은 쪽을 가짜 수치로 채우지 않고 스탯 크기·문장 배치로만 시각 균형을 보완
- **최종 확정 Layout/Variant**: `L07 Market/Problem`(레이아웃 카탈로그) 또는 `visual-insight.md` Variant B/C
- **Use When**: 두 배경 요인이 병렬이되 정보량이 본질적으로 다를 때
- **Avoid When**:
  - 원본 Reference의 좌우 배치를 임의로 반전하지 않는다
  - "공간이 남는다"는 이유만으로 Optional 보조 이미지를 Required 요소와 한 Column에 욱여넣어 크기를 과도하게 축소하지 않는다(Supporting Visual Value 원칙)
  - 이미지 출처/캡션을 본문처럼 이미지 바로 아래 반복 배치하지 말고 하단 공통 Footnote 영역으로 분리한다
- **Field Test 근거**: `cosolus-ir-deck` A/B/C Slide 3, `final.pptx` 도달 — **높음**. `cosolus-business-plan-2026` Slide 3에서 좌우 반전 + Optional 이미지 욱여넣기 이탈 → 여러 라운드 끝에 원본 방향 복원 + Primary/Supporting을 하나의 Content Group으로 재구성, 이 과정에서 "Visual Requirement Compatibility" 판단 단계가 Layout Routing에 신설됨 — **중간**.

---

## 8. Timeline/Milestone — 미채택 사례 (Avoid-전용 항목)

- **Content Relationship**: 시간축이 정보 구조의 핵심(연도별 계획, 3~5개년)
- **Content Density**: 연도당 원본 이미지 1장 + 텍스트
- **최종 결과**: 채택되지 않음. 5개년 로드맵을 Timeline/Company Milestone Layout 1장으로 시도했으나, 원본 이미지 5개를 한 슬라이드에 모두 넣자 82px 썸네일로 축소되어 식별 불가능(Image Legibility 위반) 발생 → **연차별로 슬라이드 자체를 물리 분할**(17→21슬라이드)하고 좌측 Large Visual + 우측 개별 카드 구조로 대체
- **Avoid When**: 다년치 이미지를 하나의 슬라이드/Timeline Layout에 욱여넣지 않는다 — 이미지 개수가 Region 수 대비 많고 이미지당 정보 밀도가 높으면 Content Volume Fit 위반으로 보고 슬라이드 분할을 우선 검토한다. 원본이 여러 독립 이미지를 이미 하나의 가로형 결합 이미지(예: 3.47:1 비율로 2개 다이어그램 합침)로 제공하면 세로 공간 활용이 제한되므로, 자료 수집 단계에서 개별 이미지 분리를 요청하는 편이 낫다.
- **원인 진단**: Timeline/Company Milestone Layout 자체에 Must Preserve 섹션이 없어 구조 이탈이 반복되는 카탈로그 상위 위험 Layout으로 지목됨(F-test 조사와도 일치)
- **Field Test 근거**: `cosolus-business-plan-2026` — **중간**(사용자 확정, pptx 미변환. 근본 원인 진단은 F-test와 교차 확인되어 신뢰도 있음).

---

## 9. 표지/기업소개/투자포인트/글로벌진출 — 전용 문서 강제 적용 + 실명 로고 Avoid

- **최종 확정 Layout/Variant**: 표지 = `01_cover_design_V2.md`(Hard Rule, L01~33보다 항상 우선), 기업소개 = `02_instruction_design_V1.md`, 투자포인트(Executive Summary) = `L18 Two-Column Summary`, 글로벌 진출 = `L21 Customer References/Proof`(시점 축이 없는 현재진행형 나열이면 Timeline 계열 제외)
- **일반화 가능한 Avoid-When(기업·프로젝트 무관 규칙)**: **원문에 "일본 현지투자사·재료업체 등"처럼 익명·범주로만 표현된 파트너를, 실제 실명 로고(특정 기업 로고 이미지)와 임의로 매칭하지 않는다.** 원문에 없는 특정 브랜드/기업명을 이미지 자산과 임의로 짝짓는 것은 상표·평판 리스크로 취급한다.
- **Field Test 근거**: `cosolus-ir-deck` A/B/C/D-test/E-test 전체에서 일관되게 로고 미사용 또는 텍스트만으로 처리 — **높음**. E-test는 이 문제를 별도 사용자 고지 대상(상표·평판 리스크)으로 격상 처리한 전례 있음.

---

## 10. Data Pending / 확인 불가 수치 처리 — 구조 유지 검증됨

CLAUDE.md 4장의 Data Pending 원칙(자리·역할을 구조적으로 유지)이 실제로 Layout Routing까지 관통해 살아남는지 Field Test에서 검증됨: 핵심 근거 데이터가 원문에 없는 경우(예: 수요-공급 테이블, 시장 규모 차트) escalation으로 작업을 멈추고 사용자 확인 후 `data_pending`으로 표시된 채 다음 단계까지 자리를 유지 — 정상 동작 확인.

**Field Test 근거**: `cosolus-ir-deck-E` — **중간**(프로젝트 자체는 closed 상태이나 메커니즘 검증은 유효).

---

## 11. Branching / Multi-Generation Process Flow (전용 플로우 다이어그램)

> ⚠️ 이 항목은 위 1~10과 신뢰도 성격이 다르다 — `state.json`/Human Review 기록이 전혀 없는 순수 반복 개발 이력(`p15-16-test` v1~v13)에서 역추론한 것이며, 어떤 버전이 실제로 사용자 승인을 받았는지 확인할 수 없다. 아래는 "최종 배포된 `flow-diagram-rules.md`/`flow-diagram-implementation-reference.md`에 살아남은 개념"을 최종 근사치로 삼은 **추정** 결과다.

- **Content Relationship**: 하나의 공유 시작 지점(공통 원료·전처리)에서 하나의 분기점을 거쳐 N개의 경쟁/비교 가능한 프로세스 세대·경로로 갈라지고, 그중 한 경로가 내부에서 다시 하위 분기하는 구조(전체-부분 + 비교 복합형). 단순 2-Column Before/After와 달리 **공유 트렁크가 있는 분기 토폴로지**일 때만 이 Layout을 고른다.
- **Content Density**: 공유 시작 단계 1~2개 노드, 1차 분기점 1개, 상위 레인 2개, 2차 분기점 1개(하위 레인 내부), Process 노드 4~6개, 출력 그룹 2~4개
- **Visual**: 단일 캔버스 절대좌표 플로우 다이어그램, 색상(레인별 고유색)이 1차 구분 채널, 아이콘은 보더 없이 이미지만, 화살표는 항상 solid(점선 금지)
- **최종 확정(추정) 구조**:
  - Region Map은 고정 픽셀이 아니라 **범위**로 관리(예: 분기 X 33~38%, 레인 분할 Y 45~50%) — 실측 pptx 좌표가 우선, Region Map 비율표는 보조 참고로만 사용
  - Flow Graph 선해석: 좌표를 정하기 전에 모든 요소를 Material/Process/Intermediate/Output으로 먼저 분류
  - Process 라벨은 커넥터 선 **위**에 얹혀 선이 끊기지 않게, Material/Intermediate/Output 노드는 커넥터를 **끊고** 통과(이미지 중심을 관통하지 않음)
  - 분기점은 하나의 공통 트렁크 → 한 지점 → 다수 분기가 정확히 같은 시작 X/Y를 공유(개별적으로 따로 그린 여러 선이 아님)
  - **Output Group vs Sibling Outputs Branch 판단**: 하나의 공정에서 나온 여러 출력이 자동으로 분기되는 게 아니다 — 서로 다른 하위 경로/독립적 의미를 가질 때만 분기로 그리고, 같은 범주면 단일 커넥터의 Output Group으로 묶는다
  - 원문(입력 자료)에 없는 라벨 박스·강조 문구를 임의로 만들어 넣지 않는다
  - 텍스트 최소 14pt 준수(각주 제외)
- **Avoid When(실제 반복·되돌림 사례)**:
  - 두 분기 간 Comparison Marker/Bracket을 시각적 정렬을 위해 억지로 맞추지 않는다(§2-B와 동일 원칙이 여기서도 반복 확인됨)
  - 하나의 출력 쌍(예: 동일 범주의 두 부산물)을 무조건 Sibling Outputs Branch로 그리지 않는다 — Output Group 판단 없이 분기부터 그리면 나중에 "잘못 분기했던 부분"으로 되돌려야 함
  - 노드 라벨을 커넥터 Y-라인에 통째로 중앙정렬하면 2줄 라벨이 커넥터와 겹친다 — 이미지 중심정렬과 라벨 오프셋을 분리해서 처리
  - 원문에 없는 "1세대/2세대 비교" 같은 프레이밍 텍스트나 라벨 박스를 새로 만들지 않는다(그 회차의 입력 문서에 없으면 생략)
- **Field Test 근거**: `output/p15-16-test` ~ `p15-16-test-v13`(13개 순차 반복, 최신 배포 문서와 개념 매칭으로 역추론) — **낮음(추정)**, 최종 배포 문서(`flow-diagram-rules.md`) 자체는 이미 채택되어 사용 중이므로 그 문서를 우선 신뢰하고, 이 항목은 "왜 그렇게 정했는가"의 배경 설명으로만 참고할 것.

---

## 새 Field Test 사례 추가 방법 (Reuse → Update → Merge → Add)

새 프로젝트가 [6] Human Review ②를 통과해 확정되면(`state.json.stage`가 6 이후로 진행하고 사용자가 실제로 승인한 버전), **곧바로 새 섹션부터 쓰지 않고** 그 확정 결과를 기존 Pattern 전체(현재 1~11번과 그 하위 변형)와 먼저 대조한 뒤 아래 중 해당하는 경로 하나만 따른다.

1. **완전히 동일하고 새로운 정보 없음 → 추가하지 않음**: 이미 같은 Pattern·같은 결론·같은 신뢰도 근거가 기록돼 있으면 아무것도 추가하지 않는다.
2. **기존 Pattern과 조건은 같고 근거만 강화됨 → 기존 Evidence에 병합(승인 불필요)**: 해당 섹션의 "Field Test 근거"에 프로젝트명과 신뢰도(§ "신뢰도 표기 기준")만 추가한다. 판단 필드(Content Relationship/Density/항목 수/Use When/Avoid When 등)는 건드리지 않는다. 중간에 시도했다가 되돌린 구조는 성공 사례로 추가하지 말고, 원인이 명확하면 Avoid When에만 추가한다.
3. **기존 Pattern의 판단 범위(Use When/Avoid When/항목 수/Content Density 등) 자체가 바뀌어야 함 → Update(사용자 승인 필요)**: 세부 변형이 실제로 판단 갈림길을 만들 때만 하위 항목(예: "2-A"/"2-B")으로 분리하는 것을 검토하되, 우선은 기존 판단 필드를 일반화·수정해 하나의 갱신된 Pattern으로 흡수할 수 있는지 먼저 검토한다. Use When/Avoid When 등은 Layout Routing이 실제로 참조하는 판단 기준이므로, 갱신안을 메인을 통해 사용자에게 제시하고 **승인받은 뒤에만** 반영한다.
4. **여러 기존 Pattern이 실질적으로 중복 → Merge(사용자 승인 필요)**: 별도 섹션 2개 이상이 사실은 하나의 조건으로 통합 가능함이 새 사례로 드러나면, 통합안(합쳐질 판단 필드·근거 목록·정리될 섹션 번호)을 메인을 통해 사용자에게 제시하고 **승인받은 뒤에만** 하나로 합친다. 승인 전에는 기존 섹션을 그대로 둔다.
5. **기존에 없는 새로운 구조적 패턴 → Add(승인 불필요)**: 위 1~4 어디로도 처리할 수 없을 때만 새 섹션을 추가한다 — Add 전에 반드시 기존 Pattern 전체와 콘텐츠 구조·분량 조건의 중복·포함 관계를 먼저 확인했어야 하며, 그중 하나로 처리 가능한데도 새 Pattern을 만들지 않는다. 새 섹션은 기존 스키마(Content Relationship / Content Density / 항목 수 / Visual / 강조 정보 / 최종 확정 Layout·Variant / Use When / Avoid When / Field Test 근거)를 그대로 따른다.

공통 원칙:
- 특정 회사명·제품명·문구는 기록하지 않는다 — 콘텐츠 구조와 분량 조건만 일반화해서 남긴다.
- 이 문서 자체의 서술이 Layout MD의 구현 규칙과 충돌하면 Layout MD가 우선한다.
- 위 1·2·5(추가 안 함/근거 병합/신규 Add)는 판단 기준 자체를 바꾸지 않으므로 CLAUDE.md 2장 [9]의 "사용자 명시 승인 필요" 규칙 대상이 아니다. 3·4(Update/Merge)는 판단 기준의 의미가 바뀌므로 [9]와 동일하게 승인 대상이다.
