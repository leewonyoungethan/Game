# 앱개발부 · 게임 라이브러리

> 우리가 만든 게임, 지금 바로 플레이.

앱개발부에서 만든 게임들을 모아 두는 저장소입니다.

🎮 **바로 플레이:** https://leewonyoungethan.github.io/Game/

`main` 브랜치에 푸시하면 GitHub Actions가 자동으로 사이트를 다시 배포합니다.

## 폴더 구조

```
.
├── index.html          # 게임 목록 페이지 (브라우저로 열면 모든 게임을 볼 수 있어요)
├── games.json          # 게임 목록 데이터
└── games/
    ├── _template/      # 새 게임을 만들 때 복사해서 쓰는 템플릿
    └── <게임-이름>/     # 게임 하나당 폴더 하나
        ├── index.html
        └── README.md
```

## 새 게임 추가하는 방법

1. `games/_template` 폴더를 복사해서 `games/<게임-이름>` 으로 이름을 바꿉니다.
   (폴더 이름은 영어 소문자와 `-` 만 쓰는 걸 추천해요. 예: `space-shooter`)
2. `index.html` 에 게임을 만듭니다.
3. 폴더 안의 `README.md` 에 게임 설명, 조작법, 만든 사람을 적습니다.
4. 정사각형 게임 아이콘(예: 512×512)을 `icons/<게임-이름>.svg` 또는 `.png` 로 넣습니다. 모서리는 사이트에서 둥글게 잘라 줘요. 없으면 기본 아이콘이 나옵니다.
5. 루트의 `games.json` 에 게임 정보를 한 줄 추가합니다.

```json
{ "id": "space-shooter", "title": "스페이스 슈터", "genres": ["슈팅", "액션"], "added": "2026-12-01", "author": "홍길동", "description": "우주에서 운석을 피하는 게임", "icon": "icons/space-shooter.png" }
```

`genres` 는 장르 목록이에요. 사이트 위쪽 장르 버튼이 이 값으로 자동으로 만들어집니다. 새 장르를 적으면 버튼도 새로 생겨요.

`added` 는 추가한 날짜예요. "최신순" 정렬에 쓰여요.

"인기순"은 카드를 누른 횟수로 정렬해요. 횟수는 [counterapi.dev](https://counterapi.dev) 의 `leewonyoungethan-appdevclub` 카운터에 게임 `id` 별로 쌓이고, 같은 브라우저 창에서는 게임마다 한 번만 셉니다. 상위 3개 게임에는 🥇🥈🥉 메달이 붙어요.

```json
```

다른 저장소에 이미 올라가 있는 게임은 `url` 을 넣으면 그 주소로 연결됩니다.

```json
{ "id": "rock", "title": "곡괭이 봉우리", "author": "...", "description": "...", "url": "https://leewonyoungethan.github.io/Rock/" }
```

## 실행하는 방법

`games.json` 을 불러오기 때문에 로컬 서버로 여는 것이 좋습니다.

```bash
python3 -m http.server 8000
```

그다음 브라우저에서 http://localhost:8000 을 열면 됩니다.

## 게임 목록

| 게임 | 만든 사람 | 설명 |
| --- | --- | --- |
| [⛏️ 곡괭이 봉우리](https://leewonyoungethan.github.io/Rock/) ([저장소](https://github.com/leewonyoungethan/Rock)) | leewonyoungethan | 블록 산을 파고 들어가는 1인칭 3D 채굴 게임 |
| [🦊 여우의 달걀 도둑](https://leewonyoungethan.github.io/Rock/eggsteal.html) | leewonyoungethan | 잠든 새들의 알을 몰래 훔쳐 굴로 옮기는 잠입 게임 |
| [🚗 Wander Road](https://leewonyoungethan.github.io/Road/) ([저장소](https://github.com/leewonyoungethan/Road)) | leewonyoungethan | 끝없는 절차적 도로를 달리는 힐링 드라이브 게임 |
| [🚆 Rail Dash](https://claude.ai/artifact/WqVcJh2MKjki5b1KkkMJML) | leewonyoungethan | 기차 선로를 3분 동안 달리는 러닝 게임 |
| [🚨 도둑차 대탈주](https://claude.ai/artifact/Th6Z3xiCuQwJPNAsSmBSsD) | leewonyoungethan | 경찰을 따돌리며 도시를 질주하는 추격전 게임 |
| [🎹 건반 소나기](https://leewonyoungethan.github.io/piano-tiles/) ([저장소](https://github.com/leewonyoungethan/piano-tiles)) | leewonyoungethan | 떨어지는 건반을 눌러 곡을 연주하는 피아노 타일 게임 |
| [👶 나율이 키우기](https://claude.ai/artifact/5rvyqN2jFhFxz9HxUN83CT) | leewonyoungethan | 나율이를 백 살까지 키우는 육성 시뮬레이션 |
| [⚔️ 별빛 기사](https://claude.ai/artifact/VeBfTWMoEv4Ksm5jfUWHRs) | leewonyoungethan | 픽셀 액션 플랫포머 |
| [맑은 하늘](https://claude.ai/artifact/NdVDGjGVbYmHWcLhPuET41) | leewonyoungethan | 9·11 아침을 가상으로 지키는 추모 시뮬레이션 |
| [✈️ F16 스카이 스트라이커](https://mythoflee-aiden.github.io/f16-shooter/) ([저장소](https://github.com/mythoflee-aiden/f16-shooter)) | mythoflee-aiden | F16 전투기 슈팅 게임 |
| [🪐 행성 합치기](https://leewonyoungethan.github.io/Game/games/planet-merge/) (`games/planet-merge/`) | Claude | 같은 행성을 합쳐 태양까지 키우는 물리 퍼즐 |
| [🐸 개구리 연잎 점프](https://leewonyoungethan.github.io/Game/games/lily-hop/) (`games/lily-hop/`) | Claude | 타이밍 맞춰 탭해서 연잎을 건너는 원터치 아케이드 |
| [🌟 별빛 브레이커](https://leewonyoungethan.github.io/Game/games/star-breaker/) (`games/star-breaker/`) | Claude | 밤하늘의 별빛 벽돌을 공으로 깨는 벽돌깨기 |
| [🏝️ 보물섬 탐사](https://leewonyoungethan.github.io/Game/games/treasure-island/) (`games/treasure-island/`) | Claude | 숫자를 단서로 해적 함정을 피해 섬을 파헤치는 지뢰찾기 퍼즐 |
| [🐧 펭귄 창고](https://leewonyoungethan.github.io/Game/games/penguin-warehouse/) (`games/penguin-warehouse/`) | Claude | 꼬마 펭귄이 생선 상자를 얼음 구멍으로 밀어 옮기는 상자 밀기 퍼즐 |
| [🔨 두더지 팡팡](https://leewonyoungethan.github.io/Game/games/whack-mole/) (`games/whack-mole/`) | Claude | 60초 동안 튀어나오는 두더지를 잡는 반응속도 게임 |
| [🍃 기억의 숲](https://leewonyoungethan.github.io/Game/games/memory-forest/) (`games/memory-forest/`) | Claude | 나뭇잎 카드 뒤에 숨은 숲속 친구들의 짝을 찾는 기억력 게임 |
| [🐉 꼬마 용 꼬리잡기](https://leewonyoungethan.github.io/Game/games/dragon-snake/) (`games/dragon-snake/`) | Claude | 과일을 먹을수록 길어지는 꼬마 용의 꼬리잡기 |
| [🎣 고요한 낚시터](https://leewonyoungethan.github.io/Game/games/quiet-pond/) (`games/quiet-pond/`) | Claude | 고양이 낚시꾼과 함께하는 힐링 낚시 |
| [🏙️ 구름 위 블록 탑](https://leewonyoungethan.github.io/Game/games/cloud-tower/) (`games/cloud-tower/`) | Claude | 좌우로 움직이는 블록을 타이밍 맞춰 쌓아 구름 위부터 우주까지 올라가는 탑 쌓기 |
| [🍄 버섯 마을 수비대](https://leewonyoungethan.github.io/Game/games/mushroom-defense/) (`games/mushroom-defense/`) | Claude | 길 옆에 도토리 발사대·꿀벌집·포자포·얼음 버섯을 세워 15번의 해충 공격을 막아내는 타워 디펜스 |
| [🕵️ 낱말 탐정](https://leewonyoungethan.github.io/Game/games/word-detective/) (`games/word-detective/`) | Claude | 글자판에 숨은 한글 낱말을 쭉 그어 찾아내는 12개의 사건 — 판이 커질수록 대각선·거꾸로도 숨어요 |
| [☄️ 유성우 피하기](https://leewonyoungethan.github.io/Game/games/meteor-dodge/) (`games/meteor-dodge/`) | Claude | 쏟아지는 별똥별·조준탄·레이저 사이를 꼬마 우주선으로 누비며 최대한 오래 살아남는 회피 서바이벌 |
