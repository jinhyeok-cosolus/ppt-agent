---
title: COSOLUS PPT 디자인 시스템 (공유 자산)
version: v2 · LIGHT
source: 레이아웃_샘플.pptx (14슬라이드) + 색_팔레트.pdf (10p) 분석 결과
purpose: Purpose Skill(목적별 PPT 생성 스킬)이 실행될 때 자동 참조하는 공용 규칙. 이 파일은 직접 트리거되지 않는다.
---

# 00. 디자인 시스템 개요

이 문서는 코솔러스(COSOLUS) 사내 PPT의 "공용 자산(Shared Assets)"이다.
`01_cover.md` ~ `14_closing-contact.md`는 각 슬라이드 유형의 전용 스펙이며,
모두 이 파일에 정의된 캔버스/색상/타이포/그리드/헤더-푸터 규칙을 상속한다.

## 캔버스
- 크기: **1920 × 1080px** (20 × 11.25in, 16:9) — pptx 원본 `18288000 × 10287000 EMU`
- 좌우 여백(margin): **112px** 고정
- 좌표계: 좌상단 (0,0) 기준 px

---

# 01. 컬러 팔레트

## Primary (코어 컬러 · 틸 계열)
| 이름 | HEX | 용도 |
|---|---|---|
| Cosolus Teal | `#005B58` | 대표색 · 헤더바 · 로고(라이트 배경) · 타이틀/표 헤더 강조 |
| Sea Teal | `#1A8C82` | 그래프 1순위 · 키워드 · 아이콘 · 불릿마커 |
| Mint | `#7FCBBE` | 그래프 2순위 · 딤톤(다크) 배경 위 강조 텍스트 · md힌트 뱃지 라인 |
| Deep Pine | `#06342F` | 표지 그라디언트 종단색 · 본문 최고 대비(자사 강조행) |

## Derived (파생색 · 사업축별)
| 이름 | HEX | 용도 |
|---|---|---|
| Ocean Blue | `#14618C` | 배터리 재활용 사업축 · 공정 다이어그램 전용 강조 |
| Moss | `#6F9B3F` | 자원순환 사업축 · 3계열 이상 차트에서 3번째 계열 |
| Flame Amber | `#C8801F` | 단면 강조 · 핵심 수치(%, 데이터) · 액센트 바(밑줄/좌측 라인) |

## Neutral (무채색)
| 이름 | HEX | 용도 |
|---|---|---|
| Mist | `#F3F6F5` | 카드/표/뱃지 배경 |
| Line | `#E1E7E5` | 구분선 · 보더 · 그리드라인 (두께 1px) |
| Gray | `#8C9694` | 보조 라벨 · 비활성 텍스트 · 페이지 번호 |
| Slate | `#5A6A68` | 본문 보조 텍스트 · 표 헤더(비교군/기존) 배경 |
| Ink | `#16201F` | 본문 최고 대비 텍스트 · 타이틀 |

## 다크 배경(틸 그라디언트) 전용 텍스트 톤
표지·섹션 간지·마무리 슬라이드처럼 어두운 배경 위에서는 아래 톤만 사용한다.
| 용도 | HEX |
|---|---|
| 타이틀 | `#FFFFFF` |
| 서브카피(부제) | `#B9D9D2` |
| 라벨/로고/캡션 | `#7FCBBE` (Mint) |

## 적용 규칙 (색_팔레트.pdf 06p 원문)
- 계열 순서는 **Cosolus Teal → Sea Teal → Mint → Gray**, 자사행은 Deep Pine으로 강조한다. 3계열 이상이면 Moss를 추가한다.
- 데이터만 딤 틸(Deep Pine/Cosolus Teal) → Mint → Gray. 자사만 캠버로 강조한다.
- 그리드선은 `#E1E7E5` 1px만 사용한다.
- 본문 배경 그라디언트 금지 — **그라디언트는 표지/섹션 간지에서만** 사용한다.
- AVOID: 나뭇잎·지구 아이콘 아이콘 남용, 형광 초록, 3D 차트, 다중 폰트 혼용. 그라디언트는 표지/간지에서만 씀.

---

# 02. 타이포그래피

**Pretendard × IBM Plex** 조합.
- **Pretendard** (한글 기본 서체, weight 400·600·700) — 제목/소제목/본문
- **IBM Plex** (영문·숫자 전용, weight 400·600) — 데이터 수치, 라벨, 코드형 트래킹 텍스트
- 영문 제품명·원소기호·수치 라벨·로고 워드마크는 원본 그대로 쓰고, 본문 폰트로 대체하지 않는다.
- 한글 자소가 균일하고 숫자 폭이 안정적인 고딕. 대체 폰트는 없는 고딕으로 처리한다.

## 타입 스케일 (1920×1080 기준)
| 역할 | 크기/굵기 | 서체 |
|---|---|---|
| SLIDE TITLE | 64px / 700 | Pretendard Bold |
| SUBTITLE | 38px / 600 | Pretendard SemiBold |
| BODY | 30px / 400 | Pretendard Regular |
| DATA | 50px / 600 | IBM Plex SemiBold |
| CAPTION | 20px / 400 | Pretendard/IBM Plex Regular |

## 확장 스케일 (실제 샘플에서 확인된 구조용 크기 — 위 5단계 외 예외)
| 역할 | 크기/굵기 | 서체 | 색상 |
|---|---|---|---|
| 표지 대제목 | 96px / 700 | Pretendard Bold | White |
| 마무리 슬라이드 타이틀 | 76px / 700 | Pretendard Bold | White |
| 헤더 라벨 "0X SECTION" | 20px, 트래킹 확장 | IBM Plex Regular | Gray `#8C9694` |
| 우상단 로고 COSOLUS | 24~30px, 트래킹 확장 | IBM Plex Regular | Primary(라이트) / White(다크) |
| 카드/표 캡션형 라벨 (CARD 0X, KPI 0X, TABLE A 등) | 20px, 트래킹 확장 | IBM Plex Regular | 계열 컬러 |
| 페이지 번호 | 20px | IBM Plex Regular | Gray `#8C9694` (다크 배경은 `#B9D9D2`) |
| md힌트 뱃지 텍스트 | 20px | IBM Plex Regular | Slate `#5A6A68` |

> ⚠️ **폰트 파일 필요**: 현재 샘플 pptx는 시스템 미탑재 문제로 Pretendard 자리에 `Arial`을, IBM Plex 자리에 `Courier New`를 임시로 넣어 export했다. 실제 산출물에서 원 서체를 쓰려면 **Pretendard(400/600/700)**, **IBM Plex Sans + IBM Plex Mono(400/600)** 폰트 파일(OTF/TTF)이 필요하다.

---

# 03. 레이아웃 그리드 규칙

- 좌우 여백 **112px**, 상단 헤더 바 두께 **12px**(Cosolus Teal 단색, 콘텐츠 슬라이드 전용).
- 본문 텍스트는 **최소 24px**(캡션 20px는 예외적으로 허용), 줄바꿈 기준 폭 1400px 이내 유지 — 한 슬라이드 한 메시지 원칙.
- 카드/표는 **라운드 없이 직각**, 그림자 대신 **1px 라인**(`#E1E7E5`) 또는 상단 4px 컬러 스트립으로 구분한다.
- 표지에서만 언더바 액센트(Flame Amber, 120×4px)를 제목 아래 배치한다. 콘텐츠 슬라이드 타이틀에는 밑줄 액센트를 넣지 않는다.

## 공통 헤더 (콘텐츠 슬라이드 전 종류 공통, 표지/간지/이미지풀블리드/마무리 제외)
| 요소 | 위치(px) | 크기(px) | 서체/색상 |
|---|---|---|---|
| 상단 바 | (0,0) | 1920×12 | Cosolus Teal 단색 |
| 섹션 라벨 "0X SECTION" | (112,88) | ~180~253×30 | IBM Plex 20px, Gray |
| 로고 COSOLUS | (1657,96) | 166×35 | IBM Plex 24px, Cosolus Teal |
| 슬라이드 타이틀 | (112,150) | 가변×97 | Pretendard Bold 64px, Ink |

## 공통 푸터 (모든 콘텐츠 슬라이드 좌하단 — 실제 서비스본에서는 숨김 처리하는 "md 매핑 힌트" 뱃지)
| 요소 | 위치(px) | 크기(px) | 서체/색상 |
|---|---|---|---|
| 힌트 뱃지 배경 | (112,978) | 가변×46 | Mist 배경 |
| 뱃지 좌측 라인 | (112,978) | 2×46 | Mint |
| 뱃지 텍스트(레이아웃→md 매핑 표기) | (130,988) | 가변×30 | IBM Plex 20px, Slate |
| 페이지 번호 | (1784,998) | 32×30 | IBM Plex 20px, Gray |

---

# 04. 차트 · 표 규칙 (색_팔레트.pdf 09~10p)

- 막대/도넛 차트 계열색은 **Cosolus Teal(자사) → Sea Teal(개선/2위) → Mint 또는 Gray(기존/비교군)** 순.
- 자사 수치는 Bold + Primary 색으로, 비교군/기존 수치는 Slate/Gray로 낮춘다.
- 그리드선/구분선은 `#E1E7E5` 1px만 사용, 그림자 금지.
- 표 헤더 배경: 강조 열(자사) = Deep Pine `#06342F`, 일반 열 = Slate `#5A6A68` 또는 Cosolus Teal `#005B58`(표 좌우 비교 A/B 헤더).
- 강조 셀 배경은 Mist, 강조 텍스트는 Cosolus Teal Bold.

---

# 05. 문서 구성 (14개 페이지 자산 목록)

| 파일 | 슬라이드 유형 | md 트리거 |
|---|---|---|
| 01_cover.md | 표지 | 문서 최상단 H1 1개 |
| 02_contents.md | 목차 | 순서 있는 리스트 6항목 |
| 03_section-divider.md | 섹션 간지 | H1(#) — 새 섹션 시작 |
| 04_body-1col.md | 본문 1단 | H2 제목 + 문단 + 불릿 |
| 05_body-2col.md | 본문 2단 | `---` 구분선으로 좌우 분리 |
| 06_cards-3col.md | 카드 3분할 | H3 3개 나란히 |
| 07_chart-insight.md | 차트+인사이트 | 표 데이터 + `>` 인용문 |
| 08_comparison-table.md | 비교 표 | 파이프 표, 강조열 `**볼드**` |
| 09_table-side-by-side.md | 표 좌우 비교 | 표 2개 연속 |
| 10_table-stacked.md | 표 상하 비교 | 표 2개 + 우측 불릿 |
| 11_timeline.md | 타임라인 | 5단계 로드맵 |
| 12_kpi-donut.md | KPI 도넛 | 3개 지표 % |
| 13_image-fullbleed.md | 이미지 풀블리드 | `![](경로)` 단독 문단 |
| 14_closing-contact.md | 마무리/문의 | 문서 마지막 `---` 뒤 연락처 |
