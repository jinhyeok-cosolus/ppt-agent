# Slide Outline — cosolus-ir-deck-D (v2, 규칙개선 1~4 적용 재판단)

> 대상: 고객사/외부 청중 · 언어: 한국어 · 발표시간: 20분 · 목표 슬라이드 수: 15장 · 레퍼런스: 없음
> 입력: `output/cosolus-ir-deck-D/material_analysis.json` (재추출 없음, C/D 공통 재사용)
> 이 outline은 `slide_outline_v1_archive.md`(v1, 규칙개선 이전 판단)를 참고하지 않고, 개정된 `slide-content-structuring` SKILL.md의 1-b 단계(Claim→Evidence→Relationship→Required/Optional)를 포함한 절차 전체를 처음부터 다시 수행해 작성했다. Layout 선택은 개정된 `design-rules.md` "Layout Routing 판단 순서 — Relationship 우선"을 따른다.
> 새 Layout MD는 만들지 않는다 — Cycle/Loop 및 구성요소별 기여도(Contribution) 전용 Layout이 카탈로그에 없는 경우, `design-rules.md` Layout Routing 6번(기존 Layout 조합·최소 변형 우선 시도 → 안 되면 "없음"으로 이관)을 그대로 따른다.

---

## Slide 1. 표지

- **Core Message**: COSOLUS — 지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술
- **Core Claims & Evidence**: N/A(표지는 Claim/Evidence 구조 분석 대상이 아님 — 브랜드 메시지 제시)
- **Content Roles**:
  - Primary: 회사 모토("Small actions, BIG DIFFERENCE") + 핵심 한 줄 설명
  - Dependent/Shared Supporting/Conclusion: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: 표지 전용 구조 — `01_cover_design_V2.md`를 그대로 따름(별도 Region 설계 없음)
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: Hard Rule·design-rules.md "표지 전용" 규칙에 따라 항상 우선 적용
- **Structural Check**: 문제 없음. White/Reversed 로고(`cosolus CI.png`) 사용 대상. img34(워드마크)는 참고용이며 실제 사용 자산 아님.

---

## Slide 2. 기업 소개

- **Core Message**: 코솔러스는 첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제를 선도하는 전문 기업이다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스는 신뢰할 수 있는 실체를 갖춘 화학소재·공정 전문 기업이다.
    - Evidence: table_1(기업명/대표자/임직원/소재지/비전) — 완전 확인됨
    - Relationship: 단일 독립 근거(정보 나열형, 항목 간 비교·추세 없음)
    - Required/Optional: Required(5개 항목 모두)
- **Content Roles**:
  - Primary: 핵심 메시지 + 기본 정보(기업명/대표자/임직원/소재지/비전)
  - Dependent: 비전 문구(핵심 메시지 구체화)
  - Shared Supporting/Conclusion: N/A
- **Relationship**: 단일 콘텐츠(정보 요약형)
- **Content Regions**: 좌측 Information Region(핵심 메시지 + 5개 기본 정보) / 우측 Vertical Image Region(현장 사진, img2)
- **Selected Layout**: Company Introduction (`docs/slide-design-rules/02_instruction_design_V1.md`)
- **Layout Selection Reason**: Use When "회사 정체성·핵심 메시지·기본 정보(기업명/대표자/임직원/소재지/비전)를 외부 청중에게 전달"에 정확히 부합.
- **Structural Check**: 문제 없음. B20(조직구성) 본문이 전무(NC-03)하므로 별도 슬라이드로 만들지 않고 이 슬라이드에 확인된 사실(임직원 27명 등)만 반영 — 조직도·인물 캡션 임의 생성 안 함. v1과 판단 동일.

---

## Slide 3. 배터리 밸류체인의 환경·지정학적 리스크

- **Core Message**: 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있으며, 채굴 기반 공급은 환경·사회적 비용을 수반한다.
- **Core Claims & Evidence**:
  - Claim A: 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있다.
    - Evidence: 전략광물 20개 중 19개 정제 1위 / 전략광물 정제 평균 점유율 70% / 글로벌 블랙매스 처리 비중 89% / 중국 강조 세계지도(img3)
    - Relationship: 복수 비교 근거(동일 기준 — "집중도" — 을 나타내는 3개 정량 지표가 나란히 제시되며, 세계지도가 이를 공간적으로 뒷받침)
    - Required/Optional: Required(지도 + 3개 지표 모두)
  - Claim B: 채굴 기반 공급은 환경·사회적 비용을 수반한다.
    - Evidence: 니켈 1톤당 133톤 폐기물 발생(수치, 확인됨) / 채굴 산업의 노동·인권 문제(서술) / 채굴폐기물 현장 사진(img54~57)
    - Relationship: 단일 독립 근거(133t 수치) — 서술·사진은 Optional 보강
    - Required/Optional: Required(133t 수치) / Optional(노동·인권 서술, 현장 사진)
  - Evidence-Claim 매핑: Claim A와 Claim B는 서로 다른 상위 주장이며, Claim A의 3개 지표와 Claim B의 133t 수치를 하나의 균질한 4칸 스탯 그리드로 뭉치지 않는다 — 두 근거 그룹이 시각적으로 구분되게 표현한다(v1은 4개 지표를 단일 `vi-stat-grid`로 평평하게 배치해 Claim A/B 구분이 드러나지 않았음 — v2에서 수정).
- **Content Roles**:
  - Primary: 세계지도(Main Visual, Claim A 직접 근거) + Claim A 3개 지표
  - Dependent: N/A
  - Shared Supporting: N/A(Claim A·B 근거가 서로 다른 그룹으로 명확히 분리되어 "공유" 근거가 아님 — v1에서는 이 구분 없이 뭉뚱그렸음)
  - Conclusion/Takeaway: N/A(문제 제기 단계)
- **Relationship**: 기타·복합(지도 기반 Main Visual + 서로 다른 두 주장을 뒷받침하는 두 근거 그룹)
- **Content Regions**: Main Visual Area(중국 강조 세계지도, img3, Claim A 근거) / Supporting Insight Area — **Group A "글로벌 공급망 집중도"**(미니 헤더 + 3개 지표: 19/20·70%·89%) / **Group B "환경·사회적 비용"**(미니 헤더 + 133t 지표 + 노동·인권 서술 + 채굴폐기물 현장 사진) — Group A/B를 별도 서브 블록으로 시각 구분(구분선 또는 개별 미니 헤더)
- **Selected Layout**: Visual + Insight Layout — Variant B(Chart + Insight), Layout Catalog L07 Market/Problem 대응 (`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: Main Visual(지도) + Supporting Insight(수치·시사점) 2분할 구조에 부합. Insight 영역 내부는 Claim A/B 두 근거 그룹으로 나눠 구성 — Layout 자체는 v1과 동일하나 내부 Region 구성이 Evidence-Claim 매핑을 반영해 달라짐.
- **Structural Check**: 정보량이 많음(지도+4스탯+서술+사진) — Group A/B 분리로 밀도 관리. 출처 각주(IEA/Benchmark Mineral Intelligence/Earthworks) 반드시 유지. **집중 QA 대상**: Group A/B 시각적 구분이 실제로 인지 가능한 수준인지 확인.

---

## Slide 4. 북미 ESS 시장, 고성장의 변곡점

- **Core Message**: 북미 ESS(에너지저장장치) 시장은 에너지 용량(GWh) 기준 연평균 31.6% 성장이 전망된다.
- **Core Claims & Evidence**:
  - Claim: 북미 ESS 시장은 고속 성장한다.
    - Evidence: CAGR 31.6%(원문 확인 수치, 연도별 GWh 계열·원본 차트 이미지는 75개 이미지 전수 확인 결과 없음 — NC-01)
    - Relationship: 단일 독립 근거(비교·추세 대상 없이 단일 확인 수치)
    - Required/Optional: Required
- **Content Roles**:
  - Primary: CAGR 31.6%(Large Number)
  - Dependent: "북미 ESS 시장 성장 전망(GWh 기준)" 맥락 설명
  - Shared Supporting/Conclusion: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Main Visual Area(CAGR 31.6% Large Number) / Supporting Insight Area(시장 맥락 설명 + 출처 각주)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message + Evidence), Layout Catalog L24 대응 (`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: Relationship이 "단일 독립 근거"이므로 `content-visualization-freedom.md` 표에 따라 Large Number/Key Stat 표현이 그 자체로 충분 — 원본에 없는 연도별 추세를 임의로 만들지 않음(Trend Visual 강제 금지). v1과 판단 동일(단일 독립 근거는 관계를 억지로 만들지 않는다는 원칙 그대로 적용).
- **Structural Check**: 콘텐츠량이 매우 적음 — Content Density 원칙에 따라 빈 공간을 강제 분산(space-between 등)으로 채우지 않고 압축형 배치 유지. **집중 QA 대상(고정 Slide 4)**: 여백 처리 확인.

---

## Slide 5. 순환경제 비즈니스 모델

- **Core Message**: 코솔러스는 폐자원 회수 → 유해물질·온실가스 저감 → 재활용 기반 신공급망 구축이라는 세 축의 비즈니스 모델로 순환경제를 실현한다.
- **Core Claims & Evidence**:
  - Claim 1: 폐자원 회수로 배터리 원재료 수급 문제를 해결한다.
    - Evidence: "폐자원으로부터 핵심 광물 확보로 배터리 원재료 수요부족 해결"
    - Relationship: 원인→결과(폐자원 회수 → 수급 문제 해결)
    - Required/Optional: Required
  - Claim 2: 유해물질·온실가스 저감으로 환경오염을 저감한다.
    - Evidence: "유해물질 억제 및 온실가스 감축으로 환경 오염 저감"
    - Relationship: 원인→결과
    - Required/Optional: Required
  - Claim 3: 재활용 기반 순환 신공급망을 구축한다.
    - Evidence: "제조 → 재활용 → 제조로 이어지는 재활용 기반 新공급망 구축"
    - Relationship: **순환 관계**(제조 상태 → 재활용 상태 → 제조 복귀 — 되먹임 구조. v1은 이 세 마디를 "제조 → 재활용 → 제조"라는 텍스트로만 표기하고 시각적으로는 단순 아이콘 하나로 처리해 순환 구조 자체가 드러나지 않았음)
    - Required/Optional: Required — 관계를 이루는 값 전체(제조→재활용→제조 3마디)를 대표 문구 하나로 축약하지 않고 보존
- **Content Roles**:
  - Primary: 3개 대등 메시지(①원재료 수급 ②환경영향 저감 ③신공급망 구축)
  - Dependent/Shared Supporting/Conclusion: N/A(3개 메시지 자체가 결론적 구조)
- **Relationship**: 병렬(Claim 1·2·3은 대등한 3개 축) — 단, Claim 3 **내부** Evidence는 순환 관계이며 이는 슬라이드 전체의 병렬 관계와 다른 층위임(Column 3 내부에서만 적용)
- **Content Regions**: 3개 병렬 Column(동일 Top Line·동일 Width) — Column 1·2 = Icon + 짧은 제목 + 설명 문장 / **Column 3 = 순환 관계를 보존하는 소형 Cycle Diagram(제조 → 재활용 → 제조 3-node 폐곡선) + 설명 문장**(v1은 Column 3도 Column 1·2와 동일하게 단일 아이콘+텍스트로 균질 처리했으나, v2는 Claim 3의 Relationship이 순환형이므로 이 Column만 다른 표현을 취함 — "Layout 내부 Visual 구성의 다양성" 원칙 적용)
- **Selected Layout**: Three-Column Insight Layout (`docs/slide-design-rules/three-column/three-column.md`)
- **Layout Selection Reason**: Layout Routing 1~2단계 — 슬라이드 전체 구조는 "독립·대등 항목(Claim 1·2·3) 병렬"이므로 Column/Card 계열이 우선 후보. Claim 3만 순환 관계이지만 이는 슬라이드 구조 자체(3개 대등 축)를 바꿀 사유가 아니라 해당 Column **내부**의 표현 방식 문제이므로, 전용 Cycle/Loop Layout으로 슬라이드 전체를 바꾸지 않고 Three-Column 내부에서 소형 Cycle Diagram으로 수용(Layout Routing 6번: 기존 Layout 조합·최소 변형으로 먼저 시도 — 성공). 카탈로그에 Cycle/Loop 전용 Layout이 없다는 공백이 있었지만, 이번 사례는 슬라이드 전체가 아닌 Column 하나의 국소적 표현이라 그 공백이 실제 결과 품질에 영향을 주지 않음.
- **Structural Check**: 문제 없음. 3개 항목 정보량 비교적 균등. Column 3의 Cycle Diagram이 다른 두 Column과 시각적 비중(면적·굵기)에서 과도하게 불균형하지 않도록 [5]에서 확인 필요.

---

## Slide 6. 1세대 공정의 한계와 코솔러스의 솔루션

- **Core Message**: 1세대 재활용 공정은 낮은 선택성·불안정한 상분리·과다한 부산물 발생 등의 한계를 가지며, 코솔러스는 고성능 추출제(1.5세대, RECYION Series) 도입으로 이를 해결한다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스 1.5세대 추출제(RECYION Series)가 1세대 공정의 한계를 해결한다.
    - Evidence(Before): 낮은 선택성 / 제한된 동작 환경(pH 등) / 상분리 불안정 / 부산물 과다발생(망초 등) — 1세대 공정 개념도(img60/61 실제 내용 확인 필요)
    - Evidence(After): 고성능 추출제 RECYION Series, 기존 추출제(D2EHPA) 대비 재활용 효율 개선 — 화학구조식(img7/8, 실제 내용 확인 필요)
    - Relationship: Before/After(전환 전후 두 상태)
    - Required/Optional: Required(Before 4항목 + After 솔루션 개요 전체 — 대표 항목 하나로 축약하지 않음)
- **Content Roles**:
  - Primary: Before(1세대 한계) / After(1.5세대 솔루션 개요)
  - Dependent: 1세대 한계 세부 4항목 / 1.5세대 화학적 기반(D2EHPA 대비 RECYION)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "소재 및 공정 개선 필요" → 솔루션 연결
- **Relationship**: Before/After(정확히 2개 상태 전환)
- **Content Regions**: Before Column(1세대 개념도 + 한계 4항목) / After Column(RECYION 솔루션 개요 + 화학구조 비교)
- **Selected Layout**: Before + After Layout — Variant A(Process Transformation) (`docs/slide-design-rules/before-after/before-after.md`)
- **Layout Selection Reason**: 접근 방식 자체의 전환(단계 수 변화보다 "무엇이 문제였고 무엇으로 해결하는가")이 핵심이며, 정량 비교표보다 좌→우 Diagram+Arrow가 이 시점(개요 단계)에 적합. 정량 상세 비교는 Slide 7/8에서 별도 전개. v1과 판단 동일.
- **Structural Check**: 이미지 라벨 신뢰도 주의 — B07의 img7/8(추출제 화학구조식), B06의 img60/61(1세대 공정 개념도)은 라벨 오류 가능성이 제기된 이미지이므로 [5]에서 `extracted_images/`를 직접 열어 실제 내용을 확인한 뒤 배치.

---

## Slide 7. 고성능 추출제 — 경쟁사 대비 공정 효율

- **Core Message**: COSOLUS 추출제는 벨기에 S사·중국 K사 대비 공정시간과 첨가제 사용량에서 압도적 우위를 갖는다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 추출제는 경쟁사(벨기에 S사, 중국 K사) 대비 공정시간·첨가제 사용량이 우수하다.
    - Evidence: 공정시간 — COSOLUS 기준(Baseline), 벨기에 S사 100%↑, 중국 K사 50%↑ / 첨가제 사용량 — COSOLUS 기준, 벨기에 S사 10%이상↑, 중국 K사 5%이상↑ (table_7, 공정시간 행은 원문 그래픽 처리로 텍스트 미검출 — 인접 문단+첨가제 행 대소패턴 교차검증으로 재구성, 수치 자체는 원문 그대로)
    - Relationship: 복수 비교 근거(3개 대상 × 2개 기준, 동일 기준 반복 비교)
    - Required/Optional: Required(3개 대상 × 2개 기준 전체 — 대표 수치 하나로 축약하지 않음)
- **Content Roles**:
  - Primary: 3개 대상(COSOLUS/벨기에 S사/중국 K사) × 2개 비교 기준 매트릭스
  - Dependent/Shared Supporting/Conclusion: N/A(매트릭스 자체가 메시지)
- **Relationship**: 복수 비교 근거
- **Content Regions**: 비교 매트릭스 Region — 3개 대상 Column × 2개 기준 Row, COSOLUS Column 강조
- **Selected Layout**: Comparison Matrix Layout (`docs/slide-design-rules/comparison-matrix/comparison-matrix.md`)
- **Layout Selection Reason**: Layout Routing 2단계("복수 비교 근거 → Comparison 계열 우선 검토")에 부합, 3개 대상 동일 기준 반복 비교 구조. v1과 판단 동일.
- **Structural Check**: 공정시간 행 재구성 근거를 각주에 유지. **집중 QA 대상(고정 Slide 7)**: Table Style 규칙(Header Fill, Divider, colgroup+table-layout:fixed) 적용 확인.

---

## Slide 8. 추출단수 저감이 만드는 CAPEX·OPEX 경제성

- **Core Message**: COSOLUS 추출제는 이론단수를 1단 저감(5단→4단)시켜 CAPEX·OPEX 양면에서 경제성을 확보한다.
- **Core Claims & Evidence**:
  - Claim: 추출단수 1단 저감이 CAPEX·OPEX 두 가지 정량 효과를 만든다.
    - Evidence: 추출단수 5단→4단(20% 감소, table_8 완전 확인) → ①CAPEX: 추출 효율 2~5% 개선 ②OPEX: 망초 5% 이상 저감(연간 니켈 16,000톤 생산 기준 4,800톤 저감, 16,000×(3.6-3.3)=4,800 정합 확인)
    - Relationship: 원인→결과(하나의 원인이 두 개의 병렬 정량 효과를 만듦 — 구성요소별 기여도처럼 하나의 결과를 여러 요소가 나눠 만드는 구조가 아니라, 하나의 원인이 두 개의 독립된 결과 지표를 각각 만드는 구조라는 점에서 "원인→결과"로 판단)
    - Required/Optional: Required(단수 저감 값 + CAPEX 효과 + OPEX 효과 전체)
- **Content Roles**:
  - Primary: Core Technology — 추출단수 1단 저감
  - Dependent: CAPEX Impact(효율 개선 2~5%) / OPEX Impact(망초 저감, 연간 4,800톤)
  - Shared Supporting/Conclusion: N/A
- **Relationship**: 인과(단수 저감 → 2개 정량 Impact)
- **Content Regions**: 상단 Core Technology 서술 / 좌우 병렬 Impact Region(CAPEX / OPEX, table_8 Evidence 포함)
- **Selected Layout**: Benefit + Impact Layout (`docs/slide-design-rules/benefit-impact/benefit-impact.md`)
- **Layout Selection Reason**: `Core Technology → Improvement → Quantified Impact` 흐름 + 정확히 2개의 좌우 정량 효과 구조에 정확히 부합. v1과 판단 동일.
- **Structural Check**: 임의 수치 없음, 4,800톤 계산 정합 확인됨. 문제 없음.

---

## Slide 9. 직접리튬추출(DLE) — 재활용 공정 안에서 완성

- **Core Message**: 기존 DLE(증발법)는 단일 단계·낮은 회수율(3.12%)에 그치지만, 코솔러스는 NCM 스크랩에서 Mn·Co·Ni·Li을 순차 회수하는 4단계 공정 안에서 리튬까지 회수한다.
- **Core Claims & Evidence**:
  - Claim 1: 코솔러스는 재활용 공정 안에서 4개 금속을 순차 회수한다.
    - Evidence: 침출 → 불순물 제거 → (1)Mn 추출 → (2)Co 추출 → (3)Ni 추출 → (4)Li 추출 → 역추출
    - Relationship: 순차 공정/프로세스(단계별 값 — 단계 순서 전체가 근거)
    - Required/Optional: Required(6단계 전체 순서 — 최종 단계만 남기지 않음)
  - Claim 2: 코솔러스 공정은 기존 DLE(증발법) 대비 우위에 있다.
    - Evidence: 기존 DLE(증발법) — 1단계, Li 회수율 3.12% / 코솔러스 — NCM 스크랩 재활용 공정 안에서 Mn·Co·Ni·Li 통합 회수
    - Relationship: Before/After(기존 단일 금속·단일 단계 방식 vs 코솔러스 통합·다단계 방식)
    - Required/Optional: Required
- **Content Roles**:
  - Primary: 코솔러스 4단계 공정 흐름
  - Dependent: 각 단계의 대상 금속
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 기존 DLE 대비 공정 전체 관점의 우위
- **Relationship**: 순차(공정 흐름) + Before/After(기존 DLE 대비)
- **Content Regions**: 상단 Process Flow Region(코솔러스 4단계 순차 흐름, Claim 1) / 하단 Comparison Region(기존 DLE vs 코솔러스, Claim 2)
- **Selected Layout**: Process + Comparison Layout (`docs/slide-design-rules/process-comparison/process-comparison.md`)
- **Layout Selection Reason**: Layout Routing 2단계 — "순차 관계/공정 → Process/Flow 계열" + 그 흐름과 직접 연결되는 비교(기존 DLE)를 하단에서 함께 전달하는 Use When 조건에 정확히 부합. v1과 판단 동일.
- **Structural Check**: 이미지 라벨 신뢰도 주의 — img9(칠레 아타카마 염호), img21(지열발전 연계 플랜트)은 라벨 오류 가능성이 제기된 이미지이므로 [5]에서 실제 파일을 확인한 뒤 사용.

---

## Slide 10. DLE 기술 동향 비교

- **Core Message**: DLE(직접리튬추출) 기술은 흡착제·추출제·분리막·전기화학 4개 방식으로 나뉘며, 각각 작동원리·기술성숙도(TRL)·장단점이 다르다.
- **Core Claims & Evidence**:
  - Claim: DLE는 4개 방식으로 나뉘며 각각 작동원리·TRL·장단점이 다르다.
    - Evidence: table_12(작동원리/TRL/장점/단점 × 흡착제·추출제·분리막·전기화학) — 완전 확인됨
    - Relationship: 복수 비교 근거(4개 대상, 동일 기준 반복)
    - Required/Optional: Required(4개 방식 × 4개 기준 전체)
- **Content Roles**:
  - Primary: 4개 방식 × 4개 비교 기준
  - Dependent/Shared Supporting/Conclusion: N/A(표 자체가 메시지)
- **Relationship**: 복수 비교 근거
- **Content Regions**: 표 Region — 4개 방식 Row × 4개 기준 Column
- **Selected Layout**: Table Comparison Layout (`docs/slide-design-rules/table-comparison.md`)
- **Layout Selection Reason**: 서술형 텍스트 셀(장단점 등)로 구성되어 Diagram형보다 표가 더 정확 — Column 수가 많아 밀도 감당을 위해 표 형식 필요. v1과 판단 동일.
- **Structural Check**: 임의 수치 없음. **집중 QA 대상(고정 Slide 10)**: colgroup+table-layout:fixed 폭 고정, 한글 word-break:keep-all 확인.

---

## Slide 11. DLE 핵심 경쟁력 — 추출제·분리막 결합 기술

- **Core Message**: 추출제와 분리막을 결합한 COSOLUS DLE 기술은 리튬 재자원화율을 90% 이상으로, 공정비용을 5,500원/kg 이하로 낮춘다.
- **Core Claims & Evidence**:
  - Claim 1(핵심 성과): COSOLUS DLE 기술은 재자원화율 90% 이상, 공정비용 5,500원/kg 이하를 달성한다.
    - Evidence: "COSOLUS 화학구조 설계·정제·공정 기술 → 재자원화율(>90%), 공정비용(<5,500원/kg)" (전제: 리튬선물 가격 약 44,100천원/ton 기준 각주)
    - Relationship: 단일 독립 근거(최종 성과치, 다른 대상과의 비교가 아닌 절대 도달 수준)
    - Required/Optional: Required(수치 + 전제 각주)
  - Claim 2(기여 분해, Claim 1의 근거): 재자원화율 개선은 두 기술 요소가 각각 다른 수준까지 기여한다.
    - Evidence: 분리막 & THz 기술 — 재자원화율 3%→90% / 핵심소재 — 재자원화율 3%→50%
    - Relationship: **구성요소별 기여도**(동일 baseline 3%에서 두 기술 요소가 각각 도달시키는 수준이 분해되어 제시됨 — v1은 이를 "3%→90%↑"라는 대표 수치 하나만 Large Number로 강조하고 "핵심소재 3%→50%"는 하단 보조 텍스트 한 줄로 축소했음. Relationship Preservation 원칙상 두 기여 요소 값 모두가 대등하게 남아 있어야 함)
    - Required/Optional: Required(두 기여 요소 값 모두 — 대표값 하나로 축약 금지)
  - Claim 3(공유 근거): 추출제-분리막 결합의 4가지 구조적 강점이 Claim 1·2를 함께 뒷받침한다.
    - Evidence: ①빠른 물질전달 ②화학적 결합+공간적 분리로 우수한 재활용 효율 ③액상 공정 기반 연속운전 ④분리막 기반 농축으로 첨가제 소모량 감소
    - Relationship: 기타(병렬 나열형 근거, Claim 1·2 모두를 뒷받침하는 Shared Supporting)
    - Required/Optional: Optional(근거를 강화하지만 없어도 Claim 1·2 자체는 성립)
- **Content Roles**:
  - Primary: Claim 1 핵심 성과(Large Number)
  - Dependent: Claim 2 기여도 분해(분리막&THz / 핵심소재)
  - Shared Supporting: Claim 3 4가지 Key Advantage(Claim 1·2 모두 지지)
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합(단일 결론 + 구성요소별 기여도 + 공유 근거 나열)
- **Content Regions**: Main Claim Area(Claim 1 Large Number: 재자원화율 >90%, 공정비용 <5,500원/kg) / **Contribution Region**(신설 — 분리막&THz·핵심소재 두 기여 요소를 병렬 mini Before-After/진행률 형태로 3%→90%, 3%→50% 모두 시각적으로 표시, v1의 "대표 수치 하나 + 보조 텍스트 한 줄" 구조에서 변경) / Shared Supporting Region(4개 Key Advantage 리스트)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message + Evidence), Layout Catalog L24 대응 (`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: Layout Routing 6번 적용 사례 — "구성요소별 기여도" 전용 Layout이 카탈로그에 없으므로, 먼저 기존 Layout(Visual+Insight Variant D) 내부에서 수용 가능한지 검토했다. Evidence Area 안에 두 기여 요소를 나란히 배치하는 mini Contribution 시각(진행률 바 형태)으로 Relationship을 보존할 수 있다고 판단해 Layout 자체는 바꾸지 않고 내부 Region만 재구성했다 — "적합한 Layout Reference 없음"으로 이관할 정도는 아니었음.
- **Structural Check**: 리튬선물 가격 전제 각주 반드시 표기. **집중 QA 대상**: Contribution Region이 실제로 두 기여 요소(3%→90%, 3%→50%) 값을 모두 보존하는지, 대표값 하나로 축소되지 않았는지 확인(1-c 전달 보존 Check 대상).

---

## Slide 12. 친환경 차세대 배터리 재활용 공정(2세대)

- **Core Message**: 코솔러스 2세대 공정은 유도가열 → 전처리 → 블랙매스 생성 → 부유선별의 흐름으로 고순도 정제흑연과 코발트·니켈을 회수하며, 경제성·친환경성·양산성을 동시에 확보한다.
- **Core Claims & Evidence**:
  - Claim: 2세대 공정은 4단계 흐름을 거쳐 고순도 정제흑연과 코발트·니켈을 회수하고 경제성·친환경성·양산성을 확보한다.
    - Evidence: ①COSOLUS 유도가열 ②전처리 공정 ③블랙매스 생성(양극재용/음극재용, 폐흑연 처리 포함) ④COSOLUS 부유선별 → Output(고순도 정제흑연 + 코발트·니켈 회수)
    - Relationship: 순차 공정/프로세스(4단계 전체 순서)
    - Required/Optional: Required(4단계 전체 + Output)
- **Content Roles**:
  - Primary: System/Process Title + 4개 Component 흐름
  - Dependent: 각 Component 역할·짧은 설명
  - Shared Supporting: N/A
  - Conclusion/Takeaway: Output(고순도 정제흑연 + 코발트·니켈 회수, 경제성·친환경성·양산성)
- **Relationship**: 순차(공정 흐름)
- **Content Regions**: System/Process Title Region(상단) / 4개 Component Region(좌→우 Arrow 연결) / Insight/Output Box(하단)
- **Selected Layout**: Process / System Architecture Layout — **Layout A(이미지 없음)** (`docs/slide-design-rules/process-system-architecture-layout.md`)
- **Layout Selection Reason**: Layout Routing 2단계 "순차 관계/공정 → Process/Flow 계열"에 정확히 부합. Layout A/B 중 A 선택 사유: 확보된 실사진(img62/63/64/65)이 사실상 ①유도가열 단계 또는 전체 라인 전경에만 대응하고 ②전처리 ③블랙매스 생성 ④부유선별에 대응하는 사진은 없어 4단계 중 사진 확보 비율 약 25%(80% 미만) — 문서 §3.3 규칙에 따라 Layout A. v1과 판단 동일.
- **Structural Check**: Component 수 4개(권장 범위 3~6개 충족). **집중 QA 대상(신규 Layout 실사용)**: Component 동일 Width/Top Line(Parallel Layout Alignment), Arrow 연결, Insight Box 위치가 문서 스펙대로 구현됐는지 확인.

---

## Slide 13. 2세대 공정의 가격·기술 경쟁력

- **Core Message**: 코솔러스 2세대 공정(유도가열)은 기존 소성로(Pusher Kiln) 대비 압도적으로 짧은 공정시간·적은 에너지 투입과 함께, 고순도 재생흑연·낮은 부반응 등 기술적 우위를 갖는다.
- **Core Claims & Evidence**:
  - Claim 1: 2세대 공정(유도가열)은 기존 소성로 대비 가격·기술 경쟁력이 있다.
    - Evidence: 공정시간(10시간 이상 vs 1분 이내) / 승온속도(기준 대비 200배) / 에너지 투입(432Wh/kg, 64% 절감) / 흑연 순도(99% 이상) / 부반응(낮음) / 시설투자비용(높음 vs 상대적으로 낮음) / 온도정밀도(낮음 vs 높음)
    - Relationship: Before/After(정확히 2개 대상, 다기준 비교)
    - Required/Optional: Required(7개 비교 기준 전체 — 일부만 남기지 않음)
  - Claim 2(공유 근거, Claim 1의 기술경쟁력 부분을 보강): 2세대 공정은 추가 기술 신뢰도 근거를 갖는다.
    - Evidence: Co 회수 순도 >95% / PCT 2건 출원
    - Relationship: 단일 독립 근거 2건(병렬 나열)
    - Required/Optional: Optional(Claim 1의 표 비교가 이미 핵심 주장을 성립시키며, 이 근거는 보강 성격)
- **Content Roles**:
  - Primary: 기존(Pusher Kiln) vs COSOLUS(2세대 유도가열) — 정확히 2개 대상 다기준 비교
  - Dependent: 7개 세부 비교 기준
  - Shared Supporting: Co 회수 순도, PCT 출원(2세대 공정 전반의 기술 신뢰도 근거)
  - Conclusion/Takeaway: N/A(비교표 자체가 결론)
- **Relationship**: Before/After(정확히 2개 대상, 다기준)
- **Content Regions**: Existing(Pusher Kiln) Column / COSOLUS(유도가열) Column — 동일 기준 Row 병렬 비교 + 하단 보조 Evidence(Co 순도, PCT 출원)
- **Selected Layout**: Before + After Layout — Variant B(Before/After Comparison Table) (`docs/slide-design-rules/before-after/before-after.md`)
- **Layout Selection Reason**: 정확히 2개 대상, 동일 기준 다항목으로 "무엇이 얼마나 개선되는가"를 보여주는 Variant B Use When에 정확히 부합. v1과 판단 동일.
- **Structural Check**: B19(경쟁력-솔루션2, 본문 전무)는 B18과 주제 중복으로 이 슬라이드에 통합(별도 슬라이드 생성 안 함).

---

## Slide 14. 투자 포인트

- **Core Message**: 코솔러스는 검증된 기술력과 구체적 사업화 방향을 바탕으로 Series A2 라운드 80억원 투자 유치를 추진한다.
- **Core Claims & Evidence**:
  - Claim 1: 코솔러스는 최상위 수준의 기술 경쟁력을 갖췄다.
    - Evidence: 추출제 최상위 합성·정제 기술 / 친환경 공정 기술(건식환원·유도가열) / Closed-loop system 기술
    - Relationship: 복수 비교 근거(3개 병렬 기술 축이 함께 "기술력"을 뒷받침) — 관계형은 아니나 3개 항목 모두 나열되어야 주장이 온전히 성립
    - Required/Optional: Required(3항목 전체)
  - Claim 2: 코솔러스는 세대별로 구체적 사업화 방향을 갖고 있다.
    - Evidence: (1.5세대 RECYION) XX하이텍·XX코 등 PoC 진행 중 / (2세대 친환경 공정) XX자동차 연계 신공급망, 일본·인도네시아 시장 진출
    - Relationship: 기타(1.5세대·2세대 두 트랙이 병행 — 순차적 시간 흐름이 아니라 세대별 병행 사업화 방향)
    - Required/Optional: Required(두 트랙 모두 — 실명 마스킹 "XX하이텍/XX코/XX자동차"는 원문 그대로 유지, 임의 실명 채우지 않음)
  - Claim 3: 코솔러스는 Series A2로 80억원 투자를 유치한다.
    - Evidence: 투자라운드 Series A2, 목표 투자유치 금액 80억원
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
  - Claim 4: 투자금은 해외 진출·공장 건설에 사용된다.
    - Evidence: 국외법인 설립·운영 / 토지 구매·건축(추출제 CAPA, 공정파일럿)
    - Relationship: 단일 독립 근거(2항목 나열)
    - Required/Optional: Required
- **Content Roles**:
  - Primary: 4개 병렬 항목([기술력]/[사업화 방향]/[투자라운드]/[투자금 사용 계획])
  - Dependent: 각 항목 세부 내용
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 투자라운드(Series A2, 80억원)가 사실상 핵심 결론
- **Relationship**: 병렬(4개 대등 항목) + 그중 하나(투자라운드)가 Conclusion 성격
- **Content Regions**: 4개 병렬 Region — Claim 1(3항목 리스트) / Claim 2(2트랙 병행 텍스트) / Claim 3(Large Number Hero) / Claim 4(2항목 리스트). 4개 Region 모두 "리스트+텍스트"로 균질화하지 않고, Claim 3만 Large Number로 시각적 강조를 유지(다른 3개 Claim은 관계형이 아니므로 리스트 표현이 적합, Claim 3만 단일 독립 근거의 Key Stat 표현이 적합 — Relationship 기준 판단과 일치)
- **Selected Layout**: Two-Column Summary, Layout Catalog L18 (`docs/layout-reference/2026.08.13_layout-catalog_V1.md`)
- **Layout Selection Reason**: 4개 항목이 대등 병렬 나열되는 구조에 맞는 전용 Layout Reference가 없어(Three-Column은 3개 항목 전제) L01~L33에서 목적이 가장 근접한 L18을 선택 후 4-Region 그리드로 최소 변형(Layout Routing 6번). v1과 판단 동일.
- **Structural Check**: 마스킹된 실명 그대로 유지. 투자금액(80억원) 원문 그대로. **집중 QA 대상(고정 Slide 14)**: 4개 Region Parallel Layout Alignment, 항목별 정보량 불균형 확인.

---

## Slide 15. 일본·인도네시아 시장 진출

- **Core Message**: 코솔러스는 5억 명 이상 아시아 경제권을 겨냥해 일본과 인도네시아를 전략적 거점으로 세계시장 진출을 추진한다.
- **Core Claims & Evidence**:
  - Claim 1: 인도네시아에서 구체적 투자 논의가 진행 중이다.
    - Evidence: 전기자전거 업체 1대주주와 투자 논의 / SWAP·MUKTI·eCoNiL·IBC 로고(원문에 함께 포함된 생태계 이미지) / 인도네시아 e-모빌리티·행사 실사진
    - Relationship: 단일 독립 근거(논의 현황 서술) + 이미지 근거(직접 대응)
    - Required/Optional: Required(논의 현황 서술) / Optional(로고·실사진 — 있으면 신뢰도를 높이나 서술만으로도 주장 성립)
  - Claim 2: 일본에서도 투자 논의가 진행 중이다.
    - Evidence: 현지투자사·재료업체 등과 투자 논의(익명 서술) — Panasonic Energy/Iwatani/DNP 로고는 이 익명 표현과 구체적으로 매칭되는지 원문에서 확인 불가(NC-04)
    - Relationship: 단일 독립 근거(논의 현황 서술)
    - Required/Optional: Required(서술) / Optional(로고 — 사용 시 특정 파트너십 단정 문구 없이 "일본 배터리·소재 생태계" 맥락으로만)
  - Evidence-Claim 매핑: 인도네시아 로고(img71~74)는 Claim 1에 직접 대응하는 근거이나, 일본 로고(Panasonic/Iwatani/DNP)는 Claim 2에 확정적으로 매칭되지 않는 참고 이미지 — 두 로고 그룹을 "동일한 확정 근거"로 동등하게 다루지 않는다.
- **Content Roles**:
  - Primary: 목표(일본·인도네시아 전략 거점, 5억 명 아시아 경제권)
  - Dependent: 국가별 논의 현황(Claim 1·2)
  - Shared Supporting: 관련 생태계 이미지/로고
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(일본 vs 인도네시아, 2개 거점)
- **Content Regions**: 상단 목표 서술 / 좌우 병렬 Region — 인도네시아(Claim 1 + 확정 근거 이미지) / 일본(Claim 2 + 참고 이미지, 단정 문구 없음)
- **Selected Layout**: Symmetric Two-Split, Layout Catalog L25 (`docs/layout-reference/2026.08.13_layout-catalog_V1.md`)
- **Layout Selection Reason**: 두 국가가 대등한 위계로 병렬 제시되는 구조. 전용 Layout Reference 중 이 구조(2개 대등 지역 거점 + 이미지/로고 근거)에 맞는 문서가 없어 L01~L33에서 선택. v1과 판단 동일.
- **Structural Check**: NC-04 반영 — 일본 로고는 단정 문구 없이 배치. img71~75(SWAP/MUKTI/eCoNiL/IBC/HLI 로고)는 라벨 오류 가능성이 제기된 이미지이므로 [5]에서 실제 파일을 확인한 뒤 배치(HLI는 라벨 오검증됨 — 실제 파일 확인 후 사용 여부 재확정 필요).

---

## Layout Routing 6번(적합한 Layout 없음) 적용 총평

- **Slide 5(순환 관계)**: Claim 3(제조→재활용→제조)만 국소적으로 순환 구조 — 슬라이드 전체 구조(3개 대등 Column)는 바뀌지 않으므로 Three-Column 내부에 소형 Cycle Diagram만 추가해 해결. Cycle/Loop 전용 Layout 부재가 실제 결과 품질에 영향을 주지 않은 사례.
- **Slide 11(구성요소별 기여도)**: Claim 2(분리막&THz 3%→90%, 핵심소재 3%→50%)가 슬라이드의 핵심 근거 구조 — Contribution 전용 Layout은 없지만 Visual+Insight Variant D의 Evidence Area 내부에 두 기여 요소를 병렬 mini 시각으로 배치해 해결. 두 사례 모두 새 Layout MD를 만들지 않고 기존 Layout의 내부 재구성만으로 Relationship을 보존했다 — Layout Routing 6번의 "기존 Layout 조합·최소 변형 우선" 경로가 실제로 작동함을 확인.
- Product/Application Layout: 이번 콘텐츠 중 "하나의 중심 제품이 여러 적용처로 확장" 구조에 해당하는 원본 콘텐츠 묶음이 없어 미사용(v1과 판단 동일).
