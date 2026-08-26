# QA Report — web_ppt/v1 (기술개발_지원사업_연구개발계획서)

## 0. 전체 Typography Audit
`qa_render.py --audit-fonts`로 21개 슬라이드 전체 실측 font-size를 감사. 위반 1건 발견(아래 참조), 그 외 전체 슬라이드에서 Hard Rule §9/§10/§12 및 Design System §3 기준(Source/Footnote 12pt, 그 외 14pt 미만 없음, Body 16pt 미만 없음, Section Label 12pt, Sub Message 14pt, Content Header/Region Header 20pt, Main Title 28pt) 위반 없음을 확인.

## 1. 발견 및 수정된 문제 (모두 1회 자동 수정 범위 내에서 해결, Layout 변경 없음)

| 슬라이드 | 문제 | 원인 | 조치 |
|---|---|---|---|
| 3 (과제 개요) | 우측 컬럼("핵심 성능" 배지·Key Stat 박스) 좌측이 잘려 보이는 렌더링 결함 | 2컬럼 flex 레이아웃에서 v-divider 좌표(660px)가 실제 컬럼 경계(684px)보다 안쪽(gap 시작 지점 이전)에 위치, 우측 콘텐츠 시작점과 거의 겹침 | v-divider를 gap 중앙(640px)으로 재배치 |
| 7 (기존 기술의 문제) | 좌우 두 컬럼 모두 헤더 바로 아래와 본문 사이에 큰 빈 공간이 위·아래로 분리되어 발생(중앙 정렬로 인한 이중 여백) | `justify-content:center; flex:1 1 auto`로 짧은 본문을 컬럼 전체 높이 중앙에 배치 | 중앙 정렬 제거, 헤더 바로 아래 여백(28px)만 두고 콘텐츠를 상단 정렬 |
| 8, 9 (개발 필요성 / 개발 솔루션) | Claim & Proof 그리드 하단에 슬라이드 절반 가까운 큰 빈 공간 발생(콘텐츠가 그리드 상단에만 붙어 보임) | `.proof-grid`가 `flex:1 1 auto`로 커진 컨테이너 안에서 항목이 기본 정렬(상단)로만 배치 | `.proof-grid`에 `align-content:center` 추가 — 항목들을 가용 세로 공간 중앙에 배치(style.css 공통 수정, 두 슬라이드 동시 해결) |
| 10 (핵심 기술 구성) | 3개 병렬 Column Header 중 2·3번째가 2~3줄로 줄바꿈되며 Header Bar 높이가 서로 달라짐(Hard Rule §10 고정 Header 높이·Parallel Alignment 위반) | Header 텍스트에 기술명+기관명을 `<br>`로 함께 넣어 길이가 과도, 컬럼 폭(약 370px) 대비 줄바꿈 발생 | Header는 기술명만 남기고, 기관명은 Header 아래 별도 Caption 줄로 분리. 3번째 컬럼은 "고접착 우레탄 아크릴레이트 기술"에서 "기술"을 생략해 1줄 유지 |
| 21 (클로징) | `.contact` 텍스트 실측 11.25pt로 Source/Footnote 최소 기준(12pt) 미달 | `.closing-content .contact`가 `font: 300 15px/1.6`로 지정(15px=11.25pt) | 16px(=12.0pt)로 수정 |

## 2. 재검증
위 5건 모두 수정 후 해당 슬라이드를 1·1-b·2 절차로 재검증(스크린샷 재확인 + font-audit 재실행)해 문제 해소를 확인. 10번 슬라이드는 1차 수정(Header에서 `<br>` 제거) 후에도 3번째 컬럼 Header가 여전히 2줄로 남아, 2차 수정(Header 텍스트 축약)까지 진행 — Layout 변경(예: three-column → 다른 Layout 전환) 없이 2회 이내에 해결됨.

## 3. 미해결 항목
없음. 21개 슬라이드 모두 Layout Compliance / Typography Compliance / Visual Quality Check 통과.

## 4. 참고 — 의도적으로 유지한 여백
슬라이드 4, 11, 13~18(로드맵 5장 포함)은 원본 콘텐츠 분량이 상대적으로 적어 컬럼 하단에 여백이 남아 있으나, Claude PPT Design System §5 Content Density 원칙("콘텐츠가 적은 경우에도 화면 전체를 억지로 채우기보다 Content Group 자체의 응집성을 우선")에 따라 상단 정렬 + 자연스러운 하단 여백으로 유지했다. `flex:1`/`space-between`/`margin-top:auto` 등으로 강제로 채우지 않았다.
