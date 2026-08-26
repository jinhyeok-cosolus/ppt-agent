# cosolus-business-plan-2026 — 작업 상태 (2026-08-25 기준)

> **새 세션 재개 지침(최소 토큰 원칙)**: 새 세션에서는 이 파일(`WORK_STATUS.md`)만 먼저 읽는다. 전체 프로젝트 파일을 다시 탐색하거나 이미 확정된 슬라이드를 재분석하지 않는다. 아래 "다음 검토 순서"의 대상 슬라이드 작업에 실제로 필요한 파일/구간만 그때 선택적으로 읽는다(예: 다음 대상이 2p면 `slide_outline.md`의 Slide 2 섹션과 `index.html`의 slide-2 section만 필요 시 열람).

## 현재 단계
[6] Human Review ② 진행 중. web_ppt/v1은 아직 최종 승인 전. **슬라이드13을 5개로 분할해 전체 슬라이드 수가 17 → 21로 변경됨** — 아래 페이지 매핑을 항상 먼저 확인할 것.

**확정(2026-08-25): 13~17p(연차별 개발계획 5장) 구조 통일 — 사용자가 이 상태로 최종 확정, 추가 수정 없음.** 13p에서 여러 라운드 시안 조정 끝에 구조를 확정(좌측 Large Visual — wrapper 없이 원본 그대로, 원본 비율 유지한 채 확대 — + 우측 3기관 개별 Box — White 배경/연한 Gray Border, 아이콘 없음, 기관명만 Main Color Bold). Main Title은 5개 슬라이드 공통 "5개년 개발 로드맵", Sub Header는 "N차년도 | 해당 연차 주제". 이 확정 구조를 14~17p에도 동일 적용(내용·원본 이미지만 연차별 교체). 17p(5차년도, 그림12)만 scoped 규칙(`.slide-13y5 .s13y-hero-visual { flex: 2.3; }`)으로 Visual 폭을 소폭 넓힘 — 그림12가 서로 독립된 2개 Visual(반응 메커니즘 다이어그램+스케일업 장비 사진)을 원본 단계에서 이미 하나의 가로형(약 3.47:1) 이미지로 결합해 제공된 탓에 세로 공간 활용이 제한된다는 Field Test 결과를 `slide_outline.md`(Slide 13 섹션 Structural Check)에 기록 — **차기 원본 자료는 이런 경우 개별 이미지로 분리 제공받아 좌측 Visual Region 안에서 위·아래로 배치하는 편이 낫다**는 권고 포함(SKILL.md 등 공용 규칙에는 미반영, 참고 기록용).

## 페이지 번호 매핑 (슬라이드13 분할 이후)

| 현재 # | 내용 | 비고 |
|---|---|---|
| 1~12 | 표지~기관별 역할 및 협력 구조 | 번호 변경 없음 |
| 13~17 | 1~5차년도 개발 계획 (신규, 옛 슬라이드13 Timeline 분할) | 신설 |
| 18 | 사업화 전략 | 구 14 |
| 19 | 시장성 및 기대효과 | 구 15 |
| 20 | 확장 계획 | 구 16, 내용 미변경 |
| 21 | 마무리 | 구 17, 내용 미변경 |

## 확정된 슬라이드 (더 이상 손대지 않음)

- **슬라이드 3 (시장 및 산업 배경)**: [2026-08-26] 아래 이전 이력을 대체 — **teammate-version 팀원본으로 병합**(좌: ESL 확대 배경 4 Bullet+개념도 이미지, 우: 글로벌 시장 전망 KPI 1.6조→4.3조원+시장차트, 하단 결론 문구). 이전 s3-* 기반 구조는 미사용으로 보존만.
- **슬라이드 4 (제품 적용 구조)**: 제품사진(Optional) 제거, 단면도(Primary) 단독 중심 Visual화, "CORE TECHNICAL ADVANTAGE"를 우측 Column 내부에서 슬라이드 하단 Full-Width `.insight-box`로 이동.
- **슬라이드 5 (기존 기술의 문제)**: L07 → L25(Symmetric Two-Split)로 Layout 교체(Dominant Relationship 재판단 — 2개 병렬 문제그룹, 그룹A만 내부 인과). Divider를 프로젝트 공용 `.v-divider` 패턴으로 통일.
- **슬라이드 6/8/16(구)/20(신) (Three-Column)**: Body Vertical Divider 누락 수정 완료.
- **슬라이드 7 (개발 솔루션)**: [2026-08-25 확정] Table(1차) → Existing/Improved 2-Column(2차) → Criteria+BEFORE+AFTER 3-Column Presentation(3차) → 실제 `<table>` 3열 Table(4차) → 크기·배치 확대(5차) → Table 높이 소폭 축소+얇은 Vertical Divider 2개 추가(6차, 최종). 최종 구조: 구분/기존 열경화 방식(BEFORE)/개발 UV경화 방식(AFTER) 3열 Table, 구분↔BEFORE/BEFORE↔AFTER 사이 얇고 연한 Vertical Divider(`--c-line`), Row 구분은 최소 Horizontal Line, AFTER 헤더·Body 열만 Tint+Main Color 강조, 하단 Page Number와 여백 확보. **사용자가 이 상태로 확정 — 다음 세션에서 재검토 대상에서 제외.**
- **슬라이드 9 (정량적 개발 목표)**: 재판정 결과 Layout(3개 독립 Group 병렬 + Group 내부 소형 Table) 자체는 이미 실제 HTML과 일치 — `slide_outline.md`의 분류 표기만 정정("L17 Table/Matrix" → 정확한 분류). HTML 변경 없음.
- **슬라이드 10 (선행개발 실적)**: [2026-08-26] 아래 이전 이력을 대체 — **teammate-version 팀원본으로 병합**(좌: 고객사 평가 3단계 Milestone+장기신뢰성 평가결과, 우: 본 과제의 개선방향 2개 항목). 이전 s10-* 5-Step Flow 구조는 미사용으로 보존만.
- **슬라이드 11 (수행역량)**: 최종 구조 = 상단 3기관(소니드·한국생산기술연구원·코솔러스) Three-Column(기존 `tc-grid`/`comp-header`/`tc-divider` 골격 그대로 재사용) + 하단 Full-Width Visual Region(그림6·7). 공통 규칙 "Visual Region Utilization"(SKILL.md, 아래 참조) 적용해 그림 주변의 불필요한 회색 wrapper/background 제거, 원본 이미지를 종횡비 그대로 가능한 크게 직접 배치, 본문과 중복되던 하단 Caption 삭제까지 완료. **추가 수정 없이 현 상태로 종료 — 다음 세션에서 재검토하지 않는다.**
- **슬라이드 12 (기관별 역할 및 협력 구조)**: 최종 구조 = 상단 Full-Width "협력 흐름" Header(기존 `.comp-header` 재사용, 폭 70% 중앙 정렬) → 한국생산기술연구원 → 코솔러스(Main Color 강조) → 소니드 3기관 연결 박스(크기 확대) → 하단 Full-Width `.insight-box`(COLLABORATION OUTCOME). 의미가 불명확했던 역방향 피드백 Connector(`.psa-feedback`)는 제거. **추가 비율 조정 없이 현 상태로 종료 — 다음 세션에서 재검토하지 않는다.**
- **슬라이드 13~17 (1~5차년도 개발 계획)**: 옛 슬라이드13(5개년 Timeline 1장, 원본이미지 82px 축소로 식별 불가)을 연차별 5개 슬라이드로 분할 후, 사용자와 여러 라운드 조정을 거쳐 최종 구조 확정 — Main Title 공통 "5개년 개발 로드맵" + Sub Header "N차년도 | 연차 주제", 좌측 Large Visual(wrapper 없음, 원본 비율 유지 확대) + 우측 3기관 개별 Box(White+연한 Gray Border, 아이콘 없음, 기관명만 Main Color Bold). 17p(그림12)만 Visual 영역 flex 소폭 확대(scoped). **사용자가 13~17p 전체를 이 상태로 확정 — 다음 세션에서 재검토하지 않는다.**
- **슬라이드 18 (사업화 전략, 구14)**: Process/System Architecture 유지 재확인, 하단 원본 흐름도(그림13)가 이미 흐름 관계를 충분히 표현하므로 상단 텍스트 3단계의 중복 Process 장식(번호 원형·화살표)을 제거하고 `tc-col-body`/`tc-divider` 기반 단순 병렬 그룹으로 재구성 완료.
- **슬라이드 19 (시장성 및 기대효과, 구15)**: [2026-08-25 최종] 상단 핵심 KPI 2개(좌우+중앙 Divider) + 하단 기대효과 3개 Bullet List의 **원본 구조로 확정**. 중간에 시도했던 "상단 KPI/하단 3-Column Box" 재구성은 사용자 지시로 되돌림 — 재구성 시도 이력만 남기고 실제 파일은 원본 그대로.
- **슬라이드 21 (마무리)**: [2026-08-25] 1p(표지)와 동일한 Cover 배경 방식 적용 — `.cover-bg`(회색 이미지)+`.cover-overlay`(Green Gradient, 1p와 동일 정의 재사용) 추가, 기존 로고·페이지번호·문구·Thank You 내용은 그대로 유지. Deck 시작과 끝의 Visual Language 통일.

## 이번 Field Test로 수정된 공통 SKILL / Rule / Component

- `.claude/skills/web-ppt-generator/SKILL.md` — 전용 Layout 구조 규칙(L01~L33 카탈로그까지 확대), Primary/Optional Visual Region 배치, Image Legibility, Supporting Visual Value/배치, Insight/Conclusion Box 배치 범위, Caption/Source Annotation Tier 배치, Must Preserve 체크리스트 사전 발췌, 공용 컴포넌트 재사용(Insight Box/Divider/Header/Card/Typography/Stat) 다수 보강(상세는 파일 본문 참조).
- `.claude/skills/web-ppt-generator/references/design-rules.md` — "Layout Routing 판단 순서" 2번(복수 비교 근거 → Comparison 계열 선택에 **공통 Row/Column 비교축 존재** 조건 추가, 정량 데이터양만으로 Table 선택 금지)과 6번(Visual Requirement Compatibility → **Visual/Content Fit Compatibility**로 확장 — Visual 크기 적합성·Optional Visual 배제·Content Volume Fit 하위 기준 신설) 보강.
- `.claude/skills/slide-content-structuring/SKILL.md` — Dominant Relationship 판단(기존)에 이어 **"순차/인과 관계 성립 여부 검증"**(Claim이 하나뿐이어도 적용 — 시간순 나열 가능하다는 이유만으로 순차·인과 판단 금지) 항목 신설.
- `.claude/skills/web-ppt-generator/SKILL.md` — "전용 Layout의 구조 규칙 우선 적용 > Image Legibility" 바로 뒤에 **"Visual Region Utilization"**(과소 활용 금지 — Image Legibility의 반대 방향) 항목 신설: 회색/색상 배경 박스·과도한 padding·빈 wrapper로 이미지를 실제보다 작게 만들지 않고, 여러 이미지가 한 Region을 공유해도 동일 박스 크기를 기계적으로 강제하지 않으며, 불필요한 반복 Caption은 생략. 기존 Image Legibility/Supporting Visual Value/Caption 배치 규칙과 중복 없이 같은 절에 통합(별도 신규 섹션 아님). 슬라이드11에 이 기준을 실제 적용해 검증 완료.
- `.claude/skills/web-ppt-generator/scripts/templates/components/three-column.css` / `.html` — 신설(Header/Body 행 분리, Divider 골격).
- `web_ppt/v1/style.css`의 공용 클래스: `.insight-box`(신규), `.v-divider` 관련 override 패턴 정리, `.s13y-*`(연차별 슬라이드 공용), `.s11-*`(수행역량 하단 Visual Region), `.psa-header`(슬라이드12 Header 폭 조정) 신설.

## 아직 검토 필요 — 남은 슬라이드 & 다음 시작 지점

전체 21슬라이드 중 **2p를 제외한 3~21번 전체** 재검토·수정(또는 원본 유지 확정) 완료. **나머지는 2p뿐.**
10p(선행개발 실적)는 s10-step-label 2곳의 `<br>` 위치만 의미 단위에 맞게 최소 수정(문구·크기 변경 없음, 2026-08-25).

## 다음 검토 순서
**→ 2p만 남음 — 다음 세션 시작 지점.**
7p·11p·12p·13~17p·19p·21p는 사용자가 확정/원복 처리했으며 다음 세션에서 다시 검토 대상으로 삼지 않는다.

## 팀원본 병합 (2026-08-26)
`teammate-version/review_5_18_shared.html`에서 슬라이드 제목 기준으로 **3p(시장 및 산업 배경)·10p(선행개발 실적)** 2개만 팀원 결과 그대로 이식(재설계 없음). 공용 Header/Footer/페이지번호는 현재 프로젝트 것을 유지하고 body-box 내부만 교체, Base64 이미지 포함 그대로 반영, 팀원 CSS는 두 슬라이드 전용 클래스만 `.slide-3`/`.slide-10` scoped로 추가(다른 슬라이드 영향 없음, 기존 `.s3-*`/`.s10-*`는 미사용 상태로 보존). 두 슬라이드만 렌더링해 팀원 결과와 동일함을 확인. `shared.html`도 이 내용까지 반영해 최종 재생성 완료(21장 정상).

## 아직 실행하지 않은 것
- 전체 QA(`qa_render.py` 전체 슬라이드 대상) 미실행 — 지금까지는 변경된 슬라이드만 개별 렌더링 확인
- `web_ppt/v1/shared.html`은 2026-08-25 기준 최신 내용으로 재생성 완료(21장 정상 포함, 로드 확인) — 이후 2p 등 추가 수정 시 다시 stale로 취급할 것
- [8] pptx 변환 미실행
