# slide_outline.md — cosolus-ir-deck-E

**세션 범위 안내**: 1~4단계(핵심 메시지~Content Region 설계)에 이어 5단계 Layout Routing까지 완료했다(2026-08-20, Human Review ① 승인 이후 baseline run). 각 슬라이드의 `Selected Layout`/`Layout Selection Reason`은 실제 채택된 Layout Reference와 판단 근거를 기록한다. `web-ppt-generator`([5])를 호출해 `web_ppt/v1/`에 HTML/CSS를 생성했다.

- **Source**: `material_analysis.json`, `slide_composition_map.json`
- **총 슬라이드 수**: 22 (원본 22개 Content Group과 1:1 대응 — `content-grouping` 결과 병합/분할 없음)

---

## Slide 1. 표지

- **Source Material**: CG01(entire)
- **Core Message**: 코솔러스 — 지속 가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술 기업
- **Core Claims & Evidence**:
  - Claim: 회사의 정체성과 제안가치를 한 문장으로 제시한다
    - Evidence: 표지 제목 "지속 가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술" (원문)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1 / Core Message반영 0 / 중복통합 0 / 라벨제외 0 / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 표지 제목 텍스트
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A (표지는 결론 없음)
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region A (Primary, 표지 타이틀 텍스트, Text)
- **Selected Layout**: 01_cover_design_V2.md (표지 전용)
- **Layout Selection Reason**: 표지 슬라이드 — Hard Rule에 따라 L01~L33 범용 카탈로그를 참고하지 않고 표지 전용 문서를 그대로 적용. Full Background Image + 좌상단 Brand Block + 중앙정렬 Main Title 구조.
- **Structural Check**: 문제 없음 — 단일 텍스트 요소만 존재해 밀도·병렬 불균형 이슈 해당 없음.

---

## Slide 2. 기업소개

- **Source Material**: CG02(entire)
- **Core Message**: 코솔러스는 27명 규모의 화학소재·친환경 공정 기술 기업으로, "폐배터리 순환경제 선도"라는 핵심가치와 비전을 가지고 있다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스의 핵심가치는 첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제를 선도하는 것이다
    - Evidence: 핵심가치 문구("첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제 선도"), 비전 문구("사용 후 배터리 핵심광물 회수를 위한 혁신 화학소재와 친환경 공정 기술을 통해, 인류의 지속가능한 미래를 선도하는 글로벌 리더로 도약") (원문)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
  - Claim: 코솔러스는 다지역 거점을 갖춘 27명 규모 조직이다
    - Evidence: 기업명(주식회사 코솔러스)/대표자(김성현)/임직원(27명)/소재지(전주·익산·완주·군산 4개 지역) — 나열된 개별 항목 전체 유지(일부만 대표로 축약하지 않음)
    - Relationship: 병렬 동등 항목(Parallel/Peer Items) — 기업명·대표자·임직원 수·소재지는 서로 다른 속성을 같은 기준으로 견주는 비교가 아니라, 하나의 상위 범주(회사 프로필) 아래 동등한 자격으로 나열되는 개별 사실
    - Required/Optional: Required
  - Claim: 실제 연구개발 현장에서 화학소재 실험이 이뤄지고 있다(시각적 신뢰도 보강)
    - Evidence: img1(글로브박스 앞 연구원 실험 사진, confirmed)
    - Relationship: 단일 독립 근거
    - Required/Optional: Optional (사진 없이도 회사소개 주장 자체는 성립)
- **Backward Completeness Check**: 명시반영 6(핵심가치/비전/기업명/대표자/임직원/소재지) / Core Message반영 0 / 중복통합 0 / 라벨제외 2(섹션명/제목) / uncertain보류 0 / 미반영 0. 미반영 항목 없음. (production_directives: 없음 — material_analysis.json CG02 참조)
- **Content Roles**:
  - Primary: 핵심가치 + 비전 서술
  - Dependent: 기업 프로필(기업명/대표자/임직원/소재지, 병렬 동등 항목), img1(연구현장 사진)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 종속 (프로필 정보·사진이 핵심가치/비전이라는 Primary 메시지를 구체적으로 뒷받침)
- **Content Regions**: Region A(Primary, 핵심가치+비전 텍스트) / Region B(Dependent, 기업 프로필: 기업명·대표자·임직원·소재지 — 병렬 동등 항목이므로 4개 필드를 동일 위계로 나란히 배치, 특정 항목을 대표값으로 강조하지 않음) / Region C(Dependent, img1 연구현장 사진)
- **Selected Layout**: Company Introduction (docs/slide-design-rules/02_instruction_design_V1.md)
- **Layout Selection Reason**: Use When 조건(기업명/대표자/임직원/소재지/비전 등 기본 정보를 외부 청중에게 빠르게 전달하는 회사소개)에 정확히 부합. 좌(정보 리스트)/우(세로 이미지) 2단 구조가 콘텐츠와 일치. 병렬 동등 항목(Parallel/Peer Items) 판단에 따라 4개 정보 필드를 동일 위계로 배치.
- **Structural Check**: 문제 없음 — Primary(2문장)와 Dependent(4개 프로필 필드+사진 1장)의 정보량 비율은 전형적 회사소개 슬라이드 구성으로 불균형 아님. Required Evidence 모두 Region에 반영됨. Relationship을 병렬 동등 항목으로 명확화했으나 Region 구성 자체는 이미 4개 필드를 대등하게 나열하는 구조였으므로 변경 없음.

---

## Slide 3. 문제제기-환경 및 지정학적 요인

- **Source Material**: CG03(entire)
- **Core Message**: 배터리 밸류체인은 환경오염, 핵심광물 고갈, 특정국가 편중 공급망이라는 3가지 환경·지정학적 문제에 직면해 있다.
- **Core Claims & Evidence**:
  - Claim: 배터리 밸류체인이 심각한 환경오염과 인권 문제를 유발한다
    - Evidence: "니켈 1톤당 133톤 폐기물 발생"(metric, Required), "채굴 산업의 노동 및 인권문제"(서술, Required), img2(채굴현장 아동노동 사진, confirmed, Optional), img3(해안 채굴오염 항공사진, confirmed, Optional), img4(폐배터리 더미 사진, confirmed, Optional), img5(채굴장 항공사진, confirmed, Optional)
    - Relationship: 기타 (수치·서술·사진 4장이라는 복수의 독립적 근거가 하나의 주장을 다각도로 뒷받침하는 구조 — 근거들 간 직접 비교·시계열 관계는 아님)
    - Required/Optional: 니켈133톤 수치·노동인권문제 서술은 Required, 사진 4장은 Optional
  - Claim: 광산채굴 기준 수요-공급 미스매치로 핵심광물이 고갈되고 있다
    - Evidence: "광산채굴 기준 수요-공급 미스매치 발생"(서술, 원문) + [글로벌 양극재(리튬) 수요-공급 전망] 테이블 — Data Pending(원본에 데이터 미제공, material_analysis.json CG03의 visual_placeholders[CG03-VP1] 참조. instructed_visual_type: table)
    - Relationship: 단일 독립 근거(서술뿐) + 관계형 표(Data Pending) — 유형 판단은 데이터 확보 후 확정
    - Required/Optional: Required이나 테이블 부분은 Data Pending(추정 금지, 원본 데이터 확보 필요 — escalation 유지)
  - Claim: 배터리 핵심광물 공급망이 중국에 편중되어 있다
    - Evidence: img6(중국 강조 아시아지도, confirmed), "전략광물 정제 평균 점유율 70%"(metric), "글로벌 블랙매스 처리 비중 89%"(metric)
    - Relationship: 구성요소별 기여도 (전체 공급망 중 중국이 차지하는 점유율 70%/89%)
    - Required/Optional: 3개 모두 Required
- **Backward Completeness Check**: 명시반영 8 / Core Message반영 0 / 중복통합 1("니켈 1톤당 133톤" 반복 언급을 Claim1과 통합) / 라벨제외 6(섹션/제목/박스1~3 라벨/하위내용) / uncertain보류 0 / 미반영 0. "(아래사진 삽입)"·"(테이블 삽입 예정)"·"(이미지삽입)" 3건은 production_directives(material_analysis.json CG03-PD01~03, 전부 visualization 유형)로 구조적으로 분리·보존됨 — 어느 박스의 어느 자리를 겨냥한 지시인지(target_scope)까지 남음. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3개 박스 주장(환경오염 / 핵심광물고갈 / 공급망편중) — 대등, 병렬 Main Content Group
  - Dependent: 각 박스에 종속된 수치·이미지(박스1: 니켈133톤+img2·3·4·5 / 박스2: 서술 + Data Pending 테이블 자리 / 박스3: 70%·89%+img6)
  - Shared Supporting: 그룹 각주(IEA/Benchmark Mineral Intelligence/Earthworks 출처) — 박스1·박스3에 공통 적용
  - Conclusion/Takeaway: N/A (원문에 별도 종합 결론 문장 없음, 3개 박스 자체가 "문제제기" 프레이밍의 결론격)
- **Relationship**: 병렬 (3개 독립 박스가 나란히 제시)
- **Content Regions**: Region A(Primary, 환경오염 박스: 서술+니켈133톤+img2/3/4/5) / Region B(Primary, 핵심광물고갈 박스: 서술 + 테이블 자리, Data Pending — 삭제·일반텍스트 대체 없이 instructed_visual_type=table에 맞는 자리를 그대로 예약) / Region C(Primary, 공급망편중 박스: 서술+70%/89%+img6) / Shared Supporting Region(그룹 각주·출처 표기, 하단 공통 배치)
- **Selected Layout**: Three-Column Insight Layout (docs/slide-design-rules/three-column/three-column.md)
- **Layout Selection Reason**: 동일 위계의 독립적 핵심 메시지 3개(환경오염/핵심광물고갈/공급망편중)가 병렬 제시되는 구조 — Use When 조건 정확히 부합, Do Not Use When(순차/시간흐름/단일항목 우세/2개 직접비교) 해당 없음. Data Pending 열(핵심광물고갈)도 동일 3분할 구조 안에서 자리만 예약.
- **Structural Check**: Region A(이미지 4장)가 Region C(이미지 1장+수치 2개) 대비 정보량이 뚜렷하게 많아 병렬 3-Region 간 불균형이 발견됨 — Region B는 Data Pending 테이블 자리 예약으로 명시적으로 재정의되어, 향후 원본 데이터가 채워지면 Region 구조를 다시 설계할 필요 없이 그 자리만 채우면 됨(콘텐츠 완성도 문제이지 Region 설계 문제가 아님, 별도 기록). Shared Supporting(각주)이 특정 Region에 잘못 귀속되지 않고 공통 영역으로 분리된 것을 확인.

---

## Slide 4. 왜 지금인가?-산업적 요인

- **Source Material**: CG04(entire)
- **Core Message**: 2030년 기점 전기차 폐배터리 발생 증가와 ESS 시장 고성장으로 시장이 개화하기 전, 지금 재료와 공정을 확보해야 한다.
- **Core Claims & Evidence**:
  - Claim: 2030년을 기점으로 전기차 폐배터리 발생량이 폭발적으로 증가한다
    - Evidence: [글로벌 전기차 폐배터리 발생 전망] 차트 — Data Pending(원본에 데이터 미제공, material_analysis.json CG04의 visual_placeholders[CG04-VP1] 참조. instructed_visual_type: chart). production_directives(CG04-PD01)를 통해 원문 표기가 "테이블 삽입 예정"이면서 바로 다음 줄은 "차트 제목:"으로 이어지는 표기 불일치도 그대로 노출됨(임의 정정하지 않음, applicability: ambiguous로 기록)
    - Relationship: 시간에 따른 변화·추세(의도된 유형이나 값 자체가 Data Pending)
    - Required/Optional: Required이나 Data Pending(추정 금지, escalation 유지)
  - Claim: 북미 ESS 시장이 고성장 국면으로 전환되고 있다
    - Evidence: [북미 ESS 시장 성장 전망] 차트 — Data Pending(material_analysis.json CG04의 visual_placeholders[CG04-VP2] 참조. instructed_visual_type: chart)
    - Relationship: 시간에 따른 변화·추세(의도된 유형이나 값 자체가 Data Pending)
    - Required/Optional: Required이나 Data Pending(추정 금지, escalation 유지)
  - Claim: 시장이 본격 개화하기 전에 재료·공정을 미리 확보해야 한다
    - Evidence: 박스3 서술("시장 개화 전 재료 및 공정 확보 필요", 원문), img7("5 YEARS" 스톡 그래픽, content_match_confidence: uncertain — 지시된 콘텐츠 유형은 "사진"이나 실제로는 스톡 아이콘이 삽입되었고 "5년"의 근거가 본문에 없음)
    - Relationship: 단일 독립 근거
    - Required/Optional: 서술은 Required, img7은 uncertain이므로 Optional 상한 적용(Required 승격 금지)
- **Backward Completeness Check**: 명시반영 3(박스1/2/3 제목 텍스트) / Core Message반영 0 / 중복통합 1("글로벌 전기차 폐배터리 발생 전망" 반복 표기) / 라벨제외 1(섹션) / uncertain보류 1(img7) / 미반영 0. "(테이블 삽입 예정)"·"(차트 삽입 예정)"·"(사진 삽입 예정)" 3건은 production_directives(material_analysis.json CG04-PD01~03, 전부 visualization)로 분리·보존됨. 미반영 항목 없음(다만 Claim1/2를 뒷받침할 실제 수치가 원본 자체에 없다는 점은 별도 escalation으로 이미 추적 중).
- **Content Roles**:
  - Primary: 3개 박스 주장(대등, 병렬)
  - Dependent: 각 박스 근거(현재는 Data Pending 자리이거나 img7)
  - Shared Supporting: 그룹 각주(SNE Research/Mirae Asset/KATECH, 박스1·박스2에 공통)
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합 (박스1·2가 시장 추세/원인을 제시하고 박스3이 그에 따른 결론적 행동을 제시하는 병렬+인과 혼합 구조)
- **Content Regions**: Region A(Primary, 전기차 폐배터리 전망 박스, Chart, Data Pending) / Region B(Primary, ESS시장 성장 박스, Chart, Data Pending) / Region C(Primary, 시장개화전 확보 필요 박스+img7[uncertain]) / Shared Supporting Region(그룹 각주)
- **Selected Layout**: Three-Column Insight Layout (docs/slide-design-rules/three-column/three-column.md)
- **Layout Selection Reason**: 3개 독립 산업 요인(2030년 폭발적 증가/ESS 고성장/재료·공정 확보 필요)이 대등하게 병렬 제시 — Slide 3과 동일 판단. Data Pending 2개 열도 동일 구조 안에서 자리 유지.
- **Structural Check**: Region A/B가 "근거 데이터 없음으로 인한 불균형"이 아니라 "Data Pending Chart 자리 예약"으로 명시적으로 재정의됨 — instructed_visual_type(chart)에 맞는 자리를 실제 데이터 없이도 Layout Routing 단계에서 감안해야 함(5단계 재개 시 참고). 원본 데이터가 채워지면 Region 구조 재설계 없이 값만 채우면 됨. Required Evidence는 애초에 원본에 존재하지 않아 1-b 단계에서 이미 Data Pending으로 처리했으므로 여기서 새로 발견된 유실은 아님.

---

## Slide 5. 비즈니스 모델

- **Source Material**: CG05(entire)
- **Core Message**: 코솔러스의 비즈니스 모델은 환경오염 저감, 도시광산 구축, 신공급망 구축이라는 3대 축으로 구성된다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스 비즈니스 모델은 3가지 축(환경오염저감/도시광산구축/신공급망구축)으로 이루어진다
    - Evidence: 박스1 "환경오염 저감 — 유해물질 억제 및 온실가스 감축으로 환경 오염 저감", 박스2 "도시광산 구축 — 폐자원으로부터 핵심 광물 확보로 배터리 원재료 수요부족 해결", 박스3 "新공급망 구축 — 제조→재활용→제조로 이어지는 재활용 기반 新공급망 구축" (원문)
    - Relationship: 구성요소별 기여도 (3개 축이 함께 하나의 비즈니스 모델을 구성)
    - Required/Optional: 3개 모두 Required (하나라도 빠지면 "3대 축" 주장이 성립하지 않음)
- **Backward Completeness Check**: 명시반영 3 / Core Message반영 0 / 중복통합 0 / 라벨제외 2(섹션/제목) + 제작지시 1("프롬프트: 3 BOX 구조로 만들고...") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3개 박스(대등, 병렬 Main Content Group)
  - Dependent: N/A (각 박스가 제목+짧은 설명으로 이미 완결)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C (대등 Primary 3개, 각 박스별 제목+설명, 각각 자체 완결형)
- **Selected Layout**: Three-Column Insight Layout (docs/slide-design-rules/three-column/three-column.md)
- **Layout Selection Reason**: production_directive(CG05-PD01: '3 BOX 구조로 만들고 아이콘 삽입')가 명시적으로 3분할 구조를 지시 — 이 구조별 특수 Layout Reference의 Use When과 정확히 일치하여 지시를 그대로 반영.
- **Structural Check**: 문제 없음 — 3개 박스 정보량(각 1문장씩) 균형.

---

## Slide 6. 재활용 공정 현황(1세대)

- **Source Material**: CG06(entire)
- **Core Message**: 1세대 배터리 재활용 공정(전처리→후처리)은 소재의 한계와 공정의 한계로 인해 경제성 확보에 실패했다.
- **Core Claims & Evidence**:
  - Claim: 1세대 공정은 전처리(폐배터리→블랙매스)와 후처리(양극재 재활용공정→MnSO4/CoSO4/NiSO4/Li2CO3+폐흑연)로 구성된다
    - Evidence: 공정 흐름 서술(원문) + img12(폐배터리 개념도)+img13(블랙매스)+img15(양극재재활용공정 설비)+img8(CoSO4)+img9(MnSO4)+img10(NiSO4)+img11(Li2CO3)+img14(폐흑연) — 총 8개 이미지
    - Relationship: 순차 공정/프로세스 (전처리→후처리 단계별 흐름)
    - Required/Optional: Required (공정 흐름 자체가 핵심 서사)
  - Claim: 1세대 공정은 소재 측면에서 구조적 한계가 있다
    - Evidence: "낮은 선택성", "제한된 동작 환경(pH 등)", "상분리 불안정", "부산물 과다발생(망초 등)" (원문 4개 항목)
    - Relationship: 구성요소별 기여도 (4개 한계 요인이 함께 "소재의 한계"를 구성)
    - Required/Optional: Required
  - Claim: 1세대 공정은 경제성 확보에 실패했다(실제 사례로 뒷받침)
    - Evidence: "1세대 재활용 공정 경제성 확보 실패"(서술) + img16(Li-Cycle 로고, 예시1) + img17(Glencore 로고, 예시2) — **출처 인용 없음, 실명 기업을 실패 사례로 제시하는 것의 사실관계·적절성 확인 필요(needs_confirmation NC-02)**
    - Relationship: 복수 비교 근거 (2개 실명 기업 사례를 나란히 제시)
    - Required/Optional: Required (단, 사실관계 미확인 상태임을 병기)
- **Backward Completeness Check**: 명시반영 3(공정흐름/소재의한계/공정의한계) / Core Message반영 0 / 중복통합 0 / 라벨제외 6(섹션/제목/박스제목/제작지시 2건/삽입사진list) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 전처리→후처리 공정 흐름 도식
  - Dependent: 소재의 한계 박스, 공정의 한계 박스(원문에 "그 아래쪽에 박스 들어감"으로 명시된 종속 배치)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A ("소재·공정 양면에서 한계가 있어 경제성을 확보하지 못했다"는 종합 문장은 원문에 명시적으로 존재하지 않아 창작하지 않음 — 두 Dependent 박스의 병치 자체로 암묵적 전달)
- **Relationship**: 기타·복합 (공정 흐름은 순차, 소재한계/공정한계 두 박스는 병렬)
- **Content Regions**: Region A(Primary, 전처리→후처리 공정 흐름 도식, 이미지 8장+흐름 화살표) / Region B(Dependent, 소재의 한계 박스, Region A 하단 좌측) / Region C(Dependent, 공정의 한계 박스+Li-Cycle/Glencore 로고, Region A 하단 우측, Region B와 병렬)
- **Selected Layout**: Process + Comparison Layout (docs/slide-design-rules/process-comparison/process-comparison.md)
- **Layout Selection Reason**: 순차 공정 흐름(전처리→후처리)을 먼저 보여준 뒤 그 흐름과 연결된 한계점(소재의 한계/공정의 한계)을 하단에서 함께 전달 — Use When 조건과 정확히 부합.
- **Structural Check**: Region A가 이미지 8장으로 밀도가 매우 높음 — 다만 원본이 명시적으로 "하나의 도식"으로 요구하는 구조이므로 슬라이드 분할보다 Region 내부 그리드 정렬로 해결할 문제로 판단(Layout Routing 영역, 이번 세션 범위 외). Region B/C(각 1박스)는 정보량 균형 양호. Required Evidence(8개 이미지) 전부 Region A에 반영 확인됨.

---

## Slide 7. [솔루션1] 코솔러스 추출제(1.5세대) 개요

- **Source Material**: CG07(entire)
- **Core Message**: 코솔러스는 1세대 추출제 구조를 개선한 1.5세대 추출제(RECYION)로 재활용 효율을 높인다.
- **Core Claims & Evidence**:
  - Claim: 1.5세대 코솔러스 추출제는 기존(1세대) 추출제 대비 재활용 효율이 개선되었다
    - Evidence: img18(기존 추출제 1세대 화학구조식, confirmed), "광산, 염호 기반 금속 회수용 추출제"(1세대 설명), img19(COSOLUS 1.5세대 추출제 화학구조식, **content_match_confidence: uncertain — img18과 픽셀 단위로 완전 동일한 이미지, needs_confirmation NC-03**), "재활용 효율 개선"(서술)
    - Relationship: Before/After (기존 1세대 구조 vs COSOLUS 1.5세대 구조 비교)
    - Required/Optional: "재활용 효율 개선" 서술과 img18(기존 구조식)은 Required. **img19(COSOLUS 신규 구조식)는 uncertain이므로 Optional 상한 적용 — 이 슬라이드의 핵심 시각적 차별화 근거임에도 현재 Evidence가 불확실함을 명시**
- **Backward Completeness Check**: 명시반영 4(기존추출제 제목/설명, COSOLUS추출제 제목/설명) / Core Message반영 0 / 중복통합 0 / 라벨제외 4(섹션/제목/제작지시 2건/삽입이미지 라벨 2건) / uncertain보류 1(img19) / 미반영 0. 미반영 항목 없음. 단, "이전페이지에서 보여주었던 [전처리]->[후처리] 도식 그대로 삽입해줘"라는 제작 지시는 CG06(슬라이드6)의 공정 도식을 참조하라는 지시일 뿐 이 페이지 자체의 별도 콘텐츠 데이터가 아니므로 별도 Claim으로 세우지 않음(라벨/제작지시로 분류).
- **Content Roles**:
  - Primary: 기존 추출제(1세대) 블록, COSOLUS 1.5세대 추출제 블록 — 대등한 Before/After 2개 Primary
  - Dependent: 각 블록의 화학구조식 이미지(img18, img19)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교 (Before-After)
- **Content Regions**: Region A(Primary, 기존 추출제 1세대: 제목+설명+img18) / Region B(Primary, COSOLUS 1.5세대 추출제: 제목+설명+img19[uncertain]) — 좌우 병렬 대응 배치
- **Selected Layout**: Before + After Layout, Variant A — Process Transformation (docs/slide-design-rules/before-after/before-after.md)
- **Layout Selection Reason**: 기존(1세대)/코솔러스(1.5세대) 추출제 구조식 2개를 좌→우 화살표로 비교 — '어떤 구조가 바뀌는가'가 핵심이라 Variant A(Diagram+Arrow) 적용. 비교 대상 정확히 2개, Comparison Matrix 대상(3개 이상)에 해당하지 않음.
- **Structural Check**: Region A/B는 대칭 구조(제목+설명+이미지)로 정보량 균형은 맞으나, **Region B의 핵심 근거 이미지(img19)가 uncertain 상태라는 점이 이 슬라이드의 가장 중요한 구조적 리스크** — 이 슬라이드의 존재 이유인 "구조 차별화"를 시각적으로 뒷받침할 Required급 근거가 사실상 부재함을 명시하고, [5] 단계 이전에 실제 COSOLUS 1.5세대 구조식 확보가 필요함을 재확인.

---

## Slide 8. 핵심기술-[솔루션1-1] 고성능 추출제: 경쟁사 대비 공정시간·첨가제 사용량

- **Source Material**: CG08(entire)
- **Core Message**: COSOLUS 고성능 추출제는 벨기에 S사·중국 K사 대비 첨가제 사용량이 적고 공정시간이 짧다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS는 경쟁사(벨기에 S사·중국 K사) 대비 첨가제 사용량이 적다
    - Evidence: 표 "첨가제 사용량*" 행 — COSOLUS "-", 벨기에 S사 "COSOLUS 대비 10% 이상 추가 첨가제 필요", 중국 K사 "COSOLUS 대비 5% 이상 추가 첨가제 필요"(*블랙메스 1톤당, 각주)
    - Relationship: 복수 비교 근거 (3사 비교)
    - Required/Optional: Required
  - Claim: COSOLUS는 경쟁사 대비 공정시간이 짧다(시각적 근거)
    - Evidence: img20/21(COSOLUS 반응 전/후 비커사진, confirmed), img22/23(벨기에 S사 전/후, **uncertain — img20/21과 픽셀 단위 완전 동일**), img24(중국 K사 전, **uncertain — img20/22와 동일**)/img25(중국 K사 후, confirmed — 상대적으로 덜 진행된 상분리를 보여 경쟁열위와 대체로 부합)
    - Relationship: Before/After(반응 전→후) × 복수 비교 근거(3사)
    - Required/Optional: Required이나 **벨기에 S사 열 전체와 중국 K사 열의 '전' 사진이 uncertain** — 근거의 상당 부분이 재사용된 동일 이미지임을 구조 체크에 명시
- **Backward Completeness Check**: 명시반영 2(표 데이터) / Core Message반영 1(핵심배너) / 중복통합 0 / 라벨제외 5(섹션/제목/제작지시 2건/회사명 라벨 3건) / uncertain보류 0(이미지는 Claim 안에 그대로 포함하되 uncertain 표시 유지) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 첨가제 사용량 비교표, 공정시간 비교 비커사진 — 대등한 두 근거축(정량 표 vs 시각적 비교)으로 병렬 Main Content Group
  - Dependent: 각주(*블랙메스 1톤당, 표에 종속)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 핵심배너("COSOLUS 화학구조 설계 및 정제 기술 → 공정시간 단축 및 첨가제 사용량 저감")가 두 근거(표+사진)를 종합하는 결론 성격 — 상단 배치
- **Relationship**: 비교 (경쟁사 3사) — 표는 순수 비교, 사진은 Before-After가 섞인 기타·복합
- **Content Regions**: Region A(Conclusion, 핵심배너 텍스트, 상단) / Region B(Primary, 첨가제 사용량 비교 표) / Region C(Primary, 공정시간 비교 비커사진 6장, 3사×전/후) — B/C 병렬 배치
- **Selected Layout**: Comparison Matrix Layout (docs/slide-design-rules/comparison-matrix/comparison-matrix.md)
- **Layout Selection Reason**: 3개 대상(COSOLUS/벨기에 S사/중국 K사)을 동일 기준(첨가제 사용량 표 + 반응 전/후 비커사진)으로 비교하되 각 대상마다 이미지를 자유롭게 배치해야 해 Table Comparison(직각형 Grid 강제)보다 이 Layout이 적합.
- **Structural Check**: Region C(이미지 6장)가 Region B(표 1개)보다 시각적 비중이 커질 가능성 있어 병렬 Region 간 비중 점검이 필요함을 기록. Required Evidence 반영: Claim2(공정시간)의 이미지 근거 다수가 uncertain 상태이므로, 이 근거를 그대로 Required로 노출할지는 [5] 단계에서 재검토가 필요함을 명시(이번 세션은 판단만 기록, 재구성하지 않음).

---

## Slide 9. 핵심기술-[솔루션1-1] 고성능 추출제: 추출단수·망초 저감 효과

- **Source Material**: CG09(entire)
- **Core Message**: COSOLUS 추출제 도입 시 추출단수가 1단 줄어(CAPEX 개선) 망초 발생이 5% 이상 저감된다(OPEX 개선).
- **Core Claims & Evidence**:
  - Claim: COSOLUS 추출제는 기존 추출제 대비 이론단수가 1단 적어(4단 vs 5단, 20% 감소) CAPEX 경제성을 확보한다
    - Evidence: "COSOLUS 추출제 이론단수: 4단(20% 감소)", "기존 추출제 이론단수: 5단"
    - Relationship: Before/After (기존 5단 → COSOLUS 4단)
    - Required/Optional: Required
  - Claim: 추출단수 저감으로 망초 발생이 5% 초과 저감되어 OPEX 경제성을 확보한다(가정 시나리오 기준)
    - Evidence: "대한민국 배터리 재활용 업체 1년간 니켈 16,000톤 생산 가정 시 COSOLUS 추출제로 4,800톤 망초 저감 가능" — **이 수치는 특정 실존 업체의 실측치가 아니라 원문 자체가 익명 가정 주체("대한민국 배터리 재활용 업체")를 전제로 한 시나리오 산출값임을 명시**
    - Relationship: 원인→결과 (추출단수 저감 → 망초 저감, 특정 생산량 가정 하의 결과값)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 4(이론단수 2건, 니켈생산량, 망초저감량) / Core Message반영 1(핵심배너) / 중복통합 0 / 라벨제외 4(섹션/제목/제작지시/제목1·2 라벨) / uncertain보류 0 / 미반영 0. "(표삽입 예정)"으로 예고된 세부 검증용 표는 원본에 실제로 삽입되지 않았으나, 이 표가 뒷받침하려던 핵심 수치(이론단수 4단/5단, 니켈 16,000톤, 망초 4,800톤)는 이미 본문 텍스트에 명시되어 있어 Claim1/2에 그대로 반영됨 — 미반영 항목 없음(세부 표 자체의 부재는 material_analysis.json NC-06으로 별도 추적).
- **Content Roles**:
  - Primary: CAPEX(이론단수 개선), OPEX(망초저감) — 대등한 2개 Primary(병렬)
  - Dependent: N/A (각 Claim이 이미 완결)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 핵심배너("COSOLUS 화학구조 설계 및 정제 기술 → 공정 단수 감소, 망초 발생 저감")가 두 Claim을 요약
- **Relationship**: 기타·복합 (CAPEX/OPEX 두 관점의 병렬 + 단수감소→망초저감의 인과 연결)
- **Content Regions**: Region A(Conclusion, 핵심배너, 상단) / Region B(Primary, CAPEX-이론단수 Before-After) / Region C(Primary, OPEX-망초 저감량, 가정 시나리오 수치) — B/C 병렬
- **Selected Layout**: Benefit + Impact Layout (docs/slide-design-rules/benefit-impact/benefit-impact.md)
- **Layout Selection Reason**: 하나의 기술(COSOLUS 화학구조 설계·정제 기술)이 만드는 정확히 2개의 좌/우 정량 개선효과(CAPEX-추출단수저감/OPEX-망초저감)를 Core Technology→Improvement→Quantified Impact 흐름으로 병렬 제시 — Use When 조건과 정확히 부합.
- **Structural Check**: Region B/C 정보량 균형 양호(각 1~2개 핵심수치). Required Evidence 반영 확인됨. 세부 검증 표의 부재(NC-06)로 두 수치가 표 형태로 시각적 재확인되지 않는 한계는 그대로 유지.

---

## Slide 10. 경쟁력-[솔루션1-1] 고성능 추출제 (KopperChem/Solvay 비교)

- **Source Material**: CG10(entire)
- **Core Message**: COSOLUS는 KopperChem(중국)·Solvay(벨기에) 대비 공정시간·첨가제사용량·탄소중립에서 우위를 갖는다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS는 5개 평가항목(가격/추출성능/공정시간/첨가제사용량/탄소중립) 중 공정시간·첨가제사용량·탄소중립에서 경쟁사 대비 우위를 보인다
    - Evidence: 비교표 전체(구분/COSOLUS/KopperChem/Solvay, 5개 행) — 단, **"가격"·"추출성능" 두 항목은 3사 모두 동일(◎)하여 실질적 차별화 근거가 되지 못함(needs_confirmation NC-07)**, "국가" 행 레이블에 실제로는 제품군명(RECYION/Mextral/CYANEX)이 들어있는 레이블-데이터 불일치도 존재(NC-07)
    - Relationship: 복수 비교 근거 (3사 × 5항목 매트릭스)
    - Required/Optional: Required (단, 가격·추출성능 두 항목은 근거로서 신뢰도가 낮음을 병기)
- **Backward Completeness Check**: 명시반영 1(표 전체) / Core Message반영 0 / 중복통합 0 / 라벨제외 4(We promise tomorrow/Technology/제목/평가기준) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 비교표 전체(단일 압축형 Visual)
  - Dependent: 평가기준 범례(◉ 매우좋음/○ 좋음/△ 보통)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A (표 자체가 결론을 담고 있음, 별도 종합 문장 없음)
- **Relationship**: 비교
- **Content Regions**: Region A(Primary, 5행×4열 비교표) / Region B(Dependent, 범례, 표 인접 배치)
- **Selected Layout**: Table Comparison Layout (docs/slide-design-rules/table-comparison.md) + Competitive Advantage Highlight (docs/slide-design-rules/019_competitive-advantage-highlight.md)
- **Layout Selection Reason**: 5개 평가항목×3사를 동일 기준 행으로 촘촘히 비교하는 수치·기호 중심 표 — Table Comparison Use When 부합. 비교 대상 3개(≤4)이며 자사 우위 전달이 필요해 019 자사 열 카드 강조 패턴을 함께 적용.
- **Structural Check**: 단일 Region 구조로 밀도 이슈 없음. Required Evidence(표 전체) 반영 확인됨. "가격/추출성능 무차별 평가" 및 "국가 행 레이블 불일치" 이슈는 Region 설계 문제가 아니라 원본 데이터 자체의 특성이므로 참고사항으로만 기록.

---

## Slide 11. [솔루션1-2] DLE 기술 동향

- **Source Material**: CG11(entire)
- **Core Message**: 리튬 직접추출(DLE) 기술은 흡착제/추출제/분리막/전기화학 4가지 방식으로 나뉘며 기술성숙도(TRL)와 장단점이 각기 다르다.
- **Core Claims & Evidence**:
  - Claim: 4가지 DLE 기술 방식은 작동원리·기술성숙도·장단점에서 뚜렷한 차이를 보인다
    - Evidence: 4열 비교표 전체(작동원리/TRL/장점/단점 × 흡착제/추출제/분리막/전기화학), 출처(Desalination, 2024, 575, 117249)
    - Relationship: 복수 비교 근거 (4개 기술 방식 비교)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1(표 전체+출처) / Core Message반영 0 / 중복통합 0 / 라벨제외 2(섹션/제목) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 비교표(단일)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교
- **Content Regions**: Region A(Primary, 4행×4열 비교표)
- **Selected Layout**: Table Comparison Layout (docs/slide-design-rules/table-comparison.md)
- **Layout Selection Reason**: 4개 DLE 기술 방식을 작동원리/TRL/장점/단점 동일 기준으로 나열 비교 — 자사 강조 대상이 아닌 순수 기술 동향 비교라 019 강조 패턴은 적용하지 않음.
- **Structural Check**: 단일 Region, 문제 없음.

---

## Slide 12. 핵심기술-[솔루션1-2] Key Advantages of Extractant-Separator for DLE

- **Source Material**: CG12(entire, 하위 subtopic CG12-ST01/ST02/ST03 포함)
- **Core Message**: 추출제-분리막 결합 방식은 4가지 구조적 장점을 바탕으로 흡착제·전기화학 방식 대비 재활용효율 등 6개 지표에서 종합적으로 우수하다.
- **Core Claims & Evidence**:
  - Claim: 추출제-분리막 결합 방식은 4가지 구조적 장점을 갖는다
    - Evidence: "①추출제-Li⁺ 액-액 접촉을 통한 빠른 물질전달", "②화학적 결합+공간적 분리를 통한 우수한 재활용 효율", "③액상 공정을 통한 용이한 연속 운전", "④분리막 기반 농축을 통한 첨가제 소모량 감소" (원문 4개)
    - Relationship: 구성요소별 기여도 (4개 장점이 함께 결합방식의 우수성을 구성)
    - Required/Optional: Required
  - Claim: 추출제&분리막 방식은 흡착제·전기화학 방식 대비 6개 지표(재활용효율/공정시간/연속공정/에너지효율/양산성/친환경성) 전반에서 우위를 보인다
    - Evidence: 3개 방사형 차트 데이터 — 흡착제(4.0/3.0/4.0/3.0/4.0/3.0), 전기화학(4.0/3.0/2.0/1.0/2.0/5.0), 추출제&분리막(5.0/4.0/5.0/4.0/4.0/4.0), img26(페이지 원본 렌더링 스크린샷으로 3개 차트 실제 형태 확인) — **출처 인용 없이 제시된 수치로, 코솔러스 자체 평가치로 추정됨(needs_confirmation NC-08)**
    - Relationship: 복수 비교 근거 (3개 계열 × 6개 지표)
    - Required/Optional: Required (단, 자체평가 가능성을 병기)
- **Backward Completeness Check**: 명시반영 5(①~④, 3개 subtopic 데이터 전체) / Core Message반영 0 / 중복통합 0 / 라벨제외 3(섹션/제목/제작지시 "방사형차트생성") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 3개 방사형 차트(대등, 병렬 Main Content Group)
  - Dependent: 각 차트의 계열명 라벨(흡착제/전기화학/추출제&분리막)
  - Shared Supporting: 4가지 장점 서술(①~④) — 특정 차트 하나가 아니라 3개 차트 전체, 특히 추출제&분리막의 우위를 설명하는 공통 배경 근거이므로 Shared Supporting으로 분류
  - Conclusion/Takeaway: N/A ("추출제&분리막 방식이 종합적으로 가장 우수하다"는 결론은 데이터상 자명하게 드러나나 원문에 명시적 결론 문장은 없어 창작하지 않음)
- **Relationship**: 기타·복합 (3개 계열 비교 + ①~④ 서술과의 종속 관계)
- **Content Regions**: Region A(Shared Supporting, ①~④ 4대 장점 서술, 상단 또는 좌측 공통 배치) / Region B·C·D(Primary, 방사형 차트 3개, 병렬)
- **Selected Layout**: Multi-Radar Technology Comparison (docs/slide-design-rules/013_multi-radar-technology-comparison.md)
- **Layout Selection Reason**: 동일한 6개 평가축(재활용효율/공정시간/연속공정/에너지효율/양산성/친환경성)으로 3개 기술 방식을 비교하며 실제 정량 데이터(1~5점)가 존재 — Use When 조건과 정확히 부합. production_directive(CG12: '방사형 차트 생성')와도 일치.
- **Structural Check**: Region B/C/D(3개 차트) 정보량 균형 양호(각 6개 지표로 동일). Shared Supporting(①~④)이 특정 차트에 귀속되지 않고 공통 영역에 배치되었는지 확인됨. Required Evidence(4장점+18개 수치) 모두 Region에 반영 확인.

---

## Slide 13. 핵심기술-[솔루션1-2] COSOLUS DLE 정량 성과

- **Source Material**: CG13(entire)
- **Core Message**: COSOLUS DLE 기술은 핵심소재와 분리막&THz 기술을 통해 재자원화율을 90% 이상, 공정비용을 5,500원/kg 미만으로 달성한다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 핵심소재 기술은 재자원화율을 3%에서 50%로 끌어올린다
    - Evidence: "재자원화율 3% → 50%" (원문, 출처: KOMIS/Green Chem. 2026)
    - Relationship: Before/After
    - Required/Optional: Required
  - Claim: 분리막&THz 기술은 리튬 재자원화율을 3%에서 90%로 끌어올린다
    - Evidence: "리튬 재자원화율 3% → 90%" (원문, 동일 출처)
    - Relationship: Before/After
    - Required/Optional: Required
  - Claim: 두 기술의 결합으로 전체 재자원화율 90% 초과, 공정비용 5,500원/kg 미만을 달성한다
    - Evidence: 핵심배너 "재자원화율(>90%*), 공정비용(<5,500원/kg)" — **"*" 각주가 구체적으로 무엇을 조건화하는지 별도 설명 텍스트가 원본에서 확인되지 않음(needs_confirmation NC-09)**
    - Relationship: 구성요소별 기여도 (두 하위기술이 종합 성과를 구성)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 3(핵심배너, 제목1+수치, 제목2+수치) / Core Message반영 0 / 중복통합 0 / 라벨제외 3(섹션/제목/각주 표기) / uncertain보류 0 / 미반영 0. "핵심소재 표삽입예정"·"분리막&THz 도표삽입예정"으로 예고된 세부 표/도표는 원본에 실제로 삽입되지 않았으나 헤드라인 수치(3%→50%, 3%→90%)는 Claim1/2에 이미 반영되어 있음 — 미반영 항목 없음(세부 표/도표 부재는 NC-10으로 별도 추적).
- **Content Roles**:
  - Primary: 핵심배너(종합 성과) — 이 슬라이드의 핵심 메시지
  - Dependent: 핵심소재(3%→50%), 분리막&THz(3%→90%) — 핵심배너 수치를 구성하는 2개 하위요소
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 핵심배너 자체가 Primary 겸 결론 역할을 겸함 — 별도 Conclusion Region 불필요
- **Relationship**: 전체-부분 (핵심배너가 전체, 핵심소재/분리막&THz가 부분) + 종속
- **Content Regions**: Region A(Primary, 핵심배너: 재자원화율>90%, 공정비용<5,500원/kg) / Region B(Dependent, 핵심소재 3%→50%) / Region C(Dependent, 분리막&THz 3%→90%) — B/C가 A를 뒷받침하는 병렬 하위 Region
- **Selected Layout**: Benefit + Impact Layout — 핵심배너 우선 변형 (docs/slide-design-rules/benefit-impact/benefit-impact.md)
- **Layout Selection Reason**: 핵심배너(재자원화율>90%·공정비용<5,500원/kg) 아래 2개 하위기술(핵심소재/분리막&THz)의 정량 변화(3%→50%, 3%→90%)가 병렬 제시되는 구조적으로 동일한 배너+2컬럼 패턴 — Slide 9와 동일 Layout을 배너 우선 순서로 재사용.
- **Structural Check**: Region B/C 정보량 균형 양호(각 1개 Before-After 수치, 세부표는 원본 부재로 양쪽 다 없음 — 균형 자체는 유지됨). Required Evidence 반영 확인됨. 세부표 부재는 NC-10으로 별도 추적.

---

## Slide 14. [솔루션2] 개요-친환경 차세대 배터리 재활용 공정기술(2세대)

- **Source Material**: CG14(entire)
- **Core Message**: 코솔러스의 2세대 친환경 차세대 배터리 재활용 공정기술은 블랙매스를 부유선별한 뒤 건식환원·유도가열을 통해 양극재·흑연을 회수하는 통합 공정이다.
- **Core Claims & Evidence**:
  - Claim: 2세대 공정은 블랙매스 → 부유선별 → (양극재용/음극재용 블랙매스) → 건식환원/유도가열 → 재활용양극재(MnSO4/NiSO4/CoSO4/Li2CO3)+폐흑연/고순도정제흑연으로 이어지는 순차 공정이다
    - Evidence: img27(페이지 원본 렌더링 스크린샷, 공정 흐름도 전체 확인 가능) — **도식 안에 빨간색 박스 1개·짙은 청록색 박스 1개가 내용 없이 비어 있음(needs_confirmation NC-11, 원본 자체의 미완성 상태)**
    - Relationship: 순차 공정/프로세스
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1(공정 흐름도, img27) / Core Message반영 0 / 중복통합 0 / 라벨제외 3(슬라이드15 미리보기/섹션·제목/제작지시 "큰 도식 삽입 예정") / uncertain보류 0 / 미반영 0. 원본 도식 안의 빈 박스 2개는 "정보량 없는 미완성 placeholder"로 판단해 별도 Claim으로 재구성하지 않되, 원본 자체의 미완성 상태임을 주석으로 남김. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 전체 공정 흐름도(img27 기반)
  - Dependent: N/A (단일 도식이 이미 완결)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차 / 단일 콘텐츠
- **Content Regions**: Region A(Primary, 전체 공정 흐름도 — 배터리→전처리→블랙매스→부유선별→양극재용/음극재용 분기→건식환원/유도가열→산출물)
- **Selected Layout**: Process / System Architecture Layout A (docs/slide-design-rules/process-system-architecture-layout.md)
- **Layout Selection Reason**: 배터리→전처리→블랙매스→부유선별→(양극재용/음극재용 분기)→(건식환원/유도가열)→산출물의 좌→우 선형+분기 흐름 — 단계별 실사진 Evidence가 없어 Layout A(아이콘/텍스트 컴포넌트) 적용. 원본 스크린샷(img27)은 재구성 근거로만 사용, 시각 디자인은 그대로 복제하지 않음.
- **Structural Check**: 단일 대형 Region, 밀도는 원본 이미지 구조를 따름. 원본의 빈 박스 2개(캡션 "경제성/친환경성/양산성 확보"만 존재)는 이번 세션 범위에서 임의로 보완하지 않고 미완성 상태 그대로 인지.

---

## Slide 15. 핵심기술-[솔루션2] 친환경 차세대 배터리 재활용 공정기술(2세대) 개요도

- **Source Material**: CG15(entire)
- **Core Message**: COSOLUS 고유 기술(부유선별/건식환원/유도가열)을 적용한 2세대 공정은 블랙매스로부터 코발트·니켈과 고순도 정제흑연을 회수한다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 부유선별 → (건식환원 → 코발트/니켈 회수) / (유도가열 → 고순도 정제흑연 회수)의 2갈래 공정으로 블랙매스에서 유가금속과 흑연을 각각 회수한다
    - Evidence: img28(페이지 원본 렌더링 스크린샷, COSOLUS 고유 라벨 포함 공정도), 도식 내 텍스트 라벨 전체(COSOLUS/건식환원/부유선별/니켈/코발트/전처리공정/양극재용블랙매스/유도가열/블랙매스/음극재용블랙매스/고순도정제흑연)
    - Relationship: 순차 공정/프로세스 (갈래 분기 포함이므로 단계별 변화도 겸함)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 11(도식 내 라벨 전체) / Core Message반영 0 / 중복통합 0 / 라벨제외 3(슬라이드16 미리보기/섹션·제목) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 공정도(img28)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차
- **Content Regions**: Region A(Primary, COSOLUS 2세대 공정도)
- **Selected Layout**: Process / System Architecture Layout A (docs/slide-design-rules/process-system-architecture-layout.md)
- **Layout Selection Reason**: Slide 14와 동일한 분기형 순차 흐름이나 COSOLUS 고유기술 라벨(부유선별/건식환원/유도가열)이 부착된 상세판 — 동일 Layout 계열 유지가 원칙이라 Layout A를 재사용.
- **Structural Check**: 단일 Region, 문제 없음. CG14(슬라이드14)와 도식이 유사하나 CG14는 "개요"(범용 공정 흐름, 빈 박스 존재), CG15는 "핵심기술"(COSOLUS 고유기술 라벨이 부착된 상세 버전)로 정보 위계가 다름을 재확인 — 중복 콘텐츠가 아님.

---

## Slide 16. 핵심기술-[솔루션2] 건식환원공정(COSOLUS Originality)

- **Source Material**: CG16(entire)
- **Core Message**: COSOLUS 건식환원 공정은 양극재용 블랙매스로부터 순도 95% 초과의 코발트를 회수하며, 관련 특허를 2건 출원했다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 건식환원 공정을 통해 양극재용 블랙매스에서 순도 95% 초과의 코발트(또는 니켈)를 회수한다
    - Evidence: "Co 회수 순도 >95%"(metric), "PCT 2건 출원"(metric), img29(건식환원 반응기 일러스트), img30(양극재용 블랙매스 사진), img31(금속펠릿/Co 결과물 사진)
    - Relationship: 순차 공정/프로세스 (블랙매스→건식환원→Co회수) + 단일 독립 근거(순도 수치)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 3(순도>95%, PCT2건, 공정서술) / Core Message반영 0 / 중복통합 0 / 라벨제외 2(섹션/제목) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 건식환원 공정 흐름(블랙매스→반응→Co회수)
  - Dependent: 순도>95%·PCT2건 수치(공정 결과에 종속)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차
- **Content Regions**: Region A(Primary, 공정 흐름: img30 블랙매스→img29 반응기→img31 Co 결과물) / Region B(Dependent, 순도>95%·PCT2건 수치, Region A에 인접 배치)
- **Selected Layout**: Process / System Architecture Layout B (docs/slide-design-rules/process-system-architecture-layout.md)
- **Layout Selection Reason**: 블랙매스→반응→Co회수의 단계별 실사진(img29/30/31)이 모두 confirmed 상태로 존재 — Use When의 'Layout B(이미지 있음)' 조건에 부합.
- **Structural Check**: 단일 순차 흐름, 정보량 적정. Required Evidence 반영 확인됨.

---

## Slide 17. 핵심기술-[솔루션2] 유도가열기술(COSOLUS Originality)

- **Source Material**: CG17(entire)
- **Core Message**: COSOLUS 유도가열 기술은 기존 소성로 대비 압도적으로 짧은 공정시간과 적은 에너지 투입으로 고순도 재생흑연을 생산한다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 유도가열은 가격경쟁력이 있다
    - Evidence: "짧은 공정 시간(1분 이내, 200배 빠른 승온속도)", "적은 에너지 투입(432 Wh/kg, 64% 에너지 절감)" — **출처 인용 없음(needs_confirmation NC-12)**
    - Relationship: 복수 비교 근거 (자사 vs 기존공정 비교치, 배수/절감율로 표현)
    - Required/Optional: Required (단, 출처 미확인 상태 병기)
  - Claim: COSOLUS 유도가열은 기술경쟁력이 있다
    - Evidence: "고순도 재생흑연(순도 99% 이상)", "균일한 온도 분포 구현", "낮은 부반응 발생", "PCT 2건 출원" — 출처 인용 없음(NC-12)
    - Relationship: 구성요소별 기여도
    - Required/Optional: Required (단, 출처 미확인 상태 병기)
  - Claim: 기존 소성로(Pusher Kiln)는 10시간 이상 소요되고 온도 정밀도가 낮으며 시설투자비용이 높다
    - Evidence: "10시간 이상 장시간 소요", "낮은 온도 정밀도", "높은 시설 투자비용" (비교 대조군)
    - Relationship: 복수 비교 근거 (COSOLUS 대비 기존 소성로의 열위 — Claim1의 "1분이내/200배" 등 비교 수치의 기준점)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 7([가격경쟁력]/[기술경쟁력] 각 항목, ※기존소성로 3항목) / Core Message반영 0 / 중복통합 0 / 라벨제외 4(섹션/제목/제작지시/박스1 라벨/삽입이미지list) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: [가격경쟁력] 박스, [기술경쟁력] 박스 — 대등, COSOLUS 자사 강점 병렬
  - Dependent: 관련 공정사진(img32~35)
  - Shared Supporting: ※기존소성로 비교 박스(img36 포함) — 특정 Primary 하나가 아니라 [가격경쟁력]·[기술경쟁력] 둘 모두의 비교 기준점 역할
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합 (COSOLUS vs 기존소성로의 비교 + 가격경쟁력/기술경쟁력 두 박스의 병렬)
- **Content Regions**: Region A(Primary, 가격경쟁력 박스) / Region B(Primary, 기술경쟁력 박스) / Region C(Shared Supporting, 기존소성로 비교 박스, Region A·B 모두의 비교 기준) / 공정사진(img32~35)은 각 관련 Region에 Dependent로 분산 배치
- **Selected Layout**: Before + After Layout, Variant B — Comparison Table (docs/slide-design-rules/before-after/before-after.md)
- **Layout Selection Reason**: 기존소성로(Existing)와 COSOLUS 유도가열(Improved)을 동일 기준(공정시간/에너지/투자비용)으로 비교하는 것이 핵심이라 Variant B 적용. production_directive(CG17-PD01: '박스 2개 위아래 배치')를 Improved측 내부의 가격경쟁력/기술경쟁력 두 박스 배치에 우선 반영.
- **Structural Check**: Region A/B(자사 강점) 정보량 균형 양호(각 2개 세부항목). Region C(비교대조군)가 특정 Region A 또는 B에만 귀속되지 않고 공통 비교 기준으로 유지되는지 확인 — 확인됨. Required Evidence 다수가 출처 인용 없음(NC-12) — 구조 자체엔 문제없으나 신뢰도 참고사항으로 기재.

---

## Slide 18. 경쟁력-[솔루션2] 친환경 차세대 배터리 재활용 공정기술(2세대) (BTR/Vianode 비교)

- **Source Material**: CG18(entire)
- **Core Message**: COSOLUS 유도가열(950℃, 1분 이내)은 BTR의 전기로(3,000℃, 24시간)와 Vianode의 대류가열(3,000℃, 48시간) 대비 훨씬 낮은 온도와 짧은 시간으로 처리한다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS는 BTR·Vianode 대비 가열온도가 낮고 처리시간이 극히 짧으며 에너지소비량도 낮다
    - Evidence: 비교표 전체(기업명/국가/기술/처리시간/특징 × COSOLUS/BTR/Vianode)
    - Relationship: 복수 비교 근거 (3사 비교)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 1(표 전체) / Core Message반영 0 / 중복통합 0 / 라벨제외 3(섹션/제목/제작지시 "Cosolus 우위 강조") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 비교표(단일)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A (표 자체가 결론. "Cosolus 우위 강조"라는 제작 지시는 표현 방식 판단이라 이 단계에서 반영하지 않음 — 강조 방식은 [5] 담당)
- **Relationship**: 비교
- **Content Regions**: Region A(Primary, 5행×4열 비교표)
- **Selected Layout**: Table Comparison Layout (docs/slide-design-rules/table-comparison.md) + Competitive Advantage Highlight (docs/slide-design-rules/019_competitive-advantage-highlight.md)
- **Layout Selection Reason**: 이 슬라이드가 019 문서의 실제 원본 근거 슬라이드(BTR/Vianode 비교) — 자사 열 카드 강조 패턴을 그대로 적용. production_directive(CG18-PD01/02: 표 삽입·Cosolus 우위 강조)와 정확히 일치.
- **Structural Check**: 단일 Region, 문제 없음.

---

## Slide 19. 조직구성

- **Source Material**: CG19(entire)
- **Core Message**: 코솔러스는 CEO·CTO·CSO·COO 중심의 경영진과 기업부설연구소·AI혁신팀·생산팀으로 구성된 27명 규모의 실행 조직을 갖추고 있다.
- **Core Claims & Evidence**:
  - Claim: 각 경영진은 해당 분야의 학위·경력·연구실적을 갖춘 전문가다
    - Evidence: CEO 김성현(서울대 응용화학부 박사/원광대 교수/코솔러스 CEO/논문71편·특허24편)+CTO 장재규(서울대 화학부 박사/코솔러스 CTO/논문18편·특허2편)+CSO 민사훈(서울대 화학생물공학부 박사/코솔러스 CSO/논문25편·특허5편)+COO 오성환(악조노벨 영업매니저 경력/코솔러스 COO) + img37~40(4인 프로필 사진) — 나열된 개별 항목(4인) 전체 유지
    - Relationship: 병렬 동등 항목(Parallel/Peer Items) — [경계 사례] 4인 모두 "학위/경력/실적"이라는 같은 필드 구조를 공유해 표면적으로는 같은 기준으로 나란히 비교하는 것처럼 보이지만, 실제 목적은 우열을 견주는 비교가 아니라 각 경영진이 서로 다른 전문영역(CEO-화학공정기술/CTO-유기합성/CSO-분자시뮬레이션/COO-기술영업)에서 개별적으로 자격을 갖췄음을 나열하는 것이다. COO는 학위·논문·특허 필드 자체가 없어(악조노벨 영업 경력만 존재) 4인이 완전히 동일한 비교축을 공유하지도 않는다 — 같은 기준으로 값을 견주는 비교 근거의 전제가 성립하지 않는다.
    - Required/Optional: Required
  - Claim: 기업부설연구소는 개발1~3팀과 AI혁신팀으로 세분화되어 각기 다른 기술영역을 담당한다
    - Evidence: 개발1팀(6명, 재활용소재)/개발2팀(4명, 플라스틱첨가제)/개발3팀(3명, 재활용공정기술)/AI혁신팀(4명, AI기반 차세대 배터리 재활용 공정기술), 공동개발 임춘우 교수(개발1팀)·김양배 교수(개발2팀)
    - Relationship: 구성요소별 기여도 (4개 팀이 상위 조직인 "기업부설연구소" 전체를 구성하는 부분이라는 전체-부분 성격이 있어 병렬 동등 항목보다 이 유형이 더 적합)
    - Required/Optional: Required
  - Claim: 경영지원팀·기술영업팀·생산1팀 등 지원/영업/생산 조직도 갖추고 있다
    - Evidence: 경영지원팀(2명)/기술영업팀/생산1팀(1명, 장세건 이사 공동개발)
    - Relationship: 구성요소별 기여도
    - Required/Optional: Optional (핵심 기술역량 증빙에는 부차적)
- **Backward Completeness Check**: 명시반영 다수(경영진 4인 프로필 전체, 팀 구성 전체, 공동개발 교수진) / Core Message반영 0 / 중복통합 0 / 라벨제외 2(섹션/제목) / uncertain보류 0 / 미반영 0. "프롬프트: CEO 바로 아래로 기업부설연구소, 양쪽으로 뻗는 형태..." 1건은 production_directives(material_analysis.json CG19-PD01, placement 유형)로 분리·보존되어 target_scope(조직도 전체 구조: CEO 바로 아래 기업부설연구소, 좌우로 가지가 뻗는 형태)까지 남음. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 경영진 4인 프로필(대등, 병렬 동등 항목 Main Content Group)
  - Dependent: 각 경영진 사진(img37~40)
  - Shared Supporting: 기업부설연구소 팀 구성 전체(개발1~3팀+AI혁신팀) — 특정 경영진 1인이 아니라 조직 전체를 보완하는 공통 정보
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(경영진 4인, 병렬 동등 항목) + 전체-부분(팀 구성이 조직 전체를 구성)
- **Content Regions**: Region A~D(Primary, 경영진 4인 각각의 프로필 카드, 병렬 동등 항목 — 4개 카드를 동일 위계로 배치하고 논문·특허 편수 등 일부 필드가 있거나 없다고 해서 순위를 매기는 비교 강조 요소(예: 순위 배지·색상 강조)를 넣지 않음) / Region E(Shared Supporting, 조직도/팀별 인원·담당분야 — production_directives(CG19-PD01)의 배치 지시(CEO 바로 아래 기업부설연구소, 좌: AI혁신팀/CSO/경영지원팀 · 우: 기술영업팀/COO로 가지가 뻗는 구조)를 그대로 반영)
- **Selected Layout**: Organization Chart — Curved Leadership (docs/slide-design-rules/020_organization.md)
- **Layout Selection Reason**: 핵심 경영진(CEO 중심) + 각 책임자 전문분야·담당조직을 함께 전달 — Use When 조건 정확히 부합. 병렬 동등 항목(Parallel/Peer Items) 판단에 따라 3인 임원을 동일 시각적 Weight로 배치, production_directive(CG19-PD01: 조직도 분기 구조)를 Curved Arc + Node 배치에 반영.
- **Structural Check**: Region A~D(경영진 4인) 간 정보량이 다소 상이(CEO는 논문71편·특허24편으로 가장 풍부, COO는 경력 정보만 있어 상대적으로 적음) — 이는 원본 데이터 자체(실제 인물별 실적 차이)이므로 임의로 채우지 않고 그대로 유지. Relationship을 병렬 동등 항목으로 확정함에 따라 4인을 같은 축으로 비교하는 표 형태보다 4인 각각의 독립 프로필 카드 형태가 더 적합함이 명확해짐(Layout Routing 5단계 재개 시 Layout 후보 선정에 반영 필요). Shared Supporting(Region E)이 특정 경영진 Region에 잘못 귀속되지 않고 전체 조직 공통 정보로 별도 배치되었는지 확인됨. production_directive(CG19-PD01)가 Region E 배치 지침의 근거로 명시적으로 연결됨.

---

## Slide 20. 투자포인트

- **Source Material**: CG20(entire)
- **Core Message**: 코솔러스는 최상위 수준의 추출제·친환경 공정 기술력을 바탕으로 사업화를 진행 중이며, Series A2 라운드로 80억원의 투자를 유치해 해외법인 설립과 공장 건설에 사용할 계획이다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스는 추출제 합성/정제 기술, 친환경 공정 기술(건식환원/유도가열), Closed-loop system으로 기술적 차별성을 갖는다
    - Evidence: "추출제 최상위 수준의 합성 및 정제 기술", "친환경 공정 기술(건식환원 및 유도가열 기술)", "Closed-loop system 합성/공정 기술로 환경부담 최소화" (원문 3개)
    - Relationship: 구성요소별 기여도
    - Required/Optional: Required
  - Claim: 코솔러스는 1.5세대·2세대 기술을 각각 국내외 PoC·신공급망·해외진출로 사업화하고 있다
    - Evidence: "(1.5세대-RECYION Series) XX하이텍, XX코 등 현장적용을 고려한 PoC 진행 중" — **파트너사명이 원본 자체에서 "XX"로 비식별 처리됨(needs_confirmation NC-13)**, "(2세대-친환경공정기술) XX자동차 연계 신공급망 구축, 일본 및 인도네시아 시장 진출(파일롯 기술검증 후 JV 설립)" — 동일하게 "XX자동차" 비식별
    - Relationship: 복수 비교 근거 (1.5세대/2세대 각각의 사업화 경로)
    - Required/Optional: Required (단, 실제 대상 기업명 미확인 상태임을 병기)
  - Claim: 코솔러스는 Series A2 라운드로 80억원의 투자를 유치하고자 하며, 국외법인 설립·공장건설·추출제CAPA·공정파일롯에 사용할 계획이다
    - Evidence: "Series A2", "목표 투자유치 금액 = 80억원", "국외법인 설립 및 운영", "공장 건설을 위한 토지 구매 및 건축 비용", "추출제CAPA, 공정파일롯"
    - Relationship: 단일 독립 근거(목표금액) + 구성요소별 기여도(사용계획 항목들)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 다수([기술력] 3항목/[사업화방향] 2항목/[투자라운드] 2항목/[투자금 사용계획] 3항목) / Core Message반영 0 / 중복통합 0 / 라벨제외 4(섹션/제목/박스1·2 라벨) / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 박스1(기술력 및 사업화), 박스2(예상 소요자금) — 대등한 2개 Primary(병렬)
  - Dependent: 각 박스 하위 세부항목(기술력 3개/사업화 2개, 투자라운드/사용계획)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A (두 박스 자체가 이미 "투자포인트"라는 슬라이드 제목의 완결된 답)
- **Relationship**: 병렬
- **Content Regions**: Region A(Primary, 박스1: 기술력+사업화방향) / Region B(Primary, 박스2: 투자라운드+목표금액+사용계획) — 좌우 병렬
- **Selected Layout**: L18. Two-Column Summary (docs/layout-reference/2026.08.13_layout-catalog_V1.md)
- **Layout Selection Reason**: 2개의 대등한 Primary 콘텐츠(기술력및사업화/예상소요자금)를 요약 형태로 병렬 제시 — 특수 Layout Reference 중 Use When에 맞는 문서가 없어 범용 카탈로그에서 'Executive summary / overview / key takeaways' 힌트에 부합하는 L18 채택.
- **Structural Check**: Region A(약 5개 세부항목)와 Region B(약 5개 세부항목) 정보량 대체로 균형. Required Evidence 반영 확인됨. 파트너사 비식별(NC-13)은 구조 문제가 아니라 데이터 신뢰도 문제로 별도 추적.

---

## Slide 21. 세계시장 진출

- **Source Material**: CG21(entire)
- **Core Message**: 코솔러스는 일본·인도네시아를 거점으로 5억명 이상의 아시아 경제권에 진출하며, '26년 파트너십 구축을 시작으로 '29년 판매·서비스 제공까지 단계적 마일스톤을 갖는다.
- **Core Claims & Evidence**:
  - Claim: 일본과 인도네시아를 전략적 거점으로 5억명 이상의 아시아 경제권에서 성장한다
    - Evidence: "5억 명 이상의 아시아 경제권에서 성장" — 출처 인용 없음
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
  - Claim: 인도네시아·일본에서 각각 투자논의가 진행 중이다
    - Evidence: "인도네시아 전기자전거 업체 1대주주와 투자논의 중", "일본 현지투자사, 재료업체 등과 투자논의 중" — 텍스트 서술은 Required. img41(SWAP)/img42(Panasonic Energy)/img43(Iwatani)/img44(DNP) 로고 4개는 **모두 content_match_confidence: uncertain(본문에 회사명이 전혀 언급되지 않아 어느 서술과 매칭되는지 로고 인접성만으로 확인 불가, needs_confirmation NC-14 — 특히 Panasonic Energy·Iwatani·DNP는 잘 알려진 대기업으로 사실관계 확인이 특히 중요)**
    - Relationship: 복수 비교 근거 (인니/일본 두 트랙)
    - Required/Optional: 텍스트 서술은 Required, **로고 이미지 4개는 uncertain이므로 Optional 상한 적용(Required로 승격하지 않음)**
  - Claim: '26년 파트너십 구축 → '27~28년 PoC 획득 → '29년~ 판매/서비스 제공의 3단계 마일스톤을 갖는다
    - Evidence: "'26 일본 및 인도네시아 배터리 재활용 관련 파트너쉽 구축", "'27~28 추출제 및 공정기술 PoC 획득", "'29~ 추출제 판매 및 공정 서비스 제공"
    - Relationship: 시간에 따른 변화·추세 (3개 시점의 단계별 마일스톤)
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 다수([목표]/[논의현황]/마일스톤 3항목) / Core Message반영 0 / 중복통합 0 / 라벨제외 3(섹션/제목/제작지시 "논의중인 현지투자사 이미지 삽입", 이미지 크기 메타정보 4건) / uncertain보류 4(img41~44) / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: [목표](5억명 아시아 경제권), 마일스톤(3단계 시간축) — 대등한 2개 Primary 축(정성적 목표 vs 정량적 로드맵)
  - Dependent: [논의현황] 텍스트 ([목표]를 구체화하는 진행상황이므로 종속)
  - Shared Supporting: 4개 로고 이미지(uncertain) — 특정 Claim 하나가 아니라 [논의현황] 전체(인니+일본 트랙 모두)를 보완
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합 ([목표]+[논의현황] vs 마일스톤의 병렬 + 마일스톤 자체의 시간에 따른 변화)
- **Content Regions**: Region A(Primary, [목표]+[논의현황] 텍스트 블록) / Region B(Shared Supporting, 4개 로고 이미지, uncertain 표시 유지) / Region C(Primary, 마일스톤 타임라인 3단계)
- **Selected Layout**: Timeline / Company Milestone Layout (docs/slide-design-rules/timeline-company-milestone.md) + 상단 Message band 조합
- **Layout Selection Reason**: 하단 3단계 시간축 마일스톤('26/'27~28/'29~)은 Timeline/Company Milestone Use When에 정확히 부합. 다만 상단 목표·논의현황·로고 콘텐츠까지 포괄하는 단일 특수 Layout Reference는 없어, 상단은 Message+Evidence 성격의 밴드로 최소 조합(Hard Rule·Design System 유지 범위 내 조합, 6번 판단 순서 적용).
- **Structural Check**: Region A/C 정보량 균형 양호(각 2~3개 항목). Shared Supporting(Region B, 로고 4개)이 Region A에 임의로 종속되지 않고 별도 유지되는지 확인 — 확인됨(uncertain 근거이므로 독립 배치가 신뢰도 표시에 유리). Required Evidence 반영: Claim2의 텍스트 근거는 반영되었으나 이미지 근거는 uncertain 규칙에 따라 Optional로 하향 처리됨 — 이 사실을 명확히 기록.

---

## Slide 22. 마무리 표지

- **Source Material**: CG22(entire)
- **Core Message**: 코솔러스는 책임있는 화학기술로 순환경제를 선도하고 탄소배출 저감에 기여하는 글로벌 기업으로 도약하고자 한다.
- **Core Claims & Evidence**:
  - Claim: 발표 전체를 요약하는 클로징 메시지를 제시한다
    - Evidence: "코솔러스는 책임있는 화학기술을 기반으로 순환경제를 선도하고 탄소배출 저감에 기여하며 지속가능한 미래를 만들어가는 글로벌 기업으로 도약하고자 합니다." + "Thank You" (원문)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
- **Backward Completeness Check**: 명시반영 2(클로징문구, Thank You) / Core Message반영 0 / 중복통합 0 / 라벨제외 2([마무리표지]/제작지시 "아래 이미지 삽입") / uncertain보류 0 / 미반영 0. 미반영 항목 없음.
- **Content Roles**:
  - Primary: 클로징 메시지 텍스트(Thank You 포함) — 전체 발표를 요약하는 결론 성격을 겸함
  - Dependent: img45(클로징 비주얼, 지구본을 든 손 스톡 이미지)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: (Primary와 역할 겸용, 별도 Region 불필요)
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region A(Primary, 클로징 문구+Thank You+img45)
- **Selected Layout**: L22. Closing / Contact (docs/layout-reference/2026.08.13_layout-catalog_V1.md) 참고 + Hard Rule Dark Background 허용 조항
- **Layout Selection Reason**: 'Final message + contact information' 힌트와 부합하는 클로징 슬라이드. 01_cover_design_V2.md는 표지 전용이라 그대로 적용하지 않되, Hard Rule이 허용하는 '강한 전환이 필요한 슬라이드의 Dark Background(Deep Pine 계열)'를 표지와 대칭되는 브랜드 마무리 톤으로 적용.
- **Structural Check**: 단일 Region, 문제 없음.
