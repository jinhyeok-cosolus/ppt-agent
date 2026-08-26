# Slide Claims & Evidence — cosolus-ir-deck-D-regression (slide-content-structuring 1단계+1-b 실행 결과)

> 이 문서는 `slide-content-structuring` SKILL.md의 **1단계(핵심 메시지 파악) + 1-b(Claim→Evidence→Relationship→Required/Optional)만** 실행한 중간 산출물이다. 입력은 `slide_composition_map.json`(슬라이드 경계·Source Material — 재판단하지 않고 그대로 사용)과 `material_analysis_sample.json`(23개 Content Group 전체, 새 스키마)이다. 구 `cosolus-ir-deck-D/material_analysis.json`(flat, 잘못된 이미지 라벨 포함)은 입력으로 사용하지 않았다.
>
> **이번 범위가 아닌 것**: Content Role 분류(2단계), 슬라이드 전체 Relationship 분석(3단계), Content Region 설계(4단계), Layout Routing(5단계), 구조적 사전 점검(6단계) — 즉 Visual Strategy/Layout/HTML로 이어지는 모든 판단은 각 슬라이드 하단에 "다음 단계 — 이번 범위 아님"으로만 표시하고 채우지 않았다. 최종 `slide_outline.md`는 이 단계들이 완료된 뒤 별도로 작성한다.

---

## Slide 1. 표지

- **Source Material**: CG01(entire)
- **Core Message**: COSOLUS — 지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술
- **Core Claims & Evidence**: N/A(표지는 Claim/Evidence 구조 분석 대상이 아님 — 브랜드 메시지 제시)
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 2. 기업 소개

- **Source Material**: CG02(entire)
- **Core Message**: 코솔러스는 첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제를 선도하는 전문 기업이다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스는 신뢰할 수 있는 실체를 갖춘 화학소재·공정 전문 기업이다.
    - Evidence: table_1(기업명/대표자/임직원/소재지/비전, CG02-ST02, `relation_confidence: structural`, 5개 항목 모두 metrics와 일치 확인)
    - Relationship: 단일 독립 근거(정보 나열형, 항목 간 비교·추세 없음)
    - Required/Optional: Required(5개 항목 모두)
  - 보조 근거(별도 Claim은 아님): CG02-ST03 img2(실험실 사진) — `content_match_confidence: uncertain`(이미지 내용 육안 재확인 안 됨) → **Optional 상한**, 확정 근거로 서술하지 않는다("현장 사진으로 추정, 사용 전 재확인 필요"로만 표기).
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 3. 배터리 밸류체인의 환경·지정학적 리스크

- **Source Material**: CG03-ST01(entire, evidence_clusters EC1+EC2), CG03-ST02(entire)
- **Core Message**: 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있으며, 채굴 기반 공급은 환경·사회적 비용을 수반한다.
- **Core Claims & Evidence**:
  - Claim A (EC1): 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있다.
    - Evidence: 전략광물 20개 중 19개 정제 1위(IEA) / 정제 평균 점유율 70%(IEA) / 글로벌 블랙매스 처리 비중 89%(Benchmark Mineral Intelligence) — 모두 metrics `confirmed`. img3(중국 강조 세계지도, `likely_supports: EC1`)는 `content_match_confidence: uncertain`(육안 재확인 안 됨)
    - Relationship: 복수 비교 근거(동일 기준 "집중도"를 나타내는 3개 정량 지표, 지도가 공간적으로 뒷받침)
    - Required/Optional: Required(3개 지표) / Optional(img3 — uncertain이므로 Required 승격 금지, Optional 상한)
  - Claim B (EC2): 채굴 기반 공급은 환경·사회적 비용을 수반한다.
    - Evidence: 니켈 1톤당 133톤 폐기물 발생(Earthworks, confirmed) / 채굴 산업의 노동·인권 문제(서술)
    - Relationship: 단일 독립 근거(133t 수치가 핵심, 서술은 정성적 보강)
    - Required/Optional: Required(133t) / Optional(노동·인권 서술)
  - Evidence-Claim 매핑: Claim A·B는 서로 다른 상위 주장(material-analysis 단계에서 이미 evidence_cluster로 분리돼 있었고, 여기서 그 분리를 그대로 확정) — 하나의 균질한 근거 그룹으로 합치지 않는다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 4. 북미 ESS 시장, 고성장의 변곡점

- **Source Material**: CG04(entire)
- **Core Message**: 북미 ESS(에너지저장장치) 시장은 에너지 용량(GWh) 기준 연평균 31.6% 성장이 전망된다.
- **Core Claims & Evidence**:
  - Claim: 북미 ESS 시장은 고속 성장한다.
    - Evidence: CAGR 31.6%(metrics, confirmed) — 연도별 GWh 계열·원본 차트 이미지 없음(NC-01 유지)
    - Relationship: 단일 독립 근거
    - Required/Optional: Required
  - 보조 근거: img4("5 YEARS" 성장 그래픽) — `content_match_confidence: confirmed`이지만 **특정 수치 계열을 담은 원본 차트가 아니라 범용 성장 스톡 그래픽**임을 명시. Optional(장식적 보조 시각자료, 데이터 근거 아님).
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

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
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 6. 1세대 공정의 한계와 코솔러스의 솔루션

- **Source Material**: CG06(entire), CG07-ST01(entire), CG07-ST02(entire)
- **Core Message**: 1세대 재활용 공정은 낮은 선택성·불안정한 상분리·과다한 부산물 발생 등의 한계를 가지며, 코솔러스는 고성능 추출제(1.5세대, RECYION Series) 도입으로 이를 해결한다.
- **Core Claims & Evidence**:
  - Claim: 코솔러스 1.5세대 추출제(RECYION Series)가 1세대 공정의 한계를 해결한다.
    - Evidence(Before): 낮은 선택성 / 제한된 동작 환경(pH 등) / 상분리 불안정 / 부산물 과다발생(망초 등) — CG06 텍스트, confirmed
    - Evidence(After): 고성능 추출제 RECYION Series, 기존 추출제(D2EHPA) 대비 재활용 효율 개선 — CG07 텍스트, confirmed
    - Relationship: Before/After(전환 전후 두 상태)
    - Required/Optional: Required(Before 4항목 + After 솔루션 개요 전체 — 대표 항목 하나로 축약하지 않음)
  - **이미지 근거 — 새 구조화로 정정된 부분**:
    - CG06-ST02 img5: 새 검증 결과 **GLENCORE 로고**로 확인됨(`content_match_confidence: uncertain`, NC-05) — Before(1세대 공정 개념도)의 근거로 **사용하지 않는다**. 구 flat schema는 이 위치를 "1세대 공정 개념도"로 추정 기재했으나 실제 이미지가 아니므로, 그 가정에 기반한 Evidence는 폐기한다.
    - CG07-ST02 img6/img7(화학구조식): `content_match_confidence: uncertain`(D2EHPA/RECYION 중 어느 쪽인지 미확인) — Optional 상한, 라벨 확정 전 실제 배치 금지.
    - 결과적으로 이 슬라이드의 Before/After Claim은 **텍스트 근거만으로 Required가 성립**하며, 이미지는 전부 Optional/보류 상태다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 7. 고성능 추출제 — 경쟁사 대비 공정 효율

- **Source Material**: CG08(entire)
- **Core Message**: COSOLUS 추출제는 벨기에 S사·중국 K사 대비 공정시간과 첨가제 사용량에서 우위를 갖는다.
- **Core Claims & Evidence**:
  - Claim: COSOLUS 추출제는 경쟁사(벨기에 S사, 중국 K사) 대비 공정시간·첨가제 사용량이 우수하다.
    - Evidence: 공정시간 — COSOLUS 기준, 벨기에 S사 100%↑, 중국 K사 50%↑(table_7 "공정시간" 행 셀 자체는 원문 그래픽 처리로 빈칸 — 인접 문단 텍스트로 재구성, 수치 자체는 원문 그대로) / 첨가제 사용량 — 벨기에 10%+, 중국 5%+(table_7 confirmed)
    - Relationship: 복수 비교 근거(3개 대상 × 2개 기준)
    - Required/Optional: Required(전체) — 공정시간 값은 재구성 출처임을 각주로 유지
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 8. 추출단수 저감이 만드는 CAPEX·OPEX 경제성

- **Source Material**: CG09(entire)
- **Core Message**: COSOLUS 추출제는 이론단수를 1단 저감(5단→4단)시켜 CAPEX·OPEX 양면에서 경제성을 확보한다.
- **Core Claims & Evidence**:
  - Claim: 추출단수 1단 저감이 CAPEX·OPEX 두 가지 정량 효과를 만든다.
    - Evidence: 추출단수 5단→4단(20% 감소, table_8 confirmed) → CAPEX(효율 2~5% 개선) / OPEX(망초 5% 이상 저감, 연간 니켈 16,000톤 기준 4,800톤 저감 — 16,000×(3.6-3.3)=4,800 정합 확인)
    - Relationship: 원인→결과(하나의 원인이 두 개의 병렬 정량 효과를 만듦)
    - Required/Optional: Required(단수 저감 값 + CAPEX 효과 + OPEX 효과 전체)
  - 보조 근거: img8("평형선/조업선/단수계산" 범례) — `content_match_confidence: confirmed`. 이론단수 계산 다이어그램의 범례로 판단되나 다이어그램 본체는 아님 → Optional(보조 시각자료).
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 9. 직접리튬추출(DLE) — 재활용 공정 안에서 완성

- **Source Material**: CG11(entire)
- **Core Message**: 기존 DLE(증발법)는 단일 단계·낮은 회수율(3.12%)에 그치지만, 코솔러스는 NCM 스크랩에서 Mn·Co·Ni·Li을 순차 회수하는 4단계 공정 안에서 리튬까지 회수한다.
- **Core Claims & Evidence**:
  - Claim 1: 코솔러스는 재활용 공정 안에서 4개 금속을 순차 회수한다.
    - Evidence: 침출 → 불순물 제거 → (1)Mn 추출 → (2)Co 추출 → (3)Ni 추출 → (4)Li 추출 → 역추출(confirmed, 순서 전체)
    - Relationship: 순차 공정/프로세스 / Required(6단계 전체 순서)
  - Claim 2: 코솔러스 공정은 기존 DLE(증발법) 대비 우위에 있다.
    - Evidence: 기존 DLE(증발법) — 1단계, Li 회수율 3.12%(confirmed) / 코솔러스 — NCM 스크랩 재활용 공정 안에서 통합 회수
    - Relationship: Before/After / Required
  - 이미지 근거: img10(칠레 아타카마 염호 유형 항공사진), img11(지열발전 연계 플랜트) — 둘 다 `content_match_confidence: confirmed`(직접 열어 확인) → Claim2의 "기존 DLE(증발법)" Before 상태를 보여주는 신뢰 가능한 시각 근거로 사용 가능(서술만으로도 주장은 성립하므로 Optional, 다만 uncertain이 아니라 confirmed라는 점에서 Slide 6/7의 이미지들과 신뢰도가 다름).
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 10. DLE 기술 동향 비교

- **Source Material**: CG12(entire)
- **Core Message**: DLE(직접리튬추출) 기술은 흡착제·추출제·분리막·전기화학 4개 방식으로 나뉘며, 각각 작동원리·기술성숙도(TRL)·장단점이 다르다.
- **Core Claims & Evidence**:
  - Claim: DLE는 4개 방식으로 나뉘며 각각 작동원리·TRL·장단점이 다르다.
    - Evidence: table_12(작동원리/TRL/장점/단점 × 흡착제·추출제·분리막·전기화학) — confirmed
    - Relationship: 복수 비교 근거(4개 대상, 동일 기준 반복)
    - Required/Optional: Required(4개 방식 × 4개 기준 전체)
  - 보조 근거: img12(5종 재료구조 비교 일러스트, Mxene/COF/Graphene oxide/MOF/Crown ether) — `content_match_confidence: confirmed` → Optional 보강 시각자료.
  - **정정사항**: 이 슬라이드에 H+/O/H2O 전기화학 이온 다이어그램(img19/img28)을 사용하지 **않는다**. 새 구조화로 그 이미지가 실제로는 CG15/16(Slide 12)에 구조적으로 속함이 확인됐고, CG12의 텍스트 라벨('Li'/'Cl-'/'e-')과의 연결은 Content Group 경계를 넘는 확정 근거가 없어 cross_group_ref로 잇지 않았다(NC-06) — 구 flat schema였다면 이 이미지를 이 슬라이드용으로 오인해 썼을 가능성이 있는 지점이다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 11. DLE 핵심 경쟁력 — 추출제·분리막 결합 기술

- **Source Material**: CG13(entire), CG14(entire)
- **Core Message**: 추출제와 분리막을 결합한 COSOLUS DLE 기술은 리튬 재자원화율을 90% 이상으로, 공정비용을 5,500원/kg 이하로 낮춘다.
- **Core Claims & Evidence**:
  - Claim 1(핵심 성과): COSOLUS DLE 기술은 재자원화율 90% 이상, 공정비용 5,500원/kg 이하를 달성한다.
    - Evidence: "COSOLUS 화학구조 설계·정제·공정 기술 → 재자원화율(>90%), 공정비용(<5,500원/kg)"(전제: 리튬선물 가격 약 44,100천원/ton 기준 각주, confirmed)
    - Relationship: 단일 독립 근거(최종 성과치) / Required(수치 + 전제 각주)
  - Claim 2(기여 분해, Claim 1의 근거): 재자원화율 개선은 두 기술 요소가 각각 다른 수준까지 기여한다.
    - Evidence: 분리막 & THz 기술 — 3%→90% / 핵심소재 — 3%→50%(둘 다 confirmed metrics)
    - Relationship: 구성요소별 기여도(두 기여 요소 값 모두 대등하게 보존)
    - Required/Optional: Required(두 값 모두 — 대표값 하나로 축약 금지)
    - 보조 근거: img13(폴리머 사슬이 혼합 금속이온에서 Li⁺만 선택 포집하는 개념도) — `content_match_confidence: confirmed`, Claim 2의 메커니즘을 직접 시각화 → Optional(이해를 크게 도우나 수치만으로도 주장 성립).
  - Claim 3(공유 근거): 추출제-분리막 결합의 4가지 구조적 강점(CG13)이 Claim 1·2를 함께 뒷받침한다.
    - Evidence: ①빠른 물질전달 ②우수한 재활용 효율 ③연속 운전 ④첨가제 소모량 감소
    - Relationship: 기타(병렬 나열형, Shared Supporting)
    - Required/Optional: Optional(근거를 강화하지만 없어도 Claim 1·2 자체는 성립)
  - **정정사항**: CG14-ST02의 표("RECYION501, 회수 효율")는 원문 셀 자체가 비어 있어(NC-07) **Evidence로 채택하지 않는다** — 빈 값을 추정으로 채우지 않는다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 12. 친환경 차세대 배터리 재활용 공정(2세대)

- **Source Material**: CG15(entire), CG16(entire)
- **Core Message**: 코솔러스 2세대 공정은 유도가열 → 전처리 → 블랙매스 생성 → 부유선별의 흐름으로 고순도 정제흑연과 코발트·니켈을 회수하며, 경제성·친환경성·양산성을 동시에 확보한다.
- **Core Claims & Evidence**:
  - Claim: 2세대 공정은 4단계 흐름을 거쳐 고순도 정제흑연과 코발트·니켈을 회수하고 경제성·친환경성·양산성을 확보한다.
    - Evidence: ①유도가열 ②전처리 공정 ③블랙매스 생성(양극재용/음극재용) ④부유선별 → Output(고순도 정제흑연 + 코발트·니켈) — CG15/16 텍스트, confirmed
    - Relationship: 순차 공정/프로세스(4단계 전체 순서)
    - Required/Optional: Required(4단계 전체 + Output) — **텍스트만으로 이미 성립**
  - **이미지 근거 — 대규모 정정사항**: CG15+CG16에 구조적으로 확인된 이미지가 16개 슬롯(6종 자산이 두 그룹에 중복)이나, `content_match_confidence: confirmed`로 직접 확인한 결과 대부분은 반응조 단면 개념도·흑연/광물 렌더링·NCM 분자모델·전기화학 다이어그램·3단계 효과 그래픽·EV 배터리팩 렌더링 등 **컨셉 일러스트**이며, 실사진은 img20(산업용 컨테이너, 블랙매스 추정) 1장뿐이다. 구 flat schema는 이 위치를 "COSOLUS 유도가열 실제 설비 사진(img62~65)"으로 서술했으나 이는 실제 이미지 구성과 다르다 — **그 전제에 기반한 Evidence·Layout 판단은 폐기해야 한다.**
    - 모든 이미지는 Required Claim(텍스트로 이미 완결)에 대해 Optional 보조 시각자료로만 취급한다. 어느 이미지도 Required로 승격하지 않는다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님(단, 향후 Layout Routing 시 위 이미지 구성 정정사항을 반드시 재검토해야 함 — 구 outline의 "실사진 25%뿐이라 Layout A" 판단 근거 자체가 무효화됨)

---

## Slide 13. 2세대 공정의 가격·기술 경쟁력

- **Source Material**: CG17(entire), CG18(entire)
- **Core Message**: 코솔러스 2세대 공정(유도가열)은 기존 소성로(Pusher Kiln) 대비 짧은 공정시간·적은 에너지 투입과 함께, 고순도 재생흑연·낮은 부반응 등 기술적 우위를 갖는다.
- **Core Claims & Evidence**:
  - Claim 1: 2세대 공정(유도가열)은 기존 소성로 대비 가격·기술 경쟁력이 있다.
    - Evidence: 공정시간(1분 이내 vs 10시간 이상) / 승온속도(200배) / 에너지 투입(432Wh/kg, 64% 절감) / 흑연 순도(99% 이상) / 부반응(낮음) — CG18 metrics, confirmed
    - Relationship: Before/After(정확히 2개 대상, 다기준 비교)
    - Required/Optional: Required(비교 기준 전체 — 일부만 남기지 않음)
  - Claim 2(공유 근거, Claim 1의 기술경쟁력 부분을 보강): 2세대 공정은 추가 기술 신뢰도 근거를 갖는다.
    - Evidence: Co 회수 순도 >95% / PCT 2건 출원 — CG17 metrics, confirmed
    - Relationship: 단일 독립 근거 2건(병렬 나열)
    - Required/Optional: Optional(Claim 1이 이미 핵심 주장을 성립시키며, 이 근거는 보강 성격)
  - **신규 이미지 근거(구 schema에는 전혀 없었음)**:
    - CG17 img30(건식환원 설비 렌더링) — `content_match_confidence: confirmed` → Claim 2를 뒷받침하는 시각 근거 후보, Optional. img31/32/33은 구조적 소속만 confirmed이고 개별 내용은 `uncertain` — Optional 후보로만 두고 개별 확정 근거로 쓰지 않는다.
    - CG18 img34/35(모듈형 설비·터널형 산업로 실사진) — `content_match_confidence: confirmed`, 실제 COSOLUS 설비로 추정되는 실사진 → Claim 1을 뒷받침하는 브랜드 진정성 높은 시각 근거 후보, Optional.
    - 구 `material_analysis.json`의 B17/B18은 `images_available: []`(둘 다 0장)였다 — 이 6장은 이번 신규 구조화가 아니었다면 존재 자체를 알 수 없었던 근거다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

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
    - Required/Optional: Required(두 트랙 모두 — 마스킹된 실명 "XX하이텍/XX코/XX자동차"는 원문 그대로 유지, 임의 실명 채우지 않음)
  - Claim 3: 코솔러스는 Series A2로 80억원 투자를 유치한다.
    - Evidence: 투자라운드 Series A2, 목표 투자유치 금액 80억원(metrics, confirmed)
    - Relationship: 단일 독립 근거 / Required
  - Claim 4: 투자금은 해외 진출·공장 건설에 사용된다.
    - Evidence: 국외법인 설립·운영 / 토지 구매·건축(추출제 CAPA, 공정파일롯)
    - Relationship: 단일 독립 근거(2항목 나열) / Required
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## Slide 15. 일본·인도네시아 시장 진출

- **Source Material**: CG22(entire), CG23-ST08(partial — cross_group_ref로 가져온 항목만)
- **Core Message**: 코솔러스는 5억 명 이상 아시아 경제권을 겨냥해 일본과 인도네시아를 전략적 거점으로 세계시장 진출을 추진한다.
- **Core Claims & Evidence**:
  - Claim 1: 인도네시아에서 구체적 투자 논의가 진행 중이다.
    - Evidence: 전기자전거 업체 1대주주와 투자 논의(서술, confirmed) / SWAP 로고(img36, CG22 구조적 confirmed) / MUKTI·eCoNiL·IBC 로고(CG23-ST08 cross_group_ref, 전부 confirmed — 배포 asset과 파일 크기까지 일치)
    - Relationship: 단일 독립 근거(논의 현황 서술) + 이미지 근거(직접 대응)
    - Required/Optional: Required(논의 현황 서술) / Optional(로고 4종 — 있으면 신뢰도를 높이나 서술만으로도 주장 성립)
    - **정정사항**: HLI 로고(img79)는 `content_match_confidence: uncertain`이며 과거 v1/v2에서도 미사용 이력이 있어 이번에도 **Evidence 후보에서 제외**한다(Optional로도 올리지 않음, 확정 근거처럼 취급 금지).
  - Claim 2: 일본에서도 투자 논의가 진행 중이다.
    - Evidence: 현지투자사·재료업체 등과 투자 논의(익명 서술, confirmed) — Panasonic Energy/Iwatani/DNP 로고(img37-39, 이미지 정체는 confirmed)
    - Relationship: 단일 독립 근거(논의 현황 서술)
    - Required/Optional: Required(서술) / Optional(로고 — 사용 시 특정 파트너십 단정 문구 없이 "일본 배터리·소재 생태계" 맥락으로만, NC-04 유지)
  - Evidence-Claim 매핑: 인도네시아 로고(img36+cross-ref 3종)는 Claim 1에 직접 대응하는 근거이나, 일본 로고(Panasonic/Iwatani/DNP)는 Claim 2에 이미지 정체는 확정이나(파일 크기까지 일치 확인) 본문의 익명 서술과 구체적으로 매칭된다는 확정 근거는 없다 — 두 로고 그룹을 "동일한 확정 근거"로 동등하게 다루지 않는다.
- Content Roles / Relationship / Content Regions / Selected Layout / Structural Check: 다음 단계 — 이번 범위 아님

---

## 요약: 이번 정정으로 Required/Optional·사용 근거가 바뀐 지점

| 슬라이드 | 정정 내용 |
|---|---|
| Slide 6 | Before(1세대 공정) 이미지 근거를 완전히 제거(GLENCORE 로고, 무관) — Claim은 텍스트만으로 Required 성립 |
| Slide 10 | H+/O/H2O 다이어그램을 이 슬라이드 근거에서 제외(실제로는 다른 Group 소속, cross_group_ref 미확정) |
| Slide 11 | RECYION501 표(빈 값)를 Evidence에서 제외 |
| Slide 12 | "실사진"이라는 잘못된 전제를 제거 — 이미지 전부 Optional로 하향, 실사진은 1장뿐임을 명시 |
| Slide 13 | 구 schema에 없던 이미지 6장(CG17 4장 + CG18 2장) 신규 추가, 전부 Optional로 도입(과대평가 방지) |
| Slide 15 | HLI 로고를 Evidence 후보에서 완전히 제외(Optional로도 올리지 않음) |
| 전체 공통 | `content_match_confidence: uncertain` 근거는 예외 없이 Optional 상한 적용(slide-content-structuring SKILL.md 1-b에 규칙으로 명문화함) |
