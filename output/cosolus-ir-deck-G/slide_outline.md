# Slide Outline — cosolus-ir-deck-G

## Slide 1. [솔루션2] 개요 - 친환경 차세대 배터리 재활용 공정기술 (2세대)

- **Source Material**: CG01(entire) — `slide_composition_map.json` 그대로 반영

- **Core Message**: 폐배터리를 파쇄·소각해 얻은 블랙매스를, 기존 1세대(용매추출) 공정과 COSOLUS 2세대(부유선별) 공정으로 각각 처리했을 때 공정 경로와 산출물이 어떻게 달라지는지를 하나의 공정 흐름도로 대비시켜, COSOLUS 2세대 공정이 경제성·친환경성·양산성을 확보한 차세대 재활용 기술임을 전달한다.

- **Core Claims & Evidence**:
  - Claim: 폐배터리팩은 파쇄·소각(전처리)을 거쳐 블랙매스라는 공통 중간물질로 전환되며, 이는 1세대·2세대 두 공정 경로의 공통 출발점이다.
    - Evidence: "폐배터리팩을 파쇄·소각하여 블랙매스를 생산한다." (confirmed_text, direct_evidence) + img1(EV 배터리팩 실사)·img2(배터리 셀 실사)·img3(파쇄/소각 아이콘)·img4(블랙매스 실사)
    - Relationship: 순차 공정·프로세스 — 전기차 배터리팩(시작) → 전처리 공정(파쇄·소각) → 블랙매스(결과물, 공통 중간물질)
    - Required/Optional: Required
  - Claim: 기존 1세대 공정은 블랙매스를 용매추출해 MnSO4·NiSO4·CoSO4·Li2CO3 4종 화합물을 회수하지만, 폐흑연이 부산물로 발생한다(흑연을 자원으로 회수하지 못함).
    - Evidence: "기존 1세대 공정에서는 블랙매스를 용매추출하여 MnSO4, NiSO4, CoSO4, Li2CO3를 회수하며 폐흑연이 부산물로 발생한다." + img5(용매추출 설비 도해) + img6~img9(회수 화합물 4종 분말 실사, 화합물별 1:1 매칭 uncertain) + img10(폐흑연 실사)
    - Relationship: 순차 공정·프로세스 — 블랙매스 → 용매추출 → 회수물질(MnSO4/NiSO4/CoSO4/Li2CO3, Output Group) + 폐흑연(부산물, 별도 Sibling Output)
    - Required/Optional: Required(4종 화합물 개별 근거는 img6~9가 uncertain이므로 Optional 상한 — "회수 화합물 4종" 그룹으로만 표현, 개별 화합물-이미지 색상 매칭은 사용하지 않음)
  - Claim: COSOLUS 2세대 공정은 블랙매스를 부유선별해 양극재용/음극재용 블랙매스로 분리하고, 양극재용은 건식환원으로 Co·Ni를, 음극재용은 유도가열로 고순도 정제흑연을 각각 회수한다 — 1세대와 달리 흑연까지 자원으로 재활용한다.
    - Evidence: "COSOLUS 2세대 공정에서는 블랙매스를 부유선별하여 양극재용 블랙매스와 음극재용 블랙매스로 분리한다. 양극재용 블랙매스는 건식환원을 통해 Co·Ni를 회수하고, 음극재용 블랙매스는 유도가열을 통해 고순도 정제흑연을 생산한다." + img11(부유선별 설비 도해) + img12(양극재용 블랙매스, NCM 조성 이미지) + img13(음극재용 블랙매스, 금속 알갱이 박힌 흑연 이미지) + img14(건식환원 반응 이미지) + img15(유도가열 3단계 이미지) + img16(코발트) + img17(니켈) + img18(고순도 정제흑연)
    - Relationship: 단계별 변화(재분기 포함) — 블랙매스 → 부유선별 → [양극재용 블랙매스 → 건식환원 → 코발트+니켈(Output Group)] / [음극재용 블랙매스 → 유도가열 → 고순도 정제흑연]
    - Required/Optional: Required
  - Claim: COSOLUS 2세대 공정은 경제성·친환경성·양산성을 확보한 기술이다.
    - Evidence: "COSOLUS 2세대 공정: 경제성 / 친환경성 / 양산성 확보" (강조 헤드라인, confirmed_text) — 이 자료에는 이를 뒷받침하는 정량 수치(원가절감률·회수율·생산량 등)가 없음. N/A(정성적 헤드라인으로만 존재, 임의 수치 생성 금지 — material_analysis.json needs_confirmation NC-03 참조)
    - Relationship: 단일 독립 근거(정성적 결론 문구, 수치 근거 없음)
    - Required/Optional: Required(슬라이드의 결론이므로 문구 자체는 필수 표시하되, 정량 근거가 없다는 한계를 그대로 유지 — 근거를 만들어 채우지 않음)

- **Backward Completeness Check**: 경량 모드 + 위험 항목(uncertain 근거) 상세 검증 수행.
  - 경량 추적: material_analysis.json CG01-direct_evidence의 confirmed_text 22개 전부가 위 Claim/Evidence 또는 아래 "미반영 항목 재구성"에서 처리됨. images_available 18개 전부(img1~img18) 위 Claim 중 하나 이상에 배정됨. metrics/tables는 원본에 0개이며 배정 대상도 0개로 일치. evidence_manifest 기준 개수·ID 불일치 없음.
  - 상세 검증 대상(uncertain 근거: img6~img9) — material_analysis.json 원문의 note를 직접 대조한 결과, 실제 화합물 색상(MnSO4 옅은분홍~백색/NiSO4 녹색/CoSO4 분홍·적색/Li2CO3 백색)과 이미지 관찰 색상(주황적색/백색/청록/크림백색) 순서가 확정적으로 대응하지 않음을 재확인. Required 근거로 승격하지 않고 Optional 상한을 유지했으며, Content Region 설계에서도 개별 화합물-이미지 매칭 없이 4종 화합물 이미지를 하나의 Output Group으로만 표현하도록 반영함.
  - 6분류 결과: 명시반영 20(confirmed_text 항목 대부분 + 18개 이미지) / Core Message반영 1("[강조 내용]" 라벨은 헤드라인이 그 자체로 명시반영되므로 라벨 자체는 4-라벨제외로 처리) / 라벨제외 3(원문의 "[슬라이드 제목]"/"[내용]"/"[강조 내용]"/"[공정 흐름도 라벨 — 원문 순서 그대로 보존]" 4개 대괄호 섹션 라벨은 정보량 없는 구획 표시로 판단해 슬라이드 본문에는 반영하지 않음, 그 라벨이 감싸는 실제 내용은 모두 위 Claim에 반영됨) / uncertain보류 4(img6~9) / 미반영 0.
  - 미반영 항목 없음. 슬라이드 경계 재조정(content-grouping 재호출) 필요 없음.

- **Content Roles**:
  - Primary: 공정 흐름도 전체(공통 시작 → 1차 분기[1세대/2세대] → 2세대 내부 재분기[양극재용/음극재용]) — 슬라이드의 핵심 메시지를 직접 전달하는 단일 대형 Visual
  - Dependent: 각 공정 단계 라벨·아이콘(전처리/용매추출/부유선별/건식환원/유도가열)과 각 Material/Output 라벨·이미지(배터리팩/블랙매스/회수 화합물 4종/폐흑연/양극재용·음극재용 블랙매스/코발트·니켈/고순도 정제흑연) — 공정 흐름도(Primary)에 종속되어 함께 배치
  - Shared Supporting: N/A (본문 서술 3문장은 공정 흐름도 자체의 서술적 재진술이며 별도 Region이 아니라 상단 Intro Text로 흡수 — 아래 Content Regions 참조)
  - Conclusion/Takeaway: "COSOLUS 2세대 공정: 경제성 / 친환경성 / 양산성 확보" — 공정 흐름도 전체(1세대 대비 2세대의 차별점)를 종합해 도출되는 결론 문구

- **Relationship**: 순차·인과 복합(단계별 변화 + 분기 비교) — 공통 순차 공정 이후 1세대/2세대 두 카테고리로 분기(비교), 2세대 내부에서 다시 재분기

- **Content Regions**:
  - Region A(Header, Conclusion): 상단에 결론 헤드라인 "COSOLUS 2세대 공정: 경제성/친환경성/양산성 확보" 배치 — 공정 흐름도 전체를 종합하는 문구이므로 특정 Lane에 속하지 않고 슬라이드 상단 전체 폭 기준으로 배치(Integrated Conclusion 원칙)
  - Region B(Main, Primary — Flow Diagram 본체): 좌→우 흐름의 공정 흐름도. 공통 시작 영역(배터리팩 Material → 전처리 Process → 블랙매스 Material, Region Map 0~35%) → 1차 분기점(33~38%) → 상단 Lane(1세대: 용매추출 Process → 회수 화합물 4종 Output Group + 폐흑연 Sibling Output) / 하단 Lane(2세대: 부유선별 Process → 2세대 내부 재분기점(48~55%) → 양극재용 블랙매스 Lane[건식환원 Process → 코발트+니켈 Output Group] / 음극재용 블랙매스 Lane[유도가열 Process → 고순도 정제흑연 Output]). 상단 Lane(1세대) 라벨 박스와 하단 Lane(2세대) 라벨 박스는 각 구간 위쪽에 별도 배치, 두 구간 사이 가로 점선 구분선 적용
  - Region C(카테고리 라벨): "기존공정(1세대)" / "COSOLUS(2세대)" 라벨 박스 — 각 Lane 세로 영역 안, 1차 분기점보다 왼쪽(20~35% 구간)에 위치, 색상 대비 규칙에 따라 두 카테고리를 서로 다른 색으로 구분
  - 본문 서술 3문장(폐배터리팩 파쇄·소각/1세대 공정 설명/2세대 공정 설명)은 별도 텍스트 블록으로 반복하지 않고 위 Region B의 Node 라벨·구조 자체로 대체 표현한다(동일 정보를 텍스트+다이어그램으로 중복 제시하지 않음 — 다이어그램이 이미 그 서술을 구조적으로 전달)
  - uncertain 근거(img6~img9)는 Region B의 1세대 Lane Output Group 안에서 "회수 화합물 4종"이라는 그룹 라벨로만 표현하고, 개별 화합물명-이미지 색상을 1:1로 라벨링하지 않는다

- **Selected Layout**: Flow Diagram (L25 Symmetric Two-Split) — `docs/slide-design-rules/flow-diagram-rules.md` + Region Map, 공간 구조 원본 기준은 `2026.08.13_ppt_layout_set__V3.pptx` 슬라이드 25~26(layout-catalog_V1.md L25), 실제 좌표 산출 1차 소스는 `flow-diagram-implementation-reference.md`

- **Layout Selection Reason**: `2026.08.20_special-layout-index_V1.md`의 "분기형 공정도" 카테고리 Use When("하나의 공통 시작점에서 2개 이상의 갈래로 분기하는 공정·흐름을 보여줘야 하고, 각 갈래를 색상 등으로 뚜렷하게 대비시켜야 할 때 · 갈래가 다시 하위 갈래로 재분기하는 구조를 포함할 때")에 정확히 부합한다 — 이 자료는 (1) 배터리팩→전처리→블랙매스라는 공통 시작점을 가지며, (2) 1세대/2세대로 1차 분기하고, (3) 2세대 내부에서 양극재용/음극재용으로 재분기하는 구조를 원문 자체가 갖고 있다. Do Not Use When 항목(좌우 정확히 2개 비교만이 핵심 → before-after 우선 / 공정 뒤에 하단에서 별도 비교 → process-comparison 우선 / 단일 선형 흐름만 → process-system-architecture 우선 / 비교 대상 3개 이상 → comparison-matrix 우선)에는 해당하지 않는다 — 이 슬라이드는 "공유 시작점에서 분기하는 하나의 트리 구조" 자체가 핵심이므로 L25가 가장 적합하다. 또한 목표 슬라이드 수 1장이라는 제약상 18개 이미지·22개 텍스트 항목을 별도 텍스트 요약 없이 하나의 압축적 Visual로 담아야 하는데, L25는 정확히 이 규모의 분기형 공정 콘텐츠를 한 슬라이드에 담도록 설계된 Layout이다.

- **Structural Check**: 문제 없음(경미한 조정 반영 완료).
  - 특정 Region 과밀 여부: Region B(Flow Diagram)에 18개 이미지가 모두 몰리지만, flow-diagram-rules.md의 Region Map·Occupied Area 규칙에 따라 좌→우 순차 배치되며 각 Node가 동일 위계 내 유사 크기를 유지하도록 설계되어 있어 단일 Region 과밀이 아니라 의도된 Layout 구조임.
  - 병렬 Lane 간 정보량 불균형: 1세대 Lane(용매추출 Process 1개 + Output Group 1개 + Sibling Output 1개)과 2세대 Lane(부유선별 Process 1개 + 재분기 2개 Sub-lane, 각 Process 1개+Output 1개)은 2세대 쪽이 정보량이 더 많다 — 이는 원문 자체의 비대칭(2세대가 핵심 기술이라 더 상세히 설명됨)을 반영한 것이며, Region Map의 상/하 Lane 세로 영역 비율(45~50% vs 50~55%)이 이 비대칭을 완충하도록 이미 설계되어 있어 임의 조정하지 않음.
  - Shared Supporting Content 오귀속 여부: Shared Supporting Content가 N/A이므로 해당 없음.
  - Required Evidence 반영 여부: 4개 Claim의 Required Evidence(공통 시작 공정, 1세대 공정 전체, 2세대 공정 전체, 결론 헤드라인) 모두 Region B/A에 반영됨. uncertain 근거(img6~9)는 Optional 상한을 유지한 채 그룹 표현으로만 반영.
  - 서로 다른 상위 주장의 근거 뭉뚱그림 여부: 1세대 근거(img5~10)와 2세대 근거(img11~18)는 서로 다른 Lane으로 명확히 구분되어 있어 뭉뚱그려지지 않음.
  - Data Pending 여부: 이 슬라이드에는 data_status: data_pending 항목이 없음(material_analysis.json data_pending_carried: 빈 배열).
  - Conclusion 매몰 여부: 결론 헤드라인은 특정 Lane 내부가 아니라 Region A(상단, 전체 폭 기준)에 별도 배치되어 매몰되지 않음.
  - 콘텐츠량 대비 슬라이드 분할 필요성: 1장 목표 제약 하에서 원문 전체(18개 이미지+22개 텍스트 항목)가 L25 Layout 하나에 담기는 규모이며, 별도 요약이나 부록 이관 없이 1장으로 구성 가능하다고 판단함 — 추가 분할 불필요.
