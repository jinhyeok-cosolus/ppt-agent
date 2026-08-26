# QA Report — cosolus-business-plan-2026 web_ppt/v1

## 0. 범위
[5] 최초 웹PPT 생성 직후 전체 17슬라이드 대상 1회 전체 QA(Layout/Typography/Content Fidelity) 수행.

## 1. Layout Compliance Check
- Selected Layout(slide_outline.md) 대비 실제 HTML 구조 대조 완료. 표지(01_cover_design_V2.md), Three-Column(6/8/11/16), Before-After Variant B(7), Table/Matrix(9), Process/System Architecture(12/14), Timeline(13), Closing(17) 각 컴포넌트가 Hard Rule §9(공통 Header)·§10(Content Comparison Header)·§10B(Table Header Row)·§11(Vertical Divider)·§12(Supporting Message) 스펙을 반영해 구현됨.
- 결과: 이상 없음.

## 2. Typography Compliance Check (`font-audit.json`)
- 최초 감사에서 62건 위반 발견(비-footnote 텍스트 12~13.5pt 사용): `.s9 table th`(13pt→14pt), `.s10-arrow`/`.s14-stage-arrow`(13.5pt→16pt), `.s13-year-sub`/`.s13-org-line`/`.s13-y5-concept`(12~13pt→14pt), `.cover-org`(13.5pt→14pt).
- 1회 수정 후 재검증(`qa_render.py --audit-fonts`) 결과: 위반 0건.
- Hard Rule §9가 명시적으로 12pt를 지정하는 `.hdr-section-label`, 그리고 `01_cover_design_V2.md`가 16px(=12pt)로 명시하는 `.cover-submsg`는 Hard Rule 자체의 예외 규정이므로 위반으로 처리하지 않음(수정 대상 아님).

## 3. Visual Quality Check — 2-a 자동 검사 (`layout-audit.json`)
- 17슬라이드 전체 겹침/overflow/텍스트 잘림/렌더링 오류/broken image: 없음("flagged: none").
- 2-b(응집도·시각적 균형·이미지 의미 적합성 등 정성적 판단)는 자동 QA 범위 밖 — Human Review ②로 이관.

## 4. Content Fidelity QA (`content_fidelity_qa.py`) — 확정 위반 없음, 전량 알려진 스크립트 한계로 판정
`status: fail`(53 issues)로 보고됐으나, 전수 검토 결과 실제 Required Evidence 누락은 0건이며 아래 3개 패턴으로 전량 설명된다. HTML을 수정하지 않았다(수정 시 오히려 정상 디자인을 훼손하는 경우이므로).

1. **Data Pending 오탐(전체 12개 슬라이드)**: 스크립트가 슬라이드 블록 텍스트에 문자열 "Data Pending"이 포함되면 무조건 렌더링 결과에 Data Pending 마커가 있어야 한다고 판정한다. 그러나 slide_outline.md의 모든 Backward Completeness Check 줄은 "uncertain·Data Pending **0건**"(즉 없음을 명시)이라고 적혀 있을 뿐이며, 실제로 `material_analysis.json`에 `visual_placeholders`(Data Pending)가 존재하는 슬라이드는 이 프로젝트에 하나도 없다(escalation·needs_confirmation 원본 데이터 자체도 이번 프로젝트는 0건). 즉 "0건"이라는 부정 서술이 문자열 매칭으로 긍정 신호로 오인된 스크립트 한계이며, 실제 콘텐츠 결함이 아니다.
2. **이미지 ID 표기 불일치(전체 이미지 참조 슬라이드: 3/4/11/14)**: `evidence_manifest`의 이미지 ID는 2자리 zero-padding 규칙(`CG03-IMG01`, `CG03-IMG02`)을 쓰는 반면, `material-analysis`가 실제 추출한 파일/참조명은 padding이 없는 `img1.png`~`img13.png`이다(원본 스킬 설계상 서로 다른 두 명명 체계). 스크립트는 Evidence 문자열에서 `IMG01`/`IMG02` 토큰을 추출해 렌더링 텍스트에 `img01`/`img02`가 있는지 찾으므로, 실제로는 `img3.png`/`img4.png`/`img6.png`/`img7.png`/`img13.png` 등이 정확히 매핑되어 사용됐음에도 문자열이 달라 "누락"으로 오탐된다. 각 슬라이드의 실제 `<img>` src·alt를 직접 대조해 그림3/4(슬라이드4, NC-02 매핑 그대로), 그림6/7(슬라이드11), 그림13(슬라이드14), 그림1/2(슬라이드3) 전부 정확히 삽입되어 있음을 확인했다.
3. **문장 재구성으로 인한 전체-문자열 불일치(다수 슬라이드)**: slide_outline.md의 Evidence 필드는 원본의 "라벨: 값" 형태 문장 전체를 인용부호로 감싼 경우가 많다(예: `"기존 열경화 방식: 약 1시간의 경화공정, 열에 의한 Warpage, ..."`). 스크립트는 이 전체 문자열을 하나의 원자로 취급해 렌더링 텍스트에 그 문자열 전체가 그대로(공백 제거 기준) 들어있는지만 확인한다. 실제 슬라이드에서는 가독성을 위해 이 문장을 개별 bullet/카드 항목으로 분해했고(Design System §5 Content Density 원칙에 따른 정상적인 표현 전환), 그 안의 개별 사실(수치·항목)은 전부 slide HTML에 존재한다 — 슬라이드1(표지 조직명), 5, 7, 8, 10, 11, 12, 14, 15가 이 패턴에 해당하며 항목별 직접 대조로 실제 누락이 없음을 확인했다.
   - 슬라이드1의 "소니드(주" ungrounded 플래그는 원본 표기 "소니드 주식회사"를 표지 가독성을 위해 "(주)" 약칭으로 바꾼 데서 발생 — 회사명 자체는 정확하며 축약 표기 차이일 뿐이다.
   - 슬라이드14의 "missing_atoms: 3단계"는 outline 서술문의 "3단계"라는 표현이 문자 그대로 슬라이드에 없다는 지적이나, 실제 슬라이드는 番호 배지 1/2/3으로 3단계 구조를 시각적으로 표현하고 있어 정보 손실이 아니다.
- 그 외 `ungrounded_explicit_fact`(RATIONALE/SOLUTION/TARGET 등 영문 Section Label, "COSOLUS"/"We"로 쪼개진 CI·Sub Message, "Small"/"BIG DIFFERENCE" 브랜드 모토)는 Hard Rule §7·§9·표지 규칙이 지정하는 고정 브랜드/헤더 요소이며애초에 `material_analysis.json` 근거 대상이 아니다(콘텐츠 사실이 아니라 디자인 시스템 고정 요소).
- `unchecked[]`(슬라이드2/9)는 스크립트가 결정론적 atom을 추출하지 못한 항목으로, 절차상 AI가 임의로 재판정하지 않고 그대로 남긴다 — 실제 검토 결과 슬라이드2(과제 개요 5개 속성)·슬라이드9(신뢰성/성과 목표 metric 그룹)는 모두 HTML에 정상 반영되어 있다.

## 5. 재검증 라운드
- Typography 수정 1회(전체 슬라이드 재렌더링, 위반 0건 확인) — 재검증 한도(최대 2회) 중 1회 사용, 이후 clean.
- Layout/Content Fidelity는 확정 위반이 없어 추가 자동 수정 라운드 없음.

## 6. 미해결 이슈
없음. Human Review ②로 이관할 자동 QA 미판정 항목(2-b: 응집도·시각 균형·이미지 의미 적합성 등)만 표준 절차대로 남아 있음.
