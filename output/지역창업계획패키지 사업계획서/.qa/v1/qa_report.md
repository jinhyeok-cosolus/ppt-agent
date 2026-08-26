# QA Report — web_ppt/v1 (26 slides)

## 0. 전체 Typography Audit (1회, [5] 최초 생성 직후)
`qa_render.py --audit-fonts`로 전체 26슬라이드 실측 font-size를 감사했다.

**초기 위반 8건 발견 → 모두 수정**
- 3-column 레이아웃(Slide 13) Key Message에 font-size 선언 누락 → 상속된 기본값(16px≈12pt)으로 렌더링됨 → `.tc-col .key-message`에 Three-Column Layout Reference 기준(ExtraBold 18pt, Primary color) 명시 추가
- `.pill`(투자 이력 날짜 태그, Slide 18) 12pt → 14pt로 상향(Source/Footnote 역할이 아닌 일반 콘텐츠이므로 14pt 최소 기준 적용)
- `.kpi-card .note`가 출처 각주(12pt, 허용)와 일반 remark 텍스트(Slide 10)에 혼용되고 있어 `.note.remark` modifier(14pt) 신설, Slide 10에 적용
- Slide 22 IP 요약 카드의 `label`에 인라인 12pt 오버라이드 → 제거(기본 14pt 복원)
- Stat Number(Design System §3, 24–30pt 범위 + 슬라이드 간 일관성 요구)가 슬라이드마다 18/20/22/26/44pt로 제각각 사용됨 → 모든 인라인 오버라이드 제거해 두 역할로 표준화: 그리드형 소형 스탯(`.kpi-card .num`) 24pt, 단독 강조형 대형 스탯(`.stat-block .num`) 30pt
- Visual + Insight Layout의 Supporting Header가 16pt로 구현되어 있었음(Layout Reference §8 매핑 기준은 Content Header Tier 20pt) → `.vi-insight .support-header` 20pt SemiBold로 수정

수정 후 재검증: 남은 12pt 미만 항목은 모두 Hard Rule이 명시적으로 허용하는 예외뿐임 — Section Label(Hard Rule §9, 고정 12pt), 표지 Sub Message(01_cover_design_V2.md 고정 16px=12pt), Source/Footnote 각주 2건(Slide 5, 12pt 허용 범위). 위반 없음.

## 1~4. 슬라이드별 Layout/Visual Quality Check + 자동 수정

### 발견 및 수정된 문제
| 슬라이드 | 문제 | 원인 | 조치 |
|---|---|---|---|
| 전체(Slide 2, 3, 6, 8, 11~25 등 Supporting Message 2줄인 슬라이드) | Main Title Supporting Message가 2줄로 줄바꿈될 때 본문(Content Area) 상단과 겹침 | `.body-box.with-support`가 1줄 기준 고정 Y(178px)로 설계됨 | Hard Rule §12가 최대 2줄을 허용하므로 2줄 기준 안전 여백(top 210px/height 446px)으로 전역 수정 |
| Slide 7 (Process 기술소개) | 콘텐츠가 상단에 몰리고 하단 절반이 빈 공간 | `.proc-wrap`에 수직 정렬 기준 없음(top-align 기본값) | `.proc-wrap`에 `justify-content:center` 추가 |
| Slide 8 (Benefit+Impact) | Evidence Visual이 Benefit Area 대비 지나치게 작아 중앙에 떠 있고 하단 여백 과다 | Benefit+Impact Layout Reference §6~§7이 요구하는 "Evidence 55~70% 비중" 미달 | 막대차트/비교박스 크기 확대(높이·폭·폰트) |
| Slide 17 (시장 확대 방안) | ① 방사형 Node 캡션이 Node 원과 겹침 ② 하단 "시장 확대 계획" 표가 슬라이드 하단으로 잘려 보이지 않음(Hard Rule §8 위반) | Product/Application Layout B의 기준 좌표(§6.9)를 이 슬라이드의 실제 Body Box 높이(446px, 원 기준 문서보다 낮음)에 맞게 재환산하지 않고 그대로 적용 | 허브/노드 지름·간격을 Body Box 높이에 맞게 축소 재계산, 하단 표는 컴팩트 리스트(합계 요약 + 3행)로 재구성해 잘림 제거(수치·거래 내용은 변경 없음) |
| Slide 22, 23 (테이블 셀) | "한국에너지기술연구원(울산)" 등 공백 없는 긴 한글 고유명사가 좁은 Table Column에서 옆 Column과 겹쳐 보임 | 전역 `word-break: keep-all`이 공백 없는 단일 단어 내부 줄바꿈을 막아, 좁은 Column 폭을 초과한 텍스트가 옆 Cell로 시각적으로 넘침 | 해당 셀에 의미 단위 수동 `<br>` 삽입(예: "한국에너지<br>기술연구원<br>(울산)")으로 줄바꿈 지점 확보 — 전역 keep-all 규칙 자체는 변경하지 않음(SKILL.md 요구사항 준수) |
| Slide 25 (지역이전 계획) | Business Site Map 카드(사업장 카드)가 아래 KPI 카드(이전시기/이전규모)와 겹침 | 카드 텍스트가 예상보다 많은 줄로 wrap되어 카드 실제 높이가 고정 배치 좌표(KPI 시작 Y)를 초과 | 카드 폭 확대 + 텍스트 간결화, KPI 블록 시작 Y를 하향 조정, Connector 좌표를 Pin 실제 위치 기준으로 재계산 |

### 검토했으나 수정하지 않은 항목(설계 원칙상 정상)
- 일부 텍스트 위주 슬라이드(Slide 11, 12, 19, 22 등) 하단에 여백이 남아 있음 — Claude PPT Design System §5 "콘텐츠가 적은 경우에도 화면 전체를 억지로 채우기보다 Content Group 자체의 응집성을 우선한다" 원칙에 따라 상단 정렬 유지, 인위적으로 늘리지 않음. 콘텐츠량 자체가 적어 발생하는 의도적 여백으로 판단.

## 최종 상태
26개 슬라이드 모두 최종 재렌더링 완료, Layout Compliance/Typography Compliance/Visual Quality 재검증 통과. 2회 자동 수정 한도 내에서 발견된 모든 문제 해결됨 — Human Review ②로 이관할 미해결 이슈 없음.

## 참고 — 수정 범위를 벗어난 환경 제약(에스컬레이션 아님, 참고용)
- **Pretendard 폰트 미설치**: 이 렌더링 환경(Windows, Playwright/Chromium)에 Pretendard가 시스템 폰트로 설치되어 있지 않아 `font-family: Pretendard, Malgun Gothic, ...` fallback으로 맑은 고딕이 대신 렌더링되었다. CSS의 `font-family` 선언 자체는 Hard Rule대로 Pretendard로 고정되어 있으며, 이는 `pptx-exporter/references/font_mapping.md`가 이미 명시한 "실행 PC에 Pretendard 미설치 시 대체 렌더링, 저장 폰트명은 Pretendard 유지"와 동일한 기존 프로젝트 관행이다. Pretendard 웹폰트 파일을 로컬에 받아 임베드하면 스크린샷상 폰트가 더 정확해지지만, 이번 세션에는 외부 네트워크 접근 도구가 없어 수행하지 못했다.
