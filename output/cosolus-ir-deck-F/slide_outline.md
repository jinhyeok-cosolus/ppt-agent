# slide_outline.md — cosolus-ir-deck-F

> 입력: `material_analysis.json`, `slide_composition_map.json`(23개 슬라이드 경계 확정). 이 문서는 그 경계를 재판단하지 않고 슬라이드 내부의 Content Role/Relationship/Content Region/Layout Routing/구조적 사전 점검만 수행한다.
> 참조 규칙: Hard Rule(`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`) > Claude PPT Design System §5(Content Relationship/Region Composition) > Content Visualization Freedom > Layout Reference(특수 Layout Reference 우선, 없으면 L01~L33).

---

## Slide 1. 표지

- **Source Material**: CG01(entire)
- **Core Message**: "지속 가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술" — 코솔러스의 사업 정체성을 한 문장으로 제시하는 표지.
- **Core Claims & Evidence**:
  - Claim: 코솔러스는 배터리 재활용을 위한 화학소재·공정기술 기업이다.
    - Evidence: 표지 제목 원문 "지속 가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술"
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1 / Core Message반영 0 / 중복통합 0 / 라벨제외 0 / uncertain보류 0 / 미반영 0. 미반영 항목 없음(원본 콘텐츠가 표지 제목 1건뿐).
- **Content Roles**:
  - Primary: 표지 제목 텍스트
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region A(Primary, 표지 제목 Text) — Hard Rule §9 공통 Header/CI와는 별개로 표지 전용 Brand Block 구조를 따름.
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: 표지 슬라이드이므로 Hard Rule 상 표지 전용 규칙이 4순위 범용 Layout Reference보다 항상 우선 적용됨. `docs/cover-reference/cosolus_cover_reference.png.png`를 Primary Cover Design Reference로 사용.
- **Structural Check**: 문제 없음. Background Image는 표지 문서의 Soft Rules 우선순위(사용자 제공 → Library → 단색 대체)에 따라 web-ppt-generator 단계에서 선택.

---

## Slide 2. 기업소개

- **Source Material**: CG02(entire)
- **Core Message**: 코솔러스는 전북(전주·익산·완주·군산) 소재 27명 규모의 화학소재/공정기술 기업이며, 사용 후 배터리 핵심광물 회수를 통해 지속가능한 미래를 선도하는 것을 비전으로 한다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스의 기본 정체성(회사명·대표자·규모·소재지·핵심가치·비전)
    - Evidence: 기업명(주식회사 코솔러스), 대표자(김성현), 임직원(27명), 소재지(전주/익산/완주/군산), 핵심가치, 비전 문구 — 전부 material_analysis.json CG02.direct_evidence.confirmed_text
    - Relationship: 병렬 동등 항목(Parallel/Peer Items) — 기업명/대표자/임직원/소재지/비전은 서로 비교·인과 관계가 아니라 동등한 자격으로 나열되는 기업 프로필 속성
    - Required/Optional: Required
  - Claim: 사업장이 전북 4개 지역(군산·익산·전주·완주)에 분산돼 있다.
    - Evidence: img1(전북 지역 사업장 위치 지도, content_match_confidence: confirmed)
    - Relationship: 병렬 동등 항목(4개 지역이 지도 위에 동등하게 표시)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 7(핵심가치/기업명/대표자/임직원/소재지/비전/img1) / Core Message반영 0 / 중복통합 0 / 라벨제외 2("섹션명: Company", "제목: 기업소개" — 정보량 없는 라벨) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 기업 기본정보 블록(기업명/대표자/임직원/소재지/비전) + 지도 이미지(img1) — 대등한 두 Primary(정보 vs 위치)로 병렬 Main Content Group 구성
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(정보 블록과 지도가 함께 "회사를 소개"하는 병렬 관계)
- **Content Regions**: Region A(좌, Primary #1 — 기업 기본정보 Text 병렬 나열, 압축형) / Region B(우, Primary #2 — img1 지도, 면적 점유형 Visual, 세로 방향 적극 활용)
- **Selected Layout**: Company Introduction (`docs/slide-design-rules/02_instruction_design_V1.md`)
- **Layout Selection Reason**: Use When "회사명/대표자/임직원/소재지/비전 등 기본 정보 + 좌(정보)/우(세로 이미지) 2단 구조" 정확히 부합, 제작 지시문(CG02-PD01, PD02)도 동일 구조를 명시. Business Site Map — Pin + Outside Card(`021_business-site-map.md`)도 후보로 검토했으나, 해당 문서가 "사업장 2개 이상"일 때 단일 사업장 패턴을 기계적으로 확장하기 전에 사용자 확인을 요구하도록 명시(§4)하고 있고 본 슬라이드는 4개 지점을 하나의 지도에 함께 표시하는 형태라 Business Site Map의 "Pin 1개+Card 1개" 기본 패턴과 맞지 않아 제외 — Company Introduction의 "우측 세로 이미지" 슬롯에 지도 이미지를 그대로 배치하는 쪽을 선택.
- **Structural Check**: 문제 없음. 다만 지도 표현 방식이 Business Site Map의 Pin+Card 패턴이 아니라 이미지 1장(img1) 그대로 배치되는 형태이므로, 실제 시각적 디테일(Pin/라벨 강조 등)은 web-ppt-generator가 Content Visualization Freedom 범위에서 판단. 다중 사업장 확장 규칙 자체가 필요해지면(예: 추후 각 사업장별 개별 카드 요구) 021 문서 규칙에 따라 사용자 확인이 필요함을 메모.

---

## Slide 3. 문제제기 - 환경 및 지정학적 요인

- **Source Material**: CG03(entire)
- **Core Message**: 배터리 산업은 환경오염, 핵심광물 고갈, 특정국가(중국) 편중 공급망이라는 세 가지 문제에 동시에 직면해 있다.
- **Core Claims & Evidence**:
  - Claim ①(환경오염): 배터리 밸류체인은 상당한 환경부하·사회적 비용을 유발한다.
    - Evidence: "니켈 1톤당 133톤 폐기물 발생"(metric), "채굴 산업의 노동 및 인권문제"(서술), img2/img3/img4/img5(관련 사진, content_match_confidence: uncertain), 출처(IEA 2025; Benchmark Mineral Intelligence 2025; Earthworks 2026)
    - Relationship: 단일 독립 근거(133톤이라는 대표 수치 + 서술)
    - Required/Optional: 133톤 수치·서술=Required, img2~5=Optional(uncertain이므로 Required 승격 금지)
  - Claim ②(핵심광물 고갈): 리튬 등 핵심광물은 채굴 공급만으로 수요를 충당하지 못해 부족이 심화된다.
    - Evidence: img7(리튬 수요량 차트, 2030년 채굴공급465kt+부족1kt / 2040년 채굴공급750kt+부족250kt, content_match_confidence: confirmed)
    - Relationship: 시간에 따른 변화·추세(2030→2040, 2개 시점) — 대표값(2040 수치)만이 아니라 2030/2040 두 시점의 채굴공급·부족량 전체를 근거로 유지
    - Required/Optional: Required
  - Claim ③(공급망 편중): 중국이 전략광물 정제·블랙매스 처리를 사실상 장악하고 있다.
    - Evidence: "전략광물 20개 중 19개 정제 1위"(metric), "전략광물 정제 평균 점유율 70%"(metric), "글로벌 블랙매스 처리 비중 89%"(metric), img6(중국 강조 지도, confirmed)
    - Relationship: 병렬 동등 항목(19개/70%/89% 세 수치가 서로 다른 측면을 나열)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 9(3개 metric군 전체+각주 출처+7개 이미지) / Core Message반영 0 / 중복통합 0 / 라벨제외 2("섹션: Background", "제목: 문제제기...") / uncertain보류 4(img2~5) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3개 컬럼(환경오염 / 핵심광물고갈 / 공급망편중) — 대등한 Primary 3개로 병렬 Main Content Group
  - Dependent: 각 컬럼의 이미지(img2~7)는 해당 컬럼 Claim에 종속
  - Shared Supporting: 각주 출처(3개 컬럼에 공통 적용)
  - Conclusion/Takeaway: N/A(단순 병렬 문제제기, 통합 결론 불필요)
- **Relationship**: 병렬
- **Content Regions**: Region A(환경오염, Primary #1, Text+Photo uncertain) / Region B(핵심광물고갈, Primary #2, Chart 원본 재사용) / Region C(공급망편중, Primary #3, Map+Text) / Supporting Region(공통 각주, 3개 컬럼 하단 공유)
- **Selected Layout**: Three-Column Insight Layout (`docs/slide-design-rules/three-column/three-column.md`)
- **Layout Selection Reason**: 동일 위계의 독립적 문제 3개를 병렬 제시(special-layout-index Use When 정확 부합), 제작 지시문(CG03-PD01)도 3컬럼 구조를 명시.
- **Structural Check**: img2~5(환경오염 컬럼 후보 4장)를 어느 것으로 좁힐지는 material_analysis.json NC-08로 이미 별도 기록됨 — 이 슬라이드에서는 uncertain 표시를 유지한 채 web-ppt-generator 단계의 이미지 선택 판단으로 이관. 나머지 문제 없음(3컬럼 정보량 대체로 균형).

---

## Slide 4. 왜 지금인가 - 산업적 요인

- **Source Material**: CG04(entire)
- **Core Message**: 2030년 이후 전기차 폐배터리·ESS 시장이 급격히 성장하므로, 시장이 본격 개화하기 전에 재료·공정 역량을 지금 확보해야 한다.
- **Core Claims & Evidence**:
  - Claim ①: 전기차 폐배터리 발생량이 2030년을 기점으로 폭발적으로 증가한다.
    - Evidence: img8(2023:18GWh / 2030:338GWh / 2040:3,339GWh, 배터리수명10년), confirmed
    - Relationship: 시간에 따른 변화·추세(3개 시점 값 전체 유지)
    - Required/Optional: Required
  - Claim ②: 북미 ESS 시장이 고성장 국면으로 전환된다.
    - Evidence: img9(2024:50→2028:150GWh, CAGR31.6%), confirmed
    - Relationship: 시간에 따른 변화·추세(5개 연도 값 전체 유지)
    - Required/Optional: Required
  - Claim ③: 시장이 본격 개화하기 전에 재료·공정을 확보해야 한다.
    - Evidence: img10("5 YEARS" 범용 그래픽, uncertain) / 복구된 인용구(White House OSTP, "신소재가 발견에서 시장 진입까지 통상 10~20년 소요")
    - Relationship: 단일 독립 근거(신소재 상용화 소요기간이라는 외부 근거 하나)
    - Required/Optional: img10=Optional(uncertain), 복구된 인용구=Optional(핵심 주장을 보강하나 그 자체가 없어도 ①②의 시장 성장 근거만으로 "지금이 적기"라는 주장은 성립 — Required로 격상하지 않음, 다만 material_analysis.json NC-01에 따라 실제 사용 여부는 사람 확인 필요)
- **Backward Completeness Check**: 명시반영 11(2개 차트 데이터 전체+CAGR+각주+img10+복구인용구) / Core Message반영 0 / 중복통합 0 / 라벨제외 3("섹션: Background","제목: 왜 지금인가...","테두리없는 3컬럼") / uncertain보류 1(img10) / 미반영 0. 미반영 항목 없음 — 특히 CG04-REC01(복구된 인용구)이 1-b Claim③의 Evidence로 정상 반영됨을 확인(반복 유실 패턴 점검 대상이었음).
- **Content Roles**:
  - Primary: 3개 헤더박스(전기차폐배터리발생전망 / ESS시장성장전망 / 시장개화전확보필요성) — 병렬 Main Content Group
  - Dependent: 각 헤더박스의 차트/그래픽
  - Shared Supporting: 각주 출처(3개 컬럼 공통)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A(Primary #1, Chart 원본 재사용) / Region B(Primary #2, Chart 원본 재사용) / Region C(Primary #3, Text+Optional Graphic — img10 uncertain이므로 인용구 텍스트를 주된 표현으로, img10은 보조로만 검토) / Supporting Region(공통 각주)
- **Selected Layout**: Three-Column Insight Layout (`docs/slide-design-rules/three-column/three-column.md`)
- **Layout Selection Reason**: CG03과 동일 근거(3개 독립 문제·근거가 병렬 제시). 제작 지시문(CG04-PD01)도 3컬럼 구조 명시.
- **Structural Check**: Region C가 Region A/B(둘 다 실측 차트 보유) 대비 근거 밀도가 낮음(img10 uncertain + 복구 인용구 하나) — 병렬 3-Column 정보량 불균형 가능성. 해결책은 이 스킬 범위를 넘는 콘텐츠 자체의 한계(원본에 Region C를 뒷받침할 확정 근거가 부족)이므로, Region C를 구조적으로 얇게 유지하되 인용구 텍스트를 시각적으로 충분히 강조해 균형을 보완하도록 web-ppt-generator에 전달. img10 사용 여부와 복구 인용구 표기 여부는 NC-01에 따라 최종적으로 사람 확인 필요.

---

## Slide 5. 비즈니스 모델

- **Source Material**: CG05(entire)
- **Core Message**: 코솔러스의 비즈니스 모델은 환경오염 저감, 도시광산 구축, 신공급망 구축이라는 세 축으로 구성된다.
- **Core Claims & Evidence**:
  - Claim: 3개 헤더박스(환경오염저감/도시광산구축/신공급망구축) 각각의 설명 문구
    - Evidence: "유해물질 억제 및 온실가스 감축으로 환경 오염 저감" / "폐자원으로부터 핵심 광물 확보로 배터리 원재료 수요부족 해결" / "제조 → 재활용 → 제조로 이어지는 재활용 기반 新공급망 구축"
    - Relationship: 병렬 동등 항목
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 6(3개 헤더박스 제목+설명) / Core Message반영 0 / 중복통합 0 / 라벨제외 0 / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3개 헤더박스
  - Dependent: 각 박스의 아이콘(제작 지시문 CG05-PD01에 따라 콘텐츠에 맞는 아이콘 삽입 예정)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(각 헤더박스, Primary, Icon+Text 압축형)
- **Selected Layout**: Three-Column Insight Layout (`docs/slide-design-rules/three-column/three-column.md`)
- **Layout Selection Reason**: 동일 위계의 독립 메시지 3개 병렬(제작 지시문 CG05-PD01도 3컬럼 명시).
- **Structural Check**: 문제 없음. 3개 박스 정보량 균등.

---

## Slide 6. 재활용 공정 현황 (1세대)

- **Source Material**: CG06(entire)
- **Core Message**: 1세대 재활용 공정(전처리→후처리)은 실제로 작동하지만, 소재·공정 양쪽에 구조적 한계가 있어 개선이 필요하다.
- **Core Claims & Evidence**:
  - Claim ①(공정 흐름): 1세대 공정은 전처리(폐배터리→블랙매스)와 후처리(양극재 재활용공정→MnSO4/CoSO4/NiSO4/Li2CO3+폐흑연)로 구성된다.
    - Evidence: img15(폐배터리, uncertain)→img16(블랙매스, confirmed) / img18(양극재재활용공정, uncertain)→img11~14(4개 금속염, confirmed)+img17(폐흑연, confirmed)
    - Relationship: 순차 공정/프로세스(전처리→후처리 단계별 흐름 전체 유지, 대표 산출물 하나로 축약하지 않음)
    - Required/Optional: 공정 단계 구조 자체=Required, 개별 사진 중 img15/img18=Optional(uncertain), img11~14/16/17=Required(공정 결과물을 직접 보여주는 확정 근거)
  - Claim ②(소재의 한계): 낮은 선택성, 제한된 동작환경, 상분리 불안정, 부산물 과다발생(망초 등)
    - Evidence: 4개 항목 서술 원문
    - Relationship: 병렬 동등 항목(4개 한계가 서로 다른 측면을 나열)
    - Required/Optional: Required
  - Claim ③(공정의 한계): 1세대 재활용 공정은 경제성 확보에 실패했다(실제 사례).
    - Evidence: img19(Li-Cycle 로고, confirmed) / img20(Glencore 로고, uncertain)
    - Relationship: 병렬 동등 항목(2개 사례)
    - Required/Optional: img19=Optional(사례 예시, 없어도 "경제성 확보 실패" 주장 자체는 성립), img20=Optional(uncertain이므로 추가로 Required 불가)
- **Backward Completeness Check**: 명시반영 14(공정흐름 서술+10개 이미지+4개 소재한계 항목+공정한계 서술) / Core Message반영 0 / 중복통합 0 / 라벨제외 2("섹션: Background","1세대 공정:") / uncertain보류 3(img15,img18,img20) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 상단 공정 흐름(전처리→후처리) — 단일 Primary
  - Dependent: 공정 흐름을 구성하는 개별 사진(img11~20)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 하단 "소재 및 공정 개선 필요" 문구 — 상단 공정 흐름에서 도출되는 결론이므로 별도 통합 영역(Conclusion)으로 배치, 그 아래 소재의 한계/공정의 한계 두 세부 근거를 나란히 배치
- **Relationship**: 인과(공정 흐름 → 한계라는 결과) + 그 안에 병렬(소재의 한계 vs 공정의 한계 2개 하위 축)
- **Content Regions**: Upper Region(Primary, 공정 흐름 Process/Step Sequence, 사진 다수) / Lower-Left Region(소재의 한계, 병렬 목록) / Lower-Right Region(공정의 한계, 텍스트+2개 로고 사례) / Conclusion Region("소재 및 공정 개선 필요" 화살표+텍스트, Upper와 Lower 사이에 위치)
- **Selected Layout**: Process + Comparison Layout (`docs/slide-design-rules/process-comparison/process-comparison.md`)
- **Layout Selection Reason**: Use When "단계별 공정 흐름을 먼저 보여주고, 그 흐름과 직접 연결되는 문제점·한계를 하단에서 함께 전달" 정확 부합. 제작 지시문(CG06-PD01)의 "상단58%(공정흐름)+하단32%(한계)" 2단 구조와 문서 권장 비율(Upper 55~60%/Lower 40~45%)이 정합.
- **Structural Check**: 문제 없음. Dependent 이미지 10장이 Upper Region에 몰려 있어 밀도가 높으나 원본 production directive가 명시한 구조(각 물질명 개별 표기, 금속염+폐흑연 관계 "+" 표시)이므로 콘텐츠 과다로 보지 않음 — 다만 이미지 10장을 한 Region에 모두 담을 공간이 실제로 부족하면 web-ppt-generator 단계에서 content-visualization-freedom.md의 "내용 과다 시 요약/슬라이드 분할 제안" 검토 필요할 수 있음을 메모.

---

## Slide 7. [솔루션1] 개요 - 고성능 추출제 (1.5세대 화학소재)

- **Source Material**: CG07(entire)
- **Core Message**: 코솔러스의 1.5세대 추출제(RECYION Series)는 기존 공정의 후처리 단계에서 기존 추출제(D2EHPA)를 대체해 재활용 효율을 개선한다.
- **Core Claims & Evidence**:
  - Claim ①: 코솔러스 추출제는 기존 공정(페이지6 재사용)의 후처리 특정 지점에 적용된다.
    - Evidence: 페이지6 공정도식 재사용(cross_group_ref, CG06) + 강조 마커
    - Relationship: 단일 독립 근거(적용 위치 표시)
    - Required/Optional: Required
  - Claim ②: 기존 추출제(D2EHPA, 1세대)와 코솔러스 추출제(RECYION Series, 1.5세대)는 화학구조와 용도가 다르다.
    - Evidence: img21(D2EHPA 구조식, confirmed) vs img22(RECYION Series 일반화 구조식, confirmed), "광산·염호 기반 금속회수용" vs "재활용 효율 개선" 설명
    - Relationship: Before/After(기존 1세대 → 코솔러스 1.5세대, 2개 상태 비교)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 4(D2EHPA/RECYION 라벨+구조 이미지 2건) / Core Message반영 0 / 중복통합 1(페이지6 공정도식은 CG06에서 이미 반영된 이미지를 재사용 개념으로 통합, 새 이미지 추가 아님) / 라벨제외 0 / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 상단 공정도식(적용 위치 강조) — 단일 Primary
  - Dependent: 강조 마커
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(하단이 별도 Before/After 비교로 독립적 역할)
- **Relationship**: 인과(상단 공정 내 위치) + 비교(하단 기존 vs COSOLUS)
- **Content Regions**: Upper Region(Primary, 공정도식 재사용+강조선, 약 52%) / Lower-Left Region(기존 추출제 D2EHPA, Existing) / Lower-Right Region(COSOLUS 추출제 RECYION Series, Improved, 브랜드컬러 강조) — 약 38%
- **Selected Layout**: Process + Comparison Layout (`docs/slide-design-rules/process-comparison/process-comparison.md`)
- **Layout Selection Reason**: Use When "기존 기술과 신규 기술을 공정 맥락과 함께 비교" 정확 부합(공정도식을 먼저 보여준 뒤 하단에서 기존/신규 비교). Before+After Layout도 후보로 검토했으나, before-after.md Do Not Use "공정 흐름을 먼저 보여준 뒤 그 흐름과 연결된 비교를 하단에서 함께 다뤄야 할 때 → Process+Comparison 사용"에 해당해 제외. 제작 지시문(CG07-PD01)의 "상단52%(공정도식)+하단38%(2열비교)" 구조와 정합.
- **Structural Check**: 문제 없음. 하단 좌우 2열은 Parallel Layout Alignment 원칙(동일 Top Line/Height)을 따라야 함 — web-ppt-generator 구현 시 확인 필요.

---

## Slide 8. 핵심기술 - [솔루션1-1] 고성능 추출제: 공정시간/첨가제 비교

- **Source Material**: CG08(entire)
- **Core Message**: COSOLUS 추출제는 경쟁사(벨기에 S사, 중국 K사) 대비 공정시간이 짧고 첨가제 사용량이 적다.
- **Core Claims & Evidence**:
  - Claim: 3사(COSOLUS/벨기에 S사/중국 K사)의 공정시간·첨가제 사용량 비교
    - Evidence: 표(공정시간 행: img23/img24+"100%증가"/img25+"50%증가", 첨가제사용량 행: "-"/"10%이상추가"/"5%이상추가"), 각주("*블랙메스 1톤당 첨가제 사용량")
    - Relationship: 복수 비교 근거(3사 x 2기준, 표 전체 값 유지)
    - Required/Optional: Required(img23/24/25 모두 confirmed — 표 수치와 이미지 내 텍스트가 정확히 일치하는 확정 근거)
- **Backward Completeness Check**: 명시반영 5(표 전체+각주+헤더박스 문구) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3사 비교표(공정시간+첨가제사용량) — 단일 Primary(표 전체가 하나의 비교 근거 단위)
  - Dependent: 3장의 비커 실험사진(각 기업 셀의 지배적 콘텐츠)
  - Shared Supporting: 각주
  - Conclusion/Takeaway: 상단 헤더박스("공정시간 단축 및 첨가제 사용량 저감") — 표 전체를 종합하는 결론이므로 헤더박스로 상단에 배치
- **Relationship**: 비교
- **Content Regions**: Header Region(Conclusion, "COSOLUS 화학구조 설계 및 정제 기술 → 공정시간 단축 및 첨가제 사용량 저감") / Main Region(Primary, 3열 비교표, Cell 지배 콘텐츠=실험사진) / Supporting Region(각주, 표 하단)
- **Selected Layout**: Comparison Matrix Layout (`docs/slide-design-rules/comparison-matrix/comparison-matrix.md`)
- **Layout Selection Reason**: Use When "Cell의 지배적 콘텐츠가 사진·실험결과 등 면적 점유형 Visual Evidence이며 핵심 주장을 직접 증명하는 Required Evidence가 Visual일 때" 정확 부합(3장의 비커 실험사진이 각 셀의 핵심 근거). Table Comparison Layout은 Do Not Use("면적 점유형 Visual Evidence가 핵심 주장을 직접 증명하는 경우 → Comparison Matrix")에 해당해 제외.
- **Structural Check**: 문제 없음. COSOLUS 열 강조(브랜드컬러+굵은 테두리)는 제작 지시문(CG08-PD01)에 따라 유지, 5.7/019 강조 규칙과 정합.

---

## Slide 9. 핵심기술 - [솔루션1-1] 고성능 추출제: 추출단수/망초 저감

- **Source Material**: CG09(entire)
- **Core Message**: COSOLUS 추출제는 기존 대비 추출단수를 1단 줄이고(CAPEX 경제성) 망초 발생량도 줄여(OPEX 경제성) 이중의 경제성을 확보한다.
- **Core Claims & Evidence**:
  - Claim ①(CAPEX): 추출단수가 기존 5단 → COSOLUS 4단으로 20% 감소한다.
    - Evidence: img26(기존 5단 McCabe-Thiele 그래프)/img27(COSOLUS 4단), 표 "추출단수" 행(기존5/COSOLUS4)
    - Relationship: Before/After(기존→COSOLUS, 2개 상태 값 전체 유지)
    - Required/Optional: Required
  - Claim ②(OPEX): 니켈 1톤당 망초 발생량이 기존 3.6톤 → COSOLUS 3.3톤으로 줄고, 이를 국내 업체 연간 처리량 기준으로 환산하면 연 4,800톤 저감된다.
    - Evidence: 표 "니켈1톤당 망초양" 행(기존3.6톤/COSOLUS3.3톤), "4,800톤"(니켈16,000톤/년 생산 기준 환산 수치), 출처 각주
    - Relationship: Before/After(기존→COSOLUS 단위 수치) + 그로부터 도출된 환산 Large Number(4,800톤)
    - Required/Optional: Required(3.6→3.3톤 관계값 전체 필수, 4,800톤은 그 관계를 사업 규모로 환산한 강조 수치이므로 함께 Required)
- **Backward Completeness Check**: 명시반영 7(표 전체+2개 그래프+4,800톤+환산기준+제목1/2 문구) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 좌(추출단수 Before/After, 제목1) / 우(망초저감 Before/After+4,800톤 강조, 제목2) — 대등한 Primary 2개
  - Dependent: img26/27(좌측 그래프)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(좌우 각각 독립적 결론을 담고 있어 별도 통합 Conclusion 불필요)
- **Relationship**: 비교(2열, Before-After 구조)
- **Content Regions**: Region A(좌, 추출단수, Criteria Column+Existing/Improved Cell, 그래프 포함) / Region B(우, 망초저감, Criteria Column+Existing/Improved Cell + 4,800톤 강조 텍스트)
- **Selected Layout**: Before + After Layout — Variant B(Comparison Table) (`docs/slide-design-rules/before-after/before-after.md` §5)
- **Layout Selection Reason**: Use When "공정단수·비용·효율 등 동일 기준 수치 개선이 핵심"(Variant B 선택 기준: "기존 대비 무엇이 얼마나 개선되는가를 여러 기준으로 보여주는 것이 핵심") 정확 부합. 비교 대상이 기존/COSOLUS 정확히 2개.
- **Structural Check**: 문제 없음. 좌우 2개 Region이 각각 Criteria(추출단수 vs 망초양)를 담당하므로 §5.1 Region Map(Criteria/Existing/Improved 3열) 구조를 좌우 2세트로 적용. "4,800톤" 강조는 §5.7 Improved Column 강조 규칙 범위에서 처리.

---

## Slide 10. 경쟁력 - [솔루션1-1] 고성능 추출제 (3사 비교)

- **Source Material**: CG10(entire)
- **Core Message**: COSOLUS는 KopperChem, Solvay 대비 5개 평가항목(가격/추출성능/공정시간/첨가제사용량/탄소중립) 전 항목에서 최고 등급(◎)을 받는다.
- **Core Claims & Evidence**:
  - Claim: 3사(COSOLUS/KopperChem/Solvay)의 5개 항목 평가
    - Evidence: 표 전체(Country/국가(제품시리즈)/가격/추출성능/공정시간/첨가제사용량/탄소중립, 평가기호 ◎○△), 평가기준 범례
    - Relationship: 복수 비교 근거(3사 x 5항목, 전체 값 유지)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 3(표 전체+평가기준+"We promise tomorrow") / Core Message반영 0 / 중복통합 0 / 라벨제외 1("Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음. (NC-04: 표 2행 레이블 '국가' 오기는 material_analysis.json에 이미 기록, 원문 값 그대로 반영)
- **Content Roles**:
  - Primary: 5개 항목 x 3사 평가표
  - Dependent: 평가기준 범례(◉/○/△ 정의)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교
- **Content Regions**: Main Region(Primary, 표), Legend Region(Dependent, 범례)
- **Selected Layout**: Table Comparison Layout (`docs/slide-design-rules/table-comparison.md`) + Competitive Advantage Highlight 오버레이 (`docs/slide-design-rules/019_competitive-advantage-highlight.md`)
- **Layout Selection Reason**: Cell 지배 콘텐츠가 텍스트·기호·등급(◎○△)이며 사진 등 면적 점유형 Visual 없음 — Table Comparison Use When 정확 부합. 비교 대상 3개(3~4개 범위)이므로 019 Competitive Advantage Highlight로 COSOLUS 열 강조 적용(제작 지시문 CG10-PD01의 "COSOLUS 열 강조" 요구와 정합).
- **Structural Check**: 문제 없음.

---

## Slide 11. [솔루션1-2] 직접 리튬 추출 (DLE)

- **Source Material**: CG12(entire)
- **Core Message**: 기존 Li 재활용(4단계 순차 공정, 증발농축 기반 회수율 3.12%)과 달리, COSOLUS DLE는 병렬 구조로 Li를 우선 추출한다.
- **Core Claims & Evidence**:
  - Claim ①: 기존 Li 재활용은 침출→불순물제거→(Mn→Co→Ni→역추출 4단계)→증발농축 기반 회수(3.12%)의 순차 구조다.
    - Evidence: 원문 서술 전체("침출-불순물제거-[①Mn추출-②Co추출-③Ni추출-④역추출]4단계 -> 증발농축기반 Li회수(3.12%)")
    - Relationship: 순차 공정/프로세스(4단계 전체 유지, 최종 회수율만 대표로 남기지 않음)
    - Required/Optional: Required
  - Claim ②: COSOLUS DLE는 NCM/LFP 스크랩에서 Li를 우선 추출하는 경로와, 침출·불순물제거 후 Li를 추출하는 경로 2갈래 병렬 구조다.
    - Evidence: 원문 서술 2개 경로 전체
    - Relationship: 순차 공정/프로세스(병렬 2경로, 각 경로 전체 단계 유지)
    - Required/Optional: Required
  - Claim ③: 기존 DLE(증발법)의 실제 현장 사례
    - Evidence: img29(염호 증발연못, confirmed), img30(지열 브라인 설비, confirmed)
    - Relationship: 병렬 동등 항목(2장 참고사진)
    - Required/Optional: Optional(하단 참고자료 성격, 없어도 ①②의 핵심 비교 메시지는 성립)
- **Backward Completeness Check**: 명시반영 6(2개 공정 서술 전체+img28+img29+img30+제목) / Core Message반영 0 / 중복통합 0 / 라벨제외 2("섹션: Technology","두개 도식 비교...") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 좌(기존 Li 재활용, Existing) / 우(COSOLUS DLE, Improved, 병렬 분기) — 대등한 Primary 2개
  - Dependent: img28(공정도식, 좌측 구조를 뒷받침)
  - Shared Supporting: img29/img30(하단 참고사진, 좌우 어느 한쪽에 귀속되지 않고 "기존 DLE 증발법 일반"에 대한 공통 참고자료)
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교(Before/After) — Improved 쪽 내부에 순차 병렬 분기 포함
- **Content Regions**: Existing Column(좌, 4단계 순차 Step Sequence) / Transformation Arrow(중앙) / Improved Column(우, 2경로 병렬 분기 Step Sequence, Li추출 단계 Green 강조) / Shared Supporting Region(하단, img29/img30 참고사진 2장 가로 배치)
- **Selected Layout**: Before + After Layout — Variant A(Process Transformation) (`docs/slide-design-rules/before-after/before-after.md` §4)
- **Layout Selection Reason**: 비교 대상이 기존/COSOLUS 2개로 명확히 구분되고, "단계 수·순서·분기 등 Process 구조 자체가 달라지는 것"이 핵심 메시지(Variant A 선택 기준) — Improved(COSOLUS) 쪽만 2갈래로 분기하는 구조는 §4.4 Branching Process("한쪽만 분기하고 다른 쪽은 단일 경로")의 전형적 적용 사례. 제작 지시문(CG12-PD01)도 좌(세로형 단일)/우(병렬 2갈래)+중앙 화살표 구조를 명시.
- **Structural Check**: 문제 없음. §4.3 공통 Pitch 규칙에 따라 기존(4단계)과 COSOLUS 각 분기 경로의 Step Box 높이를 가장 긴 Flow(4단계) 기준으로 통일해야 함 — web-ppt-generator 구현 시 확인 필요. 하단 Shared Supporting(img29/30)은 특정 Column에 귀속시키지 않음(§4.9 Outcome/Result와 별개로 "기존 DLE 일반" 참고자료이므로 Comparison Frame 하단 공통 영역에 배치).

---

## Slide 12. [솔루션1-2] DLE 기술 동향 (4개 방식 비교)

- **Source Material**: CG13(entire)
- **Core Message**: DLE(직접리튬추출)에는 흡착제/추출제/분리막/전기화학 4가지 방식이 있으며, 기술성숙도와 장단점이 방식별로 다르다.
- **Core Claims & Evidence**:
  - Claim: 4개 방식(흡착제/추출제/분리막/전기화학)의 작동원리·TRL·장점·단점
    - Evidence: 표 전체(4행 x 4열) + img31~35(각 방식 작동원리 다이어그램, 전부 confirmed), 출처(Desalination, 2024)
    - Relationship: 복수 비교 근거(4방식 x 4기준, 표 전체 값 유지)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 3(표 전체+5개 이미지+출처) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 4방식 비교표(작동원리/TRL/장점/단점)
  - Dependent: 각 방식의 작동원리 다이어그램(img31~35)
  - Shared Supporting: 출처 각주
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교
- **Content Regions**: Main Region(Primary, 4x4 매트릭스, 작동원리 행=Diagram Cell, TRL/장점/단점 행=Text Cell) / Supporting Region(출처 각주)
- **Selected Layout**: Comparison Matrix Layout (`docs/slide-design-rules/comparison-matrix/comparison-matrix.md`)
- **Layout Selection Reason**: comparison-matrix.md Use When이 "작동원리, 성능, TRL, 장점, 단점 등 동일한 평가 기준을 여러 대상에 반복 적용할 때"를 명시적 예시로 들고 있어 본 슬라이드와 정확히 일치. Cell마다 시각적 구성이 다름(작동원리=Diagram, 나머지=Text)도 Comparison Matrix의 "Cell별 자유로운 시각적 구성 허용" 특성과 부합 — Table Comparison Layout(직각형 Grid, Cell 자유 구성 불허)은 이 혼합 구성과 맞지 않아 제외.
- **Structural Check**: 문제 없음.

---

## Slide 13. 핵심기술 - [솔루션1-2] Key Advantages of Extractant-Separator for DLE

- **Source Material**: CG14(entire, CG14-ST01/ST02/ST03 포함)
- **Core Message**: 추출제&분리막 방식은 4가지 원리적 장점을 가지며, 방사형 차트로 봤을 때도 흡착제·전기화학 대비 전반적으로 우수한 프로파일을 보인다.
- **Core Claims & Evidence**:
  - Claim ①: 추출제&분리막 방식의 4가지 장점(빠른 물질전달/우수한 재활용효율/용이한 연속운전/첨가제 소모량 감소)
    - Evidence: 4개 bullet 원문 전체
    - Relationship: 병렬 동등 항목(4개 장점이 서로 다른 원리적 측면을 나열)
    - Required/Optional: Required
  - Claim ②: 3개 방식(흡착제/전기화학/추출제&분리막)을 6개 축(재활용효율/공정시간/연속공정/에너지효율/양산성/친환경성)으로 비교하면 추출제&분리막이 가장 균형있게 우수하다.
    - Evidence: CG14-ST01(Adsorbent 6개 값)/ST02(Electrochemical 6개 값)/ST03(Extractant&Separator 6개 값) — 3계열 x 6축 전체
    - Relationship: 구성요소별 기여도(3개 대상의 6개 평가축 프로파일 비교 — 방사형 차트의 전형적 관계, 개별 대표값이 아니라 축별 값 전체 유지)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 22(4개 bullet+3계열×6값=18개 수치+계열명 3개) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 방사형 차트(3계열, Key Advantage Summary를 뒷받침하는 정량 근거) — 단일 Primary Visual
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 상단 4개 장점 bullet — 방사형 차트가 정량적으로 증명하는 결론적 메시지이므로 Conclusion/Summary 역할로 상단 배치
- **Relationship**: 인과(4개 장점 서술 → 방사형 차트가 그 근거를 정량 증명) + 그 안에 비교(3계열)
- **Content Regions**: Summary Region(Conclusion, 상단 4개 장점 bullet 세로 배열) / Chart Region(Primary, 하단 3-Column 방사형 차트, 6축 동일 규격)
- **Selected Layout**: Multi-Radar Technology Comparison (`docs/slide-design-rules/013_multi-radar-technology-comparison.md`)
- **Layout Selection Reason**: 원본 문서의 핵심 구조("Title + Key Advantage Summary + 3-Column Radar Comparison")가 이 슬라이드 콘텐츠 구조와 완전히 일치. 동일 6개 축으로 3개 방식을 비교하고 실제 정량 데이터(1~5점)가 존재해 Use When을 정확히 충족. 제작 지시문(CG14-PD01)도 "텍스트 세로 배열 후 그 아래 방사형 차트"를 명시.
- **Structural Check**: 문제 없음. 3계열 데이터 전체(18개 수치)가 Chart Region에 반영되어야 하며 일부만 대표로 축약하지 않음(Relationship 보존 우선 원칙).

---

## Slide 14. 핵심기술 - [솔루션1-2] COSOLUS DLE

- **Source Material**: CG15(entire)
- **Core Message**: COSOLUS의 화학구조 설계·정제·공정 기술은 핵심소재(재자원화율 3%→50%)와 분리막&THz기술(재자원화율 3%→90%)이라는 두 축을 통해 재자원화율 90% 이상, 공정비용 5,500원/kg 미만을 달성한다.
- **Core Claims & Evidence**:
  - Claim ①(핵심소재): 핵심소재 개선으로 재자원화율이 3%에서 50%로 향상된다.
    - Evidence: "재자원화율 3%→50%"(metric), img36(RECYION501 회수효율 차트+미시구조 이미지, content_match_confidence: uncertain — pH별 회수효율 곡선이며 "3%→50%" 수치와 1:1 대응은 아님)
    - Relationship: Before/After(3%→50%, 두 상태 값 유지)
    - Required/Optional: "3%→50%" 수치=Required(텍스트 자체가 원본에 명시된 확정 근거), img36=Optional(uncertain이므로 Required 승격 금지, 보조 시각자료로만 사용)
  - Claim ②(분리막&THz기술): 리튬 재자원화율이 3%에서 90%로 향상된다.
    - Evidence: "리튬 재자원화율 3%→90%"(metric), img37(THz진단 AI프로세스 다이어그램: 운전지속률85%/파울링현상Low/리튬순도99.5%/잔여수명예측2400h, confirmed)
    - Relationship: Before/After(3%→90%) + 구성요소별 기여도(THz 진단 프로세스의 4개 세부 지표)
    - Required/Optional: Required(둘 다 확정 근거)
  - Claim ③(종합 Impact): 위 두 기술의 결과로 재자원화율 90% 이상, 공정비용 5,500원/kg 미만을 달성한다.
    - Evidence: "재자원화율 >90%"(출처: KOMIS 2026), "공정비용 <5,500원/kg"
    - Relationship: 단일 독립 근거(종합 KPI 2건)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 6(2개 Before/After metric+2개 종합KPI+img36+img37) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 1(img36) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 좌(핵심소재 개선) / 우(분리막&THz기술 개선) — 대등한 Primary 2개(정확히 2개의 정량 개선효과)
  - Dependent: img36(좌 Primary 종속), img37(우 Primary 종속)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 상단 헤더박스(재자원화율>90%, 공정비용<5,500원/kg) — 좌우 2개 개선효과를 종합하는 Impact이므로 Integrated Conclusion으로 상단 배치
- **Relationship**: 병렬(정확히 2개의 정량 개선효과) + 인과(Core Tech→Improvement→Impact)
- **Content Regions**: Summary/Impact Bar(Conclusion, 상단, 재자원화율/공정비용 종합 수치) / Region A(좌, 핵심소재 3%→50%, img36 보조) / Region B(우, 분리막&THz 3%→90%, img37)
- **Selected Layout**: Benefit + Impact Layout (`docs/slide-design-rules/benefit-impact/benefit-impact.md`)
- **Layout Selection Reason**: Use When "기술 적용으로 개선되는 효과가 정확히 2개, 그래프·표·Diagram 등 서로 다른 Evidence로 동일 솔루션의 2개 효과를 증명" 정확 부합(핵심소재 vs 분리막&THz, 서로 다른 Evidence 유형). `Core Technology(COSOLUS 화학구조설계/정제/공정기술) → Improvement(2개) → Quantified Impact(재자원화율/비용)` 흐름과도 일치. Left-Right Tech Comparison(성능표 vs 원리도 2관점)도 후보로 검토했으나, 좌우가 "하나의 소재를 두 관점(성능/원리)"으로 보는 구조가 아니라 "두 개의 서로 다른 기술 축이 각각 정량 개선을 만드는" 구조라 Benefit+Impact가 더 정확히 부합해 채택.
- **Structural Check**: 문제 없음. img36의 content_match_confidence: uncertain 표시를 Content Region 설계에서도 유지(Required 근거는 텍스트 metric이며 이미지는 보조).

---

## Slide 15. [솔루션2] 개요 - 친환경 차세대 배터리 재활용 공정기술 (2세대)

- **Source Material**: CG16(entire)
- **Core Message**: 이제부터 코솔러스의 2세대 기술(친환경 차세대 배터리 재활용 공정기술)을 다룬다는 섹션 전환 메시지.
- **Core Claims & Evidence**:
  - Claim: 섹션 전환("[솔루션2] 개요 - 친환경 차세대 배터리 재활용 공정기술(2세대)")
    - Evidence: 제목 원문 자체
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1(제목) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음(원본에 실질 콘텐츠가 제목뿐).
- **Content Roles**:
  - Primary: 섹션 타이틀
  - Dependent: N/A / Shared Supporting: N/A / Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region A(Primary, Section Title, 압축형)
- **Selected Layout**: L02 Contents/Section (`docs/layout-reference/2026.08.13_layout-catalog_V1.md` L02)
- **Layout Selection Reason**: 특수 Layout Reference 인덱스에 이 슬라이드의 "섹션 전환/Navigation" 구조에 맞는 항목이 없어(콘텐츠가 사실상 타이틀뿐, 비교·공정·차트 등 관계형 구조 부재) L01~L33 범용 카탈로그로 이관 — L02 "Navigation/chapter transition" 용도가 정확히 부합.
- **Structural Check**: 실질 콘텐츠가 거의 없는 섹션 전환 슬라이드임을 확인(정상 — CG16이 원본에서 독립 Heading으로 분리된 의도된 구조, slide_composition_map.json issues_found에 이미 병합 여부 검토 및 비병합 근거 기록됨).

---

## Slide 16. 핵심기술 - [솔루션2] 친환경 차세대 배터리 재활용 공정기술 (2세대) 개요

- **Source Material**: CG17(entire)
- **Core Message**: 2세대 공정은 블랙매스를 양극재용/음극재용으로 나누어 각각 건식환원·부유선별(니켈/코발트 회수)과 유도가열(고순도 정제흑연 회수)로 처리한다.
- **Core Claims & Evidence**:
  - Claim: 블랙매스가 2세대 공정을 거쳐 니켈/코발트와 고순도 정제흑연으로 분리 회수된다.
    - Evidence: 11개 라벨 원문(COSOLUS/건식환원/부유선별/니켈/코발트/전처리공정/양극재용블랙매스/유도가열/블랙매스/음극재용블랙매스/고순도정제흑연) — 원본에 노드 간 연결관계(화살표/순서)를 명시하는 문장이나 도식 이미지 없음(material_analysis.json NC-06)
    - Relationship: 순차 공정/프로세스(공통 시작점 블랙매스에서 양극재용/음극재용 2갈래로 분기하는 구조로 추정 — 라벨 배치 자체가 판단이며 원본에 명시된 관계는 아님)
    - Required/Optional: Required(11개 라벨 전체가 2세대 공정 전체를 조망하는 유일한 근거)
- **Backward Completeness Check**: 명시반영 11(11개 라벨 전체) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음 — 다만 라벨 간 연결관계 자체가 원본에 없다는 점은 NC-06으로 이미 별도 기록되어 있으며, 이 슬라이드의 다이어그램 구조(양극재용/음극재용 분기)는 이후 페이지(CG18/CG19)의 구체적 설명에 근거한 재구성 판단임을 명시.
- **Content Roles**:
  - Primary: 공정 개요 다이어그램(11개 노드) — 단일 Primary
  - Dependent: N/A / Shared Supporting: N/A / Conclusion/Takeaway: N/A
- **Relationship**: 순차·분기(공통 시작점에서 2갈래로 분기)
- **Content Regions**: Region A(Primary, 공통시작(블랙매스/전처리공정) → 1차분기(양극재용/음극재용) → 각 Lane의 세부공정(건식환원+부유선별 / 유도가열) → 결과물(니켈/코발트 / 고순도정제흑연))
- **Selected Layout**: Flow Diagram — L25 Symmetric Two-Split (`docs/slide-design-rules/flow-diagram-rules.md` + `layout-catalog_V1.md` L25)
- **Layout Selection Reason**: Use When "하나의 공통 시작점에서 2개 이상의 갈래로 분기하는 공정을 보여줘야 하고, 각 갈래를 색상 등으로 뚜렷하게 대비" 부합(블랙매스→양극재용/음극재용 2갈래). Process/System Architecture Layout(좌→우 선형 단일 구조)은 이 슬라이드의 분기 구조와 맞지 않아 제외.
- **Structural Check**: **주의 필요** — 원본에 노드 간 연결관계가 명시되어 있지 않아(NC-06), 이 슬라이드의 다이어그램 구조는 CG18(건식환원)·CG19(유도가열) 페이지의 구체적 서술에서 역으로 추론한 재구성이다. 이는 원본에 없는 새 사실을 만드는 것이 아니라 이미 주어진 라벨의 배치 관계를 구성하는 것이므로 Content Visualization Freedom 범위 내 판단이나, 실제 web-ppt-generator 구현 전 사람 확인(Human Review ①)을 권장.

---

## Slide 17. 핵심기술 - [솔루션2] 건식환원

- **Source Material**: CG18(entire)
- **Core Message**: 건식환원 공정은 양극재용 블랙매스에서 코발트를 순도 95% 이상으로 회수하며, 관련 특허 2건을 출원했다.
- **Core Claims & Evidence**:
  - Claim: 양극재용 블랙매스 → 건식환원 → Co회수(순도>95%)의 3단 가로 공정
    - Evidence: img39(양극재용 블랙매스, confirmed) → img38(건식환원 도표, uncertain) → img40(Co, confirmed), "*PCT 2건 출원", "Co회수(순도>95%)"(metric)
    - Relationship: 순차 공정/프로세스(3단계 전체 유지)
    - Required/Optional: 공정 흐름 자체=Required, img38(중간단계 시각자료)=Optional(uncertain), img39/img40=Required(양 끝단 결과물의 확정 근거), 순도>95%/PCT2건=Required
- **Backward Completeness Check**: 명시반영 5(3단계 서술+헤더박스+순도/특허 수치) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 1(img38) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3단 공정 흐름(블랙매스→건식환원→Co회수)
  - Dependent: 각 단계 사진, 순도·특허 수치 라벨
  - Shared Supporting: N/A / Conclusion/Takeaway: 헤더박스("건식환원공정 → COSOLUS Originality")
- **Relationship**: 순차
- **Content Regions**: Header Region(Conclusion) / Main Region(Primary, Component01→02→03 좌→우 선형, 각 Component 아래 사진+라벨)
- **Selected Layout**: Process / System Architecture Layout — Layout B(이미지 있음) (`docs/slide-design-rules/process-system-architecture-layout.md`)
- **Layout Selection Reason**: Use When "공정 단계를 Component01→02→03처럼 좌→우 선형 구조로 순차 설명" 정확 부합, 비교 대상(기존vs신규) 없이 단일 공정 설명이므로 Process+Comparison·Before-After 제외. 사진이 있으므로 Layout B(사진 포함 변형) 적용.
- **Structural Check**: 문제 없음.

---

## Slide 18. 핵심기술 - [솔루션2] 유도가열

- **Source Material**: CG19(entire)
- **Core Message**: 유도가열 기술은 1분 이내 초고속 승온(기존 대비 200배)과 64% 에너지 절감, 99% 이상 고순도 재생흑연을 실현하며, 10시간 이상 걸리는 기존 소성로(Pusher Kiln) 대비 압도적으로 빠르다.
- **Core Claims & Evidence**:
  - Claim ①(가격경쟁력): 짧은 공정시간(1분 이내, 200배 빠른 승온속도)과 적은 에너지 투입(432Wh/kg, 64% 절감)
    - Evidence: img41(0초/400℃·5초/945℃·30초 승온 실측 사진, confirmed), 수치 4건
    - Relationship: 시간에 따른 변화·추세(0→5→30초, 3개 시점 온도 값 전체 유지) + 병렬 동등 항목(에너지 수치)
    - Required/Optional: Required
  - Claim ②(기술경쟁력): 고순도 재생흑연(99%이상), 균일한 온도분포, 낮은 부반응, PCT 2건 출원
    - Evidence: img42(설비 사진, uncertain), 수치·서술 4건
    - Relationship: 병렬 동등 항목
    - Required/Optional: 수치·서술=Required, img42=Optional(uncertain)
  - Claim ③(레거시 대비): 기존 소성로(Pusher Kiln)는 10시간 이상 소요되고 온도 정밀도가 낮으며 시설투자비용이 높다.
    - Evidence: img43(기존 소성로 설비 사진, confirmed), img44(가열소자 개념도 Figure5, confirmed), 서술 3건
    - Relationship: Before/After(기존 소성로 vs COSOLUS 유도가열, 위 Claim①의 "1분 이내" 대 "10시간 이상"이 사실상 대비쌍)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 12(가격경쟁력4+기술경쟁력4+레거시비교3+img41~44) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 1(img42) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary(상단, 60%): 가격경쟁력 / 기술경쟁력 — 대등한 Primary 2개(정확히 2개 정량 개선효과)
  - Dependent(상단): img41(가격경쟁력 종속), img42(기술경쟁력 종속)
  - Primary(하단, 40%): 기존 소성로(Pusher Kiln) 대비 비교 — 상단과 별도 역할의 Primary(레거시 비교)
  - Dependent(하단): img43, img44
  - Shared Supporting: N/A / Conclusion/Takeaway: 헤더박스("유도가열기술 → COSOLUS Originality")
- **Relationship**: 병렬(상단 2개 효과) + 비교(하단 레거시 대비) — 복합
- **Content Regions**: Header Region(Conclusion) / Upper Region(60%, Region A: 가격경쟁력+img41 / Region B: 기술경쟁력+img42, 좌우 병렬) / Lower Region(40%, 좌: 기존 Pusher Kiln 서술+img43, 우: img44 Figure5 중앙 배치)
- **Selected Layout**: Benefit + Impact Layout(상단) 구조를 기반으로, 하단 레거시 비교 Region을 추가 결합한 변형 (`docs/slide-design-rules/benefit-impact/benefit-impact.md` 기반 + 제작 지시문 CG19-PD01의 상하 60:40 구조 반영)
- **Layout Selection Reason**: 상단 60%는 Benefit+Impact Use When("정확히 2개의 좌/우 정량 개선효과", "서로 다른 Evidence로 동일 솔루션의 2개 효과 증명")과 정확히 부합. 다만 원본이 하단 40%에 레거시(Pusher Kiln) 비교를 추가로 요구하는데, 이는 Benefit+Impact 단독 구조(좌우 2분할, 상하 구조 없음)에 없는 요소이며 Before/After Layout의 Do Not Use("Before/After 공정단계 변화 자체가 핵심인 경우와 정량효과 2개 제시가 동시에 필요하면 억지로 합치지 않는다")에 해당하는 경계 사례다. design-rules.md 6번 원칙("적합한 Layout이 없을 때 기존 Layout의 조합·최소 변형 검토")에 따라 Benefit+Impact를 상단 Primary 구조로 채택하고, 하단은 별도 Comparison Region으로 최소 결합했다 — 두 Variant를 억지로 하나의 표준 Layout에 끼워맞추지 않고 조합 사실을 명시적으로 남긴다.
- **Structural Check**: **이슈 발견** — 이 슬라이드는 Benefit+Impact(상단)와 Before/After 성격 비교(하단)가 결합된 하이브리드 구조로, 특수 Layout Reference 인덱스의 어떤 단일 항목에도 완전히 부합하지 않는다. 원본 제작 지시문이 상하 60:40 구조를 명시적으로 요구하므로 슬라이드 자체를 분할하지 않고 이 조합 구조를 유지하기로 판단(design-rules.md 6번 절차 적용, 억지 끼워맞춤 아님 — 명시적 조합/변형으로 기록). web-ppt-generator 단계에서 이 조합이 실제로 Hard Rule·Design System과 충돌 없이 구현 가능한지 재확인 필요.

---

## Slide 19. 경쟁력 - [솔루션2] 친환경 차세대 배터리 재활용 공정기술 (3사 비교)

- **Source Material**: CG20(entire)
- **Core Message**: COSOLUS 유도가열(약 950℃, 1분 이내)은 BTR 전기로(3,000℃, 24시간)·Vianode 대류가열(3,000℃, 48시간) 대비 에너지 소비량이 낮고 연속 공정·직접 가열이 가능하다.
- **Core Claims & Evidence**:
  - Claim: 3사(COSOLUS/BTR/Vianode)의 기술/처리시간/특징 비교
    - Evidence: 표 전체(기업명/국가/기술/처리시간/특징)
    - Relationship: 복수 비교 근거(3사 x 4기준, 표 전체 값 유지)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 2(표 전체+제목) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Technology") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3사 비교표
  - Dependent: N/A / Shared Supporting: N/A / Conclusion/Takeaway: N/A
- **Relationship**: 비교
- **Content Regions**: Main Region(Primary, 표)
- **Selected Layout**: Table Comparison Layout (`docs/slide-design-rules/table-comparison.md`) + Competitive Advantage Highlight(`019_competitive-advantage-highlight.md`)
- **Layout Selection Reason**: Slide 10과 동일 근거 — Cell 지배 콘텐츠가 텍스트·수치이며 사진 없음(Table Comparison), 비교 대상 3개이므로 019로 COSOLUS 열 강조(제작 지시문 CG20-PD01 "Cosolus 우위 강조"와 정합).
- **Structural Check**: 문제 없음.

---

## Slide 20. 조직구성

- **Source Material**: CG21(entire)
- **Core Message**: CEO 김성현을 중심으로 CTO·CSO·COO 3인의 임원이 각자의 전문분야(유기합성/분자시뮬레이션/기술영업)와 산하 팀을 이끄는 조직 구조.
- **Core Claims & Evidence**:
  - Claim: CEO-CTO-CSO-COO 조직 구조와 각 임원의 전문분야·경력·산하 팀
    - Evidence: CEO/CTO/CSO/COO 각각의 전문분야·학력·경력·논문/특허(4건 병렬), 경영지원팀(2명, 별도 배치), 산하 팀 구성(개발1/2/3팀, AI혁신팀, 생산1팀, 각 인원수), img45~48(4인 프로필 사진, confirmed)
    - Relationship: 병렬 동등 항목(4명의 임원 프로필이 서로 비교가 아니라 각자 나열되는 항목) — 단, CEO→CTO/CSO/COO 연결 구조 자체는 원인(중심 리더)→결과(조직 확산)의 위계 관계
    - Required/Optional: Required(4명 프로필+조직구조 전체가 이 슬라이드의 유일한 핵심 콘텐츠)
- **Backward Completeness Check**: 명시반영 15(4명 프로필+경영지원팀+5개 산하팀+4장 사진+조직구조 지시) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("섹션: Company") / uncertain보류 0 / 미반영 0. 미반영 항목 없음. (NC-05: 임직원 총원27명과 팀별합계24명 차이는 material_analysis.json에 이미 기록)
- **Content Roles**:
  - Primary: CEO(중심) + CTO/CSO/COO(3개 하위 리더) — 대등한 3개 Primary가 CEO를 중심으로 확산되는 구조
  - Dependent: 각 임원 하위 팀(개발1/2/3팀은 CTO 산하, AI혁신팀은 CSO 산하, 생산1팀은 COO 산하), 프로필 사진
  - Shared Supporting: 경영지원팀(특정 임원에 종속되지 않고 상단 좌측 별도 배치 — 제작 지시문 CG21-PD01이 명시적으로 "하단 메인 곡선이나 다른 임원 정보에 포함하지 않는다"고 지정)
  - Conclusion/Takeaway: N/A
- **Relationship**: 전체-부분(CEO→3개 임원→각 산하팀) + 병렬(3개 임원 대등)
- **Content Regions**: Top-Center Region(CEO) / Top-Left Region(경영지원팀, Shared Supporting, 원형Node+짧은연결선) / 3개 하위 Region(CTO-개발1/2/3팀, CSO-AI혁신팀, COO-생산1팀) — CTO(좌)-CSO(중)-COO(우) 순
- **Selected Layout**: Organization Chart — Curved Leadership (`docs/slide-design-rules/020_organization.md`)
- **Layout Selection Reason**: Use When "핵심 경영진을 중심으로 조직이 확장되는 구조와 각 책임자의 전문분야를 함께 전달" 정확 부합, 제작 지시문(CG21-PD01)의 CEO 중심+CTO/CSO/COO 순서 배치와 정확히 일치.
- **Structural Check**: 문제 없음. 다만 이 Layout 문서 자체가 "Reference-Locked Layout"(첨부 레퍼런스의 좌표·연결방향을 Hard Rule로 적용)임을 명시하므로, web-ppt-generator 구현 시 해당 레퍼런스 좌표를 그대로 따라야 함을 전달.

---

## Slide 21. 투자포인트

- **Source Material**: CG22(entire)
- **Core Message**: 코솔러스는 기술력·사업화 방향과 함께 Series A2 투자라운드로 80억원 목표 투자유치를 진행 중이다.
- **Core Claims & Evidence**:
  - Claim ①(기술력 및 사업화): 추출제/친환경공정 기술력과 1.5세대(RECYION Series)·2세대(친환경 공정기술) 사업화 방향
    - Evidence: 기술력 3개 bullet(추출제 최상위 합성·정제기술/친환경공정기술/Closed-loop system) + 사업화방향 3개 bullet(XX하이텍·XX코 PoC진행중 / XX자동차 신공급망 / 일본·인도네시아 진출)
    - Relationship: 병렬 동등 항목
    - Required/Optional: Required
  - Claim ②(예상 소요자금): Series A2 라운드로 80억원 목표 투자유치, 국외법인 설립·공장건설·CAPA확대에 사용
    - Evidence: "Series A2", "목표 투자유치 금액=80억원", 투자금 사용계획 2개 bullet
    - Relationship: 단일 독립 근거(투자 규모) + 병렬 동등 항목(사용계획)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 10(기술력3+사업화3+투자라운드+금액+사용계획2) / Core Message반영 0 / 중복통합 0 / 라벨제외 2("섹션: Executive Summary","헤더박스1/2") / uncertain보류 0 / 미반영 0. 미반영 항목 없음. (NC-03: 'XX하이텍/XX코/XX자동차' 익명표기는 원본 자체 익명화로 material_analysis.json에 이미 기록)
- **Content Roles**:
  - Primary: 헤더박스1(기술력및사업화) / 헤더박스2(예상소요자금) — 대등한 Primary 2개
  - Dependent: 각 헤더박스 하위 bullet
  - Shared Supporting: N/A / Conclusion/Takeaway: N/A(Executive Summary 자체가 이미 종합 요약 성격)
- **Relationship**: 병렬
- **Content Regions**: Region A(좌 또는 상, 기술력및사업화) / Region B(우 또는 하, 예상소요자금)
- **Selected Layout**: L18 Two-Column Summary (`docs/layout-reference/2026.08.13_layout-catalog_V1.md` L18)
- **Layout Selection Reason**: 콘텐츠 자체가 "Executive Summary" 섹션 라벨을 명시하고 있고, 원본 구조도 헤더박스 2개(기술력/자금)의 병렬 요약 — L18 "Executive summary / overview / key takeaways" 용도가 정확히 부합. 특수 Layout Reference 인덱스에는 이 구조(2개의 서로 다른 성격 요약 박스, 비교·공정·효과 관계 아님)에 맞는 전용 항목이 없어 L01~L33으로 이관.
- **Structural Check**: 문제 없음. 좌우(또는 상하) 2개 Region은 Parallel Layout Alignment 원칙(동일 Top Line/Height)을 따름.

---

## Slide 22. 세계시장 진출

- **Source Material**: CG23(entire)
- **Core Message**: 코솔러스는 일본·인도네시아를 거점으로 5억명 이상 아시아 경제권에 진출하며, '26 파트너십 구축 → '27~28 PoC 획득 → '29~ 판매/서비스 제공의 마일스톤을 갖는다.
- **Core Claims & Evidence**:
  - Claim ①(목표): 일본·인도네시아를 전략적 거점으로 5억명 이상 아시아 경제권에서 성장한다.
    - Evidence: "5억 명 이상"(metric)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
  - Claim ②(마일스톤): '26 파트너십구축 → '27~28 PoC획득 → '29~ 판매/서비스제공
    - Evidence: 3개 시점 마일스톤 원문 전체
    - Relationship: 시간에 따른 변화·추세(3개 시점 순차 마일스톤, 전체 유지)
    - Required/Optional: Required
  - Claim ③(논의현황): 인도네시아 전기자전거업체 1대주주, 일본 현지투자사·재료업체와 투자논의 중
    - Evidence: 논의현황 서술 2건 + img49(SWAP, confirmed)/img50(Panasonic Energy, confirmed)/img51(Iwatani, confirmed)/img52(DNP, confirmed)
    - Relationship: 병렬 동등 항목(4개 파트너 로고)
    - Required/Optional: Required(다만 material_analysis.json NC-02에 따라 실명·로고 노출의 적정성은 사람 확인 필요 — 근거로서의 Required 여부와 실제 사용 승인 여부는 별개)
- **Backward Completeness Check**: 명시반영 9(목표+논의현황2+마일스톤3+파트너로고4) / Core Message반영 0 / 중복통합 0 / 라벨제외 2("섹션:Milestone","[목표]") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 마일스톤 타임라인('26/'27~28/'29~) — 단일 Primary(시간축이 정보의 핵심 구조)
  - Dependent: N/A
  - Shared Supporting: 목표 문구(5억명) + 논의현황(2건) + 파트너 로고 4개 — 타임라인 자체에 속하지 않고 타임라인 전체 맥락을 보완하는 공통 지원 정보
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차(시간축) + 병렬(파트너 로고)
- **Content Regions**: Top Region(Shared Supporting, 목표 문구) / Timeline Region(Primary, '26-'27~28-'29~ 3개 마일스톤) / Bottom Region(Shared Supporting, 논의현황 서술+4개 파트너 로고)
- **Selected Layout**: Timeline / Company Milestone Layout (`docs/slide-design-rules/timeline-company-milestone.md`)
- **Layout Selection Reason**: Use When "투자/사업 진행 단계 등 시간흐름에 따라 여러 Milestone, 연도/시점 기준 순차배치" 정확 부합('26/'27~28/'29~ 3개 시점).
- **Structural Check**: 문제 없음. 다만 목표·논의현황·파트너로고가 Primary(타임라인)보다 많은 면적을 차지하지 않도록 Shared Supporting Region으로서의 위계를 유지해야 함(6단계 점검 — Shared Supporting이 Primary Region을 압도하지 않는지 확인). 파트너 로고 4개의 실명 노출 적정성은 material_analysis.json NC-02에 따라 Human Review에서 최종 확인 필요.

---

## Slide 23. 마무리표지 (Thank You)

- **Source Material**: CG24(entire)
- **Core Message**: 코솔러스는 책임있는 화학기술로 순환경제를 선도하고 탄소배출 저감에 기여하며 지속가능한 미래를 만드는 글로벌 기업으로 도약한다는 클로징 메시지.
- **Core Claims & Evidence**:
  - Claim: 클로징 메시지("코솔러스는 책임있는 화학기술을 기반으로...") + "Thank You"
    - Evidence: 원문 전체 + img53(클로징 이미지, confirmed)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required(메시지), Optional(img53, 장식적 클로징 이미지)
- **Backward Completeness Check**: 명시반영 3(클로징문구+ThankYou+img53) / Core Message반영 0 / 중복통합 0 / 라벨제외 1("[마무리표지]") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 클로징 메시지 + Thank You
  - Dependent: img53(배경/보조 이미지)
  - Shared Supporting: N/A / Conclusion/Takeaway: N/A(이 슬라이드 자체가 전체 덱의 Conclusion 역할)
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region A(Primary, 클로징 메시지+Thank You+img53)
- **Selected Layout**: L22 Closing/Contact (`docs/layout-reference/2026.08.13_layout-catalog_V1.md` L22)
- **Layout Selection Reason**: Use When "Final message + contact information" — 클로징 메시지+Thank You 구조와 부합(연락처 정보는 원본에 없으므로 해당 부분은 비움). 특수 Layout Reference 인덱스에는 클로징 전용 항목이 없어 L01~L33에서 선택.
- **Structural Check**: 문제 없음.

---

## 전체 Coverage 요약

- 23개 슬라이드 전부 `slide_composition_map.json`의 Source Material을 1:1로 반영(CG11은 콘텐츠 없어 제외 — 이미 [3] 단계에서 확정).
- uncertain 근거(content_match_confidence: uncertain)가 배정된 슬라이드: 3, 4, 6, 14, 17, 18 — 전부 Required로 격상하지 않고 Optional로 유지함을 재확인.
- 재구성이 필요했던 미반영(6번 분류) 항목: 없음(모든 슬라이드에서 Backward Completeness Check 결과 "미반영 항목 없음"). Slide 4의 복구된 인용구(CG04-REC01)만 특수 사례로, 1-c 점검 시 정상적으로 Claim③의 Evidence에 편입됐는지 재확인 완료.
- 사람 확인이 필요한 항목(Human Review ① 대상으로 이관): Slide 4 인용구 사용 여부(NC-01), Slide 16 다이어그램 재구성 타당성, Slide 18 Layout 조합의 적절성, Slide 22 파트너 실명·로고 노출 적정성(NC-02), Slide 21/10의 원문 표기 오류·익명화 처리(NC-03, NC-04), Slide 20 임직원 수 불일치(NC-05).
