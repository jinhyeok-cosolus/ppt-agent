# QA Report — v4 (지역창업계획패키지 사업계획서)

## 범위
[7] 피드백 반영(→[3] 재진입 포함) — v3(23장, 사업비 집행계획 포함) → v4(22장, 해당 슬라이드 삭제)로 전면 재구성. 전체 슬라이드가 A1(Divider)·A2(이미지 테두리 제거)·A3(Supporting Message 삭제) 3개 전역 규칙의 영향을 받았으므로, 22장 전체에 대해 Typography Audit(0번 단계에 준함) + 슬라이드별 Layout/Visual Quality Check를 수행했다.

## 0. Typography Audit (전체 슬라이드, `--audit-fonts`)
- 최초 스캔에서 실제 위반 2건 발견 → 즉시 수정·재검증 완료:
  1. Slide 5 `.tc-visual .cap`(이미지 캡션) — 매칭 CSS 규칙 부재로 브라우저 기본값(12pt)으로 렌더링됨. `.tc-col .tc-visual .cap { font: 300 14pt/1.3 ... }` 규칙을 `style.css`에 추가해 14pt로 수정.
  2. Slide 15 "(대한민국)" 보조 라벨 — 인라인 `font-size:0.85em`으로 14pt 부모 대비 11.9pt까지 축소되어 12pt 절대 하한 위반. `font-size` 축소 인라인 스타일 제거(부모 14pt 상속)로 수정.
- 재검증 결과 남은 12pt 항목은 모두 Hard Rule §9 Section Label(고정 12pt) 또는 §9/Cover 전용 Sub Message·Source/Footnote 역할(허용 하한 12pt)이며 실제 위반 아님.
- 최종 재감사(`font-audit.json`, 전체 22장): 미해결 위반 0건.

## 1·2. Layout Compliance + Visual Quality Check (슬라이드별)
- 신규/재구성 슬라이드(3, 4, 6, 9, 12, 13, 15, 17, 18, 19) 및 Divider 신규 추가 슬라이드(5, 6, 7)를 스크린샷으로 직접 검토.
- 1차 라운드에서 발견한 문제와 조치:
  - Slide 13: 좌우 컬럼 이미지가 작아 Content Area 하단에 과도한 빈 공간 발생 → 이미지 크기 확대(250→340px, 130→220px) + 컬럼 vertical-center 방식 조정.
  - Slide 17, 19: Header Box 바로 아래 콘텐츠를 `justify-content:center`로 배치해 Header와 텍스트 사이에 불필요한 빈 공간이 생기고 Content Group이 붕 뜬 것처럼 보임 → 상단 정렬(margin-top 고정) + 이미지 확대 + Gap 확대로 재조정, 잔여 여백은 하단 안전영역으로만 남도록 수정.
  - Slide 5, 7 (Three-Column, `.tc-col .tc-visual`): 동일한 원인(공유 CSS의 `justify-content:center`)으로 컬럼 내부가 중앙 정렬되어 상단에 여백이 생김 → 공통 CSS를 상단 정렬로 변경(`.tc-col .tc-visual`), Slide 7의 아이콘 크기를 48→64px로 확대해 시각적 비중 보완.
- 재검증(2회차) 결과 위 항목 모두 해결 확인(스크린샷 재캡처로 대조).

## 3. 미해결/수용된 항목 (Human Review 참고용, 자동 수정 범위 밖 아님 — 판단으로 수용)
- Slide 7(정책 모멘텀), 10(기술고도화 로드맵), 14(사업화 모델), 18(투자 유치 계획 우측 컬럼)은 "브리프 지시상 v3 콘텐츠 변경 없음"에 해당하는 슬라이드로, Part A3(Supporting Message 삭제)로 Content Start Y가 약 75px 앞당겨지며 본문 사용 가능 높이가 늘어난 결과 하단에 다소 넉넉한 여백이 남는다. 콘텐츠 자체(문구·수치)는 원본 브리프가 "변경 없음"으로 명시했으므로 임의로 새 문장을 추가하지 않았다 — Design System §5상 "콘텐츠량이 적어 의도적으로 응집 배치한 여백"에 해당한다고 판단해 수용했다. 겹침·잘림·정렬 오류는 없음.
- 이 항목들은 Layout 자체를 바꿔야 해결되는 문제가 아니라 콘텐츠량 문제이므로 자동 수정 범위(크기·Gap·정렬 조정)를 이미 적용했고, 추가 수정은 콘텐츠 확장(브리프에 없는 문장 생성)이 필요해 Content Visualization Freedom 원칙(자료에 없는 내용 임의 생성 금지)에 따라 보류했다. Human Review에서 여백 정도가 과도하다고 판단되면 추가 조정 가능.

## 4. A1(Divider) 커버리지 재점검
Part A1 지시문의 "table+image side-by-side" 예시에 Slide 16(경쟁사 대비 우수성, 비교표+레이더차트 좌우 배치)이 해당함을 재확인 — 최초 구현에서 누락되어 있었다. `.body-box`에 position:relative를 부여하고 표(590px)-Gap(48px)-이미지 사이 중앙에 `.v-divider`를 추가(left:614px, top:24px, height:399px). 표와 차트 그룹 사이 Gap을 32→48px로 확대해 Divider가 시각적으로 구분되도록 조정. 재렌더링으로 겹침·잘림 없음 확인.

## 결론
2회 수정 라운드 내에서 실제 위반(Typography 2건, Layout/Visual 5건, Divider 커버리지 1건)을 모두 해결했다. 위 "수용된 항목"은 결함이 아니라 콘텐츠량에 따른 의도적 여백으로 판단해 Human Review로 참고 표시만 남긴다.
