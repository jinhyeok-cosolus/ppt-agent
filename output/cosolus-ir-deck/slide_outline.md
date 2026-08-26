# COSOLUS IR Deck — Slide Outline

- 목표 슬라이드 수: **15장** (사용자 지정값, 임의 변경 금지)
- 원본 콘텐츠: `material_analysis.json`의 콘텐츠 묶음 B01~B22 (B19·B20은 본문 콘텐츠가 없어 각각 B18·B02로 흡수, 그 외 22개 묶음은 아래처럼 15장으로 재구성)
- 청중: 고객사/외부 청중 · 언어: 한국어 · 발표시간: 20분 내외
- 레이아웃 우선순위: Hard Rule > Claude PPT Design System > Content Visualization Freedom > (콘텐츠 구조별 특수 Layout Reference 우선, 없으면) Layout Catalog(L01~L33)
- `[확인필요]` 표기 대상: NC-01(CAGR 31.6% 외 시계열 없음), NC-02(솔루션1-1 경쟁력 매트릭스 원본 배치 유실), NC-03(조직구성 본문 없음), NC-04(일본 파트너 로고-텍스트 매칭 불확실) — 상세는 `material_analysis.json`의 `needs_confirmation` 참조.

---

## Slide 1. 표지

- **Core Message**: COSOLUS — 지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술 (모토: Small actions, BIG DIFFERENCE)
- **Content Roles**:
  - Primary: 회사 모토 + 발표 제목(B01 확정 텍스트)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Brand Block(좌상단, Sub Message+CI) / Main Title(중앙, "지속가능한 배터리 재활용을 위한 화학소재 및 친환경 차세대 공정기술") / Full-bleed Background Image
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: 표지 슬라이드는 Hard Rule에 따라 항상 이 문서를 우선 적용. 배경 이미지는 Soft Rules 우선순위(사용자 제공 없음 → `docs/brand-assets/cover-images/` 중 주제 적합 이미지)에 따라 `표지 이미지_1.png`(시험관 클로즈업, 화학소재 R&D 톤) 또는 `이미지_3.png`(공정/설비 연구원) 후보 중 화학소재·공정기술을 동시에 다루는 본 발표 주제에 맞춰 web-ppt-generator 단계에서 최종 선택.
- **Structural Check**: 문제 없음. 표지는 페이지 번호 없음(Hard Rule).

---

## Slide 2. 기업소개

- **Core Message**: 코솔러스는 첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제를 선도하는 회사다.
- **Content Roles**:
  - Primary: 회사 기본정보(기업명/대표자/임직원/소재지/비전) — B02 table_1
  - Dependent: 핵심 메시지 "첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제 선도"(Main Title Supporting Message)
  - Shared Supporting: 우측 이미지(img2, 실험실 글러브박스 작업 실사진)
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠(정보 나열)
- **Content Regions**: 좌측 Main Content(Company Facts: 기업명/대표자/임직원 27명/소재지 4곳/비전) / 우측 세로 Image Region(img2)
- **Selected Layout**: `02_instruction_design_V1.md` (Company Introduction)
- **Layout Selection Reason**: Use When 조건(기업명/대표자/임직원/소재지/비전 등 기본정보를 외부 청중에게 전달) 정확히 충족.
- **Structural Check**: 문제 없음. B20(조직구성) 본문이 원문에 전무(NC-03)하므로 별도 조직도 슬라이드를 만들지 않고, 이미 확정된 임직원 27명·소재지 4곳 정보만 이 슬라이드에 반영 — 조직 인원 구성(부서/직책)까지 있는 것처럼 과장하지 않는다.

---

## Slide 3. 배경 — 왜 지금, 배터리 재활용인가

- **Core Message**: 배터리 밸류체인의 환경·지정학적 리스크가 커지는 동시에, 북미 ESS 시장이 빠르게 성장하며 재활용 수요가 확대되고 있다.
- **Content Roles**:
  - Primary: (병렬 2개) ① 환경·지정학적 요인 4개 수치(전략광물 20개 중 19개 정제 1위, 정제 평균 점유율 70%, 블랙매스 처리 89%, 니켈 1톤당 133톤 폐기물) ② 북미 ESS 시장 CAGR 31.6%
  - Dependent: ①에는 중국 강조 세계지도(img3) 및 출처(IEA 등), ②에는 출처(SNE Research 등)
  - Shared Supporting: N/A (두 Primary가 각각 독립적인 출처·수치를 가짐)
  - Conclusion/Takeaway: N/A (다음 슬라이드의 비즈니스 모델로 자연스럽게 이어짐, 이 슬라이드에서 결론 강제하지 않음)
- **Relationship**: 병렬(2개의 독립적 배경 요인)
- **Content Regions**: 좌측 Region(환경·지정학적 요인 — 4개 수치 + 세계지도) / 우측 Region(산업적 요인 — CAGR 31.6% 단일 스탯 + 문맥 설명)
- **Selected Layout**: Layout Catalog `L07. Market / Problem` (2개 병렬 Background 요인을 좌우 Region으로 구성 — Visual+Insight의 Variant B 톤을 두 Region에 각각 적용하되, 동일 위계의 두 요인을 나열하는 구조라 특정 2-대상 비교 전용 Layout이 아닌 일반 Market/Problem 카탈로그를 기반으로 자유 구성)
- **Layout Selection Reason**: 두 요인은 대립하는 Before/After가 아니고, 정확히 3개도 아니므로 Three-Column·Before-After 조건에 해당하지 않음. Content Visualization Freedom에 따라 병렬 배경 설명이 목적일 때 Market/Problem 계열이 적합.
- **Structural Check**: 우측(산업적 요인) 정보량이 좌측(환경적 요인 4개 수치)보다 현저히 적음(NC-01, 시계열 데이터 없음) — 균형을 맞추기 위해 임의로 막대그래프를 만들지 않고, 우측은 CAGR 31.6%를 Large Number로 강조 + 배경 설명 문장으로 시각적 밀도를 보완하는 방식으로 처리(웹PPT 단계에서 좌우 Visual Weight를 텍스트/스탯 크기로 조정, 가짜 수치로 채우지 않음).

---

## Slide 4. 비즈니스 모델

- **Core Message**: 폐자원 기반 핵심광물 확보 → 환경오염 저감 → 제조-재활용-제조 순환 공급망 구축이라는 3가지 축으로 사업을 정의한다.
- **Content Roles**:
  - Primary: 3개 병렬 메시지 — ① 폐자원으로부터 핵심 광물 확보(원재료 수요부족 해결) ② 유해물질 억제·온실가스 감축(환경 오염 저감) ③ 제조→재활용→제조 재활용 기반 新공급망 구축
  - Dependent: N/A (원문에 각 메시지를 뒷받침하는 세부 수치 없음)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(대등한 위계의 3개 독립 메시지)
- **Content Regions**: Column 1(자원 확보) / Column 2(환경 저감) / Column 3(신공급망)
- **Selected Layout**: `three-column/three-column.md`
- **Layout Selection Reason**: Use When "핵심 경쟁력 또는 특징 3가지를 설명할 때"에 정확히 부합. 3개 항목이 순차 프로세스가 아니라 대등한 사업 철학 3축이므로 Do Not Use 조건에 해당하지 않음.
- **Structural Check**: 문제 없음. 각 Column의 Main Visual은 원문에 세부 수치·이미지가 없으므로 Icon+Message(개념 아이콘) 방식으로 구성 예정(콘텐츠에 없는 수치를 임의로 만들지 않음).

---

## Slide 5. 기존 재활용 공정의 한계

- **Core Message**: 1세대 재활용 공정은 낮은 선택성·제한된 동작 환경·상분리 불안정·부산물 과다발생 등의 한계로 소재·공정 개선이 필요하다.
- **Content Roles**:
  - Primary: 1세대 공정 흐름(개념)
  - Dependent: 4개 한계점(낮은 선택성 / 제한된 동작 환경(pH 등) / 상분리 불안정 / 부산물 과다발생(망초 등))
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "소재 및 공정 개선 필요" — 4개 한계가 수렴하는 결론
- **Relationship**: 인과(공정 → 한계 → 개선 필요)
- **Content Regions**: 상단(1세대 공정 Process Flow, 이미지 자산 img60/61 활용 검토) / 하단(4개 Limitation → Improvement Need 수렴 구조)
- **Selected Layout**: `process-comparison/process-comparison.md`
- **Layout Selection Reason**: Use When "소재/공정의 현재 한계와 개선 필요성을 한 장에서 설명할 때"에 정확히 부합. §6.2 "Multiple Limitations to One Direction" 구조(4개 Limitation → 1개 Improvement Need) 적용.
- **Structural Check**: 문제 없음. 하단 4개 한계는 독립적으로 이해 가능하도록 구분하고 개선 방향(소재·공정 개선 필요)으로 수렴시킴.

---

## Slide 6. 솔루션1 개요 — 고성능 추출제(1.5세대 화학소재)

- **Core Message**: 기존 추출제(1세대, 예: D2EHPA) 대비 코솔러스 RECYION Series(1.5세대)는 재활용 효율을 개선한다.
- **Content Roles**:
  - Primary: (2개 대비) 기존 추출제 vs COSOLUS 추출제(RECYION Series)
  - Dependent: 기존 추출제 예시 D2EHPA 화학구조식(img7), COSOLUS 추출제 R기 일반형 구조식(img8)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "재활용 효율 개선"
- **Relationship**: 비교(기존 1개 vs 개선 1개)
- **Content Regions**: Existing Column(기존 추출제 D2EHPA, 광산·염호 기반 금속회수용 추출제 + 구조식) / Improved Column(COSOLUS RECYION Series + 구조식)
- **Selected Layout**: `before-after/before-after.md` — **Variant A (Process Transformation)**
- **Layout Selection Reason**: 비교 대상이 기존/개선 정확히 2개이며, 공정 단계 수 변화보다는 두 화학소재(이미지) 자체의 직접 비교가 핵심 메시지 — Variant A의 Main Visual 유형을 "Image ↔ Image"(화학구조식)로 적용(Process/Step Sequence 조건부 규칙은 미적용, Comparison Frame만 적용).
- **Structural Check**: 문제 없음. 원문에 구체적 수치가 없어 "재활용 효율 개선"이라는 정성적 결론만 사용하고 임의 수치를 추가하지 않음.

---

## Slide 7. 핵심기술 — 고성능 추출제 성능·원가 경쟁력

- **Core Message**: RECYION 추출제는 경쟁사 대비 공정시간·첨가제 사용량이 적고, 기존 세대 대비 추출단수를 1단 줄여 CAPEX·OPEX 경제성을 확보한다.
- **Content Roles**:
  - Primary: 3사 비교(COSOLUS / 벨기에 S사 / 중국 K사) — 공정시간·첨가제 사용량 (table_7 재구성, B08)
  - Dependent: 이론단수 비교(기존 5단 vs COSOLUS 4단, 20% 감소) 및 니켈 1톤당 망초 발생량(기존 3.6톤 vs COSOLUS 3.3톤) — table_8, B09
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "대한민국 배터리 재활용 업체 연간 니켈 16,000톤 생산 기준, COSOLUS 추출제로 망초 4,800톤/년 저감 가능" — Highlight Band
- **Relationship**: 비교(3개 대상) + 종속(단수·망초 수치가 CAPEX/OPEX 결론을 뒷받침)
- **Content Regions**: 상단 Table(구분: 공정시간·첨가제 사용량 / 대상: COSOLUS·벨기에 S사·중국 K사, COSOLUS 열 강조) / 하단 Highlight Band(이론단수 4단·20%↓, 연간 망초 4,800톤 저감, CAPEX/OPEX 경제성 확보)
- **Selected Layout**: `table-comparison.md` (Variant A, Data Comparison Table) + `019_competitive-advantage-highlight.md`의 자사 열 강조 패턴을 COSOLUS 열에 적용
- **Layout Selection Reason**: 비교 대상이 3개(COSOLUS/벨기에/중국)이고 동일 기준(공정시간/첨가제 사용량)을 반복 비교 — Table Comparison Use When에 부합. Benefit+Impact는 "여러 경쟁 대상을 동일 기준으로 비교"하는 경우 Do Not Use로 명시되어 있어 제외. 하단 Highlight Band(table-comparison.md §3의 Footnote/Highlight Band 영역)로 B09의 CAPEX/OPEX 결론을 표 전체 결론으로 통합.
- **Structural Check**: table_7의 공정시간 행은 원본 셀이 그래픽으로 처리되어 있어 인접 문단 텍스트로 재구성한 값임(NC 아님, material_analysis.json B08 기록 참고, 수치 자체는 원문 그대로: 벨기에 100%↑/중국 50%↑). "기존 추출제"(B09, 5단/3.6톤)는 3사 비교 표와 별도 축(세대 비교)이므로 같은 표에 억지로 4번째 열로 합치지 않고 Highlight Band 문장으로 분리해 정보 왜곡을 방지.

---

## Slide 8. 솔루션1-2 — 직접 리튬 추출(DLE)

- **Core Message**: 기존 DLE(증발법, 1단계, Li 회수 3.12%)와 달리 COSOLUS는 침출-불순물제거-Mn/Co/Ni추출-역추출의 4단계 추출 후 재활용 공정을 사용한다.
- **Content Roles**:
  - Primary: (2개 대비) 기존 DLE(증발법) vs COSOLUS 추출 후 재활용(4단계: Mn추출→Co추출→Ni추출→역추출)
  - Dependent: 아타카마 염호 항공사진(img9, 기존 증발법 예시), 지열 리튬 추출 플랜트 실사진(img21)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(다음 슬라이드의 기술 동향 비교로 이어짐)
- **Relationship**: 비교(기존 1개 vs 개선 1개), 공정 단계 자체가 핵심
- **Content Regions**: Existing Column(기존 DLE 증발법, 1단계, Li 회수 3.12%) / Improved Column(COSOLUS 4단계: 침출→불순물제거→Mn/Co/Ni추출→역추출)
- **Selected Layout**: `before-after/before-after.md` — **Variant A (Process Transformation)**
- **Layout Selection Reason**: "어떤 단계가 어떻게 줄어드는가/구성되는가"가 핵심이 아니라 정확히는 "1단계(단순 증발) vs 4단계(다단 정제 추출)"라는 공정 구조 자체의 차이가 메시지 핵심 — Variant A 정확히 부합. Main Visual은 Process/Step Sequence.
- **Structural Check**: 문제 없음. 단계 수 표시(1단계 vs 4단계)를 Comparison Marker Pair로 명확히 대비.

---

## Slide 9. DLE 기술 동향 비교

- **Core Message**: 리튬 추출 기술은 흡착제·추출제·분리막·전기화학 4가지 방식이 있으며, 각각 작동원리·기술성숙도(TRL)·장단점이 다르다.
- **Content Roles**:
  - Primary: 4개 기술(흡착제/추출제/분리막/전기화학) × 4개 비교기준(작동원리/TRL/장점/단점) — table_12, 완전 확인됨
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A(다음 슬라이드에서 COSOLUS가 추출제+분리막 방식을 결합한 강점으로 이어짐)
- **Relationship**: 비교(4개 대상, 동일 기준 반복)
- **Content Regions**: 단일 Table(4열: 흡착제/추출제/분리막/전기화학 × 4행: 작동원리/TRL/장점/단점)
- **Selected Layout**: `table-comparison.md` (Variant A, Data Comparison Table)
- **Layout Selection Reason**: 비교 대상 4개, 동일 기준 반복 비교, 텍스트 밀도가 높아 표 형태가 Diagram보다 정확 — Table Comparison Use When에 정확히 부합. Multi-Radar는 "정량 데이터/평가 점수"가 있을 때 조건인데 본 데이터는 TRL(정성 등급)+장단점(서술형)이라 정확한 수치를 그대로 읽어야 하는 Table이 더 적합(Multi-Radar Do Not Use 조건: "정성 설명·항목별 주석이 많아 정확한 수치를 그대로 읽어야 할 때 → Table 유지").
- **Structural Check**: 4행 모두 텍스트 분량이 있어 Row 높이를 콘텐츠 기준으로 배분(균등 고정 아님). COSOLUS 자사 강조는 이 슬라이드에서는 특정 열이 자사가 아니므로(범주 비교) 적용하지 않음 — 다음 슬라이드에서 COSOLUS가 추출제+분리막 결합임을 설명.

---

## Slide 10. COSOLUS DLE의 핵심 강점과 성과

- **Core Message**: 추출제-분리막 결합 구조의 4가지 강점을 바탕으로, 분리막&THz 기술은 리튬 재자원화율을 3%→90%로, 핵심소재 기술은 3%→50%로 끌어올린다.
- **Content Roles**:
  - Primary: (정확히 2개 정량 효과) ① 분리막&THz 기술 → 재자원화율 3%→90% ② 핵심소재 기술 → 재자원화율 3%→50%
  - Dependent: 4가지 핵심 강점(①빠른 물질전달 ②화학적 결합+공간적 분리로 우수한 재활용 효율 ③액상 공정 연속운전 용이 ④분리막 기반 농축으로 첨가제 소모량 감소) — Core Technology 설명으로 상단 배치
  - Shared Supporting: 공정비용 <5,500원/kg (리튬선물가격 약 44,100천원/ton 기준)
  - Conclusion/Takeaway: "COSOLUS 화학구조 설계·정제·공정 기술 → 재자원화율 >90%, 공정비용 <5,500원/kg"
- **Relationship**: 인과(강점 → 정량 성과) + 병렬(정확히 2개 효과)
- **Content Regions**: 상단(Core Technology, B13의 4개 강점 요약) / 좌우 Benefit Area(분리막&THz: 3%→90% / 핵심소재: 3%→50%), 각각 Evidence로 Before/After 수치 시각화
- **Selected Layout**: `benefit-impact/benefit-impact.md`
- **Layout Selection Reason**: "하나의 기술이 만드는 정확히 2개의 정량적 개선 효과"(재자원화율 90%/50%)를 Core Technology → Improvement → Quantified Impact 흐름으로 제시 — Use When에 정확히 부합. Header는 두 Benefit의 주제(분리막&THz / 핵심소재)가 서로 다른 기술 축이므로 분할 Header(기본값) 적용.
- **Structural Check**: 문제 없음. `*리튬선물 가격 약 44,100천원/ton 기준`은 Footnote로 작게 표기.

---

## Slide 11. 솔루션2 개요 — 친환경 차세대 배터리 재활용 공정기술(2세대)

- **Core Message**: 기존 공정(1세대: 유도가열/부유선별/건식환원)과 달리 COSOLUS(2세대)는 경제성·친환경성·양산성을 확보한 통합 공정을 구현한다.
- **Content Roles**:
  - Primary: (2개 대비) 기존공정(1세대) vs COSOLUS(2세대)
  - Dependent: 기존공정 흐름(유도가열→부유선별→건식환원, 양극재/음극재용 블랙매스 → 재활용 양극재/고순도 정제흑연/코발트/니켈), COSOLUS 2세대 동일 산출물 + 폐흑연 처리
  - Shared Supporting: COSOLUS 실제 설비 실사진(img62~65)
  - Conclusion/Takeaway: "경제성·친환경성·양산성 확보"
- **Relationship**: 비교(기존 1개 vs 개선 1개), 공정 단계 자체가 핵심
- **Content Regions**: Existing Column(1세대 공정 흐름 Diagram) / Improved Column(COSOLUS 2세대 공정 흐름 Diagram + 실제 설비 사진)
- **Selected Layout**: `before-after/before-after.md` — **Variant A (Process Transformation)**
- **Layout Selection Reason**: 두 공정의 단계 구성 자체(유도가열/부유선별/건식환원 경로 vs COSOLUS 통합 경로)가 핵심 메시지 — Variant A 부합. Main Visual은 Process/Diagram이며, 실사진(img62~65)은 §4.9 Result/Output Visual로 COSOLUS측에 보완 배치(실제 자산 존재 시에만 사용 원칙 충족).
- **Structural Check**: 문제 없음. 원문에 정량 비교 수치가 없어(정성적 "경제성·친환경성·양산성 확보"만 존재) 임의 수치를 추가하지 않음 — 정량 비교는 다음 슬라이드(솔루션2 경쟁력)에서 다룸.

---

## Slide 12. 핵심기술 — 유도가열·부유선별 공정과 코발트 회수

- **Core Message**: COSOLUS 유도가열-부유선별 공정을 거쳐 건식환원으로 코발트(또는 니켈)를 순도 95% 이상으로 회수한다(PCT 2건 출원).
- **Content Roles**:
  - Primary: COSOLUS 공정 흐름(유도가열 → 전처리 → 블랙매스(양극재용/음극재용) → 부유선별 → 고순도 정제흑연 / 코발트·니켈)
  - Dependent: 건식환원에 의한 코발트(니켈) 회수, 순도 >95%
  - Shared Supporting: 실제 COSOLUS 설비 실사진(img62~65, 유도가열 장비 및 파일럿 라인)
  - Conclusion/Takeaway: "Co 회수 순도 >95%, PCT 2건 출원"
- **Relationship**: 순차(공정 흐름) + 인과(공정 → 회수 성과)
- **Content Regions**: 상단(Process Flow: 유도가열→전처리→부유선별, 실사진 활용) / 하단(코발트 회수 순도 >95%, PCT 2건 출원 — Insight/결과)
- **Selected Layout**: `process-comparison/process-comparison.md`
- **Layout Selection Reason**: 단계별 공정 흐름을 먼저 보여주고 그 흐름에서 도출되는 성과(코발트 회수 순도)를 하단에서 연결 — Use When "여러 단계의 공정이 하단의 핵심 Insight와 직접 연결될 때"에 부합.
- **Structural Check**: 문제 없음. 상단 Process Visual에 실제 COSOLUS 설비 사진을 우선 사용(Content Visualization Freedom의 이미지 자산 우선 활용 원칙 — 실제 자사 설비 사진이 있으므로 일반 아이콘보다 우선).

---

## Slide 13. 경쟁력 — 가격·기술 우위

- **Core Message**: 기존 소성로(Pusher Kiln) 대비 COSOLUS 공정은 공정시간·에너지 투입을 크게 줄이면서도 더 높은 순도의 재생흑연을 얻는다.
- **Content Roles**:
  - Primary: (2개 대비) 기존 소성로(Pusher Kiln) vs COSOLUS
  - Dependent: 가격경쟁력(공정시간 1분 이내·200배 빠른 승온속도, 에너지 432Wh/kg·64% 절감), 기술경쟁력(재생흑연 순도 99% 이상, 균일한 온도분포, 낮은 부반응)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "PCT 2건 출원" (가격·기술 경쟁력을 모두 뒷받침하는 공통 근거)
  - 원문 B19(경쟁력-솔루션2, 별도 제목만 존재)는 본 슬라이드에 흡수 — 중복 제목이며 본문 없음
- **Relationship**: 비교(기존 1개 vs 개선 1개), 여러 기준으로 개선 정도 제시
- **Content Regions**: Criteria Column(공정시간/승온속도/에너지투입/재생흑연 순도/온도분포/부반응/시설투자비용) × Existing(기존 소성로) / Improved(COSOLUS) 2개 Column
- **Selected Layout**: `before-after/before-after.md` — **Variant B (Before/After Comparison Table)**
- **Layout Selection Reason**: "기존 대비 무엇이 얼마나 개선되는가"를 다수의 동일 기준(공정시간/에너지/순도 등)으로 보여주는 것이 핵심 — Variant B에 정확히 부합. 비교 대상이 정확히 2개(기존 소성로 vs COSOLUS)뿐이며 3개 이상 경쟁사 비교가 아니므로 Comparison Matrix/Table Comparison보다 Before-After Variant B가 적합.
- **Structural Check**: 비교 기준이 6~7개로 Variant B 권장 범위(3~6개) 상한에 가까움 — 우선순위가 낮은 기준(예: 온도 정밀도)은 상위 기준에 통합해 5~6개로 조정 검토(웹PPT 단계 반영 필요). **주의(설계 시 명시적으로 배제)**: `019_competitive-advantage-highlight.md`가 기술하는 "COSOLUS vs BTR vs Vianode" 3사 비교는 본 프로젝트 원본 자료(B18/B19)에 해당 경쟁사명·구체 수치가 confirm되지 않으므로 그대로 가져오지 않는다 — 원본에 있는 "기존 소성로(Pusher Kiln)" 대비 비교만 사용하고, 자사 열 강조 "패턴"(형식 차이로 강조, 카드 승격 등)만 참고한다.

---

## Slide 14. 투자포인트

- **Core Message**: 최상위 수준의 추출제·친환경 공정 기술력을 바탕으로 1.5세대(PoC)와 2세대(신공급망·해외진출) 사업화를 추진하며, Series A2로 80억원 투자를 유치해 해외법인 설립과 공장 건설에 투입한다.
- **Content Roles**:
  - Primary: (2개 병렬 섹션) ① 기술력+사업화 방향 ② 투자라운드+투자금 사용계획
  - Dependent: 기술력 3항목(추출제 합성·정제 기술 / 친환경 공정기술 / Closed-loop system), 사업화 방향 2항목(1.5세대 PoC 진행 중, 2세대 신공급망+해외진출)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "Series A2, 목표 투자유치 80억원"
- **Relationship**: 종합(Executive Summary — 여러 앞선 슬라이드 내용의 요약 + 신규 정보(투자라운드))
- **Content Regions**: 좌측(기술력 + 사업화 방향) / 우측(투자라운드 + 투자금 사용계획)
- **Selected Layout**: Layout Catalog `L18. Two-Column Summary`
- **Layout Selection Reason**: Executive Summary/overview/key takeaways 목적에 정확히 부합하는 카탈로그 항목. 좌우 2개의 대등한 섹션(기술·사업 요약 vs 투자 정보)으로 자연스럽게 나뉨.
- **Structural Check**: 문제 없음. 원문에 "XX하이텍", "XX코", "XX자동차"로 마스킹된 실명은 그대로 마스킹 유지(임의로 실명을 채우지 않음).

---

## Slide 15. 세계시장 진출

- **Core Message**: 일본과 인도네시아를 전략적 거점으로 5억 명 이상의 아시아 경제권 진출을 추진하며, 양 지역에서 투자 논의가 진행 중이다.
- **Content Roles**:
  - Primary: 목표(일본·인도네시아 거점, 아시아 경제권 5억 명 이상)
  - Dependent: 진행 현황 2건(인도네시아 전기자전거 업체 1대주주와 투자논의 중 / 일본 현지투자사·재료업체 등과 투자논의 중)
  - Shared Supporting: 인도네시아 e모빌리티·배터리 생태계 로고(SWAP/MUKTI/eCoNiL/IBC/HLI) 및 실사진(img43/44)
  - Conclusion/Takeaway: N/A(마지막 정보 슬라이드로 목표·진행현황 자체가 결론)
- **Relationship**: 전체-부분(하나의 목표 아래 두 지역 진행현황)
- **Content Regions**: 상단(목표 Statement) / 하단(2개 지역 카드: 인도네시아 진행현황+로고·사진, 일본 진행현황)
- **Selected Layout**: Layout Catalog `L21. Customer References / Proof`
- **Layout Selection Reason**: Customers/partners/PoC 성격의 로고·진행현황 나열에 적합. Timeline/Milestone Layout은 "시간축 자체가 정보의 핵심 구조"일 때 우선 적용 대상인데, 본 슬라이드는 연도별 시점이 아니라 현재 진행 중인 두 지역 현황 나열이라 제외.
- **Structural Check**: NC-04에 따라 일본 기업 로고(Panasonic Energy/Iwatani/DNP)는 원문의 "일본 현지투자사·재료업체 등"이라는 익명 표현과 특정 매칭이 확인되지 않으므로 **사용하지 않는다** — 대신 인도네시아 측은 원문 맥락과 정합적인 로고(SWAP/MUKTI/eCoNiL/IBC/HLI)와 실사진만 사용하고, 일본 측은 텍스트 설명만으로 구성해 확정되지 않은 파트너십을 암시하지 않는다.

---

## 요약 — 원본 콘텐츠 묶음(B01~B22) → 슬라이드 매핑

| 슬라이드 | 원본 콘텐츠 묶음 |
|---|---|
| 1 | B01 |
| 2 | B02 + B20(임직원/소재지 사실만) |
| 3 | B03 + B04 |
| 4 | B05 |
| 5 | B06 |
| 6 | B07 |
| 7 | B08 + B09 |
| 8 | B11 |
| 9 | B12 |
| 10 | B13 + B14 |
| 11 | B15 |
| 12 | B16 + B17 |
| 13 | B18 (+ B19 제목만 흡수) |
| 14 | B21 |
| 15 | B22 |

B10(솔루션1-1 경쟁력 매트릭스, 원본 배치 유실 NC-02)은 별도 슬라이드로 만들지 않고 Slide 7의 정량 데이터로 대체.
