# Business Site Map Layout (v3)

> v2(2026-08-18, 코솔러스-넥스모션테스트 프로젝트에서 등록)를 대체한다. 변경 사유: 사용자가
> "지도 자체를 이미지 생성 기능으로 만들고, PPT 객체(Marker/Text/Connector/Card)는 별도로
> 얹는" 3분리 원칙(§17 Core Principle)을 명시적으로 승인해 v2의 "PPT 도형(SVG 실루엣)만으로
> 직접 그린 개략 지도" 방식을 대체함(2026-08-18).
> 원문에서 Hard Rule 참조 파일명을 `00_design-system.md`로 표기했으나, 이 프로젝트에서 실제
> 적용 중인 공통 Hard Rule은 `docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`
> (§9 공통 Header System 포함)이므로 아래 §2에서 해당 경로로 정정해 반영했다. 그 외 원문
> 내용은 변경하지 않았다.
>
> **실행 방식 확정(2026-08-18)**: §5~§7의 "이미지 생성 기능"은 이 파이프라인(웹PPT 생성
> 에이전트) 내부에서 호출할 수 있는 도구가 아니며, 임시 제약이 아니라 **구조적으로 이 단계는
> 항상 파이프라인 바깥(사용자가 별도의 이미지 생성 도구/서비스에서 직접 생성)에서 수행**하는
> 것으로 워크플로우를 확정한다. 따라서 실제 진행 순서는 다음과 같다.
> 1. 에이전트가 §6 프롬프트의 `{사업장 지역 목록}`을 실제 입력 데이터로 채워 사용자에게 전달한다.
> 2. 사용자가 그 프롬프트를 외부 이미지 생성 도구에 넣어 Base Map 이미지를 만들고,
>    파일로 전달한다(권장 저장 경로: `docs/brand-assets/images/business-site/`).
> 3. 에이전트는 전달받은 이미지를 Base Map으로 놓고 §8~§14(Marker/Connection Line/
>    Information Card)를 PPT Object로 그 위에 조립한다.
> Base Map 이미지가 아직 없는 프로젝트/슬라이드는 이전 리비전(v2)의 PPT 도형(SVG) 기반
> 개략 지도를 대체재로 유지한다.

## 1. Purpose

본사, 연구소, 공장, 생산센터, 고객지원센터 등
복수 사업장의 위치와 역할을 지도 기반으로 표현하기 위한 범용 레이아웃이다.

사업장 위치 자체가 중요한 정보인 경우 단순 표나 카드보다
지도 기반 레이아웃을 우선적으로 고려한다.

---

## 2. Hard Rule

전체 디자인은 [`docs/design-hard-rules/2026.08.12_design_hard-rules_V2.md`](../design-hard-rules/2026.08.12_design_hard-rules_V2.md)의 Hard Rule을 최우선으로 적용한다.

다음 요소는 Hard Rule의 정의를 그대로 따른다.

- Brand Color
- Font
- Title / Subtitle
- Background
- Margin
- Line
- Card Style
- 기본 도형 스타일

본 MD에서 별도의 고정 HEX Color를 지정하지 않는다.

Hard Rule과 본 MD가 충돌하는 경우 Hard Rule을 우선한다.

---

## 3. When to Use

다음 조건에서는 본 지도형 레이아웃을 우선 고려한다.

- 사업장이 2개 이상 존재
- 본사 / 연구소 / 공장 / 지원센터 등 지역별 역할이 구분됨
- 사업장 위치를 함께 보여주는 것이 정보 전달에 도움이 됨
- 회사 개요 / 사업장 소개 / 생산 인프라 소개 슬라이드

다음의 경우에는 지도 사용을 강제하지 않는다.

- 사업장이 1개뿐인 경우
- 모든 사업장이 동일 지역에 집중된 경우
- 위치보다 사업장 간 기능 비교가 중요한 경우

사용자가 명시적으로 지도형 표현을 요청한 경우에는
본 레이아웃을 우선 적용한다.

---

## 4. Layout Structure

기본 구조는 다음과 같다.

```
[ MAP ] + [ LOCATION MARKER ] + [ SITE INFORMATION ]
```

사업장 상세정보가 필요한 경우:

```
┌──────────────────────┬────────────────────────┐
│                      │  SITE 01               │
│                      │  [PHOTO]               │
│                      │  주요 기능              │
│       MAP            ├────────────────────────┤
│                      │  SITE 02               │
│     ●                │  [PHOTO]               │
│          ●           │  주요 기능              │
│              ●       ├────────────────────────┤
│                      │  SITE 03               │
│                      │  [PHOTO]               │
│                      │  주요 기능              │
└──────────────────────┴────────────────────────┘
```

사업장 정보량과 개수에 따라
지도와 Information Card의 비율은 조정할 수 있다.

---

## 5. Map Generation

### 핵심 원칙

지도 이미지가 제공되지 않은 경우
PPT 도형만으로 지도를 임의 제작하지 않는다.

사용 가능한 이미지 생성 기능을 이용하여
PPT용 Base Map 이미지를 먼저 생성한 후 슬라이드에 삽입한다.

역할을 다음과 같이 분리한다.

**Generated Image**
- 지도 형태
- 행정구역 경계
- 지도 배경

**PPT Object**
- Location Marker
- 사업장명
- 지역명
- Connection Line
- Information Card
- Legend

**External Image**
- 실제 사업장 사진
- 공장 사진
- 연구소 사진
- 사옥 사진

---

## 6. Map Image Generation Prompt

사업장 위치 정보를 분석한 후
아래 프롬프트의 `{변수}`를 실제 입력 정보에 맞게 구성하여
지도 이미지를 생성한다.

### Prompt

```
대한민국 내 {사업장 지역 목록}의 위치 관계를 표현하기 위한
기업용 PPT Base Map 이미지를 생성해줘.

대한민국 전체 지형과 행정구역 형태를 실제 지리적 구조에 가깝게 표현하고,
특히 {사업장 지역 목록}이 위치한 지역을 지도 위에서 정확하게 식별할 수 있는
지리적 구조를 유지해줘.

전체 디자인은 이 프로젝트의 Hard Rule 브랜드 디자인(Cosolus Teal 계열)과
조화되는 미니멀한 corporate infographic 스타일로 구성해줘.

지도는 매우 밝고 절제된 저채도 스타일로 표현하고,
PPT에서 추가할 Location Marker와 텍스트보다 시각적으로 강조되지 않도록 해줘.

지도 내부에는 광역 행정구역 경계 정도만 얇게 표현해줘.

지도 위에는 다음 요소를 절대 넣지 마:

- 지역명
- 도시명
- 텍스트
- Location Pin
- 사업장명
- 주소
- 도로
- 건물
- 범례
- 장식용 아이콘

Location Marker와 사업장 정보는 PPT에서 별도로 추가할 예정이다.

배경은 흰색 또는 투명 배경으로 제작해줘.

Clean corporate infographic,
minimal vector map,
flat design,
high resolution,
no text,
no labels,
no location pins,
no decorative elements.
```

---

## 7. Map Scale Selection

입력된 사업장 위치에 따라 지도 범위를 자동 판단한다.

### 전국 단위

사업장이 서로 다른 광역권에 분산된 경우
대한민국 전체 지도를 사용한다.

예: 수도권 + 충청권 + 영남권 → 대한민국 전체 지도

### 권역 단위

모든 사업장이 특정 권역에 집중된 경우
해당 지역을 확대하여 표현할 수 있다.

예: 전주 + 익산 + 군산 → 전북 중심 확대 지도 고려

### 도시 단위

모든 사업장이 동일 도시 내에 위치하는 경우
전국 지도보다 도시 또는 지역 확대 지도를 우선 고려한다.

지도 범위는 디자인적 균형보다
사업장 간 위치 관계를 명확하게 전달하는 것을 우선한다.

---

## 8. Location Marker

지도 이미지 생성 후
각 사업장 위치에 PPT 객체로 Location Marker를 추가한다.

Marker는 이미지에 포함시키지 않는다.

Marker Style은 Hard Rule의 Primary / Accent Color를 따른다.

Marker 주변에는 간결한 지역명을 표시할 수 있다.

예: ● 전주 / ● 서울 / ● 화성

가능한 경우 사용자가 제공한 실제 주소를 기준으로 위치를 판단한다.

위치 판단 우선순위:

1. 상세 주소
2. 시 / 군 / 구
3. 도시
4. 광역자치단체

Marker의 위치 정확도를 시각적 균형보다 우선한다.

---

## 9. Connection Line

필요한 경우 Marker와 Site Information Card를 연결한다.

Connection Line은 PPT 객체로 생성한다.

권장 방식:

- Thin Line
- Dashed / Dotted
- Brand Color
- 2~3 Segment Connector

연결선끼리 교차하지 않도록 우선 배치한다.

지도 위의 주요 Marker를 가리지 않는다.

---

## 10. Site Information Card

각 사업장은 하나의 Information Card로 표현할 수 있다.

권장 정보:

- 사업장명
- 지역
- 주소
- 주요 기능 3~5개
- 사업장 사진

정보 우선순위:

1. 사업장명
2. 지역
3. 사업장 사진
4. 주요 역할
5. 상세 주소

장문의 설명은 사용하지 않는다.

---

## 11. Business Site Image

사업장 사진은 지도 이미지 생성 과정에 포함하지 않는다.

실제 사업장 사진이 제공된 경우
Information Card 내부에 별도로 삽입한다.

이미지 자산이 별도 폴더에 존재하는 경우
사업장명 또는 지역명을 기준으로 적절한 이미지를 탐색한다.

예시 경로: `docs/brand-assets/images/business-site/`

이미지 파일 예시:

```
headquarters.png
factory.png
research-center.png
site-01.png
```

---

## 12. Image Placeholder

실제 사업장 사진이 없는 경우
AI가 임의의 회사 건물 사진을 생성하여 사용하지 않는다.

대신 사진이 들어갈 영역만 확보한다.

```
[ SITE PHOTO ]
```
또는
```
[ INSERT IMAGE ]
```

Placeholder는 실제 사진 삽입을 위한 위치와 크기만 정의한다.

최종본 제작 시 실제 이미지로 교체할 수 있어야 한다.

---

## 13. Multiple Site Rule

사업장 개수에 따라 정보 표현량을 조절한다.

### 1 Site
지도 사용 여부를 재검토한다. 필요하면 지도 + 대형 Information Card 구성.

### 2 Sites
지도 + 2개 Information Card.

### 3 Sites
지도 + 3개 Information Card의 Vertical Stack을 우선 고려.

### 4 Sites
지도 + 2×2 Card 또는 지도 주변 분산 배치.

### 5 Sites 이상
모든 사업장을 대형 Card로 표현하지 않는다.

지도에는 전체 Marker를 표시하고 핵심 사업장만 상세 Card로 표현한다.

나머지는 Legend 또는 Summary 형태로 단순화한다.

---

## 14. Visual Priority

시각적 우선순위:

1. 사업장 위치 관계
2. Location Marker
3. 사업장명
4. 사업장 사진
5. 주요 기능
6. 상세 주소

지도는 배경 장식이 아니라
사업장 간 지리적 관계를 전달하는 정보 시각화 요소로 사용한다.

단, 지도 자체가 Marker와 사업장 정보를 압도해서는 안 된다.

---

## 15. Prohibited

다음은 금지한다.

- AI 생성 지도 내부에 텍스트 삽입
- AI 생성 지도 내부에 Location Marker 삽입
- AI 생성 지도 내부에 사업장명 삽입
- AI 생성 지도 내부에 사업장 사진 합성
- 존재하지 않는 사업장 건물 이미지 생성
- 실제 위치와 무관한 Marker 배치
- 과도한 3D 지도
- 위성지도 스타일
- 관광지도 스타일
- 도로지도 스타일
- 불필요한 지역명 표시
- 과도한 그림자 및 장식 효과

---

## 16. Workflow

사업장 정보가 입력되면 다음 순서로 처리한다.

1. 사업장명 / 주소 / 역할 추출
2. 사업장 지역 목록 생성
3. 사업장 간 지리적 분포 분석
4. 전국 / 권역 / 도시 지도 범위 결정
5. Map Image Generation Prompt 구성
6. Base Map 이미지 생성
7. 생성된 Map 이미지를 PPT에 삽입
8. 실제 위치 기준 Location Marker 배치
9. Connection Line 생성
10. Information Card 구성
11. 실제 사업장 사진이 있으면 삽입
12. Hard Rule 기준 최종 디자인 검증

---

## 17. Core Principle

본 레이아웃은 다음 세 요소를 분리하여 제작한다.

**AI Generated Map** → 고품질 Base Map

**PPT Objects** → Marker / Text / Connection Line / Information Card

**External Assets** → 실제 사업장 사진

지도 이미지는 시각적 기반만 담당하고,
수정 가능성이 높은 사업장 위치·텍스트·사진은
PPT에서 별도 객체로 관리한다.
