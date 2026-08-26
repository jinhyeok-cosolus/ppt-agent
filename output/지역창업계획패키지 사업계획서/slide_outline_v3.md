# Slide Outline v3 — 지역창업계획패키지 사업계획서 (코솔러스)

## 전제 정보
- **청중**: 정부지원사업(지역창업패키지) 심사위원
- **언어**: 한국어
- **원본**: `코솔러스_사업계획서_PPT_페이지별_축약안.docx` → `material_analysis_v3.json`(신규 브리프, 204개 문단, 슬라이드별 프롬프트·헤더·사진삽입 지시 포함). 원본 문서에 임베드된 이미지 2개(특허목록 표, COSOLUS/BTR/Vianode 비교표)를 실측 확인해 Slide 13·17에 반영.
- **슬라이드 수**: 23장 (표지 1 + 본문 21 + 클로징 1). 이전 프로젝트(26장, 구 소스 문서 기반)는 참고용으로만 사용하고 이번 브리프가 최종 스펙.
- **버전 관계**: `web_ppt/v2`(이전 26장 빌드)의 Hard-Rule 준수 CSS 스캐폴딩·컴포넌트를 재사용하되, 콘텐츠가 겹치는 슬라이드(시장성장/경쟁사비교/투자/IP/지역이전 등)만 마크업을 어댑트하고 나머지는 이번 브리프 기준으로 새로 구성한다.
- **금지사항 재확인**: 사업비 집행계획(Slide 3)에 금액 수치 없음 — 임의 생성 금지. 특허 건수(Slide 13)는 이전 프로젝트에서 사용자 확인을 거친 등록8/국내출원11/PCT4=23건을 재사용(신규 생성 아님). 매출액·투자유치('25년, Slide 2)는 공란/[확인필요] 유지.

---

## Slide 1. 표지

- **Core Message**: 코솔러스 — 사용 후 배터리 유래 흑연 음극재 재활용 및 고부가 소재 사업화 (2026년 지역창업패키지 사업계획서)
- **Content Roles**:
  - Primary: 발표 제목(과제명), 부제(2026년 창업도시 조성 프로젝트 · 지역창업패키지 사업계획서), 회사명(주식회사 코솔러스)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Brand Block(좌상단, CI+Sub Message) / Main Title Region(중앙, 제목+부제)
- **Selected Layout**: `01_cover_design_V2.md` (표지 전용, L01~L33 미참고)
- **Layout Selection Reason**: 표지 슬라이드이므로 규칙에 따라 표지 전용 문서를 최우선 적용
- **Structural Check**: 문제 없음. 부제 문구는 브리프 원문 "2026년 창업도시 조성 프로젝트 · 지역창업패키지 사업계획서"를 그대로 사용

---

## Slide 2. 창업기업 정보

- **Core Message**: 코솔러스는 2020년 설립된 전북 전주 소재 이차전지 재활용 전문기업으로, 대표 김성현 아래 22명이 근무하는 성장기 스타트업이다
- **Content Roles**:
  - Primary: 대표자 정보(김성현/010-9565-5801/shkim@cosolus.com), 창업기업 기본정보(유형/기업명/개업일/사업자유형/소재지/사업자등록번호/법인등록번호), 과제명
  - Dependent: 2025년 현황 스냅샷(매출액·총고용·투자유치·누적투자)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(정보 항목들이 대등하게 나열) + 전체-부분(회사 정보 → 지역 위치)
- **Content Regions**: Region A(좌, 대표자+회사 기본정보 카드) / Region B(우, 회사 소재지 지도 이미지 또는 정보 카드)
- **Selected Layout**: `02_instruction_design_V1.md` (Company Introduction, 좌 정보/우 세로 이미지 2단 구조)
- **Layout Selection Reason**: 브리프가 명시적으로 "대표자 및 회사 정보를 왼쪽에, 우측에 지도사진"을 요청 — Company Introduction의 Use When(회사 기본정보 전달 + 좌 정보/우 세로 이미지) 조건에 정확히 부합
- **Structural Check**: 매출액('25년)·투자유치('25년)는 원문에 값 없음 — `[확인필요]`로 표시(이전 프로젝트에서 이미 사용자 확인 완료, 재확인 불필요). 우측 지도이미지는 `web_ppt/v2/assets/images/location.png` 재사용 가능 여부를 [5] 단계에서 확인 후 결정 — 부적합하면 이미지 없는 정보 카드 구성으로 대체(임의 지도 생성 금지)

---

## Slide 3. 사업비 집행 계획

- **Core Message**: 정부지원사업비는 파일롯 공정검증·설비설계·기술이전·인력교육에, 자기부담사업비는 신규인력 인건비와 기계장치 현물 대응에 사용한다
- **Content Roles**:
  - Primary: 정부지원사업비 3개 항목(재료비/외주용역·지급수수료/인건비·교육비·여비), 자기부담사업비 2개 항목(인건비/기계장치)
  - Dependent: 각 항목의 용도 설명
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교(대등한 2개 예산 축)
- **Content Regions**: Region A(정부지원사업비, 아이콘+3항목) / Region B(자기부담사업비, 아이콘+2항목)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프가 "좌우 헤더 구조", "아이콘 1개씩"을 명시적으로 요청 — 두 예산 항목군이 동일 위계로 병렬 제시되는 구조에 부합. 이전 프로젝트 Slide 11과 동일 계열 레이아웃 재사용
- **Structural Check**: **[확인필요 유지]** 금액 수치가 원문에 전혀 없음(이전 버전보다 더 축약된 소스) — 항목명·용도만 표시하고 금액 칸 자체를 만들지 않음. 임의 금액 생성 절대 금지

---

## Slide 4. 개발동기·목적 — 사용 후 배터리 재활용 시장 유망

- **Core Message**: 배터리 재활용은 핵심소재를 회수하는 기술이지만, 현재는 양극재 중심으로만 이루어지고 흑연 음극재는 경제성 부족으로 재활용 대상에서 제외되고 있다
- **Content Roles**:
  - Primary: 배터리 구성(양극재/음극재/분리막/전해질) 및 재활용 기술 정의, 현재 재활용이 NCM·NCA 양극재 중심이라는 현황
  - Dependent: 흑연이 제외되는 이유(경제성 낮음)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 흑연 음극재 재활용이라는 공백 시장의 존재
- **Relationship**: 기타·복합(정의+현황+공백 지적)
- **Content Regions**: Region A(설명 텍스트 — 배터리 구성/재활용 정의/현황) / Region B(공정모식도 이미지, 019_공정모식도)
- **Selected Layout**: Visual + Insight Layout — Variant C(Technology·Principle)
- **Layout Selection Reason**: 재활용 공정의 개념/원리를 모식도 이미지와 설명으로 함께 전달하는 목적에 부합. 완성된 원본 모식도 이미지가 존재하므로 Content Visualization Freedom 우선순위에 따라 원본 이미지를 그대로 사용(재구성 금지)
- **Structural Check**: 문제 없음. 섹션 라벨은 BACKGROUND

---

## Slide 5. 1-1 원천 기술·아이디어의 우수성 — 배터리 순환경제 핵심

- **Core Message**: 사용 후 배터리 재활용은 채굴 대비 탄소발자국·폐수 발생이 적어 탄소중립 실현의 핵심 기술이며, 공급망 내재화 전략으로도 중요성이 커지고 있다
- **Content Roles**:
  - Primary: 헤더 메시지("배터리 순환경제의 핵심"), 근거 2가지(탄소중립 기여, 공급망 내재화 전략)
  - Dependent: 배터리 순환경제 모식도(008), 채굴·재활용 비교(009) — 두 이미지 모두 위 근거를 직접 뒷받침
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(2개 근거 텍스트) + 그 근거를 뒷받침하는 2개 이미지(각각 대응)
- **Content Regions**: Region A(헤더 메시지+2개 근거 텍스트) / Region B(2개 근거 이미지를 나란히 배치 — 순환경제모식도/채굴비교)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message+Evidence)
- **Layout Selection Reason**: 하나의 핵심 주장(배터리 순환경제=핵심기술)을 2개의 원본 Evidence 이미지로 뒷받침하는 구조에 부합. 두 이미지 모두 완성된 원본이므로 그대로 사용
- **Structural Check**: 문제 없음. 섹션 라벨 BACKGROUND

---

## Slide 6. 전기차 폐배터리 시장 전망

- **Core Message**: 전기차 보급 확대, 폐배터리 발생 급증, ESS 시장 성장이 동시에 진행되며 사용 후 배터리 재활용 시장의 성장 기반을 만든다
- **Content Roles**:
  - Primary: 3개 대등 항목(전기차 시장 성장/폐배터리 발생 확대/ESS 시장 성장) — 각각 독립 수치와 이미지를 보유
  - Dependent: 각 항목의 근거 이미지(020/021/022)
  - Shared Supporting: 각주(출처 3건)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(동일 위계의 독립 근거 3개)
- **Content Regions**: Region A(전기차 시장 성장) / Region B(폐배터리 발생 확대) / Region C(ESS 시장 성장) — 3개 병렬 컬럼, 각 컬럼 하단에 대응 이미지
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 브리프가 "3헤더 컬럼 구조"를 명시적으로 요청하며, 대등한 위계의 독립적 근거 3개를 병렬 제시하는 Use When 조건에 정확히 부합
- **Structural Check**: 문제 없음. 3개 이미지 모두 원본 그대로 사용, 각주 3건은 슬라이드 하단 공통 Source 영역에 배치

---

## Slide 7. 흑연 재활용 시장 기회

- **Core Message**: 흑연 재활용 시장은 빠르게 성장하지만, 배터리 핵심소재인 흑연은 대부분 폐기되고 있으며 국내 재자원화율은 0%에 머물러 있다
- **Content Roles**:
  - Primary: 4개 대등 항목(흑연 재활용 시장 성장/폐기되는 핵심소재/급증하는 흑연 수요/국내 재활용 현황) — 각각 독립 수치 보유
  - Dependent: N/A
  - Shared Supporting: 각주(출처 4건)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(동일 위계의 독립 근거 4개)
- **Content Regions**: 4개 KPI 카드 Region(각 아이콘+수치+설명)
- **Selected Layout**: L04 KPI Summary
- **Layout Selection Reason**: 브리프가 "4개 항목 4컬럼, 아이콘"을 요청. 4개는 Three-Column 문서의 적용 범위(3개 대등 근거)를 벗어나며, 각 항목이 짧은 수치+설명 조합(압축형 Visual)으로 구성되어 카드형 KPI 그리드 구조(L04)에 더 적합. 특수 Layout Reference 중 4개 병렬 독립 근거에 맞는 전용 문서가 없어 범용 카탈로그에서 선택
- **Structural Check**: 문제 없음. 아이콘은 Design System Shape 컴포넌트(브랜드 컬러 Flat 아이콘)로 구성, 이모지 컬러 렌더링 금지 원칙 준수

---

## Slide 8. 정책 모멘텀

- **Core Message**: 정부는 "순환경제 생태계 조성" 국정과제와 배터리 순환이용 활성화 방안을 통해 음극재·분리막 재활용 기술 고도화를 신규 정책 과제로 추진하고 있다
- **Content Roles**:
  - Primary: 3개 대등 정책(국정과제-순환경제 생태계 조성/배터리 순환이용 활성화 방안/음극재·분리막 고부가 재활용 기술의 정책 과제 부상)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(대등한 정책 근거 3개)
- **Content Regions**: 3개 병렬 컬럼(정책명+설명, 개념 아이콘)
- **Selected Layout**: Three-Column Insight Layout
- **Layout Selection Reason**: 브리프가 "3개 컬럼 구조"를 명시적으로 요청. 대등한 위계의 독립 정책 근거 3개를 병렬 제시하는 조건에 부합
- **Structural Check**: **[판단 사항]** 브리프는 "관련 이미지를 웹에서 찾아서 넣어줘"라고 요청했으나, 로컬 처리 원칙(원본 자료 외부 검색 미수행) 및 web-ppt-generator의 오프라인 원칙상 실제 웹 이미지를 가져오지 않는다 — 대신 Design System §6 Shape/Icon 컴포넌트로 정책 개념을 표현하는 아이콘(예: 순환 화살표, 문서 아이콘, 상승 그래프 아이콘)을 구성한다. Content Visualization Freedom "개념·기능·효과·추상적 메시지 → Icon" 기준에 부합하는 대체 판단이며, 브랜드 컬러 범위 안에서만 구성

---

## Slide 9. 코솔러스 흑연 기술

- **Core Message**: 코솔러스는 사용 후 배터리 블랙매스에서 흑연을 선택 분리·정제해 고순도 정제흑연을 만들고, 이를 음극재·전도성 첨가제·방열 첨가제 등 고부가 소재로 재자원화한다
- **Content Roles**:
  - Primary: 흑연 음극재 재활용 공정 설명(선택적 분리·정제→고순도 정제흑연), 고부가 음극재 재활용 흑연 소재 설명(음극재/전도성첨가제/방열첨가제로 제품화)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차(공정) + 전체-부분(산출물 확장)
- **Content Regions**: Region A(상단, 설명 텍스트 전체) / Region B(하단, 007_흑연소재화모식도 큰 이미지)
- **Selected Layout**: Visual + Insight Layout — Variant A(Image+Explanation), 브리프 지시에 따라 좌우 대신 상(텍스트)·하(큰 이미지) 배치로 조정
- **Layout Selection Reason**: 브리프가 "사진이 길기 때문에 텍스트를 전체 다 넣고, 그림을 아래에서 크게 보여주는 형태"를 명시적으로 요청 — Content Visualization Freedom의 "콘텐츠 양에 따른 좌우/상하 영역 비율 조정" 허용 범위 안에서 Visual+Insight Family를 상하 방향으로 재해석. 이미지 자체가 긴 형태(세로형 모식도)라는 실제 자산 특성에 맞춘 구조적 조정
- **Structural Check**: 문제 없음. 섹션 라벨 TECHNOLOGY

---

## Slide 10. 기술 개발 현황

- **Core Message**: 코솔러스는 강산 미사용 친환경 공정으로 TRL 6, 연 1.5톤 파일롯 기반을 확보했으며 초고온 공정 대비 에너지 64%를 절감한다
- **Content Roles**:
  - Primary: 4개 핵심 성과(강산 미사용 친환경 공정/유도가열 1분 이내 1,000℃·순도99%/에너지 64% 절감/연 1.5톤 파일롯 구축 중)
  - Dependent: SEM 결과 이미지(023), 유도가열설비 이미지(013) — 성과를 뒷받침하는 Evidence
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 종속(주장 4개 + 이미지 Evidence 2개)
- **Content Regions**: Region A(상단, 4개 성과 bullet) / Region B(하단, SEM+정제설비 이미지 좌우 배치)
- **Selected Layout**: Visual + Insight Layout — Variant A(Image+Explanation), 듀얼 이미지 Evidence 구성
- **Layout Selection Reason**: 브리프가 "SEM 결과와 유도가열 설비 사진을 좌우 배치"를 명시적으로 요청 — 설명 텍스트(4개 성과)와 2개의 원본 Evidence 이미지를 함께 보여주는 구조에 부합
- **Structural Check**: 문제 없음. 두 이미지 모두 원본 그대로 사용(재구성 금지)

---

## Slide 11. 기술고도화 로드맵

- **Core Message**: 2026년 울산 사업장 구축·기술이전·투자유치를 시작으로 2028년까지 시제품 양산, 자동화, 기술라이센싱 단계로 고도화한다
- **Content Roles**:
  - Primary: 4개 시점 Milestone(2026/2026~2027/2027/2028)
  - Dependent: 각 시점의 세부 내용
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차(시간 흐름)
- **Content Regions**: Timeline Region(2026~2028, 4개 Milestone)
- **Selected Layout**: Timeline / Company Milestone Layout
- **Layout Selection Reason**: 연도 기준 Milestone을 순차 배치하는 목적에 정확히 부합. 이전 프로젝트 Slide 9와 유사 계열이나 이번 브리프는 2026~2028 4개 시점만 존재해 더 단순한 구성
- **Structural Check**: 문제 없음. 원문 수치·일정 그대로 유지, 임의 연도 확장 없음

---

## Slide 12. 기술개발 인력

- **Core Message**: 코솔러스는 기술개발을 뒷받침하는 조직 체계를 갖추고 있다
- **Content Roles**:
  - Primary: 조직도 이미지(015_조직도)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region(원본 조직도 이미지, 슬라이드 중앙 대형 배치)
- **Selected Layout**: Visual + Insight Layout — Variant A(Image+Explanation)의 단일 전체 이미지 변형
- **Layout Selection Reason**: 완성된 원본 조직도 이미지가 이미 존재하므로 Content Visualization Freedom의 "완성된 원본 Graph/Chart 존재 시 원본 이미지 재사용" 원칙에 따라 원본을 그대로 사용한다. `020_organization.md`(Organization Chart — Curved Leadership)는 데이터로부터 신규 조직도를 구성하는 문서라 원본 이미지가 있는 이번 경우에는 적용하지 않는다(원본 재구성 금지 원칙 우선)
- **Structural Check**: 문제 없음. 이미지 원본 비율 유지, 과도한 확대로 인한 화질 저하 방지

---

## Slide 13. 보유 기술 및 인증 현황

- **Core Message**: 코솔러스는 등록 8건·국내출원 11건·PCT 4건 등 총 23건의 지식재산권과 6종의 정부·기관 인증을 보유하고 있다
- **Content Roles**:
  - Primary: 특허 현황(등록8/국내출원11/PCT4=총23건), 인증 현황(001~006 이미지 6종)
  - Dependent: 대표 특허 목록(원본 임베드 표 이미지에서 확인된 실제 특허명 일부 활용)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 비교(대등한 2개 영역 — 특허 table vs 인증 이미지)
- **Content Regions**: Region A(좌, 특허 현황 — 총건수 요약 + 대표 특허 table) / Region B(우, 인증 현황 — 001~006 배지 그리드)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프가 "좌측 특허 table, 우측 인증현황"을 명시적으로 요청 — 대등한 위계의 두 영역을 병렬 제시하는 구조에 부합
- **Structural Check**: **[확인사항]** ① 특허 건수(등록8/국내출원11/PCT4=23건)는 이전 프로젝트에서 사용자 확인을 거쳐 확정된 수치를 그대로 재사용(신규 생성 아님) — `material_analysis_v3.json`의 원본 임베드 표 이미지(7건 확인)는 상호 배타적이지 않은 대표 사례로 함께 활용 가능. ② 인증 이미지 004(벤처기업확인서)는 문서상 타사('주식회사 앱클러스') 자료로 보이나 사용자가 "그냥 넣고 진행해"라고 명시적으로 확정 — 001~006 전체를 그대로 사용하고 슬라이드에는 별도 경고 문구를 넣지 않는다(사용자 지시 그대로 반영)

---

## Slide 14. 흑연 음극재 시장 성장가능성

- **Core Message**: 글로벌 음극재 시장은 2024년 50억 달러에서 2035년 115억 달러로 성장하지만, 한국은 흑연 원료의 중국 의존도가 97~99%에 달해 미국·EU 규제에 따른 공급망 재편이 필요하다
- **Content Roles**:
  - Primary: 컬럼1(글로벌 음극재 시장 성장 — 이미지 024), 컬럼2(중국 의존도 수치 + 미국·EU 규제 — 이미지 025)
  - Dependent: N/A
  - Shared Supporting: 각주(출처 3건)
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(2개 대등 주제)
- **Content Regions**: Region A(글로벌 음극재 시장) / Region B(중국 의존도+규제)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프가 "컬럼1 글로벌 음극재 시장, 컬럼2 나머지 — 2컬럼 구조"를 명시적으로 요청
- **Structural Check**: 문제 없음. 두 이미지 모두 원본 그대로 사용. 섹션 라벨 MARKET(이전 프로젝트 시장 계열 슬라이드와 일관성 유지)

---

## Slide 15. 사업화 모델

- **Core Message**: 정제비용 경쟁력 확보 → 배터리용 정제흑연 판매 → 고부가 제품 확대의 3단계로 수익원을 확장하며, 2027년 1억원에서 2029년 50억원 매출을 목표로 한다
- **Content Roles**:
  - Primary: 3단계 순차 흐름(정제비용 경쟁력 확보→정제흑연 판매→고부가 제품 확대)
  - Dependent: 각 단계 설명, 매출 목표(2027년 1억→2029년 50억원)
  - Shared Supporting: 방열시트(016)·사업화전략(017) 이미지
  - Conclusion/Takeaway: 매출 목표 수치
- **Relationship**: 순차(3단계 공정/전략 흐름)
- **Content Regions**: Region A(3단계 좌→우 순차 Component) / Region B(하단, 매출 목표 Output 정리 + 이미지)
- **Selected Layout**: Process / System Architecture Layout — Layout B(이미지 있음)
- **Layout Selection Reason**: "1단계→2단계→3단계"의 좌→우 순차 구조와, 하단에 최종 Output(매출 목표)을 정리하는 구조가 이 Layout의 Use When 조건에 정확히 부합. 단계별 이미지(방열시트/사업화전략) 존재로 Layout B 선택
- **Structural Check**: 문제 없음. 매출 목표 수치는 원문 그대로("2027년 1억→2029년 50억원") 유지

---

## Slide 16. 고객사 분석

- **Core Message**: 국내 배터리 3사와 음극재 기업을 중심으로 약 1조원 내수시장이 추정되며, 중국산 대체와 공급망 안정성을 원하는 한국·일본·유럽 수요를 공략한다
- **Content Roles**:
  - Primary: 시장 규모 주장(약 1조원 내수시장 추정), 주요 고객 후보(포스코퓨처엠·대주전자재료·HS효성 등)
  - Dependent: 공급망 다변화 수요(한국·일본·유럽)
  - Shared Supporting: 고객군·파트너 밸류체인 다이어그램
  - Conclusion/Takeaway: N/A
- **Relationship**: 종속(주장 + 근거 다이어그램)
- **Content Regions**: Region A(메시지 — 시장 규모+고객 후보 텍스트) / Region B(밸류체인 다이어그램 — 공급자→코솔러스→수요처 흐름)
- **Selected Layout**: Visual + Insight Layout — Variant D(Message+Evidence)
- **Layout Selection Reason**: "국내 1조원 내수시장" 핵심 주장을 밸류체인 다이어그램(Evidence)으로 뒷받침하는 구조에 부합
- **Structural Check**: **[판단 사항]** 브리프는 밸류체인 이미지를 "웹에서 서치"하라고 요청했으나, 로컬 처리·오프라인 원칙에 따라 실제 웹 이미지를 가져오지 않는다 — 대신 Design System §6 Shape/Connector 컴포넌트로 공급자(사용후배터리)→코솔러스(정제)→수요처(배터리3사/음극재기업) 흐름을 직접 구성한다. Content Visualization Freedom "국가·지역·거점·공급망 → Map"/구조 다이어그램 자유도 범위 안에서의 판단이며 임의 수치 생성 없음(추정치는 원문 "추정" 표기 유지)

---

## Slide 17. 경쟁사 대비 우수성

- **Core Message**: 코솔러스의 유도가열 공정은 BTR(중국)·Vianode(노르웨이)의 초고온 간접가열 대비 처리시간(1분 이내 vs 24~48시간)과 에너지 효율에서 압도적 우위를 가진다
- **Content Roles**:
  - Primary: 3사 비교(국가/기술/처리시간/특징) — COSOLUS/BTR/Vianode
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 유도가열 공정의 처리시간·효율 우위
- **Relationship**: 비교(3사, 동일 기준 반복 비교)
- **Content Regions**: Region A(3사 비교 table, 자사 열 강조) / Region B(026_유도가열우수성 이미지)
- **Selected Layout**: Comparison Matrix Layout + Competitive Advantage Highlight(자사 열 강조)
- **Layout Selection Reason**: 브리프가 "테이블 재구성 후 그림 삽입, 좌우 배치"를 요청하며, 원본 문서에 임베드된 COSOLUS/BTR/Vianode 실측 표(`material_analysis_v3.json` img2)와 이전 프로젝트 Slide 16이 동일 수치임을 확인 — 이전 프로젝트의 검증된 레이아웃(자사 열 강조 Comparison Matrix)을 그대로 재사용
- **Structural Check**: 문제 없음. 표 수치는 원본 임베드 표 및 이전 프로젝트와 완전히 일치, 임의 변경 없음

---

## Slide 18. 시장확대방안

- **Core Message**: 고순도 정제흑연은 음극재를 넘어 전도성 첨가제·방열 첨가제 등 고부가 업사이클 제품과 그래핀 원료로 확장 가능하며, 이미 목표 고객사들과 협의를 진행 중이다
- **Content Roles**:
  - Primary: 중심 소재(고순도 정제흑연) → 확장 적용처(전자소재/방열소재/그래핀 원료)
  - Dependent: 목표 고객사(S사 1차 벤더 XX하이테크·XX시냅스, XX쎄미켐)
  - Shared Supporting: 방열시트전망(027)·BM전망(028) 이미지
  - Conclusion/Takeaway: N/A
- **Relationship**: 전체-부분(하나의 소재 → 다수 적용처로 확장)
- **Content Regions**: Region A(중심 소재 허브) / Region B(적용처별 스포크 — 전자소재/방열소재/그래핀) / Dependent Region(목표 고객사+시장 전망 이미지)
- **Selected Layout**: Product / Application Layout — Layout B(방사형, Hub-and-Spoke)
- **Layout Selection Reason**: 하나의 중심 소재가 여러 산업으로 확장되는 Hub-and-Spoke 관계에 정확히 부합. 이전 프로젝트 Slide 17과 동일 계열 콘텐츠라 레이아웃 재사용
- **Structural Check**: 문제 없음. 이전 프로젝트 v2 라디얼 마크업 구조를 재사용해 어댑트

---

## Slide 19. 투자 유치 계획

- **Core Message**: 양극재·음극재 사업화 자금으로 61억원을 유치했으며, 2026년 Series A2(10억원 확정)에 이어 2028년 Series B를 준비 중이다
- **Content Roles**:
  - Primary: 투자유치 현황(누적 61억원, 2025년 Series A1 — 에코프로파트너스), 투자유치 계획(2026년 Series A2 10억원 확정-MYSC, 2028년 Series B)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차(현황→계획) — 2개 컬럼으로 병렬 제시
- **Content Regions**: Region A(투자 유치 현황) / Region B(투자 유치 계획)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프가 "2개 컬럼 구조로 생성"을 명시적으로 요청
- **Structural Check**: 문제 없음. 61억원·10억원(MYSC, 2026.07 확정) 수치는 브리프 원문 그대로 유지

---

## Slide 20. 울산 기술사업화 계획

- **Core Message**: 울산 사업장을 구축해 파일롯 라인을 설치하고, 연구원 기술이전·석박사 인력 채용·공동연구를 거쳐 시제품 생산과 고객 검증을 통해 시장경쟁력을 확보한다
- **Content Roles**:
  - Primary: 4개 순차 항목(사업장·파일롯 라인 설치/기술이전+공정융합/석박사 채용+공동연구/시제품생산+고객검증)
  - Dependent: N/A
  - Shared Supporting: 014_흑연파일럿 이미지
  - Conclusion/Takeaway: N/A
- **Relationship**: 순차(추진 단계)
- **Content Regions**: Region A(4개 순차 bullet) / Region B(파일롯 이미지)
- **Selected Layout**: Visual + Insight Layout — Variant A(Image+Explanation)
- **Layout Selection Reason**: 순차적 추진 항목 설명과 원본 파일롯 이미지를 함께 보여주는 구조에 부합. 4단계가 뚜렷한 Process Component 명칭(예: 설비명)이라기보다 추진 활동 서술에 가까워 Process/System Architecture보다 Visual+Insight가 더 적합
- **Structural Check**: 문제 없음. 이전 프로젝트에 없던 신규 슬라이드(구 프로젝트는 "지역 내 기술사업화 현황 및 계획"이 현황+계획 혼합이었으나 이번 브리프는 계획 중심 4단계로 재구성)

---

## Slide 21. 지역 활성화

- **Core Message**: 울산 내 대기업·이차전지 특화단지 기업과의 거래·협업을 추진하고, 시제품 양산 전환 시 지역 청년 인력을 우선 채용해 지역 사업화 네트워크를 구축한다
- **Content Roles**:
  - Primary: 지역 내 거래계획(현대중공업 납품/양극재 재활용 기업 협업-고려아연·LS MnM·코스모화학/현대차 공급망 프로젝트), 지역 내 고용계획(청년 생산인력 우선채용/산학연 네트워크 구축)
  - Dependent: N/A
  - Shared Supporting: N/A
  - Conclusion/Takeaway: N/A
- **Relationship**: 병렬(거래계획 vs 고용계획, 대등한 2주제)
- **Content Regions**: Region A(거래 계획) / Region B(고용 계획)
- **Selected Layout**: L25 Symmetric Two-Split
- **Layout Selection Reason**: 브리프가 "2개 컬럼 구조로 만들어"를 명시적으로 요청 — 대등한 두 주제를 동일 비중으로 병렬 제시하는 구조에 부합. 이전 프로젝트 Slide 24와 동일 계열(거래/고용)이라 마크업 어댑트
- **Structural Check**: 문제 없음. 브리프의 "권장 시각자료(거래·고용·협력 3개 효과)"는 두 컬럼 내부의 강조 포인트(아이콘/pill)로 흡수해 별도 3분할 Region을 새로 만들지 않음(2컬럼 요청과 상충하지 않도록 조정)

---

## Slide 22. 지역이전 실행계획

- **Core Message**: 2026년 말부터 본사·부설연구소·파일롯 공장을 울산 이차전지 특화단지로 단계적으로 이전해, 초기 2명에서 연구·파일롯 인력 10명 규모로 확대한다
- **Content Roles**:
  - Primary: 이전 개요(형태/지역/시기/규모)
  - Dependent: 핵심 목표(고순도 정제흑연 실증·양산 기반 구축+글로벌 시장 진출)
  - Shared Supporting: 034_울산 이미지
  - Conclusion/Takeaway: N/A
- **Relationship**: 전체-부분(이전 개요 각 항목) + 단일 콘텐츠(목표)
- **Content Regions**: Region A(좌, 이전 개요 항목+핵심 목표) / Region B(우, 울산 이미지)
- **Selected Layout**: Business Site Map Layout (Pin + Outside Card) — 브리프 요청("좌측 내용, 우측 사진")에 맞춰 Pin 지도 대신 원본 사진(034_울산)을 Outside Card와 함께 배치
- **Layout Selection Reason**: 특정 지역(울산 이차전지 특화단지)의 이전 계획을 이미지와 함께 전달하는 단일 사업장 조건에 부합. 이전 프로젝트 Slide 25와 동일 자산(034_울산 = s25-ulsan-cluster.jpg) 재사용 가능
- **Structural Check**: 문제 없음. 이미지는 원본 그대로 재사용(v2에서 이미 사용 중인 자산과 동일 소스 확인됨)

---

## Slide 23. 클로징

- **Core Message**: COSOLUS, small actions, BIG DIFFERENCE — 흑연 음극재 재활용으로 배터리 순환경제와 지역 이차전지 산업의 성장을 함께 만든다
- **Content Roles**:
  - Primary: 브랜드 모토
  - Dependent: Contact 정보(대표 연락처)
  - Shared Supporting: N/A
  - Conclusion/Takeaway: 전체 발표를 종합하는 비전 메시지
- **Relationship**: 단일 콘텐츠
- **Content Regions**: Region(Closing Message + Contact)
- **Selected Layout**: L22 Closing / Contact
- **Layout Selection Reason**: 최종 메시지와 연락처를 정리하는 클로징 목적에 정확히 부합. Hard Rule §7이 Motto를 Closing 페이지에서 사용 가능하도록 명시적으로 허용
- **Structural Check**: **[브리프 범위 외 추가사항]** 이번 브리프(204개 문단)에는 명시적 클로징 슬라이드 지시가 없다 — 이전 프로젝트(v2)에서 이미 승인된 클로징 디자인/패턴을 그대로 재사용해 추가한 것으로, 최종 보고 시 이 판단을 별도로 표시함

---

## [3]→[5] 인계 사항

1. **원본 이미지 자산**: 브리프에 명시된 이미지 파일(019/007/008/009/020~028/013/014/015/023/026/034 등)은 `HWP_PPT_추출자료_정리본/images/`에서 확인 완료, `web_ppt/v3/assets/images/`로 복사해 사용한다. `.bmp` 원본은 `.png`로 변환한다(픽셀 내용 변경 없음).
2. **웹 이미지 검색 미수행**: Slide 8(정책 모멘텀), Slide 16(고객사 분석 밸류체인)은 브리프가 "웹에서 찾아서/서치"를 요청했으나 로컬 처리 원칙에 따라 실제 웹 이미지를 가져오지 않고 Design System Shape/Icon 컴포넌트로 대체 구성한다.
3. **인증 이미지 004 처리**: 사용자가 명시적으로 확정한 대로 001~006 전체를 그대로 사용하며 슬라이드 내 경고 문구는 넣지 않는다(보고서에만 기록).
4. **금액 수치 없음**: Slide 3(사업비 집행계획)은 항목·용도만 표시, 금액 칸을 만들지 않는다.
5. **재사용 수치**: Slide 13(특허 8/11/4=23건)은 이전 프로젝트 확정치 재사용. Slide 17(COSOLUS/BTR/Vianode 비교)은 원본 문서 임베드 표 실측치와 이전 프로젝트 수치가 일치함을 확인 후 재사용.
