# slide_outline.md — 기술개발_지원사업_연구개발계획서

> 근거: `material_analysis.json` (1차 소스: `2026.08.25_...프롬프트_V1.docx`, 교차확인: `..._내용정리_V1.docx`)
> 대상 청중: 정부/심사위원 · 언어: 한국어 · 발표시간: 15~20분 · 목표 슬라이드 수: 약 20장
> 사용자 지시: 5개년 로드맵은 1개년당 1슬라이드(총 5슬라이드)로 분리. 본문 축약은 허용하되 수치·핵심주장은 원본 그대로 유지.
> 총 슬라이드 수: **21장** (목표 20장 대비 +1 — 로드맵 5분할 지시 반영 결과. 그 외 섹션은 원본 문서 순서를 따르되 컨소시엄 소개·기대효과/확장계획 등 일부를 통합해 슬라이드 수를 최소화함)
> 레이아웃 판단은 `.claude/skills/web-ppt-generator/references/design-rules.md`의 우선순위(Hard Rule > Claude PPT Design System > Content Visualization Freedom > Layout Reference)를 따름. 표지는 `01_cover_design_V2.md`를 우선 적용.

---

## Slide 1. 표지 (Cover)

- **Core Message**: 전자잉크(E-Ink) 디스플레이용 고기능성 UV경화형 봉지소재 개발 — 기술개발 지원사업 연구개발계획서
- **Content Roles**: N/A (표지 전용 규칙 적용, Content Role 분류 대상 아님)
- **Relationship**: N/A
- **Content Regions**: Brand Block(좌측 상단, CI+모토) / Main Title(중앙, "전자잉크 디스플레이용 고기능성 UV경화형 봉지소재 개발") / (선택) 부제 "기술개발 지원사업 연구개발계획서"
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: 표지 슬라이드이므로 표지 전용 규칙을 최우선 적용
- **Structural Check**: 문제 없음. 배경 이미지는 `docs/brand-assets/cover-images/`에서 디스플레이·전자소재 기술 주제에 맞는 이미지를 [5] 단계에서 선정(없으면 브랜드 컬러 단색 대체) — 본 단계에서는 이미지 자체를 확정하지 않음

---

## Slide 2. 목차

- **Core Message**: 발표 구성 안내 (배경·필요성 → 기술 → 5개년 로드맵 → 경쟁력·사업화·기대효과)
- **Content Roles**: Primary: 섹션 목록(약 6~7개 그룹) / Dependent: N/A / Shared Supporting: N/A / Conclusion: N/A
- **Relationship**: 병렬
- **Content Regions**: 단일 Region — 섹션 그룹 목록(예: 01 과제개요·컨소시엄 / 02 시장·기술배경 / 03 개발솔루션·핵심기술 / 04 정량목표·역할 / 05 5개년 로드맵 / 06 경쟁력·사업화·기대효과)
- **Selected Layout**: L02 (Contents/Section)
- **Layout Selection Reason**: 카탈로그 용도가 "Navigation/chapter transition"으로 목차 슬라이드에 정확히 대응
- **Structural Check**: 문제 없음. 21개 슬라이드를 6개 내외 그룹으로 묶어 나열, 개별 슬라이드 제목을 모두 나열하지 않음(정보 과다 방지)

---

## Slide 3. 과제 개요

- **Core Message**: 열경화 방식의 한계(TACT 증가, Warpage)를 UV경화형 단일층 봉지소재로 해결하여 200kg 양산 검증까지 추진
- **Content Roles**:
  - Primary: 과제명, 개발 목적(공정 TACT 단축, 기판 Warpage 개선)
  - Dependent: 핵심 성능 5개(저투습/고접착/저수축/높은 경화율/장기 신뢰성), 최종 단계(200kg 양산 검증과 고객사 적용)
  - Shared Supporting: 주관기관(소니드)·공동 연구역량(생기원, 코솔러스) 소속 정보
  - Conclusion/Takeaway: N/A (요약 성격의 슬라이드 자체가 개요이므로 별도 Conclusion 불필요)
- **Relationship**: 전체-부분
- **Content Regions**: Region A(Primary, 과제명+개발목적) / Region B(Dependent, 핵심성능 5개 — 압축형 Visual, Key Term 나열) / Supporting Region(공통, 주관/공동기관 배지형 표기)
- **Selected Layout**: L18 (Two-Column Summary)
- **Layout Selection Reason**: "Executive summary/overview/key takeaways" 용도에 부합 — 과제 개요는 여러 요약 정보를 균형 있게 배치해야 하는 Overview 성격
- **Structural Check**: 문제 없음. 핵심성능 5개는 압축형 Visual(Key Term Tag 등)로 배치해 텍스트 밀도를 낮추는 것을 권장

---

## Slide 4. 컨소시엄 구성 및 보유역량

- **Core Message**: 소니드(주관)·한국생산기술연구원·코솔러스 3개 기관이 각자의 전문 역량을 결합한 컨소시엄
- **Content Roles**:
  - Primary: 3개 기관(대등한 병렬 Primary Content 묶음) — 소니드/한국생산기술연구원/코솔러스
  - Dependent: 각 기관의 보유역량·실적(기관별 2~3개 사실)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A(소니드) / Region B(한국생산기술연구원) / Region C(코솔러스) — 3개 병렬 Region, 각 Region 내부에 기관명(Primary)+역량 bullet(Dependent)
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: "동일·유사 위계의 독립적 핵심 메시지·근거·특징 3개를 병렬적으로 제시할 때"에 정확히 부합(3개 기관이 대등한 위계)
- **Structural Check**: 문제 없음. 3개 Region의 정보량이 대체로 균형(소니드·생기원 각 2개 사실, 코솔러스 1개 사실)이나 코솔러스 항목이 상대적으로 짧음 — Column 폭은 동일 유지하고 내부 여백으로만 조정(Content Difference 처리 원칙)

---

## Slide 5. 시장 및 산업 배경

- **Core Message**: 매장 자동화·재고관리 자동화 수요 확대로 글로벌 ESL 시장이 가파르게 성장 중(2023년 1.6조원 → 2028년 4.3조원, CAGR 15~17%)
- **Content Roles**:
  - Primary: ESL 확대 배경(좌) / 글로벌 시장 전망(우) — 대등한 병렬 Primary
  - Dependent: 좌측 4개 bullet(원본 다이어그램 포함), 우측 시장규모 수치+원본 차트 이미지
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "클라우드 기반 매장 운영 자동화 → 글로벌 ESL 수요 확대" (하단 통합 인사이트 문장)
- **Relationship**: 병렬
- **Content Regions**: Region A(좌, ESL 확대배경 — 면적점유형 Visual: img_market_intro + bullet 4개) / Region B(우, 글로벌시장전망 — 면적점유형 Visual: img_market_chart(원본) + 수치 3개) / 하단 Integrated Conclusion(인사이트 문장, 전체 폭 기준 배치)
- **Selected Layout**: L25 (Symmetric Two-Split)
- **Layout Selection Reason**: 원본 문서가 명시적으로 "좌우 2개 컬럼 구조" 지시, 두 주제(확대배경/시장전망)가 대등한 위계 — "Two topics with equal hierarchy"에 정확히 부합
- **Structural Check**: 문제 없음. 우측 차트는 원본 이미지(img_market_chart, USD 표기)를 그대로 재사용하고 본문 수치(원화)는 텍스트로 병기 — Content Visualization Freedom의 "완성된 원본 Graph 우선 재사용" 원칙 준수, 임의 재구성 금지

---

## Slide 6. 제품 적용 구조

- **Core Message**: 개발 봉지소재는 E-Ink 표시소자 가장자리(Edge Glue)에 단일층으로 적용되어 수분·열·먼지로부터 내부 소재를 보호
- **Content Roles**:
  - Primary: 원본 단면도(img_product_cross_section) — 면적점유형 Main Visual
  - Dependent: 적용위치/기판/보호대상/보호기능 설명 bullet
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "단일층으로 E-Ink를 보호해야 하므로 고기능성이 요구됨"
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Main Visual Region(원본 단면도) + Explanation Region(적용구조 설명, Dependent)
- **Selected Layout**: Visual + Insight Layout — Variant A(Image+Explanation)
- **Layout Selection Reason**: "대표 이미지를 중심으로 보여주고 반대 영역에서 그 의미를 설명"하는 구조에 정확히 부합, 하나의 중심 이미지(제품구조도)와 설명 텍스트로 구성된 전형적 사례
- **Structural Check**: 문제 없음. 문서 내 동일 도면이 2회 등장하나 1개만 사용

---

## Slide 7. 기존 기술의 문제

- **Core Message**: E-Ink는 수분·먼지·열에 취약해 봉지소재가 필수이나, 기존 열경화 방식은 긴 경화시간과 Warpage 문제를 동시에 안고 있음
- **Content Roles**:
  - Primary: 긴 경화시간(좌) / Warpage 발생(우) — 대등한 병렬 Primary
  - Dependent: 각 문제의 원인·결과 bullet(2개씩)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A (다음 슬라이드 "개발 필요성"으로 이어지는 전개상 별도 결론 불필요)
- **Relationship**: 병렬
- **Content Regions**: Region A(긴 경화시간) / Region B(Warpage 발생) — 2개 병렬 Region, 각 Region 내부 Title(Primary)+원인/결과 bullet(Dependent)
- **Selected Layout**: L25 (Symmetric Two-Split)
- **Layout Selection Reason**: 2개의 대등한 문제를 병렬 제시 — "Two topics with equal hierarchy"에 부합. Three-Column은 항목 3개 기준이라 부적합, Before/After는 기존→개선 비교 구조가 아니므로(이 슬라이드는 문제 정의에 한정) 부적합
- **Structural Check**: 문제 없음(항목당 bullet 2개로 정보량 균형). 각 Region 내용이 상대적으로 짧아 시각적으로 여백이 남을 수 있음 — [5] 단계에서 아이콘 등 보조 요소로 균형 보완 검토 가능(단, 장식 목적의 임의 요소 추가는 금지)

---

## Slide 8. 개발 필요성

- **Core Message**: 해외기업 중심의 ESL 봉지소재 시장에서 국내 E-Ink 소재시장 진입 기반을 확보해야 함
- **Content Roles**:
  - Primary: "국내 E-Ink 소재시장 진입 기반 확보" 주장(Claim)
  - Dependent: N/A
  - Shared Supporting: 경쟁구도(BOE/JABIL/E-Ink Holdings/Innolux, 중국·독일 기업 주도, Henkel 등 경쟁 심화) + 진입장벽(국내 산업 양극화, 개발비용 증가) + 기회요인(미개척 신규시장, 소니드 선행실적) — 7개 bullet 전체가 하나의 Claim을 뒷받침하는 공통 근거군
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합 (단일 주장 + 다면적 근거)
- **Content Regions**: Claim Region(상단, 핵심 주장 1줄) + Evidence Region(하단, 근거 bullet — 경쟁구도/진입장벽/기회요인 3개 소그룹으로 묶어 배치)
- **Selected Layout**: L19 (Claim & Proof)
- **Layout Selection Reason**: "Strength/differentiator supported by evidence" — 하나의 핵심 주장을 다수 근거로 뒷받침하는 구조에 부합
- **Structural Check**: 근거 bullet 7개는 단일 Region에 담기에 다소 많음 — [5] 단계에서 경쟁구도/진입장벽/기회요인 3개 소그룹(Content Group)으로 묶어 간격 차등 배치하고, 문장을 핵심 키워드 중심으로 축약 권장(수치·고유명사는 원본 유지)

---

## Slide 9. 개발 솔루션

- **Core Message**: 열경화 방식을 UV경화형 소재로 전환하여 기존 공정의 한계를 개선
- **Content Roles**:
  - Primary: "열경화 → UV경화형 소재 전환" 주장(Claim)
  - Dependent: N/A
  - Shared Supporting: 개발 방향 4개(UV경화 전환, 저WVTR 소재, 난부착 기판용 고접착 소재, 공정조건 최적화) + 적용정보(위치/기판/보호기능)
  - Conclusion/Takeaway: N/A
- **Relationship**: 기타·복합
- **Content Regions**: Claim Region(상단) + Evidence Region(하단, 개발방향 4개 — 대등한 병렬 소항목)
- **Selected Layout**: L19 (Claim & Proof)
- **Layout Selection Reason**: 슬라이드 7과 동일하게 단일 주장 + 근거형 구조. Before/After Layout은 정량적 전후 비교값이 아직 제시되지 않는 단계(정량목표는 별도 슬라이드)라 부적합하다고 판단
- **Structural Check**: 문제 없음(bullet 4개, 균형적 분량)

---

## Slide 10. 핵심 기술 구성

- **Core Message**: 3개 기관이 각자의 핵심기술 영역(봉지재 조성/저투습 고분자/고접착 올리고머)을 담당해 하나의 솔루션을 완성
- **Content Roles**:
  - Primary: 3개 기관의 핵심기술(대등한 병렬) — UV경화형 봉지재 기술(소니드) / 저투습 하이브리드 고분자 기술(생기원) / 고접착 우레탄 아크릴레이트 기술(코솔러스)
  - Dependent: 각 기술의 세부 개발 항목(기관당 4개 bullet)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(기관별) — 각 Region 내 기술명(Primary)+세부항목(Dependent)
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 3개 기관의 대등한 핵심기술을 병렬 제시 — Use When 조건에 정확히 부합
- **Structural Check**: 기관당 bullet 4개씩(총 12개)로 정보량이 많은 편 — [5] 단계에서 기관별로 가장 핵심적인 2~3개 항목만 남기고 나머지는 문장 압축(불필요한 세부 반응조건 등은 축약) 권장. 수치·화학구조 관련 핵심 주장은 임의 삭제하지 않음

---

## Slide 11. 정량적 개발 목표

- **Core Message**: 성능뿐 아니라 양산 재현성과 저장 안정성까지 확보하는 것이 목표
- **Content Roles**:
  - Primary: 성능 목표 / 신뢰성·양산 목표 / 정량적 성과 목표 — 대등한 병렬 3개 그룹(원본 문서가 "3컬럼 구조"로 명시)
  - Dependent: 각 그룹 내 세부 수치 항목
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A(성능목표, 6개 수치) / Region B(신뢰성·양산목표, 5개 수치) / Region C(정량적 성과목표, 5개 수치)
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 원본 문서 명시적 지시("3컬럼 구조")와 3개 그룹의 대등한 위계 모두 Three-Column Use When에 부합
- **Structural Check**: 3개 Region 항목 수가 5~6개로 균형적. Region B의 "양산성 평가(소재)"/"양산성 평가(제품)" 항목은 원본에서 한 줄에 결합되어 있어 [5] 단계에서 별도 줄로 분리해 가독성 확보 권장(수치 자체는 변경 없음)

---

## Slide 12. 기관별 역할 및 협력 흐름

- **Core Message**: 생기원·코솔러스가 소재를 개발하고 소니드가 조성물 적용·신뢰성 평가를 거쳐 코솔러스가 스케일업, 소니드가 최종 양산·판매하는 순차 협력 구조
- **Content Roles**:
  - Primary: 4단계 흐름(생기원·코솔러스 소재개발 → 소니드 적용/평가 → 코솔러스 스케일업 → 소니드 양산/판매) — 순차 Primary
  - Dependent: N/A
  - Shared Supporting: 기관별 역할 표(3행 — 소니드/생기원/코솔러스의 역할 요약, 흐름 전체를 뒷받침하는 공통 참조 자료)
  - Conclusion/Takeaway: "세 기관이 소재 개발부터 제품화·양산까지 단계별 역할을 분담"
- **Relationship**: 순차
- **Content Regions**: Flow Region(상단, 4단계 좌→우 순차 Process) + Supporting Region(하단, 기관별 역할 표 — 특정 단계에 종속시키지 않고 공통 참조 자료로 별도 배치)
- **Selected Layout**: Process / System Architecture Layout
- **Layout Selection Reason**: "공정 단계, 시스템 구성요소, 기술/데이터 전달 흐름을 Component01→02→...처럼 좌→우 순차 설명하고 최종 Output을 하단에 정리"하는 구조에 부합. 이미지 유무에 따라 Layout A(이미지 없음) 적용
- **Structural Check**: 문제 없음. 표(3행)는 순차 Flow의 보조 자료로만 사용해 Flow가 시각적으로 종속되지 않도록 유지

---

## Slide 13. 5개년 개발 로드맵 — 1차년도

- **Core Message**: 1차년도는 선행개발 기반의 UV경화형 봉지재 개발, 도포 시스템 구축, 3개 기관의 기초 소재 설계·합성에 집중
- **Content Roles**:
  - Primary: 소니드(도포시스템 구축·IP-R&D) / 한국생산기술연구원(PSQ 고분자 설계) / 코솔러스(우레탄 아크릴레이트 올리고머 설계) — 대등한 병렬 3개 기관
  - Dependent: 각 기관별 세부 개발 항목(3~4개 bullet)
  - Shared Supporting: 원본 1년차 로드맵 다이어그램(img_roadmap_y1 — 3개 기관 활동을 하나의 도식으로 종합)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(기관별, Primary+Dependent) + Supporting Region(원본 다이어그램, 3개 Region과 분리된 공통 시각자료)
- **Selected Layout**: Three-Column Insight Layout (+ 원본 다이어그램을 Shared Supporting Visual로 결합)
- **Layout Selection Reason**: 3개 기관의 대등한 병렬 활동 구조가 핵심이므로 Three-Column Use When에 부합. Timeline/Milestone Layout은 한 슬라이드에 여러 시점을 나열하는 구조라 "1개년당 1슬라이드" 지시와 맞지 않아 제외
- **Structural Check**: 원본 다이어그램(면적점유형 Visual)과 3개 기관 텍스트를 함께 배치하면 밀도가 높음 — [5] 단계에서 각 기관 bullet을 3개 내외로 축약하고 다이어그램 크기를 콘텐츠 밀도에 맞게 조정 권장(수치·기술 주장 임의 삭제 금지)

---

## Slide 14. 5개년 개발 로드맵 — 2차년도

- **Core Message**: 2차년도는 1차년도 장비를 활용한 조성물 개발·ESL Damage 평가와 함께 가교 구조 형성을 통한 접착력 고도화에 집중
- **Content Roles**:
  - Primary: 소니드(고부착력 저WVTR 조성물 개발) / 한국생산기술연구원(dual-curing 코팅소재) / 코솔러스(3차원 가교구조 형성) — 대등한 병렬 3개 기관
  - Dependent: 각 기관별 세부 개발 항목(3~5개 bullet)
  - Shared Supporting: 원본 2년차 로드맵 다이어그램(img_roadmap_y2)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(기관별) + Supporting Region(원본 다이어그램)
- **Selected Layout**: Three-Column Insight Layout (+ 원본 다이어그램 Shared Supporting Visual)
- **Layout Selection Reason**: 슬라이드 13과 동일한 논리(3개 기관 대등 병렬)
- **Structural Check**: 소니드 항목이 5개 bullet로 다른 두 기관(각 3개)보다 많음 — Column 폭은 동일 유지하고 내부 문장 압축으로 균형 조정 권장(Content Difference 처리 원칙, 수치·핵심주장 유지)

---

## Slide 15. 5개년 개발 로드맵 — 3차년도

- **Core Message**: 3차년도는 첨가제 적용 평가와 2D 나노입자 기반 필러 소재 개발, 폴리올 2종 도입 공중합체 설계로 성능을 고도화
- **Content Roles**:
  - Primary: 소니드(첨가제 적용·신뢰성 재현성 평가) / 한국생산기술연구원(2D 나노 필러 소재) / 코솔러스(폴리올 2종 공중합체 설계) — 대등한 병렬 3개 기관
  - Dependent: 각 기관별 세부 개발 항목(3개 bullet)
  - Shared Supporting: 원본 3년차 로드맵 다이어그램(img_roadmap_y3)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(기관별) + Supporting Region(원본 다이어그램)
- **Selected Layout**: Three-Column Insight Layout (+ 원본 다이어그램 Shared Supporting Visual)
- **Layout Selection Reason**: 슬라이드 13·14와 동일한 논리 — Deck 전체에서 로드맵 5슬라이드는 동일 레이아웃 계열 유지(카탈로그 사용 원칙: "동일 유형 슬라이드는 가능한 한 동일 계열 유지")
- **Structural Check**: 3개 기관 bullet 수가 균등(각 3개) — 문제 없음

---

## Slide 16. 5개년 개발 로드맵 — 4차년도

- **Core Message**: 4차년도는 E-paper Flexible 시장 대응(Polyimide 기판 적용)과 내굴곡·저투습 특성 동시 확보, 가교 구조 최적화에 집중
- **Content Roles**:
  - Primary: 소니드(Flexible 시장 대응 봉지재) / 한국생산기술연구원(내굴곡·저투습 코팅소재) / 코솔러스(가교첨가제 도입 최적화) — 대등한 병렬 3개 기관
  - Dependent: 각 기관별 세부 개발 항목(2~3개 bullet)
  - Shared Supporting: 원본 4년차 로드맵 다이어그램(img_roadmap_y4 — Modulus/Creep Test 그래프, 제품 실물사진 포함)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(기관별) + Supporting Region(원본 다이어그램)
- **Selected Layout**: Three-Column Insight Layout (+ 원본 다이어그램 Shared Supporting Visual)
- **Layout Selection Reason**: 슬라이드 13~15와 동일한 논리
- **Structural Check**: 문제 없음(3개 기관 bullet 수 균형). 원본 다이어그램에 이미 정량 그래프(Modulus/Creep Test)가 포함되어 있으므로 별도 수치를 새로 만들지 않고 원본 그래프 이미지를 그대로 사용

---

## Slide 17. 5개년 개발 로드맵 — 5차년도

- **Core Message**: 5차년도는 최종 조성물을 확정해 200kg 규모 양산 신뢰성 평가를 완료하고 코솔러스 양산 기술이전까지 완수
- **Content Roles**:
  - Primary: 소니드(200kg 양산 규모 신뢰성 평가) / 한국생산기술연구원(양산 스케일 기술이전·최적화) / 코솔러스(양산화 기술 확보, 파일럿·양산 합성기 제작) — 대등한 병렬 3개 기관
  - Dependent: 각 기관별 세부 항목(1~3개 bullet)
  - Shared Supporting: N/A (원본 도식 없음)
  - Conclusion/Takeaway: "5개년 로드맵의 최종 목표 — 200kg 양산 규모 신뢰성 확보"(압축형 Key Stat으로 강조 가능)
- **Relationship**: 병렬
- **Content Regions**: Region A/B/C(기관별) + Conclusion Region(200kg 양산 목표를 Key Stat으로 강조, 전체 Region 하단 통합 배치)
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 슬라이드 13~16과 동일한 레이아웃 계열 유지. 원본 도식이 없어 Shared Supporting Visual 없이 텍스트+Key Stat 중심으로 구성
- **Structural Check**: 다른 4개 로드맵 슬라이드 대비 텍스트 분량이 적어 상대적으로 여백이 클 수 있음 — [5] 단계에서 "200kg 양산 검증"을 Large Number/Key Stat으로 시각적으로 강조해 균형 보완 권장(자료 없는 도식을 임의로 새로 만들지 않음 — material-analysis 원칙 준수)

---

## Slide 18. 선행개발 실적

> **[7] 피드백 반영 (2026-08-25)**: Human Review ② 피드백에 따라 전면 재구성. 기존 "3개 기관 병렬 역량 + 상단 공통 실적" 구조를 폐기하고, "고객사 평가 결과가 드러낸 문제(좌)"와 "본 과제의 개선 방향(우)"을 대비시키는 좌우 2-Column 구조로 교체한다. 3개 기관별 보유역량 나열은 이 슬라이드에서 제거(기관 역량 자체는 Slide 4/10에서 이미 다룸) — 이 슬라이드는 "왜 이 과제가 필요한가(선행개발에서 드러난 한계)"와 "그래서 무엇을 개선하는가"에 집중한다.

> **[7] 피드백 반영 Round 2 (2026-08-25)**: Human Review ②에서 3가지 추가 수정 지시. (1) 상단 핵심 문장은 "헤더박스에 삽입하는 강조 내용이 아니라 부제목"이라는 사용자 정정에 따라 `.claim-box`(강조 박스) 대신 **Hard Rule §12 Main Title Supporting Message**(`.support-msg`, 20pt, Main Title 아래·Main Content 위, Content Start Y가 §12 규칙대로 아래로 확장 — `.body-box.with-support`)로 구현 방식을 교체(문구·역할 자체는 유지). (2) 좌측 3단계 마일스톤 문구를 축약하고, 배지 사이 화살표(↓)를 얇은 세로선(1px 이내, 팔레트 내 `--c-primary`)으로, 배지 크기를 31px→26px로 축소. (3) "장기 신뢰성 평가 결과" `.result-panel` 박스(제목행+24pt 강조 숫자+pill+세부 2행)를 완전히 제거하고 본문과 동일한 16pt 텍스트 한 줄("240시간 기준 미충족 → 개선필요")로 대체 — 세부 근거(목표조건/주요현상/판단)는 슬라이드에서 생략.

> **[7] 피드백 반영 Round 3 (2026-08-25)**: Human Review ②에서 2가지 추가 수정 지시. (1) Round 2에서 도입한 배지 간 얇은 세로선(`.ms-connector::before`, width:1px)이 "일직선 구현이 안 되는 것 같다"는 피드백에 따라 완전히 제거하고, 다운 화살표(↓)로 복원하되 기존(14pt)보다 눈에 띄게 키움(20pt, 색상은 기존 `--c-primary` 팔레트 유지) — `scripts/qa_render.py` 스크린샷으로 가시성 확인. (2) "장기 신뢰성 평가 결과"가 한 줄("240시간 기준 미충족 → 개선필요")로는 텍스트 칸이 부족하다는 피드백에 따라 3개 문장으로 확장: "장기신뢰성 평가결과: 60℃·1,000시간 목표에서 240시간 시점 Fail. 개선필요" / "주요현상: Edge Mura 및 표시소자 변색 발생" / "적용 가능성은 확인했으나 장기 신뢰성 개선 필요". 박스/카드 없이 순수 텍스트 유지, 폰트 크기는 본문 기준 16pt 그대로 유지(임의 확대 금지). 핵심 결론 1문장만 Bold+Primary Color로 강조(1행 강조 허용 원칙 유지, "Fail" 단어만 별도로 거대하게 키우지 않음)하고 나머지 2문장은 일반 본문 톤(400 weight, `--c-ink`)으로 낮춰 좌측 컬럼이 과도하게 무거워지지 않도록 함. 텍스트 블록 확장에 따라 `.ms-list` 앞 margin-top(20px→그대로) 및 `.ms-result-block` margin-top을 10px→8px로 소폭 축소해 좌측 컬럼 높이 여유를 확보했으며, `scripts/qa_render.py --audit-fonts` 결과 모든 텍스트 16pt 이상·overflow 없음을 확인함(v4).

- **Core Message**: 고객사 평가 결과, 240시간 이후 발생한 신뢰성 문제의 개선이 상용화의 핵심 과제로 확인
- **Content Roles**:
  - Primary: 고객사 평가 및 확인 결과(좌, 3단계 평가 경과 + 장기 신뢰성 평가 결과 한 줄 요약) / 본 과제의 개선 방향(우, 2개 개선 항목) — 대등한 병렬 Primary 2개
  - Dependent: 좌측 — 3단계 평가 경과 각 단계 축약 설명("01 고객 수요 확인 — 열경화 공정 문제 및 UV 전환 요구" / "02 시제품 평가 — 1차 시제품 5종 고객평가" / "03 개선제품 평가 — Edge Mura 개선제품 6종 추가 발송"), 장기 신뢰성 평가 결과는 박스 없이 본문(16pt)과 동일 크기의 텍스트 3문장("장기신뢰성 평가결과: 60℃·1,000시간 목표에서 240시간 시점 Fail. 개선필요" / "주요현상: Edge Mura 및 표시소자 변색 발생" / "적용 가능성은 확인했으나 장기 신뢰성 개선 필요")으로 표기(Round 3, 핵심 결론 1문장만 Bold+Primary 강조) / 우측 — 개선 항목 2개 각각의 sub-bullet 3개(변경 없음)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: **Main Title Supporting Message**(Hard Rule §12, `.support-msg`, 20pt)로 배치 — "고객사 평가 결과, 240시간 이후 발생한 신뢰성 문제의 개선이 상용화의 핵심 과제로 확인"(좌측 문제와 우측 해결방향을 잇는 통합 메시지이므로 Main Title 바로 아래·Main Content 위, 전체 폭 배치). Round 1에서는 이를 강조 박스(`.claim-box`)로 구현했으나, Round 2에서 "이 문장은 헤더박스 삽입용 강조 문구가 아니라 부제목"이라는 사용자 정정에 따라 Hard Rule §12 표준 부제목 컴포넌트로 교체
- **Relationship**: 비교 (문제 확인 ↔ 개선 방향의 대비 구조 — 두 Region이 동일 위계로 병렬 배치되되, 내용 성격은 "확인된 한계" vs "해결 접근"으로 대비됨)
- **Content Regions**: 상단 Main Title Supporting Message(Hard Rule §12, 전체 폭, 부제목) + Region A(좌, "고객사 평가 및 확인 결과" — 3단계 마일스톤 Primary + 장기 신뢰성 평가 결과 텍스트 한 줄) + Region B(우, "본 과제의 개선 방향" — 서브카피 + 개선 항목 2개, 각 Dependent sub-bullet 3개)
- **Selected Layout**: L25 Symmetric Two-Split 재해석 (Before/After 계열 Variant B는 기각 — 사유는 아래 Layout Selection Reason 참조)
- **Layout Selection Reason**: 좌/우가 "기존 대비 개선 수치"를 동일 기준(Row)으로 나열하는 Before/After Comparison Table(Variant B)이 아니며, 공정 단계 자체가 달라지는 Process Transformation(Variant A)도 아니다 — 좌측은 "평가 이력과 그 결과 드러난 한계", 우측은 "그 한계에 대응하는 개발 방향"으로 정보 성격이 다른 대등한 두 Primary Topic의 병렬 배치이므로 `before-after.md`의 Do Not Use When("Process 흐름 없이 속성만 비교")에 해당하지 않으면서도 Variant A/B 어느 쪽 구조에도 맞지 않는다. 반면 이 Deck에서 이미 검증된 Symmetric Two-Split(Slide 5/7/19/20, `.sym-wrap`/`.sym-col`/`region-header rh-parallel`/`.v-divider` 컴포넌트)의 "동일 위계 두 주제 병렬" 구조가 그대로 부합하므로 이를 재해석해 적용한다. 좌측 내부의 3단계 경과는 Claude PPT Design System §6이 원칙적으로 지양하는 "원형 Step/숫자 아이콘의 Process Stage 기본 사용"에 해당하지 않는다 — 전체 슬라이드의 Main Visual이 아니라 좌측 Region 내부의 압축된 이력 요약(Compressed Visual)이며, 사용자가 Human Review ②에서 이 시각 언어(circle badge+연결선)를 명시적으로 요청한 1회성 예외로 처리(design-rules.md 본문에는 반영하지 않음, [9] 대상 아님)
- **Structural Check**: 좌측(3단계 이력 + 결과 3문장)과 우측(서브카피 + 2개 항목×3 sub-bullet)의 정보량이 유사하게 균형(Parallel Layout Alignment 원칙의 동일 Top Line·동일 Width 적용). "장기 신뢰성 평가 결과"는 Round 3에서 한 줄 요약이 텍스트 칸 부족 피드백을 받아 3문장으로 확장됐으나, Stat Number(24pt) 강조는 다시 넣지 않고 본문과 동일한 16pt 텍스트를 유지(가독성을 위해 핵심 결론 1문장만 Bold+Primary Color, 나머지 2문장은 일반 톤 — 좌측 컬럼이 과도하게 무거워지지 않도록 함, Hard Rule §5 Color Usage 범위 내). 텍스트 3줄 확장 후에도 `.body-box.with-support`(top:210px, height:446px) 안에서 overflow 없이 들어감을 `qa_render.py` 스크린샷·font-audit으로 확인(v4). 배지 간 연결은 Round 2의 얇은 세로선을 Round 3에서 폐기하고 20pt 다운 화살표(↓)로 복원(팔레트 내 `--c-primary` 유지). Main Title Supporting Message 추가로 Content Start Y가 §12 규칙(`.body-box.with-support`, 지역창업계획패키지 사업계획서 v3에서 이미 검증된 동일 Hard Rule §12 구현값 재사용)에 따라 아래로 조정됨에 맞춰 좌우 2-Column 영역 높이·정렬도 함께 재조정. 원본 수치(60℃·1,000시간 목표, 240시간, Edge Mura)는 변경 없이 그대로 유지

---

## Slide 19. 사업화 전략

- **Core Message**: 대만 글로벌 고객사 검증을 시작으로 소재 기술이전·스케일업·양산 공급체계를 단계적으로 구축
- **Content Roles**:
  - Primary: 기술이전·공급 흐름(생기원 개발소재 → 코솔러스 기술이전·스케일업 → 소니드 양산·판매) — 순차 Primary
  - Dependent: 3단계 판매확대 전략(1차 대만 선두 수요기업 → 2차 기존 열경화재 대체/신규모델 → 3차 국내 ESL 업체 확대)
  - Shared Supporting: 대만 고객사 검증 현황(NDA, 제품평가 이력), 목표 시점(3차년도 신뢰성 평가 승인, 2028년 매출 발생), 판매처 다양화·IP 확보 계획
  - Conclusion/Takeaway: N/A (다음 슬라이드 "기대효과"로 연결)
- **Relationship**: 순차
- **Content Regions**: Flow Region(상단, 기술이전·공급 흐름 — 원본 다이어그램 img_biz_flow 활용) + Dependent Region(판매확대 3단계, Flow에 종속) + Supporting Region(검증현황·목표시점 등 공통 맥락 정보)
- **Selected Layout**: Process / System Architecture Layout
- **Layout Selection Reason**: 기술이전→스케일업→양산이라는 좌→우 순차 흐름이 핵심이며, 원본 다이어그램(COSOLUS/KITECH→SONID→BOE 등)이 이미 이 구조를 시각화하고 있어 Use When 조건에 부합
- **Structural Check**: 원본 bullet이 10개로 매우 많음 — [5] 단계에서 (1) 기술이전 흐름, (2) 3단계 판매확대, (3) 기타 추진사항(판매처 다양화, IP 확보)의 3개 Content Group으로 재편해 압축 권장. 특허법무법인 협의 등 부차적 내용은 우선순위를 낮추거나 축약(핵심 수치·시점 2026년/2028년은 유지)

---

## Slide 20. 기대효과 및 확장 계획

- **Core Message**: 글로벌 ESL 고객사 채택을 기반으로 2030년경 국내외 매출 200억 원을 달성하고, 전자종이·디스플레이 전 분야로 기술을 확장
- **Content Roles**:
  - Primary: 기대효과(정량적 매출·경쟁기반 성과) / 확장 계획(응용분야 확대 로드맵) — 대등한 병렬 2개 주제
  - Dependent: 각 주제 하위 bullet
  - Shared Supporting: N/A
  - Conclusion/Takeaway: "글로벌 ESL 고객사 채택을 기반으로 신규 해외 매출과 국내시장 진입을 추진"(기대효과 섹션 원문 결론)
- **Relationship**: 병렬
- **Content Regions**: Region A(좌, 기대효과 — 매출 100억원/200억원 등 Key Stat 중심) / Region B(우, 확장계획 — 단계적 bullet 목록)
- **Selected Layout**: L18 (Two-Column Summary)
- **Layout Selection Reason**: 두 주제 모두 "발표를 마무리하며 강조하는 핵심 요약·시사점" 성격 — Executive summary/key takeaways 용도에 부합. 정량 지표(기대효과)와 정성적 로드맵(확장계획)이 섞여 있어 완전한 대칭 비교는 아니므로 Symmetric Two-Split(L25)보다 Two-Column Summary가 더 적합
- **Structural Check**: 좌측(기대효과 5개)·우측(확장계획 6개) bullet 수가 비슷해 균형적. 좌측은 Key Stat(100억원/200억원) 강조, 우측은 목록형으로 유지해 정보 성격 차이를 시각적으로 구분 권장

---

## Slide 21. 클로징

- **Core Message**: COSOLUS 컨소시엄이 UV경화형 봉지소재 기술로 ESL 시장의 새로운 표준을 제시
- **Content Roles**: Primary: 브랜드 클로징 메시지(모토) / Conclusion/Takeaway: 발표 전체 요약 한 줄(선택)
- **Relationship**: 단일 콘텐츠
- **Content Regions**: 단일 Region — 클로징 메시지 + 모토("COSOLUS, small actions, BIG DIFFERENCE") + (선택) 연락처
- **Selected Layout**: L22 (Closing/Contact)
- **Layout Selection Reason**: "Final message + contact information" 용도에 정확히 부합
- **Structural Check**: 문제 없음. 페이지 번호 미표시 여부는 Hard Rule 기준(표지만 예외)을 따르되, 클로징은 일반 콘텐츠 슬라이드이므로 페이지 번호 표시 유지

---

## 구조적 사전 점검 종합 메모

- 로드맵 5슬라이드(13~17)는 사용자 지시에 따라 1개년 = 1슬라이드로 분리했으며, 모두 Three-Column Insight Layout 계열로 통일해 Deck 전체의 시각적 일관성을 확보함.
- 정보량이 많아 [5] 단계에서 축약이 필요하다고 표시한 슬라이드: 8(개발 필요성), 10(핵심 기술 구성), 13(로드맵 1차년도), 14(로드맵 2차년도), 19(사업화 전략). 모든 축약은 문장 압축·소그룹화 방식으로 처리하며, 수치·핵심 기술 주장은 변경하지 않는다(material-analysis 원칙 준수).
- Shared Supporting Content(특정 기관/Column에 귀속시키지 않아야 하는 공통 근거)는 슬라이드 12(기관별 역할 표)에서 별도 Supporting Region으로 분리 배치하도록 명시함.
- 원본 이미지(차트·다이어그램)가 존재하는 슬라이드(5, 6, 13~16, 19)는 Content Visualization Freedom의 "완성된 원본 Graph/Chart/Diagram 우선 재사용" 원칙에 따라 [5] 단계에서 원본 이미지를 그대로 사용하고 새로 재구성하지 않는다.
- **[7] 2026-08-25 갱신**: 슬라이드 18은 Human Review ② 피드백에 따라 "3개 기관 병렬 역량" 구조에서 "고객사 평가 결과(좌) vs 개선 방향(우)" 대비 구조로 전면 재구성됨(Selected Layout: L25 Symmetric Two-Split 재해석). 상세는 Slide 18 항목 참조.
- **[7] 2026-08-25 갱신 (Round 2)**: 슬라이드 18에 Round 1 이후 추가 피드백 3건 반영 — 상단 핵심 문장을 `.claim-box`에서 Hard Rule §12 Main Title Supporting Message로 교체, 좌측 마일스톤 문구 축약 및 배지/연결선 스타일 변경(화살표→얇은 세로선, 배지 31px→26px), "장기 신뢰성 평가 결과" 박스를 16pt 텍스트 한 줄로 대체. 이 Deck에서 Hard Rule §12 Supporting Message가 처음 사용된 사례이며, `.body-box.with-support`(top:210px, height:446px)는 "지역창업계획패키지 사업계획서" v3에서 검증된 동일 Hard Rule §12 구현값을 그대로 재사용함(신규 임의값 아님). 상세는 Slide 18 항목 참조.
- **[7] 2026-08-25 갱신 (Round 3)**: 슬라이드 18에 Round 2 이후 추가 피드백 2건 반영(web_ppt v4) — (1) 배지 간 얇은 세로선(`.ms-connector::before`, 1px)이 화면상 일직선으로 잘 보이지 않는다는 피드백에 따라 완전히 제거하고 20pt 다운 화살표(↓)로 복원(팔레트 내 `--c-primary` 유지), (2) "장기 신뢰성 평가 결과" 한 줄 요약을 텍스트 칸 부족 피드백에 따라 3문장(장기신뢰성 평가결과·주요현상·적용 가능성)으로 확장하되 본문 기준 16pt 유지, 핵심 결론 1문장만 Bold+Primary 강조. `qa_render.py --audit-fonts` 스크린샷으로 overflow 없음·전체 텍스트 16pt 이상 준수를 확인함. 상세는 Slide 18 항목 참조.
