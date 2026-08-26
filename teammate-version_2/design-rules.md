# 디자인 규칙 (design-rules.md)

> 이 문서는 웹PPT/pptx 생성 시 항상 먼저 참조하는 디자인 규칙이다. **고정 규칙**과 **가변 규칙**으로 구분한다.
> 신규 규칙은 LLM이 스스로 "일반화 가능하다"고 판단하더라도 **사용자의 명시적 승인 없이는 본문에 반영하지 않는다.** 승인 전 후보는 하단 "검토 대기 후보" 섹션에만 기록한다.

## 적용 우선순위

아래 4개 문서는 각각 별도 원본 파일로 관리하며(본 문서에 내용을 복사하지 않고 경로만 참조), 충돌 시 다음 순서로 우선 적용한다.

| 우선순위 | 구분 | 원본 문서 | 역할 |
|---|---|---|---|
| 1 | Hard Rule | [`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`](../../../../docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md) | 규격·폰트·크기·컬러·로고 등 절대 변경 불가 규칙 |
| 2 | Claude PPT Design System | [`docs/design-system/Claude_PPT_Design_System.md`](../../../../docs/design-system/Claude_PPT_Design_System.md) | Hard Rule 범위 내에서 PPT 전체의 Visual Style, Color, Typography, Grid/Spacing, Component(Shape/Card/Line) Style, Image Treatment, Chart/Table/Diagram Style을 결정하는 공통 Design System |
| 3 | Content Visualization Freedom | [`docs/design-system/content-visualization-freedom.md`](../../../../docs/design-system/content-visualization-freedom.md) | 위 두 규칙을 준수하는 범위에서, 콘텐츠별 표현 방식(레이아웃·표/차트/이미지 선택 등)에 대한 AI 판단 허용/금지 경계 |
| 4 | Layout Reference | [`docs/layout-reference/2026.08.13_layout-catalog_V1.md`](../../../../docs/layout-reference/2026.08.13_layout-catalog_V1.md)(선택 인덱스) + [`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`](../../../../docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx)(시각적 구조 원본) + `docs/slide-design-rules/`의 콘텐츠 구조별 특수 Layout Reference(예: [`three-column.md`](../../../../docs/slide-design-rules/three-column/three-column.md)) | 위 세 규칙을 준수하는 범위에서, 콘텐츠 유형·정보 구조에 따라 적합한 레이아웃(L01~L33, 또는 조건에 맞는 구조별 특수 Layout Reference)을 고르기 위한 참고 자료. 디자인 고정 규칙이 아니며 가장 낮은 우선순위 |
| 표지 전용 | Slide-Type Rule — Cover | [`docs/slide-design-rules/01_cover_design_V2.md`](../../../../docs/slide-design-rules/01_cover_design_V2.md) | **표지(Cover) 슬라이드를 생성할 때만** 적용. Hard Rule·Claude PPT Design System을 준수하는 범위에서 표지의 레이아웃·비주얼 스타일을 구체적으로 지정한 문서. 표지 슬라이드에 한해 4번 범용 Layout Reference(L01~L33)보다 우선 적용하며, 표지 생성 시 L01~L33 카탈로그는 참고하지 않는다 |

상위 우선순위 문서와 충돌하는 내용은 하위 문서에서 적용하지 않는다. 아래 "고정 규칙" 섹션은 1번 문서를, "가변 규칙" 섹션은 레이아웃 등 프로젝트별 판단 대상을 다루며, 그 판단은 2번·3번·4번 문서의 기준을 따른다. "표지 전용" 문서는 슬라이드 유형이 표지일 때만 적용되는 예외이며, 그 외 슬라이드 유형에는 영향을 주지 않는다.

> **참고 — `docs/design-system/visual-style.md`와의 관계**: 기존 2순위였던 `visual-style.md`(Deck 전체 무드·여백·위계 등 정성적 기준)는 삭제하지 않고 그대로 보존한다. 다만 2순위 슬롯은 더 구체적인 `Claude_PPT_Design_System.md`가 대체하며, 두 문서가 겹치거나 충돌하는 부분(무드/일관성/여백/위계/이미지 처리/데이터 시각화 등)은 `Claude_PPT_Design_System.md` 쪽을 기준으로 따른다. `visual-style.md`는 현재 우선순위 체인에서 활성 참조 대상이 아니며, 두 문서의 중복 정리 여부는 별도 검토·승인이 필요하다.

## 고정 규칙 (반드시 유지) — 1순위 · Hard Rule

> 회사 로고, 브랜드 요소, 지정된 표지 등. 사용자가 별도로 명시하지 않는 한 레퍼런스 분석 대상에서 제외되며, 사용자가 직접 지정할 때만 이 섹션에 추가한다.
> 출처: [`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`](../../../../docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md) (사용자 제공, 2026-08-12 등록). 본 Hard Rule은 아래 "가변 규칙" 및 개별 레이아웃 문서보다, 그리고 아래 Claude PPT Design System·Content Visualization Freedom보다 **항상 우선 적용**한다.

### 슬라이드 규격
- 모든 PPT는 **16:9**를 기본 규격으로 사용한다.

### 폰트
- 전체 기본 글씨체(Font Family)는 **Pretendard 단일 서체**로 통일한다. 표지를 포함한 모든 슬라이드에서 Pretendard 외 다른 서체를 사용하지 않는다.
- Pretendard 내 Weight(Light/Regular/Medium/SemiBold/Bold/ExtraBold 등)는 정보 위계와 강조 수준에 따라 자유롭게 사용하며, 역할별 구체적 Weight는 아래 "Claude PPT Design System" 문서에서 정의한다.

### 글씨 크기
- 역할별(제목/본문/각주 등) 구체적인 글씨 크기는 아래 "Claude PPT Design System" 문서에서 정의한다. 본 Hard Rule은 Font Family(Pretendard 통일)만 고정하며 크기 수치는 고정하지 않는다.

### 제목 및 부제목
- 본문 슬라이드는 내용을 명확히 나타내는 제목을 기본적으로 포함한다.
- 필요한 경우 제목을 보완하는 부제목 또는 한 줄 핵심 메시지를 사용할 수 있다.
- 동일한 역할의 제목과 부제목은 PPT 전체에서 일관된 위계와 스타일을 유지한다.
- 표지·Section Divider 등 특수 슬라이드를 제외한 **일반 콘텐츠 슬라이드의 Main Title**은 아래 "공통 Header System(일반 슬라이드)"에서 정의하는 고정 위치·크기·Section Label 규칙을 따른다. 부제목(있는 경우)의 위치·색상·간격 등 그 외 세부 표현 방식은 적용되는 가변 규칙(레이아웃 문서)을 따른다.

### Brand Color

**Primary**
| 이름 | HEX | 용도 |
|---|---|---|
| Primary(구 Cosolus Teal) | `#067875` | 회사 기본 브랜드 컬러 |
| Dark/Main(구 Deep Pine) | `#034443` | 제목, 강한 대비, Dark Background 등 무게감이 필요한 요소 |
| Secondary(구 Sea Teal) | `#349887` | 데이터 및 핵심 정보의 강조색 |
| Light(구 Mint) | `#AFE2E3` | 보조 데이터, 영역 구분, 상대적으로 약한 강조 |

**Secondary / Neutral**
| 이름 | HEX |
|---|---|
| Ocean Blue | `#1A6A8C` |
| Moss | `#6E9B3F` |
| Flame Amber | `#C8801F` |
| Ink | `#162B1F` |
| Slate | `#5A6664` |
| Gray | `#8C9694` |
| Line | `#E1E7E5` |
| Mist | `#F3F6F5` |

**Color Usage**
- 기본 사용 색상은 Main Color 계열(Primary Colors: Cosolus Teal/Deep Pine/Sea Teal/Mint) + Black/Dark(Ink) + Gray(Gray, Slate)로 제한한다.
- 일반 제목·본문·일반 수치는 Black/Dark(Ink 등)를 사용한다.
- COSOLUS/자사 및 핵심 강조 요소는 Main Color 계열(Primary Colors)을 우선 사용한다.
- Gray(Gray, Slate)는 기존(Existing) 방식, 경쟁/비교 대상, 비활성·보조 정보를 표현할 때 사용한다.
- Red/Blue는 명확한 의미가 필요한 예외적인 경우에만 제한적으로 사용한다.
- Orange/Amber(Flame Amber) 및 기타 Secondary Color는 일반 Text, 제목, KPI, 핵심 수치 강조에 사용하지 않는다.
- Secondary Color(Ocean Blue, Moss, Flame Amber 등)는 Claude PPT Design System에서 용도가 명시적으로 정의된 경우에만 사용한다.
- 강조 우선순위는 Font Weight를 먼저 적용하고, 그다음 Main Color를 사용한다(Font Weight → Main Color).
- 시각적 다양성 확보만을 목적으로 한 임의의 색상 사용을 금지한다.
- 한 슬라이드에 불필요하게 많은 색상을 혼용하지 않는다.

### 전체 디자인 분위기
- 기술 기반 소재·화학 기업의 전문성, 신뢰성 및 정돈된 이미지를 전달한다.
- 기본적으로 White 또는 밝은 Neutral Background + Teal 계열 조합을 사용한다.
- 표지, Section Divider 등 강한 전환이 필요한 슬라이드는 Deep Pine / Cosolus Teal 계열의 Dark Background를 사용할 수 있다.
- 충분한 여백을 확보하고 장식 요소를 과도하게 사용하지 않는다. 색상과 그래픽은 콘텐츠보다 시각적으로 우선하지 않는다.
- 동일한 역할의 요소에는 PPT 전체에서 일관된 색상 체계를 적용한다.

### 회사 로고 및 Motto
- 모든 슬라이드에는 등록된 COSOLUS 공식 로고 이미지를 우선 사용한다. COSOLUS 로고를 텍스트로 임의 재현하거나 새로 생성하지 않는다.
- 로고의 비율, 형태, 색상을 임의로 변형·왜곡하지 않는다.
- 로고 파일 (등록됨, 2026-08-13):
  - Color(일반/밝은 배경용): [`docs/brand-assets/CI/cosolus CI_2.png`](../../../../docs/brand-assets/CI/cosolus%20CI_2.png)
  - White/Reversed(다크 배경용, 예: 표지): [`docs/brand-assets/CI/cosolus CI.png`](../../../../docs/brand-assets/CI/cosolus%20CI.png)
- 로고 구체적 크기·배치 위치는 아래 "회사 로고 및 Motto" 기준 또는 적용되는 가변 규칙(레이아웃 문서)에서 정의하며, 별도 기준이 없는 경우에만 전체 슬라이드와의 시각적 균형을 고려해 판단한다.
- 회사 Motto "COSOLUS, small actions, BIG DIFFERENCE"는 브랜드 요소로 사용할 수 있다. 표지, Section Divider, Closing 또는 브랜드 메시지 강조가 필요한 페이지에서 활용하며, 모든 페이지에 반복해 콘텐츠를 방해하지 않는다.
- 별도의 짧은 태그라인 "We promise tomorrow"는 위 Motto와 구분되는 공통 Header System 요소다. 아래 "공통 Header System(표지 제외 모든 슬라이드)" 규칙에 따라 표지를 제외한 모든 슬라이드에 고정 반복 배치하며, 이 반복 배치는 위 Motto 반복 제한 규정의 예외로 취급한다.

### 공통 Header System (표지 제외 모든 슬라이드)
> Layout Reference(가변 규칙)가 아니라 PPT 전체에 반복 적용되는 고정 Brand/Header 규칙이다. Section Label, Main Title, 좌측 상단 CI, 우측 상단 Sub Message, 상단 구분선, 우측 하단 페이지 번호 6개 요소로 구성된다. 아래 각 요소의 위치·크기·색상·표기 형식은 권장 사항이 아니라 반드시 준수해야 하는 Hard Rule이며, 개별 디자인/Layout MD 및 Claude PPT Design System보다 우선 적용한다.
>
> **좌표 기준**: 16:9, **1280×720px** 캔버스(웹PPT 생성기 표준 템플릿 `web-ppt-generator/scripts/templates/style.css` 및 기존 프로젝트 전체와 동일 — Claude PPT Design System §5의 "1920×1080px 상당" 표기는 EMU 환산 참고용 문구일 뿐 실제 생성 캔버스가 아니므로 좌표 기준으로 사용하지 않는다) 기준 절대 좌표(X, Y는 좌상단 원점 기준 좌측/상단 여백). 1280×720px는 13.333×7.5in 슬라이드를 96dpi로 렌더링한 값과 정확히 일치하므로, 폰트 크기의 pt→px 환산은 **1pt = 1.3333px(96dpi)** 기준을 그대로 사용한다(별도 스케일 보정 불필요). pptx 변환 시에도 캔버스 대비 동일한 상대 위치·비율을 유지한다.

- **Section Label**: 모든 일반 콘텐츠 슬라이드에서 Main Title 바로 위에 배치한다. 해당 슬라이드가 속한 섹션 표시 용도(예: BACKGROUND, COMPANY, TECHNOLOGY, PRODUCT), 영문 대문자 표기. Font: Pretendard Light, **12pt(=16px)**. Color: Gray(`#8C9694`). **X=68px**(Main Title X=64px보다 4px 안쪽). **Y=62px**(상단 구분선 Y=56px + 고정 간격 6px). 위치·스타일 고정, 텍스트만 콘텐츠에 따라 변경한다.
- **Main Title**: Section Label 바로 아래 배치. Font: Pretendard ExtraBold, **28pt(=37.3px)**. 좌측 정렬, **X=64px**, **Y=83px**(Section Label Y=62px + 라인 높이 20px + 고정 간격 1px). 모든 일반 슬라이드에서 동일한 X축 시작점과 Y축 기본 위치를 사용한다. 표준 가정은 **1줄**이며, Header Safe Area 경계 자체가 1줄 기준으로 고정되므로 Main Title이 실제로 2줄까지 늘어나는 상황은 지양한다 — 제목을 간결하게 작성해 1줄을 유지하는 것이 원칙이다. 임의로 폰트 크기나 시작 위치를 변경하지 않는다. Header Safe Area 하단 경계는 **Y=135px**로 고정한다(Reference(`benefit-impact.pptx`) 실측: Main Title 1줄·28pt ExtraBold·line-height 1.25 기준 하단 약 129.67px, Content Header 상단 약 134.86px, 간격 약 5.18px — 이 실측값을 근거로 산출한 값이며, 지나치게 밀착되어 보이지 않도록 최소한의 여유를 유지한다).
- **좌측 상단 — CI(로고)**: 등록된 COSOLUS 공식 CI를 고정 배치한다. **X=64px, Y=25px, Height=20px**. Width는 원본 비율 유지해 자동 산출(비율 왜곡 금지) — 등록 파일 `cosolus CI_2.png`(179×28px, 비율 약 6.39:1) 기준 참고 Width **약 128px**. 모든 슬라이드에서 동일한 크기와 위치를 유지한다.
- **우측 상단 — Sub Message**: 태그라인 "We promise tomorrow"를 고정 배치한다. Font Size: **14pt(=18.7px)**. Color: 고정색 `#478689`(Sub Message 전용 고정 색상 — Brand Palette와 별도로 고정되며, Primary 등 Brand Color가 변경되어도 이 값은 바뀌지 않는다). 우측 정렬, 오른쪽 끝 기준선 **X=1216px**(=1280-64, 좌측 여백과 대칭), **Y=25px**(CI와 동일 상단 높이). 모든 슬라이드에서 동일한 위치·크기·정렬을 유지한다.
- **상단 구분선**: **Y=56px**(위치 고정, 변경 없음). **X=64px ~ X=1216px**(좌우 콘텐츠 여백과 동일한 폭, 길이 **1152px**). 두께 **1px**. Color: 고정색 `#478689`(Sub Message와 동일한 값 — Brand Palette와 별도로 고정되며, Primary 등 Brand Color가 변경되어도 이 값은 바뀌지 않는다). 모든 슬라이드에서 동일하게 유지한다.
- **우측 하단 — 페이지 번호**: 현재 페이지 번호만 "1", "2", "3"과 같은 단독 숫자 형식으로 표시한다. "1/20", "2/20" 등 전체 페이지 수를 병기하는 형식은 사용하지 않는다. 모든 슬라이드에서 동일한 위치와 스타일을 유지한다.
- 표지는 페이지 번호를 표시하지 않는다(표지 구성은 `01_cover_design_V2.md`를 따른다).
- 위 6개 요소는 콘텐츠 레이아웃이 달라져도 동일한 위치·크기·스타일을 유지하며, 본문 콘텐츠가 이 영역(특히 Header Safe Area 하단 경계 Y=135px 이상 구간)을 침범하지 않도록 안전영역(safe area)을 확보한다.
- 위에 명시되지 않은 세부 사항(페이지 번호의 정확한 마진 px 등)은 전체 슬라이드와의 시각적 균형을 고려하여 판단하되, 위에 명시된 위치·크기·색상·표기 형식 기준과 충돌해서는 안 된다.

### 기본 디자인 품질 (모든 슬라이드 공통 체크리스트)
- 텍스트, 이미지 및 도형 간 의도하지 않은 겹침을 허용하지 않는다.
- 슬라이드 영역 밖으로 요소가 잘리지 않도록 한다.
- 텍스트가 텍스트 박스 영역을 초과하지 않도록 한다.
- 이미지 및 로고의 가로·세로 비율을 왜곡하지 않는다.

## Claude PPT Design System — 2순위 · Hard Rule 다음 우선 적용

> PPT 전체가 하나의 프레젠테이션처럼 보이도록 하는 공통 Design System(Visual Style/무드, Color, Typography, Grid/Spacing, Component(Shape/Card/Line/Arrow/Connector) Style, Image Treatment, Chart/Table/Diagram Style). Hard Rule을 대체하지 않으며 그 범위 안에서만 적용한다.
> 원본 문서(항상 이 경로를 직접 참조 — 본 문서에 내용을 복사하지 않음): [`docs/design-system/Claude_PPT_Design_System.md`](../../../../docs/design-system/Claude_PPT_Design_System.md)
> Hard Rule과 충돌하는 부분은 적용하지 않는다. 아래 "가변 규칙"(레이아웃 선택 등)과 "콘텐츠 표현 자유도"(다음 섹션) 판단은 모두 이 Design System 범위 안에서 이루어져야 한다. 기존 `docs/design-system/visual-style.md`와 중복되는 정성적 기준(무드·일관성·여백·이미지 처리·데이터 시각화 등)은 이 문서를 기준으로 적용한다 — 위 "적용 우선순위"의 참고 문단 참조.

## 콘텐츠 표현 자유도 — 3순위 · Hard Rule·Claude PPT Design System 다음 우선 적용

> AI(content-designer)가 슬라이드별로 표, 그래프, 다이어그램, 이미지, 텍스트 중심 구성 등 콘텐츠 표현 방식을 스스로 판단할 수 있는 허용 범위와, 임의로 변경해서는 안 되는 금지 범위를 정의한다. "디자인 스타일 생성"이 아니라 "콘텐츠를 가장 효과적으로 전달하는 표현 방식 선택"에 한정된 자유도다.
> 원본 문서(항상 이 경로를 직접 참조 — 본 문서에 내용을 복사하지 않음): [`docs/design-system/content-visualization-freedom.md`](../../../../docs/design-system/content-visualization-freedom.md)
> Hard Rule, Claude PPT Design System과 충돌하는 판단(예: 고정 규칙의 폰트/컬러 변경, Design System과 다른 새 디자인 언어 생성)은 이 문서가 "Allowed"로 열어두는 범위에 포함되지 않는다 — 두 상위 문서가 항상 우선한다.

## 표지(Cover) 전용 규칙 — 표지 슬라이드에서만 적용, Layout Reference보다 우선

> 표지 슬라이드를 생성·수정할 때 **항상 자동으로 참조**한다(별도 지시나 `@` 지정 없이도 적용). Hard Rule·Claude PPT Design System·Content Visualization Freedom을 준수하는 범위 안에서만 적용되며, 상위 규칙과 충돌하는 부분은 적용하지 않는다. 표지가 아닌 슬라이드(본문, Section Divider, Closing 등)에는 적용하지 않는다.
> 원본 문서(항상 이 경로를 직접 참조 — 본 문서에 내용을 복사하지 않음): [`docs/slide-design-rules/01_cover_design_V2.md`](../../../../docs/slide-design-rules/01_cover_design_V2.md) (사용자 제공, 2026-08-13 등록)
> 표지 생성 시 이 문서가 4순위 범용 Layout Reference(L01~L33)를 대체한다 — 표지에는 L01 등 카탈로그를 참고하지 않고 이 문서의 Layout/Visual Style/Soft Rules/Additional Rules/Avoid를 따른다.

## 가변 규칙 (레퍼런스 참고, 목적에 맞게 구성)

> 슬라이드 레이아웃, 표/차트 스타일, 정보 시각화, 강조 방식 등. 레퍼런스 자료 분석 후 사용자 승인을 받아 이곳에 추가한다.

### 레이아웃 선택 기준 — 채택 (2026-08-13, 사용자 승인) · 4순위 Layout Reference

> 디자인 고정 규칙이 아니다. 콘텐츠 유형·정보 구조에 따라 적합한 레이아웃을 고르기 위한 참고 기준이며, Hard Rule·Claude PPT Design System·Content Visualization Freedom과 충돌하는 부분은 적용하지 않는다.

- **선택 인덱스**(레이아웃 판단 시 항상 먼저 참조): [`docs/layout-reference/2026.08.13_layout-catalog_V1.md`](../../../../docs/layout-reference/2026.08.13_layout-catalog_V1.md) — 콘텐츠 유형·정보 구조 기준으로 레이아웃 후보를 빠르게 선택하기 위한 33종(L01~L33) 인덱스. 원본 내용은 수정하지 않고 경로만 참조한다.
- **시각적 구조 원본**(카탈로그에서 후보를 고른 뒤, 실제 요소 배치·구조를 확인해야 할 때만 참고): [`docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx`](../../../../docs/layout-reference/2026.08.13_ppt_layout_set__V3.pptx) — 33종 레이아웃 와이어프레임 원본(L01~L33이 슬라이드 1~33번에 대응).
  - 색상·서체는 이 pptx에 플레이스홀더로만 표시되어 있으므로 **그대로 쓰지 않는다** — 실제 적용 시 항상 위 "고정 규칙"(Pretendard 단일 서체, Brand Color)과 "Claude PPT Design System"을 따른다.
- **콘텐츠 구조별 특수 Layout Reference**(L01~L33 일반 카탈로그보다 먼저 검토): `docs/slide-design-rules/` 폴더에는 특정 콘텐츠 구조에 최적화된 개별 Layout Reference 문서가 누적된다(표지 전용 문서는 위 "표지 전용" 행에서 별도로 다룸). 슬라이드 콘텐츠 구조가 아래 문서의 Use When 조건에 해당하면 일반 카탈로그(L01~L33)보다 이 문서를 먼저 검토·적용하고, 해당하지 않으면 기존 절차대로 L01~L33에서 선택한다.

  | 문서 | 적용 조건(Use When) | 제외 조건(Do Not Use When) |
  |---|---|---|
  | [Three-Column Insight Layout](../../../../docs/slide-design-rules/three-column/three-column.md) | 동일·유사 위계의 독립적 핵심 메시지·근거·특징 3개를 병렬적으로 제시할 때 | 3개 항목이 순차 프로세스이거나 시간 흐름이 중요할 때 · 하나의 항목이 나머지보다 현저히 중요할 때 · 두 대상의 직접 비교가 핵심일 때 · 3분할이 콘텐츠 의미상 부자연스러울 때 |
  | [Process + Comparison Layout](../../../../docs/slide-design-rules/process-comparison/process-comparison.md) | 단계별 공정·기술·소재 흐름을 먼저 보여주고, 그 흐름과 직접 연결되는 문제점·한계·개선 방향 또는 기존/신규 기술 비교를 같은 슬라이드 하단에서 함께 전달할 때 | 공정 흐름만 보여주면 충분할 때 · 공정 없이 두 대상만 직접 비교할 때 · 시간축 중심의 연혁/로드맵일 때 · 3개 이상의 독립적 메시지를 병렬 비교하는 것이 핵심일 때 |
  | [Comparison Matrix Layout](../../../../docs/slide-design-rules/comparison-matrix/comparison-matrix.md) | 여러 제품·기술·경쟁사·솔루션(대상 3개 이상, 또는 2개 이상이라도 동일한 비교 기준이 여러 개 반복될 때)을 동일한 비교 기준(작동원리·성능·TRL·장단점·비용 등)으로 가로 방향 병렬 비교할 때. 자사/핵심 기술 등 특정 대상을 강조하면서도 객관적 비교 구조를 유지해야 할 때 | 비교 대상이 2개뿐이고 Before/After 구조가 더 적합할 때 · 시간 흐름·단계 진행이 핵심일 때(→ Process + Comparison) · 각 항목이 독립적이며 병렬 메시지 전달이 핵심일 때(→ Three-Column) · 비교 기준이 대상마다 달라 동일한 행 구조를 만들기 어려울 때 · 단순히 표 형태 데이터가 있다는 이유만으로는 적용하지 않음(각 대상의 독립적 설명이 비교 기준보다 중요하면 Multi-column 우선 검토) |
  | [Benefit + Impact Layout](../../../../docs/slide-design-rules/benefit-impact/benefit-impact.md) | 하나의 기술·솔루션·제품이 만드는 **정확히 2개**의 좌/우 정량적 개선 효과(CAPEX/OPEX·공정시간·수율·사용량 등)와 그 비즈니스/공정 Impact를, 각 효과별 Evidence(그래프·표·KPI 등)와 함께 `Core Technology → Improvement → Quantified Impact` 흐름으로 병렬 제시할 때 | 핵심 효과(Benefit)가 1개뿐이거나 3개 이상인 경우(→ Three-Column 또는 Comparison Matrix) · 여러 경쟁 대상을 동일 기준으로 비교할 때(→ Comparison Matrix) · 단계별 공정 흐름 자체가 핵심일 때 · Before/After 공정 단계 변화 자체가 핵심일 때(→ Before + After Layout) · 단순 장점 Bullet 나열에 그칠 때(Evidence 없이는 적용하지 않음) |
  | [Before + After Layout](../../../../docs/slide-design-rules/before-after/before-after.md) | 기존(Existing/Current)과 개선(Improved/New) **단 2개**를 비교하는 범용 Before/After Layout — 콘텐츠에 따라 하위 2개 Variant 중 선택. **Variant A(Process Transformation)**: 공정 단계 자체(단계 수·순서·분기·단순화)가 핵심일 때 좌→우 Diagram+Arrow로 표현. **Variant B(Before/After Comparison Table)**: 공정단수·공정시간·비용·효율·부산물·성능 등 동일 기준으로 기존 대비 개선 정도를 보여주는 것이 핵심일 때 Existing/Improved 2열 Presentation형 비교표로 표현("어떤 단계가 줄어드는가"→Variant A, "무엇이 얼마나 개선되는가"→Variant B) | 비교 대상이 3개 이상일 때(→ Comparison Matrix) · 공정 흐름을 먼저 보여준 뒤 그 흐름과 연결된 문제점·비교를 하단에서 함께 다뤄야 할 때(→ Process + Comparison) · 하나의 솔루션이 만드는 정량적 Impact를 Evidence로 증명하는 것이 핵심일 때(→ Benefit + Impact) · 시간축 기반 로드맵/연혁일 때 |
  | [Table Comparison Layout](../../../../docs/slide-design-rules/table-comparison.md) | 제품/기술 스펙을 항목별로 표 형태로 나열해야 할 때 · 자사와 경쟁사(또는 여러 대상)를 동일 기준의 행으로 촘촘히 비교해야 할 때 · 수치·데이터 중심이라 Diagram보다 표가 더 정확하고 신뢰도 있게 전달될 때 · 비교 항목(Row) 수가 많아 Card/Diagram형 배치로는 밀도를 감당하기 어려울 때 | 비교 대상이 2개뿐이고 Before/After처럼 변화·전환 자체가 핵심일 때(→ Before + After Layout) · 비교 항목마다 Icon/Diagram/이미지·강조 배지 등을 자유롭게 배치해 항목별로 다른 시각적 구성을 허용해야 할 때(→ Comparison Matrix Layout — 직각형 Grid를 강제하는 본 Layout과 달리 Cell마다 자유 구성을 허용하는 별도 Layout) · 하나의 솔루션이 만드는 정확히 2개의 병렬 효과를 보여줄 때(→ Benefit + Impact Layout) |
  | [Multi-Radar Technology Comparison](../../../../docs/slide-design-rules/013_multi-radar-technology-comparison.md) | 동일한 5~8개 평가축으로 3개 이상의 기술·제품·기업(자사/경쟁사 포함)을 비교할 때 · 개별 수치의 정확한 차이보다 각 대상의 강점/약점 Pattern(종합 Profile)이 중요할 때 · Radar Chart로 시각화할 실제 정량 데이터 또는 사용자 제공 평가 점수가 있을 때 | 정확한 수치 차이·항목별 Ranking이 중요할 때(→ Bar Chart) · 시간 흐름·연도별·공정 단계별 연속 변화가 핵심일 때(→ Line Chart) · 단위가 서로 다르거나 정성 설명·항목별 주석이 많아 정확한 수치를 그대로 읽어야 할 때(→ Table 유지) · 근거 데이터 없이 점수를 만들어야 하는 경우(임의 점수 생성 금지, 데이터 없으면 사용자에게 요청) |
  | [Left-Right Tech Comparison](../../../../docs/slide-design-rules/014_left-right-tech-comparison.md) | 하나의 핵심 소재/제품·기술을 정량 성능(좌측 Table/Data)과 작동 원리·공정(우측 Process Diagram) 두 관점에서 한 화면에 동시에 설명해야 할 때 · 전폭 Summary Bar로 슬라이드 전체 핵심 결론을 먼저 제시하고 그 아래 좌우 병렬 구성이 적합할 때 | 하나의 관점(성능만, 또는 공정만)으로 충분해 좌우 두 관점 병렬 구성이 불필요할 때 · 이 Layout의 필수 요소인 상단 Summary Bar를 유지할 콘텐츠·공간이 없을 때(문서 §11 Avoid — Summary Bar 생략·대체 금지가 전제 조건) |
  | [Competitive Advantage Highlight — 자사 열 카드 강조](../../../../docs/slide-design-rules/019_competitive-advantage-highlight.md) | 경쟁사 비교표 1개만으로 구성된 단일 오브젝트 슬라이드에서, 자사 열(또는 행)을 Solid Card 강조로 부각해 경쟁 우위를 형식 차이로 전달해야 할 때(비교 대상 3~4개 범위) — Table Comparison/Comparison Matrix 위에 얹는 자사 강조 처리 패턴으로 함께 적용 가능 | 비교 대상이 5개를 초과해 카드 대비 효과가 약해질 때 · 화살표·별표·"BEST" 뱃지 등 장식적 강조가 필요할 때(본 패턴은 형식 차이만으로 강조하며 장식 요소를 쓰지 않음) |
  | [Organization Chart — Curved Leadership](../../../../docs/slide-design-rules/020_organization.md) | 핵심 경영진·주요 책임자를 중심으로 조직이 확장되는 구조와 각 책임자의 전문 분야·담당 조직을 함께 전달해야 할 때(조직 관계가 비교적 단순한 경우) | 조직 관계 자체보다 단순 직급 계층(Pyramid) 전달이 목적이고 책임자 전문성·조직 확산 관계를 강조할 필요가 없을 때 |
  | [Business Site Map — Pin + Outside Card](../../../../docs/slide-design-rules/021_business-site-map.md) | 회사소개/사업장 소개에서 특정 지역(본사·공장·연구소 등)의 위치를 지도 기반으로 보여주면서 사진·주소도 함께 전달해야 할 때(단일 사업장 기준) | 사업장이 2개 이상으로 늘어나는 경우 — 이 문서는 단일 사업장(Pin 1개 + Card 1개) 패턴만 정의하며 다중 사업장 확장 규칙은 아직 미확정이다. 기계적으로 반복 확장(Pin·Card 여러 개)하기 전에 메인을 통해 사용자에게 배치 방향을 먼저 확인한다 |
  | [Timeline / Company Milestone Layout](../../../../docs/slide-design-rules/timeline-company-milestone.md) | 회사 연혁, 기술 개발 이력, 주요 성과, 투자/사업 진행 단계 등 시간의 흐름에 따라 여러 Milestone을 보여줘야 할 때 · 연도 또는 시점을 기준으로 이벤트를 순차적으로 배치해야 할 때 · 단순 Process가 아니라 시간축 자체가 정보의 핵심 구조일 때 | 단계 순서만 중요하고 시간 정보가 핵심이 아닐 때(→ Process + Comparison 등 Process 계열 우선) · Before/After 비교 자체가 핵심일 때(→ Before + After Layout 우선) · 연도별 계획을 막대(기간) 형태로 보여줘야 할 때(→ Layout Catalog L27 Gantt Roadmap 등 Roadmap/Gantt 계열 우선) · 더 구체적인 전용 Layout의 선택 조건에 해당하면 이 문서보다 해당 Layout을 우선 적용한다 |
  | [Company Introduction](../../../../docs/slide-design-rules/02_instruction_design_V1.md) | 회사의 정체성, 핵심 메시지, 기본 정보(기업명/대표자/임직원/소재지/비전 등)를 외부 청중에게 빠르게 전달하는 회사소개 슬라이드를 만들 때 | 문서 내 명시적 제외 조건 없음 — 회사소개 목적이 아니거나 좌(정보)/우(세로 이미지) 2단 구조가 콘텐츠와 맞지 않을 때는 다른 후보(L01~L33 등)를 검토 |
  | [Process / System Architecture Layout](../../../../docs/slide-design-rules/process-system-architecture-layout.md) | 공정 단계, 시스템 구성 요소, 기술/데이터 전달 흐름을 `Component 01 → Component 02 → ...`처럼 좌→우 선형 구조로 순차 설명하고, 전체 흐름이 만드는 최종 Output/Insight/Customer Value를 하단에 정리해야 할 때. 단계별 사진 유무에 따라 Layout A(이미지 없음)/B(이미지 있음)를 자동 선택 | 두 대상(기존/개선 등)을 공정과 함께 비교해야 할 때(→ Process + Comparison Layout) · 단계 간 시간 흐름(연혁/로드맵)이 핵심일 때(→ Timeline / Company Milestone Layout) · 공정이 아니라 하나의 중심 제품이 여러 적용처로 확장되는 관계일 때(→ Product / Application Layout) |
  | [Product / Application Layout](../../../../docs/slide-design-rules/product-application-layout.md) | 대표 제품/소재/플랫폼과 그 적용 분야·고객군·Use Case를 `제품 → 적용처` 관계로 한 슬라이드에서 보여줘야 할 때. 하나의 중심 제품이 여러 산업으로 확장되는 Hub-and-Spoke 관계면 Layout B(방사형), 적용 사례를 개별적으로 자세히 소개해야 하면 Layout A(Grid형) | 제품 자체의 세부 성능·스펙 비교가 핵심일 때(→ Table Comparison 또는 Comparison Matrix) · 적용처 사이에 단계·시간 순서·인과관계가 있을 때(→ Process / System Architecture Layout 또는 Timeline / Company Milestone Layout) |
  | [Visual + Insight Layout](../../../../docs/slide-design-rules/visual-insight/visual-insight.md) — Image+Text / Market·Problem / Technology·Principle / Message+Evidence / Financial·Growth(Layout Catalog L06/L07/L09/L15/L24)를 하나의 Layout Family로 통합한 범용 2분할 Layout | Visual + Insight 구조가 적합한 콘텐츠에 사용한다 — 대표 이미지, Chart, 기술/공정 Diagram, 핵심 Data Visualization 등 하나의 Main Visual을 중심으로 보여주고 반대 영역에서 그 의미·원인·근거(시사점)를 설명해야 할 때 우선 고려. Variant A(Image+Explanation)/B(Chart+Insight)/C(Technology·Principle)/D(Message+Evidence)/E(Growth·Driver) 중 콘텐츠 성격에 맞는 것을 선택 | 회사소개 전용 정보 구조가 필요할 때(→ Company Introduction) · 정확히 2개의 정량 Benefit 비교가 핵심일 때(→ Benefit + Impact) · 정량 Table과 Technology Diagram을 필수 Summary Bar와 함께 좌우로 보여줘야 할 때(→ Left-Right Tech Comparison) 등 더 구체적인 전용 Layout의 선택 조건에 해당하면 이 범용 Layout보다 해당 전용 Layout을 우선 적용한다 · 비교 대상이 2개 이상 대등하게 병렬 비교되는 것이 핵심일 때(→ Before/After · Comparison Matrix · Three-Column) |

  이 문서들은 각자 "Hard Rule > Claude PPT Design System > 해당 Layout Reference"라는 자체 우선순위를 명시하며, 이는 본 design-rules.md의 전체 우선순위 체계(1~4순위)와 정합한다. 단순히 콘텐츠 항목 개수가 조건과 일치한다는 이유만으로 기계적으로 적용하지 않고, 실제 정보 구조(위계 동일성, 병렬성, 프로세스/비교 여부 등)를 판단 기준으로 삼는다. Visual + Insight Layout은 이 표의 다른 문서들보다 조건이 넓은 범용 Family이므로, 콘텐츠가 회사소개·정량 Benefit 비교·좌우 Table+Technology 비교 등 더 구체적인 전용 Layout의 조건에 먼저 해당하는지 확인한 뒤에만 후보로 선택한다.
- **사용 절차**: (1) 슬라이드 콘텐츠 유형·정보량·관계 구조 판단 — 관계 구조 판단은 [`Claude_PPT_Design_System.md`](../../../../docs/design-system/Claude_PPT_Design_System.md) §5 "Content Relationship / Region Composition 원칙"의 Primary/Dependent/Shared Supporting/Conclusion 역할 분류와 Region 구성 절차를 먼저 따른다(형식이 아닌 역할·관계 기준) → (2) `docs/slide-design-rules/`의 콘텐츠 구조별 특수 Layout Reference(위 표) 중 Use When 조건에 맞는 문서가 있는지 확인 → 있으면 해당 문서를 우선 적용 → 없으면 `layout-catalog_V1.md`의 L01~L33 중 적합한 후보 선택(적합한 구조가 여럿이면 더 단순하고 위계가 명확한 쪽 우선, 동일 유형 슬라이드는 가능한 한 동일·유사 계열 유지) → (3) 실제 요소 배치가 필요할 때만 V3 pptx에서 해당 슬라이드 번호를 열어 구조 확인 → (4) Hard Rule·Claude PPT Design System을 적용해 재해석. 콘텐츠를 레이아웃에 억지로 맞추지 않으며, 표/그래프/이미지 사용 여부는 Content Visualization Freedom 범위 안에서 판단한다.
- 카탈로그(또는 특수 Layout Reference)에 적합한 구조가 없을 때만 기존 레이아웃을 조합하거나 최소 범위에서 변형한다 — 변형 시에도 Hard Rule·Claude PPT Design System은 반드시 유지한다.

### 폐기됨 — 참고하지 않음
- `docs/design-candidates/cosolus-v1/`(2026-08-11, 구 샘플 `레이아웃 샘플.pptx` 14슬라이드 기반 상세 스펙 14종)는 2026-08-12 사용자 승인으로 **폐기**되었다. 이후 아래 V2 레이아웃 세트로 대체되었으며, 더 이상 웹PPT 생성 시 참조하지 않는다. 파일은 기록 보존을 위해 삭제하지 않고 폴더에 `README.md`로 폐기 표시만 남겼다.
- 구조 전용 레이아웃 30종(2026-08-12 채택, 기준 자료 `docs/layout-reference/2026.08.12_ppt layout set_integrated_V2.pptx`)은 2026-08-13 사용자 지시로 **폐기**되었다. 위 "레이아웃 선택 기준"의 V1 카탈로그(33종)로 대체되었으며, 더 이상 웹PPT 생성 시 참조하지 않는다. 해당 V2 pptx 파일은 현재 `docs/layout-reference/` 폴더에서 확인되지 않는다(V3로 교체된 것으로 보임).

## 검토 대기 후보 (사용자 승인 대기)

> content-designer가 [9] 단계에서 "일반화 가능하다"고 판단했지만 아직 사용자 승인을 받지 못한 후보. 승인되면 위 섹션으로 이동하고 여기서 삭제, 거절되면 사유와 함께 여기 보존(재제안 방지).

| 날짜 | 프로젝트 | 후보 규칙 | 판단 사유 | 상태 |
|---|---|---|---|---|
| - | - | - | - | - |
