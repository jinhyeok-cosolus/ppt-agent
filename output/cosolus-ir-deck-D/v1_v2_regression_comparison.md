# v1 → v2 회귀 비교 리포트 — cosolus-ir-deck-D

> 비교 대상: v1 = `slide_outline_v1_archive.md` + `web_ppt/v1/index.html`(규칙개선 1~4 이전 판단) / v2 = `slide_outline.md` + `web_ppt/v2/index.html`(규칙개선 1~4 이후 — Claim→Evidence→Relationship 1-b 단계 포함 절차로 15장 전체 재판단)
> 원본 자료·`material_analysis.json`·`extracted_images`는 동일(재추출 없음). v1은 이 세션에서 전혀 수정하지 않았다.

## 요약

15장 중 **Selected Layout이 바뀐 슬라이드는 0개**다 — 1-b 단계(Claim→Evidence→Relationship 구조화)를 전체에 적용했지만, Layout Routing 자체를 뒤집을 만큼 Relationship 판단이 달라진 슬라이드는 없었다. 대신 **Visual Strategy(같은 Layout 내부에서 근거를 어떻게 보여주는가)가 바뀐 슬라이드는 3개**(Slide 3, 5, 11)다 — 모두 "대표 수치/텍스트 하나로 관계형 근거가 축약되던 지점"을 1-b가 명시적으로 걸러내 실제 시각 요소를 추가·분리한 사례다. 나머지 12개 슬라이드는 Relationship 판단이 v1과 동일해 구현도 사실상 동일하게 수렴했다(다만 HTML/CSS 자체는 v1 파일을 복사하지 않고 v2에서 새로 작성).

Cycle/Loop·Contribution 전용 Layout이 카탈로그에 없다는 v1 검증 시점의 공백은 Slide 5·11에서 실제로 마주쳤으나, 두 경우 모두 기존 Layout(Three-Column / Visual+Insight) 내부 재구성만으로 해결되어 "적합한 Layout Reference 없음"으로 이관할 정도의 문제로 이어지지는 않았다(§10 참조).

---

## 1~9. 슬라이드별 비교표

| # | v2 Relationship | Visual Strategy 변경 | Selected Layout 변경 | Required Evidence가 대표값으로 축약되지 않고 Visual에 보존됐는가 | Region별 Visual 다양성 | Required Evidence 누락 | Required Image 누락 | Optional Image 생략(사유) | 관련성 낮은 이미지 장식 오용 |
|---|---|---|---|---|---|---|---|---|---|
| 1 표지 | 단일 콘텐츠(N/A) | 없음 | 없음(표지 전용 규칙) | N/A | N/A | 없음 | 없음(White 로고 사용) | N/A | 없음 |
| 2 기업소개 | 단일 콘텐츠 | 없음 | 없음 | 예(5개 기본정보 전체) | 정보열+이미지 2종, v1과 동일 | 없음 | 없음(company-lab.png) | 없음 | 없음 |
| 3 밸류체인 리스크 | 기타·복합(Claim A 복수비교근거 + Claim B 단일독립근거) | **변경** — Claim A(3스탯)/Claim B(133t+서술+사진) Evidence Group을 분리(좌측 컬러 보더+미니헤더)해 v1의 균질 4스탯 그리드를 대체 | 없음(Visual+Insight Variant B 유지) | 예 — v1은 4개 지표를 형식만 같다는 이유로 하나의 `vi-stat-grid`에 뭉쳤으나, v2는 어느 근거가 어느 Claim을 뒷받침하는지 시각적으로 구분 | 예 — Stat Row(Claim A) vs Stat+Text+Photo 혼합(Claim B)로 Region 내부 표현이 근거 성격에 따라 다름 | 없음 | 없음(china-map.png, mining-waste.jpeg) | 없음 | 없음 |
| 4 북미 ESS | 단일 독립 근거 | 없음(Large Number 그대로 충분 — 관계를 억지로 만들지 않음) | 없음 | 예(N/A, 관계형 아님) | N/A | 없음 | N/A(원본 차트 이미지 자체가 없음, NC-01) | N/A | 없음 |
| 5 순환경제 모델 | 병렬(Claim1·2 원인→결과, Claim3 순환 관계) | **변경** — Column 3만 소형 2-node Cycle Diagram(SVG)으로 교체, Column 1·2는 기존 아이콘+텍스트 유지 | 없음(Three-Column 유지) | 예 — v1은 Column 3도 아이콘 하나로 균질 처리해 "제조→재활용→제조"가 텍스트로만 존재했으나, v2는 순환 구조 자체를 다이어그램으로 시각화 | 예 — 동일 Layout 안에서 Column 3만 다른 표현(신규 diversity) | 없음 | N/A(아이콘 기반, 원본 이미지 없음) | N/A | 없음 |
| 6 1세대 한계→솔루션 | Before/After | 없음 | 없음 | 예(Before 4항목 + After 개요 전체) | Before(이미지+리스트)/After(스텝박스+이미지+캡션) 이미 다양 | 없음 | 없음(gen1-reactor-a/b.jpeg) | 없음 | 없음 |
| 7 추출제 경쟁력 | 복수 비교 근거 | 없음 | 없음(Comparison Matrix) | 예(3대상×2기준 전체) | N/A(단일 Table Region) | 없음 | N/A(이미지 근거 아님) | N/A | 없음 |
| 8 CAPEX·OPEX | 원인→결과 | 없음 | 없음(Benefit+Impact) | 예(CAPEX·OPEX 값 모두) | CAPEX/OPEX 모두 단일 정량값이라 동일 표현이 오히려 적절(억지 다양화 안 함) | 없음 | N/A | N/A | 없음 |
| 9 DLE 공정 | 순차 공정 + Before/After | 없음 | 없음(Process+Comparison) | 예(6단계 전체 + 기존 DLE 비교) | Process Flow(단계 박스)/Comparison(이미지+텍스트) 이미 다양 | 없음 | 없음(atacama-salt-flat.jpeg) | 없음(img21은 라벨 불확실로 v1부터 미사용 유지) | 없음 |
| 10 DLE 기술 비교 | 복수 비교 근거 | 없음 | 없음(Table Comparison) | 예(4방식×4기준 전체) | N/A(단일 Table) | 없음 | N/A | N/A | 없음 |
| 11 DLE 핵심 경쟁력 | 기타·복합(단일독립근거 결론 + **구성요소별 기여도** + 공유근거) | **변경** — 분리막&THz(3%→90%)·핵심소재(3%→50%) 두 기여 요소를 2-bar Contribution 시각으로 병렬 표시(신규 `contrib-region`). v1은 "3%→90%↑"만 vi-stat으로 강조하고 "핵심소재 3%→50%"는 하단 보조 문장 한 줄로 축소 | 없음(Visual+Insight Variant D 유지) | **핵심 변경 지점** — v1은 두 기여 요소 중 하나만 대표값으로 강조, 나머지는 텍스트에 매몰. v2는 두 값 모두 동일 비중의 시각 요소로 보존 | 예 — Large Number(핵심 성과)/Contribution Bar(기여 분해)/Bullet List(공유 근거) 3종 혼재 | 없음 | N/A(이미지 근거 없음) | N/A | 없음 |
| 12 2세대 공정 | 순차 공정/프로세스 | 없음 | 없음(Process/System Architecture Layout A) | 예(4단계 전체 + Output) | N/A(단일 Component 흐름, 4개 모두 동일 역할이라 균질 표현이 적절) | 없음 | N/A(Layout A는 이미지 미사용이 규칙) | 예 — img62~65(실사진)는 4단계 중 1단계만 커버(25%<80%)해 Layout A(이미지 없음) 채택, Optional 사진 전체를 의도적으로 생략(v1과 동일 판단) | 없음 |
| 13 2세대 경쟁력 | Before/After(다기준) + 단일독립근거 보조 | 없음 | 없음(Before+After Variant B) | 예(7개 비교 기준 전체 + 보조 근거) | N/A(단일 Table) | 없음 | N/A | N/A | 없음 |
| 14 투자 포인트 | 병렬(4항목, 관계유형 혼합) | 없음(이미 Claim 3만 Large Number, 나머지 리스트로 구분되어 있었음 — v1도 관계 기준과 일치) | 없음(L18 4-Region 변형) | 예 | 이미 다양(3개 텍스트 리스트 + 1개 Hero 넘버) | 없음 | N/A | N/A | 없음 |
| 15 시장 진출 | 병렬(2거점) | 없음 | 없음(Symmetric Two-Split) | 예 | 인도네시아(확정 근거 이미지)/일본(단정 없는 참고 이미지)로 이미 Evidence 확실성 차이 반영 | 없음 | 없음(인도네시아 확정 로고 4종 모두 사용) | 일본 Panasonic/Iwatani/DNP는 Optional로 유지하되 단정 문구 없이 배치(NC-04, v1과 동일) | 없음(HLI 미사용 유지, IBC 정상 매핑 확인) |

---

## 10. Cycle/Loop·Contribution 전용 Layout 부재의 실제 영향

v1 검증 단계에서 이미 식별됐던 카탈로그 공백 — "순환 관계"와 "구성요소별 기여도"를 위한 전용 Layout Reference가 없다는 점 — 을 이번 v2에서 실제로 두 번 마주쳤다.

- **Slide 5(순환 관계, Claim 3 "제조→재활용→제조")**: Design Rules Layout Routing 6번(기존 Layout 조합·최소 변형 우선 시도)을 적용했다. 순환 구조는 슬라이드 전체가 아니라 3개 병렬 Column 중 **하나(Column 3)**에만 존재했으므로, Three-Column Insight Layout 자체를 바꿀 필요 없이 그 Column 내부에 2-node Cycle Diagram(SVG)만 추가해 해결했다. "적합한 Layout Reference 없음"으로 이관할 필요조차 없었다 — 결과 품질도 문제없이 3개 Column이 시각적으로 균형을 이뤘다(§QA 확인).
- **Slide 11(구성요소별 기여도, 분리막&THz 3%→90% / 핵심소재 3%→50%)**: 이 경우는 슬라이드의 핵심 근거 구조 자체였다. Visual+Insight Variant D의 Evidence Area 내부에 2-bar Contribution 시각(진행률 바 + baseline 표시)을 신설해 두 기여 요소 값을 모두 보존했다. Layout 자체를 바꾸지 않고도 Relationship을 보존할 수 있었다.
- **결론**: 두 사례 모두 Layout Routing 6번의 "기존 Layout 조합·최소 변형" 경로가 실제로 작동해 새 Layout MD 없이 해결됐다. 다만 두 경우 모두 슬라이드 구조상 국소적(Column 하나, 또는 Evidence Area 하나)이었기 때문에 가능했던 결과이며, 만약 어떤 슬라이드의 **Primary Content 전체**가 순환 관계나 다수(3개 이상) 구성요소의 기여도 분해였다면 이번처럼 "내부 재구성"만으로 충분했을지는 이번 테스트로 확인되지 않는다 — 이는 여전히 관찰되지 않은 공백이며, memory 지침대로 이번 범위에서 신규 Layout MD를 만들지는 않았다.

---

## 11. v1 QA 이력 항목의 v2 상태

| v1 QA 이력 문제 | v2 상태 | 근거 |
|---|---|---|
| Typography 위반(이미지 캡션/마커 12pt→14pt 미달, Stat Number 범위 초과, Body 14pt 인라인 오버라이드) | **해결** — v1은 최초 생성 시 위반이 발생했지만 자체 QA에서 즉시 수정해 최종본은 0건. v2도 동일한 패턴으로 최초 생성 시 신규 컴포넌트(Slide 3 evidence-group, Slide 11 contribution) 3건의 위반이 발생했으나 즉시 수정해 전체 15장 재감사 결과 **위반 0건** 확정(false positive 2건 제외 — `step-detail`은 Caption 역할로 v1부터 14pt 허용). | `.qa/v2/font-audit.json` 재감사 결과 |
| Slide 15 로고 매핑 오류(HLI 로고가 IBC로 잘못 표시) | **해결(재발 없음)** — v2는 v1이 이미 바로잡은 asset 파일(`logo-swap.jpeg`/`logo-mukti.jpeg`/`logo-econil.jpeg`/`logo-ibc.png`, HLI 파일 자체가 없음)을 그대로 재사용해 동일 오류가 재발할 여지가 없었다. 스크린샷상 SWAP/MUKTI/eCoNiL·ibattery/IBC 4개 로고가 정상 표시됨을 재확인. | `.qa/v2/slide-15.png` |
| Content Group 부자연스러운 배치(Slide 4/5/12) | **해결(재발 없음)** — v1이 이미 수정한 최종 구조(Slide 4 `vi-message-hero`, Slide 12 `psa-components` 등)를 v2가 그대로 기반으로 삼았고, Slide 5는 Column 3 내용이 바뀌었음에도 3개 Column이 시각적으로 균형을 유지함을 스크린샷으로 확인. | `.qa/v2/slide-04.png`, `slide-05.png`, `slide-12.png` |
| Divider/Table/한글 줄바꿈 이슈 | **해결(재발 없음)** — `.v-divider`(1px fallback), `.data-table`/`.pres-table`(colgroup+table-layout:fixed), 전역 `word-break:keep-all`을 v1과 동일한 값으로 재구현했고, Slide 7/10/13(Table)·Slide 15(Divider) 스크린샷에서 정상 렌더링 확인. 단어 중간 줄바꿈 없음. | `.qa/v2/slide-07.png`, `slide-10.png`, `slide-15.png` |

---

## 참고 — 이번 세션에서 다루지 않은 것

- Human Review②([6]) 대화형 승인은 이번 세션 범위에 포함되지 않았다. v2는 QA(Typography/Layout/1-c 전달 보존/Visual Quality)를 통과한 **초안** 상태이며, `state.json`의 `web_ppt_version`/`web_ppt_finalized`는 v1 확정 상태를 그대로 유지한다.
- pptx 변환([8])·`shared.html` 생성/공유 게시는 이번 범위에 포함하지 않았다.
- design-rules.md 등 규칙 파일은 이번 세션 중 수정하지 않았다(적용만 함).
