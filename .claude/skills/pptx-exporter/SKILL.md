---
name: pptx-exporter
description: 확정된 웹PPT(HTML/CSS)를 편집 가능한 네이티브 PowerPoint(.pptx)로 재구성한다. 슬라이드 수/요소 일치 검증과 파일 무결성 체크를 포함한다. pptx-converter가 워크플로우 [8] 단계에서 사용한다.
---

# pptx-exporter

## 언제 사용하는가
pptx-converter가 [8] pptx 변환 단계에 진입했을 때. 입력은 확정된 `web_ppt/v{N}/` 경로, 출력은 `final.pptx`.

## 변환 원칙
- **편집 가능성 우선, 디자인은 실측 재현.** Playwright/Chromium으로 웹PPT를 실제 렌더링한 뒤 `getBoundingClientRect()`/`getComputedStyle()` 결과(위치·크기·폰트·색상·배경·테두리·정렬 등)를 그대로 읽어 python-pptx 네이티브 요소(텍스트박스/도형/표/이미지)로 재구성한다. 웹페이지를 통째로 이미지로 캡처해서 붙여넣지 않는다 — 그러면 편집이 불가능해진다.
- **차트(현재 제한, 추후 보완 예정)**: `<canvas>`/`<svg>`는 현재 버전에서 모두 Chromium이 실제 렌더링한 결과를 PNG로 캡처해 삽입한다(`data-chart-mode="native"`여도 동일). `data-chart-json`을 이용한 python-pptx 네이티브 `chart` 객체 재생성은 아직 이식되지 않았다 — 알려진 제한 사항으로 남겨두고, 재구현 전까지는 모든 차트가 이미지로 삽입된다는 점을 변환 결과 확인 시 감안한다.
- **폰트**: `references/font_mapping.md`에 따라 Pretendard로 고정하며 다른 폰트로 대체하지 않는다. `<a:latin>`·`<a:ea>` 모두 "Pretendard"로 기록하고, 실행 PC에 Pretendard가 없어도 파일에 저장되는 폰트명 자체는 항상 Pretendard로 유지한다(별도 임베딩은 하지 않음).
- **고정 규칙 요소**(로고 등)는 브라우저가 계산한 실제 위치·크기를 그대로 사용하므로 별도 비율 계산 없이 원본과 동일하게 배치된다.

## 스크립트

```bash
python .claude/skills/pptx-exporter/scripts/export_pptx.py \
  --web-ppt /output/{project-name}/web_ppt/v{N} \
  --output /output/{project-name}/final.pptx
```

사전 설치(최초 1회): `pip install -r requirements.txt` 후 `playwright install chromium`.

동작:
1. Playwright로 Chromium을 headless 실행해 `index.html`을 `file://`로 로드하고, 폰트 로딩·렌더링 완료를 기다린다.
2. 슬라이드(`.slide`)별로 DOM을 순회하며 각 요소의 실제 좌표·스타일을 추출한다. 배경/테두리가 있는 요소는 도형(box)으로, 텍스트 노드는 텍스트박스로, `<table>`은 셀 구조가 살아있는 네이티브 표로, `<img>`는 실제 위치·크기 그대로, `<svg>`/`<canvas>`는 해당 요소만 PNG로 스크린샷해 기록한다.
3. 추출한 데이터를 기반으로 슬라이드별 python-pptx 슬라이드를 생성해 요소를 배치한다.
4. 변환 후 슬라이드 수를 원본과 대조해 검증한다(불일치 시 stderr에 상세 로그 출력, 종료 코드 1).
5. 결과 파일이 PowerPoint에서 열리는 유효한 OOXML 구조인지 `python-pptx`로 재오픈해 무결성 확인.

## 검증 기준 (성공 기준)
- 원본 웹PPT의 디자인·레이아웃을 최대한 유지
- 슬라이드 수·내용 일치
- PowerPoint에서 텍스트/도형이 편집 가능한 상태
- 파일 손상 없음 (재오픈 성공)

실패 시(렌더링/변환 오류) 최대 2회 자동 재시도. 지속 실패하면 pptx-converter가 메인에게 에스컬레이션한다. **[8] 단계는 판단 영역이 아니므로, 요소 파싱 실패 등 예외 상황 외에는 자체 재해석하지 않는다.**

## references
- `references/font_mapping.md` — Pretendard 고정 정책 (대체 없음, 임베딩 없음)
