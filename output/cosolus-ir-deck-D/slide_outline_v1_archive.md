# Slide Outline — cosolus-ir-deck-D (회귀 테스트 D)

> 대상: 고객사/외부 청중 · 언어: 한국어 · 발표시간: 20분 · 목표 슬라이드 수: 15장 · 레퍼런스: 없음
> 입력: `output/cosolus-ir-deck-D/material_analysis.json` (cosolus-ir-deck-C에서 복사, 재추출 없음)
> 본 outline은 C의 기존 slide_outline.md를 참고하지 않고 현재 시점 design-rules.md(신규 Layout 2종 포함) 기준으로 새로 판단했다.
> QA 참고(메인 지시 사항): 집중 Visual QA 대상은 Slide 4/7/10/14(고정) + 신규 Layout이 실제 선택된 Slide 12(Process/System Architecture Layout)이다. 신규 Layout 후보였던 Product/Application Layout은 이번 콘텐츠에 적합한 슬라이드가 없어 미사용이다(사유는 각 슬라이드 판단 참조, 특히 미사용 사유 총평은 문서 최하단 참고).

---

## Slide 1. 표지

- **Core Message**: COSOLUS — 지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술
- **Content Roles**:
  - Primary: 회사 모토("Small actions, BIG DIFFERENCE") + 핵심 한 줄 설명("지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술")
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: 표지 전용 구조 — Region 구성은 `01_cover_design_V2.md`를 그대로 따른다(여기서 별도 Region을 새로 설계하지 않음).
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: Hard Rule 및 design-rules.md "표지 전용" 규칙에 따라 표지는 항상 이 문서를 우선 적용.
- **Structural Check**: 문제 없음. 로고는 White/Reversed 버전(`cosolus CI.png`, Dark Background용) 사용 대상. img34(워드마크)는 참고용일 뿐 실제 로고 자산이 아니므로 사용하지 않음(B01 notes).

---

## Slide 2. 기업 소개

- **Core Message**: 코솔러스는 첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제를 선도하는 전문 기업이다.
- **Content Roles**:
  - Primary: 회사 핵심 메시지("첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제 선도") + 기본 정보(기업명/대표자/임직원/소재지/비전) — table_1 기반
  - Dependent: 비전 문구(핵심 메시지를 구체화)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠(정보 요약형)
- **Content Regions**: 좌측 Information Region(핵심 메시지 + 기업명/대표자/임직원/소재지/비전 기본 정보) / 우측 Vertical Image Region(현장 사진)
- **Selected Layout**: Company Introduction (`docs/slide-design-rules/02_instruction_design_V1.md`)
- **Layout Selection Reason**: Use When "회사 정체성·핵심 메시지·기본 정보(기업명/대표자/임직원/소재지/비전)를 외부 청중에게 전달"에 정확히 부합. Do Not Use 조건(좌우 2단 구조가 콘텐츠와 안 맞는 경우)에 해당하지 않음.
- **Structural Check**: 문제 없음. img2(글러브박스 작업 사진, 실제 COSOLUS 연구현장 추정)를 우측 이미지로 활용. B20(조직구성) 본문이 전무하므로(NC-03) 별도 슬라이드로 만들지 않고 이 슬라이드에 임직원 27명 등 확인된 사실만 반영 — 조직도·인물 캡션은 임의 생성하지 않음.

---

## Slide 3. 배터리 밸류체인의 환경·지정학적 리스크

- **Core Message**: 배터리 핵심광물 공급망은 중국에 고도로 집중되어 있으며, 채굴 기반 공급은 환경·사회적 비용을 수반한다.
- **Content Roles**:
  - Primary: 중국의 글로벌 배터리 핵심광물 공급망 장악 구도(세계지도 Main Visual) + 이를 뒷받침하는 4개 정량 지표
  - Dependent: N/A
  - Shared Supporting: 채굴 산업의 환경부하·노동/인권 문제 서술 + 채굴폐기물 현장 사진(둘 이상의 상위 메시지—지정학적 집중, 환경·사회적 비용—를 함께 뒷받침)
  - Conclusion/Takeaway: N/A(문제 제기 단계, 결론은 이후 슬라이드에서 전개)
- **Relationship**: 기타·복합(지도 기반 Main Visual + 다중 정량 지표 + 서술형 근거)
- **Content Regions**: Main Visual Area(중국 강조 세계지도, img3) / Supporting Insight Area(4개 스탯: 전략광물 20개 중 19개 정제 1위·평균 점유율 70%·글로벌 블랙매스 처리 89%·니켈 1톤당 133톤 폐기물 + 환경부하/노동·인권 서술 + 채굴폐기물 현장 사진 1~2컷)
- **Selected Layout**: Visual + Insight Layout — Variant B(Chart + Insight), Layout Catalog L07 Market/Problem 대응 (`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: Main Visual(시장/공급망 구도를 보여주는 지도) + Supporting Insight(핵심 수치 해석·시사점) 2분할 구조에 정확히 부합. 3개 이상 대등 병렬 비교가 핵심은 아니므로 Three-Column/Comparison Matrix 제외 조건에 해당.
- **Structural Check**: 정보량이 다소 많음(지도+4스탯+서술+사진) — Supporting Insight Area 안에서 4스탯을 압축형(Large Number 소형 그리드)으로 배치하고 서술/사진은 그 아래 보조로 배치해 밀도를 관리하도록 [5]에 전달 필요. 출처 각주(IEA/Benchmark Mineral Intelligence/Earthworks) 반드시 유지.

---

## Slide 4. 북미 ESS 시장, 고성장의 변곡점

- **Core Message**: 북미 ESS(에너지저장장치) 시장은 에너지 용량(GWh) 기준 연평균 31.6% 성장이 전망된다.
- **Content Roles**:
  - Primary: CAGR 31.6% (Large Number, 단일 확인 수치)
  - Dependent: "북미 ESS 시장 성장 전망(에너지 용량 GWh 기준)"이라는 맥락 설명
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Main "Visual" Area(CAGR 31.6% Large Number를 핵심 주장으로 제시) / Supporting Insight Area(시장 맥락 설명 + 출처 각주)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message + Evidence), Layout Catalog L24 Message + Evidence 대응 (`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: 원본에 연도별 GWh 계열 데이터나 원본 차트 이미지가 없어(NC-01) Chart를 임의로 재구성할 수 없음 — Variant B(Chart+Insight) 대신, 확인된 단일 수치 자체를 핵심 주장(주 영역)으로 제시하고 근거(출처)로 뒷받침하는 Variant D가 적합. Content Visualization Freedom "원본에 없는 수치로 Chart 생성 금지" 원칙 준수.
- **Structural Check**: 콘텐츠량이 매우 적음(확인된 수치 1개) — Content Density 원칙에 따라 빈 공간을 억지로 채우지 않고 Large Number 중심의 압축형 배치를 유지하도록 [5]에 명시. **집중 Visual QA 대상(고정 Slide 4)**: 여백 처리가 부자연스러운 강제 분산(space-between 등)으로 이어지지 않는지 특히 확인 필요.

---

## Slide 5. 순환경제 비즈니스 모델

- **Core Message**: 코솔러스는 폐자원 회수 → 유해물질·온실가스 저감 → 재활용 기반 신공급망 구축이라는 세 축의 비즈니스 모델로 순환경제를 실현한다.
- **Content Roles**:
  - Primary: 3개 대등 메시지 — ① 폐자원 핵심광물 회수(원재료 수급 해결) ② 유해물질 억제·온실가스 감축(환경오염 저감) ③ 제조→재활용→제조 신공급망 구축
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(3개 메시지 자체가 결론적 구조)
- **Relationship**: 병렬
- **Content Regions**: 3개 병렬 Column(동일 Top Line·동일 Width) — 각 Column = Icon/짧은 제목 + 설명 문장
- **Selected Layout**: Three-Column Insight Layout (`docs/slide-design-rules/three-column/three-column.md`)
- **Layout Selection Reason**: 동일 위계의 독립적 핵심 메시지 3개를 병렬 제시하는 Use When 조건에 정확히 부합. 순차 프로세스나 시간 흐름이 아니며, 특정 항목이 나머지보다 현저히 중요하지도 않음.
- **Structural Check**: 문제 없음. 3개 항목의 정보량이 비교적 균등해 Column 간 불균형 우려 적음.

---

## Slide 6. 1세대 공정의 한계와 코솔러스의 솔루션

- **Core Message**: 1세대 재활용 공정은 낮은 선택성·불안정한 상분리·과다한 부산물 발생 등의 한계를 가지며, 코솔러스는 고성능 추출제(1.5세대, RECYION Series) 도입으로 이를 해결한다.
- **Content Roles**:
  - Primary: Before(1세대 공정의 한계) / After(코솔러스 1.5세대 추출제 솔루션 개요) — 대등한 두 상태의 전환
  - Dependent: 1세대 한계의 세부 항목(낮은 선택성, 제한된 동작 환경, 상분리 불안정, 부산물 과다) / 1.5세대 솔루션의 화학적 기반(기존 추출제 D2EHPA 대비 COSOLUS 추출제 RECYION)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "소재 및 공정 개선 필요" → 코솔러스 솔루션으로 연결
- **Relationship**: 비교(Before/After, 정확히 2개 상태 전환)
- **Content Regions**: Before Column(1세대 공정 한계 — 개념도 + 한계 서술) / After Column(코솔러스 1.5세대 추출제 개요 — 화학구조 비교)
- **Selected Layout**: Before + After Layout — Variant A(Process Transformation) (`docs/slide-design-rules/before-after/before-after.md`)
- **Layout Selection Reason**: 공정 단계 자체의 한계에서 솔루션으로의 전환(단계 수·구조 변화가 아니라 접근 방식 자체의 전환)이 핵심이며, 정량적 비교표보다 좌→우 Diagram+Arrow로 "한계 → 해결 방향"을 보여주는 것이 이 시점(개요 단계)에 적합. 정량적 상세 비교는 Slide 7/8에서 별도 전개.
- **Structural Check**: 이미지 라벨 신뢰도 주의 — B07의 img8(RECYION류 R기 일반형 추출제 화학구조식)은 D-test 사전 공지에서 라벨 오류 가능성이 제기된 이미지 중 하나이므로, [5] 생성 시 라벨 설명만 믿지 말고 `extracted_images/img8`, `img7`을 직접 열어 실제 내용(D2EHPA 구조식 vs RECYION 구조식 여부)을 확인 후 배치할 것. img60/61(1세대 공정 개념도)도 동일하게 실제 내용 확인 후 사용.

---

## Slide 7. 고성능 추출제 — 경쟁사 대비 공정 효율

- **Core Message**: COSOLUS 추출제는 벨기에 S사·중국 K사 대비 공정시간과 첨가제 사용량에서 압도적 우위를 갖는다.
- **Content Roles**:
  - Primary: 3개 대상(COSOLUS / 벨기에 S사 / 중국 K사) × 2개 비교 기준(공정시간, 첨가제 사용량)의 매트릭스
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(매트릭스 자체가 메시지)
- **Relationship**: 비교(3개 대상, 동일 기준 반복 비교)
- **Content Regions**: 비교 매트릭스 Region — 3개 대상 Column × 2개 기준 Row, COSOLUS Column 강조
- **Selected Layout**: Comparison Matrix Layout (`docs/slide-design-rules/comparison-matrix/comparison-matrix.md`)
- **Layout Selection Reason**: 비교 대상 3개(COSOLUS/벨기에 S사/중국 K사) × 동일 비교 기준(공정시간·첨가제) 반복 구조로, 자사(COSOLUS)를 강조하면서도 객관적 비교 구조를 유지해야 하는 Use When 조건에 정확히 부합.
- **Structural Check**: table_7의 공정시간 행은 원문에서 그래픽 처리되어 텍스트 추출이 안 되었고, 인접 문단과 첨가제 행의 대소 패턴(벨기에>중국) 교차검증으로 "벨기에 S사=COSOLUS 대비 100%↑, 중국 K사=50%↑"로 재구성됨(수치 자체는 원문 그대로, 배치만 재구성, 신뢰도 중간-높음) — [5] 생성 시 이 재구성 근거를 각주로 표기할지 검토. **집중 Visual QA 대상(고정 Slide 7)**: Comparison Matrix가 Table 성격이 강하므로 Table Style 규칙(Header Row Fill, Divider, Column 폭 고정 등) 적용 여부 확인 필요.

---

## Slide 8. 추출단수 저감이 만드는 CAPEX·OPEX 경제성

- **Core Message**: COSOLUS 추출제는 이론단수를 1단 저감(5단→4단)시켜 CAPEX·OPEX 양면에서 경제성을 확보한다.
- **Content Roles**:
  - Primary: Core Technology — "추출단수 1단 저감(COSOLUS 4단 vs 기존 5단, 20% 감소)"
  - Dependent: 2개 병렬 Quantified Impact — ① CAPEX 경제성(추출 효율 2~5% 개선) ② OPEX 경제성(망초 5% 이상 저감 → 연간 4,800톤 저감 사례)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(Impact 자체가 결론)
- **Relationship**: 인과(단수 저감 → 2개 정량 Impact)
- **Content Regions**: 상단 Core Technology 서술 / 좌우 병렬 Impact Region — CAPEX Impact(효율 개선 %) / OPEX Impact(망초 저감 %, 연간 4,800톤 Evidence) — 하단/우측에 table_8(추출단수·니켈 1톤당 망초양) Evidence
- **Selected Layout**: Benefit + Impact Layout (`docs/slide-design-rules/benefit-impact/benefit-impact.md`)
- **Layout Selection Reason**: 원문에 "추출단수 1단 저감 → CAPEX 경제성 확보" / "추출단수 1단 저감 → 망초 5% 이상 저감 → OPEX 경제성 확보"로 명시되어 있어, 하나의 Core Technology가 만드는 정확히 2개의 좌/우 정량 개선 효과를 Evidence와 함께 `Core Technology → Improvement → Quantified Impact` 흐름으로 제시하는 Use When 조건에 정확히 부합.
- **Structural Check**: table_8(항목/추출단수/니켈 1톤당 망초양) 완전 확인됨, 4,800톤 수치는 16,000톤×(3.6-3.3)톤 계산과 정합 확인됨 — 임의 수치 없음. 문제 없음.

---

## Slide 9. 직접리튬추출(DLE) — 재활용 공정 안에서 완성

- **Core Message**: 기존 DLE(증발법)는 단일 단계·낮은 회수율(3.12%)에 그치지만, 코솔러스는 NCM 스크랩에서 Mn·Co·Ni·Li을 순차 회수하는 4단계 공정 안에서 리튬까지 회수한다.
- **Content Roles**:
  - Primary: 코솔러스 4단계 공정 흐름 — 침출 → 불순물 제거 → (1)Mn 추출 → (2)Co 추출 → (3)Ni 추출 → (4)Li 추출 → 역추출
  - Dependent: 각 단계의 대상 금속
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 기존 DLE(증발법, 1단계, Li 회수율 3.12%)와의 대비 — 공정 전체 관점에서의 우위
- **Relationship**: 순차(공정 흐름) + 비교(기존 DLE 대비)
- **Content Regions**: 상단 Process Flow Region(코솔러스 4단계 순차 흐름) / 하단 Comparison Region(기존 DLE 증발법 1단계 vs 코솔러스 공정, 회수율 대비)
- **Selected Layout**: Process + Comparison Layout (`docs/slide-design-rules/process-comparison/process-comparison.md`)
- **Layout Selection Reason**: 단계별 공정 흐름(코솔러스 4단계)을 먼저 보여주고, 그 흐름과 직접 연결되는 기존 기술 비교(기존 DLE 증발법)를 같은 슬라이드 하단에서 함께 전달해야 하는 Use When 조건에 정확히 부합.
- **Structural Check**: 이미지 라벨 신뢰도 주의 — img9(칠레 아타카마 염호 리튬 채굴장, 기존 DLE 예시)와 img21(지열발전 연계 리튬 추출 플랜트)은 D-test 사전 공지에서 라벨 오류 가능성이 제기된 이미지이므로, [5] 생성 시 실제 파일을 열어 내용을 확인한 뒤 사용할 것(img21이 실제로 "기존 DLE" 예시로 적합한지, 혹은 다른 맥락 이미지인지 확인 필요).

---

## Slide 10. DLE 기술 동향 비교

- **Core Message**: DLE(직접리튬추출) 기술은 흡착제·추출제·분리막·전기화학 4개 방식으로 나뉘며, 각각 작동원리·기술성숙도(TRL)·장단점이 다르다.
- **Content Roles**:
  - Primary: 4개 방식(흡착제/추출제/분리막/전기화학) × 4개 비교 기준(작동원리/TRL/장점/단점)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(표 자체가 메시지, 코솔러스의 추출제-분리막 결합 방식의 포지셔닝은 다음 슬라이드에서 전개)
- **Relationship**: 비교(4개 대상, 동일 기준 반복)
- **Content Regions**: 표 Region — 4개 방식 Row × (작동원리/TRL/장점/단점) Column
- **Selected Layout**: Table Comparison Layout (`docs/slide-design-rules/table-comparison.md`)
- **Layout Selection Reason**: 4개 기술 방식을 동일 기준(작동원리·TRL·장단점)의 행으로 촘촘히 비교해야 하며, 각 셀이 짧은 기호가 아닌 서술형 텍스트(장단점 등)로 구성되어 Diagram형 자유 배치보다 표가 더 정확하고 신뢰도 있게 전달됨. 비교 항목(Column) 수가 많아 Card/Diagram형으로는 밀도 감당이 어려움.
- **Structural Check**: table_12 완전 확인됨(흡착제 TRL9 상용화단계 / 추출제·분리막 TRL4-5 / 전기화학 TRL3-4, 장단점 원문 그대로) — 임의 수치 없음. **집중 Visual QA 대상(고정 Slide 10)**: colgroup+table-layout:fixed로 동일 역할 Column 폭이 실제 고정되는지, 서술형 셀 텍스트가 한글 word-break:keep-all로 단어 중간에서 끊기지 않는지 우선 확인.

---

## Slide 11. DLE 핵심 경쟁력 — 추출제·분리막 결합 기술

- **Core Message**: 추출제와 분리막을 결합한 COSOLUS DLE 기술은 리튬 재자원화율을 3%에서 90% 이상으로 끌어올리고, 공정비용을 5,500원/kg 이하로 낮춘다.
- **Content Roles**:
  - Primary: COSOLUS DLE 핵심 성과(재자원화율 3%→90%, 공정비용 <5,500원/kg) — Large Number 중심 주장
  - Dependent: 성과를 뒷받침하는 기술 요인 분해 — 분리막&THz 기술(3%→90% 기여), 핵심소재(3%→50% 기여)
  - Shared Supporting: 추출제-분리막 결합의 4가지 Key Advantage(①빠른 물질전달 ②화학적 결합+공간적 분리로 우수한 재활용 효율 ③액상 공정 기반 연속운전 용이 ④분리막 기반 농축으로 첨가제 소모량 감소) — 성과 수치와 성과 요인 분해 양쪽을 함께 뒷받침
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합(핵심 주장 + 요인 분해 + 근거 나열)
- **Content Regions**: Main 주장 Area(재자원화율 3%→90%, 공정비용 <5,500원/kg Large Number) / Supporting Evidence Area(분리막&THz·핵심소재 기여도 + 4개 Key Advantage 목록)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message + Evidence), Layout Catalog L24 Message + Evidence 대응 (`docs/slide-design-rules/visual-insight/visual-insight.md`)
- **Layout Selection Reason**: 결론(핵심 성과 수치)을 먼저 제시하고 그 근거(구조적 강점 4가지, 기술 요소별 기여도)로 뒷받침하는 구조로, Variant D의 Use When("결론/주장을 먼저 던지고 그 근거로 뒷받침")에 부합. 재자원화율은 단일 정량 Benefit이 아니라 여러 근거가 함께 뒷받침하는 주장이므로 Benefit+Impact(정확히 2개의 좌우 병렬 Benefit 구조)보다 이 Layout이 더 적합.
- **Structural Check**: "*리튬선물 가격이 약 44,100천원/ton 수준일 때 재활용 목표 기준"이라는 전제 조건 각주를 반드시 함께 표기(원문 각주 누락 금지). 콘텐츠량(4 Key Advantage + 3개 수치)이 다소 많아 Supporting Evidence Area 안에서 밀도 관리 필요 — [5]에서 Key Advantage는 압축형 리스트로, 수치는 소형 Stat 그룹으로 분리 배치 권장.

---

## Slide 12. 친환경 차세대 배터리 재활용 공정(2세대)

- **Core Message**: 코솔러스 2세대 공정은 유도가열 → 전처리 → 블랙매스 생성 → 부유선별의 흐름으로 고순도 정제흑연과 코발트·니켈을 회수하며, 경제성·친환경성·양산성을 동시에 확보한다(폐흑연 처리 포함).
- **Content Roles**:
  - Primary: System/Process Title(친환경 차세대 배터리 재활용 공정) + Component 흐름 전체 — ①COSOLUS 유도가열 ②전처리 공정 ③블랙매스 생성(양극재용/음극재용) ④COSOLUS 부유선별
  - Dependent: 각 Component의 역할·짧은 설명
  - Shared Supporting: N/A
  - Conclusion/Takeaway: Insight/Output — "고순도 정제흑연 + 코발트·니켈 회수" 및 "경제성·친환경성·양산성 확보(폐흑연 처리 포함)"
- **Relationship**: 순차(공정 흐름)
- **Content Regions**: System/Process Title Region(상단) / 4개 Component Region(좌→우 수평 배열, Arrow로 연결) / Insight/Output Box(하단, 전체 Component 흐름을 종합)
- **Selected Layout**: Process / System Architecture Layout — **Layout A(이미지 없음)** (`docs/slide-design-rules/process-system-architecture-layout.md`)
- **Layout Selection Reason**: 공정 단계(유도가열→전처리→블랙매스→부유선별)를 `Component 01→02→03→04`처럼 좌→우 선형 구조로 순차 설명하고, 전체 흐름의 최종 Output(고순도 정제흑연/코발트·니켈 회수)을 하단에 정리해야 하는 Use When 조건에 정확히 부합 — 이번 D-test에서 신규 등록된 Layout이 실제로 선택된 사례. **Layout A/B 중 A를 선택한 이유**: 문서 §3.3 선택 우선순위에 따르면 "일부 단계에만 이미지가 있으면 임의로 빈 이미지 박스를 혼용하지 않는다"(규칙 2) 및 "전체 단계 중 사진 확보 비율이 80% 미만이면 기본적으로 Layout A를 선택한다"(규칙 3). 확보된 실사진(img62 COSOLUS 유도가열 설비, img63/64 유도가열 공정 중 촬영, img65 파일럿 라인 전경)은 모두 사실상 ①유도가열 단계 또는 전체 라인 전경에 해당하고, ②전처리 ③블랙매스 생성 ④부유선별 단계에 대응하는 사진은 확인되지 않아 4단계 중 1단계만 사진 확보(약 25%, 80% 미만) — 규칙에 따라 Layout A를 선택.
- **Structural Check**: 문제 없음(Component 수 4개, 권장 범위 3~6개 충족). img62~65는 이 슬라이드의 Component Box에 1:1로 강제 배정하지 않되, [5] 단계에서 공간이 허용되면 브랜드 진정성이 높은 실사진(img62/65 등)을 Insight Box 주변 보조 시각자료로 활용하는 것을 검토할 수 있음(단, Layout A 구조 자체를 임의로 변형하지 않는 범위에서). **집중 Visual QA 대상(신규 Layout 실사용)**: Component Group 간 동일 Width/동일 Top Line(Parallel Layout Alignment), Arrow 연결 위치, Insight Box 하단 배치가 문서 §5~§6 스펙대로 구현됐는지 확인 필요.

---

## Slide 13. 2세대 공정의 가격·기술 경쟁력

- **Core Message**: 코솔러스 2세대 공정(유도가열)은 기존 소성로(Pusher Kiln) 대비 압도적으로 짧은 공정시간·적은 에너지 투입과 함께, 고순도 재생흑연·낮은 부반응 등 기술적 우위를 갖는다.
- **Content Roles**:
  - Primary: 기존(Pusher Kiln) vs COSOLUS(2세대 유도가열) — 정확히 2개 대상의 다기준 비교
  - Dependent: 세부 비교 기준 — 공정시간(10시간 이상 vs 1분 이내), 승온 속도(200배 차이), 에너지 투입(432Wh/kg, 64% 절감), 흑연 순도(99% 이상), 부반응(낮음), 시설 투자비용, 온도 정밀도
  - Shared Supporting: Co 회수 순도 >95%, PCT 2건 출원(2세대 공정 전반의 기술 신뢰도 근거)
  - Conclusion/Takeaway: N/A(비교표 자체가 결론)
- **Relationship**: 비교(정확히 2개 대상, 다기준)
- **Content Regions**: Existing(Pusher Kiln) Column / COSOLUS(유도가열) Column — 동일 기준 Row로 병렬 비교(공정시간/승온속도/에너지투입/순도/부반응/투자비/온도정밀도) + 하단 보조 Evidence(Co 회수 순도, PCT 출원)
- **Selected Layout**: Before + After Layout — Variant B(Before/After Comparison Table) (`docs/slide-design-rules/before-after/before-after.md`)
- **Layout Selection Reason**: 비교 대상이 정확히 2개(기존 Pusher Kiln vs COSOLUS)이며, 공정시간·에너지·순도 등 동일 기준으로 "무엇이 얼마나 개선되는가"를 보여주는 것이 핵심이므로 Variant B(Comparison Table)의 Use When에 정확히 부합. 3개 이상 대상 비교가 아니므로 Comparison Matrix 제외.
- **Structural Check**: B19(경쟁력-솔루션2, 본문 전무)는 B18과 주제 중복으로 이 슬라이드에 통합됨(별도 슬라이드 생성하지 않음, material_analysis notes 반영).

---

## Slide 14. 투자 포인트

- **Core Message**: 코솔러스는 검증된 기술력과 구체적 사업화 방향을 바탕으로 Series A2 라운드 80억원 투자 유치를 추진한다.
- **Content Roles**:
  - Primary: 4개 병렬 항목 — [기술력] [사업화 방향] [투자라운드] [투자금 사용 계획]
  - Dependent: 각 항목의 세부 내용(예: 기술력 항목의 추출제/친환경 공정/Closed-loop 3개 세부 요소)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 투자라운드(Series A2, 80억원)가 사실상 이 슬라이드의 핵심 결론
- **Relationship**: 병렬(4개 대등 항목) + 그 중 하나(투자라운드)가 핵심 결론 성격
- **Content Regions**: 4개 병렬 Region([기술력]/[사업화 방향]/[투자라운드]/[투자금 사용 계획]) — 투자라운드(80억원)는 Large Number로 시각적 강조
- **Selected Layout**: Two-Column Summary, Layout Catalog L18 (`docs/layout-reference/2026.08.13_layout-catalog_V1.md`)
- **Layout Selection Reason**: Executive Summary/핵심 요약 목적에 부합하는 L18을 기본 후보로 선택하되, 4개 항목이 대등하게 병렬 나열되는 구조라 2×2 그리드(또는 4-Column) 배치로 재해석 — 이 정보 구조에 맞는 전용 콘텐츠 구조별 특수 Layout Reference가 없어(Three-Column은 3개 항목 전제, 4개 항목과 불일치) L01~L33 카탈로그에서 목적이 가장 근접한 L18을 선택 후 카탈로그 사용 규칙("적합한 구조가 없을 때만 기존 레이아웃을 조합·최소 변형")에 따라 4-Region 그리드로 최소 변형.
- **Structural Check**: 원문에 실명이 마스킹된 "XX하이텍", "XX코", "XX자동차"는 마스킹 그대로 유지하고 임의로 실명을 채우지 않음(B21 notes). 투자금액(80억원)은 원문 확정 수치 그대로. **집중 Visual QA 대상(고정 Slide 14)**: 4개 Region 병렬 배치 시 Parallel Layout Alignment(동일 Top Line·동일 폭) 준수 여부, 항목별 정보량 불균형(특히 [투자금 사용 계획] 2줄 vs 다른 항목) 여부 확인.

---

## Slide 15. 일본·인도네시아 시장 진출

- **Core Message**: 코솔러스는 5억 명 이상 아시아 경제권을 겨냥해 일본과 인도네시아를 전략적 거점으로 세계시장 진출을 추진한다.
- **Content Roles**:
  - Primary: 목표(일본·인도네시아를 전략 거점으로 5억 명 이상 아시아 경제권 성장)
  - Dependent: 국가별 논의 현황 — 인도네시아(전기자전거 업체 1대주주와 투자 논의), 일본(현지투자사·재료업체 등과 투자 논의)
  - Shared Supporting: 관련 생태계 이미지/로고(인도네시아 e-모빌리티·행사 실사진, SWAP/MUKTI/eCoNiL/IBC/HLI 로고, 일본 Panasonic Energy/Iwatani/DNP 로고)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(일본 vs 인도네시아, 2개 거점)
- **Content Regions**: 상단 목표 서술 / 좌우 병렬 Region — 인도네시아 Region(논의 현황 + 실사진/로고) / 일본 Region(논의 현황 + 로고)
- **Selected Layout**: Symmetric Two-Split, Layout Catalog L25 (`docs/layout-reference/2026.08.13_layout-catalog_V1.md`)
- **Layout Selection Reason**: 두 국가(일본/인도네시아)가 대등한 위계로 병렬 제시되는 구조로 "Two topics with equal hierarchy"에 부합. 전용 콘텐츠 구조별 특수 Layout Reference 중 이 구조(2개 대등 지역 거점 + 이미지/로고 근거)에 정확히 맞는 문서가 없어 L01~L33에서 선택.
- **Structural Check**: NC-04(일본 기업 로고 매칭 불확실) 반영 — Panasonic Energy/Iwatani/DNP 로고는 "일본 현지투자사·재료업체 등과 투자 논의 중"이라는 익명 표현과 구체적으로 매칭되는지 원문에서 확인 불가하므로, 사용 시 특정 파트너십을 단정하는 문구 없이 "일본 배터리·소재 생태계" 맥락 이미지로만 배치. img71~75(SWAP/MUKTI/eCoNiL/IBC/HLI 로고)는 D-test 사전 공지에서 라벨 오류 가능성이 제기된 이미지 그룹에 포함되므로, [5] 생성 시 실제 파일을 열어 내용을 확인한 뒤 배치할 것.

---

## 신규 Layout 사용 총평

- **Process / System Architecture Layout** (`process-system-architecture-layout.md`): **Slide 12에서 실제 사용됨**(Layout A 변형, 사진 확보 비율 부족으로 이미지 없는 버전 선택). 콘텐츠(2세대 재활용 공정의 좌→우 순차 Component 흐름 + 하단 Output/Insight)가 Use When 조건에 정확히 부합해 자연스럽게 채택.
- **Product / Application Layout** (`product-application-layout.md`): **미사용**. 이번 15장 콘텐츠 중 "하나의 중심 제품이 여러 적용처로 확장되는 Hub-and-Spoke" 또는 "대표 제품 → 복수 적용 사례" 구조에 해당하는 원본 콘텐츠 묶음이 없음(코솔러스 자료는 기술/공정 단계 설명, 정량 비교, 시장 진출 논의 현황 중심이며 "제품→적용처" 관계로 정리된 콘텐츠가 확인되지 않음). Use When 조건에 억지로 끼워 맞추지 않고 미사용으로 판단.
