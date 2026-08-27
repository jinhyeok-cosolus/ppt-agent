# COSOLUS PPT Design System v1

## 1. Brand Visual Direction
- 톤: 로우-키, 기술 신뢰감, 저채도 단색 중심. 장식 최소화(그라디언트/쉐도우는 예외적 강조에만).
- 컬러 축: 단일 브랜드 컬러(딥 틸)의 명도 단계로 위계를 표현. 다색 배색 금지.
- 정보 표현: 텍스트보다 도형 기반 도식(프로세스/구조/타임라인)을 우선.
- 인물·제품 사진은 원색이 아닌 브랜드 팔레트로 톤을 맞춘다(흑백/듀오톤/틴트).

## 2. Color System
| 역할 | Token | Hex |
|---|---|---|
| Base White | `color.bg.base` | #FFFFFF |
| Base Black/Ink | `color.ink.900` | #0F1E1F |
| Brand Darkest | `color.brand.900` | #034443 |
| Brand Dark | `color.brand.800` | #034443 |
| Brand | `color.brand.700` | #067875 |
| Brand Mid | `color.brand.500` | #067875 |
| Brand Bright | `color.brand.400` | #349887 |
| Brand Accent | `color.brand.300` | #349887 |
| Tint Light | `color.tint.100` | #AFE2E3 |
| Tint Lightest | `color.tint.50` | #F4FAFA |
| Neutral Gray | `color.neutral.500` | #808080 |
| Neutral Gray Light | `color.neutral.300` | #AFABAB / #D0CECE |
| Signal (제한적 사용) | `color.signal.alert` | #FF0000 / #003399 |

규칙:
- 한 슬라이드에 브랜드 틸 계열 2~3단계 + 화이트 + 그레이 1단계만 사용.
- 시그널 컬러(빨강/파랑)는 표/차트의 증가·감소, 경고 표시 등 국소적 데이터 강조 1~2곳에만 허용. 배경/도형 채우기로 사용 금지.
- 배경 틴트(Tint 100/50)는 섹션 구분 카드·배경에만, 텍스트 배경으로 남용 금지.

## 3. Typography System
- 전체 서체(Font Family): **Pretendard 단일 서체** (Thin/Light/Regular/Medium/SemiBold/Bold/ExtraBold/ExtraLight). Font Family 및 타 서체 혼용 금지 규칙은 Hard Rule §2를 따른다.
- 역할 분리 원칙: 서체가 아닌 **Weight**로 정보 위계·강조 수준을 구분한다. 커버 타이틀·핵심 통계 숫자 등 가장 강한 위계는 Pretendard ExtraBold, 일반 섹션 타이틀은 ExtraBold~Bold, 본문은 Regular/Medium을 기본으로 한다.

| 레벨 | 서체/웨이트 | 크기(pt) | 용도 |
|---|---|---|---|
| Display | Pretendard ExtraBold | 44–60 | 커버 타이틀 |
| H1 | Pretendard ExtraBold | 28–30 | 섹션 타이틀 |
| Content Header (H2) | Pretendard SemiBold | 20 | Content Header, 본문 영역의 주요 소제목 |
| Explanation | Pretendard Medium/SemiBold | 18 | Key Message, 핵심 설명, Main Visual/KPI의 의미나 원인을 직접 설명하는 주요 Explanation |
| Body | Pretendard Regular/Medium | 16 | 일반 Body Text, Supporting Text, Supporting Evidence, 상세 설명 — 일반적인 본문 정보는 16pt 미만으로 축소하지 않는다 |
| Caption / Auxiliary | Pretendard Light/Regular | 14 | Chart X/Y Axis Label·축 이름, Legend 등 본문의 이해를 보조하는 정보 전용(Source/Footnote/각주는 아래 별도 행 참조) — 이 역할을 포함해 Source/Footnote/각주를 제외한 모든 텍스트는 14pt 미만으로 축소하지 않는다 |
| Source / Footnote / 각주 | Pretendard Light | 12(예외적 최소값) | 출처 표기, 각주, Deck Footnote 등 Deck 전체에서 가장 낮은 위계의 보조 정보 전용 — **14pt 미만이 허용되는 유일한 역할**이며 최소 12pt까지만 허용한다. 이 역할이 아닌 텍스트에는 공간 부족을 이유로 12pt 또는 14pt 미만을 적용하지 않는다(2026-08-19 확정) |
| Stat Number | Pretendard ExtraBold | 24–30 | 강조 수치 — 동일 역할(예: 슬라이드마다 반복되는 Before/After 대비 수치)은 Deck 전체에서 동일한 pt 값을 사용하고, 컴포넌트마다 임의로 다른 값을 쓰지 않는다 |

### Font Size 적용 원칙
- 텍스트의 크기는 공간이 아니라 **정보 위계와 역할**을 기준으로 결정한다.
- 공간이 부족한 경우 Font Size를 임의로 축소하지 않는다. 문장 압축 → 불필요한 내용 제거 → 줄 수 조정 → Gap 조정 → Visual 크기 조정 → Layout 재검토 순으로 해결한다.
- 동일한 역할의 텍스트는 슬라이드마다 일관된 Font Size를 적용한다.
- **최소 크기**: Source/Footnote/각주를 제외한 모든 텍스트는 14pt 미만으로 내려가지 않는다. Source/Footnote/각주에 한해서만 최소 12pt까지 허용한다(위 표의 "Source / Footnote / 각주" 행 참조). 공간이 부족하다는 이유로 이 최소값 아래로 축소하지 않는다 — 위 문장 압축~Layout 재검토 순서로 해결한다.
- **단위(pt/px)**: 위 표의 크기는 모두 **pt** 단위다. 웹PPT(HTML/CSS) 구현 시 `font-size`는 pt 단위로 그대로 작성하는 것을 기본으로 한다. px 단위가 반드시 필요한 경우에만 **1pt = 1.3333px** 기준으로 정확히 환산한다 — pt 숫자를 그대로 px 숫자로 옮기지 않는다(예: Body 16pt를 `font-size: 16px`로 적는 것은 오류다. 16pt의 올바른 px 환산은 21.3px이며, 16px는 12pt에 불과하다).

## 4. Information Hierarchy
1. 섹션 타이틀(무엇에 대한 슬라이드인가) → 2. 핵심 메시지/숫자(가장 굵고 큰 요소) → 3. 지지 도식/이미지 → 4. 세부 텍스트·캡션.
- 슬라이드당 강조 요소(가장 큰 텍스트 또는 숫자)는 1개만. 경쟁하는 두 개의 큰 요소 금지.
- 색 대비가 아닌 크기·웨이트로 1차 위계를 만들고, 색은 브랜드 카테고리 구분(예: 단계별 틸 명도)에만 사용.

## 5. Grid / Spacing / Alignment
- 캔버스: 16:9 (12192000 × 6858000 EMU 기준, 1920×1080px 상당)
- 마진: 좌우 최소 64px, 상단 header 영역 고정 높이대(타이틀 존) 확보 후 하단에 콘텐츠 존.
- 레이아웃 골격: 상단 타이틀 존 + 하단 콘텐츠 존(그리드/타임라인/카드형)으로 고정, 표지만 중앙 정렬 예외.
- 정렬: 본문은 좌측 정렬 기본. 중앙 정렬은 표지·임팩트 문구 등 예외적으로만.
- 다수 도형(도식)은 반드시 균등 gap의 행/열 그리드에 정렬 — 자유배치 금지.

### Content Relationship / Region Composition 원칙 (전체 Layout 공통, Content Density·Parallel Layout Alignment보다 선행 적용)
> 특정 Layout 전용 규칙이 아니라, 모든 PPT Layout에서 요소를 배치하기 전에 가장 먼저 적용되는 상위 판단 원칙이다. 목적은 슬라이드 요소를 입력된 순서나 콘텐츠 형식(표/차트/이미지/텍스트 등)이 아니라 콘텐츠 간 실제 역할·관계를 기준으로 먼저 큰 Content Region을 구성하는 것이다. 이 원칙에 따라 Region을 구성한 **이후에만** 아래 "Content Density / Content Group 원칙"과 "Parallel Layout Alignment 원칙"을 적용한다 — 두 원칙은 이 원칙이 구성한 Region 내부·Region 간의 세부 정렬·간격·크기 규칙을 그대로 담당하며, 이 원칙에서 그 규칙을 다시 정의하지 않는다.

**1) 콘텐츠 역할 분류 (Region 구성 전 선행 판단)** — 실제 슬라이드에 입력된 콘텐츠를 형식이 아니라 다른 콘텐츠와의 관계를 기준으로 아래 4가지 역할로 먼저 분류한다.
- **Primary Content**: 슬라이드의 핵심 메시지를 직접 전달하는 주요 정보. 중요도·역할이 대등한 Primary Content가 여러 개 있으면 하나의 병렬 Main Content Group으로 묶어 취급한다.
- **Dependent Content**: 특정 Primary Content 하나를 직접 설명·보완하는 정보. 해당 Primary Content와 같은 Region 안에 배치한다.
- **Shared Supporting Content**: 특정 Primary Content 하나가 아니라 둘 이상의 Primary Content를 함께 보완·종합하는 정보. **특정 Primary의 Column/Region 내부에 임의로 귀속시키지 않는다** — Main Content Group과 분리된 별도의 공통 Supporting Area 배치를 우선 검토한다.
- **Conclusion / Takeaway**: 여러 Primary Content를 종합해 도출되는 결론·시사점. 필요한 경우 전체 Main Content Group을 기준으로 별도의 통합 영역에 배치한다(병렬 구조에서의 구체적 배치 방식은 아래 Parallel Layout Alignment 원칙의 Integrated Conclusion 항목을 따른다).

**2) Region 구성 절차** — 콘텐츠 역할 분류 후, 세부 요소 배치보다 먼저 큰 Content Region을 구성한다.
- Primary Content(또는 대등한 Primary Content 묶음)를 기준으로 Main Content Region을 정한다.
- 각 Dependent Content는 대응하는 Primary Content의 Region 내부에 포함한다.
- Shared Supporting Content는 특정 Region에 종속시키지 않고, Main Content Region과 구분되는 별도 Supporting Region으로 둘지 먼저 판단한다.
- Conclusion/Takeaway가 필요하면 전체 Main Content Region 하단(또는 별도 위치)에 통합 Region으로 둘지 판단한다.
- Region의 수·크기는 고정하지 않는다. 실제 콘텐츠의 양·중요도·관계에 따라 필요한 Region의 개수와 크기를 그때그때 결정한다.

**3) 형식이 아닌 역할 기준 배치** — 표, 그래프, 이미지, KPI, 텍스트, 공정도 등 콘텐츠 형식 자체를 기준으로 위치를 고정하지 않는다(예: "좌측은 항상 표, 우측은 항상 그래프, 하단은 항상 강조 포인트"와 같은 형식별 고정 배치 규칙을 만들지 않는다). Region 배치는 항상 위 1)의 역할 분류와 콘텐츠 간 관계를 기준으로 결정한다. 표/차트/이미지/텍스트 중 무엇을 사용할지 자체의 선택 기준은 이 원칙이 아니라 `content-visualization-freedom.md`를 따른다.

**4) 적용 순서** — (1) 콘텐츠 역할 분류 → (2) 그 관계를 기준으로 Content Region 구성 → (3) Region 내부·Region 간 세부 배치는 아래 "Content Density / Content Group 원칙"(그룹 응집도·간격)과 "Parallel Layout Alignment 원칙"(동일 Top Line·Header·Width·Height 등)을 적용해 완성한다. 두 원칙의 세부 정렬·크기·간격 규칙은 이 원칙에서 다시 정의하지 않는다.

### Content Density / Content Group 원칙 (전체 Layout 공통)
> 특정 Layout 전용 규칙이 아니라, Three-Column을 포함한 모든 PPT Layout에 공통 적용되는 Design System 원칙이다. 의미적으로 연결된 콘텐츠가 불필요하게 멀리 떨어져 서로 무관해 보이지 않도록 하는 것이 목적이다. 어떤 요소가 어떤 Primary Content에 종속되는지(Dependent Content)는 위 "Content Relationship / Region Composition 원칙"의 역할 분류를 먼저 따른다.

- 의미적으로 연결된 요소(Key Message / Main Visual / Supporting Text / Evidence / Table / Chart / Bullet 등)는 하나의 **Content Group**으로 인식해 배치한다.
- **Group 내부 요소 간 간격은 좁게, 서로 다른 Content Group 사이의 간격은 상대적으로 넓게** 두어, 간격의 크기 차이 자체로 정보 위계와 묶음을 표현한다.
- 슬라이드에 남는 공간을 채우기 위해 의미적으로 연결된 요소 사이를 인위적으로 벌리지 않는다. `flex:1`, `space-between`, `justify-content:center` 등으로 여백을 배분하는 구현이 Content Group 내부 요소를 과도하게 떨어뜨리지 않도록 한다.
- 콘텐츠가 적은 경우에도 화면 전체를 억지로 채우기보다 Content Group 자체의 응집성을 우선한다. 반대로 콘텐츠를 한쪽에 과도하게 압축하지 않고, 전체 Content Area 안에서 시각적으로 균형 있게 배치한다.
- **Main Visual 특성에 따른 밀도 기준**:
  - **면적 점유형 Visual**(Chart / Photo / Image / Map / 복합 Diagram / Table 등): 필요한 시각적 면적을 충분히 확보하되, 연결된 제목·설명·Evidence와 관계가 끊겨 보이지 않도록 같은 Content Group 안에 배치한다.
  - **압축형 Visual**(Large Number / Icon / Symbol / 짧은 Quote / 짧은 Text 등): 넓은 고정 영역을 억지로 차지하게 하지 않고, Supporting Text/Evidence와 하나의 응집된 Content Group으로 밀착 배치한다.
  - Visual 유형과 실제 콘텐츠 양에 따라 높이·간격을 유동적으로 판단하며, 모든 Visual에 동일한 점유율이나 세로 배치 방식을 기계적으로 적용하지 않는다.
- 위 원칙은 상대적 밀도·그룹화 기준이며, 이 문서는 새로운 고정 px 간격 값을 정의하지 않는다 — 구체적인 여백 수치가 필요한 경우 해당 Layout Reference 또는 Hard Rule의 기존 수치를 따른다.

### Parallel Layout Alignment 원칙 (전체 Layout 공통)
> 특정 Layout 전용 규칙이 아니라, 2개 이상의 Column/Card/Comparison Area/Content Group이 동일 계층으로 병렬 배치되는 모든 PPT Layout에 공통 적용되는 Design System 원칙이다. 목적은 모든 슬라이드의 본문 시작 위치를 고정하는 것도, 모든 병렬 Layout을 기계적으로 동일 폭·동일 구조로 만드는 것도 아니다 — 콘텐츠에 따라 본문 전체의 위치·높이는 자유롭게 결정하되, **별도의 구조적 이유가 없는 병렬 영역에서 임의적인 비대칭을 방지하고 정렬 일관성을 확보**해 같은 슬라이드 안에서 병렬 배치된 요소들이 하나의 정렬된 그룹처럼 보이도록 하는 것이 목적이다. 아래 항목은 슬라이드 간 절대 위치를 통일하는 규칙이 아니라, 동일 슬라이드 내부의 병렬 요소 간 상대 정렬·균형 규칙이다.

- **동일 Top Line**: 동일 계층으로 병렬 배치되는 2개 이상의 Column/Card/Comparison Area/Content Group은 반드시 동일한 Top Y에서 시작한다. 한쪽 콘텐츠가 적거나 많다는 이유로 개별 영역의 시작 위치를 위·아래로 옮기지 않는다. 이 Top Y는 Content Area 최상단에 단순히 붙이는 값이 아니라, 상단 여백과 전체 수직 균형을 고려해 정한 위치이며, 병렬 영역은 그 위치에서 함께 시작한다(2026-08-19 명확화 — 이전에는 "동일 Y"만 규정해 상단에 붙인 정렬도 이 원칙을 만족하는 것으로 오독될 수 있었다).
- **동일 Header Alignment**: 병렬 영역 각각에 Header가 있는 경우 모든 Header의 Y Position과 Height를 동일하게 하고, Header 아래 Main Content의 시작 위치도 동일하게 맞춘다.
- **동일 Width / 균등 분할(기본값, 절대 강제값 아님)**: 동일 역할·동일 위계의 병렬 영역은 기본적으로 동일 Width를 사용한다(2-Column은 1:1, 3-Column은 1:1:1을 **기본값**으로 한다). 이 기본값은 절대 강제값이 아니며, 다음 중 하나에 해당하면 비대칭 비율을 허용한다.
  - **Reference 확정 비율 유지**: 해당 Layout Reference의 실제 Reference PPT에서 이미 의도적으로 확정된 비대칭 비율이 있는 경우, 그 비율을 그대로 유지한다 — 이 공통 원칙 때문에 자동으로 1:1 등 기본값으로 덮어쓰지 않는다.
  - **구조적으로 다른 역할**: 병렬 영역의 역할·정보 유형이 구조적으로 다른 경우(예: 기준/범례 Column vs 데이터 Column, Criteria Column vs Target Column) 비대칭을 허용한다.
  - **명확한 강조 목적**: 특정 영역의 강조가 해당 Layout의 명확한 목적인 경우 비대칭을 허용한다.
  - **Table/Matrix형 구조**: Table/Matrix처럼 Column별 역할이 본질적으로 다른 구조에는 이 동일 폭 기본값 자체를 강제하지 않는다 — Column/Row 크기는 각 Layout Reference가 정의한 콘텐츠 분량 기준을 따른다.
  - 위 예외에 해당하지 않고 단순히 한쪽 텍스트가 조금 더 많다는 이유만으로는 Column 폭을 임의 조정하지 않는다 — 먼저 내부 Content Group·Gap·Text Length 등 내부 구성 조정으로 해결한다(아래 Content Difference 처리 참조).
- **동일 Height / Bottom Alignment**: 동일 역할의 Column/Card/Container는 가능한 한 동일 Height를 사용하고 Bottom Line을 맞춘다. 콘텐츠량이 적다는 이유로 한쪽 Container만 짧게 만들지 않는다. 단, Container 자체를 사용하지 않는 자유형(Freeform) 구조에는 강제하지 않는다.
- **대응 요소 정렬**: 병렬 영역 내부에서 역할이 동일하거나 서로 대응되는 요소(예: Title↔Title, Visual↔Visual, Step↔Step, Supporting Text↔Supporting Text)는 가능한 한 동일 Y축에 배치한다. 의미적 흐름을 왜곡하면서까지 강제로 정렬하지는 않는다.
- **Gap / Padding 통일**: 병렬 영역 사이의 Gap은 동일하게 유지한다. 동일 종류의 Column/Card/Box는 동일한 Internal Padding을 사용한다. 빈 공간을 채우기 위해 특정 영역만 임의로 확대하거나 이동하지 않는다.
- **Content Difference 처리**: 병렬 영역 간 콘텐츠량이 달라도 외곽 영역의 정렬과 비율을 먼저 유지한다. 콘텐츠량 차이는 Column/Container의 폭·높이가 아니라 내부 Gap, Text Length, Visual Size 등 내부 구성으로 해결한다. 콘텐츠가 적다는 이유로 해당 Column 자체를 축소하거나 중앙으로 따로 이동시키지 않는다. `space-between`, `margin-top:auto` 등으로 콘텐츠를 양 끝에 강제 분산해 그 차이를 흡수하지 않는다(line 87의 Content Group 내부 응집 anti-pattern과 동일한 이유 — 병렬 영역 간 균형에도 동일하게 적용된다) — 이런 기법은 콘텐츠가 적은 영역에서 중앙에 의도치 않은 죽은 공간을 만든다.
- **Integrated Conclusion**: 2개 이상의 병렬 영역을 비교·종합해 하나의 결론을 도출할 수 있는 경우, 하단에 전체 영역을 통합하는 Conclusion/Key Takeaway를 우선 고려한다. Conclusion은 특정 Column에 속하지 않고 전체 병렬 Content Group의 폭과 중심축을 기준으로 배치한다. 단순 나열형이거나 통합 결론이 필요하지 않은 콘텐츠에는 강제하지 않는다.

**중요**: 위 원칙은 모든 슬라이드의 Content Start Y를 동일하게 고정하는 규칙이 아니다 — 슬라이드마다 본문의 위치·높이는 콘텐츠에 따라 자유롭게 결정하며, 이 원칙은 동일 슬라이드 내부에서 병렬 배치된 요소 간 상대적 정렬·균형에만 적용된다. 기존 Hard Rule 및 개별 Layout Reference의 고유 구조는 그대로 유지하며, 이 원칙이 그것을 대체하지 않는다. 특히 **이미 확정(1차 확정 포함)된 개별 Layout Reference의 Reference 실측 비율·구조는 이 공통 원칙 때문에 자동으로 덮어쓰지 않는다** — 해당 Layout을 다시 다룰 필요가 생겼을 때 이 문서의 기본값·예외 조건을 함께 검토한다.

## 6. Shape / Card / Line Style
네이티브 표/차트 대신 아래 컴포넌트 조합으로 모든 도식을 구성한다.
- **Line**: 얇은(1px 상당) 구분선/연결선. 색상은 Neutral Gray 또는 Brand Mid.
- **RoundRect Card/Tag**: 라운드렉트, 코너 radius 소–중. 카드 배경은 화이트 또는 Tint 배경, 테두리 없음 또는 1px Neutral 테두리. 좌측 컬러 바 등 장식적 accent border는 사용하지 않음. Card는 콘텐츠를 감싸는 기본 표현 방식이 아니다 — 짧은 Tag/Label 또는 그룹 구분이 명확히 필요한 경우에만 제한적으로 사용하고, 일반 콘텐츠는 카드로 감싸지 않는 직선적·평면적(Flat/Open) Presentation Layout을 우선한다.
- **Arrow**: rightArrow 도형으로 프로세스/흐름 표시. 색은 Brand 계열.
- **Connector**: 커넥터 라인으로 플로우차트·조직도 연결.
- **Ellipse/Arc**: 아이콘성 포인트, 원형 프레임(인물 사진 등)에 제한적으로 사용. Process Stage의 기본 시각 요소로 원형 Step/숫자 아이콘을 사용하지 않으며, Process Stage는 실제 이미지·다이어그램 등 콘텐츠 기반 Visual을 우선한다.
- 그림자(Shadow)는 원칙적으로 미사용. 그라디언트는 커버/강조 배경 1곳 이하로 제한.

## 7. Image Treatment
- 인물 사진: 흑백 또는 듀오톤 처리, 배경 투명/화이트, 배경색은 Tint 계열로 통일.
- 제품/기술 이미지: 3D 컷어웨이·다이어그램 렌더링은 원색 유지 허용(제품 실제 색 전달이 목적).
- 현장/실험 사진: 채도를 낮추거나 브랜드 틸 톤으로 틴트하여 팔레트에 흡수.
- 커버/배경용 사진: 저투명도(alpha 50–60%) + 브랜드 그라디언트 오버레이로 텍스트 가독성과 톤 통일 확보.
- 모든 이미지는 배경과 자연스럽게 붙도록 리무브/크롭 처리, 사진 주위 장식 프레임(그림자, 테두리) 금지.

## 8. Chart / Table / Diagram Style
- 네이티브 파워포인트 표/차트를 그대로 쓰지 않고, 위 Shape 컴포넌트로 재구성한 도식을 기본으로 한다.
- 데이터 강조는 색이 아닌 크기·웨이트 우선, 색 강조는 시그널 컬러로 최소 사용.
- 타임라인/프로세스: Image/Diagram/Visual 중심 Stage + Connector/Arrow로 좌→우 또는 상→하 흐름 구성. Stage를 원형 Step/숫자 아이콘이나 RoundRect 카드로 기본 표현하지 않는다.
- 비교/구조 다이어그램: 동일 크기의 영역 + 얇은 라인 구분을 기본으로 하며, Card 그리드는 기본값이 아니다. 그룹 구분이 명확히 필요한 경우에만 제한적으로 Card를 사용한다.
- 수치 강조: 큰 숫자(Pretendard ExtraBold) + 하단 작은 라벨(Pretendard Light) 조합은 기본 표현 방식이 아니며, KPI·핵심 지표를 강조해야 하는 경우에만 제한적으로 사용한다.

### Chart / Graph Color Usage
- COSOLUS/자사 데이터: Company Main Color 계열(Hard Rule §5 Brand Color 표의 Primary 컬러)을 사용한다.
- 기존 방식·경쟁사·비교 대상 데이터: Gray 계열(Neutral Gray)을 사용한다.
- 비교 과정의 Difference/Guide Line, 보조 연결선: 연한 Orange 계열(Flame Amber 계열의 옅은 톤)을 제한적으로 사용한다.
- Chart Title에서 기존/비교 대상은 Black/Dark + SemiBold, COSOLUS/자사는 Company Main Color + ExtraBold로 강조한다.
- 일반 축, 눈금, Label, 단위는 Black/Dark 또는 Gray를 사용한다.
- 데이터 구분을 위해 임의의 다양한 색상을 추가하지 않는다.
- Orange를 핵심 수치나 일반 Text의 강조색으로 사용하지 않는다.
- 별도 의미가 없는 경우 Main Color + Gray 중심의 최소 색상 구성을 유지한다.

### Table Style
- Table Header/Body/강조/Grid 관련 규칙은 Hard Rule §10B를 따른다.
- 그 외 불필요한 색상·장식(그라디언트, 다색 배색, 과도한 Border 강조 등)을 사용하지 않는다.
- 모든 Header/Body Cell Text는 가로·세로 모두 Center Align을 기본으로 한다.
- Table은 배치된 Content Area/Evidence Area를 강제로 꽉 채우지 않는다 — 내용량(Row 수·텍스트 길이)에 맞춰 Table 전체 크기와 Row Height를 조정한다.
- 위 조정으로 Table이 Content Area/Evidence Area보다 작아지는 경우, 축소된 Table은 해당 영역 안에서 중앙 배치한다.
- 크기·Row Height가 축소되는 경우에도 기존 Column 비율과 위 Table Style 항목(Header/Body 색상, Divider, 자사 강조 방식 등)은 그대로 유지한다.

## 9. 공통적으로 유지해야 하는 디자인 원칙
- 컬러: 브랜드 틸 계열 + 화이트 + 그레이의 단색 팔레트, 시그널 컬러는 예외적·국소적 사용만.
- 폰트: Pretendard 단일 서체(Weight로 위계 구분, 강조 숫자/타이틀은 ExtraBold). Font Family 규칙은 Hard Rule §2를 따른다.
- 레이아웃 골격: 상단 타이틀 / 하단 콘텐츠, 좌측 정렬 기본.
- 모든 도식은 정의된 Shape 컴포넌트(Line/RoundRect/Arrow/Connector/Ellipse)로만 구성.
- 사진은 항상 팔레트에 맞게 톤 처리.
- 그림자 미사용, 그라디언트는 슬라이드당 1개 이하.
- 슬라이드당 1차 강조 요소는 1개.

## 10. 콘텐츠에 따라 자유롭게 변경 가능한 요소
- 슬라이드별 레이아웃 구조(그리드 열 수, 카드 개수, 타임라인 방향 등)
- 강조 숫자/통계의 개수와 배치
- 사용하는 이미지의 종류(제품 렌더링/인물/현장 사진 등)와 개수
- 카드·타임라인·비교 다이어그램 등 콘텐츠 유형별 도식 조합 방식
- 섹션별 포인트 컬러(브랜드 틸 계열 내에서의 명도 선택)
