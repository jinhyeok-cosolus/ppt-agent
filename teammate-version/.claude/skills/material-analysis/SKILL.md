---
name: material-analysis
description: 원본 자료(docx/pdf/xlsx/csv/이미지)에서 텍스트·표·차트·이미지를 추출하고, 핵심 메시지·데이터를 식별한다. content-designer가 워크플로우 [2] 자료 분석 단계에서 사용한다.
---

# material-analysis

## 언제 사용하는가
content-designer가 [2] 자료 분석 단계에 진입했을 때. 원본 자료 파일 경로 목록을 입력받아 구조화된 `material_analysis.json`을 만들기 위한 원재료(추출된 텍스트/표/이미지)를 준비한다.

## 처리 흐름
1. `scripts/extract.py`로 파일 형식별 파싱 실행 (docx/pdf/xlsx/csv/이미지)
2. 추출 결과(JSON)를 LLM이 검토하며 핵심 메시지·데이터 중요도·표현 요소 적합성을 판단
3. 수치는 추출된 원본 값을 그대로 사용 — 재계산·추정 금지
4. 결과를 `/output/{project-name}/material_analysis.json`으로 저장

## 스크립트 사용법

```bash
python .claude/skills/material-analysis/scripts/extract.py \
  --input <원본파일 또는 폴더> \
  --output /output/{project-name}/material_analysis.json
```

- 여러 파일을 한 번에 넘기면 파일별 결과가 `sources` 배열에 누적된다.
- docx: 문단 텍스트(스타일 포함), 표(행/열 그대로), 임베드 이미지 추출
- pdf: 페이지별 텍스트, 표(pdfplumber 표 추출), 임베드 이미지 추출. 텍스트 레이어가 없는 스캔 PDF는 OCR을 시도하지 않고 `needs_manual_review: true`로 표시(임의 판독 금지)
- xlsx/csv: 시트별 표 데이터, 임베드 차트는 "차트 감지됨 — 원본 수치 추출 불가, 원본 이미지/파일 활용 권장"으로 표시
- 이미지: 파일 경로만 등록(내용 판단은 LLM이 직접 이미지를 보고 수행)

## 출력 스키마 (`material_analysis.json`)

```json
{
  "sources": [
    {
      "file": "원본 파일 경로",
      "type": "docx|pdf|xlsx|csv|image",
      "text_blocks": [{"text": "...", "importance_hint": null}],
      "tables": [{"headers": [...], "rows": [[...]], "row_count": 0, "needs_appendix": false}],
      "images": ["추출된 이미지 경로", "..."],
      "charts_detected": [{"location": "...", "note": "원본 수치 추출 불가 — 원본 활용 또는 사용자 확인 필요"}],
      "needs_manual_review": false
    }
  ],
  "escalations": [
    {"type": "core_number_unconfirmed|chart_source_unavailable|scanned_pdf", "detail": "...", "source": "파일:위치"}
  ],
  "needs_confirmation": [
    {"detail": "부가 수치 [확인필요] 사유", "source": "파일:위치"}
  ]
}
```

## 원칙 (설계서 1.6, 2.4 준수)
- 수치·실험 결과·기술적 의미는 원본 그대로 반영. 임의 생성·변경·추정 금지.
- 핵심 수치(발표 주장의 근거)를 확인할 수 없으면 → `escalations`에 기록하고 **즉시 이 수치를 다루는 후속 작업을 중단**, content-designer가 메인에게 보고.
- 부가 수치를 확인할 수 없으면 → `needs_confirmation`에 기록하고 나머지 작업은 계속 진행. 슬라이드 구성안·웹PPT에는 `[확인필요]` 표시로 반영.
- 차트 원본 수치를 추출할 수 없으면 → 눈대중 추정으로 새 차트를 만들지 않는다. 원본 차트/이미지를 그대로 활용하거나 escalation으로 원본 데이터를 요청.
- 상세 표(수십 행 이상)는 `needs_appendix: true`로 표시 — 슬라이드 구성 단계에서 핵심 행·열만 선별하고 전체 표는 부록 슬라이드로 분리.
- 파일 파싱은 로컬에서만 수행. 외부 API로 파일을 전송하지 않는다.

## references
- `references/` : 형식별 파싱 시 주의사항(병합 셀, 각주, 다단 레이아웃 등)을 프로젝트 경험이 쌓이며 축적하는 공간. 현재는 비어 있음.
