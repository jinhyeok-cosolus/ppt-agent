# QA Report — cosolus-ir-deck-C / web_ppt/v1

QA 절차: `.claude/skills/web-ppt-generator/SKILL.md` "생성 후 QA 절차"(Layout Compliance Check + `scripts/qa_render.py` 렌더링 + Visual Quality Check + 최대 2회 자동 수정·재검증)를 15개 슬라이드 전체에 적용.

## 요약

- 15장 전체 렌더링 성공(Playwright/Chromium, 렌더링 오류 없음).
- Layout Compliance Check에서 발견·수정: 4건 (Slide 4, 7, 10, 13 — A 프로젝트에서 이미 확인된 결함과 동일 유형, 재현 여부 대조 후 교정).
- Visual Quality Check(스크린샷 육안 확인)에서 추가로 발견·수정: 4건 (Slide 4/5/12 아이콘 렌더링 버그, Slide 6/8 이미지 오배치, Slide 14 여백 불균형, Slide 15 여백+로고 5종 오배치).
- 2회 재시도 한도 내 전부 해결. `qa_report.md`로 넘어간(2회 후에도 미해결) 슬라이드는 없음.

## 슬라이드별 상세

### Slide 4 — 비즈니스 모델 (Three-Column)
- **Layout Compliance**: three-column.md §5(Main Visual이 Column 콘텐츠 영역의 55~65% 차지) 대조. 초안에서 `.tc-visual`이 flex:1로 크지만 내부 아이콘(54px 글리프)만 있어 실제 시각 밀도가 낮은 A와 동일한 패턴이 될 것으로 판단, 생성 시점에 `.tc-icon-frame`(210px 원형 틴트 타일 + 92px 아이콘)을 선반영.
- **Visual Quality Check (1차 스크린샷)**: 가운데 컬럼(환경 저감) 아이콘 `&#9899;`(⚫)이 Chromium 이모지 폰트에서 광택 있는 검정 구체로 렌더링되어 좌/우 컬럼의 플랫 틴트 아이콘과 색상·스타일이 불일치(브랜드 컬러 미적용).
- **수정**: `&#9899;&#65038;`(텍스트 프레젠테이션 변형 선택자 VS15 추가)로 이모지 렌더링을 억제, `var(--c-secondary)` 틸 색상 적용.
- **재검증**: 3개 컬럼 아이콘이 모두 동일한 톤·크기로 렌더링됨을 확인. 1회 수정으로 해결.

### Slide 5 — 기존 재활용 공정의 한계 (Process+Comparison)
- **Visual Quality Check**: 1단계 "블랙매스 투입" 아이콘이 Slide 4와 동일한 이모지 렌더링 버그.
- **수정**: 동일하게 VS15 적용. 1회 수정으로 해결.

### Slide 6 — 솔루션1 개요 (Before-After Variant A)
- **Layout Compliance**: before-after.md Comparison Frame(4.1) 대조, 이상 없음.
- **Visual Quality Check**: 우측 "COSOLUS 추출제 (1.5세대)" 이미지(`recyion-structure.png`)가 실제로는 화학구조식이 아니라 "평형선/조업선/단수계산" 범례 차트였음 — 원본 자료 `img8`이 material_analysis.json에는 "RECYION류 R기 일반형 추출제 화학구조식"으로 잘못 기술되어 있었음(원본 추출 단계의 인덱스 오류로 추정).
- **조치**: 원본 `extracted_images/img6.png`를 직접 열람해 실제 R기 일반형 추출제 구조식(D2EHPA와 동일한 골격에 R 대신 실제 알킬기가 채워진 구조)임을 육안 확인 후 `recyion-structure.png`를 이 파일로 교체(임의 생성 없이 실제 원본 이미지로 대체).
- **재검증**: 좌/우 모두 화학구조식으로 정상 비교됨을 확인. 1회 수정으로 해결.

### Slide 7 — 핵심기술 성능·원가 경쟁력 (Table Comparison)
- **Layout Compliance**: table-comparison.md 대조 결과 3건 확인, 생성 시점에 선반영:
  - §6 Header Row 통일 Fill — A는 '구분' 헤더에 `background:transparent` 인라인 예외를 둠 → C는 인라인 예외 제거, 4개 헤더 모두 Main Color Fill 통일.
  - §5 Cell 중앙 정렬 기본 — A는 `.crit`(기준 라벨) 셀이 좌측 정렬 → C는 중앙 정렬로 수정.
  - §3 Overall Region Map — A는 Row 2개뿐인 좁은 표 아래 521px Body Box에 방치된 큰 빈 공간 → C는 `.tcmp-wrap`(flex column)으로 감싸고 Cell padding 확대(10px→22px) + `.tcmp-highlight-band{margin-top:auto}`로 Highlight Band를 하단에 정렬, 빈 공간을 "의도된 여백"으로 재배치.
- **Visual Quality Check**: 스크린샷 확인 결과 3건 모두 정상 반영, 추가 문제 없음. 생성 시점 반영만으로 해결(추가 재수정 불요).

### Slide 8 — 솔루션1-2 DLE (Before-After Variant A)
- **Visual Quality Check**: 좌측 "기존 DLE(증발법)" 이미지(`atacama-salt-flat.png`)가 실제로는 칠레 아타카마 염호 사진이 아니라 벨기에 국기였음 — 원본 `img9`가 material_analysis.json에는 "칠레 아타카마 염호 리튬 채굴장 항공사진"으로 잘못 기술.
- **조치**: 원본 `extracted_images/img10.jpeg`를 열람해 실제 아타카마 염호 증발지 항공사진(다색 증발조·산맥 배경)임을 확인 후 교체.
- **재검증**: "Chile, Atacama Salt Flat" 캡션과 실제 이미지가 일치함을 확인. 1회 수정으로 해결.

### Slide 9 — DLE 기술 동향 비교 (Table Comparison)
- Layout Compliance·Visual Quality Check 모두 문제 없음.

### Slide 10 — COSOLUS DLE 강점·성과 (Benefit+Impact)
- **Layout Compliance**: benefit-impact.md 대조 결과 2건 확인, 생성 시점에 선반영:
  - §1 "Core Technology는 Main Title에서 이미 전달되므로 본문은 Benefit 증명에 집중" — A는 본문 최상단에 Main Title과 의미 중복되는 `KEY ADVANTAGES OF EXTRACTANT-SEPARATOR` 블록을 별도 배치 → C는 이 블록을 제거하고, 4개 핵심 강점을 관련성에 따라 좌(②④ 분리막 관련)/우(①③ 추출제·공정 관련) Benefit Area의 Supporting Text로 분산.
  - §7 Avoid "큰 KPI 숫자 + 넓은 여백... 금지" — A는 `.bi-evidence{justify-content:center}` 안에 "3%→90%" 숫자만 배치 → C는 실측 수치(3%/90%/50%)를 그대로 사용한 Before/After 막대 비교(`.evidence-bar-*`)로 Evidence Visual을 재구성.
- **Visual Quality Check**: 좌우 Benefit Area의 시각적 균형·Divider·Supporting Text 배치 확인, 문제 없음. 생성 시점 반영만으로 해결.

### Slide 11 — 솔루션2 개요 (Before-After Variant A)
- 문제 없음.

### Slide 12 — 핵심기술 상세 (Process+Comparison)
- **Visual Quality Check**: 2번째 스테이지 "전처리·블랙매스" 아이콘이 Slide 4/5와 동일한 이모지 렌더링 버그.
- **수정**: 동일 VS15 적용. 1회 수정으로 해결.

### Slide 13 — 경쟁력 가격·기술 우위 (Before-After Variant B)
- **Layout Compliance**: before-after.md §5.1 기본 Column 폭(Criteria 20% : Existing 39% : Improved 41%) 대조 — A는 existing/improved가 39%:39%로 동일 폭(§5.1 위반) → C는 `colgroup`(`table-layout:fixed`)으로 20:39:41 비율을 명시 적용해 생성 시점에 선반영.
- **Visual Quality Check**: 렌더링 결과 Improved(COSOLUS) 컬럼이 Existing보다 약간 넓게 표시됨을 확인, 정상. 추가 수정 불요.

### Slide 14 — 투자포인트 (Two-Column Summary)
- **Visual Quality Check(1차)**: 좌우 컬럼 모두 상단에 콘텐츠가 몰리고 하단에 큰 빈 공간이 방치됨(Design System의 "본문 중앙·하단에 콘텐츠 없이 비어 보이는 영역 발생 방지" 원칙 위반 소지).
- **수정**: `.summary-col`에 `justify-content: space-between` 적용(기존 `margin-bottom` 고정 간격 방식 대체), `.summary-highlight`의 `margin-top:auto` 제거(상위 컨테이너가 간격을 담당하도록 정리).
- **재검증(2차 스크린샷)**: 좌측(기술력/사업화 방향), 우측(투자라운드/Highlight Band/투자금 사용계획) 모두 컬럼 전체에 고르게 분산 배치됨을 확인. 1회 수정으로 해결.

### Slide 15 — 세계시장 진출 (Milestone / Customer References)
- **Visual Quality Check(1차)**: (a) 상단 목표 문구 이후 본문이 body-box 상단에만 몰리고 하단 절반이 비어 있음. (b) 일본 컬럼이 인도네시아 컬럼과 동일 높이로 stretch되어 텍스트 2줄만 있고 나머지가 텅 빈 형태. (c) 인도네시아 로고 5개 중 실제 이미지가 캡션과 전혀 다름을 발견(아래 참조).
- **로고 오배치 상세**: `logo-swap.jpeg`가 실제로는 MUKTI 로고, `logo-mukti.jpeg`가 실제로는 eCoNiL/ibattery 로고, `logo-econil.png`가 실제로는 IBC 로고, `logo-ibc.jpeg`가 실제로는 HLI Green Power 로고, `logo-hli.jpeg`는 로고가 아닌 무관한 흑백 스톡 사진(지구본을 든 손)이었음. 원본 `extracted_images`의 img70~74를 직접 열람해 각각 SWAP/MUKTI/eCoNiL·ibattery/IBC/HLI로 정확히 매칭되는 것을 육안 확인(material_analysis.json의 img71~75 라벨이 실제 콘텐츠보다 정확히 1씩 밀려 기술되어 있었음 — 체계적 인덱스 오류로 추정).
- **수정(1차)**: `.mile-regions`에 `align-items:flex-start` 적용 시도 — 그러나 두 `.mile-region`이 배경/테두리 없는 빈 div라 시각적 효과가 거의 없어 근본 해결이 아니었음(2차 판단에서 기각).
- **수정(2차)**: 본문 전체를 `.mile-wrap`(flex column, `justify-content:center`, height:100%)으로 감싸 body-box 내 수직 중앙 정렬, `.mile-goal`/`.mile-region-title`/`.mile-region-desc` 폰트 크기 확대, `.mile-photo`(130px→220px)·`.mile-logo-row img`(30px→40px) 실제 이미지 크기 확대(콘텐츠 날조 없이 기존 실제 자산만 확대). 5개 로고 파일을 위에서 확인한 올바른 원본으로 교체.
- **재검증(3차 스크린샷)**: 본문이 슬라이드 중앙에 균형 있게 배치되고 로고 5개가 모두 올바르게 표시됨을 확인. 2회 수정 한도 내 해결(일본 측 텍스트만 있는 비대칭 자체는 NC-04에 따라 검증되지 않은 로고를 사용하지 않기로 한 의도적 설계 판단이므로 임의 콘텐츠로 채우지 않음 — 잔여 비대칭은 결함이 아니라 원본 자료 한계로 기록).

## 발견된 이미지 인덱스 오류에 대한 별도 권고 (Escalation 성격)

이번 QA에서 `material_analysis.json`(A의 [2] 산출물을 그대로 재사용한 파일)의 이미지 설명·인덱스가 실제 추출 이미지 내용과 다른 사례를 2개 구간에서 확인했다:
- B07(img8) / B11(img9, img21) — 실제 내용과 다른 개별 이미지가 라벨링됨(불규칙한 오프셋).
- B22(img71~75, SWAP/MUKTI/eCoNiL/IBC/HLI 로고) — 5개 전부 정확히 1씩 밀려 라벨링됨(규칙적 오프셋).

이번 QA 범위에서는 실제 배치에 사용된 이미지(위 7개)만 원본과 대조해 교정했으며, `material_analysis.json` 문서 자체는 수정하지 않았다(이번 호출 범위 밖 — [2] 재작업 금지 지시 준수). **다만 위 두 구간 외에 다른 이미지 인덱스도 유사하게 밀려 있을 가능성이 있으므로, [2] material-analysis 산출물의 이미지 인덱스 전수 재검증을 별도로 권고한다.** 이번 C 실행에서 실제로 슬라이드에 배치되지 않은 이미지(예: `geothermal-lithium-plant.png`/img21 자리, mining-waste 계열 등)는 이번 QA에서 대조하지 않았다.
