맞아. **이번엔 아까 코드의 숲 배경 + 부드러운 이동을 유지하면서, 메인화면/상점/재화/퀘스트까지 합친 Streamlit 전체 코드**로 줄게.

**`main.py`에 넣을 때 `import streamlit as st`부터 마지막 줄까지 복사해.**
아래 코드 자체에는 실행에 필요한 별도 파일이 없어.

```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

st.markdown("""
<style>
header {visibility:hidden;}
.block-container {
    padding-top:1rem;
    max-width:950px;
}
</style>
""", unsafe_allow_html=True)


GAME = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

<style>

*{
    box-sizing:border-box;
    user-select:none;
    -webkit-user-select:none;
}

html,body{
    margin:0;
    padding:0;
    background:#102615;
    color:white;
    font-family:Arial,"Noto Sans KR",sans-serif;
    overflow:hidden;
}

button{
    font-family:inherit;
    border:0;
    cursor:pointer;
}

#app{
    width:780px;
    height:840px;
    margin:auto;
    position:relative;
    overflow:hidden;
    border-radius:28px;

    background:
        radial-gradient(
            circle at 8% 8%,
            #76a94b 0 7%,
            transparent 18%
        ),
        radial-gradient(
            circle at 90% 12%,
            #497e3b 0 8%,
            transparent 20%
        ),
        radial-gradient(
            circle at 12% 90%,
            #4c8739 0 9%,
            transparent 22%
        ),
        radial-gradient(
            circle at 90% 88%,
            #356b32 0 10%,
            transparent 22%
        ),
        #214d2b;
}

/* 숲 장식 */

.tree{
    position:absolute;
    width:115px;
    height:115px;
    border-radius:50%;

    background:
        radial-gradient(
            circle at 30% 25%,
            #a6df62,
            #5d9d3d 45%,
            #214f29 82%
        );

    box-shadow:
        inset -12px -14px 22px rgba(0,0,0,.3),
        0 10px 18px rgba(0,0,0,.4);
}

.grass{
    position:absolute;
    width:80px;
    height:40px;
    opacity:.6;
}

.grass::before,
.grass::after{
    content:"";
    position:absolute;
    bottom:0;
    width:5px;
    height:35px;
    background:#72a849;
    border-radius:100%;
    transform:rotate(-25deg);
}

.grass::after{
    left:20px;
    transform:rotate(25deg);
}

/* 화면 */

.screen{
    position:absolute;
    inset:0;
    display:none;
}

.screen.active{
    display:block;
}

/* 메인 */

#mainScreen{
    text-align:center;
    padding-top:65px;
}

.logo{
    font-size:64px;
    font-weight:1000;
    letter-spacing:-4px;
    text-shadow:0 5px 0 #17321e;
}

.subtitle{
    color:#b5cdb7;
    font-size:17px;
    margin-top:5px;
}

.mainWorm{
    width:180px;
    height:180px;
    margin:30px auto 15px;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:120px;

    animation:
        floating 1.7s ease-in-out infinite;
}

@keyframes floating{
    0%,100%{
        transform:translateY(0) rotate(-3deg);
    }

    50%{
        transform:translateY(-12px) rotate(3deg);
    }
}

.stats{
    display:flex;
    justify-content:center;
    gap:12px;
    margin:10px 0 30px;
}

.stat{
    background:rgba(0,0,0,.35);
    border:2px solid rgba(255,255,255,.12);
    padding:12px 24px;
    border-radius:14px;
    font-size:18px;
    font-weight:bold;
}

.coin{
    color:#ffd84d;
}

.mainButton{
    width:370px;
    height:62px;
    margin:8px;
    border-radius:15px;
    color:white;
    font-size:21px;
    font-weight:900;
    transition:.15s;
}

.mainButton:hover{
    transform:scale(1.025);
}

.startButton{
    background:#315fc9;
    box-shadow:0 5px 0 #1d3b7e;
}

.shopButton{
    background:#744dc4;
    box-shadow:0 5px 0 #4b3081;
}

/* 상점 */

#shopScreen{
    padding:24px 35px;
}

.topBar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:20px;
}

.backButton{
    background:#354139;
    color:white;
    border-radius:10px;
    padding:11px 18px;
    font-weight:bold;
}

.title{
    font-size:40px;
    font-weight:1000;
}

.shopCoins{
    color:#ffd84d;
    font-size:20px;
    font-weight:900;
}

.section{
    font-size:24px;
    font-weight:900;
    margin:17px 0 10px;
}

.shopGrid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:11px;
}

.shopItem{
    background:rgba(0,0,0,.28);
    border:2px solid rgba(255,255,255,.12);
    border-radius:15px;
    padding:12px;
    text-align:center;
}

.itemEmoji{
    height:65px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:48px;
}

.itemName{
    font-size:15px;
    font-weight:900;
}

.itemPrice{
    color:#ffd84d;
    margin:6px;
    font-weight:bold;
}

.itemButton{
    width:100%;
    height:36px;
    border-radius:8px;
    background:#315fc9;
    color:white;
    font-weight:bold;
}

.itemButton.owned{
    background:#39784b;
}

.itemButton.equipped{
    background:#a87927;
}

/* 게임 */

#gameScreen{
    padding-top:5px;
}

.gameHeader{
    height:62px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 24px;
}

.score{
    font-size:20px;
    font-weight:900;
}

.highScore{
    color:#ffd84d;
    font-size:19px;
    font-weight:900;
}

#gameArea{
    position:relative;
    width:648px;
    height:648px;
    margin:auto;
}

#game{
    position:absolute;
    left:0;
    top:0;

    width:648px;
    height:648px;

    overflow:hidden;

    border:18px solid #254da5;
    border-radius:22px;

    background:
        radial-gradient(
            ellipse at 15% 20%,
            rgba(73,130,48,.75),
            transparent 20%
        ),
        radial-gradient(
            ellipse at 80% 75%,
            rgba(45,105,40,.65),
            transparent 24%
        ),
        radial-gradient(
            ellipse at 40% 60%,
            rgba(104,158,54,.55),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #4d8b35,
            #79ad45 35%,
            #467e32 70%,
            #62963a
        );

    box-shadow:
        inset 0 0 35px rgba(0,0,0,.28),
        0 12px 25px rgba(0,0,0,.45);
}

/* 숲속 바닥 무늬 */

#game::before{
    content:"";
    position:absolute;
    inset:0;
    pointer-events:none;

    background:
        radial-gradient(
            ellipse at 20% 15%,
            rgba(30,90,35,.45) 0 4px,
            transparent 5px
        ),
        radial-gradient(
            ellipse at 70% 30%,
            rgba(25,80,30,.45) 0 5px,
            transparent 6px
        ),
        radial-gradient(
            ellipse at 35% 80%,
            rgba(20,75,30,.5) 0 4px,
            transparent 5px
        ),
        radial-gradient(
            ellipse at 90% 55%,
            rgba(100,160,55,.45) 0 4px,
            transparent 5px
        );

    background-size:
        130px 150px,
        180px 170px,
        155px 180px,
        210px 200px;
}

#scoreBox{
    position:absolute;
    left:14px;
    top:12px;
    z-index:100;

    padding:9px 15px;
    border-radius:13px;

    background:rgba(0,0,0,.75);

    font-weight:bold;
    font-size:18px;
}

#highBox{
    position:absolute;
    right:14px;
    top:12px;
    z-index:100;

    padding:9px 15px;
    border-radius:13px;

    background:rgba(0,0,0,.75);

    color:#ffd84d;
    font-weight:bold;
    font-size:18px;
}

#dashBox{
    position:absolute;
    left:50%;
    top:13px;
    transform:translateX(-50%);
    z-index:110;

    background:rgba(0,0,0,.78);
    padding:8px 15px;
    border-radius:13px;

    font-weight:bold;
    font-size:15px;
}

#dashStatus{
    color:#6eff91;
}

/* 퀘스트 */

#questBox{
    position:absolute;
    right:14px;
    bottom:14px;
    z-index:100;

    width:175px;
    padding:9px 11px;

    background:rgba(0,0,0,.76);
    border:1px solid rgba(255,255,255,.15);

    border-radius:12px;

    font-size:12px;
}

.questTitle{
    color:#ffd84d;
    font-weight:900;
    margin-bottom:4px;
}

.questReward{
    color:#ffd84d;
    margin-top:3px;
}

/* 뱀 */

#snakeSVG{
    position:absolute;
    inset:0;

    width:648px;
    height:648px;

    overflow:visible;
    pointer-events:none;
    z-index:30;
}

#snakeShadow{
    fill:none;
    stroke:#18386f;
    stroke-width:43;
    stroke-linecap:round;
    stroke-linejoin:round;
    opacity:.32;
}

#snakeBody{
    fill:none;
    stroke:#315fc9;
    stroke-width:36;
    stroke-linecap:round;
    stroke-linejoin:round;
}

#snakeLight{
    fill:none;
    stroke:#8aacff;
    stroke-width:6;
    stroke-linecap:round;
    opacity:.5;
}

#headGroup{
    transform-box:fill-box;
    transform-origin:center;
    transition:transform .05s linear;
}

#mouthClosed{
    fill:none;
    stroke:#112c64;
    stroke-width:3;
    stroke-linecap:round;
}

#mouthOpenGroup{
    display:none;
}

#openMouth{
    fill:#111;
    stroke:#071535;
    stroke-width:2;
}

#tongue{
    fill:#ff4b55;
    stroke:#b51f2c;
    stroke-width:1.5;
}

.tooth{
    fill:white;
}

/* 사과 */

#food{
    position:absolute;

    width:34px;
    height:34px;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:30px;

    z-index:40;

    animation:
        applePulse .65s ease-in-out infinite;
}

@keyframes applePulse{
    0%,100%{
        transform:scale(.78);
    }

    50%{
        transform:scale(1.15);
    }
}

/* 질주 */

#dashTrail{
    display:none;

    fill:none;
    stroke:#d9eaff;
    stroke-width:9;
    stroke-linecap:round;
    opacity:.42;
    stroke-dasharray:14 14;
}

.dashing #dashTrail{
    display:block;
    animation:
        trailMove .22s linear infinite;
}

@keyframes trailMove{
    from{
        stroke-dashoffset:0;
    }

    to{
        stroke-dashoffset:-28px;
    }
}

#windLayer{
    display:none;
}

.dashing #windLayer{
    display:block;
}

.wind{
    fill:none;
    stroke:white;
    stroke-width:4;
    stroke-linecap:round;
    opacity:0;
}

.dashing .wind1{
    animation:wind .28s infinite;
}

.dashing .wind2{
    animation:wind .34s infinite .08s;
}

.dashing .wind3{
    animation:wind .4s infinite .14s;
}

@keyframes wind{
    0%{
        opacity:0;
        transform:translateX(25px);
    }

    30%{
        opacity:.85;
    }

    100%{
        opacity:0;
        transform:translateX(-35px);
    }
}

/* 충돌 */

#crash{
    position:absolute;
    display:none;

    font-size:80px;

    z-index:400;

    transform:
        translate(-50%,-50%);

    animation:
        crashPop .5s ease-out;
}

@keyframes crashPop{
    0%{
        transform:
            translate(-50%,-50%)
            scale(.2);
    }

    60%{
        transform:
            translate(-50%,-50%)
            scale(1.25);
    }

    100%{
        transform:
            translate(-50%,-50%)
            scale(1);
    }
}

.shake{
    animation:shake .45s;
}

@keyframes shake{
    0%,100%{
        transform:translate(0,0);
    }

    20%{
        transform:translate(-8px,5px);
    }

    40%{
        transform:translate(8px,-5px);
    }

    60%{
        transform:translate(-6px,3px);
    }

    80%{
        transform:translate(6px,-3px);
    }
}

/* 오버레이 */

.overlay{
    position:absolute;
    inset:0;

    display:none;
    justify-content:center;
    align-items:center;

    z-index:500;

    background:rgba(0,0,0,.84);
}

.overlayCard{
    width:430px;
    padding:38px;

    text-align:center;

    background:#111a13;
    border:2px solid #3e5041;
    border-radius:25px;

    box-shadow:
        0 20px 50px rgba(0,0,0,.6);
}

.overlay h1{
    margin:0 0 28px;
    font-size:65px;
    font-weight:1000;
}

.overlayButton{
    display:block;

    width:280px;
    height:58px;

    margin:11px auto;

    border-radius:13px;

    color:white;

    font-size:20px;
    font-weight:900;
}

.continue{
    background:#315fc9;
}

.restart{
    background:#3d8b51;
}

.home{
    background:#444c45;
}

#gameOverTitle{
    color:#ff4545;
}

/* 알림 */

#notice{
    position:absolute;
    left:50%;
    bottom:20px;

    transform:translateX(-50%);

    z-index:1000;

    display:none;

    padding:12px 20px;

    border-radius:12px;

    background:#152119;
    border:2px solid #47604b;

    font-weight:bold;
}

</style>
</head>

<body>

<div id="app">

    <!-- 숲 장식 -->

    <div class="tree" style="left:-50px;top:-45px;"></div>
    <div class="tree" style="left:130px;top:-65px;"></div>
    <div class="tree" style="left:320px;top:-55px;"></div>
    <div class="tree" style="left:510px;top:-45px;"></div>
    <div class="tree" style="right:-55px;top:190px;"></div>
    <div class="tree" style="left:-55px;top:410px;"></div>
    <div class="tree" style="right:-60px;top:500px;"></div>

    <div class="grass" style="left:20px;top:150px;"></div>
    <div class="grass" style="left:650px;top:130px;"></div>
    <div class="grass" style="left:20px;top:650px;"></div>
    <div class="grass" style="left:650px;top:650px;"></div>


    <!-- ================= MAIN ================= -->

    <section
        id="mainScreen"
        class="screen active">

        <div class="logo">
            🪱 WORM QUEST
        </div>

        <div class="subtitle">
            숲속에서 살아남아라
        </div>

        <div
            class="mainWorm"
            id="mainWorm">
            🪱
        </div>

        <div class="stats">

            <div class="stat">
                🪙
                <span id="mainCoins">
                    0
                </span>
            </div>

            <div class="stat">
                🏆
                <span id="mainHigh">
                    0
                </span>
            </div>

        </div>

        <button
            class="mainButton startButton"
            onclick="startGame()">
            🎮 게임 시작하기
        </button>

        <br>

        <button
            class="mainButton shopButton"
            onclick="openShop()">
            🛒 상점
        </button>

    </section>


    <!-- ================= SHOP ================= -->

    <section
        id="shopScreen"
        class="screen">

        <div class="topBar">

            <button
                class="backButton"
                onclick="showScreen('mainScreen')">
                ← 메인으로
            </button>

            <div class="title">
                🛒 상점
            </div>

            <div class="shopCoins">
                🪙
                <span id="shopCoins">
                    0
                </span>
            </div>

        </div>

        <div class="section">
            🪱 지렁이 외형
        </div>

        <div
            id="wormShop"
            class="shopGrid">
        </div>

        <div class="section">
            ⚡ 스킬 변경
        </div>

        <div
            id="skillShop"
            class="shopGrid">
        </div>

    </section>


    <!-- ================= GAME ================= -->

    <section
        id="gameScreen"
        class="screen">

        <div class="gameHeader">

            <div class="score">
                🍎 점수:
                <span id="headerScore">
                    0
                </span>
                &nbsp;
                🪙
                <span id="gameCoins">
                    0
                </span>
            </div>

            <div class="highScore">
                🏆 최고기록:
                <span id="headerHigh">
                    0
                </span>
            </div>

        </div>


        <div id="gameArea">

            <div id="game">

                <div id="scoreBox">
                    🍎
                    <span id="score">
                        0
                    </span>
                </div>

                <div id="highBox">
                    🏆
                    <span id="highScore">
                        0
                    </span>
                </div>

                <div id="dashBox">
                    ⚡ 질주:
                    <span id="dashStatus">
                        준비
                    </span>
                </div>


                <!-- 작은 퀘스트 -->

                <div id="questBox">

                    <div class="questTitle">
                        📜 QUEST
                    </div>

                    <div id="questText">
                        사과 먹기 0/5
                    </div>

                    <div class="questReward">
                        🪙 보상:
                        <span id="questReward">
                            80
                        </span>
                    </div>

                </div>


                <div id="food">
                    🍎
                </div>


                <svg
                    id="snakeSVG"
                    viewBox="0 0 648 648">

                    <path
                        id="snakeShadow">
                    </path>

                    <path
                        id="snakeBody">
                    </path>

                    <path
                        id="snakeLight">
                    </path>

                    <path
                        id="dashTrail">
                    </path>


                    <!-- 바람 -->

                    <g id="windLayer">

                        <path
                            class="wind wind1"
                            d="M0 -15 Q-35 -25 -65 -15">
                        </path>

                        <path
                            class="wind wind2"
                            d="M0 0 Q-40 -8 -75 3">
                        </path>

                        <path
                            class="wind wind3"
                            d="M0 15 Q-35 24 -65 15">
                        </path>

                    </g>


                    <!-- 머리 -->

                    <g id="headGroup">

                        <ellipse
                            cx="0"
                            cy="5"
                            rx="29"
                            ry="25"
                            fill="#17336e"
                            opacity=".35">
                        </ellipse>


                        <path
                            d="
                            M -18 -21
                            Q 4 -28 21 -15
                            Q 34 0 21 15
                            Q 4 28 -18 21
                            Q -30 11 -30 0
                            Q -30 -11 -18 -21
                            "
                            fill="#315fc9"
                            stroke="#244a9f"
                            stroke-width="3">
                        </path>


                        <!-- 눈 -->

                        <circle
                            cx="4"
                            cy="-18"
                            r="10"
                            fill="white">
                        </circle>

                        <circle
                            cx="4"
                            cy="18"
                            r="10"
                            fill="white">
                        </circle>

                        <circle
                            cx="7"
                            cy="-17"
                            r="4.5"
                            fill="#18234b">
                        </circle>

                        <circle
                            cx="7"
                            cy="17"
                            r="4.5"
                            fill="#18234b">
                        </circle>

                        <circle
                            cx="8"
                            cy="-19"
                            r="1.5"
                            fill="white">
                        </circle>

                        <circle
                            cx="8"
                            cy="15"
                            r="1.5"
                            fill="white">
                        </circle>


                        <!-- 닫힌 입 -->

                        <path
                            id="mouthClosed"
                            d="
                            M16 -5
                            Q23 0 16 5
                            ">
                        </path>


                        <!-- 크게 벌어진 입 -->

                        <g id="mouthOpenGroup">

                            <path
                                id="openMouth"
                                d="
                                M12 -9
                                Q25 -12 29 0
                                Q25 12 12 9
                                Q17 0 12 -9
                                ">
                            </path>

                            <path
                                id="tongue"
                                d="
                                M15 3
                                Q21 0 26 4
                                Q22 12 16 7
                                Z
                                ">
                            </path>

                            <path
                                class="tooth"
                                d="
                                M16 -8
                                L20 -2
                                L23 -8
                                Z
                                ">
                            </path>

                            <path
                                class="tooth"
                                d="
                                M22 -8
                                L25 -2
                                L28 -7
                                Z
                                ">
                            </path>

                        </g>

                    </g>

                </svg>


                <div id="crash">
                    💥
                </div>


                <!-- 일시정지 -->

                <div
                    id="pauseOverlay"
                    class="overlay">

                    <div class="overlayCard">

                        <h1>
                            일시정지
                        </h1>

                        <button
                            class="overlayButton continue"
                            onclick="resumeGame()">
                            ▶️ 계속하기
                        </button>

                        <button
                            class="overlayButton restart"
                            onclick="restart()">
                            🔄 다시하기
                        </button>

                    </div>

                </div>


                <!-- 게임오버 -->

                <div
                    id="gameOver"
                    class="overlay">

                    <div class="overlayCard">

                        <h1 id="gameOverTitle">
                            YOU DIE
                        </h1>

                        <h2>
                            점수:
                            <span id="finalScore">
                                0
                            </span>
                        </h2>

                        <h2>
                            🏆 최고기록:
                            <span id="gameOverHigh">
                                0
                            </span>
                        </h2>

                        <button
                            class="overlayButton restart"
                            onclick="restart()">
                            🔄 다시하기
                        </button>

                        <button
                            class="overlayButton home"
                            onclick="goHome()">
                            🏠 메인으로
                        </button>

                    </div>

                </div>

            </div>

        </div>

    </section>


    <div id="notice"></div>

</div>


<script>

/* =========================================================
   기본 설정
========================================================= */

const GRID = 34;

const COLS = 18;
const ROWS = 18;

const NORMAL_MOVE_TIME = 160;

const DASH_MOVE_TIME = 65;

const DASH_DURATION = 2000;

const DASH_COOLDOWN = 10000;


/* =========================================================
   외형
========================================================= */

const worms = {

    basic:{
        name:"기본 지렁이",
        emoji:"🪱",
        color:"#315fc9",
        price:0
    },

    fire:{
        name:"화염 지렁이",
        emoji:"🔥",
        color:"#e94a32",
        price:500
    },

    lightning:{
        name:"번개 지렁이",
        emoji:"⚡",
        color:"#e7ca36",
        price:1000
    },

    ghost:{
        name:"유령 지렁이",
        emoji:"👻",
        color:"#a879e8",
        price:1500
    },

    rainbow:{
        name:"무지개 지렁이",
        emoji:"🌈",
        color:"#e35db7",
        price:2000
    },

    dragon:{
        name:"용 지렁이",
        emoji:"🐉",
        color:"#df4b45",
        price:2500
    }

};


/* =========================================================
   스킬
========================================================= */

const skills = {

    dash:{
        name:"질주",
        desc:"LShift 홀드",
        price:0,
        speed:65
    },

    turbo:{
        name:"터보 질주",
        desc:"더 빠른 질주",
        price:700,
        speed:50
    },

    wind:{
        name:"윈드 러너",
        desc:"강력한 바람",
        price:1200,
        speed:42
    },

    flash:{
        name:"플래시",
        desc:"최고속 질주",
        price:1800,
        speed:32
    }

};


/* =========================================================
   저장 데이터
========================================================= */

let coins =
    Number(
        localStorage.getItem(
            "wormCoins"
        ) || 0
    );

let highScore =
    Number(
        localStorage.getItem(
            "wormHighScore"
        ) || 0
    );

let equippedWorm =
    localStorage.getItem(
        "wormEquipped"
    ) || "basic";

let equippedSkill =
    localStorage.getItem(
        "wormSkill"
    ) || "dash";


let ownedWorms =
    JSON.parse(
        localStorage.getItem(
            "wormOwned"
        ) || '["basic"]'
    );


let ownedSkills =
    JSON.parse(
        localStorage.getItem(
            "skillOwned"
        ) || '["dash"]'
    );


/* =========================================================
   퀘스트
========================================================= */

const questPool = [

    {
        type:"apple",
        text:"🍎 사과 먹기",
        target:5,
        reward:80
    },

    {
        type:"apple",
        text:"🍎 사과 먹기",
        target:10,
        reward:150
    },

    {
        type:"apple",
        text:"🍎 사과 먹기",
        target:15,
        reward:200
    },

    {
        type:"score",
        text:"🏆 점수 달성",
        target:10,
        reward:100
    },

    {
        type:"score",
        text:"🏆 점수 달성",
        target:20,
        reward:180
    },

    {
        type:"score",
        text:"🏆 점수 달성",
        target:30,
        reward:200
    },

    {
        type:"length",
        text:"🪱 몸 길이 늘리기",
        target:8,
        reward:100
    },

    {
        type:"length",
        text:"🪱 몸 길이 늘리기",
        target:12,
        reward:150
    },

    {
        type:"length",
        text:"🪱 몸 길이 늘리기",
        target:18,
        reward:200
    }

];


let quests =
    JSON.parse(
        localStorage.getItem(
            "wormQuests"
        ) || "null"
    );


function createQuests(){

    quests = [];

    const pool =
        [...questPool];

    for(
        let i=0;
        i<3;
        i++
    ){

        const index =
            Math.floor(
                Math.random() *
                pool.length
            );

        quests.push({
            ...pool[index],
            progress:0
        });

        pool.splice(
            index,
            1
        );

    }

    saveQuests();

}


function saveQuests(){

    localStorage.setItem(
        "wormQuests",
        JSON.stringify(
            quests
        )
    );

}


if(
    !Array.isArray(quests) ||
    quests.length !== 3
){

    createQuests();

}


/* =========================================================
   DOM
========================================================= */

const game =
    document.getElementById(
        "game"
    );

const foodElement =
    document.getElementById(
        "food"
    );

const scoreElement =
    document.getElementById(
        "score"
    );

const highScoreElement =
    document.getElementById(
        "highScore"
    );

const headerScore =
    document.getElementById(
        "headerScore"
    );

const headerHigh =
    document.getElementById(
        "headerHigh"
    );

const gameCoins =
    document.getElementById(
        "gameCoins"
    );

const mainCoins =
    document.getElementById(
        "mainCoins"
    );

const mainHigh =
    document.getElementById(
        "mainHigh"
    );

const shopCoins =
    document.getElementById(
        "shopCoins"
    );

const dashStatus =
    document.getElementById(
        "dashStatus"
    );

const crashElement =
    document.getElementById(
        "crash"
    );

const snakeBody =
    document.getElementById(
        "snakeBody"
    );

const snakeShadow =
    document.getElementById(
        "snakeShadow"
    );

const snakeLight =
    document.getElementById(
        "snakeLight"
    );

const dashTrail =
    document.getElementById(
        "dashTrail"
    );

const headGroup =
    document.getElementById(
        "headGroup"
    );

const mouthClosed =
    document.getElementById(
        "mouthClosed"
    );

const mouthOpenGroup =
    document.getElementById(
        "mouthOpenGroup"
    );


/* =========================================================
   화면
========================================================= */

function showScreen(id){

    document
        .querySelectorAll(
            ".screen"
        )
        .forEach(
            element => {
                element.classList.remove(
                    "active"
                );
            }
        );

    document
        .getElementById(id)
        .classList.add(
            "active"
        );

    updateUI();

}


function openShop(){

    renderShop();

    showScreen(
        "shopScreen"
    );

}


function goHome(){

    gameRunning = false;

    paused = false;

    dashing = false;

    shiftHeld = false;

    stopDash();

    document
        .getElementById(
            "pauseOverlay"
        )
        .style.display = "none";

    document
        .getElementById(
            "gameOver"
        )
        .style.display = "none";

    showScreen(
        "mainScreen"
    );

}


/* =========================================================
   UI
========================================================= */

function updateUI(){

    mainCoins.textContent =
        coins;

    shopCoins.textContent =
        coins;

    gameCoins.textContent =
        coins;

    mainHigh.textContent =
        highScore;

    highScoreElement.textContent =
        highScore;

    headerHigh.textContent =
        highScore;

    document.getElementById(
        "mainWorm"
    ).textContent =
        worms[
            equippedWorm
        ].emoji;

}


function saveData(){

    localStorage.setItem(
        "wormCoins",
        coins
    );

    localStorage.setItem(
        "wormHighScore",
        highScore
    );

    localStorage.setItem(
        "wormEquipped",
        equippedWorm
    );

    localStorage.setItem(
        "wormSkill",
        equippedSkill
    );

    localStorage.setItem(
        "wormOwned",
        JSON.stringify(
            ownedWorms
        )
    );

    localStorage.setItem(
        "skillOwned",
        JSON.stringify(
            ownedSkills
        )
    );

    saveQuests();

    updateUI();

}


/* =========================================================
   상점
========================================================= */

function renderShop(){

    let html = "";

    Object.entries(
        worms
    ).forEach(
        ([id,item]) => {

            const owned =
                ownedWorms.includes(
                    id
                );

            const equipped =
                equippedWorm === id;

            let buttonText =
                equipped
                ? "장착 중"
                : owned
                ? "장착하기"
                : "구매";

            let className =
                equipped
                ? "equipped"
                : owned
                ? "owned"
                : "";

            html += `

                <div class="shopItem">

                    <div
                        class="itemEmoji"
                        style="color:${item.color}">
                        ${item.emoji}
                    </div>

                    <div class="itemName">
                        ${item.name}
                    </div>

                    <div class="itemPrice">
                        ${
                            item.price === 0
                            ? "무료"
                            : "🪙 " + item.price
                        }
                    </div>

                    <button
                        class="itemButton ${className}"
                        onclick="buyWorm('${id}')">
                        ${buttonText}
                    </button>

                </div>

            `;

        }
    );


    document.getElementById(
        "wormShop"
    ).innerHTML = html;


    let skillHTML = "";

    Object.entries(
        skills
    ).forEach(
        ([id,item]) => {

            const owned =
                ownedSkills.includes(
                    id
                );

            const equipped =
                equippedSkill === id;

            let buttonText =
                equipped
                ? "사용 중"
                : owned
                ? "변경하기"
                : "구매";

            let className =
                equipped
                ? "equipped"
                : owned
                ? "owned"
                : "";

            skillHTML += `

                <div class="shopItem">

                    <div class="itemEmoji">
                        ⚡
                    </div>

                    <div class="itemName">
                        ${item.name}
                    </div>

                    <div class="itemPrice">
                        ${
                            item.price === 0
                            ? "무료"
                            : "🪙 " + item.price
                        }
                    </div>

                    <button
                        class="itemButton ${className}"
                        onclick="buySkill('${id}')">
                        ${buttonText}
                    </button>

                </div>

            `;

        }
    );


    document.getElementById(
        "skillShop"
    ).innerHTML =
        skillHTML;

}


function buyWorm(id){

    const item =
        worms[id];


    if(
        ownedWorms.includes(id)
    ){

        equippedWorm =
            id;

        applyWorm();

        saveData();

        notify(
            item.name +
            " 장착!"
        );

        renderShop();

        return;

    }


    if(
        coins < item.price
    ){

        notify(
            "🪙 코인이 부족합니다!"
        );

        return;

    }


    coins -=
        item.price;

    ownedWorms.push(
        id
    );

    equippedWorm =
        id;

    applyWorm();

    saveData();

    notify(
        item.name +
        " 구매 완료!"
    );

    renderShop();

}


function buySkill(id){

    const item =
        skills[id];


    if(
        ownedSkills.includes(id)
    ){

        equippedSkill =
            id;

        saveData();

        notify(
            item.name +
            "으로 변경!"
        );

        renderShop();

        return;

    }


    if(
        coins < item.price
    ){

        notify(
            "🪙 코인이 부족합니다!"
        );

        return;

    }


    coins -=
        item.price;

    ownedSkills.push(
        id
    );

    equippedSkill =
        id;

    saveData();

    notify(
        item.name +
        " 구매 완료!"
    );

    renderShop();

}


function applyWorm(){

    const color =
        worms[
            equippedWorm
        ].color;


    snakeBody.style.stroke =
        color;


    document
        .querySelector(
            "#headGroup > path"
        )
        .style.fill =
        color;

}


/* =========================================================
   알림
========================================================= */

let noticeTimer = null;

function notify(text){

    const element =
        document.getElementById(
            "notice"
        );

    element.textContent =
        text;

    element.style.display =
        "block";

    clearTimeout(
        noticeTimer
    );

    noticeTimer =
        setTimeout(
            () => {
                element.style.display =
                    "none";
            },
            1800
        );

}


/* =========================================================
   게임 변수
========================================================= */

let snake = [];

let previousSnake = [];

let direction = {
    x:1,
    y:0
};

let nextDirection = {
    x:1,
    y:0
};

let food = {
    x:10,
    y:9
};

let score = 0;

let dead = false;

let paused = false;

let gameRunning = false;


/* =========================================================
   질주
========================================================= */

let dashing = false;

let dashEndTime = 0;

let lastDashTime = -Infinity;

let shiftHeld = false;


/* =========================================================
   애니메이션
========================================================= */

let lastMoveTime =
    performance.now();

let animationFrame =
    null;


/* =========================================================
   뱀 초기화
========================================================= */

function resetSnake(){

    snake = [

        {x:8,y:9},
        {x:7,y:9},
        {x:6,y:9},
        {x:5,y:9},
        {x:4,y:9}

    ];


    previousSnake =
        snake.map(
            part => ({
                x:part.x,
                y:part.y
            })
        );

}


/* =========================================================
   사과
========================================================= */

function createFood(){

    let valid =
        false;


    while(!valid){

        food = {

            x:
                Math.floor(
                    Math.random() *
                    COLS
                ),

            y:
                Math.floor(
                    Math.random() *
                    ROWS
                )

        };


        valid =
            !snake.some(
                part =>
                    part.x ===
                        food.x &&
                    part.y ===
                        food.y
            );

    }

}


/* =========================================================
   사과 거리
========================================================= */

function foodDistance(){

    const head =
        snake[0];


    return Math.max(

        Math.abs(
            head.x -
            food.x
        ),

        Math.abs(
            head.y -
            food.y
        )

    );

}


/* =========================================================
   입
========================================================= */

function updateMouth(){

    if(dead){
        return;
    }


    /*
        정확히 2칸 이내면
        확실하게 크게 벌림
    */

    if(
        foodDistance() <= 2
    ){

        mouthClosed.style.display =
            "none";

        mouthOpenGroup.style.display =
            "block";

    }else{

        mouthClosed.style.display =
            "block";

        mouthOpenGroup.style.display =
            "none";

    }

}


/* =========================================================
   보간
========================================================= */

function lerp(
    a,
    b,
    t
){

    return (
        a +
        (b-a)*t
    );

}


function ease(t){

    return t < .5

        ? 2*t*t

        : 1 -
          Math.pow(
              -2*t+2,
              2
          ) / 2;

}


/* =========================================================
   부드러운 지렁이
========================================================= */

function getAnimatedSnake(
    progress
){

    const eased =
        ease(
            Math.max(
                0,
                Math.min(
                    1,
                    progress
                )
            )
        );


    return snake.map(
        (part,index) => {

            const oldPart =
                previousSnake[index] ||
                part;


            return {

                x:
                    lerp(
                        oldPart.x,
                        part.x,
                        eased
                    ),

                y:
                    lerp(
                        oldPart.y,
                        part.y,
                        eased
                    )

            };

        }
    );

}


/* =========================================================
   몸통 경로
========================================================= */

function createPath(
    animatedSnake
){

    const points =
        [...animatedSnake]
        .reverse()
        .map(
            part => ({

                x:
                    part.x *
                    GRID +
                    GRID/2,

                y:
                    part.y *
                    GRID +
                    GRID/2

            })
        );


    if(
        points.length < 2
    ){
        return "";
    }


    let path =
        `M ${points[0].x} ${points[0].y}`;


    for(
        let i=1;
        i<points.length-1;
        i++
    ){

        const a =
            points[i];

        const b =
            points[i+1];


        const midX =
            (a.x+b.x)/2;

        const midY =
            (a.y+b.y)/2;


        path +=
            ` Q ${a.x} ${a.y} ${midX} ${midY}`;

    }


    const last =
        points[
            points.length-1
        ];


    path +=
        ` L ${last.x} ${last.y}`;


    return path;

}


/* =========================================================
   머리 방향
========================================================= */

function getAngle(){

    if(
        direction.x === 1
    ){
        return 0;
    }

    if(
        direction.y === 1
    ){
        return 90;
    }

    if(
        direction.x === -1
    ){
        return 180;
    }

    if(
        direction.y === -1
    ){
        return -90;
    }

    return 0;

}


/* =========================================================
   렌더링
========================================================= */

function render(
    progress=1
){

    const animatedSnake =
        getAnimatedSnake(
            progress
        );


    const path =
        createPath(
            animatedSnake
        );


    snakeBody.setAttribute(
        "d",
        path
    );

    snakeShadow.setAttribute(
        "d",
        path
    );

    snakeLight.setAttribute(
        "d",
        path
    );

    dashTrail.setAttribute(
        "d",
        path
    );


    const head =
        animatedSnake[0];


    const x =
        head.x *
        GRID +
        GRID/2;

    const y =
        head.y *
        GRID +
        GRID/2;


    headGroup.setAttribute(
        "transform",
        `
        translate(
            ${x}
            ${y}
        )
        rotate(
            ${getAngle()}
        )
        `
    );


    foodElement.style.left =
        food.x *
        GRID +
        "px";

    foodElement.style.top =
        food.y *
        GRID +
        "px";


    scoreElement.textContent =
        score;

    headerScore.textContent =
        score;


    updateMouth();

}


/* =========================================================
   이동 속도
========================================================= */

function getMoveTime(){

    if(
        dashing
    ){

        return skills[
            equippedSkill
        ].speed;

    }

    return NORMAL_MOVE_TIME;

}


/* =========================================================
   이동
========================================================= */

function move(){

    if(
        dead ||
        paused ||
        !gameRunning
    ){
        return;
    }


    direction =
        {
            ...nextDirection
        };


    const head =
        snake[0];


    const newHead = {

        x:
            head.x +
            direction.x,

        y:
            head.y +
            direction.y

    };


    if(
        newHead.x < 0 ||
        newHead.x >= COLS ||
        newHead.y < 0 ||
        newHead.y >= ROWS
    ){

        crash(
            head
        );

        return;

    }


    if(
        snake.some(
            part =>
                part.x ===
                    newHead.x &&
                part.y ===
                    newHead.y
        )
    ){

        crash(
            newHead
        );

        return;

    }


    previousSnake =
        snake.map(
            part => ({
                x:part.x,
                y:part.y
            })
        );


    snake.unshift(
        newHead
    );


    if(
        newHead.x === food.x &&
        newHead.y === food.y
    ){

        score++;

        if(
            score >
            highScore
        ){

            highScore =
                score;

            localStorage.setItem(
                "wormHighScore",
                highScore
            );

        }


        createFood();

        updateQuestProgress();

    }else{

        snake.pop();

    }


    lastMoveTime =
        performance.now();


    render(0);

}


/* =========================================================
   애니메이션 루프
========================================================= */

function animate(
    time
){

    if(
        dead ||
        paused ||
        !gameRunning
    ){

        return;

    }


    if(
        dashing &&
        time >= dashEndTime
    ){

        stopDash();

    }


    const moveTime =
        getMoveTime();


    const progress =
        Math.min(
            (
                time -
                lastMoveTime
            ) /
            moveTime,
            1
        );


    render(
        progress
    );


    updateDashUI();


    animationFrame =
        requestAnimationFrame(
            animate
        );

}


/* =========================================================
   질주 시작
========================================================= */

function startDash(){

    if(
        dead ||
        paused ||
        dashing ||
        !gameRunning
    ){
        return;
    }


    const now =
        performance.now();


    if(
        now -
        lastDashTime <
        DASH_COOLDOWN
    ){

        return;

    }


    dashing = true;

    lastDashTime =
        now;

    dashEndTime =
        now +
        DASH_DURATION;


    game.classList.add(
        "dashing"
    );


    lastMoveTime =
        now;


    updateDashUI();

}


/* =========================================================
   질주 종료
========================================================= */

function stopDash(){

    dashing = false;

    game.classList.remove(
        "dashing"
    );

    updateDashUI();

}


/* =========================================================
   질주 UI
========================================================= */

function updateDashUI(){

    const now =
        performance.now();


    if(
        dashing
    ){

        const remaining =
            Math.max(
                0,
                dashEndTime -
                now
            );


        dashStatus.textContent =
            "🔥 " +
            (
                remaining/1000
            ).toFixed(1) +
            "초";

        dashStatus.style.color =
            "#ffd84d";

        return;

    }


    const elapsed =
        now -
        lastDashTime;


    if(
        lastDashTime ===
            -Infinity ||
        elapsed >=
            DASH_COOLDOWN
    ){

        dashStatus.textContent =
            "준비";

        dashStatus.style.color =
            "#6eff91";

    }else{

        const remaining =
            Math.ceil(
                (
                    DASH_COOLDOWN -
                    elapsed
                ) / 1000
            );


        dashStatus.textContent =
            "쿨타임 " +
            remaining +
            "초";

        dashStatus.style.color =
            "#ff7777";

    }

}


/* =========================================================
   충돌
========================================================= */

function crash(
    position
){

    dead = true;

    gameRunning = false;

    stopDash();


    mouthClosed.style.display =
        "block";

    mouthOpenGroup.style.display =
        "none";


    crashElement.style.left =
        position.x *
        GRID +
        GRID/2 +
        "px";

    crashElement.style.top =
        position.y *
        GRID +
        GRID/2 +
        "px";


    crashElement.style.display =
        "block";


    game.classList.add(
        "shake"
    );


    if(
        score >
        highScore
    ){

        highScore =
            score;

        localStorage.setItem(
            "wormHighScore",
            highScore
        );

    }


    setTimeout(
        () => {

            game.classList.remove(
                "shake"
            );

            document.getElementById(
                "finalScore"
            ).textContent =
                score;

            document.getElementById(
                "gameOverHigh"
            ).textContent =
                highScore;

            document.getElementById(
                "gameOver"
            ).style.display =
                "flex";

            updateUI();

        },
        500
    );

}


/* =========================================================
   시작
========================================================= */

function startGame(){

    showScreen(
        "gameScreen"
    );


    score = 0;

    dead = false;

    paused = false;

    gameRunning = true;

    dashing = false;

    shiftHeld = false;

    lastDashTime =
        -Infinity;


    direction = {
        x:1,
        y:0
    };

    nextDirection = {
        x:1,
        y:0
    };


    document.getElementById(
        "pauseOverlay"
    ).style.display =
        "none";


    document.getElementById(
        "gameOver"
    ).style.display =
        "none";


    crashElement.style.display =
        "none";


    resetSnake();

    createFood();


    lastMoveTime =
        performance.now();


    applyWorm();

    updateQuestUI();

    render(1);

    updateDashUI();


    if(
        animationFrame
    ){

        cancelAnimationFrame(
            animationFrame
        );

    }


    animationFrame =
        requestAnimationFrame(
            animate
        );

}


/* =========================================================
   다시하기
========================================================= */

function restart(){

    startGame();

}


/* =========================================================
   일시정지
========================================================= */

function pauseGame(){

    if(
        dead ||
        paused ||
        !gameRunning
    ){

        return;

    }


    paused = true;


    if(
        animationFrame
    ){

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame =
            null;

    }


    document.getElementById(
        "pauseOverlay"
    ).style.display =
        "flex";

}


/* =========================================================
   계속하기
========================================================= */

function resumeGame(){

    if(
        dead
    ){

        return;

    }


    paused = false;


    document.getElementById(
        "pauseOverlay"
    ).style.display =
        "none";


    lastMoveTime =
        performance.now();


    animationFrame =
        requestAnimationFrame(
            animate
        );

}


/* =========================================================
   퀘스트
========================================================= */

function updateQuestProgress(){

    quests.forEach(
        quest => {

            if(
                quest.type ===
                    "apple"
            ){

                quest.progress =
                    score;

            }

            if(
                quest.type ===
                    "score"
            ){

                quest.progress =
                    score;

            }

            if(
                quest.type ===
                    "length"
            ){

                quest.progress =
                    snake.length;

            }

        }
    );


    checkQuestCompletion();

    updateQuestUI();

    saveQuests();

}


function checkQuestCompletion(){

    for(
        let i=0;
        i<quests.length;
        i++
    ){

        const quest =
            quests[i];


        if(
            quest.progress >=
            quest.target
        ){

            const reward =
                Math.min(
                    quest.reward,
                    200
                );


            coins +=
                reward;


            notify(
                "🎉 퀘스트 완료! +" +
                reward +
                " 🪙"
            );


            /*
                완료된 퀘스트 하나만
                새 퀘스트로 교체
            */

            let available =
                questPool.filter(
                    candidate =>
                        !quests.some(
                            current =>
                                current.type ===
                                    candidate.type &&
                                current.target ===
                                    candidate.target
                        )
                );


            if(
                available.length === 0
            ){

                available =
                    [...questPool];

            }


            const replacement =
                available[
                    Math.floor(
                        Math.random() *
                        available.length
                    )
                ];


            quests[i] = {

                ...replacement,

                progress:0

            };


            saveData();

            break;

        }

    }

}


function updateQuestUI(){

    if(
        !quests ||
        quests.length === 0
    ){

        return;

    }


    let quest =
        quests[0];


    for(
        let i=0;
        i<quests.length;
        i++
    ){

        if(
            quests[i].progress <
            quests[i].target
        ){

            quest =
                quests[i];

            break;

        }

    }


    document.getElementById(
        "questText"
    ).textContent =
        quest.text +
        " " +
        Math.min(
            quest.progress,
            quest.target
        ) +
        "/" +
        quest.target;


    document.getElementById(
        "questReward"
    ).textContent =
        Math.min(
            quest.reward,
            200
        );

}


/* =========================================================
   키보드
========================================================= */

document.addEventListener(
    "keydown",
    function(e){

        const key =
            e.key.toLowerCase();


        /* ESC */

        if(
            e.code ===
            "Escape"
        ){

            e.preventDefault();


            if(
                document
                    .getElementById(
                        "gameScreen"
                    )
                    .classList.contains(
                        "active"
                    )
            ){

                if(
                    paused
                ){

                    resumeGame();

                }else{

                    pauseGame();

                }

            }

            return;

        }


        /* LSHIFT */

        if(
            e.code ===
            "ShiftLeft"
        ){

            e.preventDefault();


            if(
                !shiftHeld
            ){

                shiftHeld =
                    true;

                startDash();

            }

            return;

        }


        if(
            !gameRunning ||
            paused ||
            dead
        ){

            return;

        }


        /* WASD / 방향키 */

        if(
            (
                key === "w" ||
                key === "arrowup"
            ) &&
            direction.y !== 1
        ){

            nextDirection = {
                x:0,
                y:-1
            };

        }


        if(
            (
                key === "s" ||
                key === "arrowdown"
            ) &&
            direction.y !== -1
        ){

            nextDirection = {
                x:0,
                y:1
            };

        }


        if(
            (
                key === "a" ||
                key === "arrowleft"
            ) &&
            direction.x !== 1
        ){

            nextDirection = {
                x:-1,
                y:0
            };

        }


        if(
            (
                key === "d" ||
                key === "arrowright"
            ) &&
            direction.x !== -1
        ){

            nextDirection = {
                x:1,
                y:0
            };

        }

    }
);


/* =========================================================
   SHIFT 떼기
========================================================= */

document.addEventListener(
    "keyup",
    function(e){

        if(
            e.code ===
            "ShiftLeft"
        ){

            shiftHeld =
                false;


            /*
                Shift를 떼는 순간
                질주 즉시 종료
            */

            if(
                dashing
            ){

                stopDash();

            }

        }

    }
);


/* =========================================================
   창 밖으로 나갔을 때
========================================================= */

window.addEventListener(
    "blur",
    function(){

        shiftHeld =
            false;


        if(
            dashing
        ){

            stopDash();

        }

    }
);


/* =========================================================
   초기화
========================================================= */

updateUI();

renderShop();

applyWorm();

</script>

</body>
</html>
"""


components.html(
    GAME,
    height=870,
    scrolling=False
)
```
