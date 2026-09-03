import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 WORM QUEST",
    page_icon="🪱",
    layout="centered"
)

st.markdown("""
<style>
header {visibility:hidden;}
footer {visibility:hidden;}

.block-container {
    padding-top: 10px;
    padding-bottom: 0;
    max-width: 1000px;
}

body {
    background: #111;
}
</style>
""", unsafe_allow_html=True)


components.html(r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>

* {
    box-sizing: border-box;
    user-select: none;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 900px;
    background: #14251a;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

#page {
    width: 900px;
    margin: 0 auto;
    position: relative;
}

/* =====================================================
   TOP BAR
===================================================== */

#topbar {
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 5px 10px;
}

.stat {
    background: rgba(0,0,0,.82);
    color: white;
    border-radius: 15px;
    padding: 12px 18px;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 5px 15px rgba(0,0,0,.3);
}

#coinTop {
    color: #ffd84d;
}

#highTop {
    color: #fff;
}

/* =====================================================
   GAME
===================================================== */

#game {
    width: 648px;
    height: 648px;
    margin: 5px auto 0;
    position: relative;
    overflow: hidden;

    border: 18px solid #234da3;
    border-radius: 22px;

    background:
        linear-gradient(
            90deg,
            rgba(0,0,0,.06) 1px,
            transparent 1px
        ),
        linear-gradient(
            rgba(0,0,0,.06) 1px,
            transparent 1px
        ),
        #9dcc4a;

    background-size: 34px 34px;

    box-shadow:
        inset 0 0 35px rgba(0,0,0,.25),
        0 12px 30px rgba(0,0,0,.5);

    outline: none;
}

/* =====================================================
   SCORE
===================================================== */

#scoreBox {
    position: absolute;
    top: 15px;
    left: 15px;

    z-index: 200;

    padding: 9px 15px;
    border-radius: 13px;

    background: rgba(0,0,0,.78);
    color: white;

    font-size: 18px;
    font-weight: bold;
}

#skillBox {
    position: absolute;
    top: 15px;
    right: 15px;

    z-index: 200;

    padding: 9px 15px;
    border-radius: 13px;

    background: rgba(0,0,0,.78);
    color: white;

    font-size: 16px;
    font-weight: bold;
}

/* =====================================================
   APPLE
===================================================== */

#food {
    position: absolute;

    width: 34px;
    height: 34px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 30px;

    z-index: 60;

    animation:
        applePulse 1s infinite ease-in-out;

    transform-origin: center;
}

@keyframes applePulse {
    0% {
        transform: scale(.78);
    }

    50% {
        transform: scale(1.12);
    }

    100% {
        transform: scale(.78);
    }
}

/* =====================================================
   SNAKE SVG
===================================================== */

#snakeSVG {
    position: absolute;
    left: 0;
    top: 0;

    width: 648px;
    height: 648px;

    overflow: visible;

    pointer-events: none;

    z-index: 40;
}

#snakeShadow {
    fill: none;
    stroke: #172a60;
    stroke-width: 43;
    stroke-linecap: round;
    stroke-linejoin: round;
    opacity: .35;
}

#snakeBody {
    fill: none;
    stroke-width: 36;
    stroke-linecap: round;
    stroke-linejoin: round;
}

#snakeLight {
    fill: none;
    stroke-width: 6;
    stroke-linecap: round;
    opacity: .45;
}

#dashTrail {
    display: none;

    fill: none;
    stroke-width: 9;
    stroke-linecap: round;

    stroke-dasharray: 15 15;
    opacity: .42;
}

.dashing #dashTrail {
    display: block;

    animation:
        trailMove .22s linear infinite;
}

@keyframes trailMove {
    from {
        stroke-dashoffset: 0;
    }

    to {
        stroke-dashoffset: -30;
    }
}

/* =====================================================
   HEAD
===================================================== */

#headGroup {
    transition: transform .03s linear;
}

#mouthClosed {
    stroke: #101e4c;
    stroke-width: 3;
    fill: none;
    stroke-linecap: round;
}

#mouthOpenGroup {
    display: none;
}

#openMouth {
    fill: #111;
    stroke: #081535;
    stroke-width: 2;
}

#tongue {
    fill: #ff4c62;
    stroke: #a92335;
    stroke-width: 1.5;
}

.tooth {
    fill: white;
}

/* =====================================================
   WIND
===================================================== */

#windLayer {
    display: none;
}

.dashActive #windLayer {
    display: block;
}

.wind {
    fill: none;
    stroke: white;
    stroke-width: 4;
    stroke-linecap: round;
    opacity: 0;
}

.dashActive .wind1 {
    animation: wind .28s infinite;
}

.dashActive .wind2 {
    animation: wind .36s infinite .06s;
}

.dashActive .wind3 {
    animation: wind .32s infinite .12s;
}

.dashActive .wind4 {
    animation: wind .4s infinite .17s;
}

@keyframes wind {
    0% {
        opacity: 0;
        transform: translateX(20px) scaleX(.4);
    }

    35% {
        opacity: .85;
    }

    100% {
        opacity: 0;
        transform: translateX(-40px) scaleX(1.4);
    }
}

/* =====================================================
   EXPLOSION
===================================================== */

#crash {
    display: none;

    position: absolute;

    font-size: 78px;

    z-index: 400;

    transform:
        translate(-50%,-50%);

    animation:
        crashPop .45s ease-out;
}

@keyframes crashPop {
    0% {
        transform:
            translate(-50%,-50%)
            scale(.2)
            rotate(-20deg);
    }

    60% {
        transform:
            translate(-50%,-50%)
            scale(1.3)
            rotate(8deg);
    }

    100% {
        transform:
            translate(-50%,-50%)
            scale(1)
            rotate(0deg);
    }
}

/* =====================================================
   OVERLAY
===================================================== */

.overlay {
    display: none;

    position: absolute;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%,-50%);

    width: 450px;

    padding: 35px 25px;

    border-radius: 25px;

    background: rgba(0,0,0,.94);

    color: white;

    text-align: center;

    z-index: 700;

    box-shadow:
        0 15px 45px rgba(0,0,0,.55);
}

.overlay h1 {
    margin: 0 0 28px;

    font-size: 62px;
    font-weight: 900;
}

.menuButton {
    width: 280px;
    height: 60px;

    margin: 9px auto;

    border: none;
    border-radius: 15px;

    font-size: 22px;
    font-weight: bold;

    cursor: pointer;

    color: white;
}

.menuButton:hover {
    transform: scale(1.04);
}

#continueButton {
    background: #4c89ff;
}

#restartButton,
#gameOverRestart {
    background: #43b96a;
}

#gameOver h1 {
    color: #ff4141;
}

/* =====================================================
   QUEST PANEL
===================================================== */

#questPanel {
    position: absolute;

    left: 15px;
    top: 150px;

    width: 205px;

    z-index: 250;

    background: rgba(0,0,0,.83);

    color: white;

    border-radius: 17px;

    padding: 15px;

    box-shadow:
        0 8px 20px rgba(0,0,0,.35);
}

#questTitle {
    font-size: 20px;
    font-weight: 900;

    margin-bottom: 12px;

    color: #ffd84d;
}

.quest {
    border-top: 1px solid rgba(255,255,255,.15);

    padding: 10px 0;
}

.questName {
    font-size: 14px;
    font-weight: bold;
}

.questProgress {
    font-size: 12px;
    color: #cfcfcf;

    margin-top: 4px;
}

.questReward {
    font-size: 12px;
    color: #ffd84d;

    margin-top: 3px;
}

/* =====================================================
   SHOP BUTTON
===================================================== */

#shopButton {
    position: absolute;

    right: 15px;
    top: 150px;

    z-index: 250;

    width: 160px;
    height: 55px;

    border: none;
    border-radius: 16px;

    background: rgba(0,0,0,.86);

    color: white;

    font-size: 19px;
    font-weight: bold;

    cursor: pointer;
}

#shopButton:hover {
    transform: scale(1.04);
}

/* =====================================================
   SHOP
===================================================== */

#shopOverlay {
    display: none;

    position: fixed;

    inset: 0;

    z-index: 1000;

    background: rgba(0,0,0,.75);
}

#shop {
    position: absolute;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%,-50%);

    width: 750px;
    max-height: 800px;

    overflow-y: auto;

    background: #18201a;

    color: white;

    border-radius: 25px;

    padding: 25px;

    box-shadow:
        0 20px 60px rgba(0,0,0,.7);
}

#shopHeader {
    display: flex;

    justify-content: space-between;
    align-items: center;

    margin-bottom: 20px;
}

#shopHeader h1 {
    margin: 0;

    font-size: 36px;
}

#shopCoins {
    color: #ffd84d;

    font-size: 20px;
    font-weight: bold;
}

#closeShop {
    position: absolute;

    right: 18px;
    top: 15px;

    border: none;

    background: transparent;

    color: white;

    font-size: 28px;

    cursor: pointer;
}

#shopItems {
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 15px;
}

.shopItem {
    background: #263329;

    border-radius: 18px;

    padding: 18px;

    text-align: center;

    border: 2px solid transparent;
}

.shopItem.equipped {
    border-color: #ffd84d;
}

.preview {
    height: 95px;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 55px;
}

.itemName {
    font-size: 20px;

    font-weight: bold;
}

.skillName {
    color: #8fc5ff;

    margin-top: 5px;
}

.price {
    color: #ffd84d;

    margin: 8px;
}

.shopAction {
    width: 140px;

    height: 42px;

    border: none;

    border-radius: 11px;

    background: #4d8cff;

    color: white;

    font-weight: bold;

    cursor: pointer;
}

/* =====================================================
   QUEST COMPLETE
===================================================== */

#questComplete {
    display: none;

    position: fixed;

    left: 50%;
    top: 18%;

    transform:
        translateX(-50%);

    z-index: 1500;

    padding: 18px 30px;

    border-radius: 18px;

    background: rgba(0,0,0,.93);

    color: #ffd84d;

    font-size: 24px;

    font-weight: 900;

    box-shadow:
        0 10px 35px rgba(0,0,0,.5);

    animation:
        questPop .45s ease-out;
}

@keyframes questPop {
    0% {
        transform:
            translateX(-50%)
            scale(.5);
    }

    70% {
        transform:
            translateX(-50%)
            scale(1.1);
    }

    100% {
        transform:
            translateX(-50%)
            scale(1);
    }
}

/* =====================================================
   SKILL FLASH
===================================================== */

#skillFlash {
    display: none;

    position: absolute;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%,-50%);

    z-index: 350;

    color: white;

    font-size: 35px;

    font-weight: 900;

    text-shadow:
        0 3px 10px black;
}

</style>
</head>

<body>

<div id="page">

    <div id="topbar">

        <div class="stat">
            🏆 최고기록
            <span id="highScore">0</span>
        </div>

        <div class="stat" id="coinTop">
            🪙
            <span id="coins">0</span>
        </div>

    </div>


    <div id="game" tabindex="0">

        <div id="scoreBox">
            점수:
            <span id="score">0</span>
        </div>


        <div id="skillBox">
            ⚡
            <span id="skillNameTop">질주</span>
            <br>
            <small id="skillStatus">준비</small>
        </div>


        <div id="food">🍎</div>


        <svg id="snakeSVG"
             viewBox="0 0 648 648">

            <path id="snakeShadow"></path>

            <path id="snakeBody"></path>

            <path id="snakeLight"></path>

            <path id="dashTrail"></path>


            <g id="windLayer">

                <path
                    class="wind wind1"
                    d="M 0 -12 Q -30 -20 -60 -12">
                </path>

                <path
                    class="wind wind2"
                    d="M 0 0 Q -40 -6 -70 5">
                </path>

                <path
                    class="wind wind3"
                    d="M 0 12 Q -30 20 -60 14">
                </path>

                <path
                    class="wind wind4"
                    d="M -5 22 Q -35 30 -55 25">
                </path>

            </g>


            <g id="headGroup">

                <ellipse
                    cx="0"
                    cy="4"
                    rx="28"
                    ry="24"
                    fill="#14274e"
                    opacity=".35">
                </ellipse>


                <path
                    id="headShape"
                    d="
                    M -18 -21
                    Q 4 -28 21 -15
                    Q 34 0 21 15
                    Q 4 28 -18 21
                    Q -30 11 -30 0
                    Q -30 -11 -18 -21
                    "
                    stroke-width="3">
                </path>


                <path
                    id="headHighlight"
                    d="
                    M -17 -17
                    Q -2 -23 10 -15
                    "
                    fill="none"
                    stroke-width="6"
                    stroke-linecap="round"
                    opacity=".5">
                </path>


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
                    id="eye1"
                    cx="7"
                    cy="-17"
                    r="4.5">
                </circle>

                <circle
                    id="eye2"
                    cx="7"
                    cy="17"
                    r="4.5">
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


                <path
                    id="mouthClosed"
                    d="M 16 -5 Q 23 0 16 5">
                </path>


                <g id="mouthOpenGroup">

                    <path
                        id="openMouth"
                        d="
                        M 12 -8
                        Q 25 -10 28 0
                        Q 25 10 12 8
                        Q 17 0 12 -8
                        ">
                    </path>

                    <path
                        id="tongue"
                        d="
                        M 16 3
                        Q 21 0 25 3
                        Q 21 10 16 6
                        Z">
                    </path>

                    <path
                        class="tooth"
                        d="M16 -7 L19 -2 L22 -7 Z">
                    </path>

                    <path
                        class="tooth"
                        d="M22 -7 L25 -2 L27 -6 Z">
                    </path>

                    <path
                        class="tooth"
                        d="M17 7 L20 3 L22 8 Z">
                    </path>

                </g>

            </g>

        </svg>


        <div id="crash">💥</div>


        <div id="skillFlash"></div>


        <!-- QUEST -->

        <div id="questPanel">

            <div id="questTitle">
                📜 QUEST
            </div>

            <div id="quest0" class="quest"></div>
            <div id="quest1" class="quest"></div>
            <div id="quest2" class="quest"></div>

        </div>


        <button id="shopButton">
            🛒 상점
        </button>


        <!-- PAUSE -->

        <div id="pauseOverlay"
             class="overlay">

            <h1>일시정지</h1>

            <button
                id="continueButton"
                class="menuButton">
                ▶️ 계속하기
            </button>

            <button
                id="restartButton"
                class="menuButton">
                🔄 다시하기
            </button>

        </div>


        <!-- GAME OVER -->

        <div id="gameOver"
             class="overlay">

            <h1>YOU DIE</h1>

            <h2>
                점수:
                <span id="finalScore">0</span>
            </h2>

            <h2>
                🪙 획득 코인:
                <span id="earnedCoins">0</span>
            </h2>

            <h2>
                👑 최고기록:
                <span id="gameOverHigh">0</span>
            </h2>

            <button
                id="gameOverRestart"
                class="menuButton">
                🔄 다시하기
            </button>

            <p>
                R 키를 눌러 다시 시작
            </p>

        </div>

    </div>


    <!-- SHOP -->

    <div id="shopOverlay">

        <div id="shop">

            <button id="closeShop">
                ✕
            </button>

            <div id="shopHeader">

                <h1>
                    🛒 지렁이 상점
                </h1>

                <div id="shopCoins">
                    🪙
                    <span id="shopCoinValue">0</span>
                </div>

            </div>

            <div id="shopItems"></div>

        </div>

    </div>

</div>


<div id="questComplete">
    🎉 QUEST COMPLETE!
</div>


<script>

/* =====================================================
   기본 설정
===================================================== */

const GRID = 34;
const COLS = 18;
const ROWS = 18;

const NORMAL_SPEED = 160;


/* =====================================================
   지렁이 종류
===================================================== */

const worms = {

    basic: {

        name: "기본 지렁이",

        price: 0,

        skill: "기본 질주",

        color: "#315fc9",

        light: "#739cff",

        head: "#315fc9",

        skillType: "dash",

        duration: 2000,

        cooldown: 10000,

        speed: 65,

        emoji: "🪱"
    },


    fire: {

        name: "🔥 화염 지렁이",

        price: 500,

        skill: "화염질주",

        color: "#e34b32",

        light: "#ff9d45",

        head: "#e34b32",

        skillType: "fire",

        duration: 2500,

        cooldown: 9000,

        speed: 55,

        emoji: "🔥"
    },


    lightning: {

        name: "⚡ 번개 지렁이",

        price: 1000,

        skill: "번개질주",

        color: "#704ee8",

        light: "#fff45a",

        head: "#704ee8",

        skillType: "lightning",

        duration: 1300,

        cooldown: 8000,

        speed: 38,

        emoji: "⚡"
    },


    ghost: {

        name: "👻 유령 지렁이",

        price: 2000,

        skill: "유령화",

        color: "#dce9ff",

        light: "#ffffff",

        head: "#b9d5ff",

        skillType: "ghost",

        duration: 3000,

        cooldown: 12000,

        speed: 72,

        emoji: "👻"
    },


    rainbow: {

        name: "🌈 무지개 지렁이",

        price: 3000,

        skill: "무지개질주",

        color: "#ff55bb",

        light: "#fff",

        head: "#ff55bb",

        skillType: "rainbow",

        duration: 2200,

        cooldown: 10000,

        speed: 60,

        emoji: "🌈"
    }

};


/* =====================================================
   퀘스트 종류
===================================================== */

const questPool = [

    {
        type: "apples",
        name: "🍎 사과 먹기",
        target: 5,
        reward: 80
    },

    {
        type: "apples",
        name: "🍎 사과 많이 먹기",
        target: 10,
        reward: 150
    },

    {
        type: "score",
        name: "🏆 점수 달성",
        target: 10,
        reward: 100
    },

    {
        type: "score",
        name: "🏆 고득점 도전",
        target: 20,
        reward: 200
    },

    {
        type: "dash",
        name: "⚡ 스킬 사용",
        target: 3,
        reward: 80
    },

    {
        type: "dash",
        name: "⚡ 스킬 마스터",
        target: 7,
        reward: 180
    },

    {
        type: "distance",
        name: "🪱 이동하기",
        target: 50,
        reward: 70
    },

    {
        type: "distance",
        name: "🪱 장거리 이동",
        target: 150,
        reward: 160
    }

];


/* =====================================================
   저장 데이터
===================================================== */

let coins =
    Number(
        localStorage.getItem("wormCoins") || 0
    );


let highScore =
    Number(
        localStorage.getItem("wormHighScore") || 0
    );


let owned =
    JSON.parse(
        localStorage.getItem(
            "wormOwned"
        ) || '["basic"]'
    );


let equipped =
    localStorage.getItem(
        "wormEquipped"
    ) || "basic";


let questData =
    JSON.parse(
        localStorage.getItem(
            "wormQuests"
        ) || "null"
    );


/* =====================================================
   퀘스트 생성
===================================================== */

function makeQuest() {

    const available =
        questPool.filter(
            q =>
                !questData.some(
                    old =>
                        old.type === q.type &&
                        old.target === q.target
                )
        );


    const source =
        available.length
        ? available
        : questPool;


    const q =
        source[
            Math.floor(
                Math.random() *
                source.length
            )
        ];


    return {

        type: q.type,

        name: q.name,

        target: q.target,

        reward:
            Math.min(
                q.reward,
                200
            ),

        progress: 0

    };
}


if (
    !questData ||
    !Array.isArray(questData) ||
    questData.length !== 3
) {

    questData = [
        makeQuest(),
        makeQuest(),
        makeQuest()
    ];

    saveQuests();
}


/* =====================================================
   저장
===================================================== */

function saveAll() {

    localStorage.setItem(
        "wormCoins",
        coins
    );

    localStorage.setItem(
        "wormHighScore",
        highScore
    );

    localStorage.setItem(
        "wormOwned",
        JSON.stringify(owned)
    );

    localStorage.setItem(
        "wormEquipped",
        equipped
    );

    saveQuests();
}


function saveQuests() {

    localStorage.setItem(
        "wormQuests",
        JSON.stringify(
            questData
        )
    );
}


/* =====================================================
   DOM
===================================================== */

const game =
    document.getElementById("game");

const scoreEl =
    document.getElementById("score");

const highEl =
    document.getElementById("highScore");

const coinsEl =
    document.getElementById("coins");

const shopCoinsEl =
    document.getElementById(
        "shopCoinValue"
    );

const foodEl =
    document.getElementById("food");

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

const headShape =
    document.getElementById(
        "headShape"
    );

const headHighlight =
    document.getElementById(
        "headHighlight"
    );

const eye1 =
    document.getElementById("eye1");

const eye2 =
    document.getElementById("eye2");

const mouthClosed =
    document.getElementById(
        "mouthClosed"
    );

const mouthOpenGroup =
    document.getElementById(
        "mouthOpenGroup"
    );

const crash =
    document.getElementById("crash");

const pauseOverlay =
    document.getElementById(
        "pauseOverlay"
    );

const gameOver =
    document.getElementById(
        "gameOver"
    );

const shopOverlay =
    document.getElementById(
        "shopOverlay"
    );

const shopItems =
    document.getElementById(
        "shopItems"
    );

const questComplete =
    document.getElementById(
        "questComplete"
    );

const skillNameTop =
    document.getElementById(
        "skillNameTop"
    );

const skillStatus =
    document.getElementById(
        "skillStatus"
    );

const skillFlash =
    document.getElementById(
        "skillFlash"
    );


/* =====================================================
   게임 변수
===================================================== */

let snake = [];

let previousSnake = [];

let direction = {
    x: 1,
    y: 0
};

let nextDirection = {
    x: 1,
    y: 0
};

let food = {
    x: 10,
    y: 9
};

let score = 0;

let dead = false;

let paused = false;

let shiftHeld = false;

let dashing = false;

let dashEnd = 0;

let lastSkill = -Infinity;

let lastMove = performance.now();

let animationFrame = null;

let distance = 0;

let apples = 0;

let skillUses = 0;


/* =====================================================
   현재 지렁이
===================================================== */

function worm() {
    return worms[equipped];
}


/* =====================================================
   외형 적용
===================================================== */

function applyWormAppearance() {

    const w = worm();

    snakeBody.style.stroke =
        w.color;

    snakeLight.style.stroke =
        w.light;

    snakeShadow.style.stroke =
        "#172a60";

    headShape.style.fill =
        w.head;

    headShape.style.stroke =
        w.color;

    headHighlight.style.stroke =
        w.light;

    eye1.setAttribute(
        "fill",
        "#17213d"
    );

    eye2.setAttribute(
        "fill",
        "#17213d"
    );

    skillNameTop.textContent =
        w.skill;

    if (w.skillType === "ghost") {

        snakeBody.style.opacity =
            ".65";

        snakeLight.style.opacity =
            ".7";

    } else {

        snakeBody.style.opacity =
            "1";

        snakeLight.style.opacity =
            ".45";
    }
}


/* =====================================================
   초기화
===================================================== */

function resetSnake() {

    snake = [
        {x: 8, y: 9},
        {x: 7, y: 9},
        {x: 6, y: 9},
        {x: 5, y: 9},
        {x: 4, y: 9}
    ];

    previousSnake =
        snake.map(
            p => ({
                x: p.x,
                y: p.y
            })
        );
}


/* =====================================================
   사과 생성
===================================================== */

function createFood() {

    let valid = false;

    while (!valid) {

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
                p =>
                    p.x === food.x &&
                    p.y === food.y
            );
    }
}


/* =====================================================
   거리
===================================================== */

function foodDistance() {

    return Math.max(

        Math.abs(
            snake[0].x -
            food.x
        ),

        Math.abs(
            snake[0].y -
            food.y
        )

    );
}


/* =====================================================
   입
===================================================== */

function updateMouth() {

    if (
        !dead &&
        foodDistance() <= 2
    ) {

        mouthClosed.style.display =
            "none";

        mouthOpenGroup.style.display =
            "block";

    } else {

        mouthClosed.style.display =
            "block";

        mouthOpenGroup.style.display =
            "none";
    }
}


/* =====================================================
   보간
===================================================== */

function lerp(a, b, t) {

    return a + (b - a) * t;
}


function animatedSnake(progress) {

    return snake.map(
        (part, i) => {

            const old =
                previousSnake[i] ||
                part;

            return {

                x:
                    lerp(
                        old.x,
                        part.x,
                        progress
                    ),

                y:
                    lerp(
                        old.y,
                        part.y,
                        progress
                    )
            };
        }
    );
}


/* =====================================================
   부드러운 몸통
===================================================== */

function makePath(parts) {

    const points =
        [...parts]
        .reverse()
        .map(
            p => ({
                x:
                    p.x * GRID +
                    GRID / 2,

                y:
                    p.y * GRID +
                    GRID / 2
            })
        );


    if (points.length < 2) {
        return "";
    }


    let path =
        `M ${points[0].x} ${points[0].y}`;


    for (
        let i = 1;
        i < points.length - 1;
        i++
    ) {

        const a = points[i];

        const b = points[i + 1];

        const mx =
            (a.x + b.x) / 2;

        const my =
            (a.y + b.y) / 2;


        path +=
            ` Q ${a.x} ${a.y} ${mx} ${my}`;
    }


    const last =
        points[points.length - 1];


    path +=
        ` L ${last.x} ${last.y}`;


    return path;
}


/* =====================================================
   방향 각도
===================================================== */

function angle() {

    if (direction.x === 1)
        return 0;

    if (direction.y === 1)
        return 90;

    if (direction.x === -1)
        return 180;

    return -90;
}


/* =====================================================
   렌더
===================================================== */

function render(progress = 1) {

    const parts =
        animatedSnake(
            progress
        );

    const path =
        makePath(parts);


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
        parts[0];


    const hx =
        head.x * GRID +
        GRID / 2;

    const hy =
        head.y * GRID +
        GRID / 2;


    headGroup.setAttribute(
        "transform",
        `translate(${hx} ${hy}) rotate(${angle()})`
    );


    foodEl.style.left =
        food.x * GRID + "px";

    foodEl.style.top =
        food.y * GRID + "px";


    scoreEl.textContent =
        score;

    highEl.textContent =
        highScore;

    coinsEl.textContent =
        coins;

    shopCoinsEl.textContent =
        coins;


    updateMouth();

    renderQuests();
}


/* =====================================================
   이동속도
===================================================== */

function moveTime() {

    if (!dashing) {
        return NORMAL_SPEED;
    }

    return worm().speed;
}


/* =====================================================
   애니메이션
===================================================== */

function animate(time) {

    if (
        dead ||
        paused
    ) {
        return;
    }


    if (
        dashing &&
        time >= dashEnd
    ) {

        stopSkill();
    }


    const progress =
        Math.min(
            (
                time -
                lastMove
            ) /
            moveTime(),
            1
        );


    const eased =
        progress < .5

        ? 2 * progress * progress

        : 1 -
          Math.pow(
              -2 * progress + 2,
              2
          ) / 2;


    render(eased);


    updateSkillUI();


    animationFrame =
        requestAnimationFrame(
            animate
        );
}


/* =====================================================
   이동
===================================================== */

function move() {

    if (
        dead ||
        paused
    ) {
        return;
    }


    direction =
        nextDirection;


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


    /* 유령 스킬은 벽 통과 */

    if (
        worm().skillType === "ghost" &&
        dashing
    ) {

        if (
            newHead.x < 0
        )
            newHead.x =
                COLS - 1;

        if (
            newHead.x >= COLS
        )
            newHead.x = 0;

        if (
            newHead.y < 0
        )
            newHead.y =
                ROWS - 1;

        if (
            newHead.y >= ROWS
        )
            newHead.y = 0;

    } else {

        if (
            newHead.x < 0 ||
            newHead.x >= COLS ||
            newHead.y < 0 ||
            newHead.y >= ROWS
        ) {

            crashGame(
                newHead
            );

            return;
        }
    }


    /* 몸 충돌 */

    if (
        snake.some(
            p =>
                p.x === newHead.x &&
                p.y === newHead.y
        )
    ) {

        crashGame(
            newHead
        );

        return;
    }


    previousSnake =
        snake.map(
            p => ({
                x: p.x,
                y: p.y
            })
        );


    snake.unshift(
        newHead
    );


    distance++;


    if (
        newHead.x === food.x &&
        newHead.y === food.y
    ) {

        score++;

        apples++;

        coins += 10;


        if (score > highScore) {

            highScore =
                score;

            localStorage.setItem(
                "wormHighScore",
                highScore
            );
        }


        createFood();

        checkQuests();

    } else {

        snake.pop();
    }


    lastMove =
        performance.now();


    saveAll();

    render(0);
}


/* =====================================================
   스킬 시작
===================================================== */

function startSkill() {

    if (
        dead ||
        paused ||
        dashing
    ) {
        return;
    }


    const now =
        performance.now();

    const w =
        worm();


    if (
        now - lastSkill <
        w.cooldown
    ) {
        return;
    }


    dashing = true;

    shiftHeld = true;

    lastSkill = now;

    dashEnd =
        now + w.duration;

    skillUses++;


    game.classList.add(
        "dashing"
    );

    game.classList.add(
        "dashActive"
    );


    showSkillName();


    checkQuests();


    lastMove =
        now;

    updateSkillUI();
}


/* =====================================================
   스킬 종료
===================================================== */

function stopSkill() {

    dashing = false;


    game.classList.remove(
        "dashing"
    );

    game.classList.remove(
        "dashActive"
    );


    lastMove =
        performance.now();


    updateSkillUI();
}


/* =====================================================
   스킬 이름
===================================================== */

function showSkillName() {

    const w =
        worm();

    skillFlash.textContent =
        w.emoji + " " +
        w.skill;

    skillFlash.style.display =
        "block";


    setTimeout(
        () => {

            skillFlash.style.display =
                "none";

        },
        500
    );
}


/* =====================================================
   스킬 UI
===================================================== */

function updateSkillUI() {

    const w =
        worm();

    const now =
        performance.now();


    if (dashing) {

        const left =
            Math.max(
                0,
                dashEnd - now
            );


        skillStatus.textContent =
            "🔥 " +
            (
                left / 1000
            ).toFixed(1) +
            "초";

        skillStatus.style.color =
            "#ffcf4d";

        return;
    }


    const left =
        w.cooldown -
        (now - lastSkill);


    if (
        lastSkill === -Infinity ||
        left <= 0
    ) {

        skillStatus.textContent =
            "READY ⚡";

        skillStatus.style.color =
            "#6cff91";

    } else {

        skillStatus.textContent =
            "쿨타임 " +
            Math.ceil(
                left / 1000
            ) +
            "초";

        skillStatus.style.color =
            "#ff7272";
    }
}


/* =====================================================
   충돌
===================================================== */

function crashGame(pos) {

    dead = true;

    stopSkill();


    crash.style.left =
        pos.x * GRID +
        GRID / 2 +
        "px";

    crash.style.top =
        pos.y * GRID +
        GRID / 2 +
        "px";

    crash.style.display =
        "block";


    setTimeout(
        () => {

            document.getElementById(
                "finalScore"
            ).textContent =
                score;

            document.getElementById(
                "earnedCoins"
            ).textContent =
                apples * 10;

            document.getElementById(
                "gameOverHigh"
            ).textContent =
                highScore;

            gameOver.style.display =
                "block";

        },
        450
    );
}


/* =====================================================
   일시정지
===================================================== */

function pauseGame() {

    if (
        dead ||
        paused
    ) {
        return;
    }


    render(
        Math.min(
            (
                performance.now() -
                lastMove
            ) /
            moveTime(),
            1
        )
    );


    paused = true;


    pauseOverlay.style.display =
        "block";


    if (animationFrame) {

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame = null;
    }
}


/* =====================================================
   계속하기
===================================================== */

function resumeGame() {

    if (dead) {
        return;
    }


    paused = false;


    pauseOverlay.style.display =
        "none";


    lastMove =
        performance.now();


    animationFrame =
        requestAnimationFrame(
            animate
        );
}


/* =====================================================
   다시하기
===================================================== */

function restart() {

    score = 0;

    apples = 0;

    distance = 0;

    skillUses = 0;

    dead = false;

    paused = false;

    dashing = false;

    shiftHeld = false;

    lastSkill = -Infinity;


    direction = {
        x: 1,
        y: 0
    };

    nextDirection = {
        x: 1,
        y: 0
    };


    gameOver.style.display =
        "none";

    pauseOverlay.style.display =
        "none";

    crash.style.display =
        "none";


    game.classList.remove(
        "dashing"
    );

    game.classList.remove(
        "dashActive"
    );


    resetSnake();

    createFood();

    applyWormAppearance();


    lastMove =
        performance.now();


    render(1);


    if (animationFrame) {

        cancelAnimationFrame(
            animationFrame
        );
    }


    animationFrame =
        requestAnimationFrame(
            animate
        );
}


/* =====================================================
   퀘스트 UI
===================================================== */

function renderQuests() {

    questData.forEach(
        (q, i) => {

            const el =
                document.getElementById(
                    "quest" + i
                );


            el.innerHTML = `

                <div class="questName">
                    ${q.name}
                </div>

                <div class="questProgress">
                    ${Math.min(
                        q.progress,
                        q.target
                    )}
                    / ${q.target}
                </div>

                <div class="questReward">
                    🪙 ${q.reward}
                </div>

            `;
        }
    );
}


/* =====================================================
   퀘스트 진행
===================================================== */

function checkQuests() {

    questData.forEach(
        (q, i) => {

            if (
                q.type === "apples"
            ) {

                q.progress =
                    apples;

            }

            else if (
                q.type === "score"
            ) {

                q.progress =
                    score;

            }

            else if (
                q.type === "dash"
            ) {

                q.progress =
                    skillUses;

            }

            else if (
                q.type === "distance"
            ) {

                q.progress =
                    distance;

            }


            if (
                q.progress >=
                q.target
            ) {

                completeQuest(i);
            }

        }
    );


    saveAll();

    renderQuests();
}


/* =====================================================
   퀘스트 완료
===================================================== */

function completeQuest(index) {

    const completed =
        questData[index];


    coins +=
        Math.min(
            completed.reward,
            200
        );


    questComplete.textContent =
        "🎉 QUEST COMPLETE! +" +
        completed.reward +
        " 🪙";


    questComplete.style.display =
        "block";


    setTimeout(
        () => {

            questComplete.style.display =
                "none";

        },
        1600
    );


    /*
       완료한 퀘스트를
       새로운 퀘스트로 교체
    */

    questData[index] =
        makeQuest();


    saveAll();

    renderQuests();
}


/* =====================================================
   상점
===================================================== */

function openShop() {

    paused = true;

    if (animationFrame) {

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame = null;
    }


    renderShop();


    shopOverlay.style.display =
        "block";
}


function closeShop() {

    shopOverlay.style.display =
        "none";


    if (!dead) {

        paused = false;

        lastMove =
            performance.now();

        animationFrame =
            requestAnimationFrame(
                animate
            );
    }
}


/* =====================================================
   상점 렌더링
===================================================== */

function renderShop() {

    shopItems.innerHTML = "";


    Object.entries(worms)
    .forEach(
        ([id, w]) => {

            const isOwned =
                owned.includes(id);

            const isEquipped =
                equipped === id;


            let buttonText;


            if (isEquipped) {

                buttonText =
                    "✅ 장착 중";

            }

            else if (isOwned) {

                buttonText =
                    "⚡ 장착";

            }

            else {

                buttonText =
                    "🪙 " +
                    w.price +
                    " 구매";
            }


            const card =
                document.createElement(
                    "div"
                );


            card.className =
                "shopItem" +
                (
                    isEquipped
                    ? " equipped"
                    : ""
                );


            card.innerHTML = `

                <div class="preview">
                    ${w.emoji}
                </div>

                <div class="itemName">
                    ${w.name}
                </div>

                <div class="skillName">
                    ⚡ ${w.skill}
                </div>

                <div class="price">
                    ${
                        w.price === 0
                        ? "무료"
                        : "🪙 " + w.price
                    }
                </div>

                <button
                    class="shopAction">
                    ${buttonText}
                </button>

            `;


            const button =
                card.querySelector(
                    ".shopAction"
                );


            button.addEventListener(
                "click",
                () => {

                    if (
                        isEquipped
                    ) {
                        return;
                    }


                    if (
                        isOwned
                    ) {

                        equipped =
                            id;

                        saveAll();

                        applyWormAppearance();

                        renderShop();

                        return;
                    }


                    if (
                        coins <
                        w.price
                    ) {

                        button.textContent =
                            "🪙 코인 부족!";

                        setTimeout(
                            () => {
                                renderShop();
                            },
                            800
                        );

                        return;
                    }


                    coins -=
                        w.price;

                    owned.push(id);

                    equipped =
                        id;


                    saveAll();

                    applyWormAppearance();

                    renderShop();

                    render();

                }
            );


            shopItems.appendChild(
                card
            );

        }
    );
}


/* =====================================================
   버튼
===================================================== */

document
.getElementById(
    "continueButton"
)
.addEventListener(
    "click",
    resumeGame
);


document
.getElementById(
    "restartButton"
)
.addEventListener(
    "click",
    restart
);


document
.getElementById(
    "gameOverRestart"
)
.addEventListener(
    "click",
    restart
);


document
.getElementById(
    "shopButton"
)
.addEventListener(
    "click",
    openShop
);


document
.getElementById(
    "closeShop"
)
.addEventListener(
    "click",
    closeShop
);


/* =====================================================
   키보드
===================================================== */

document.addEventListener(
    "keydown",
    function(e) {

        const key =
            e.key.toLowerCase();


        /* LSHIFT */

        if (
            e.code ===
            "ShiftLeft"
        ) {

            e.preventDefault();


            if (!shiftHeld) {

                shiftHeld = true;

                startSkill();
            }


            return;
        }


        /* ESC */

        if (
            e.code ===
            "Escape"
        ) {

            e.preventDefault();


            if (
                shopOverlay.style.display ===
                "block"
            ) {

                closeShop();

                return;
            }


            if (dead) {
                return;
            }


            if (paused) {

                resumeGame();

            } else {

                pauseGame();
            }


            return;
        }


        /* R */

        if (
            key === "r" &&
            dead
        ) {

            restart();

            return;
        }


        if (
            paused ||
            dead
        ) {
            return;
        }


        /* W / UP */

        if (
            (
                key === "w" ||
                key === "arrowup"
            ) &&
            direction.y !== 1
        ) {

            nextDirection = {
                x: 0,
                y: -1
            };
        }


        /* S / DOWN */

        if (
            (
                key === "s" ||
                key === "arrowdown"
            ) &&
            direction.y !== -1
        ) {

            nextDirection = {
                x: 0,
                y: 1
            };
        }


        /* A / LEFT */

        if (
            (
                key === "a" ||
                key === "arrowleft"
            ) &&
            direction.x !== 1
        ) {

            nextDirection = {
                x: -1,
                y: 0
            };
        }


        /* D / RIGHT */

        if (
            (
                key === "d" ||
                key === "arrowright"
            ) &&
            direction.x !== -1
        ) {

            nextDirection = {
                x: 1,
                y: 0
            };
        }

    }
);


/* =====================================================
   SHIFT 떼기
===================================================== */

document.addEventListener(
    "keyup",
    function(e) {

        if (
            e.code ===
            "ShiftLeft"
        ) {

            shiftHeld = false;


            /*
               핵심:
               Shift를 떼는 즉시
               스킬 종료
            */

            if (dashing) {

                stopSkill();
            }
        }

    }
);


/* =====================================================
   브라우저에서 포커스 잃었을 때
===================================================== */

window.addEventListener(
    "blur",
    function() {

        shiftHeld = false;


        if (dashing) {

            stopSkill();
        }

    }
);


/* =====================================================
   이동 루프
===================================================== */

setInterval(
    () => {

        if (
            dead ||
            paused
        ) {
            return;
        }


        const now =
            performance.now();


        if (
            now - lastMove >=
            moveTime()
        ) {

            move();
        }

    },
    12
);


/* =====================================================
   시작
===================================================== */

applyWormAppearance();

resetSnake();

createFood();

render(1);

renderQuests();

updateSkillUI();


animationFrame =
    requestAnimationFrame(
        animate
    );


/*
   iframe에 키 입력을 확실히 전달
*/

game.focus();

</script>

</body>
</html>
""", height=950)
