# AGENTS.md

> 이 문서는 이전 세션(Claude)에서 진행된 작업을 Codex가 이어받을 수 있도록 정리한 인수인계 문서다. 여기 적힌 내용은 해당 세션에서 이미 파악·확정된 사실만 담고 있으며, 추가 조사나 검증 없이 작성되었다.

## 1. 프로젝트 목적 및 전체 작업 흐름

이 프로젝트는 **기술 발표용 PPT를 자동 제작하는 에이전트 오케스트레이터**다. 메인 에이전트는 직접 자료 분석·슬라이드 작성을 하지 않고, 사용자와 대화하며 입력을 수집한 뒤 서브에이전트(`content-designer`, `pptx-converter`)를 호출해 작업을 위임한다.

표준 워크플로우(`CLAUDE.md` §1~§9):
1. 자료 입력(원본 자료, 레퍼런스, 청중, 언어, 발표시간/슬라이드 수 확인)
2~3. 자료 분석 · 구성 설계(`content-designer` → material-analysis → content-grouping → slide-content-structuring)
4. Human Review ① — 구성(`slide_outline.md`) 검토
5. 웹PPT 초안 생성(`web-ppt-generator`)
6. Human Review ② — 웹PPT(`web_ppt/v{N}/index.html`) 검토, 확정 시 `shared.html` 자동 생성
7. 피드백 반영(새 `web_ppt/vN+1/` 스냅샷)
8. `pptx-converter`로 pptx 변환
9. (선택) 사용자가 명시적으로 요청한 경우에만 design-rules 갱신

각 프로젝트 상태는 `/output/{project-name}/state.json`에 기록되며, 새 세션은 이 파일을 먼저 읽고 해당 단계부터 이어간다.

## 2. 주요 규칙 파일과 역할

- **`CLAUDE.md`**(프로젝트 루트) — 오케스트레이터 동작 지침. 서브에이전트 호출 시점, Human Review 절차, 실패/에스컬레이션 처리 원칙(§4) 등을 정의.
- **`tech-ppt-agent-design.md`** — 설계 근거·트레이드오프 문서. `CLAUDE.md`와 충돌 시 이 문서가 우선.
- **`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`**(Hard Rule) — 전체 PPT 공통 디자인 규칙(폰트, Brand Color, 공통 Header System, Content Region Header, Table Header Row, Divider 등). 개별 Layout MD보다 항상 우선.
- **`docs/design-system/Claude_PPT_Design_System.md`**(Design System) — Typography Tier, Color System, Chart/Table Style 등 세부 디자인 값.
- **`docs/slide-design-rules/*.md`**(Layout MD, 17개) — 개별 레이아웃(Three-Column, Before-After, Benefit+Impact, Table Comparison, Comparison Matrix, Process+Comparison, Multi-Radar, Organization, Business-Site-Map, Timeline, Process/System Architecture, Product/Application, Visual+Insight, Cover, Company Intro, 14p/19p 레거시 분석 문서 등). 각 Layout의 **구조**(사용 여부·개수·위치·의미)를 정의하며, **디자인 값**은 Hard Rule을 참조.
- **`.claude/skills/{material-analysis, content-grouping, slide-content-structuring, web-ppt-generator, pptx-exporter}/SKILL.md`** — 각 워크플로우 단계의 실행 로직.
- **`/output/{project-name}/state.json`** — 프로젝트별 진행 상태·history 기록.

## 3. 현재 Field Test E 진행 상태

프로젝트: `output/cosolus-ir-deck-E/` (source: `input/코솔러스_IR_내용 추출_V2.docx`, 22슬라이드, 청중=고객사/외부, 20분/15장 목표는 참고치).

`state.json` 기준 마지막 확인 상태:
- `stage: "6"`, `web_ppt_version: "v1"`, `web_ppt_finalized: false`, `pptx_generated: false`
- Human Review ①([4]) 승인 완료. `slide_outline.md`(22장), `material_analysis.json`, `slide_composition_map.json` 확정.
- [5] 웹PPT 초안(`web_ppt/v1/`) 생성 완료 — Typography 위반 0건, Visual QA 렌더링 결함 0건까지 재검증 완료된 상태.
- Human Review ②([6])는 **정식 브라우저 대화형 승인이 아직 진행되지 않음** — 사용자가 승인 절차를 생략하고 공유용 HTML만 먼저 만들어 달라고 요청해 `bundle_for_share.py`만 실행됨. 이 때문에 `web_ppt_finalized`는 여전히 `false`.
- `shared_html.v1: "generated"`로 기록되어 있으나, 실제 `web_ppt/v1/` 폴더를 확인한 결과 파일명이 `shared.html`이 아니라 **`2026.08.20_보완자료 input_V1.html`**로 되어 있음(크기는 state.json 기록과 일치 — 내용은 같은 파일로 추정되나 규칙상 파일명과 다름, 아직 정정하지 않음).
- 미해결 escalation 3건: Slide3(CG03-VP1 리튬 수요-공급 전망 테이블), Slide4(CG04-VP1/VP2 전기차 폐배터리·북미 ESS 차트) — 원본에 수치 자체가 없어 Data Pending 상태 유지 중(사용자 결정: 삭제·추정 없이 자리만 유지하고 진행).
- needs_confirmation NC-14: Slide21 실명 대기업 로고 4개(SWAP/Panasonic Energy/Iwatani/DNP), 본문에 회사명 미언급 — 확인 대기 중.
- [8] pptx 변환은 아직 진행되지 않음.
- 이번 세션에서 Slide 5 3-Column 본문 디자인 검증용 `web_ppt/v2/` 스냅샷을 생성했다. **Slide 5만 수정**됐으며, `state.json`은 갱신하지 않아 여전히 `web_ppt_version: "v1"`이다. v2는 Human Review ② 확정본이 아니라 대표 Layout 테스트 결과다.

## 4. 완료된 토큰/실행시간 최적화

이번 세션 시작 시점에 사용자가 "Field Test E의 파이프라인 검증과 1·2차 토큰 최적화, 1차 실행시간 최적화까지 완료된 상태"라고 알려왔다. 이 세션에서는 해당 작업을 직접 수행하지 않았으며, 세부 변경 내역도 세션 내에서 확인하지 않았다. 다만 `slide-content-structuring/SKILL.md`, `web-ppt-generator/SKILL.md`가 `state.json`의 마지막 기록 시점 이후에 수정된 흔적(파일 mtime)을 확인했으며, 이 최적화 작업의 결과로 추정된다. **이 최적화 구조는 이번 세션에서 변경하지 않았고, 앞으로도 건드리지 않는다.**

## 5. 방금 완료한 Header / Divider Hard Rule 통합 및 Layout MD 정리

사용자 요청으로 `docs/slide-design-rules/`의 17개 Layout MD를 조사해 Header(Content Region Header)/Divider 관련 규칙을 "구조 규칙(Layout MD 유지)"과 "디자인 규칙(Hard Rule로 통합)"으로 분리하고, 통합안을 제안 → 승인받아 실제 파일에 반영했다.

**Hard Rule 변경**(`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`):
- §10을 "Content Comparison Header" → **"Content Region Header"**로 확장. "2개 이상 병렬 Region + 독립 주제 → Header 기본 사용, 역할 분리 구조는 강제 안 함" 원칙 신설.
- 기존 두 Fill 변형을 **Parallel Variant**(대등 병렬)/**Contrast Variant**(대립 비교)로 명명. 값 자체는 변경 없음.
- **Header Gap** 원칙 신설 — 새 고정 %/px 값은 추가하지 않고 "동일 Gap 유지 + Content Region Grid 기준 자연 배치"만 명문화.
- 신규 **§10B. Table Header Row** 섹션 추가 — Content Region Header(§10)와 별도 컴포넌트로 분리, 기존 Design System §8/`table-comparison.md`에 있던 값(Primary Fill+White Bold, Table Grid 1px/Line, Typography 14/16/14pt)을 그대로 승격. **Layout-specific Emphasis 예외 조항** 포함(자사 강조처럼 Layout 고유 목적이 있는 경우 기본 강조 규칙과 다른 Variant 허용).
- §11(Vertical Content Divider) — Header 영역 정의에 §12(Supporting Message) 포함, 개별 % Inset 수치(8%, 10~15% 등)를 "Content Region 실제 범위 기준" 원칙으로 대체(새 고정값 도입 없음), **Dashed Variant** 신설(dash pattern은 강제하지 않음), Table Grid와 명확히 구분.
- "적용 원칙"에 Hard Rule=컴포넌트가 "어떻게 보이는지", Layout MD=컴포넌트가 "어디에·몇 개·어떤 의미로" 필요한지를 정의한다는 역할 분리 원칙 추가.

**수정된 Layout MD(10개)**: `three-column.md`, `before-after.md`, `benefit-impact.md`, `table-comparison.md`, `comparison-matrix.md`, `014_left-right-tech-comparison.md`, `019_competitive-advantage-highlight.md`, `process-comparison.md`, `013_multi-radar-technology-comparison.md`, `02_instruction_design_V1.md`(경미).

**변경하지 않은 Layout MD(7개, Header/Divider 관련 내용 없음 또는 이미 준수 상태)**: `01_cover_design_V2.md`, `020_organization.md`, `021_business-site-map.md`, `timeline-company-milestone.md`, `visual-insight.md`(이미 Hard Rule만 참조하는 모범 사례), `process-system-architecture-layout.md`, `product-application-layout.md`.

**핵심 원칙**:
- 리터럴 HEX/%/px 값(`#F4FAFA`, `#067875`, `#034443`, `#349887`, Gap 1~2%, Divider Inset 8%/10~15%, Table 1px 등)은 Layout MD에서 제거하고 Hard Rule 참조로 교체.
- **019(`019_competitive-advantage-highlight.md`)의 COSOLUS Column Solid Fill 강조는 의도적으로 유지** — Hard Rule §10B의 Layout-specific Emphasis 예외로 명시적 근거를 부여했을 뿐 디자인 자체는 바꾸지 않음.
- Layout MD의 구조적 판단(Header 사용 여부·개수·위치, Divider 사용 위치, Variant 선택 로직 등)은 전혀 삭제하지 않음.
- HTML/PNG/QA 실행, Field Test E 산출물 수정, 토큰/실행시간 최적화 구조 변경은 이번 작업 범위에서 제외됨(수행하지 않음).

## 6. Content Visualization Freedom 보완 완료

`docs/design-system/content-visualization-freedom.md`의 Graph/Chart/Table 관련 자유도 적용 범위를 최소 수정했다. 전체 디자인 자유도를 줄이는 것이 아니라, 원본에 이미 완성된 데이터 Visual이 있을 때 AI가 이를 임의로 재해석·재디자인하지 못하도록 우선순위를 명확히 한 변경이다.

확정된 우선순위:
1. **완성된 원본 Graph/Chart 존재 → 원본 이미지 최우선 재사용**
   - Graph↔Table 등 다른 표현 방식으로 임의 변환하거나 데이터를 다시 해석해 새 Chart로 만들지 않는다.
   - 수치, Series, Category, Axis, Unit, Label, 범례, 비교 관계를 보존한다.
   - Layout에 맞춘 크기·위치·Crop/Contain 등 배치 조정만 허용한다.
2. **완성된 Graph/Chart 없이 Raw Data만 존재 → AI 시각화 허용**
   - 값·단위·관계를 바꾸지 않는 범위에서 Graph/Chart/Table/KPI 중 적절한 표현을 선택할 수 있다.
   - 기존 "표와 그래프 중 더 적합한 방식 선택" 규칙은 이 경우에만 적용한다.
3. **사진·Diagram·Icon·Map·KPI 등 일반 콘텐츠 → 기존 Visualization Freedom 유지**

핵심 수치 강조 위치 조정은 원본의 값·단위·대응관계와 기존 Visual의 의미 구조를 바꾸지 않는 범위에서만 허용한다. 원본 Visual의 품질이 사용 불가능할 정도로 낮거나 사용자가 명시적으로 재디자인을 요청한 경우만 예외이며, 불명확하면 임의 재생성하지 않는다. Relationship 기반 Visual 판단보다 이 원본 Visual 보존 우선순위가 앞선다.

## 7. 1차 최소 Content Fidelity QA 구현 완료

대형 provenance 시스템이나 원본 재독 없이 기존 산출물을 재사용하는 1차 최소 검증을 `web-ppt-generator`에 추가했다.

**추가 파일**:
- `.claude/skills/web-ppt-generator/scripts/content_fidelity_qa.py`

**수정 파일**:
- `.claude/skills/web-ppt-generator/SKILL.md` — Post-Generation QA의 별도 `1-d. Content Fidelity QA`로 호출 시점·범위·결과 처리 규칙 추가.

**입력 재사용**:
- `material_analysis.json`
- `slide_composition_map.json`
- `slide_outline.md`
- 생성된 `web_ppt/vN/index.html`

**현재 검증 범위**:
1. Grounding에 없는 명시적 수치·단위·연도와 규칙으로 식별 가능한 회사명·제품명 후보 추가 여부
2. `slide_outline.md`의 Required Evidence에서 결정론적으로 추출 가능한 수치·인용문·명시 필드·이미지 ref 누락 여부
3. Data Pending, `[확인필요]`, 추적 가능한 uncertain 자산의 상태 marker 유실 여부

최초 생성에서는 전체 슬라이드, 수정 라운드에서는 변경된 슬라이드만 `--slides`로 묶어 배치 검사한다. 입력 파일은 실행당 한 번만 읽으며 LLM 호출이나 원본 PPT/PDF/DOCX 재독은 하지 않는다. 확정 위반은 `issues[]`, provenance 없이 판정할 수 없는 uncertain 사용 여부나 결정론적 atom이 없는 Required Evidence는 `unchecked[]`로 분리한다.

**중요: 아직 실제 실행 검증은 완료하지 못했다.** 당시 환경에서 `python.exe` 접근 실패 및 `py` Python 미설치 상태가 확인되어 Script의 실제 실행·Field Test E 적용을 하지 않았다. Field Test E 전체 QA도 재실행하지 않았다. 향후 Python 실행 환경이 준비되면 변경 슬라이드 또는 작은 fixture로 먼저 동작 검증해야 한다.

**1차 범위에서 제외한 항목**:
- Relationship Fidelity
- Chart Series/Axis/Legend 비교
- 세밀한 의미적 Claim 검증
- HTML→PPTX 콘텐츠 parity
- provenance 없이는 사용 여부를 특정할 수 없는 uncertain 콘텐츠의 확정 판정

## 8. Slide 5 Three-Column 대표 테스트 및 확정 결과

Field Test E의 Slide 5(비즈니스 모델)를 대상으로, 새로운 디자인 규칙을 만들지 않고 현재 Hard Rule + Three-Column Layout + Content Visualization Freedom 범위에서 Main Visual과 Supporting Text의 응집도를 개선하는 대표 테스트를 수행했다.

**산출물**:
- 테스트 스냅샷: `output/cosolus-ir-deck-E/web_ppt/v2/`
- 최종 렌더링: `output/cosolus-ir-deck-E/.qa/v2/slide-05.png`

**확정된 Slide 5 결과**:
- CG05에는 재사용할 원본 이미지·Graph/Chart가 없고, 원본 제작 지시는 "3 BOX 구조 + 내용에 맞는 아이콘"이었다.
- 복잡한 설명형 Diagram 대신 각 메시지를 직관적으로 나타내는 단순 Main Visual/Icon 3개를 사용했다. Visual 내부 설명 Text와 원본에 없는 새로운 사실·수치·Visual Evidence는 추가하지 않았다.
- Header/Divider DOM과 `.tc-grid`, `.tc-col`, `.tc-col-body`, `.comp-header` 등 공통 Container 구조·Padding·Gap·크기·위치를 v1 기준으로 보존했다.
- v2 초안에서 추가했던 `.s5-col-body` Padding/Gap Override는 공통 공간 관계를 바꾼 원인이어서 제거했다. 이후 수정 범위를 Visual 전용 Wrapper와 내부 SVG, Slide 5 전용 Supporting Text 정렬로 제한했다.
- Vertical Divider는 실제 Chromium 렌더링에서 두 개가 모두 명확히 보이도록 Slide 5 웹 렌더링 한정 1px fallback과 stacking을 적용했다. DOM/CSS 존재 여부만이 아니라 최종 PNG로 표시 여부를 확인했다.
- 3개 Visual의 시작 위치와 체감 크기·무게를 균형화하고, Visual 영역 높이와 Supporting Text 시작 Y 및 아이콘–텍스트 간격을 통일했다.
- Hard Rule, Content Visualization Freedom, 다른 Layout MD, 다른 슬라이드는 이 테스트에서 수정하지 않았다.

**`three-column.md`에 일반화해 반영한 공통 기준**:
- Divider 2개를 각각 인접 Column Gap 중앙에 배치하고 실제 렌더링에서 모두 보이는지 확인
- Visual Type이 달라도 Visual 영역 시작 위치·높이와 체감 크기·시각적 무게를 균형화
- Supporting Text가 3개 Column에 있으면 시작 Y와 Visual–Text 간격을 통일
- 본문 Visual 수정 시 확정된 Header Bar와 공통 Container를 보존하고 수정 범위를 Visual 전용 영역 내부로 제한

Slide 5 고유 아이콘·콘텐츠·px값은 Layout 규칙으로 일반화하지 않았다.

## 9. 현재 미완료 상태와 다음 작업

**다음 작업 후보**: Field Test E 전체를 다시 생성하는 것이 **아니다**. Slide 5 Three-Column 대표 검증은 완료됐으므로, 필요할 때만 다른 대표 Layout을 소규모로 이어서 확인한다. 예: Before-After Variant A/B(슬라이드7/17), Benefit+Impact(슬라이드9/13), Table Comparison/Competitive Advantage(슬라이드10/18), Comparison Matrix(슬라이드8). 전체 22장 재렌더링·재QA·재생성은 하지 않는다.

이 확인은 규모를 최소화한 대표 샘플 점검이며, 전체 22장 재렌더링·재QA·재생성이 아니다.

**그 외 미해결 항목**:
- Field Test E escalation 3건(Slide3/4 Data Pending) — 실제 데이터 미확보 상태 그대로.
- NC-14(Slide21 실명 대기업 로고 4개) — 확인 대기.
- `web_ppt/v1/`의 공유용 HTML 파일명이 `shared.html` 규칙과 다르게(`2026.08.20_보완자료 input_V1.html`) 되어 있는 점 — 정정 여부 미결정.
- Human Review ②(정식 대화형 승인) 미완료 — `web_ppt_finalized`가 아직 `false`.
- [8] pptx 변환 미착수.
- `content_fidelity_qa.py` 실제 실행 검증 미완료 — Python 실행 환경 확보 후 작은 범위부터 확인 필요.
- `web_ppt/v2/`는 Slide 5 대표 테스트 스냅샷이며 Human Review ② 확정 전이다. `state.json`도 아직 v1을 가리킨다.
- Hard Rule §10B Typography(14/16/14pt)를 `table-comparison.md`에서 다른 Table 계열 문서로 소급 적용했는데, 콘텐츠 성격상 문제없는지 최종 확인 필요.
- 014의 `Dark Process Panel #263238`은 Header/Divider와 무관한 Diagram 전용 색상이라 이번 정리에서 제외함 — 별도 정리 필요 여부 확인 필요.

## 10. Codex가 반드시 지켜야 할 주의사항

- **Field Test E를 처음부터 다시 분석·생성하지 말 것.** `material_analysis.json`/`slide_composition_map.json`/`slide_outline.md`/`web_ppt/v1/`은 이미 확정된 산출물이며, 재실행이 아니라 이미 있는 결과 위에서 대표 Layout만 점검하는 것이 목표다.
- **토큰/실행시간 최적화 구조(SKILL.md들)를 임의로 변경하지 말 것.** 이번 세션에서 최적화 이후 로직을 검증하지 않았으므로, 그 구조를 건드리는 작업은 별도 확인 후 진행한다.
- **Hard Rule과 Layout MD의 역할 분리를 유지할 것.** 디자인 값(색상·크기·Typography·Padding·Gap·Divider 두께 등)은 Hard Rule에만 존재해야 하며, Layout MD에 새로운 리터럴 값을 추가하지 않는다.
- **새로운 고정 Gap %/px, Divider Inset %/px, Dashed dash pattern 값을 임의로 만들지 말 것.** 사용자가 명시적으로 이 값들을 "정성적 원칙만 유지, 고정 수치 강제 금지"로 확정했다.
- **019의 COSOLUS Column Solid Fill 강조(Layout-specific Emphasis)를 일반 Table 강조 규칙(Text+Bold)으로 되돌리지 말 것.** 이는 의도적으로 유지된 예외다.
- **CLAUDE.md의 Human Review 체크포인트([4], [6])를 임의로 생략하지 말 것.** 특히 [6] 확정 전에는 `shared.html` 자동 생성 외의 공유/게시를 진행하지 않는다.
- **`state.json`을 먼저 읽고 해당 단계부터 이어갈 것.** 프로젝트별 진행 상태를 임의로 앞서가지 않는다.
- **원본 자료는 로컬에서만 처리한다**(`CLAUDE.md` §5) — 미검증 원본을 외부 서비스로 보내지 않는다.
- **완성된 원본 Graph/Chart가 있으면 원본 이미지를 우선 재사용한다.** Raw Data만 있을 때에만 AI가 Graph/Chart/Table/KPI 표현 방식을 선택한다.
- **Content Fidelity QA 때문에 원본 전체를 다시 읽거나 전체 내용을 LLM으로 의미 비교하지 않는다.** 기존 분석 산출물을 재사용하고 최초 생성 또는 변경 슬라이드만 결정론적으로 검사한다.
- **확정된 Header/Divider 또는 공통 Container가 있는 슬라이드에서 본문 Visual만 수정할 때 해당 DOM/CSS를 함께 재구현하지 않는다.** Visual 전용 Wrapper 내부로 수정 범위를 제한하고 실제 렌더링으로 Divider 표시·정렬 회귀를 확인한다.
