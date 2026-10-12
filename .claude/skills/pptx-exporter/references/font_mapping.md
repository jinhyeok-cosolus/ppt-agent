# 폰트 매핑표

정책: **Hard Rule 우선** — Design Hard Rule(`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md` §2)에
따라 PPT 전체 폰트는 Pretendard 계열로 통일하며, pptx 변환 시에도 다른 폰트로 대체하지 않는다.
`<a:latin>`(영문/숫자)과 `<a:ea>`(한글 등 동아시아 문자) 타이프페이스는 항상 같은 이름으로 기록한다.

실행 PC에 Pretendard가 설치되어 있지 않으면 PowerPoint가 표시용으로 유사 폰트를 자체
대체할 수 있지만, 파일에 저장되는 폰트명 자체는 항상 Pretendard 계열로 유지한다(별도 임베딩은
하지 않음 — 필요 시 사용자에게 임베딩 여부를 확인한다).

| 디자인 규칙상 폰트 | pptx 저장 폰트명 | 비고 |
|---|---|---|
| Pretendard | Pretendard 계열(아래 "굵기 매핑") | 국문/영문 공통, 대체 금지(Hard Rule) |
| (미지정/기본값) | Pretendard | 매핑표에 없는 경우의 기본값도 Pretendard 유지 |
| Noto Sans KR 등 그 외 폰트 | Pretendard | Hard Rule상 Pretendard 외 폰트는 애초에 웹PPT 단계에서 쓰이지 않아야 함. 발견 시 웹PPT 원인 수정이 우선이며, 변환 단계에서 임의 매핑하지 않는다. |

## 굵기 매핑 (2026-10-12, 사용자 승인)

**변경 근거**: 기존에는 모든 굵기를 "Pretendard" + 굵게 on/off로만 저장해, PowerPoint에서 Light→Regular,
SemiBold·ExtraBold→Bold로 표시됐다(예: Closing Motto 폭 +15px, 본문 SemiBold 획 농도 +12%). 설치된
Pretendard 폰트 파일의 name 테이블(ID 1, Windows 패밀리 이름)을 확인한 결과 Regular·Bold만 "Pretendard"
한 패밀리이고 나머지 굵기는 각각 별도 패밀리였으며, 그 이름으로 저장한 PPTX를 PowerPoint로 렌더링하면
9개 굵기 모두 Chrome과 같은 굵기·폭(30pt 기준 폭 차 0.5~1.5px)으로 표시됐다.

| CSS font-weight | pptx 저장 폰트명 | 굵게(b) |
|---|---|---|
| 100 | Pretendard Thin | 끔 |
| 200 | Pretendard ExtraLight | 끔 |
| 300 | Pretendard Light | 끔 |
| 400 | Pretendard | 끔 |
| 500 | Pretendard Medium | 끔 |
| 600 | Pretendard SemiBold | 끔 |
| 700 | Pretendard | 켬 |
| 800 | Pretendard ExtraBold | 끔 |
| 900 | Pretendard Black | 끔 |

- 굵기별 패밀리에 굵게를 켜지 않는다 — PowerPoint가 획을 덧입혀 한 단계 더 굵게 그린다.
- 표 헤더 셀처럼 굵게가 강제되는 텍스트는 600 미만이면 700으로 본다.
- **적용 범위**: export_pptx.py가 만드는 모든 텍스트(일반 텍스트 상자·표 셀). 폰트 이름만 바뀌며 위치·크기·색은 그대로다.
- **미설치 시 처리**: 변환 PC의 시스템·사용자 폰트 폴더에서 해당 굵기 패밀리를 찾지 못하면 그 굵기는
  기존 방식("Pretendard" + 600 이상 굵게)으로 저장한다. 설치되지 않은 이름을 쓰면 PowerPoint가 전혀 다른
  글꼴로 대체해 그리는 것을 확인했기 때문이다.
- **열람 PC 주의**: 굵기별 패밀리는 PPTX를 여는 PC에도 설치돼 있어야 그대로 보인다. Pretendard 전체
  굵기(9개 파일)가 설치되지 않은 PC에서는 그 굵기의 텍스트가 대체 글꼴로 표시될 수 있다.

## 갱신 방법
Hard Rule에서 폰트 정책이 변경되면(현재는 Pretendard 고정) 이 표도 함께 갱신한다. 사용자
명시 승인 없이 이 표의 정책을 변경하지 않는다.
