```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="WORM QUEST",
    page_icon="🪱",
    layout="centered"
)

components.html(r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>
*{
    box-sizing:border-box;
    user-select:none;
}

html,body{
    margin:0;
    padding:0;
    width:100%;
    min-height:950px;
    background:#101810;
    font-family:Arial,sans-serif;
    overflow:hidden;
}

button{
    font-family:Arial,sans-serif;
    cursor:pointer;
}

/* =========================
   공통
========================= */

.screen{
    width:900px;
    min-height:900px;
    margin:auto;
    position:relative;
}

/* =========================
   메인 화면
========================= */

#mainScreen{
    display:flex;
    flex-direction:column;
    align-items:center;
    padding-top:80px;
}

.logo{
    font-size:90px;
    margin-bottom:5px;
}

.title{
    color:white;
    font-size:65px;
    font-weight:900;
    letter-spacing:4px;
    text-shadow:0 5px 15px #000;
}

.subtitle{
    color:#9eb69e;
    font-size:18px;
    margin-top:8px;
    margin-bottom:55px;
}

.mainStats{
    display:flex;
    gap:15px;
    margin-bottom:35px;
}

.mainStat{
    background:#1c281e;
    border:1px solid #344737;
    color:white;
    border-radius:15px;
    padding:14px 28px;
    font-size:19px;
    font-weight:bold;
}

.mainStat.coin{
    color:#ffd84d;
}

.mainButton{
    width:390px;
    height:70px;
    margin:9px;
    border:none;
    border-radius:18px;
    font-size:25px;
    font-weight:900;
    color:white;
    box-shadow:0 8px 18px rgba(0,0,0,.3);
    transition:.15s;
}

.mainButton:hover{
    transform:scale(1.04);
}

.startButton{
    background:#3979e8;
}

.shopMainButton{
    background:#a45ae8;
}

.wormPreview{
    margin-top:55px;
    font-size:75px;
    animation:float 1.8s infinite ease-in-out;
}

@keyframes float{
    0%,100%{transform:translateY(0);}
    50%{transform:translateY(-12px);}
}


/* =========================
   상점 화면
========================= */

#shopScreen{
    display:none;
    padding:35px 45px;
}

.shopTop{
    display:flex;
    align-items:center;
    justify-content:space-between;
    color:white;
    margin-bottom:25px;
}

.shopTitle{
    font-size:42px;
    font-weight:900;
}

.shopMoney{
    color:#ffd84d;
    font-size:22px;
    font-weight:bold;
}

.backButton{
    border:none;
    border-radius:12px;
    background:#303c32;
    color:white;
    padding:12px 20px;
    font-size:17px;
    font-weight:bold;
}

.shopGrid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:18px;
}

.shopCard{
    background:#1b261d;
    border:2px solid #2d3d30;
    border-radius:20px;
    padding:22px;
    text-align:center;
    color:white;
}

.shopCard.equipped{
    border-color:#ffd84d;
}

.shopEmoji{
    height:95px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:62px;
}

.shopName{
    font-size:22px;
    font-weight:900;
}

.shopSkill{
    margin-top:7px;
    color:#7eb5ff;
    font-weight:bold;
}

.shopPrice{
    margin:10px;
    color:#ffd84d;
    font-weight:bold;
}

.shopAction{
    width:150px;
    height:43px;
    border:none;
    border-radius:11px;
    background:#4c83e8;
    color:white;
    font-weight:bold;
    font-size:15px;
}


/* =========================
   게임 화면
========================= */

#gameScreen{
    display:none;
    padding-top:10px;
}

.gameTop{
    height:65px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 30px;
}

.gameStat{
    background:rgba(0,0,0,.8);
    color:white;
    border-radius:13px;
    padding:11px 18px;
    font-size:17px;
    font-weight:bold;
}

.gameCoin{
    color:#ffd84d;
}


/* 게임판 */

#game{
    width:648px;
    height:648px;
    margin:5px auto;
    position:relative;
    overflow:hidden;

    border:17px solid #214ba0;
    border-radius:22px;

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

    background-size:34px 34px;

    box-shadow:
        inset 0 0 35px rgba(0,0,0,.25),
        0 12px 30px rgba(0,0,0,.5);

    outline:none;
}


/* 점수 */

#scoreBox{
    position:absolute;
    top:12px;
    left:12px;
    z-index:200;

    padding:8px 13px;
    border-radius:11px;

    background:rgba(0,0,0,.8);
    color:white;

    font-size:17px;
    font-weight:bold;
}


/* 스킬 */

#skillBox{
    position:absolute;
    top:12px;
    right:12px;
    z-index:200;

    padding:7px 12px;
    border-radius:11px;

    background:rgba(0,0,0,.8);
    color:white;

    text-align:right;
    font-size:14px;
    font-weight:bold;
}


/* =========================
   작은 퀘스트
========================= */

#questMini{
    position:absolute;
    top:72px;
    right:12px;

    z-index:200;

    width:170px;

    padding:9px 11px;

    background:rgba(0,0,0,.76);
    border-radius:12px;

    color:white;
}

.questMiniTitle{
    color:#ffd84d;
    font-size:13px;
    font-weight:900;
    margin-bottom:5px;
}

.miniQuest{
    font-size:10px;
    padding:4px 0;
    border-top:1px solid rgba(255,255,255,.1);
}

.miniQuestReward{
    color:#ffd84d;
    font-size:9px;
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

    z-index:60;

    animation:applePulse 1s infinite ease-in-out;
}

@keyframes applePulse{
    0%{transform:scale(.8);}
    50%{transform:scale(1.12);}
    100%{transform:scale(.8);}
}


/* 지렁이 */

#snakeSVG{
    position:absolute;
    left:0;
    top:0;

    width:648px;
    height:648px;

    pointer-events:none;

    z-index:40;
}

#snakeShadow{
    fill:none;
    stroke:#172a60;
    stroke-width:43;
    stroke-linecap:round;
    stroke-linejoin:round;
    opacity:.35;
}

#snakeBody{
    fill:none;
    stroke-width:36;
    stroke-linecap:round;
    stroke-linejoin:round;
}

#snakeLight{
    fill:none;
    stroke-width:6;
    stroke-linecap:round;
    opacity:.45;
}

#dashTrail{
    display:none;
    fill:none;
    stroke:white;
    stroke-width:9;
    stroke-linecap:round;
    stroke-dasharray:15 15;
    opacity:.4;
}

.dashing #dashTrail{
    display:block;
    animation:trail .22s linear infinite;
}

@keyframes trail{
    from{stroke-dashoffset:0;}
    to{stroke-dashoffset:-30px;}
}


/* 머리 */

#headGroup{
    transition:transform .03s linear;
}

#mouthClosed{
    stroke:#101e4c;
    stroke-width:3;
    fill:none;
}

#mouthOpenGroup{
    display:none;
}

#openMouth{
    fill:#111;
    stroke:#081535;
    stroke-width:2;
}

#tongue{
    fill:#ff4c62;
}


/* 바람 */

#windLayer{
    display:none;
}

.dashActive #windLayer{
    display:block;
}

.wind{
    fill:none;
    stroke:white;
    stroke-width:4;
    stroke-linecap:round;
    opacity:0;
}

.dashActive .wind1{
    animation:wind .28s infinite;
}

.dashActive .wind2{
    animation:wind .36s infinite .06s;
}

.dashActive .wind3{
    animation:wind .32s infinite .12s;
}

@keyframes wind{
    0%{
        opacity:0;
        transform:translateX(20px);
    }
    35%{opacity:.8;}
    100%{
        opacity:0;
        transform:translateX(-40px);
    }
}


/* 폭발 */

#crash{
    display:none;

    position:absolute;

    font-size:78px;

    z-index:400;

    transform:translate(-50%,-50%);
}


/* =========================
   오버레이
========================= */

.overlay{
    display:none;

    position:absolute;

    left:50%;
    top:50%;

    transform:translate(-50%,-50%);

    width:450px;

    padding:35px 25px;

    border-radius:25px;

    background:rgba(0,0,0,.95);

    color:white;

    text-align:center;

    z-index:700;
}

.overlay h1{
    font-size:60px;
    margin:0 0 25px;
}

.overlayButton{
    width:280px;
    height:58px;
    margin:8px;
    border:none;
    border-radius:14px;

    color:white;
    font-size:21px;
    font-weight:bold;
}

.continue{
    background:#477fe5;
}

.restart{
    background:#43b96a;
}

#gameOver h1{
    color:#ff4040;
}


/* 스킬 알림 */

#skillFlash{
    display:none;

    position:absolute;

    left:50%;
    top:48%;

    transform:translate(-50%,-50%);

    z-index:350;

    color:white;

    font-size:35px;
    font-weight:900;

    text-shadow:0 3px 10px black;
}


/* 퀘스트 완료 */

#questComplete{
    display:none;

    position:fixed;

    left:50%;
    top:15%;

    transform:translateX(-50%);

    z-index:1500;

    background:rgba(0,0,0,.94);

    color:#ffd84d;

    padding:16px 27px;

    border-radius:17px;

    font-size:22px;
    font-weight:900;
}
</style>
</head>


<body>

<div class="screen">

<!-- ==================================================
     메인 화면
================================================== -->

<div id="mainScreen">

    <div class="logo">🪱</div>

    <div class="title">
        WORM QUEST
    </div>

    <div class="subtitle">
        먹고 · 성장하고 · 질주하라
    </div>

    <div class="mainStats">

        <div class="mainStat coin">
            🪙 <span id="mainCoins">0</span>
        </div>

        <div class="mainStat">
            🏆 최고기록
            <span id="mainHigh">0</span>
        </div>

    </div>

    <button
        class="mainButton startButton"
        id="startGameButton">
        🎮 게임 시작하기
    </button>

    <button
        class="mainButton shopMainButton"
        id="openShopMain">
        🛒 상점
    </button>

    <div class="wormPreview">
        🪱
    </div>

</div>


<!-- ==================================================
     상점 화면
================================================== -->

<div id="shopScreen">

    <div class="shopTop">

        <div class="shopTitle">
            🛒 지렁이 상점
        </div>

        <div class="shopMoney">
            🪙 <span id="shopCoins">0</span>
        </div>

        <button
            class="backButton"
            id="shopBack">
            ← 메인으로
        </button>

    </div>

    <div
        class="shopGrid"
        id="shopItems">
    </div>

</div>


<!-- ==================================================
     게임 화면
================================================== -->

<div id="gameScreen">

    <div class="gameTop">

        <div class="gameStat">
            🏆 최고기록
            <span id="highScore">0</span>
        </div>

        <div class="gameStat gameCoin">
            🪙 <span id="coins">0</span>
        </div>

    </div>


    <div id="game" tabindex="0">

        <div id="scoreBox">
            점수:
            <span id="score">0</span>
        </div>


        <div id="skillBox">

            ⚡ <span id="skillNameTop">
                질주
            </span>

            <br>

            <small id="skillStatus">
                READY
            </small>

        </div>


        <!-- 작은 퀘스트 -->
        <div id="questMini">

            <div class="questMiniTitle">
                📜 QUEST
            </div>

            <div id="miniQuest0"
                 class="miniQuest">
            </div>

            <div id="miniQuest1"
                 class="miniQuest">
            </div>

            <div id="miniQuest2"
                 class="miniQuest">
            </div>

        </div>


        <div id="food">
            🍎
        </div>


        <svg
            id="snakeSVG"
            viewBox="0 0 648 648">

            <path id="snakeShadow"></path>

            <path id="snakeBody"></path>

            <path id="snakeLight"></path>

            <path id="dashTrail"></path>


            <g id="windLayer">

                <path
                    class="wind wind1"
                    d="M0 -12 Q-30 -20 -60 -12">
                </path>

                <path
                    class="wind wind2"
                    d="M0 0 Q-40 -6 -70 5">
                </path>

                <path
                    class="wind wind3"
                    d="M0 12 Q-30 20 -60 14">
                </path>

            </g>


            <g id="headGroup">

                <path
                    id="headShape"
                    d="
                    M-18-21
                    Q4-28 21-15
                    Q34 0 21 15
                    Q4 28-18 21
                    Q-30 11-30 0
                    Q-30-11-18-21
                    "
                    stroke-width="3">
                </path>


                <path
                    id="headHighlight"
                    d="M-17-17 Q-2-23 10-15"
                    fill="none"
                    stroke-width="6"
                    stroke-linecap="round">
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


                <path
                    id="mouthClosed"
                    d="M16-5 Q23 0 16 5">
                </path>


                <g id="mouthOpenGroup">

                    <path
                        id="openMouth"
                        d="
                        M12-8
                        Q25-10 28 0
                        Q25 10 12 8
                        Q17 0 12-8
                        ">
                    </path>

                    <path
                        id="tongue"
                        d="
                        M16 3
                        Q21 0 25 3
                        Q21 10 16 6 Z">
                    </path>

                </g>

            </g>

        </svg>


        <div id="crash">
            💥
        </div>


        <div id="skillFlash"></div>


        <!-- 일시정지 -->

        <div
            id="pauseOverlay"
            class="overlay">

            <h1>일시정지</h1>

            <button
                id="continueButton"
                class="overlayButton continue">
                ▶️ 계속하기
            </button>

            <button
                id="restartButton"
                class="overlayButton restart">
                🔄 다시하기
            </button>

        </div>


        <!-- 게임 오버 -->

        <div
            id="gameOver"
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
                🏆 최고기록:
                <span id="gameOverHigh">0</span>
            </h2>

            <button
                id="gameOverRestart"
                class="overlayButton restart">
                🔄 다시하기
            </button>

            <button
                id="gameBackMain"
                class="overlayButton continue">
                🏠 메인으로
            </button>

        </div>

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
   지렁이 데이터
===================================================== */

const worms = {

    basic:{
        name:"기본 지렁이",
        price:0,
        skill:"기본 질주",
        color:"#315fc9",
        light:"#739cff",
        head:"#315fc9",
        duration:2000,
        cooldown:10000,
        speed:65,
        emoji:"🪱"
    },

    fire:{
        name:"🔥 화염 지렁이",
        price:500,
        skill:"화염질주",
        color:"#e34b32",
        light:"#ff9d45",
        head:"#e34b32",
        duration:2500,
        cooldown:9000,
        speed:55,
        emoji:"🔥"
    },

    lightning:{
        name:"⚡ 번개 지렁이",
        price:1000,
        skill:"번개질주",
        color:"#704ee8",
        light:"#fff45a",
        head:"#704ee8",
        duration:1300,
        cooldown:8000,
        speed:38,
        emoji:"⚡"
    },

    ghost:{
        name:"👻 유령 지렁이",
        price:2000,
        skill:"유령화",
        color:"#dce9ff",
        light:"#ffffff",
        head:"#b9d5ff",
        duration:3000,
        cooldown:12000,
        speed:72,
        emoji:"👻"
    },

    rainbow:{
        name:"🌈 무지개 지렁이",
        price:3000,
        skill:"무지개질주",
        color:"#ff55bb",
        light:"#fff",
        head:"#ff55bb",
        duration:2200,
        cooldown:10000,
        speed:60,
        emoji:"🌈"
    }

};


/* =====================================================
   퀘스트
===================================================== */

const questPool = [

    {
        type:"apples",
        name:"🍎 사과 먹기",
        target:5,
        reward:80
    },

    {
        type:"apples",
        name:"🍎 사과 많이 먹기",
        target:10,
        reward:150
    },

    {
        type:"score",
        name:"🏆 점수 달성",
        target:10,
        reward:100
    },

    {
        type:"score",
        name:"🏆 고득점 도전",
        target:20,
        reward:200
    },

    {
        type:"dash",
        name:"⚡ 스킬 사용",
        target:3,
        reward:80
    },

    {
        type:"dash",
        name:"⚡ 스킬 마스터",
        target:7,
        reward:180
    },

    {
        type:"distance",
        name:"🪱 이동하기",
        target:50,
        reward:70
    },

    {
        type:"distance",
        name:"🪱 장거리 이동",
        target:150,
        reward:160
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
        localStorage.getItem("wormOwned")
        || '["basic"]'
    );

let equipped =
    localStorage.getItem("wormEquipped")
    || "basic";

let questData =
    JSON.parse(
        localStorage.getItem("wormQuests")
        || "null"
    );


/* =====================================================
   퀘스트 생성
===================================================== */

function makeQuest(){

    let available =
        questPool.filter(q =>
            !questData ||
            !questData.some(old =>
                old.type === q.type &&
                old.target === q.target
            )
        );

    if(available.length === 0){
        available = questPool;
    }

    const q =
        available[
            Math.floor(
                Math.random() *
                available.length
            )
        ];

    return {
        type:q.type,
        name:q.name,
        target:q.target,
        reward:Math.min(q.reward,200),
        progress:0
    };
}


if(
    !Array.isArray(questData) ||
    questData.length !== 3
){

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

function saveQuests(){

    localStorage.setItem(
        "wormQuests",
        JSON.stringify(questData)
    );
}


function saveAll(){

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


/* =====================================================
   화면 전환
===================================================== */

const mainScreen =
    document.getElementById(
        "mainScreen"
    );

const gameScreen =
    document.getElementById(
        "gameScreen"
    );

const shopScreen =
    document.getElementById(
        "shopScreen"
    );


function showMain(){

    stopGameCompletely();

    mainScreen.style.display =
        "flex";

    gameScreen.style.display =
        "none";

    shopScreen.style.display =
        "none";

    updateMain();
}


function showGame(){

    mainScreen.style.display =
        "none";

    shopScreen.style.display =
        "none";

    gameScreen.style.display =
        "block";

    restart();

    game.focus();
}


function showShop(){

    stopGameCompletely();

    mainScreen.style.display =
        "none";

    gameScreen.style.display =
        "none";

    shopScreen.style.display =
        "block";

    renderShop();
}


/* =====================================================
   메인 UI
===================================================== */

function updateMain(){

    document.getElementById(
        "mainCoins"
    ).textContent = coins;

    document.getElementById(
        "mainHigh"
    ).textContent = highScore;
}


/* =====================================================
   게임 변수
===================================================== */

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

let shiftHeld = false;
let dashing = false;

let dashEnd = 0;
let lastSkill = -Infinity;
let lastMove = performance.now();

let distance = 0;
let apples = 0;
let skillUses = 0;

let animationFrame = null;


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

const foodEl =
    document.getElementById("food");

const snakeBody =
    document.getElementById("snakeBody");

const snakeShadow =
    document.getElementById("snakeShadow");

const snakeLight =
    document.getElementById("snakeLight");

const dashTrail =
    document.getElementById("dashTrail");

const headGroup =
    document.getElementById("headGroup");

const headShape =
    document.getElementById("headShape");

const headHighlight =
    document.getElementById("headHighlight");

const mouthClosed =
    document.getElementById("mouthClosed");

const mouthOpenGroup =
    document.getElementById("mouthOpenGroup");

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
   현재 지렁이
===================================================== */

function worm(){
    return worms[equipped];
}


/* =====================================================
   외형
===================================================== */

function applyAppearance(){

    const w = worm();

    snakeBody.style.stroke =
        w.color;

    snakeLight.style.stroke =
        w.light;

    headShape.style.fill =
        w.head;

    headShape.style.stroke =
        w.color;

    headHighlight.style.stroke =
        w.light;

    skillNameTop.textContent =
        w.skill;

    if(equipped === "ghost"){

        snakeBody.style.opacity =
            ".65";

    }else{

        snakeBody.style.opacity =
            "1";
    }
}


/* =====================================================
   초기화
===================================================== */

function resetSnake(){

    snake = [
        {x:8,y:9},
        {x:7,y:9},
        {x:6,y:9},
        {x:5,y:9},
        {x:4,y:9}
    ];

    previousSnake =
        snake.map(p => ({
            x:p.x,
            y:p.y
        }));
}


function createFood(){

    let valid = false;

    while(!valid){

        food = {
            x:Math.floor(
                Math.random()*COLS
            ),
            y:Math.floor(
                Math.random()*ROWS
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
   사과 거리 / 입
===================================================== */

function foodDistance(){

    return Math.max(
        Math.abs(
            snake[0].x-food.x
        ),
        Math.abs(
            snake[0].y-food.y
        )
    );
}


function updateMouth(){

    if(
        !dead &&
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


/* =====================================================
   부드러운 이동
===================================================== */

function lerp(a,b,t){
    return a+(b-a)*t;
}


function animatedSnake(progress){

    return snake.map(
        (part,i) => {

            const old =
                previousSnake[i] ||
                part;

            return {
                x:lerp(
                    old.x,
                    part.x,
                    progress
                ),
                y:lerp(
                    old.y,
                    part.y,
                    progress
                )
            };
        }
    );
}


function makePath(parts){

    const points =
        [...parts]
        .reverse()
        .map(p => ({
            x:p.x*GRID+GRID/2,
            y:p.y*GRID+GRID/2
        }));

    if(points.length < 2){
        return "";
    }

    let path =
        `M ${points[0].x} ${points[0].y}`;

    for(
        let i=1;
        i<points.length-1;
        i++
    ){

        const a = points[i];
        const b = points[i+1];

        const mx =
            (a.x+b.x)/2;

        const my =
            (a.y+b.y)/2;

        path +=
            ` Q ${a.x} ${a.y} ${mx} ${my}`;
    }

    const last =
        points[points.length-1];

    path +=
        ` L ${last.x} ${last.y}`;

    return path;
}


function angle(){

    if(direction.x===1) return 0;
    if(direction.y===1) return 90;
    if(direction.x===-1) return 180;

    return -90;
}


/* =====================================================
   렌더
===================================================== */

function render(progress=1){

    const parts =
        animatedSnake(progress);

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
        head.x*GRID+GRID/2;

    const hy =
        head.y*GRID+GRID/2;

    headGroup.setAttribute(
        "transform",
        `translate(${hx} ${hy}) rotate(${angle()})`
    );

    foodEl.style.left =
        food.x*GRID+"px";

    foodEl.style.top =
        food.y*GRID+"px";

    scoreEl.textContent =
        score;

    highEl.textContent =
        highScore;

    coinsEl.textContent =
        coins;

    updateMouth();
    renderMiniQuests();
}


/* =====================================================
   속도
===================================================== */

function moveTime(){

    if(!dashing){
        return NORMAL_SPEED;
    }

    return worm().speed;
}


/* =====================================================
   애니메이션
===================================================== */

function animate(time){

    if(dead || paused){
        return;
    }

    if(
        dashing &&
        time>=dashEnd
    ){

        stopSkill();
    }

    const progress =
        Math.min(
            (time-lastMove)/
            moveTime(),
            1
        );

    const eased =
        progress<.5
        ? 2*progress*progress
        : 1-Math.pow(
            -2*progress+2,
            2
        )/2;

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

function move(){

    if(dead || paused){
        return;
    }

    direction =
        nextDirection;

    const head =
        snake[0];

    const newHead = {
        x:head.x+direction.x,
        y:head.y+direction.y
    };


    /* 유령화 */

    if(
        equipped === "ghost" &&
        dashing
    ){

        if(newHead.x<0)
            newHead.x=COLS-1;

        if(newHead.x>=COLS)
            newHead.x=0;

        if(newHead.y<0)
            newHead.y=ROWS-1;

        if(newHead.y>=ROWS)
            newHead.y=0;

    }else{

        if(
            newHead.x<0 ||
            newHead.x>=COLS ||
            newHead.y<0 ||
            newHead.y>=ROWS
        ){

            crashGame(newHead);
            return;
        }
    }


    /* 몸 충돌 */

    if(
        snake.some(
            p =>
                p.x===newHead.x &&
                p.y===newHead.y
        )
    ){

        crashGame(newHead);
        return;
    }


    previousSnake =
        snake.map(p => ({
            x:p.x,
            y:p.y
        }));

    snake.unshift(newHead);

    distance++;


    if(
        newHead.x===food.x &&
        newHead.y===food.y
    ){

        score++;
        apples++;

        coins+=10;

        if(score>highScore){

            highScore=score;

            localStorage.setItem(
                "wormHighScore",
                highScore
            );
        }

        createFood();
        checkQuests();

    }else{

        snake.pop();
    }


    lastMove =
        performance.now();

    saveAll();

    render(0);
}


/* =====================================================
   스킬
===================================================== */

function startSkill(){

    if(
        dead ||
        paused ||
        dashing
    ){
        return;
    }

    const now =
        performance.now();

    const w =
        worm();

    if(
        now-lastSkill<w.cooldown
    ){
        return;
    }

    dashing=true;

    lastSkill=now;

    dashEnd =
        now+w.duration;

    skillUses++;

    game.classList.add(
        "dashing"
    );

    game.classList.add(
        "dashActive"
    );

    skillFlash.textContent =
        w.emoji+" "+w.skill;

    skillFlash.style.display =
        "block";

    setTimeout(
        ()=>{
            skillFlash.style.display =
                "none";
        },
        500
    );

    checkQuests();
}


function stopSkill(){

    dashing=false;

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


function updateSkillUI(){

    const w =
        worm();

    const now =
        performance.now();

    if(dashing){

        skillStatus.textContent =
            "🔥 "+
            Math.max(
                0,
                (dashEnd-now)/1000
            ).toFixed(1)+
            "초";

        return;
    }

    const left =
        w.cooldown-
        (now-lastSkill);

    if(
        lastSkill===-Infinity ||
        left<=0
    ){

        skillStatus.textContent =
            "READY ⚡";

    }else{

        skillStatus.textContent =
            "쿨타임 "+
            Math.ceil(
                left/1000
            )+
            "초";
    }
}


/* =====================================================
   죽음
===================================================== */

function crashGame(pos){

    dead=true;

    stopSkill();

    crash.style.left =
        pos.x*GRID+GRID/2+"px";

    crash.style.top =
        pos.y*GRID+GRID/2+"px";

    crash.style.display =
        "block";


    setTimeout(
        ()=>{

            document.getElementById(
                "finalScore"
            ).textContent=score;

            document.getElementById(
                "earnedCoins"
            ).textContent=
                apples*10;

            document.getElementById(
                "gameOverHigh"
            ).textContent=
                highScore;

            gameOver.style.display =
                "block";

        },
        450
    );
}


/* =====================================================
   완전 정지
===================================================== */

function stopGameCompletely(){

    paused=true;

    dead=true;

    shiftHeld=false;

    dashing=false;

    if(animationFrame){

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame=null;
    }

    if(pauseOverlay){
        pauseOverlay.style.display =
            "none";
    }

    if(gameOver){
        gameOver.style.display =
            "none";
    }
}


/* =====================================================
   게임 다시 시작
===================================================== */

function restart(){

    score=0;
    apples=0;
    distance=0;
    skillUses=0;

    dead=false;
    paused=false;
    dashing=false;
    shiftHeld=false;

    lastSkill=-Infinity;

    direction={
        x:1,
        y:0
    };

    nextDirection={
        x:1,
        y:0
    };

    pauseOverlay.style.display =
        "none";

    gameOver.style.display =
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
    applyAppearance();

    lastMove =
        performance.now();

    render(1);

    if(animationFrame){

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
   일시정지
===================================================== */

function pauseGame(){

    if(dead || paused){
        return;
    }

    paused=true;

    pauseOverlay.style.display =
        "block";

    if(animationFrame){

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame=null;
    }
}


function resumeGame(){

    if(dead){
        return;
    }

    paused=false;

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
   작은 퀘스트 UI
===================================================== */

function renderMiniQuests(){

    questData.forEach(
        (q,i)=>{

            const el =
                document.getElementById(
                    "miniQuest"+i
                );

            if(!el){
                return;
            }

            el.innerHTML = `
                <b>${q.name}</b><br>
                ${Math.min(
                    q.progress,
                    q.target
                )}/${q.target}
                <div class="miniQuestReward">
                    🪙 ${q.reward}
                </div>
            `;
        }
    );
}


/* =====================================================
   퀘스트 체크
===================================================== */

function checkQuests(){

    questData.forEach(
        (q,i)=>{

            if(q.type==="apples"){
                q.progress=apples;
            }

            if(q.type==="score"){
                q.progress=score;
            }

            if(q.type==="dash"){
                q.progress=skillUses;
            }

            if(q.type==="distance"){
                q.progress=distance;
            }

            if(
                q.progress>=q.target
            ){

                completeQuest(i);
            }
        }
    );

    saveAll();
    renderMiniQuests();
}


/* =====================================================
   퀘스트 완료
===================================================== */

function completeQuest(index){

    const completed =
        questData[index];

    const reward =
        Math.min(
            completed.reward,
            200
        );

    coins+=reward;


    const popup =
        document.getElementById(
            "questComplete"
        );

    popup.textContent =
        "🎉 QUEST COMPLETE! +"+
        reward+
        " 🪙";

    popup.style.display =
        "block";

    setTimeout(
        ()=>{
            popup.style.display =
                "none";
        },
        1600
    );


    /*
       완료한 퀘스트만
       새로운 퀘스트로 교체
    */

    questData[index]={
        ...makeQuest(),
        progress:0
    };

    saveAll();
    renderMiniQuests();
}


/* =====================================================
   상점
===================================================== */

function renderShop(){

    const container =
        document.getElementById(
            "shopItems"
        );

    container.innerHTML="";


    document.getElementById(
        "shopCoins"
    ).textContent=coins;


    Object.entries(worms)
    .forEach(
        ([id,w])=>{

            const ownedItem =
                owned.includes(id);

            const equippedItem =
                equipped===id;

            const card =
                document.createElement(
                    "div"
                );

            card.className =
                "shopCard"+
                (
                    equippedItem
                    ? " equipped"
                    : ""
                );


            let actionText;

            if(equippedItem){

                actionText="✅ 장착 중";

            }else if(ownedItem){

                actionText="⚡ 장착";

            }else{

                actionText=
                    "🪙 "+
                    w.price+
                    " 구매";
            }


            card.innerHTML=`

                <div class="shopEmoji">
                    ${w.emoji}
                </div>

                <div class="shopName">
                    ${w.name}
                </div>

                <div class="shopSkill">
                    ⚡ ${w.skill}
                </div>

                <div class="shopPrice">
                    ${
                        w.price===0
                        ? "무료"
                        : "🪙 "+w.price
                    }
                </div>

                <button class="shopAction">
                    ${actionText}
                </button>

            `;


            card
            .querySelector(
                ".shopAction"
            )
            .onclick=()=>{

                if(equippedItem){
                    return;
                }


                if(ownedItem){

                    equipped=id;

                    saveAll();

                    renderShop();

                    return;
                }


                if(coins<w.price){

                    alert(
                        "코인이 부족합니다!"
                    );

                    return;
                }


                coins-=w.price;

                owned.push(id);

                equipped=id;

                saveAll();

                renderShop();
            };


            container.appendChild(
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
    "startGameButton"
)
.onclick=showGame;


document
.getElementById(
    "openShopMain"
)
.onclick=showShop;


document
.getElementById(
    "shopBack"
)
.onclick=showMain;


document
.getElementById(
    "continueButton"
)
.onclick=resumeGame;


document
.getElementById(
    "restartButton"
)
.onclick=restart;


document
.getElementById(
    "gameOverRestart"
)
.onclick=restart;


document
.getElementById(
    "gameBackMain"
)
.onclick=showMain;


/* =====================================================
   키보드
===================================================== */

document.addEventListener(
    "keydown",
    function(e){

        const key =
            e.key.toLowerCase();


        /* SHIFT */

        if(
            e.code==="ShiftLeft"
        ){

            e.preventDefault();

            if(!shiftHeld){

                shiftHeld=true;

                startSkill();
            }

            return;
        }


        /* ESC */

        if(
            e.code==="Escape"
        ){

            e.preventDefault();

            /*
               게임 화면일 때만
               일시정지
            */

            if(
                gameScreen.style.display===
                "block"
            ){

                if(
                    dead
                ){
                    return;
                }

                if(paused){
                    resumeGame();
                }else{
                    pauseGame();
                }
            }

            return;
        }


        /* R */

        if(
            key==="r" &&
            dead &&
            gameScreen.style.display===
            "block"
        ){

            restart();

            return;
        }


        if(
            paused ||
            dead ||
            gameScreen.style.display!==
            "block"
        ){
            return;
        }


        /* W / UP */

        if(
            (
                key==="w" ||
                key==="arrowup"
            ) &&
            direction.y!==1
        ){

            nextDirection={
                x:0,
                y:-1
            };
        }


        /* S / DOWN */

        if(
            (
                key==="s" ||
                key==="arrowdown"
            ) &&
            direction.y!==-1
        ){

            nextDirection={
                x:0,
                y:1
            };
        }


        /* A / LEFT */

        if(
            (
                key==="a" ||
                key==="arrowleft"
            ) &&
            direction.x!==1
        ){

            nextDirection={
                x:-1,
                y:0
            };
        }


        /* D / RIGHT */

        if(
            (
                key==="d" ||
                key==="arrowright"
            ) &&
            direction.x!==-1
        ){

            nextDirection={
                x:1,
                y:0
            };
        }

    }
);


/* =====================================================
   SHIFT 떼기
===================================================== */

document.addEventListener(
    "keyup",
    function(e){

        if(
            e.code==="ShiftLeft"
        ){

            shiftHeld=false;

            if(dashing){
                stopSkill();
            }
        }

    }
);


/* =====================================================
   창에서 나갔을 때
===================================================== */

window.addEventListener(
    "blur",
    function(){

        shiftHeld=false;

        if(dashing){
            stopSkill();
        }
    }
);


/* =====================================================
   이동 루프
===================================================== */

setInterval(
    ()=>{

        if(
            dead ||
            paused ||
            gameScreen.style.display!==
            "block"
        ){
            return;
        }

        const now =
            performance.now();

        if(
            now-lastMove>=
            moveTime()
        ){

            move();
        }

    },
    10
);


/* =====================================================
   시작
===================================================== */

updateMain();
renderMiniQuests();

</script>

</body>
</html>
""", height=950)
```
