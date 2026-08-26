# output

발표 자료(프로젝트) 단위로 산출물을 분리 보관하는 폴더다. 새 프로젝트를 시작하면
`{project-name}/`을 새로 만든다 (프로젝트 이름은 [1] 단계에서 사용자와 함께 정한다).

## 프로젝트 폴더 구조

```
{project-name}/
  state.json              # 워크플로우 진행 상태 (CLAUDE.md 1장 참조)
  material_analysis.json  # [2] 자료 분석 결과
  slide_outline.md        # [3] 슬라이드 구성안
  extracted_images/       # [2]에서 추출된 원본 이미지
  web_ppt/
    v1/                    # 버전 스냅샷 (폴더 복사 방식, git 아님)
    v2/
    ...
  final.pptx               # [8] 최종 산출물
```

## state.json 예시

```json
{
  "project_name": "example-project",
  "stage": "3",
  "audience": "고객사/외부 청중",
  "language": "ko",
  "presentation_time_min": 20,
  "target_slide_count": 15,
  "web_ppt_version": null,
  "pptx_generated": false,
  "history": [
    {"stage": "1", "note": "자료 입력 완료", "at": "2026-08-11"}
  ]
}
```

과거 프로젝트를 다시 열 때는 항상 해당 프로젝트의 `state.json`을 먼저 읽고 그 단계부터
이어간다.
