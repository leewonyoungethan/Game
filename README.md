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
| [✉️ Letter Rush](https://leewonyoungethan.github.io/subway-surfers/) | leewonyoungethan | 우편 기관차에서 쏟아진 초대장을 3분 안에 모아 축제 광장까지 달리는 3D 러닝 게임 |
| [🚨 도둑차 대탈주](https://leewonyoungethan.github.io/chase/) | leewonyoungethan | 경찰을 따돌리며 도시를 질주하는 추격전 게임 |
| [🎹 건반 소나기](https://leewonyoungethan.github.io/piano-tiles/) ([저장소](https://github.com/leewonyoungethan/piano-tiles)) | leewonyoungethan | 떨어지는 건반을 눌러 곡을 연주하는 피아노 타일 게임 |
| [⚔️ 별빛 기사](https://leewonyoungethan.github.io/knight/) | leewonyoungethan | 픽셀 액션 플랫포머 |
| [✈️ F16 스카이 스트라이커](https://mythoflee-aiden.github.io/f16-shooter/) ([저장소](https://github.com/mythoflee-aiden/f16-shooter)) | mythoflee-aiden | F16 전투기 슈팅 게임 |
| [🧬 몬스터 합치기](https://leewonyoungethan.github.io/combining/) | leewonyoungethan | 섬을 꾸미고 11가지 속성의 몬스터를 교배·부화시켜 키운 뒤 턴제 전투를 벌이는 몬스터 육성 RPG |
| [✊ 결전의 가위바위보](https://leewonyoungethan.github.io/RSP/) | leewonyoungethan | 3D 손으로 겨루는 긴장감 넘치는 가위바위보 · 묵찌빠 · 참참참 — 내 버릇을 읽는 '검은 장갑'과 친구 온라인 대전 |
| [🏰 디펜스 게임](https://leewonyoungethan.github.io/defence-game/) | leewonyoungethan | 풀밭에 20가지 타워를 세우고 업그레이드해 100 웨이브를 막아내는 타워 디펜스 — 5웨이브마다 👑 보스 등장 |
| [🎰 NOT-GAMBLING](https://raw.githack.com/leewonyoungethan/not-gambling/main/index.html) | leewonyoungethan | 플레이머니로만 즐기는 카지노 시뮬레이터 — 룰렛·블랙잭·바카라·홀덤 등 9가지 게임으로 규칙과 하우스 에지를 체험해요 (실제 돈 거래 없음) |
