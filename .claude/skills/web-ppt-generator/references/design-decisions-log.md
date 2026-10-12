# Design Decisions Log

이 문서는 `web-ppt-generator/SKILL.md`의 특정 규칙이 왜 생겼는지 근거가 된 과거 Field Test 회귀 사례를 모아둔 곳이다. **판단 기준 자체는 SKILL.md 본문에 그대로 있다** — 이 로그는 그 판단 기준을 매 [5]/[7] 호출마다 다시 읽을 필요가 없는 배경 설명으로 분리한 것뿐이며, 규칙을 이해하거나 실행하는 데 필수는 아니다. 규칙의 적용 방식 자체가 의심스럽거나("왜 이렇게까지 엄격한가") 새 사례를 이 문서에 추가할지 판단해야 할 때만 참조한다.

각 항목은 SKILL.md 본문에서 `(사유: design-decisions-log.md#앵커)` 형태로 역참조된다.

---

## flow-diagram-region-map-drift
**관련 규칙**: "전용 Layout의 구조 규칙 우선 적용 (Dedicated Layout Structure Enforcement)"

2026-08-24, `cosolus-ir-deck-F` Slide 16에서 Selected Layout은 정확히 Flow Diagram(L25)이었으나 실제 HTML은 그 문서의 Region Map·Connector 규칙 대신 다른 Layout용 범용 컴포넌트를 그대로 가져다 쓴 사례가 있었다. Selected Layout이 전용 Layout Reference 문서를 가리킬 때 그 문서의 Region Map·Connector 처리 방식을 "참고용 예시"가 아니라 "구현 명세"로 취급하도록 규칙을 강화한 계기다.

## l07-primary-visual-reversed
**관련 규칙**: "Primary/Optional Visual의 Region 배치"

2026-08-25, `cosolus-business-plan-2026` Slide 3에서 L07의 좌=Main Visual/우=Text 구조가 반전되고, Optional 보조 이미지를 넣기 위해 Primary Visual까지 축소된 사례가 있었다. Optional/Supporting Visual을 위해 원본 Reference의 Main Region 좌우 관계를 반전하거나 Primary Visual을 축소하지 않도록 규칙을 강화한 계기다.

## shared-visual-region-uneven-boxes
**관련 규칙**: "이미지 표시 크기·시각적 위계 > 과소 활용 금지(Visual Region Utilization)"

2026-08-25, `cosolus-business-plan-2026` Slide 11에서 그림6·7을 균등 폭 회색 박스에 강제로 맞춰 실제 이미지가 절반 이하 크기로 줄어든 사례가 있었다. 여러 이미지가 하나의 Visual Region을 공유할 때 동일한 박스 크기를 기계적으로 강제하지 않도록 규칙을 강화한 계기다.

## html-css-implementation-defects
**관련 규칙**: "구현 기준 (HTML/CSS Implementation Standards)" 전체(한글 줄바꿈/Divider 서브픽셀/Table 동일 폭 Column/아이콘 렌더링)

2026-08-19, C 테스트 `cosolus-ir-deck-C`에서 여러 슬라이드·레이아웃에 걸쳐 반복 발생한 구현 결함(단어 중간 줄바꿈, 서브픽셀 Divider 소실, Table Column 폭 불일치, 컬러 이모지 렌더링 등)을 공통 기준으로 정리해 이 섹션이 만들어졌다.

## shared-component-reinvention
**관련 규칙**: "공용 컴포넌트 재사용 (Shared Component Reuse)" 전체

2026-08-25, `cosolus-business-plan-2026` Field Test에서 아래 세 가지가 반복 확인됐다:
- Insight/Conclusion Box가 슬라이드마다 다른 border 방식으로 재발명됨
- Body 텍스트가 슬라이드별로 14~15pt로 임의 축소됨
- 이미 있는 Stat Number 공용 클래스를 두고도 슬라이드 전용 클래스로 동일 값이 중복 재정의됨

이 세 가지 재발명·중복·임의 축소를 막기 위해 "공용 클래스 통합", "Body Text는 Typography Tier 그대로 사용", "이미 있는 공용 클래스 우선 재사용" 규칙이 만들어졌다.

## image-display-size-by-role
**관련 규칙**: "이미지 표시 크기·시각적 위계(Image Display Size)" 전체, `flow-diagram-rules.md` "구조 정렬과 이미지 표시 크기의 구분", slide-structuring 2단계 "이미지별 시각 역할"

2026-10-08, `cosolus-ir-deck-G` Slide 1(공정 흐름도)에서 Node 종류별 고정 `max-width`×`max-height` 박스(예: Process 72×46px) 때문에 여러 단계가 담긴 가로형 공정 도해(유도가열 3단계 등)가 정사각형 시료 사진과 같은 크기로 축소돼 단계를 식별하기 어려웠다. 규칙상 "동일 위계 Node 유사 체감 크기"가 Node 종류 기준으로 해석됐고, 이미지별 시각 역할·정보 밀도는 [3] 산출물에 기록되지 않아 [5]에서 구분할 근거가 없었다. 같은 조사에서 `object-fit: cover`로 콘텐츠 사진이 최대 47% 잘리고, pptx 변환기가 `object-fit`을 무시해 그 이미지들을 최대 88% 늘려 넣던 사례(`cosolus-ir-deck-B` final.pptx)도 확인됐다. 이미지 중요도를 원본 크기·비율이 아니라 역할·정보 밀도·판독성으로 판단하고, 컨테이너 정렬과 이미지 표시 크기를 분리하며, 원본 비율 유지를 QA·pptx 변환까지 일관되게 적용하도록 정리한 계기다.

## flow-visual-composition
**관련 규칙**: `flow-diagram-rules.md` "Visual Composition — Lane Band·연결점·구분선", qa_render.py `flow_issues`

2026-10-12, `cosolus-ir-deck-G` Slide 1에서 이미지 크기만 역할별로 조정하자 배치 문제가 드러났다. 폐흑연 화살표의 불필요한 Z자 꺾임, 건식환원 이미지를 가로지르는 구분선, 소속 Lane이 모호한 유도가열 이미지, COSOLUS(2세대) 박스와 분기 브래킷의 겹침, 상단 결론 헤드라인에 가까운 Lane A 콘텐츠, 회수 화합물·폐흑연의 서로 다른 중심축이다. 원인은 다섯 가지였다. (1) Process가 연결선 위로만 쌓이는데 위쪽 공간 한도가 없었다. (2) Material Node는 이미지+라벨 블록 중심을 Lane에 맞춰서 이미지 높이가 바뀌면 연결점이 어긋났다. (3) 구분선이 고정 좌표였다. (4) PNG 투명 여백 때문에 박스 기준 간격과 보이는 간격이 달랐다(유도가열 이미지 하단 26%가 투명). (5) QA가 화살촉 marker 때문에 Connector 오버레이를 장식으로 판정하지 못해 오탐 32건만 내고 실제 충돌은 잡지 못했다. 그래서 가용 공간 → 이미지 크기 → Node 위치 → Connector → 구분선을 한 절차로 계산하도록 정리했다.

## common-header-ir-reference
**관련 규칙**: Hard Rule §9(공통 Header·좌측 Brand Line·페이지 번호·슬라이드 유형별 적용 범위)·§12 예외, `02_instruction_design_V1.md`(기업개요 구조 고정형), `01_cover_design_V2.md` Closing 절, `templates/style.css`·`components/company-overview.*`

2026-10-12, Design Consistency 개선. **목적**: 공통 디자인 요소를 실제 COSOLUS IR 레퍼런스(`docs/brand-assets/기업개요 Reference.pptx`)에 맞춰 통일하고 기업개요에만 최소 예외를 둔다. **원인**: 기본 템플릿 `style.css`가 브랜드 확정 전 임시 스타일이라 프로젝트마다 Header CSS를 새로 써서, 페이지 번호 클래스가 `.deck-page`/`.page-number`/`.header-page-number`로 섞이고 위치도 제각각이었다. QA는 `.deck-page`만 검사해 deck-F·G의 페이지 번호가 검사에서 빠져 있었다.

**주요 결정**
- **공통 Header**: 레퍼런스 실측값으로 재정비했다 — CI (46.5, 31) 높이 17.5 / Section Label (46.9, 64.7) / Main Title (41.6, 83.2) / Sub Message 우측 끝 1262.2·상단 28.5 / 상단 구분선 Y=57.6, X=41.6~오른쪽 끝, 0.5pt. 기업개요도 위치·크기는 동일하다.
- **좌측 Brand Line**: 레퍼런스의 2단 세로 띠(X=0, 폭 13.9 — Y 0~137 `#294F51` / 137~720 `#DFF1F1`)를 공통 요소로 추가했다. 일반 본문·기업개요에 적용, 표지·Closing에는 미적용.
- **페이지 번호**: 우측 끝 X=1248, 하단 Y=704, `.deck-page`로 통일. 표지·기업개요·Closing은 미표시. Bottom Safe Area(678)와 Footnote 영역은 유지.
- **기업개요**: 구조 고정형이며 핵심 메시지·Company Facts(최대 5행)·우측 사진만 교체한다. 전용 예외는 Sub Message White, 구분선 `#96A4A5`, Section Label `Company`(`#808080` 70%), 페이지 번호 없음. 우측 사진은 레퍼런스 그림 효과 그대로 투명도 60%.
- **정확한 선 두께 요소**: 브라우저는 1px 미만 테두리를 1px로 그린다. 그래서 투명 테두리 + `--pptx-line`/`--pptx-line-color` + `::after` 표시선(scaleY 0.5)으로 구현했다. 대상은 상단 구분선 0.5pt, Facts 행선 0.25pt이며, 이 변수를 선언한 요소에만 적용한다.
- **변환기(export_pptx.py)**: 이미지 opacity → 그림 투명도(alphaModFix), 텍스트 rgba → 글자 투명도, `text-transform` 반영, 정확한 선 두께를 연결선으로 변환(빈 컨테이너 도형 미생성), 연결선 테마 그림자 제거.
- **템플릿 버그 수정**: `templates/index.html` 상단 주석의 `<!-- SLIDES:INSERT -->` 문구가 주석을 일찍 닫아, 템플릿 주석을 둔 덱은 슬라이드가 표시되지 않았다.

**검증(4장 테스트 덱: 표지·일반 본문·기업개요·Closing 골격)**: QA 4장 모두 clean(겹침·잘림·Body Box·공통 요소·폰트). 기업개요 레퍼런스 대비 결과:
- 사진 평균 밝기: ref 163 / HTML 163 / PPTX 163
- 선 누적 진하기: ref 95·208·128 / HTML 95·207·127 / PPTX 95·207·127
- 변환 PPTX 좌표는 레퍼런스와 ±1px 일치

남은 차이: CI 폭 111.9 vs 114.8(레퍼런스는 벡터, 등록 PNG와 비율 차이), 텍스트 1~2px 렌더링 차, HTML 스크린샷에만 브라우저 안내 문구. 기존 deck-F·G 산출물은 변경하지 않았으며, 새 QA로 다시 검사하면 구 Header 위치·비표준 클래스로 지적된다(의도된 결과).

**상태(인수인계)**
- 브랜치 `visual-composition-image-sizing`, 마지막 커밋 `9e7f231`(Visual Composition). Design Consistency 변경은 **아직 커밋하지 않았다** — Skill·MD·템플릿·스크립트, `templates/assets/ci/`, `components/company-overview.*`, `introduction-images/company-overview-photo.png`, `docs/brand-assets/기업개요 Reference.pptx`(커밋 포함 대상).
- 커밋 제외: `output/cosolus-ir-deck-G/web_ppt/v1-composition-test/`, `output/cosolus-ir-deck-G/.qa/`, 기존 미추적 울산 프로젝트 폴더. 테스트 덱·비교 이미지는 세션 임시 폴더에 있어 다음 세션에서 사라질 수 있다(템플릿으로 재생성 가능).
- ~~미완료: Closing 디자인~~ → 아래 `closing-reference`에서 확정.

**다음 세션 확인 사항**
1. 사용자 승인 후 커밋(위 포함·제외 목록).
2. Supporting Message(Hard Rule §12)의 공통 클래스·X 위치가 템플릿에 없다(프로젝트마다 `.supporting-message`/`.conclusion-headline` 제각각) — Main Title(41.6) 또는 본문(64) 중 정렬 기준 결정 필요.
3. Section Divider 전용 Layout이 없어 좌측 Brand Line 적용 여부는 미정.
4. 기존 진행 중 프로젝트는 `new_version.py --from-latest`가 이전 CSS를 그대로 복사하므로 새 Header가 자동 반영되지 않는다(필요 시 마이그레이션).
5. 카탈로그 L22·L31 번호가 실제 pptx 슬라이드 번호와 어긋나 있다(범위 밖, 미수정).

## closing-reference
**관련 규칙**: `01_cover_design_V2.md` "Closing" 절, `templates/components/closing.*`, Hard Rule §9 슬라이드 유형별 적용 범위, export_pptx.py `add_box`

2026-10-12, Closing(마지막 표지)을 레퍼런스 `docs/brand-assets/Closing.pptx` 실측값으로 구조 고정형 컴포넌트화했다(기업개요와 같은 방식). 공통 Header·좌측 Brand Line·페이지 번호는 기존 결정대로 미적용. 교체 가능 요소는 마무리 메시지(최대 3줄)와 배경 사진뿐이다.

**재현 과정에서 정한 것**
- **사진**: 레퍼런스는 원본 우측 23.4% Crop + 좌우 반전. 그 결과물을 `closing-images/closing-photo.png`(925×900, 원본 해상도)로 등록해 CSS 변환 없이 쓴다. CI는 레퍼런스 원본 White CI(728×112)를 `assets/ci/cosolus-ci-white-closing.png`로 추가했다(기존 399px White CI와 비율이 약간 다름).
- **그라데이션**: PowerPoint는 색·투명도를 따로 보간하고 브라우저는 투명도를 곱한 값으로 보간해, 1.4~24% 구간이 최대 6/255 밝았다. 그 구간에 PowerPoint 방식으로 계산한 중간 stop 7개를 넣어 HTML·PPTX 모두 레퍼런스와 ±1로 맞췄다.
- **메시지 줄 간격**: 150% 줄 높이를 그대로 주면 PowerPoint는 남는 행간을 글자 위에 몰아 두어 변환 PPTX에서 줄마다 약 15px 아래로 밀렸다. 각 줄을 1.2 줄 높이로 두고 줄 사이 간격(25.6px)으로 띄웠다.
- **Thank You**: 레퍼런스가 ExtraBold에 굵게(b=1)를 추가 적용해 PowerPoint가 획을 덧입혀 그린다 — 브라우저에서는 900으로 근사(폭 차 9.5px → 2.5px).
- **변환기 그림자**: python-pptx 도형 기본 스타일(effectRef idx=2)이 테마 그림자를 끌어와, 반투명 오버레이 아래로 그림자가 비쳐 PPTX 전체가 약 14/255 어두웠다. 연결선(이전 수정)처럼 `add_box` 도형에도 그림자 상속을 끊었다 — HTML에 없는 그림자라 일반 본문·기업개요 PPTX에서도 그림자만 사라진다.

**PPTX 글꼴 굵기·줄바꿈(같은 날 후속)**: 변환기가 설치된 Pretendard 굵기별 패밀리 이름(예: "Pretendard SemiBold", b=0)으로 저장하고, 미설치 시 기존 방식("Pretendard" + 굵게)으로 돌아간다(`pptx-exporter/references/font_mapping.md` "굵기 매핑"). PowerPoint는 Pretendard 커닝을 적용하지 않아(한글 혼합 문장 최대 약 1.7% 넓음) 굵기를 정확히 맞추면 줄바꿈이 달라질 수 있어, 여러 줄 텍스트는 브라우저 줄 구성 그대로(`<a:br/>`, 행잉 인덴트는 줄별 상자) 옮긴다. 검증(테스트 덱 + deck-F/G 28장): HTML과 줄 수 불일치 7 → 0, HTML 대비 이미지 차이 합 105.6 → 99.6.

## 2026-10-12 마무리 — Supporting Message·Closing·PPTX 글꼴
**완료**: Supporting Message 공통 클래스(`.supporting-message`, X=41.6, 기업개요는 `.co-message` 예외 — Hard Rule §12) · Closing 구조 고정형 컴포넌트(위 `closing-reference`) · PPTX 굵기별 글꼴 매핑과 줄바꿈 보존(위 후속) · 변환 도형 테마 그림자 제거.

**남은 차이**
- **자간 미변환**: CSS letter-spacing이 PPTX로 옮겨지지 않는다 — Closing Motto 끝 +11.5px, Section Label(+0.2pt)·기업개요 핵심 메시지(−0.2pt)도 영향.
- **Closing 텍스트 폭**: "Thank You"는 HTML에서 900으로 근사해 PPTX에도 Black으로 저장돼 레퍼런스보다 약 11.5px 넓다. 긴 굵은 제목은 미커닝으로 줄 끝이 2~3px 밀린다.
- **열람 PC 폰트**: 굵기별 패밀리는 PPTX를 여는 PC에도 Pretendard 9개 굵기가 설치돼 있어야 그대로 보인다(미설치 시 해당 굵기가 대체 글꼴로 표시될 수 있음, 임베딩 없음).
