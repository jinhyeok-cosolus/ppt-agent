---
name: web-ppt-generator
description: design-rules.md(고정 규칙 + 가변 규칙)를 기반으로 HTML/CSS 웹PPT 슬라이드를 생성·수정하고, 차트/표를 렌더링한다. content-designer가 워크플로우 [5][7](웹PPT 생성/수정) 및 [9](규칙 갱신)에서 사용한다.
---

# web-ppt-generator

## 언제 사용하는가
content-designer가 [5] 웹PPT 초안 생성, [7] 피드백 반영, [9] 디자인 규칙 갱신 단계에 진입했을 때.

## 핵심 산출물
- `/output/{project-name}/web_ppt/v{N}/index.html` — 슬라이드 전체를 담는 진입점(섹션별 슬라이드 또는 `slides/slide-01.html` 형태로 분리 후 include, 프로젝트 규모에 따라 LLM이 선택)
- `/output/{project-name}/web_ppt/v{N}/assets/` — 이미지, 차트 데이터, 로고 등 정적 자산
- `/output/{project-name}/web_ppt/v{N}/style.css` — 공통 스타일(디자인 규칙 반영)

## 버전 스냅샷
수정할 때마다 새 버전을 만든다. 기존 버전은 삭제하지 않는다.

```bash
python .claude/skills/web-ppt-generator/scripts/new_version.py \
  --project /output/{project-name} \
  --from-latest   # 직전 버전을 복사해 새 vN 폴더 생성 (최초 생성 시에는 --scaffold)
```

- `--scaffold`: `v1/`을 templates 기반으로 새로 생성 (최초 웹PPT 생성 시)
- `--from-latest`: 가장 번호가 높은 `vN/`을 복사해 `vN+1/` 생성 (수정 시) — LLM은 복사된 폴더 위에서 diff를 적용
- 롤백: 과거 `vK/`를 `--from-latest` 대신 `--rollback-from vK` 옵션으로 지정하면 해당 버전을 복사해 새 최신 버전으로 만든다(과거 스냅샷 자체는 그대로 보존).

## 디자인 규칙 적용 원칙
`references/design-rules.md`를 항상 먼저 읽는다.

- **고정 규칙**(로고, 브랜드 색상, 지정 표지 등): 그대로 준수한다. 변형·생략 금지. 자산 파일은 `/docs/brand-assets/`에서 참조(프로젝트 폴더로 복사하지 말고 상대/절대 경로로 참조하거나, 배포 편의를 위해 필요 시 `assets/`로 1회 복사 후 출처를 유지).
- **가변 규칙**(레이아웃, 표/차트 스타일, 정보 시각화, 강조 방식): 레퍼런스 자료에서 파악한 장점을 슬라이드 목적에 맞게 해석해 적용한다.
  - `design-rules.md`에 가변 규칙이 아직 없는 프로젝트(최초 사용)라면, 업로드된 레퍼런스 자료를 분석해 초안 규칙을 제안하고 content-designer가 메인을 통해 사용자 확인을 받는다. 확인 전까지는 `design-rules.md`에 반영하지 않고, 해당 세션 내에서만 임시로 적용한다.
  - 레퍼런스 간 스타일이 상충하면 임의 선택 금지 — 메인을 통해 사용자에게 선택지를 제시한다.
- 원본 이미지는 그대로 사용. 디자인 통일성을 위한 크롭·색보정만 허용, 합성·수치 변형 금지.
- 원본 수치·데이터는 `material_analysis.json`/`slide_outline.md`와 정확히 일치해야 한다. 임의로 반올림·재해석하지 않는다. `[확인필요]` 표시가 있는 값은 슬라이드에도 동일하게 `[확인필요]`로 노출한다.

## 상세 데이터 표 처리
원본 표가 수십 행 이상(`needs_appendix: true`)이면:
1. 슬라이드 본문에는 핵심 행·열만 선별해 표시 (선별 기준: 발표 스토리라인상 강조할 수치, 이상치, 요약 행 등 — content-designer가 [3] 단계에서 결정한 기준을 따름)
2. 전체 표는 별도 부록 슬라이드(`appendix`)로 추가
3. 선별 과정에서 표시되는 수치 자체는 변경하지 않는다.

## 차트 렌더링
- 웹PPT에서는 **Chart.js**로 인터랙티브 렌더링한다. `scripts/vendor/chart.min.js`를 로컬에 두고 `<script src="../../assets/vendor/chart.min.js">`로 참조한다 (CDN 미사용 — 오프라인·로컬 처리 원칙 준수). 최초 셋업 시 `scripts/vendor/`에 Chart.js 파일을 1회 내려받아 배치해야 한다(현재 리포지토리에는 포함되어 있지 않음 — README 참고).
- 차트에 쓰이는 수치는 `material_analysis.json`에서 추출된 원본 값을 그대로 사용한다. 원본 수치를 추출할 수 없는 차트(`charts_detected`)는 새 차트를 그리지 않고 원본 이미지를 `<img>`로 삽입한다.
- pptx 변환 단계에서 네이티브 차트/이미지 중 무엇으로 변환할지 판단할 수 있도록, 차트를 감싸는 요소에 `data-chart-mode="native|image"` 힌트 속성과 원본 데이터(`data-chart-json`)를 함께 남긴다.

## 스크립트
- `scripts/new_version.py` — 버전 스냅샷 생성/롤백
- `scripts/templates/` — 슬라이드 기본 HTML/CSS 템플릿 (표지, 본문, 표, 차트, 부록 레이아웃)
- `scripts/vendor/` — 로컬 번들 JS 라이브러리 배치 위치 (Chart.js 등)

## references
- `references/design-rules.md` — 고정 규칙 + 가변 규칙 + 검토 대기 후보 (누적 갱신, 사용자 명시 승인 후에만 본문 반영)
