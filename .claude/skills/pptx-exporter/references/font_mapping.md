# 폰트 매핑표

정책: **Hard Rule 우선** — Design Hard Rule(`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md` §2)에
따라 PPT 전체 폰트는 Pretendard로 통일하며, pptx 변환 시에도 다른 폰트로 대체하지 않는다.
`<a:latin>`(영문/숫자)과 `<a:ea>`(한글 등 동아시아 문자) 타이프페이스 모두 "Pretendard"로 기록한다.

실행 PC에 Pretendard가 설치되어 있지 않으면 PowerPoint가 표시용으로 유사 폰트를 자체
대체할 수 있지만, 파일에 저장되는 폰트명 자체는 항상 Pretendard로 유지한다(별도 임베딩은
하지 않음 — 필요 시 사용자에게 임베딩 여부를 확인한다).

| 디자인 규칙상 폰트 | pptx 저장 폰트명 | 비고 |
|---|---|---|
| Pretendard | Pretendard | 국문/영문 공통, 대체 금지(Hard Rule) |
| (미지정/기본값) | Pretendard | 매핑표에 없는 경우의 기본값도 Pretendard 유지 |
| Noto Sans KR 등 그 외 폰트 | Pretendard | Hard Rule상 Pretendard 외 폰트는 애초에 웹PPT 단계에서 쓰이지 않아야 함. 발견 시 웹PPT 원인 수정이 우선이며, 변환 단계에서 임의 매핑하지 않는다. |

## 갱신 방법
Hard Rule에서 폰트 정책이 변경되면(현재는 Pretendard 고정) 이 표도 함께 갱신한다. 사용자
명시 승인 없이 이 표의 정책을 변경하지 않는다.
