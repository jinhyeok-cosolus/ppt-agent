# brand-assets

회사 로고, 브랜드 요소 등 **고정 규칙**에 쓰이는 자산을 등록하는 폴더다. 프로젝트마다 새로
받지 않고 한 번 등록해 모든 프로젝트에서 재사용한다.

## 사용법
1. 로고 등 브랜드 자산 파일을 이 폴더에 저장한다 (예: `logo.svg`, `logo-white.svg`).
2. `.claude/skills/web-ppt-generator/references/design-rules.md`의 "고정 규칙" 섹션에
   파일 경로와 적용 규칙(위치, 크기, 예외 등)을 사용자 승인을 받아 기록한다.
3. 이후 모든 프로젝트의 웹PPT/pptx 생성 시 이 폴더의 파일을 상대/절대 경로로 참조한다.

## 현재 등록된 자산
- `cosolus CI_2.png` — COSOLUS 공식 로고 (Color, 일반/밝은 배경용)
- `cosolus CI.png` — COSOLUS 공식 로고 (White/Reversed, 다크 배경용 — 예: 표지)
- `화살표 이미지.png` — 화살표 이미지 자산

적용 규칙(사용 우선순위, 반복 배치 등)은 [`.claude/skills/web-ppt-generator/references/design-rules.md`](../../.claude/skills/web-ppt-generator/references/design-rules.md)의 "고정 규칙 > 회사 로고 및 Motto" / "공통 Deck Element" 섹션 참고.

## cover-images/ — 표지용 Background Image Library

`cover-images/` 폴더는 COSOLUS 표지 슬라이드 전용 배경 이미지 라이브러리다.
표지 배경 이미지 선택 우선순위는
[`docs/slide-design-rules/01_cover_design_V2.md`](../slide-design-rules/01_cover_design_V2.md)를 따른다.

표지 이미지를 선택할 때는 폴더 내 파일을 매번 전부 열어 분석하지 않고,
아래 파일명·권장 사용 주제 설명을 먼저 참고해 발표 주제와 가장 적합한
이미지를 고른다.

| 파일명 | 이미지 내용 | 권장 사용 주제 |
|---|---|---|
| `표지 이미지_1.png` | 시험관 클로즈업, 액체 방울이 떨어지는 장면 (틸톤 계열 흑백) | 화학소재 R&D, 신소재/신제품 개발, 화학 공정·분석 관련 발표 |
| `이미지_2.png` | 정장 차림 인물이 양손으로 글로벌 네트워크 홀로그램(지구본 + 비즈니스 아이콘)을 받쳐 든 장면 (흑백) | 글로벌 사업 전략, 파트너십, 회사소개/경영 개요 등 비즈니스 중심 발표 |
| `이미지_3.png` | 방진복·마스크·보안경을 착용한 연구원이 밀폐 장비(반응기/컴파운딩 설비)를 다루는 장면 (흑백) | 생산·제조 공정, 컴파운딩/마스터배치 제조, 품질관리 등 공정·설비 중심 발표 |

새 이미지를 추가할 때는 파일을 `cover-images/`에 저장한 뒤 위 표에
파일명과 권장 사용 주제를 함께 등록한다.
