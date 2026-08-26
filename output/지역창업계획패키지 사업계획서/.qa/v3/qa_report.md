# QA Report — web_ppt/v3 (23 slides)

## 0. 최초 생성 후 전체 Typography Audit
`qa_render.py --audit-fonts` (전체 23슬라이드) 실행 결과, 위반 40건 발견 — 전부 `.img-evidence/.mini-stat/.org-chart-wrap .cap`(이미지 캡션, 12pt)과 `.cert-badge span`(인증 배지 라벨, 12pt) 클래스에서 발생. 두 클래스는 Source/Footnote/각주 역할이 아닌 Caption/Auxiliary 역할(이미지 설명·배지 라벨)로 판단해 14pt로 상향 수정. `hdr-section-label`(12pt)과 표지 `submsg`(12px=12pt)는 Hard Rule §9 및 `01_cover_design_V2.md`가 명시적으로 고정한 값이므로 위반 아님(제외).

재검증 결과 폰트 위반 0건.

## 1회차 — Layout/Visual Quality Check (전체 23슬라이드 스크린샷 육안 검토)

발견 및 수정한 이슈:

| 슬라이드 | 문제 | 수정 |
|---|---|---|
| 2 (창업기업 정보) | `.ci-fact-label` 고정폭 120px에 "사업자등록번호"(7자) 라벨이 넘쳐 값과 겹침 | 라벨 폭 168px로 확대, `.ci-fact-row`에 gap 추가 |
| 3 (사업비 집행 계획) | 콘텐츠(항목 5개)가 상단에만 몰리고 하단 공백 과다 | 좌우 컬럼에 `justify-content:center` 적용해 응집 배치로 수직 균형 확보 |
| 8 (정책 모멘텀) | Three-Column 각 컬럼 내부(아이콘+메시지+본문)가 flex:1 없이 상단 고정, 하단 공백 과다 | 아이콘+메시지+본문을 `.tc-visual`(flex:1, 중앙정렬)로 묶어 컬럼 내 수직 중앙 배치 |
| 10 (기술 개발 현황) | 하단 2단 이미지 행에 `height:calc(100% - 132px)` 고정값 사용 — 실제 KPI 카드 높이와 어긋나 유도가열 설비 이미지가 상단 KPI 카드와 겹침 | body-box를 flex column화, KPI 그리드 flex:0 0 auto / 이미지 행 flex:1 1 auto + min-height:0으로 전환, 이미지에 max-height 지정 |
| 16 (고객사 분석) | `.vc-wrap`이 `align-items:stretch; height:100%`라 화살표(`.vc-arrow-col`)가 박스 높이가 아닌 전체 컨테이너 높이 기준으로 중앙정렬되어 박스와 화살표 위치가 어긋나고, 하단 문단이 슬라이드 밖으로 잘림(footer 영역과 겹침) | `.vc-wrap`을 `align-items:flex-start`로, `.vc-arrow-col`에 박스와 동일한 `height:92px` 지정 — 전체 높이가 자연스럽게 줄며 하단 문단도 잘리지 않게 됨 |
| 18 (시장확대방안) | 방사형(radial) 좌표를 4-node로 확장하며 하단 텍스트/이미지 블록과 겹치고 슬라이드 하단으로 오버플로(이미지 잘림) | 방사형 절대좌표 레이아웃을 허브(좌)+3개 가지(중앙, flex 세로 나열)+텍스트/이미지(우) 3컬럼 flex 구조로 전면 재구성 — Product/Application Layout B(Hub-and-Spoke)의 구조적 의도는 유지하되 견고한 flex 기반으로 구현 |
| 22 (지역이전 실행계획) | `.site-card` 절대좌표(`top:290px`)가 KPI 카드 영역 실제 높이보다 낮게 잡혀 이미지가 body-box 하단을 넘어 페이지 번호와 겹치며 잘림 | 좌(KPI 4개+핵심목표)/우(이미지+캡션) 2컬럼 flex 구조로 재구성, 이미지 `max-height:280px` 지정 |

## 2회차 — 재검증
위 7개 슬라이드를 포함해 전체 23슬라이드를 재렌더링·재검토. 모든 오버랩/오버플로 이슈 해소 확인. Typography 위반 0건 재확인.

## 남은 사항 (Layout 자체 변경 불필요 — 자동 수정 범위 내 조정으로 개선했으나 완전한 "빈 공간 없음" 상태는 아님)
- Slide 3(사업비 집행계획), 8(정책 모멘텀), 11(기술고도화 로드맵), 21(지역 활성화)는 원본 소스가 짧은 항목 나열형이라 응집 배치(중앙 정렬) 후에도 Content Area 하단에 다소의 여백이 남는다. Design System §5 "콘텐츠가 적은 경우에도 화면 전체를 억지로 채우기보다 Content Group 자체의 응집성을 우선"에 따라 자료에 없는 내용을 임의로 추가해 채우지 않았다. Layout 자체를 바꿔야 할 정도의 문제는 아니라고 판단해 Human Review 에스컬레이션 대상으로 표시하지 않았다.
- Slide 13 인증 이미지 004(벤처기업확인서)는 사용자가 이미 확정 지시한 사항(타사 표기 가능성 인지 후에도 포함 확정)이므로 QA 대상에서 제외.

## 결론
2회차 QA 절차 내에서 모든 발견된 Critical(오버랩/오버플로/폰트 위반) 이슈를 해결했다. 추가 Human Review ②로 에스컬레이션할 미해결 문제는 없다.
