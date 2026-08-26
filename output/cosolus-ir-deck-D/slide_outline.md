# Slide Outline — cosolus-ir-deck-D (v3, 신규 material-analysis 스키마 기반 재구성)

> 대상: 고객사/외부 청중 · 언어: 한국어 · 발표시간: 20분 · 목표 슬라이드 수: 15장 · 레퍼런스: 없음
> 입력: `material_analysis.json`(Content Group→Subtopic→Evidence 신규 스키마, 23개 그룹) + `slide_composition_map.json`(content-grouping이 확정한 15개 슬라이드 경계 — 재판단하지 않고 그대로 소비) + `extracted_images/`(신규 재추출, 80개)
> 1단계+1-b(Claim→Evidence→Relationship)는 `output/_material-analysis-regression/cosolus-ir-deck-D/slide_claims_evidence.md`를 출발점으로 재검증했다. 1-c(Backward Completeness Check)·2단계(Content Role)~6단계(구조적 사전 점검)는 이번에 처음 수행한다.
> 이미지는 slide_claims_evidence.md/material_analysis.json에 이미 기록된 "직접 열어 확인함(confirmed)" 판정을 신뢰하되, 실제 파일 존재 여부는 `extracted_images/`에서 재확인했다. `content_match_confidence: uncertain` 이미지는 예외 없이 Optional 상한이며, 슬라이드 맥락과의 관계 자체가 불명확한 경우(NC-05, img6/7)는 Optional로도 배치하지 않는다.

---

## Slide 1. 표지

- **Source Material**: CG01(entire)
- **Core Message**: COSOLUS — 지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술
- **Core Claims & Evidence**: N/A(표지는 Claim/Evidence 구조 분석 대상이 아님 — 브랜드 메시지 제시)
- **Backward Completeness Check**: 명시반영 2(모토 "Small actions, BIG DIFFERENCE" + 핵심 한 줄 설명, Core Message에 직접 반영) / 라벨제외 0 / uncertain보류 0 / 미반영 0. img1(COSOLUS 워드마크)은 Hard Rule에 따라 그대로 쓰지 않고 등록된 CI 자산(`docs/brand-assets/CI/cosolus CI.png`, White/Reversed)으로 대체 — 대체 사용도 "반영"으로 처리(원본 의도인 로고 노출 자체는 유지).
- **Content Roles**:
  - Primary: 회사 모토 + 핵심 한 줄 설명
  - Dependent/Shared Supporting/Conclusion: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: 표지 전용 구조 — `01_cover_design_V2.md`를 그대로 따름(별도 Region 설계 없음)
- **Selected Layout**: `01_cover_design_V2.md`(표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: Hard Rule·design-rules.md "표지 전용" 규칙에 따라 항상 우선 적용
- **Structural Check**: 문제 없음. White/Reversed 로고 사용 대상. img1은 참고용이며 실제 사용 자산 아님(등록 CI 우선).

---

## Slide 2. 기업 소개

- **Source Material**: CG02(entire)
- **Core Message**: 코솔러스는 첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제를 선도하는 전문 기업이다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스는 신뢰할 수 있는 실체를 갖춘 화학소재·공정 전문 기업이다.
    - Evidence: table_1(기업명 주식회사 코솔러스 / 대표자 김성현 / 임직원 27명 / 소재지 대한민국 전주·익산·완주·군산 / 비전 — `relation_confidence: structural`, 5개 항목)
    - Relationship: 단일 독립 근거(정보 나열형, 항목 간 비교·추세 없음)
    - Required/Optional: Required(5개 항목 모두)
- **Backward Completeness Check**: 명시반영 6(CG02-ST01 텍스트 1 + table_1 5항목) / Core Message반영 0 / 중복통합 0 / 라벨제외 0 / uncertain보류 1(img2, 실험실/글러브박스 사진 추정 — content_match_confidence uncertain) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 핵심 메시지 + 기본 정보(기업명/대표자/임직원/소재지/비전)
  - Dependent: 비전 문구(핵심 메시지 구체화)
  - Shared Supporting/Conclusion: N/A
- **Relationship**: 단일 콘텐츠(정보 요약형)
- **Content Regions**: 좌측 Information Region(핵심 메시지 + 5개 기본 정보, table_1 Required 전체 반영) / 우측 Vertical Image Region(img2, Optional — "실험실 현장 사진으로 추정"이라는 불확실성 문구 없이 특정 실험 내용을 단정하지 않고 일반적인 현장 이미지로만 사용)
- **Selected Layout**: Company Introduction(`docs/slide-design-rules/02_instruction_design_V1.md`)
- **Layout Selection Reason**: Use When "회사 정체성·핵심 메시지·기본 정보(기업명/대표자/임직원/소재지/비전)를 외부 청중에게 전달"에 정확히 부합.
- **Structural Check**: 문제 없음. CG20(조직구성)은 원본에 제목만 있고 본문이 전무해(coverage_check 참조) 별도 슬라이드로 만들지 않았고 이 슬라이드에도 임의로 조직도·인물 캡션을 추가하지 않는다.

---

## Slide 3. 배터리 밸류체인의 환경·지정학적 리스크

- **Source Material**: CG03-ST01(entire, evidence_clusters EC1+EC2), CG03-ST02(entire)
- **Core Message**: 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있으며, 채굴 기반 공급은 환경·사회적 비용을 수반한다 — 이 구조적 문제가 광물 수요-공급 미스매치를 심화시킨다.
- **Core Claims & Evidence**:
  - Claim A(EC1): 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있다.
    - Evidence: 전략광물 20개 중 19개 정제 1위(IEA) / 전략광물 정제 평균 점유율 70%(IEA) / 글로벌 블랙매스 처리 비중 89%(Benchmark Mineral Intelligence) — 모두 metrics confirmed. img3(중국 강조 세계지도, `likely_supports: EC1`)는 content_match_confidence uncertain
    - Relationship: 복수 비교 근거(동일 기준 "집중도"를 나타내는 3개 정량 지표)
    - Required/Optional: Required(3개 지표) / Optional(img3)
  - Claim B(EC2): 채굴 기반 공급은 환경·사회적 비용을 수반한다.
    - Evidence: 니켈 1톤당 133톤 폐기물 발생(Earthworks, confirmed) / 채굴 산업의 노동·인권 문제(서술)
    - Relationship: 단일 독립 근거(133t 수치가 핵심, 서술은 정성적 보강)
    - Required/Optional: Required(133t) / Optional(노동·인권 서술)
  - Evidence-Claim 매핑: Claim A·B는 서로 다른 상위 주장 — 하나의 균질한 근거 그룹으로 합치지 않는다.
- **Backward Completeness Check**: 명시반영 9(EC1 텍스트 4 + EC2 텍스트 2 + metrics 4 — 일부 중복 표기) / Core Message반영 1("배터리 밸류체인 전반의 환경부하 및 사회적 비용 — 광산채굴 기준 수요-공급 미스매치 발생" 프레이밍 문장. 이 문장은 특정 evidence_cluster에 속하지 않고 Subtopic 최상위에 남아있는 유형이라 처음에는 Claim A/B 요약에만 흡수되고 "수요-공급 미스매치"라는 구체 표현이 누락될 위험이 있어 재확인함 — Core Message 문구에 "수요-공급 미스매치를 심화시킨다"를 명시적으로 추가해 반영) / uncertain보류 1(img3) / 미반영 0. 미반영 항목 없음(재확인 완료).
- **Content Roles**:
  - Primary: 세계지도(Main Visual, Claim A 근거) + Claim A 3개 지표
  - Dependent: N/A
  - Shared Supporting: N/A(Claim A·B 근거가 서로 다른 그룹으로 명확히 분리)
  - Conclusion/Takeaway: 수요-공급 미스매치 프레이밍(Main Title Supporting Message로 배치)
- **Relationship**: 기타·복합(지도 기반 Main Visual + 서로 다른 두 주장을 뒷받침하는 두 근거 그룹)
- **Content Regions**: Main Title Supporting Message(프레이밍 문장) / Main Visual Area(중국 강조 세계지도, img3) / Supporting Insight Area — Group A "글로벌 공급망 집중도"(미니 헤더 + 3개 지표) / Group B "환경·사회적 비용"(미니 헤더 + 133t 지표 + 노동·인권 서술), 좌측 컬러 보더+미니헤더로 시각 구분
- **Selected Layout**: Visual + Insight Layout — Variant B(Chart + Insight), Layout Catalog L07 대응(`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: Main Visual(지도) + Supporting Insight(수치·시사점) 2분할 구조에 부합. Insight 영역 내부는 Claim A/B 두 근거 그룹으로 나눠 구성해 Evidence-Claim 매핑을 시각적으로 보존.
- **Structural Check**: 정보량이 많음(지도+4스탯+서술) — Group A/B 분리로 밀도 관리. 출처 각주(IEA/Benchmark Mineral Intelligence/Earthworks) 반드시 유지.

---

## Slide 4. 북미 ESS 시장, 고성장의 변곡점

- **Source Material**: CG04(entire)
- **Core Message**: 북미 ESS(에너지저장장치) 시장은 에너지 용량(GWh) 기준 연평균 31.6% 성장이 전망된다.
- **Core Claims & Evidence**:
  - Claim: 북미 ESS 시장은 고속 성장한다.
    - Evidence: CAGR 31.6%(metrics, confirmed. 출처: SNE Research 2023 / Mirae Asset Securities Research Center 2026.1 / KATECH Mobility Insight 2024.4) — 연도별 GWh 계열·원본 차트 이미지 없음(NC-01)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1(CAGR 31.6%) / Core Message반영 2("[북미 ESS 시장 성장 전망]", "에너지 용량 (GWh)" — 단위·맥락 설명으로 Core Message에 흡수) / 라벨제외 1("왜 지금인가?-산업적 요인", 슬라이드 성격 라벨) / uncertain보류 0 / 미반영 0.
- **Content Roles**:
  - Primary: CAGR 31.6%(Large Number)
  - Dependent: "북미 ESS 시장 성장 전망(GWh 기준)" 맥락 설명
  - Shared Supporting/Conclusion: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Main Visual Area(CAGR 31.6% Large Number) / Supporting Insight Area(시장 맥락 설명 + 출처 각주)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message + Evidence), Layout Catalog L24 대응(`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: Relationship이 "단일 독립 근거"이므로 Large Number/Key Stat 표현이 그 자체로 충분 — 원본에 없는 연도별 추세를 임의로 만들지 않는다(Trend Visual 강제 금지).
- **Structural Check**: 콘텐츠량이 매우 적음 — Content Density 원칙에 따라 빈 공간을 강제 분산(space-between 등)으로 채우지 않고 압축형 배치 유지. img4(범용 성장 스톡 그래픽, confirmed)는 Optional 장식 보조로만 소극적 사용(특정 수치 계열을 담은 차트로 오인되지 않게 캡션 없이 배치).

---

## Slide 5. 순환경제 비즈니스 모델

- **Source Material**: CG05(entire)
- **Core Message**: 코솔러스는 폐자원 회수 → 유해물질·온실가스 저감 → 재활용 기반 신공급망 구축이라는 세 축의 비즈니스 모델로 순환경제를 실현한다.
- **Core Claims & Evidence**:
  - Claim 1: 폐자원 회수로 배터리 원재료 수급 문제를 해결한다.
    - Evidence: "폐자원으로부터 핵심 광물 확보로 배터리 원재료 수요부족 해결"
    - Relationship: 원인→결과 / Required
  - Claim 2: 유해물질·온실가스 저감으로 환경오염을 저감한다.
    - Evidence: "유해물질 억제 및 온실가스 감축으로 환경 오염 저감"
    - Relationship: 원인→결과 / Required
  - Claim 3: 재활용 기반 순환 신공급망을 구축한다.
    - Evidence: "제조 → 재활용 → 제조로 이어지는 재활용 기반 新공급망 구축"
    - Relationship: 순환 관계(제조→재활용→제조 3-node 되먹임 구조, 값 전체 보존)
    - Required/Optional: Required — 3마디 전체 보존, 대표 문구로 축약 금지
- **Backward Completeness Check**: 명시반영 4(제목 제외 3개 문장 그대로 Claim 1·2·3 Evidence) / 라벨제외 1("비즈니스 모델" 제목) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3개 대등 메시지(①원재료 수급 ②환경영향 저감 ③신공급망 구축)
  - Dependent/Shared Supporting/Conclusion: N/A(3개 메시지 자체가 결론적 구조)
- **Relationship**: 병렬(Claim 1·2·3은 대등한 3개 축) — Claim 3 내부 Evidence만 순환 관계(Column 3 국소 적용)
- **Content Regions**: 3개 병렬 Column(동일 Top Line·동일 Width) — Column 1·2 = Icon + 짧은 제목 + 설명 문장 / Column 3 = 순환 관계를 보존하는 소형 Cycle Diagram(제조→재활용→제조 3-node 폐곡선 SVG) + 설명 문장
- **Selected Layout**: Three-Column Insight Layout(`docs/slide-design-rules/three-column/three-column.md`)
- **Layout Selection Reason**: 슬라이드 전체 구조는 "독립·대등 항목(Claim 1·2·3) 병렬"이므로 Column/Card 계열이 우선 후보. Claim 3만 순환 관계이지만 이는 슬라이드 구조 자체를 바꿀 사유가 아니라 해당 Column 내부의 표현 방식 문제이므로, Three-Column 내부에서 소형 Cycle Diagram으로 수용(Layout Routing 6번 — 기존 Layout 최소 변형으로 해결).
- **Structural Check**: 문제 없음. 3개 항목 정보량 비교적 균등. Column 3의 Cycle Diagram이 다른 두 Column과 시각적 비중에서 과도하게 불균형하지 않도록 [5]에서 확인.

---

## Slide 6. 1세대 공정의 한계와 코솔러스의 솔루션

- **Source Material**: CG06(entire), CG07-ST01(entire), CG07-ST02(entire)
- **Core Message**: 1세대 재활용 공정(기존 추출제 D2EHPA 기반)은 낮은 선택성·불안정한 상분리·과다한 부산물 발생 등의 한계를 가지며, 코솔러스는 고성능 추출제 RECYION Series(1.5세대) 도입으로 이를 해결한다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스 1.5세대 추출제(RECYION Series)가 1세대 공정의 한계를 해결한다.
    - Evidence(Before): 낮은 선택성 / 제한된 동작 환경(pH 등) / 상분리 불안정 / 부산물 과다발생(망초 등) — CG06 텍스트 confirmed. 기존 추출제(1세대) = D2EHPA(광산·염호 기반 금속 회수용) — CG07-ST01 텍스트 confirmed
    - Evidence(After): 고성능 추출제 RECYION Series, D2EHPA 대비 재활용 효율 개선 — CG07-ST01 텍스트 confirmed
    - Relationship: Before/After(전환 전후 두 상태)
    - Required/Optional: Required(Before 4항목 + D2EHPA 식별 + After 솔루션 개요 전체 — 대표 항목 하나로 축약하지 않음)
  - 이미지 근거: **사용하지 않음**. CG06-ST02 img5는 재확인 결과 GLENCORE 로고로 확인됐고 "1세대 공정의 한계" 서술과의 관계가 원문에서 불명확(NC-05)해 Before 근거로 쓰지 않는다. CG07-ST02 img6/img7은 D2EHPA/RECYION 중 어느 쪽인지 미확인(uncertain)이라 라벨 오배치 위험이 있어 배치하지 않는다. 이 슬라이드는 텍스트 근거만으로 Required가 성립한다.
- **Backward Completeness Check**: 명시반영 7(Before 4항목 + D2EHPA 식별 + RECYION 소개 + 재활용효율 개선) / 라벨제외 2(두 Group 제목) / uncertain보류 3(img5·img6·img7 — 모두 관계 불명 또는 라벨 미확인으로 배치하지 않음, Optional로도 올리지 않음) / 미반영 0.
- **Content Roles**:
  - Primary: Before(1세대 한계) / After(1.5세대 솔루션 개요)
  - Dependent: 1세대 한계 세부 4항목 + 기존 추출제(D2EHPA) 식별 / 1.5세대 화학적 기반(RECYION, D2EHPA 대비 개선)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "소재 및 공정 개선 필요" → 솔루션 연결
- **Relationship**: Before/After(정확히 2개 상태 전환)
- **Content Regions**: Before Column(Header "1세대 공정 — D2EHPA" + 한계 4항목 리스트, 이미지 없음) / After Column(Header "1.5세대 — RECYION Series" + 솔루션 개요 텍스트, 이미지 없음) — Main Visual 유형은 Process/Step Sequence가 아닌 Text/Feature 패널(신뢰 가능한 이미지 자산이 없으므로 4.2~4.13의 Process 전용 조건부 규칙은 적용하지 않고 Comparison Frame만 적용)
- **Selected Layout**: Before + After Layout — Variant A(Process Transformation)(`docs/slide-design-rules/before-after/before-after.md`)
- **Layout Selection Reason**: "무엇이 문제였고 무엇으로 해결하는가"라는 개요 단계의 전환이 핵심이며, 정량 비교표(Variant B)보다 좌우 Comparison Frame이 이 시점에 적합. 정량 상세 비교는 Slide 7/8에서 별도 전개.
- **Structural Check**: 이미지 근거 전무 확정(위 사유) — Placeholder 이미지·빈 아이콘으로 공간을 채우지 않는다(Prohibited Reinterpretations 준수). Before/After 두 Column 모두 텍스트 밀도가 유사해 Visual Balance 문제 없음.

---

## Slide 7. 고성능 추출제 — 경쟁사 대비 공정 효율

- **Source Material**: CG08(entire)
- **Core Message**: COSOLUS 추출제는 벨기에 S사·중국 K사 대비 공정시간과 첨가제 사용량에서 우위를 갖는다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 추출제는 경쟁사(벨기에 S사, 중국 K사) 대비 공정시간·첨가제 사용량이 우수하다.
    - Evidence: 공정시간 — COSOLUS 기준, 벨기에 S사 100%↑, 중국 K사 50%↑(table_7 "공정시간" 행 셀은 원문 그래픽 처리로 빈칸 — 인접 문단 텍스트로 재구성, 수치 자체는 원문 그대로) / 첨가제 사용량 — 벨기에 10%↑, 중국 5%↑(table_7 confirmed) / 각주: *블랙매스 1톤당 첨가제 사용량 기준
    - Relationship: 복수 비교 근거(3개 대상 × 2개 기준)
    - Required/Optional: Required(전체) — 공정시간 값은 재구성 출처임을 각주로 유지
- **Backward Completeness Check**: 명시반영 7(재구성 텍스트 2 + 각주 1 + metrics 4) / 미반영 0.
- **Content Roles**:
  - Primary: 3개 대상(COSOLUS/벨기에 S사/중국 K사) × 2개 비교 기준 매트릭스
  - Dependent/Shared Supporting/Conclusion: N/A(매트릭스 자체가 메시지)
- **Relationship**: 복수 비교 근거
- **Content Regions**: 비교 매트릭스 Region — 3개 대상 Column × 2개 기준 Row, COSOLUS Column 강조(Text+Bold, Fill 강조 아님)
- **Selected Layout**: Comparison Matrix Layout(`docs/slide-design-rules/comparison-matrix/comparison-matrix.md`)
- **Layout Selection Reason**: "복수 비교 근거 → Comparison 계열 우선 검토"에 부합, 3개 대상 동일 기준 반복 비교 구조.
- **Structural Check**: 공정시간 행 재구성 근거를 각주에 유지. Table colgroup+table-layout:fixed로 동일 폭 Column 구현 필요.

---

## Slide 8. 추출단수 저감이 만드는 CAPEX·OPEX 경제성

- **Source Material**: CG09(entire)
- **Core Message**: COSOLUS 추출제는 이론단수를 1단 저감(5단→4단)시켜 CAPEX·OPEX 양면에서 경제성을 확보한다.
- **Core Claims & Evidence**:
  - Claim: 추출단수 1단 저감이 CAPEX·OPEX 두 가지 정량 효과를 만든다.
    - Evidence: 추출단수 5단→4단(20% 감소, table_8 confirmed, 니켈 1톤당 망초 3.6톤→3.3톤) → CAPEX(추출 효율 2~5% 개선) / OPEX(망초 5% 이상 저감, 연간 니켈 16,000톤 기준 4,800톤 저감 — 16,000×(3.6-3.3)=4,800 정합 확인, *대한민국 배터리 재활용 업체 블랙매스 연간 처리량 기준)
    - Relationship: 원인→결과(하나의 원인이 두 개의 병렬 정량 효과를 만듦)
    - Required/Optional: Required(단수 저감 값 + CAPEX 효과 + OPEX 효과 + 기준 각주 전체)
- **Backward Completeness Check**: 명시반영 6(metrics 5 + table_8) / 라벨제외 2("수상 내 금속 농도"/"유기상 내 금속 농도" — McCabe-Thiele류 다이어그램 축 라벨로 추정되나 다이어그램 본체 자산이 없어 라벨만으로는 독립 정보가 되지 않음, 다이어그램 재구성 없이 제외) / 미반영 0.
- **Content Roles**:
  - Primary: Core Technology — 추출단수 1단 저감
  - Dependent: CAPEX Impact(효율 개선 2~5%) / OPEX Impact(망초 저감, 연간 4,800톤)
  - Shared Supporting/Conclusion: N/A
- **Relationship**: 인과(단수 저감 → 2개 정량 Impact)
- **Content Regions**: 상단 Core Technology 서술 / 좌우 병렬 Impact Region(CAPEX / OPEX, table_8 Evidence 포함)
- **Selected Layout**: Benefit + Impact Layout(`docs/slide-design-rules/benefit-impact/benefit-impact.md`)
- **Layout Selection Reason**: `Core Technology → Improvement → Quantified Impact` 흐름 + 정확히 2개의 좌우 정량 효과 구조에 정확히 부합.
- **Structural Check**: 임의 수치 없음, 4,800톤 계산 정합 확인됨. img8(McCabe-Thiele류 범례, confirmed)은 다이어그램 본체 없이 범례만 있어 단독으로 정보 가치가 낮다고 판단해 사용하지 않음(Optional 생략, 관련성 낮은 이미지로 공간을 채우지 않는다는 원칙에 부합).

---

## Slide 9. 직접리튬추출(DLE) — 재활용 공정 안에서 완성

- **Source Material**: CG11(entire)
- **Core Message**: 기존 DLE(증발법)는 단일 단계·낮은 회수율(3.12%)에 그치지만, 코솔러스는 NCM 스크랩에서 Mn·Co·Ni·Li을 순차 회수하는 4단계 공정 안에서 리튬까지 회수한다.
- **Core Claims & Evidence**:
  - Claim 1: 코솔러스는 재활용 공정 안에서 4개 금속을 순차 회수한다.
    - Evidence: NCM 스크랩 → 침출 → 불순물 제거 → (1)Mn 추출 → (2)Co 추출 → (3)Ni 추출 → (4)Li 추출 → 역추출(confirmed, 순서 전체)
    - Relationship: 순차 공정/프로세스 / Required(전체 순서)
  - Claim 2: 코솔러스 공정은 기존 DLE(증발법) 대비 우위에 있다.
    - Evidence: 기존 DLE(증발법) — 1단계, Li 회수율 3.12%(한국광해광업공단 2024, 오세희 의원실 2025 국정감사 분석) / 코솔러스 — NCM 스크랩 재활용 공정 안에서 통합 회수
    - Relationship: Before/After / Required
  - 이미지 근거: img10(칠레 아타카마 염호 유형 항공사진, confirmed), img11(지열발전 연계 플랜트 실사진, confirmed) — 둘 다 직접 열어 확인됨. Claim 2의 "기존 DLE(증발법)" Before 상태를 보여주는 신뢰 가능한 시각 근거 → Optional(서술만으로도 주장은 성립하나 confirmed 이미지이므로 우선 사용).
- **Backward Completeness Check**: 명시반영 5(Claim1 순서 텍스트 + Claim2 비교 텍스트 + metric 3.12% + img10/11) / 라벨제외 1(제목) / 미반영 0.
- **Content Roles**:
  - Primary: 코솔러스 4단계 공정 흐름
  - Dependent: 각 단계의 대상 금속
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 기존 DLE 대비 공정 전체 관점의 우위
- **Relationship**: 순차(공정 흐름) + Before/After(기존 DLE 대비)
- **Content Regions**: 상단 Process Flow Region(코솔러스 4단계 순차 흐름, Claim 1) / 하단 Comparison Region(기존 DLE vs 코솔러스, Claim 2, img10/11 사용)
- **Selected Layout**: Process + Comparison Layout(`docs/slide-design-rules/process-comparison/process-comparison.md`)
- **Layout Selection Reason**: "순차 관계/공정 → Process/Flow 계열" + 그 흐름과 직접 연결되는 비교(기존 DLE)를 하단에서 함께 전달하는 Use When 조건에 정확히 부합.
- **Structural Check**: 이미지 refs 정정 완료(img10=아타카마 염호, img11=지열발전 플랜트, 구 스키마의 라벨 오류 없음 확인).

---

## Slide 10. DLE 기술 동향 비교

- **Source Material**: CG12(entire)
- **Core Message**: DLE(직접리튬추출) 기술은 흡착제·추출제·분리막·전기화학 4개 방식으로 나뉘며, 각각 작동원리·기술성숙도(TRL)·장단점이 다르다.
- **Core Claims & Evidence**:
  - Claim: DLE는 4개 방식으로 나뉘며 각각 작동원리·TRL·장단점이 다르다.
    - Evidence: table_12(작동원리/TRL/장점/단점 × 흡착제·추출제·분리막·전기화학, confirmed)
    - Relationship: 복수 비교 근거(4개 대상, 동일 기준 반복)
    - Required/Optional: Required(4개 방식 × 4개 기준 전체)
- **Backward Completeness Check**: 명시반영 1(table_12) / 라벨제외 1(제목) / 기타(상위 단계 처리 완료) 1("Li"/"Cl-"/"e-" 텍스트 조각 — material_analysis.json의 `unassigned_or_dropped_content`에 이미 "인접 이미지 img12와 직접 대응하지 않고, 완전히 일치하는 이미지(H+/O/H2O 다이어그램)는 CG15/16에 구조적으로 위치해 Content Group 경계상 확정적 연결 근거 없음"으로 기록·제외 처리됨 — 이 슬라이드에서 재론하지 않음) / 미반영 0.
- **Content Roles**:
  - Primary: 4개 방식 × 4개 비교 기준
  - Dependent/Shared Supporting/Conclusion: N/A(표 자체가 메시지)
- **Relationship**: 복수 비교 근거
- **Content Regions**: 표 Region — 4개 방식 Row × 4개 기준 Column
- **Selected Layout**: Table Comparison Layout(`docs/slide-design-rules/table-comparison.md`)
- **Layout Selection Reason**: 서술형 텍스트 셀(장단점 등)로 구성되어 Diagram형보다 표가 더 정확 — Column 수가 많아 밀도 감당을 위해 표 형식 필요.
- **Structural Check**: img12(5종 재료구조 비교 일러스트 — Mxene/COF/Graphene oxide/MOF/Crown ether, confirmed)는 4개 방식 중 특정 Row/Cell과 명확히 1:1 대응하지 않고(여러 방식에 걸친 범용 재료 예시) Table Comparison Layout의 Region Map에 별도 이미지 슬롯이 없어 사용하지 않음(Optional 생략) — 구 스키마가 이 위치에 기재했던 H+/O/H2O 전기화학 다이어그램은 실제로 이 Group의 이미지가 아님(CG15/16 소속)을 재확인, 오배치 없음.

---

## Slide 11. DLE 핵심 경쟁력 — 추출제·분리막 결합 기술

- **Source Material**: CG13(entire), CG14(entire)
- **Core Message**: 추출제와 분리막을 결합한 COSOLUS DLE 기술은 리튬 재자원화율을 90% 이상으로, 공정비용을 5,500원/kg 이하로 낮춘다.
- **Core Claims & Evidence**:
  - Claim 1(핵심 성과): COSOLUS DLE 기술은 재자원화율 90% 이상, 공정비용 5,500원/kg 이하를 달성한다.
    - Evidence: "COSOLUS 화학구조 설계·정제·공정 기술 → 재자원화율(>90%), 공정비용(<5,500원/kg)"(전제 각주: 리튬선물 가격 약 44,100천원/ton 기준, KOMIS/Green Chem. 2026 인용, confirmed)
    - Relationship: 단일 독립 근거(최종 성과치) / Required(수치 + 전제 각주)
  - Claim 2(기여 분해, Claim 1의 근거): 재자원화율 개선은 두 기술 요소가 각각 다른 수준까지 기여한다.
    - Evidence: 분리막&THz 기술 — 3%→90% / 핵심소재 — 3%→50%(둘 다 confirmed metrics)
    - Relationship: 구성요소별 기여도(두 기여 요소 값 모두 대등하게 보존)
    - Required/Optional: Required(두 값 모두 — 대표값 하나로 축약 금지)
    - 보조 근거: img13(폴리머 사슬이 혼합 금속이온에서 Li⁺만 선택 포집하는 개념도, confirmed) — Claim 2의 메커니즘을 직접 시각화 → Optional
  - Claim 3(공유 근거): 추출제-분리막 결합의 4가지 구조적 강점(CG13)이 Claim 1·2를 함께 뒷받침한다.
    - Evidence: ①빠른 물질전달 ②우수한 재활용 효율 ③연속 운전 ④첨가제 소모량 감소
    - Relationship: 기타(병렬 나열형, Shared Supporting)
    - Required/Optional: Optional(근거를 강화하지만 없어도 Claim 1·2 자체는 성립)
- **Backward Completeness Check**: 명시반영 10(CG13 4항목 + CG14 본문 1 + 각주 1 + metrics 4 + img13) / 라벨제외 2(두 Group 제목) / 중복통합 0 / uncertain보류 1(CG14-ST02 표 "RECYION501 회수 효율" — 원문 셀 자체가 빈칸, NC-07) / 미반영 0.
- **Content Roles**:
  - Primary: Claim 1 핵심 성과(Large Number)
  - Dependent: Claim 2 기여도 분해(분리막&THz / 핵심소재) + img13
  - Shared Supporting: Claim 3 4가지 Key Advantage
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합(단일 결론 + 구성요소별 기여도 + 공유 근거 나열)
- **Content Regions**: Main Claim Area(Claim 1 Large Number: 재자원화율 >90%, 공정비용 <5,500원/kg) / Contribution Region(분리막&THz·핵심소재 두 기여 요소를 병렬 mini Before-After/진행률 형태로 3%→90%, 3%→50% 모두 시각적으로 표시 + img13을 이 Region 인근에 메커니즘 보조 시각으로 배치) / Shared Supporting Region(4개 Key Advantage 리스트)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message + Evidence), Layout Catalog L24 대응(`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: "구성요소별 기여도" 전용 Layout이 카탈로그에 없으므로, Layout Routing 6번에 따라 기존 Layout(Visual+Insight Variant D) 내부에서 수용 가능한지 먼저 검토 — Evidence Area 안에 두 기여 요소를 나란히 배치하는 mini Contribution 시각(진행률 바)으로 Relationship을 보존할 수 있어 Layout 자체는 바꾸지 않고 내부 Region만 재구성.
- **Structural Check**: 리튬선물 가격 전제 각주 반드시 표기. Contribution Region이 두 기여 요소 값을 모두 보존하는지(대표값 하나로 축소되지 않는지) [5]/[6]에서 재확인 필요.

---

## Slide 12. 친환경 차세대 배터리 재활용 공정(2세대)

- **Source Material**: CG15(entire), CG16(entire)
- **Core Message**: 코솔러스 2세대 공정은 유도가열 → 전처리 → 블랙매스 생성 → 부유선별의 흐름으로 고순도 정제흑연과 코발트·니켈을 회수하며, 기존 1세대 공정(유도가열/부유선별/건식환원 경로) 대비 경제성·친환경성·양산성을 확보한다.
- **Core Claims & Evidence**:
  - Claim: 2세대 공정은 4단계 흐름(폐흑연 처리 포함)을 거쳐 고순도 정제흑연과 코발트·니켈을 회수하고, 기존 1세대 공정 대비 경제성·친환경성·양산성을 확보한다.
    - Evidence: ①COSOLUS 유도가열 ②전처리 공정(폐흑연 처리 포함) ③블랙매스 생성(양극재용/음극재용) ④COSOLUS 부유선별 → Output(고순도 정제흑연 + 코발트·니켈) — CG16 텍스트 confirmed. 비교 맥락: 기존공정(1세대)도 동일 계열 기술(유도가열/부유선별/건식환원)로 같은 산출물(재활용 양극재/고순도 정제흑연/코발트/니켈)을 만들지만, COSOLUS(2세대)는 이를 경제성·친환경성·양산성 측면에서 개선한 버전 — CG15 텍스트 confirmed
    - Relationship: 순차 공정/프로세스(4단계 전체 순서) — 기존 1세대와의 비교 맥락은 Before/After 성격의 부가 프레이밍
    - Required/Optional: Required(4단계 전체 + Output + 기존 1세대 대비 개선이라는 프레이밍) — 텍스트만으로 이미 성립
  - 이미지 근거: **사용하지 않음(Layout A)**. CG15+CG16에 구조적으로 확인된 이미지는 16개 슬롯(6종 자산 중복, 고유 10장 — img14~20, img21/22/25)이나 대부분 반응조 단면 개념도·흑연/광물 렌더링·NCM 분자모델·전기화학 다이어그램·3단계 효과 그래픽 등 **컨셉 일러스트**이며, 실사진은 img20(산업용 컨테이너, 블랙매스 추정) 1장뿐이다. 4단계 중 신뢰 가능한 사진이 사실상 1단계에도 명확히 대응하지 않아 사진 확보 비율이 80% 미만 — Process/System Architecture Layout §3.3 규칙에 따라 Layout A(이미지 없음) 선택. 구 material_analysis.json이 "COSOLUS 유도가열 실제 설비 사진(img62~65)"으로 전제했던 것은 이번 재검증으로 사실이 아님이 확인됨(실제 실사진은 Slide 13의 img34/35).
- **Backward Completeness Check**: 명시반영 2(CG16 흐름 텍스트 + CG15 COSOLUS 목표 텍스트) / Core Message반영 2("기존공정(1세대)" 비교 텍스트, "폐흑연 처리 포함" — 둘 다 처음에는 CG16의 4단계 흐름 서술에 밀려 누락될 위험이 있는 전형적 패턴(병합된 Group 중 한쪽 서사가 대표로 채택되며 다른 쪽 세부가 조용히 빠지는 경우)이라 재확인함. "기존공정(1세대)" 비교는 Core Message와 Insight Box 프레이밍으로, "폐흑연 처리 포함"은 전처리 Component의 Short Detail로 각각 명시 반영) / 라벨제외 2(두 Group 제목 중복) / 중복통합 1(CG16 제목이 CG15 제목과 사실상 동일 주제라 중복 처리) / uncertain보류 0(이미지는 uncertain이 아니라 confirmed이나 Layout A 선택으로 미사용 — 아래 Structural Check 참조) / 미반영 0(재확인 완료).
- **Content Roles**:
  - Primary: System/Process Title + 4개 Component 흐름
  - Dependent: 각 Component 역할·짧은 설명(전처리 Component에 "폐흑연 처리 포함" 반영)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: Output(고순도 정제흑연 + 코발트·니켈 회수) + 기존 1세대 대비 경제성·친환경성·양산성 확보 프레이밍
- **Relationship**: 순차(공정 흐름), 부가적으로 기존 1세대 대비 개선이라는 Before/After 프레이밍
- **Content Regions**: System/Process Title Region(상단) / 4개 Component Region(좌→우 Arrow 연결, 이미지 없음) / Insight/Output Box(하단 — "기존 1세대 공정 대비 경제성·친환경성·양산성 확보"로 비교 맥락 명시)
- **Selected Layout**: Process / System Architecture Layout — Layout A(이미지 없음)(`docs/slide-design-rules/process-system-architecture-layout.md`)
- **Layout Selection Reason**: "순차 관계/공정 → Process/Flow 계열"에 정확히 부합. Layout A 선택 사유는 위 이미지 근거 항목 참조(사진 확보 비율 <80%, 실제로는 컨셉 일러스트가 대부분이라 §3.1 "사진이 의미를 추가하지 못하는 경우"에도 해당).
- **Structural Check**: Component 수 4개(권장 범위 3~6개 충족). "기존 1세대 대비" 비교 프레이밍이 Insight Box에 누락 없이 반영됐는지 확인 필요. 확보된 10장의 컨셉 이미지는 Layout A 구조상 슬롯이 없어 사용하지 않음 — Optional 이미지를 억지로 빈 공간에 채우지 않는다는 원칙에 부합.

---

## Slide 13. 2세대 공정의 가격·기술 경쟁력

- **Source Material**: CG17(entire), CG18(entire)
- **Core Message**: 코솔러스 2세대 공정(유도가열)은 기존 소성로(Pusher Kiln) 대비 짧은 공정시간·빠른 승온속도·적은 에너지 투입 등에서 우위를 가지며(일부 항목은 기존 대비 열세일 수 있음), 고순도 코발트 회수·특허 등 기술 신뢰도 근거도 갖는다.
- **Core Claims & Evidence**:
  - Claim 1: 2세대 공정(유도가열)은 기존 소성로 대비 다수 기준에서 경쟁력이 있다.
    - Evidence: 공정시간(10시간 이상 → 1분 이내) / 승온속도(기존 대비 200배) / 에너지 투입(432Wh/kg, 64% 절감) / 흑연 순도(99% 이상, 기존 값 원문 미기재) — CG18 metrics confirmed
    - Relationship: Before/After(정확히 2개 대상, 다기준 비교)
    - Required/Optional: Required(4개 비교 기준 전체) + 각주 Required("※ 기존 소성로 대비 열세 항목" — 원문에 이 캐벗 문구만 있고 구체적으로 어떤 항목이 열세인지는 원문에 명시되지 않음. 임의로 항목을 지어내지 않고 캐벗 문구 자체를 각주로 그대로 보존)
  - Claim 2(공유 근거, Claim 1의 기술경쟁력 부분을 보강): 2세대 공정은 추가 기술 신뢰도 근거를 갖는다.
    - Evidence: Co 회수 순도 >95%(CG17) / PCT 2건 출원(CG17·CG18 중복 언급, confirmed)
    - Relationship: 단일 독립 근거 2건(병렬 나열)
    - Required/Optional: Optional(Claim 1이 이미 핵심 주장을 성립시키며, 이 근거는 보강 성격)
  - 이미지 근거(신규 확인, 구 schema에는 전혀 없었음): img34(모듈형 산업 장비 실사진, confirmed), img35(터널형 산업로 실사진, confirmed) — COSOLUS 실제 파일럿/양산 설비로 추정되는 실사진 → Claim 2를 뒷받침하는 브랜드 진정성 높은 시각 근거, Optional. img30(건식환원 설비 렌더링, confirmed이나 실사진 아님)·img31~33(구조적 소속만 confirmed, 개별 내용 uncertain)은 사용하지 않음(우선순위상 실사진 img34/35만 채택, 밀도 관리).
- **Backward Completeness Check**: 명시반영 8(CG17 텍스트 2 + metrics 2 + CG18 텍스트 4 중 2 + metrics 6) / Core Message반영 1("※ 기존 소성로 대비 열세 항목" 각주 — 구체 항목 미기재로 처음에는 "COSOLUS가 모든 기준에서 우위"로 오독될 위험이 있는 캐벗 문구라 재확인, 각주로 명시 보존) / 라벨제외 2(두 Group 제목 중복) / uncertain보류 2(img31~33) / 미반영 0. **v2 대비 정정**: 과거 v2 outline은 이 슬라이드에 "시설투자비용(높음 vs 낮음)"·"온도정밀도(낮음 vs 높음)" 2개 비교 기준을 포함했으나, 현재 material_analysis.json의 CG18 metrics에는 이 두 항목이 존재하지 않는다 — 원본에 없는 수치를 만들지 않는다는 원칙에 따라 v3에서는 이 두 기준을 제외하고, 대신 원문의 "※ 열세 항목" 캐벗 문구를 각주로 그대로 보존하는 방식으로 대체했다.
- **Content Roles**:
  - Primary: 기존(Pusher Kiln) vs COSOLUS(2세대 유도가열) — 정확히 2개 대상 다기준 비교
  - Dependent: 4개 세부 비교 기준 + 열세 항목 각주
  - Shared Supporting: Co 회수 순도, PCT 출원 + img34/35(실사진)
  - Conclusion/Takeaway: N/A(비교표 자체가 결론)
- **Relationship**: Before/After(정확히 2개 대상, 다기준)
- **Content Regions**: Existing(Pusher Kiln) Column / COSOLUS(유도가열) Column — 동일 기준 Row 병렬 비교(4개 기준, 데이터 없는 항목은 "-" 표기) + 하단 각주("※ 일부 기준은 기존 소성로 대비 열세일 수 있음") + 하단 보조 Evidence Region(Co 순도, PCT 출원 텍스트 + img34/35 실사진 소형 배치)
- **Selected Layout**: Before + After Layout — Variant B(Before/After Comparison Table)(`docs/slide-design-rules/before-after/before-after.md`)
- **Layout Selection Reason**: 정확히 2개 대상, 동일 기준 다항목으로 "무엇이 얼마나 개선되는가"를 보여주는 Variant B Use When에 정확히 부합.
- **Structural Check**: CG19(경쟁력-솔루션2, 본문 전무)는 CG18과 주제 중복으로 별도 슬라이드 생성 안 함(coverage_check에 이미 기록). 데이터 없는 셀("흑연 순도" Existing 등)은 "-"로 표기하고 임의 수치를 채우지 않음.

---

## Slide 14. 투자 포인트

- **Source Material**: CG21(entire)
- **Core Message**: 코솔러스는 검증된 기술력과 구체적 사업화 방향을 바탕으로 Series A2 라운드 80억원 투자 유치를 추진한다.
- **Core Claims & Evidence**:
  - Claim 1: 코솔러스는 최상위 수준의 기술 경쟁력을 갖췄다.
    - Evidence: 추출제 최상위 합성·정제 기술 / 친환경 공정 기술(건식환원·유도가열) / Closed-loop system 기술
    - Relationship: 복수 비교 근거(3개 병렬 기술 축) / Required(3항목 전체)
  - Claim 2: 코솔러스는 세대별로 구체적 사업화 방향을 갖고 있다.
    - Evidence: (1.5세대 RECYION) XX하이텍·XX코 등 PoC 진행 중 / (2세대 친환경 공정) XX자동차 연계 신공급망, 일본·인도네시아 시장 진출
    - Relationship: 기타(1.5세대·2세대 두 트랙 병행)
    - Required/Optional: Required(두 트랙 모두 — 마스킹된 실명 원문 그대로 유지)
  - Claim 3: 코솔러스는 Series A2로 80억원 투자를 유치한다.
    - Evidence: 투자라운드 Series A2, 목표 투자유치 금액 80억원(confirmed)
    - Relationship: 단일 독립 근거 / Required
  - Claim 4: 투자금은 해외 진출·공장 건설에 사용된다.
    - Evidence: 국외법인 설립·운영 / 토지 구매·건축(추출제 CAPA, 공정파일롯)
    - Relationship: 단일 독립 근거(2항목 나열) / Required
- **Backward Completeness Check**: 명시반영 6(제목 제외 3개 bracket 항목 텍스트 + metrics 2) / 라벨제외 1(제목) / 미반영 0.
- **Content Roles**:
  - Primary: 4개 병렬 항목([기술력]/[사업화 방향]/[투자라운드]/[투자금 사용 계획])
  - Dependent: 각 항목 세부 내용
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 투자라운드(Series A2, 80억원)가 사실상 핵심 결론
- **Relationship**: 병렬(4개 대등 항목) + 그중 하나(투자라운드)가 Conclusion 성격
- **Content Regions**: 4개 병렬 Region — Claim 1(3항목 리스트) / Claim 2(2트랙 병행 텍스트) / Claim 3(Large Number Hero) / Claim 4(2항목 리스트) — Claim 3만 Large Number로 시각적 강조 유지, 나머지는 리스트 표현
- **Selected Layout**: Two-Column Summary 변형, Layout Catalog L18(`docs/layout-reference/2026.08.13_layout-catalog_V1.md`)
- **Layout Selection Reason**: 4개 항목이 대등 병렬 나열되는 구조에 맞는 전용 Layout Reference가 없어(Three-Column은 3개 항목 전제) L01~L33에서 목적이 가장 근접한 L18을 선택 후 4-Region 그리드로 최소 변형(Layout Routing 6번).
- **Structural Check**: 마스킹된 실명 그대로 유지. 투자금액(80억원) 원문 그대로. 4개 Region Parallel Layout Alignment 확인 필요.

---

## Slide 15. 일본·인도네시아 시장 진출

- **Source Material**: CG22(entire), CG23-ST08(partial — cross_group_ref로 가져온 img76/77/78만)
- **Core Message**: 코솔러스는 5억 명 이상 아시아 경제권을 겨냥해 일본과 인도네시아를 전략적 거점으로 세계시장 진출을 추진한다.
- **Core Claims & Evidence**:
  - Claim 1: 인도네시아에서 구체적 투자 논의가 진행 중이다.
    - Evidence: 전기자전거 업체 1대주주와 투자 논의(서술, confirmed) / SWAP 로고(img36, CG22 구조적 confirmed) / MUKTI 로고(img76)·eCoNiL 로고(img77)·IBC 로고(img78) — CG23-ST08 cross_group_ref, 전부 confirmed(배포 asset과 파일 크기까지 일치)
    - Relationship: 단일 독립 근거(논의 현황 서술) + 이미지 근거(직접 대응)
    - Required/Optional: Required(논의 현황 서술) / Optional(로고 4종)
    - **정정**: img79(HLI Green Power 로고로 추정)는 content_match_confidence uncertain이며 과거 v1/v2에서도 미사용 이력이 있어 Evidence 후보에서 완전히 제외(Optional로도 올리지 않음)
  - Claim 2: 일본에서도 투자 논의가 진행 중이다.
    - Evidence: 현지투자사·재료업체 등과 투자 논의(익명 서술, confirmed) — Panasonic Energy(img37)/Iwatani(img38)/DNP(img39) 로고(이미지 정체는 confirmed)
    - Relationship: 단일 독립 근거(논의 현황 서술)
    - Required/Optional: Required(서술) / Optional(로고 — 사용 시 특정 파트너십 단정 문구 없이 "일본 배터리·소재 생태계" 맥락으로만, NC-04)
  - Evidence-Claim 매핑: 인도네시아 로고(img36+cross-ref 3종)는 Claim 1에 직접 대응하는 근거이나, 일본 로고(Panasonic/Iwatani/DNP)는 Claim 2의 익명 서술과 구체적으로 매칭된다는 확정 근거는 없다(NC-04) — 두 로고 그룹을 동일한 확정 근거로 동등하게 다루지 않는다.
- **Backward Completeness Check**: 명시반영 3(목표 텍스트 + 2개 논의현황 텍스트) / uncertain보류 1(img79, 완전 제외) / 미반영 0. img36~39, img76~78 모두 confirmed로 반영.
- **Content Roles**:
  - Primary: 목표(일본·인도네시아 전략 거점, 5억 명 아시아 경제권)
  - Dependent: 국가별 논의 현황(Claim 1·2)
  - Shared Supporting: 관련 파트너 로고 이미지
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(일본 vs 인도네시아, 2개 거점)
- **Content Regions**: 상단 목표 서술 / 좌우 병렬 Region — 인도네시아(Claim 1 + SWAP·MUKTI·eCoNiL·IBC 4개 로고) / 일본(Claim 2 + Panasonic·Iwatani·DNP 3개 로고, 단정 문구 없음)
- **Selected Layout**: Symmetric Two-Split, Layout Catalog L25(`docs/layout-reference/2026.08.13_layout-catalog_V1.md`)
- **Layout Selection Reason**: 두 국가가 대등한 위계로 병렬 제시되는 구조. 전용 Layout Reference 중 이 구조(2개 대등 지역 거점 + 이미지/로고 근거)에 맞는 문서가 없어 L01~L33에서 선택.
- **Structural Check**: NC-04 반영 — 일본 로고는 단정 문구 없이 배치. img79(HLI 추정)는 사용하지 않음. 이미지 refs 정정 완료(img36/37/38/39는 CG22 자체 소속, img76/77/78은 CG23-ST08에서 cross_group_ref로 가져온 것 — v2가 사용했던 "img71~74" 번호는 구 추출본 기준이라 이번 새 추출본 번호와 다름, 혼동 금지).

---

## Layout Routing 6번(적합한 Layout 없음) 적용 총평

- **Slide 5(순환 관계)**: Claim 3(제조→재활용→제조)만 국소적으로 순환 구조 — Three-Column 내부에 소형 Cycle Diagram만 추가해 해결.
- **Slide 11(구성요소별 기여도)**: Contribution 전용 Layout은 없지만 Visual+Insight Variant D의 Evidence Area 내부에 두 기여 요소를 병렬 mini 시각으로 배치해 해결.
- **Slide 14(4개 대등 항목 병렬)**: Three-Column은 3개 항목 전제라 부적합, L18을 4-Region 그리드로 최소 변형.
- Product/Application Layout: "하나의 중심 제품이 여러 적용처로 확장" 구조에 해당하는 원본 콘텐츠 묶음이 없어 미사용.

## v2 대비 주요 변경점 요약(새 material-analysis 스키마 반영 결과)

| 슬라이드 | 변경 내용 |
|---|---|
| Slide 3 | 프레이밍 문장("수요-공급 미스매치")을 Core Message에 명시 추가(1-c 재확인) |
| Slide 6 | v2가 "확인 필요"로 남겨뒀던 이미지(1세대 개념도, 화학구조식)를 이번엔 명확히 GLENCORE 로고(무관)·D2EHPA/RECYION 미확인으로 확정 → 이미지 전면 미사용, 텍스트 전용 Before/After로 확정. D2EHPA 식별 텍스트를 Before Evidence에 추가 반영 |
| Slide 9 | 이미지 refs 정정(img10/img11, 구 번호 체계와 다름) |
| Slide 10 | img12가 실제로는 5종 재료구조 비교도(전기화학 다이어그램 아님)임을 재확인, 미사용 유지(사유 정정) |
| Slide 11 | img13(선택적 Li+ 포집 메커니즘도)을 Contribution Region 보조 시각으로 신규 추가 |
| Slide 12 | "기존 1세대 공정 대비" 비교 프레이밍과 "폐흑연 처리 포함"을 1-c로 새로 발견해 반영. 이미지가 대부분 컨셉 렌더링(실사진 아님)임을 재확인해 Layout A 선택 근거를 더 명확히 함 |
| Slide 13 | 신규 발견 이미지(img34/35, 실제 COSOLUS 설비 사진)를 Shared Supporting Evidence로 추가. v2에 있던 "시설투자비용/온도정밀도" 비교 기준은 현재 material_analysis.json에 근거가 없어 제외하고 "※ 열세 항목" 원문 각주로 대체 |
| Slide 15 | 이미지 refs 정정(img36~39, img76~78 — v2의 "img71~74" 번호와 다른 새 추출본 기준) |
| 그 외 9개 슬라이드 | Relationship·Layout 판단 동일 유지 |
