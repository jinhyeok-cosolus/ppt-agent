# Slide Outline v4 — 지역창업계획패키지 사업계획서 (코솔러스)

## 전제 정보
- **청중**: 정부지원사업(지역창업패키지) 심사위원
- **언어**: 한국어
- **원본**: `코솔러스_사업계획서_프롬프트_V1.docx`(227개 문단, 슬라이드별 프롬프트·헤더박스·사진삽입 지시 포함) → `material_analysis_v4.json`. 이 문서가 v3의 소스(`코솔러스_사업계획서_PPT_페이지별_축약안.docx`)를 대체하는 신규 authoritative 브리프다. 근접 파일 `코솔러스_사업계획서_내용정리_V1.docx`는 v3 소스의 리네임본(신규 변경 없음)으로 확인되어 미사용.
- **슬라이드 수**: 22장 (표지 1 + 본문 20 + 클로징 1). v3(23장)에서 "사업비 집행계획"(구 Slide 3)이 신규 브리프에 존재하지 않아 삭제, 이후 전체 슬라이드 번호 -1 시프트.
- **전역 변경 3건 (모든 슬라이드 적용)**:
  1. **A1 — Vertical Content Divider(Hard Rule §11)**: 2개 이상 병렬 Content Region이 있는 모든 슬라이드에 Solid Variant(0.5pt, `#034443`, Vertical Gradient 중심 53%) 적용. 웹 렌더링 한정 1px fallback(`.v-divider` 공용 클래스 재사용).
  2. **A2 — 이미지 테두리/배경 박스 제거**: `.img-evidence img`, `.mini-stat img`, `.cert-badge img`, `.org-chart-wrap img` 등 이미지 관련 CSS의 `border`·불필요 `background` 선언을 전부 제거. 픽셀 단위 원본 이미지 편집(알파 매팅 등)은 하지 않음.
  3. **A3 — Main Title Supporting Message(부제) 삭제**: 모든 `<p class="support-msg">` 제거, `.body-box.with-support` → 기본 `.body-box`(Content Start Y=135px)로 복귀. 이미지에 붙는 캡션(예: Slide 2의 연구원 사진 캡션)은 Hard Rule §12 삭제 대상이 아니므로 유지.
- **버전 관계**: `web_ppt/v3`를 `new_version.py --from-latest`로 복사한 `web_ppt/v4` 위에서 전역 규칙 3건 + 콘텐츠/레이아웃 변경을 반영. 동일 소스 이미지는 v3 asset을 그대로 재사용, Slide 2 신규 이미지(`이미지_3.png` → `s02-founder-lab.png`)만 `docs/brand-assets/cover-images/`에서 신규 복사.
- **재사용 확정 수치**: 매출액/투자유치('25년) 공란·`[확인필요]`(누적투자 포함, 3건 모두 원문 미기재), 특허 8/11/4=23건(이전 프로젝트 확정치 재사용). 인증 이미지 004(벤처기업확인서, 앱클러스 소속 문서)는 사용자 명시 확정에 따라 그대로 포함.
- **신규 확보 데이터(이번 브리프 임베드 이미지 실측)**: 특허 목록 원본 표(img1) 실측으로 Slide 12의 1·3·4번째 항목(v3 목록 제목 기준) 등록/출원번호 확정 — ① 블랙매스 리튬회수(등록 10-2920129), ③ 마이크로웨이브 정제 고순도흑연(출원 10-2025-0160215), ④ 폐양극재·폐음극재 분리(출원 10-2025-0209511). Slide 15 고객사 표(img3+img4 실측)로 HS효성·포스코퓨처엠·대주전자재료 3개사의 사업/기술 현황 문장을 원문 그대로 확보 — `[확인필요]` 없이 표 구성.

---

## Slide 1. 표지

- **Core Message**: 코솔러스 — 사용 후 배터리 유래 흑연 음극재 재활용 및 고부가 소재 사업화
- **Content Roles**: Primary(제목/부제/회사명) — 나머지 N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Brand Block(좌상단) / Main Title Region(중앙)
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용)
- **Layout Selection Reason**: 표지 규칙 최우선 적용, 브리프도 "표지디자인 RULE을 따르면 됨"으로 명시
- **Structural Check**: 문제 없음. v3와 동일(변경 없음)

---

## Slide 2. 창업기업 정보

- **Core Message**: 코솔러스는 2020년 설립된 전북 전주 소재 이차전지 재활용 전문기업으로, 대표 김성현 아래 22명이 근무한다
- **Content Roles**: Primary(대표자/회사 기본정보/과제명), Dependent(2025년 현황 스냅샷)
- **Relationship**: 병렬 + 전체-부분
- **Content Regions**: Region A(좌, 정보 카드) / Region B(우, 연구원 실험 사진+캡션)
- **Selected Layout**: `02_instruction_design_V1.md` (Company Introduction)
- **Layout Selection Reason**: 브리프가 "왼쪽 정보, 우측 IMAGE3" 명시
- **Structural Check**: v3 대비 변경 — ① 생년월일·성별·전화번호 필드 삭제(신규 브리프 원문에 없음, v3처럼 표시하지 않음). ② 우측 이미지를 `location.png`(위치도)에서 `이미지_3.png`(흑백 연구원 실험 사진, `docs/brand-assets/cover-images/이미지_3.png` → `assets/images/s02-founder-lab.png`)로 교체. ③ 이미지 아래 캡션 "첨단 화학 소재와 차세대 친환경 공정으로 폐배터리 순환경제 선도" 추가 — 이는 Hard Rule §12 Supporting Message가 아니라 이미지 종속 캡션(Body 콘텐츠)이므로 A3 삭제 대상 아님. A1: Region A/B는 "정보 카드 + 우측 Full-bleed 사진 패널" 구조(Company Introduction 고유 패턴)로, 여러 검증 사례에서 이 패턴에 별도 Divider를 쓰지 않는 것이 확인되어(사진이 이미 별도 패널로 시각적 분리) Divider 미적용.

---

## Slide 3. 개발동기·목적

- **Core Message**: 사용 후 배터리 재활용 시장은 유망하지만, 흑연 음극재는 경제성 부족으로 현재 재활용 대상에서 제외되고 있다
- **Content Roles**: Primary(헤더박스 메시지, 배터리 구성/재활용 정의), Dependent(공정모식도), Conclusion(흑연 제외 공백시장 지적)
- **Relationship**: 기타·복합
- **Content Regions**: 상단 Full-width Header Box("사용 후 배터리 재활용 시장 유망") / 하단 30:70 분할(좌 텍스트, 우 공정모식도 이미지)
- **Selected Layout**: Visual + Insight Layout — Variant C(Technology·Principle), 상단 Header Box + 좌우 30:70 변형
- **Layout Selection Reason**: 브리프가 "헤더박스를 길게 위치시킨 뒤 좌우 30:70 분리"를 명시적으로 지정
- **Structural Check**: **v3 대비 변경** — 좌우 비율을 v3의 40:60(420px:flex1)에서 30:70(334px:778px)으로 재조정, 이에 맞춰 Divider 위치도 이동(left 440px→354px). Main Title도 v3의 긴 제목("개발동기·목적 — 사용 후 배터리 재활용 시장 유망")에서 브리프 지정대로 "개발동기·목적"으로 단순화(메시지는 헤더박스가 전달). A1: 좌우 Region 사이 Divider 유지(위치만 이동).

---

## Slide 4. 원천 기술·아이디어의 우수성

- **Core Message**: 사용 후 배터리 재활용은 배터리 순환경제의 핵심이며, 탄소중립·공급망 내재화 두 측면에서 중요성이 커지고 있다
- **Content Roles**: Primary(헤더박스), 2개 병렬 Region(탄소중립 실현 / 공급망 내재화) — 각 소제목+텍스트+이미지 묶음
- **Relationship**: 병렬(2개 근거, 각각 이미지 종속)
- **Content Regions**: Region A(탄소중립 실현: 소제목+설명+009_채굴비교) / Region B(공급망 내재화: 소제목+설명+008_모식도)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message+Evidence)를 2-Column으로 재해석
- **Layout Selection Reason**: 브리프가 "2컬럼 구조로 컬럼마다 소제목+텍스트+이미지 묶어서 배치"를 명시 요청
- **Structural Check**: **v3 대비 변경(구조 전환)** — v3는 헤더 텍스트 좌측 + 2개 이미지를 나란히 배치하는 `mini-stat-row`(이미지만 병렬) 구조였으나, 이번 브리프는 컬럼마다 "소제목+텍스트+이미지"를 세로로 묶는 구조로 전환. A1: 두 컬럼 사이 Divider 신규 배치(v3에는 이 슬라이드에 Divider 없었음 — 이번에 추가).

---

## Slide 5. 전기차 폐배터리 시장 전망

- **Core Message**: 전기차 보급 확대·폐배터리 급증·ESS 시장 성장이 동시에 진행되며 재활용 시장의 성장 기반을 만든다
- **Content Roles**: Primary 3개(전기차 시장 성장/폐배터리 발생 확대/ESS 시장 성장), Shared Supporting(각주 3건)
- **Relationship**: 병렬(대등 근거 3개)
- **Content Regions**: 3개 병렬 컬럼, 각 컬럼 Header+수치+이미지+캡션+설명
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 브리프 "3헤더 컬럼 구조" 명시
- **Structural Check**: **v3 대비 변경** — ① 각 이미지에 캡션 신규 추가("글로벌 전기차 폐배터리 시장 규모" / "폐배터리 발생량 전망" / "EV, ESS 성장 전망", v3는 캡션 없었음). ② A1: 컬럼 사이 Divider 2개 신규 추가(v3는 이 슬라이드에 Divider 없었음). 이미지 자산은 v3와 동일 소스(수치 일치 확인) 재사용.

---

## Slide 6. 흑연 음극재 재활용 시장 전망

- **Core Message**: 흑연 재활용 시장은 빠르게 성장하지만, 배터리 핵심소재인 흑연은 대부분 폐기되고 국내 재자원화율은 0%다
- **Content Roles**: Primary 4개(연평균 9.1%성장/폐기되는핵심소재/급증하는수요/국내재활용현황), Shared Supporting(각주 4건)
- **Relationship**: 병렬(대등 근거 4개)
- **Content Regions**: 좌 절반(상하 2항목) / 우 절반(상하 2항목) — 2x2 재배열, 각 항목 아이콘(좌)+제목/강조수치/핵심내용(우) 순서
- **Selected Layout**: L04 KPI Summary → 2x2 Grid 변형(카드 테두리 없음)
- **Layout Selection Reason**: 브리프가 "4컬럼이 아니라 좌우 절반으로 나눠 2x2 배치, 테두리 삭제, 제목/강조수치/핵심내용 순, 아이콘은 텍스트 왼쪽" 명시
- **Structural Check**: **v3 대비 변경(구조 전환)** — v3는 4-Column KPI Grid(카드형, 아이콘 상단 중앙)였으나 이번엔 좌우 절반×상하 2항목의 2x2, 카드 테두리 삭제(이 삭제는 A2 이미지 테두리 규칙과 별개의 이 슬라이드 전용 지시), 아이콘을 텍스트 왼쪽에 배치. A1: 좌우 절반 사이 Divider 신규 추가. 상하 두 항목끼리는 규칙상 강제 아니므로 별도 Divider 없이 여백으로 구분.

---

## Slide 7. 정책 모멘텀

- **Core Message**: 정부는 순환경제 생태계 조성 국정과제와 배터리 순환이용 활성화 방안으로 음극재·분리막 재활용 기술 고도화를 추진한다
- **Content Roles**: Primary 3개 대등 정책
- **Relationship**: 병렬
- **Content Regions**: 3개 병렬 컬럼(정책명+아이콘+설명)
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 브리프 "변경 없음 — v3 그대로 유지" 명시, 3컬럼 구조 유지
- **Structural Check**: **콘텐츠 변경 없음**(브리프 지시대로 v3 텍스트·아이콘 그대로 유지, 실제 웹 이미지 미사용 원칙도 유지). A1: 컬럼 사이 Divider 2개 신규 추가(v3는 이 슬라이드에 Divider 없었음 — 전역 규칙 적용으로 추가).

---

## Slide 8. Cosolus 흑연 기술

- **Core Message**: 코솔러스는 블랙매스에서 흑연을 선택 분리·정제해 고순도 정제흑연을 만들고 고부가 소재로 재자원화한다
- **Content Roles**: Primary 2개(흑연 음극재 재활용 공정 / 고부가 흑연 소재화)
- **Relationship**: 순차 + 전체-부분
- **Content Regions**: 상단 텍스트 전체 / 하단 큰 이미지(007_흑연소재화모식도)
- **Selected Layout**: Visual + Insight Layout — Variant A(상하 배치)
- **Layout Selection Reason**: 브리프 "텍스트 전체 넣고 그림을 아래에 크게" 명시, v3와 동일 구조 유지 지시
- **Structural Check**: 콘텐츠 변경 없음(이미지·캡션 이미 v3에 반영되어 있었음). 단일 순차 흐름이라 Divider 미적용 대상.

---

## Slide 9. 기술 개발 현황

- **Core Message**: 코솔러스는 강산 미사용 친환경 공정으로 TRL 6, 연 1.5톤 파일롯 기반을 확보했다
- **Content Roles**: Primary 2그룹(친환경 고순도 공정 / Pilot 설비 기반 확보), 각 그룹에 Dependent 이미지 종속
- **Relationship**: 병렬 2그룹(그룹별 종속 이미지)
- **Content Regions**: 상단 Header Box / 좌 컬럼(공정 설명+SEM 이미지) / 우 컬럼(설비 설명+정제설비 이미지)
- **Selected Layout**: Visual + Insight Layout — Variant A, 2-Column 재해석
- **Layout Selection Reason**: 브리프 "좌우 2그룹으로 재구성, 그룹별로 텍스트+이미지를 묶음" 명시
- **Structural Check**: **v3 대비 변경(구조 전환)** — v3는 상단 4-KPI Grid(텍스트만) + 하단 좌우 이미지(SEM/정제설비, 텍스트와 분리)였으나, 이번엔 텍스트와 대응 이미지를 그룹별로 묶어 좌우 배치. A1: 두 그룹 사이 Divider 유지(위치 재조정).

---

## Slide 10. 기술고도화 로드맵

- **Core Message**: 2026년 울산 사업장 구축을 시작으로 2028년 기술라이센싱까지 단계적으로 고도화한다
- **Content Roles**: Primary 4개 Milestone(2026/2026~2027/2027/2028)
- **Relationship**: 순차(시간 흐름)
- **Content Regions**: Timeline Region
- **Selected Layout**: Timeline / Company Milestone Layout
- **Layout Selection Reason**: 브리프 "내용 동일, v3의 timeline 구조 유지" 명시
- **Structural Check**: 콘텐츠 변경 없음. 순차 Timeline이라 Divider 미적용 대상.

---

## Slide 11. 기술개발 인력

- **Core Message**: 코솔러스는 기술개발을 뒷받침하는 조직 체계를 갖추고 있다
- **Content Roles**: Primary(조직도 이미지)
- **Relationship**: 단일 콘텐츠
- **Content Regions**: 중앙 대형 조직도 이미지
- **Selected Layout**: Visual + Insight Layout — Variant A(단일 전체 이미지 변형)
- **Layout Selection Reason**: 원본 조직도 이미지(015_조직도) 존재 시 원본 재사용 원칙
- **Structural Check**: **v3 대비 변경** — 그림설명(캡션) 텍스트 삭제(브리프 명시 지시). A2: 이미지 배경 박스(`var(--c-dark)`)·테두리 제거(이미지 자체는 불투명 원본이라 시각적 손실 없음).

---

## Slide 12. 보유 기술 및 인증 현황

- **Core Message**: 코솔러스는 특허 8건 등록·11건 국내출원·4건 PCT 등 총 23건의 지식재산권과 6종의 정부·기관 인증을 보유한다
- **Content Roles**: Primary(헤더박스+총건수), Region A(대표 특허 3건 table), Region B(인증 6종)
- **Relationship**: 비교(2개 병렬 영역)
- **Content Regions**: 상단 Header Box("특허 및 인증 기술 현황") / 좌(특허 현황 KPI+table) / 우(인증 현황 6개 한 줄)
- **Selected Layout**: L25 Symmetric Two-Split + 상단 Header Box
- **Layout Selection Reason**: 브리프가 헤더박스 지정 + 좌우 분할 유지
- **Structural Check**: **v3 대비 변경** — ① 특허 table 컬럼을 "순번·특허명·등록/출원번호"만 사용(구분 컬럼 삭제), 표시 항목을 3건(v3 목록의 1·3·4번째 항목, 제목 기준)으로 축소 — 등록/출원번호는 브리프 지정 우선순위(v3 목록 우선, 실측은 이번 브리프 임베드 표로 교차검증)에 따라 확정(①10-2920129, ②10-2025-0160215, ③10-2025-0209511), 임의 생성 없음. ② table 하단 설명 캡션 삭제. ③ 인증 6개를 그리드(3x2)에서 한 줄 배치로 변경, 사진 설명(캡션) 전부 삭제. A1: 좌우 Divider 유지(위치 재조정).

---

## Slide 13. 흑연 음극재 시장 성장가능성

- **Core Message**: 글로벌 음극재 시장은 2035년 115억 달러로 성장하지만, 한국은 원료의 중국 의존도가 97~99%에 달해 공급망 재편이 필요하다
- **Content Roles**: Region A(글로벌 음극재 시장), Region B(중국 의존도+글로벌 규제)
- **Relationship**: 병렬(2개 대등 주제)
- **Content Regions**: 좌(Header Box+수치+이미지) / 우(Header Box+통계+텍스트+이미지)
- **Selected Layout**: L25 Symmetric Two-Split, 각 컬럼 상단 Header Box 추가
- **Layout Selection Reason**: 브리프가 "헤더박스1/헤더박스2"로 두 컬럼 모두에 Header Box 지정 — Hard Rule §10 Parallel Variant 적용
- **Structural Check**: **v3 대비 변경** — ① 우측 컬럼의 이미지(025_글로벌진출강화)를 텍스트 아래로 재배치(v3는 통계-이미지-텍스트 순, 이번엔 통계-텍스트-이미지 순으로 "사진은 텍스트 아래" 지시 반영). ② 각주에서 "출처" 단어 제거, 출처명만 표기(좌우 각주를 하단 공통 각주로 통합: "Fortune Business Insights · Energy Act of 2020 · Regulation(EU) 2023/1542(2023.08.17 시행)"). A1: Divider 유지.

---

## Slide 14. 사업화 모델

- **Core Message**: 정제흑연 판매에서 고부가 소재로 수익원을 확대하며 2027년 1억원에서 2029년 50억원 매출을 목표로 한다
- **Content Roles**: Primary 3단계 순차 + Conclusion(매출 목표)
- **Relationship**: 순차
- **Content Regions**: 상단 Header Box / 좌(3단계 텍스트) 우(전략 이미지) / 하단 매출 목표 bar
- **Selected Layout**: Process / System Architecture Layout — Layout B
- **Layout Selection Reason**: 브리프 "내용 동일, v3 구조 유지" 명시
- **Structural Check**: 콘텐츠 변경 없음. 순차 Process+Output 구조라 Divider 미적용 대상(v3 원 설계 유지).

---

## Slide 15. 고객사 분석

- **Core Message**: 국내 배터리 3사 중심 약 1조원의 음극재 내수시장이 형성되어 있으며, 국내 주요 음극재 기업(HS효성/포스코퓨처엠/대주전자재료)이 기술 확대를 추진 중이다
- **Content Roles**: Primary(헤더박스+시장규모 주장), Dependent(국내 기업 table)
- **Relationship**: 종속(주장 + 표 근거)
- **Content Regions**: 상단 Header Box+텍스트 / 하단 Table("국내 주요 음극재 기업 및 기술 현황")
- **Selected Layout**: Table Comparison Layout(단일 표, Hard Rule §10B Table Header Row 적용)
- **Layout Selection Reason**: 브리프 "표 생성(v3는 value-chain 다이어그램이었는데 이번엔 표로 전환)" 명시 지시
- **Structural Check**: **v3 대비 변경(구조 전환)** — v3의 공급자→코솔러스→수요처 Value-Chain 다이어그램을 폐기하고 표로 전환. 표 데이터는 원문에 개별 기업 세부 스펙이 없다는 우려가 있었으나, 브리프 문서에 임베드된 실측 표 이미지(순번/기관명/사업 및 기술 현황)를 `material_analysis_v4.json`에서 확인해 3개사(HS효성/포스코퓨처엠/대주전자재료) 데이터를 원문 그대로 확보 — **`[확인필요]` 없이 구성 완료**(임의 스펙 생성 없음). 단일 순차(텍스트→표) 구조라 Divider 미적용 대상.

---

## Slide 16. 경쟁사 대비 우수성

- **Core Message**: 코솔러스의 유도가열 공정은 BTR·Vianode의 초고온 간접가열 대비 처리시간과 에너지 효율에서 압도적 우위를 가진다
- **Content Roles**: Primary(3사 비교 table), Conclusion(레이더 차트 이미지)
- **Relationship**: 비교(3사)
- **Content Regions**: 좌(비교 table, 자사 열 강조) / 우(레이더 비교 이미지)
- **Selected Layout**: Comparison Matrix Layout + Competitive Advantage Highlight
- **Layout Selection Reason**: 브리프 "테이블 재구성 + 이미지, 좌우 배치, 테이블·사진 크기 맞춤" 명시, v3 검증 레이아웃 재사용
- **Structural Check**: **v3 대비 변경** — ① 헤더박스 "유도가열 공정의 경쟁력" 추가. ② 기업명 헤더 행에 테두리 신규 적용(Hard Rule §10B Table Grid 기준, 이전엔 하단 강조선만 있었음). ③ COSOLUS 열(자사 강조 열) 전체 Bold 처리 추가. ④ 사진 설명(캡션) 삭제. ⑤ 표와 사진을 동일 높이 컨테이너로 맞춰 시각적 크기를 정렬. A2: 사진 테두리 없음(기존에도 없었음, 유지).

---

## Slide 17. 시장확대방안

- **Core Message**: 고순도 정제흑연은 음극재를 넘어 전도성·방열 첨가제 등 고부가 업사이클 제품과 그래핀 원료로 확장 가능하며, 목표 고객사와 협의 중이다
- **Content Roles**: Region A(시장 확대 방향), Region B(업사이클 확대 방향)
- **Relationship**: 병렬(2개 대등 방향)
- **Content Regions**: 좌 Header Box(시장 확대 방향+시장전망 이미지 2개) / 우 Header Box(업사이클 확대 방향+목표고객사 2건)
- **Selected Layout**: 2× Content Region Header(Hard Rule §10 Parallel Variant) 병렬 2-Column
- **Layout Selection Reason**: 브리프가 명시적으로 "Hard Rule §10 Content Region Header, Parallel Variant로 재구성"을 지정
- **Structural Check**: **v3 대비 변경(구조 전환)** — v3의 Hub-and-Spoke(방사형, 중심 허브+3개 스포크) 구조를 폐기하고 2개 병렬 Header Box 구조로 전환(브리프 명시 지시). A1: 두 Header Box 영역 사이 Divider 신규 배치.

---

## Slide 18. 투자 유치 계획

- **Core Message**: 양극재·음극재 사업화 자금 61억원을 유치했으며, 2026년 Series A2(10억원 확정)에 이어 2028년 Series B를 준비 중이고, 보유 기술력·제품 사업화 역량도 갖추고 있다
- **Content Roles**: 헤더1(투자 유치 현황+계획), 헤더2(보유기술력+제품 사업화)
- **Relationship**: 병렬(2개 대등 축) — 좌: 외부 자금 조달, 우: 내적 역량
- **Content Regions**: 좌(투자 유치 실적) / 우(내적 역량, **신규**)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프 "2개 컬럼 구조" 명시
- **Structural Check**: **v3 대비 변경(콘텐츠 추가)** — v3는 좌(투자유치 현황)/우(투자유치 계획)로 분할했으나, 이번 브리프는 좌에 현황+계획을 모두 통합하고 우측에 **v3에 없던 신규 콘텐츠 "내적 역량"**(보유기술력 3건 + 제품 사업화 3건)을 추가. 콘텐츠 밀도가 높아 Typography(16pt 유지)·Gap(12~14px)을 촘촘히 조정해 담음 — Body 최소 크기(16pt) 기준은 유지(임의 축소 없음). A1: 좌우 Divider 유지.

---

## Slide 19. 울산 기술사업화 계획

- **Core Message**: 울산 사업장을 구축해 파일롯 라인을 설치하고, 기술이전·인력채용·공동연구를 거쳐 시제품 생산과 고객 검증으로 시장경쟁력을 확보한다
- **Content Roles**: 헤더1(지역 내 기술사업화 계획, 4단계), 헤더2(Pilot 설비 라인 모식도)
- **Relationship**: 병렬(설명 vs 시각자료)
- **Content Regions**: 좌(4단계 순차 bullet, Header Box) / 우(파일롯 이미지, Header Box)
- **Selected Layout**: Visual + Insight Layout — Variant A, 병렬 Header Box 추가
- **Layout Selection Reason**: 브리프가 "헤더2"로 우측 이미지 영역에 라벨을 명시 지정, 좌측도 대칭 적용
- **Structural Check**: **v3 대비 변경** — 좌우 각각에 Header Box 신규 배치(v3는 Header 없이 vi-wrap 구조). 우측 이미지 설명(캡션) 삭제(브리프 명시 지시). A1: Divider 유지(위치 재조정).

---

## Slide 20. 지역 활성화

- **Core Message**: 울산 내 대기업·이차전지 특화단지 기업과의 거래·협업을 추진하고, 연구인력·생산인력을 지역에서 채용한다
- **Content Roles**: Region A(지역 내 거래 계획), Region B(지역 내 고용 계획)
- **Relationship**: 병렬
- **Content Regions**: 좌(거래 계획 3건) / 우(고용 계획 2건)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프 "2개 컬럼 구조" 명시, v3와 동일 계열
- **Structural Check**: **v3 대비 콘텐츠 교체** — 거래 계획은 동일 유지. 고용 계획 텍스트를 브리프 신규 문구로 **완전 교체**(병기 아님): 기존 "지역 청년 생산인력 우선 채용"/"산학연 네트워크 구축" → 신규 "한국에너지기술연구원과 기술이전 및 고도화를 위한 석박사 인재를 울산소재 대학으로부터 연간 1명 이상 고용" + "시제품 개발 완료 후 생산 착수 시 지역인력 우선 채용". A1: Divider 유지.

---

## Slide 21. 지역이전 실행계획

- **Core Message**: 2026년 말부터 본사·부설연구소·파일롯 공장을 울산 이차전지 특화단지로 단계적으로 이전해, 연구·파일롯 인력을 2명에서 10명으로 확대한다
- **Content Roles**: Primary(이전 개요 4항목), Dependent(핵심 목표), Shared Supporting(울산 이미지)
- **Relationship**: 전체-부분 + 단일 콘텐츠
- **Content Regions**: 좌(이전 개요+핵심 목표) / 우(울산 이미지)
- **Selected Layout**: Business Site Map Layout(Pin 대신 원본 사진 사용 변형)
- **Layout Selection Reason**: 브리프 "내용 동일, v3 구조 유지" 명시
- **Structural Check**: 콘텐츠 변경 없음. A1: Divider 유지(v3에서 이미 있던 위치).

---

## Slide 22. 클로징

- **Core Message**: COSOLUS, small actions, BIG DIFFERENCE — 흑연 음극재 재활용으로 배터리 순환경제와 지역 이차전지 산업의 성장을 함께 만든다
- **Content Roles**: Primary(브랜드 모토), Dependent(Contact)
- **Relationship**: 단일 콘텐츠
- **Selected Layout**: L22 Closing/Contact
- **Layout Selection Reason**: Hard Rule §7이 Closing 페이지 Motto 사용을 명시적으로 허용, v2/v3에서 이미 승인된 디자인 재사용
- **Structural Check**: **브리프 범위 외 유지 항목** — 이번 신규 브리프(227문단)에도 클로징 슬라이드 명시 지시가 없다. v3에서 이미 사용자 확인을 거쳐 채택된 클로징 디자인을 v4에서도 그대로 유지(연락처에서 전화번호는 Slide 2와 동일하게 신규 브리프 원문 기준으로 이메일만 표기).

---

## [3]→[5] 인계 사항 (v4 갱신)

1. **사업비 집행계획 삭제**: v3 Slide 3(사업비 집행계획)은 신규 브리프에 대응 슬라이드가 없어 완전 삭제, 이후 전체 슬라이드 번호 -1 시프트. 최종 22장 구성은 본 문서 상단 "전제 정보" 참조.
2. **이미지 자산**: 브리프 명시 파일번호(019/009/008/020~022/023/013/014/007/026/024/025/027/028/034 등)는 v3에서 이미 매핑된 동일 소스 파일을 그대로 재사용. Slide 2의 IMAGE3(`이미지_3.png`)만 `docs/brand-assets/cover-images/`에서 신규 복사(`s02-founder-lab.png`).
3. **특허 목록 재확인**: v3 특허 table 순번 1·3·4번째 항목(제목 기준)의 등록/출원번호를 이번 브리프 임베드 표 이미지로 교차 검증해 확정 — 신규 생성 아님, 두 소스(구 project material_analysis.json 마스터 리스트 / 신규 브리프 임베드 표)가 완전 일치함을 확인.
4. **고객사 표 데이터**: 신규 브리프 임베드 표 이미지(img3+img4)에서 HS효성/포스코퓨처엠/대주전자재료 3개사의 사업 및 기술 현황 문장을 실측 확보 — `material_analysis_v4.json`의 `images_content_note`에 기록.
5. **전역 규칙 적용 범위**: A1(Divider)은 실제 병렬 Region이 있는 슬라이드에만 적용하고, 순차/단일 콘텐츠 슬라이드(8, 10, 14, 15, 21 일부)에는 적용하지 않음 — Hard Rule §11 "Divider 자체의 사용 여부는 Layout Reference 규칙을 따른다" 원칙에 따름.
