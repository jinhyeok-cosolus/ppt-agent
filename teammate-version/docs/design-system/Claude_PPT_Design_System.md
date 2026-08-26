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
- 전체 서체(Font Family): **Pretendard 단일 서체** (Thin/Light/Regular/Medium/SemiBold/Bold/ExtraBold/ExtraLight). Hard Rule §2에 따라 표지를 포함한 모든 슬라이드에서 Pretendard 외 서체(과거 G마켓 산스 등)는 사용하지 않는다.
- 역할 분리 원칙: 서체가 아닌 **Weight**로 정보 위계·강조 수준을 구분한다. 커버 타이틀·핵심 통계 숫자 등 가장 강한 위계는 Pretendard ExtraBold, 일반 섹션 타이틀은 ExtraBold~Bold, 본문은 Regular/Medium을 기본으로 한다.

| 레벨 | 서체/웨이트 | 크기(pt) | 용도 |
|---|---|---|---|
| Display | Pretendard ExtraBold | 44–60 | 커버 타이틀 |
| H1 | Pretendard ExtraBold | 28–30 | 섹션 타이틀 |
| H2 | Pretendard SemiBold | 20–24 | 서브 타이틀 |
| Body | Pretendard Regular/Medium | 14–16 | 본문 |
| Caption | Pretendard Light | 9–12 | 캡션·출처·주석 |
| Stat Number | Pretendard ExtraBold | 24–30 | 강조 수치 |

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

### Content Density / Content Group 원칙 (전체 Layout 공통)
> 특정 Layout 전용 규칙이 아니라, Three-Column을 포함한 모든 PPT Layout에 공통 적용되는 Design System 원칙이다. 의미적으로 연결된 콘텐츠가 불필요하게 멀리 떨어져 서로 무관해 보이지 않도록 하는 것이 목적이다.

- 의미적으로 연결된 요소(Key Message / Main Visual / Supporting Text / Evidence / Table / Chart / Bullet 등)는 하나의 **Content Group**으로 인식해 배치한다.
- **Group 내부 요소 간 간격은 좁게, 서로 다른 Content Group 사이의 간격은 상대적으로 넓게** 두어, 간격의 크기 차이 자체로 정보 위계와 묶음을 표현한다.
- 슬라이드에 남는 공간을 채우기 위해 의미적으로 연결된 요소 사이를 인위적으로 벌리지 않는다. `flex:1`, `space-between`, `justify-content:center` 등으로 여백을 배분하는 구현이 Content Group 내부 요소를 과도하게 떨어뜨리지 않도록 한다.
- 콘텐츠가 적은 경우에도 화면 전체를 억지로 채우기보다 Content Group 자체의 응집성을 우선한다. 반대로 콘텐츠를 한쪽에 과도하게 압축하지 않고, 전체 Content Area 안에서 시각적으로 균형 있게 배치한다.
- **Main Visual 특성에 따른 밀도 기준**:
  - **면적 점유형 Visual**(Chart / Photo / Image / Map / 복합 Diagram / Table 등): 필요한 시각적 면적을 충분히 확보하되, 연결된 제목·설명·Evidence와 관계가 끊겨 보이지 않도록 같은 Content Group 안에 배치한다.
  - **압축형 Visual**(Large Number / Icon / Symbol / 짧은 Quote / 짧은 Text 등): 넓은 고정 영역을 억지로 차지하게 하지 않고, Supporting Text/Evidence와 하나의 응집된 Content Group으로 밀착 배치한다.
  - Visual 유형과 실제 콘텐츠 양에 따라 높이·간격을 유동적으로 판단하며, 모든 Visual에 동일한 점유율이나 세로 배치 방식을 기계적으로 적용하지 않는다.
- 위 원칙은 상대적 밀도·그룹화 기준이며, 이 문서는 새로운 고정 px 간격 값을 정의하지 않는다 — 구체적인 여백 수치가 필요한 경우 해당 Layout Reference 또는 Hard Rule의 기존 수치를 따른다.

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
- 직각형(Rectangular) Table 구조를 기본으로 한다. Rounded Corner, Card 그림자를 사용하지 않는다.
- **Data Comparison Table 기본형**: 비교 대상 개수와 무관하게 첫 Header Row 전체 = Company Main Color 계열(Hard Rule §5 Brand Color 표의 Primary 컬러) Fill + White Bold Text로 통일한다. Header Row를 Column/대상 단위로 나눠 일부만 Fill하는 예외를 두지 않는다.
- Body Row: White 배경 + Black/Dark Text.
- Cell 구분은 얇은 직선(Divider)으로만 표현한다.
- COSOLUS/자사 강조가 필요한 Cell/Text는 Body Fill이 아니라 Company Main Color Text + Bold로 표현한다. 기존/비교 대상의 Body Text는 Black/Dark를 유지한다.
- COSOLUS 강조를 Row 또는 Column 전체 배경 Fill로 고정하지 않는다 — 강조는 항상 텍스트 색상과 Weight로만 표현한다.
- **Reference가 있는 경우**, 위 기본 Header/강조 방식보다 Reference가 실제로 사용한 방식을 우선 적용한다.
- 그 외 불필요한 색상·장식(그라디언트, 다색 배색, 과도한 Border 강조 등)을 사용하지 않는다.
- 모든 Header/Body Cell Text는 가로·세로 모두 Center Align을 기본으로 한다.
- Table은 배치된 Content Area/Evidence Area를 강제로 꽉 채우지 않는다 — 내용량(Row 수·텍스트 길이)에 맞춰 Table 전체 크기와 Row Height를 조정한다.
- 위 조정으로 Table이 Content Area/Evidence Area보다 작아지는 경우, 축소된 Table은 해당 영역 안에서 중앙 배치한다.
- 크기·Row Height가 축소되는 경우에도 기존 Column 비율과 위 Table Style 항목(Header/Body 색상, Divider, 자사 강조 방식 등)은 그대로 유지한다.

## 9. 공통적으로 유지해야 하는 디자인 원칙
- 컬러: 브랜드 틸 계열 + 화이트 + 그레이의 단색 팔레트, 시그널 컬러는 예외적·국소적 사용만.
- 폰트: Pretendard 단일 서체(Weight로 위계 구분, 강조 숫자/타이틀은 ExtraBold). Hard Rule §2에 따라 다른 서체를 혼용하지 않는다.
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
