```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="WORM QUEST",
    page_icon="🪱",
    layout="centered"
)

html = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
    user-select: none;
}

body {
    margin: 0;
    background: #101510;
    color: white;
    font-family: Arial, sans-serif;
}

button {
    cursor: pointer;
    border: none;
}

#app {
    width: 720px;
    min-height: 800px;
    margin: auto;
    position: relative;
}

/* =========================
   MAIN
========================= */

.screen {
    display: none;
}

.screen.active {
    display: block;
}

#mainScreen {
    text-align: center;
    padding-top: 65px;
}

.title {
    font-size: 72px;
    font-weight: 900;
    margin-bottom: 5px;
}

.subtitle {
    color: #9cad9c;
    font-size: 19px;
    margin-bottom: 40px;
}

.mainWorm {
    font-size: 100px;
    margin: 20px;
}

.stats {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-bottom: 30px;
}

.stat {
    background: #1c281e;
    border: 2px solid #354937;
    border-radius: 15px;
    padding: 15px 35px;
    font-size: 20px;
    font-weight: bold;
}

.bigButton {
    width: 330px;
    height: 65px;
    margin: 9px;
    border-radius: 15px;
    color: white;
    font-size: 21px;
    font-weight: bold;
    background: #315fc9;
}

.bigButton:hover {
    transform: scale(1.03);
}

.shopButton {
    background: #8a5bd6;
}

.backButton {
    background: #333e35;
    width: 150px;
    height: 45px;
    color: white;
    border-radius: 10px;
    font-size: 16px;
    margin-bottom: 15px;
}

/* =========================
   SHOP
========================= */

#shopScreen {
    padding: 30px;
}

.shopTitle {
    font-size: 42px;
    font-weight: 900;
    margin-bottom: 5px;
}

.coinDisplay {
    color: #ffd84d;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 25px;
}

.shopSection {
    margin-top: 25px;
    margin-bottom: 10px;
    font-size: 25px;
    font-weight: bold;
}

.items {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.item {
    background: #1c281e;
    border: 2px solid #354937;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.itemEmoji {
    font-size: 60px;
}

.itemName {
    font-size: 19px;
    font-weight: bold;
    margin: 8px;
}

.itemPrice {
    color: #ffd84d;
    margin: 8px;
}

.item button {
    width: 100%;
    height: 42px;
    border-radius: 9px;
    background: #315fc9;
    color: white;
    font-size: 15px;
    font-weight: bold;
}

.item button.owned {
    background: #3c7048;
}

.item button.equipped {
    background: #d08b28;
}

/* =========================
   GAME
========================= */

#gameScreen {
    width: 720px;
}

.gameTop {
    height: 65px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px 18px;
}

.score {
    font-size: 19px;
    font-weight: bold;
}

.high {
    color: #ffd84d;
    font-size: 18px;
    font-weight: bold;
}

.gameArea {
    width: 650px;
    height: 650px;
    margin: auto;
    position: relative;
}

#board {
    width: 612px;
    height: 612px;
    position: absolute;
    left: 19px;
    top: 10px;

    border: 9px solid #234e9e;
    border-radius: 20px;
    overflow: hidden;

    background-color: #91c74b;

    background-image:
        linear-gradient(
            rgba(0,0,0,0.08) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(0,0,0,0.08) 1px,
            transparent 1px
        );

    background-size: 34px 34px;
}

#snakeSvg {
    position: absolute;
    width: 612px;
    height: 612px;
    left: 0;
    top: 0;
    overflow: visible;
}

#snakeBody {
    fill: none;
    stroke: #315fc9;
    stroke-width: 29;
    stroke-linecap: round;
    stroke-linejoin: round;
}

#snakeHighlight {
    fill: none;
    stroke: #8fb2ff;
    stroke-width: 5;
    stroke-linecap: round;
}

#head {
    fill: #315fc9;
}

.eye {
    fill: white;
}

.pupil {
    fill: black;
}

#normalMouth {
    stroke: #111;
    stroke-width: 4;
    fill: none;
}

#openMouth {
    display: none;
}

#apple {
    position: absolute;
    width: 34px;
    height: 34px;
    font-size: 29px;
    text-align: center;
    z-index: 20;
    animation: applePulse .7s infinite;
}

@keyframes applePulse {
    0% { transform: scale(.82); }
    50% { transform: scale(1.12); }
    100% { transform: scale(.82); }
}

/* Quest */

#questBox {
    position: absolute;
    right: 30px;
    top: 25px;
    width: 180px;
    background: rgba(0,0,0,.75);
    border-radius: 12px;
    padding: 9px 12px;
    z-index: 100;
    font-size: 12px;
}

.questTitle {
    color: #ffd84d;
    font-weight: bold;
    font-size: 14px;
    margin-bottom: 5px;
}

.questReward {
    color: #ffd84d;
    margin-top: 4px;
}

/* Skill */

#skillBox {
    position: absolute;
    left: 30px;
    top: 25px;
    background: rgba(0,0,0,.75);
    border-radius: 12px;
    padding: 9px 12px;
    z-index: 100;
    font-size: 12px;
}

.skillReady {
    color: #71e28a;
}

.skillCooldown {
    color: #ffd84d;
}

/* wind */

.wind {
    position: absolute;
    height: 4px;
    background: white;
    border-radius: 4px;
    opacity: 0;
    z-index: 150;
    pointer-events: none;
}

.wind.active {
    animation: windSlash .35s linear infinite;
}

@keyframes windSlash {
    0% {
        opacity: 0;
        transform: translateX(-30px) rotate(-15deg);
    }
    30% {
        opacity: .9;
    }
    100% {
        opacity: 0;
        transform: translateX(60px) rotate(-15deg);
    }
}

/* Pause */

.overlay {
    display: none;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);

    width: 440px;
    padding: 35px;

    background: rgba(0,0,0,.95);
    border-radius: 25px;
    text-align: center;

    z-index: 500;
}

.overlay.active {
    display: block;
}

.overlay h1 {
    font-size: 55px;
    margin: 5px;
}

.overlay button {
    display: block;
    width: 280px;
    height: 53px;
    margin: 10px auto;
    border-radius: 12px;
    color: white;
    font-size: 18px;
    font-weight: bold;
}

.continue {
    background: #315fc9;
}

.restart {
    background: #3e9d5b;
}

.death h1 {
    color: #ff4545;
}

#boom {
    display: none;
    position: absolute;
    font-size: 75px;
    z-index: 400;
}

#deathScreen {
    z-index: 600;
}

/* notification */

#notification {
    position: fixed;
    left: 50%;
    bottom: 30px;
    transform: translateX(-50%);

    background: #202c22;
    border: 2px solid #4c684e;
    border-radius: 12px;

    padding: 13px 25px;
    font-weight: bold;

    display: none;
    z-index: 1000;
}

</style>
</head>

<body>

<div id="app">

<!-- ================= MAIN ================= -->

<div id="mainScreen" class="screen active">

    <div class="title">🪱 WORM QUEST</div>

    <div class="subtitle">
        먹고 · 성장하고 · 질주하라
    </div>

    <div class="mainWorm" id="mainWorm">🪱</div>

    <div class="stats">

        <div class="stat">
            🪙 <span id="mainCoins">0</span>
        </div>

        <div class="stat">
            🏆 <span id="mainHigh">0</span>
        </div>

    </div>

    <button class="bigButton" onclick="startGame()">
        🎮 게임 시작하기
    </button>

    <br>

    <button
        class="bigButton shopButton"
        onclick="openShop()">
        🛒 상점
    </button>

</div>


<!-- ================= SHOP ================= -->

<div id="shopScreen" class="screen">

    <button
        class="backButton"
        onclick="showScreen('mainScreen')">
        ← 메인으로
    </button>

    <div class="shopTitle">🛒 상점</div>

    <div class="coinDisplay">
        🪙 <span id="shopCoins">0</span>
    </div>

    <div class="shopSection">
        🪱 지렁이 외형
    </div>

    <div class="items" id="wormItems"></div>

    <div class="shopSection">
        ⚡ 스킬 변경
    </div>

    <div class="items" id="skillItems"></div>

</div>


<!-- ================= GAME ================= -->

<div id="gameScreen" class="screen">

    <div class="gameTop">

        <div class="score">
            점수: <span id="score">0</span>
            &nbsp;&nbsp;
            🪙 <span id="gameCoins">0</span>
        </div>

        <div class="high">
            🏆 최고기록:
            <span id="gameHigh">0</span>
        </div>

    </div>

    <div class="gameArea">

        <div id="board">

            <div id="skillBox">
                ⚡ <span id="skillName">질주</span>
                <br>
                <span id="skillStatus" class="skillReady">
                    READY
                </span>
            </div>

            <div id="questBox">

                <div class="questTitle">
                    📜 QUEST
                </div>

                <div id="questText">
                    사과 먹기 0/5
                </div>

                <div class="questReward">
                    🪙 보상: <span id="questReward">80</span>
                </div>

            </div>

            <div id="apple">🍎</div>

            <svg id="snakeSvg"
                 viewBox="0 0 612 612">

                <path
                    id="snakeBody">
                </path>

                <path
                    id="snakeHighlight">
                </path>

                <g id="headGroup">

                    <circle
                        id="head"
                        cx="0"
                        cy="0"
                        r="18">
                    </circle>

                    <circle
                        class="eye"
                        cx="7"
                        cy="-11"
                        r="7">
                    </circle>

                    <circle
                        class="eye"
                        cx="7"
                        cy="11"
                        r="7">
                    </circle>

                    <circle
                        class="pupil"
                        cx="9"
                        cy="-11"
                        r="3">
                    </circle>

                    <circle
                        class="pupil"
                        cx="9"
                        cy="11"
                        r="3">
                    </circle>

                    <!-- 평소 입 -->
                    <path
                        id="normalMouth"
                        d="M 12,-4 Q 19,0 12,4">
                    </path>

                    <!-- 입 벌린 모습 -->
                    <g id="openMouth">

                        <ellipse
                            cx="15"
                            cy="0"
                            rx="10"
                            ry="8"
                            fill="#111">
                        </ellipse>

                        <path
                            d="M10,3 Q15,10 20,3"
                            stroke="#ff4960"
                            stroke-width="3"
                            fill="none">
                        </path>

                    </g>

                </g>

            </svg>

            <div id="boom">💥</div>


            <!-- PAUSE -->

            <div id="pauseScreen" class="overlay">

                <h1>일시정지</h1>

                <button
                    class="continue"
                    onclick="continueGame()">
                    ▶️ 계속하기
                </button>

                <button
                    class="restart"
                    onclick="restartGame()">
                    🔄 다시하기
                </button>

            </div>


            <!-- DEATH -->

            <div id="deathScreen"
                 class="overlay death">

                <h1>YOU DIE</h1>

                <h2>
                    점수:
                    <span id="finalScore">0</span>
                </h2>

                <button
                    class="restart"
                    onclick="restartGame()">
                    🔄 다시하기
                </button>

                <button
                    class="continue"
                    onclick="showScreen('mainScreen')">
                    🏠 메인으로
                </button>

            </div>


            <!-- WIND EFFECTS -->

            <div
                class="wind"
                id="wind1"
                style="width:100px;top:230px;left:80px">
            </div>

            <div
                class="wind"
                id="wind2"
                style="width:70px;top:300px;left:420px">
            </div>

            <div
                class="wind"
                id="wind3"
                style="width:90px;top:380px;left:150px">
            </div>

        </div>

    </div>

</div>

<div id="notification"></div>

</div>


<script>

/* =====================================================
   DATA
===================================================== */

const worms = {

    basic: {
        name: "기본 지렁이",
        emoji: "🪱",
        color: "#315fc9",
        price: 0
    },

    fire: {
        name: "화염 지렁이",
        emoji: "🔥",
        color: "#e14b32",
        price: 500
    },

    lightning: {
        name: "번개 지렁이",
        emoji: "⚡",
        color: "#d8b62b",
        price: 1000
    },

    ghost: {
        name: "유령 지렁이",
        emoji: "👻",
        color: "#a77be8",
        price: 1500
    },

    rainbow: {
        name: "무지개 지렁이",
        emoji: "🌈",
        color: "#e95db8",
        price: 2000
    }

};


const skills = {

    dash: {
        name: "질주",
        price: 0,
        description: "LShift 홀드"
    },

    turbo: {
        name: "터보 질주",
        price: 700,
        description: "더 빠른 질주"
    },

    wind: {
        name: "윈드 러너",
        price: 1200,
        description: "강력한 바람 질주"
    },

    flash: {
        name: "플래시",
        price: 1800,
        description: "최고속 질주"
    }

};


/* =====================================================
   SAVE DATA
===================================================== */

let coins =
    Number(localStorage.getItem("wormCoins") || 0);

let highScore =
    Number(localStorage.getItem("wormHigh") || 0);

let equippedWorm =
    localStorage.getItem("wormEquipped") || "basic";

let equippedSkill =
    localStorage.getItem("wormSkill") || "dash";

let ownedWorms =
    JSON.parse(
        localStorage.getItem("wormOwned") ||
        '["basic"]'
    );

let ownedSkills =
    JSON.parse(
        localStorage.getItem("skillOwned") ||
        '["dash"]'
    );


/* =====================================================
   QUEST
===================================================== */

const questPool = [

    {
        type: "apple",
        text: "🍎 사과 먹기",
        target: 5,
        reward: 80
    },

    {
        type: "apple",
        text: "🍎 사과 먹기",
        target: 10,
        reward: 150
    },

    {
        type: "score",
        text: "🏆 점수 달성",
        target: 15,
        reward: 200
    },

    {
        type: "score",
        text: "🏆 점수 달성",
        target: 25,
        reward: 200
    },

    {
        type: "length",
        text: "🪱 몸 길이 늘리기",
        target: 10,
        reward: 120
    },

    {
        type: "length",
        text: "🪱 몸 길이 늘리기",
        target: 15,
        reward: 180
    }

];

let quests = [];

function newQuests() {

    quests = [];

    let copy = [...questPool];

    for(let i=0;i<3;i++) {

        let index =
            Math.floor(
                Math.random()*copy.length
            );

        quests.push(
            copy.splice(index,1)[0]
        );

    }

    quests.forEach(q => q.progress = 0);

    localStorage.setItem(
        "wormQuests",
        JSON.stringify(quests)
    );
}

function loadQuests() {

    let saved =
        localStorage.getItem("wormQuests");

    if(saved) {

        try {

            quests = JSON.parse(saved);

            if(
                !Array.isArray(quests) ||
                quests.length !== 3
            ) {
                newQuests();
            }

        } catch {

            newQuests();

        }

    } else {

        newQuests();

    }

}

loadQuests();


/* =====================================================
   UI
===================================================== */

function saveData() {

    localStorage.setItem(
        "wormCoins",
        coins
    );

    localStorage.setItem(
        "wormHigh",
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
        JSON.stringify(ownedWorms)
    );

    localStorage.setItem(
        "skillOwned",
        JSON.stringify(ownedSkills)
    );

    localStorage.setItem(
        "wormQuests",
        JSON.stringify(quests)
    );

    updateUI();

}


function updateUI() {

    document.getElementById(
        "mainCoins"
    ).textContent = coins;

    document.getElementById(
        "shopCoins"
    ).textContent = coins;

    document.getElementById(
        "gameCoins"
    ).textContent = coins;

    document.getElementById(
        "mainHigh"
    ).textContent = highScore;

    document.getElementById(
        "gameHigh"
    ).textContent = highScore;

    document.getElementById(
        "mainWorm"
    ).textContent =
        worms[equippedWorm].emoji;

    document.getElementById(
        "skillName"
    ).textContent =
        skills[equippedSkill].name;

}


/* =====================================================
   SCREEN
===================================================== */

function showScreen(id) {

    document
        .querySelectorAll(".screen")
        .forEach(
            s => s.classList.remove("active")
        );

    document
        .getElementById(id)
        .classList.add("active");

    updateUI();

    if(id === "shopScreen") {
        renderShop();
    }

}


function openShop() {
    showScreen("shopScreen");
}


/* =====================================================
   SHOP
===================================================== */

function renderShop() {

    let wormHTML = "";

    for(
        const [id,worm]
        of Object.entries(worms)
    ) {

        let owned =
            ownedWorms.includes(id);

        let equipped =
            equippedWorm === id;

        let buttonText =
            equipped
            ? "장착 중"
            : owned
            ? "장착하기"
            : "구매";

        let cls =
            equipped
            ? "equipped"
            : owned
            ? "owned"
            : "";

        wormHTML += `

        <div class="item">

            <div
                class="itemEmoji"
                style="color:${worm.color}">
                ${worm.emoji}
            </div>

            <div class="itemName">
                ${worm.name}
            </div>

            <div class="itemPrice">
                ${
                    worm.price === 0
                    ? "무료"
                    : "🪙 " + worm.price
                }
            </div>

            <button
                class="${cls}"
                onclick="buyWorm('${id}')">
                ${buttonText}
            </button>

        </div>

        `;

    }

    document.getElementById(
        "wormItems"
    ).innerHTML = wormHTML;


    let skillHTML = "";

    for(
        const [id,skill]
        of Object.entries(skills)
    ) {

        let owned =
            ownedSkills.includes(id);

        let equipped =
            equippedSkill === id;

        let buttonText =
            equipped
            ? "사용 중"
            : owned
            ? "변경하기"
            : "구매";

        let cls =
            equipped
            ? "equipped"
            : owned
            ? "owned"
            : "";

        skillHTML += `

        <div class="item">

            <div
                class="itemEmoji">
                ⚡
            </div>

            <div class="itemName">
                ${skill.name}
            </div>

            <div>
                ${skill.description}
            </div>

            <div class="itemPrice">
                ${
                    skill.price === 0
                    ? "무료"
                    : "🪙 " + skill.price
                }
            </div>

            <button
                class="${cls}"
                onclick="buySkill('${id}')">
                ${buttonText}
            </button>

        </div>

        `;

    }

    document.getElementById(
        "skillItems"
    ).innerHTML = skillHTML;

}


function buyWorm(id) {

    if(ownedWorms.includes(id)) {

        equippedWorm = id;

        applyWorm();

        saveData();

        notify(
            worms[id].name +
            " 장착!"
        );

        renderShop();

        return;
    }

    let price = worms[id].price;

    if(coins < price) {

        notify("🪙 코인이 부족합니다!");

        return;
    }

    coins -= price;

    ownedWorms.push(id);

    equippedWorm = id;

    applyWorm();

    saveData();

    notify(
        worms[id].name +
        " 구매 완료!"
    );

    renderShop();

}


function buySkill(id) {

    if(ownedSkills.includes(id)) {

        equippedSkill = id;

        saveData();

        notify(
            skills[id].name +
            "으로 변경!"
        );

        renderShop();

        return;
    }

    let price = skills[id].price;

    if(coins < price) {

        notify("🪙 코인이 부족합니다!");

        return;
    }

    coins -= price;

    ownedSkills.push(id);

    equippedSkill = id;

    saveData();

    notify(
        skills[id].name +
        " 구매 완료!"
    );

    renderShop();

}


function applyWorm() {

    let color =
        worms[equippedWorm].color;

    document.getElementById(
        "snakeBody"
    ).style.stroke = color;

    document.getElementById(
        "head"
    ).style.fill = color;

}


/* =====================================================
   NOTIFICATION
===================================================== */

let notificationTimer;

function notify(text) {

    let n =
        document.getElementById(
            "notification"
        );

    n.textContent = text;

    n.style.display = "block";

    clearTimeout(notificationTimer);

    notificationTimer =
        setTimeout(
            () => {
                n.style.display = "none";
            },
            1800
        );

}


/* =====================================================
   GAME VARIABLES
===================================================== */

const GRID = 34;
const SIZE = 18;

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

let apple = {
    x:10,
    y:10
};

let score = 0;

let gameRunning = false;
let paused = false;
let dead = false;

let lastMove = 0;

let shiftHeld = false;
let dashActive = false;

let dashStart = 0;
let lastDash = -10000;


/* =====================================================
   GAME START
===================================================== */

function startGame() {

    showScreen("gameScreen");

    applyWorm();

    snake = [

        {x:8,y:9},
        {x:7,y:9},
        {x:6,y:9},
        {x:5,y:9},
        {x:4,y:9}

    ];

    previousSnake =
        snake.map(
            p => ({...p})
        );

    direction = {
        x:1,
        y:0
    };

    nextDirection = {
        x:1,
        y:0
    };

    score = 0;

    gameRunning = true;
    paused = false;
    dead = false;

    document.getElementById(
        "score"
    ).textContent = 0;

    document.getElementById(
        "pauseScreen"
    ).classList.remove("active");

    document.getElementById(
        "deathScreen"
    ).classList.remove("active");

    document.getElementById(
        "boom"
    ).style.display = "none";

    spawnApple();

    lastMove =
        performance.now();

    updateQuestUI();

    requestAnimationFrame(gameLoop);

}


function restartGame() {
    startGame();
}


/* =====================================================
   APPLE
===================================================== */

function spawnApple() {

    do {

        apple = {
            x: Math.floor(
                Math.random()*SIZE
            ),
            y: Math.floor(
                Math.random()*SIZE
            )
        };

    } while(
        snake.some(
            p =>
                p.x === apple.x &&
                p.y === apple.y
        )
    );

}


/* =====================================================
   MOVEMENT
===================================================== */

function moveSnake() {

    if(
        !gameRunning ||
        paused ||
        dead
    ) return;


    direction =
        {...nextDirection};


    let head = snake[0];

    let next = {

        x:
            head.x +
            direction.x,

        y:
            head.y +
            direction.y

    };


    if(
        next.x < 0 ||
        next.x >= SIZE ||
        next.y < 0 ||
        next.y >= SIZE
    ) {

        die(next);

        return;

    }


    if(
        snake.some(
            p =>
                p.x === next.x &&
                p.y === next.y
        )
    ) {

        die(next);

        return;

    }


    previousSnake =
        snake.map(
            p => ({...p})
        );


    snake.unshift(next);


    if(
        next.x === apple.x &&
        next.y === apple.y
    ) {

        score++;

        document.getElementById(
            "score"
        ).textContent = score;

        spawnApple();

        updateQuestProgress();

    } else {

        snake.pop();

    }


    lastMove =
        performance.now();

}


/* =====================================================
   SMOOTH RENDER
===================================================== */

function lerp(a,b,t) {
    return a + (b-a)*t;
}


function render(progress) {

    if(snake.length < 2)
        return;


    let points =
        snake.map(
            (p,i) => {

                let old =
                    previousSnake[i] || p;

                return {

                    x: lerp(
                        old.x,
                        p.x,
                        progress
                    ),

                    y: lerp(
                        old.y,
                        p.y,
                        progress
                    )

                };

            }
        );


    let path =
        "M " +
        (
            points[
                points.length-1
            ].x*GRID+17
        ) +
        " " +
        (
            points[
                points.length-1
            ].y*GRID+17
        );


    for(
        let i =
            points.length-2;
        i >= 0;
        i--
    ) {

        path +=
            " L " +
            (
                points[i].x*GRID+17
            ) +
            " " +
            (
                points[i].y*GRID+17
            );

    }


    document.getElementById(
        "snakeBody"
    ).setAttribute(
        "d",
        path
    );

    document.getElementById(
        "snakeHighlight"
    ).setAttribute(
        "d",
        path
    );


    let head =
        points[0];


    let angle = 0;

    if(direction.x === 1)
        angle = 0;

    if(direction.x === -1)
        angle = 180;

    if(direction.y === 1)
        angle = 90;

    if(direction.y === -1)
        angle = -90;


    document.getElementById(
        "headGroup"
    ).setAttribute(
        "transform",
        `
        translate(
            ${head.x*GRID+17}
            ${head.y*GRID+17}
        )
        rotate(${angle})
        `
    );


    let appleElement =
        document.getElementById(
            "apple"
        );


    appleElement.style.left =
        apple.x*GRID + "px";

    appleElement.style.top =
        apple.y*GRID + "px";


    /* 입 벌리기 */

    let distance =
        Math.max(
            Math.abs(
                snake[0].x -
                apple.x
            ),
            Math.abs(
                snake[0].y -
                apple.y
            )
        );


    if(distance <= 2) {

        document.getElementById(
            "normalMouth"
        ).style.display = "none";

        document.getElementById(
            "openMouth"
        ).style.display = "block";

    } else {

        document.getElementById(
            "normalMouth"
        ).style.display = "block";

        document.getElementById(
            "openMouth"
        ).style.display = "none";

    }

}


/* =====================================================
   GAME LOOP
===================================================== */

function gameLoop(time) {

    if(
        !gameRunning ||
        dead
    ) return;


    if(!paused) {

        let speed =
            dashActive
            ? getDashSpeed()
            : 155;


        let progress =
            Math.min(
                (time-lastMove)/speed,
                1
            );


        /*
            부드러운 ease-in-out
        */

        let smooth =
            progress < .5
            ? 2*progress*progress
            : 1 -
              Math.pow(
                  -2*progress+2,
                  2
              )/2;


        render(smooth);


        if(
            time-lastMove >= speed
        ) {

            moveSnake();

        }


        updateDash();


        requestAnimationFrame(
            gameLoop
        );

    }

}


/* =====================================================
   SKILLS
===================================================== */

function getDashSpeed() {

    if(equippedSkill === "turbo")
        return 48;

    if(equippedSkill === "wind")
        return 38;

    if(equippedSkill === "flash")
        return 28;

    return 65;

}


function activateDash() {

    if(
        !gameRunning ||
        paused ||
        dead ||
        dashActive
    )
        return;


    let now =
        performance.now();


    if(
        now-lastDash < 10000
    )
        return;


    dashActive = true;

    dashStart = now;

    lastDash = now;

    document
        .querySelectorAll(".wind")
        .forEach(
            w =>
                w.classList.add("active")
        );

}


function updateDash() {

    let now =
        performance.now();


    if(dashActive) {

        if(
            now-dashStart >= 2000
        ) {

            dashActive = false;

            document
                .querySelectorAll(".wind")
                .forEach(
                    w =>
                        w.classList.remove(
                            "active"
                        )
                );

        }

    }


    let status =
        document.getElementById(
            "skillStatus"
        );


    let remaining =
        10000 -
        (now-lastDash);


    if(
        lastDash < 0 ||
        remaining <= 0
    ) {

        status.textContent =
            "READY";

        status.className =
            "skillReady";

    } else if(dashActive) {

        status.textContent =
            "🔥 질주 중!";

        status.className =
            "skillReady";

    } else {

        status.textContent =
            Math.ceil(
                remaining/1000
            ) + "초";

        status.className =
            "skillCooldown";

    }

}


/* =====================================================
   DEATH
===================================================== */

function die(position) {

    dead = true;

    gameRunning = false;

    dashActive = false;


    if(score > highScore) {

        highScore = score;

        localStorage.setItem(
            "wormHigh",
            highScore
        );

    }


    let boom =
        document.getElementById(
            "boom"
        );


    boom.style.left =
        position.x*GRID + "px";

    boom.style.top =
        position.y*GRID + "px";

    boom.style.display =
        "block";


    setTimeout(
        () => {

            document.getElementById(
                "finalScore"
            ).textContent = score;

            document.getElementById(
                "deathScreen"
            ).classList.add(
                "active"
            );

            updateUI();

        },
        600
    );

}


/* =====================================================
   PAUSE
===================================================== */

function pauseGame() {

    if(
        !gameRunning ||
        dead
    ) return;


    paused = true;

    document.getElementById(
        "pauseScreen"
    ).classList.add(
        "active"
    );

}


function continueGame() {

    if(dead)
        return;


    paused = false;

    document.getElementById(
        "pauseScreen"
    ).classList.remove(
        "active"
    );


    lastMove =
        performance.now();


    requestAnimationFrame(
        gameLoop
    );

}


/* =====================================================
   KEYBOARD
===================================================== */

document.addEventListener(
    "keydown",
    function(e) {

        /*
            ESC
        */

        if(e.code === "Escape") {

            e.preventDefault();

            if(
                document
                .getElementById(
                    "gameScreen"
                )
                .classList.contains(
                    "active"
                )
            ) {

                if(paused)
                    continueGame();
                else
                    pauseGame();

            }

            return;

        }


        /*
            LSHIFT
        */

        if(
            e.code === "ShiftLeft"
        ) {

            e.preventDefault();

            shiftHeld = true;

            activateDash();

            return;

        }


        if(
            paused ||
            dead ||
            !gameRunning
        )
            return;


        let key =
            e.key.toLowerCase();


        if(
            (
                key === "w" ||
                key === "arrowup"
            ) &&
            direction.y !== 1
        ) {

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
        ) {

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
        ) {

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
        ) {

            nextDirection = {
                x:1,
                y:0
            };

        }

    }
);


document.addEventListener(
    "keyup",
    function(e) {

        if(
            e.code === "ShiftLeft"
        ) {

            shiftHeld = false;

            dashActive = false;

            document
                .querySelectorAll(".wind")
                .forEach(
                    w =>
                        w.classList.remove(
                            "active"
                        )
                );

        }

    }
);


/* =====================================================
   QUEST SYSTEM
===================================================== */

function updateQuestProgress() {

    quests.forEach(
        q => {

            if(
                q.type === "apple"
            ) {

                q.progress = score;

            }

            if(
                q.type === "score"
            ) {

                q.progress = score;

            }

            if(
                q.type === "length"
            ) {

                q.progress =
                    snake.length;

            }

        }
    );


    checkQuestCompletion();

    updateQuestUI();

    saveData();

}


function checkQuestCompletion() {

    let completedIndex = -1;


    for(
        let i=0;
        i<quests.length;
        i++
    ) {

        if(
            quests[i].progress >=
            quests[i].target
        ) {

            completedIndex = i;

            break;

        }

    }


    if(completedIndex !== -1) {

        let reward =
            Math.min(
                quests[
                    completedIndex
                ].reward,
                200
            );


        coins += reward;


        notify(
            "🎉 퀘스트 완료! +" +
            reward +
            " 🪙"
        );


        /*
            완료한 퀘스트 하나만
            새로운 퀘스트로 교체
        */

        let available =
            questPool.filter(
                q =>
                    !quests.some(
                        current =>
                            current.text === q.text &&
                            current.target === q.target
                    )
            );


        if(
            available.length === 0
        ) {

            available =
                questPool;

        }


        let replacement =
            available[
                Math.floor(
                    Math.random() *
                    available.length
                )
            ];


        quests[
            completedIndex
        ] = {
            ...replacement,
            progress: 0
        };


        saveData();

    }

}


function updateQuestUI() {

    if(!quests.length)
        return;


    let q = quests[0];


    /*
        게임 화면에는
        가장 먼저 진행 중인 퀘스트
        하나만 작게 표시
    */

    for(
        let i=0;
        i<quests.length;
        i++
    ) {

        if(
            quests[i].progress <
            quests[i].target
        ) {

            q = quests[i];

            break;

        }

    }


    let progress =
        Math.min(
            q.progress,
            q.target
        );


    document.getElementById(
        "questText"
    ).textContent =
        q.text +
        " " +
        progress +
        "/" +
        q.target;


    document.getElementById(
        "questReward"
    ).textContent =
        Math.min(
            q.reward,
            200
        );

}


/* =====================================================
   INIT
===================================================== */

updateUI();

renderShop();

</script>

</body>
</html>
"""

components.html(
    html,
    height=850,
    scrolling=False
)
```
