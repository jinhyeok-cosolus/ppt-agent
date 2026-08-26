---
name: pptx-exporter
description: 확정된 웹PPT(HTML/CSS)를 편집 가능한 네이티브 PowerPoint(.pptx)로 재구성한다. 슬라이드 수/요소 일치 검증과 파일 무결성 체크를 포함한다. pptx-converter가 워크플로우 [8] 단계에서 사용한다.
---

# pptx-exporter

## 언제 사용하는가
pptx-converter가 [8] pptx 변환 단계에 진입했을 때. 입력은 확정된 `web_ppt/v{N}/` 경로, 출력은 `final.pptx`.

## 변환 원칙
- **편집 가능성 우선, 디자인은 근사치 허용.** 웹PPT의 HTML 구조(텍스트박스/도형/표/차트/이미지)를 슬라이드별로 파싱해 python-pptx 네이티브 요소로 재구성한다. 웹페이지를 통째로 이미지로 캡처해서 붙여넣지 않는다 — 그러면 편집이 불가능해진다.
- **차트 혼합 적용**: HTML에 남긴 `data-chart-mode` 힌트를 따른다.
  - `data-chart-mode="native"` → python-pptx `chart` 객체로 재생성 (원본 데이터는 `data-chart-json`에서 그대로 가져옴, 재계산 금지)
  - `data-chart-mode="image"` 또는 힌트가 없는 경우 → 렌더링된 차트 영역을 이미지로 캡처해 삽입
  - 원본 수치를 추출할 수 없어 원본 이미지를 그대로 쓴 차트(`<img>`만 있는 경우)는 이미지로 삽입
- **폰트**: Hard Rule에 따라 PPT 전체 폰트는 Pretendard로 통일하며, pptx 변환 시에도 대체하지 않는다(`references/font_mapping.md` 참조). Pretendard 외 폰트가 웹PPT에서 발견되면 변환 단계에서 임의로 다른 폰트로 매핑하지 않고 변환 로그에 기록해 에스컬레이션한다.
- **고정 규칙 요소**(로고 등)는 위치·크기 비율을 유지해 배치한다.

## 스크립트

```bash
python .claude/skills/pptx-exporter/scripts/export_pptx.py \
  --web-ppt /output/{project-name}/web_ppt/v{N} \
  --output /output/{project-name}/final.pptx
```

동작:
1. `index.html`(및 링크된 슬라이드 파일)을 파싱해 슬라이드 목록·요소 트리를 만든다.
2. 슬라이드별로 python-pptx 슬라이드를 생성하고 텍스트/표/이미지/차트 요소를 배치한다.
3. 변환 후 슬라이드 수·요소 수를 원본과 대조해 검증한다(불일치 시 stderr에 상세 로그 출력, 종료 코드 1).
4. 결과 파일이 PowerPoint에서 열리는 유효한 OOXML 구조인지 `python-pptx`로 재오픈해 무결성 확인.

## 검증 기준 (성공 기준)
- 원본 웹PPT의 디자인·레이아웃을 최대한 유지
- 슬라이드 수·내용 일치
- PowerPoint에서 텍스트/도형이 편집 가능한 상태
- 파일 손상 없음 (재오픈 성공)

실패 시(렌더링/변환 오류) 최대 2회 자동 재시도. 지속 실패하면 pptx-converter가 메인에게 에스컬레이션한다. **[8] 단계는 판단 영역이 아니므로, 요소 파싱 실패 등 예외 상황 외에는 자체 재해석하지 않는다.**

## references
- `references/font_mapping.md` — 웹 폰트 → PowerPoint 표준 폰트 매핑표 (레이아웃 깨짐 방지 우선 정책)
