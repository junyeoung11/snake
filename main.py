import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="WORM QUEST",
    page_icon="🪱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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
    background:#0b120d;
    color:white;
    font-family:Arial,"Noto Sans KR",sans-serif;
    overflow:hidden;
}

button{
    font-family:inherit;
    cursor:pointer;
    border:0;
}

#app{
    width:760px;
    min-height:850px;
    margin:auto;
    position:relative;
}

.screen{
    display:none;
    width:100%;
    min-height:850px;
}

.screen.active{
    display:block;
}


/* =========================
   MAIN
========================= */

#mainScreen{
    text-align:center;
    padding-top:55px;
}

.logo{
    font-size:72px;
    font-weight:1000;
    letter-spacing:-4px;
    text-shadow:0 5px 0 #182219;
}

.logoSub{
    margin-top:-4px;
    color:#91a695;
    font-size:18px;
}

.mainWorm{
    margin:35px auto 15px;
    width:180px;
    height:180px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:125px;
    filter:drop-shadow(0 12px 10px rgba(0,0,0,.4));
    animation:floatWorm 1.8s ease-in-out infinite;
}

@keyframes floatWorm{
    0%,100%{
        transform:translateY(0) rotate(-3deg)
    }

    50%{
        transform:translateY(-10px) rotate(3deg)
    }
}

.mainStats{
    display:flex;
    justify-content:center;
    gap:14px;
    margin:20px 0 30px;
}

.mainStat{
    min-width:155px;
    padding:13px 22px;
    border:2px solid #304b35;
    border-radius:15px;
    background:#152119;
    font-size:19px;
    font-weight:800;
}

.mainButton{
    width:360px;
    height:65px;
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
    box-shadow:0 5px 0 #1e3d82;
}

.shopOpen{
    background:#744cc0;
    box-shadow:0 5px 0 #4b3180;
}


/* =========================
   SHOP
========================= */

#shopScreen{
    padding:25px 35px;
}

.pageTop{
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:22px;
}

.back{
    background:#29352c;
    color:white;
    padding:11px 18px;
    border-radius:10px;
    font-size:15px;
    font-weight:bold;
}

.pageTitle{
    font-size:43px;
    font-weight:1000;
}

.shopCoin{
    color:#ffd84d;
    font-size:20px;
    font-weight:900;
}

.sectionTitle{
    font-size:25px;
    font-weight:900;
    margin:22px 0 12px;
}

.shopGrid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:12px;
}

.shopItem{
    background:#152119;
    border:2px solid #304b35;
    border-radius:15px;
    padding:14px;
    text-align:center;
}

.shopEmoji{
    height:75px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:55px;
}

.shopName{
    font-size:16px;
    font-weight:900;
    margin:4px 0;
}

.shopDesc{
    font-size:12px;
    color:#9aaa9e;
    min-height:28px;
}

.shopPrice{
    color:#ffd84d;
    font-weight:bold;
    margin:8px;
}

.shopBtn{
    width:100%;
    height:38px;
    border-radius:8px;
    background:#315fc9;
    color:white;
    font-weight:bold;
}

.shopBtn.owned{
    background:#347548;
}

.shopBtn.equipped{
    background:#c28727;
}


/* =========================
   GAME
========================= */

#gameScreen{
    min-height:850px;
}

.gameHeader{
    width:720px;
    margin:auto;
    height:70px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 18px;
}

.scoreBox{
    font-size:19px;
    font-weight:900;
}

.bestBox{
    color:#ffd84d;
    font-size:18px;
    font-weight:900;
}

#gameWrapper{
    position:relative;
    width:680px;
    height:680px;
    margin:auto;
}

#board{
    position:absolute;
    left:20px;
    top:15px;
    width:640px;
    height:640px;
    border:10px solid #214e9c;
    border-radius:20px;
    overflow:hidden;

    background:
        linear-gradient(
            rgba(255,255,255,.045) 2px,
            transparent 2px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,.045) 2px,
            transparent 2px
        ),
        #75b93d;

    background-size:35px 35px;

    box-shadow:
        0 10px 25px rgba(0,0,0,.45),
        inset 0 0 20px rgba(0,0,0,.2);
}


/* =========================
   WORM
========================= */

#snakeSvg{
    position:absolute;
    inset:0;
    width:620px;
    height:620px;
    overflow:visible;
}

#snakeBody{
    fill:none;
    stroke:#315fc9;
    stroke-width:30;
    stroke-linecap:round;
    stroke-linejoin:round;
}

#snakeHighlight{
    fill:none;
    stroke:#9ab9ff;
    stroke-width:5;
    stroke-linecap:round;
    stroke-linejoin:round;
    opacity:.75;
    pointer-events:none;
}

#head{
    fill:#315fc9;
}

.eye{
    fill:white;
}

.pupil{
    fill:#111;
}

#normalMouth{
    fill:none;
    stroke:#111;
    stroke-width:4;
}

#openMouth{
    display:none;
}


/* =========================
   APPLE
========================= */

#apple{
    position:absolute;
    z-index:20;
    width:35px;
    height:35px;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:30px;

    animation:applePulse .65s infinite;
}

@keyframes applePulse{
    0%,100%{
        transform:scale(.85)
    }

    50%{
        transform:scale(1.13)
    }
}


/* =========================
   QUEST
========================= */

#questBox{
    position:absolute;
    z-index:100;
    right:20px;
    top:18px;
    width:190px;

    padding:10px 12px;

    border-radius:12px;

    background:rgba(0,0,0,.78);
    border:1px solid rgba(255,255,255,.15);

    font-size:12px;
}

.questTitle{
    color:#ffd84d;
    font-weight:900;
    font-size:14px;
    margin-bottom:5px;
}

.questReward{
    color:#ffd84d;
    margin-top:4px;
}


/* =========================
   SKILL
========================= */

#skillBox{
    position:absolute;
    z-index:100;
    left:20px;
    top:18px;

    padding:9px 12px;

    border-radius:12px;

    background:rgba(0,0,0,.78);

    font-size:12px;
}

.skillReady{
    color:#68e985;
    font-weight:bold;
}

.skillCool{
    color:#ffd84d;
    font-weight:bold;
}


/* =========================
   WIND
========================= */

.wind{
    position:absolute;
    z-index:150;

    height:4px;

    border-radius:4px;

    background:white;

    opacity:0;

    pointer-events:none;
}

.wind.active{
    animation:slash .25s linear infinite;
}

@keyframes slash{

    0%{
        opacity:0;
        transform:translateX(-40px) rotate(-15deg);
    }

    25%{
        opacity:.9;
    }

    100%{
        opacity:0;
        transform:translateX(80px) rotate(-15deg);
    }
}


/* =========================
   OVERLAY
========================= */

.overlay{
    display:none;

    position:absolute;
    z-index:500;

    inset:0;

    background:rgba(0,0,0,.82);

    justify-content:center;
    align-items:center;
}

.overlay.active{
    display:flex;
}

.overlayCard{
    width:450px;

    padding:38px;

    border-radius:25px;

    background:#101711;

    border:2px solid #3b4e3e;

    text-align:center;

    box-shadow:
        0 20px 50px rgba(0,0,0,.7);
}

.overlayCard h1{
    margin:0 0 30px;

    font-size:65px;

    font-weight:1000;
}

.pauseBtn,
.deathBtn{
    display:block;

    width:290px;
    height:55px;

    margin:11px auto;

    border-radius:12px;

    color:white;

    font-size:18px;

    font-weight:900;
}

.continueBtn{
    background:#315fc9;
}

.restartBtn{
    background:#38834c;
}

.mainBackBtn{
    background:#39423b;
}

.deathTitle{
    color:#ff4545;
}


/* =========================
   EFFECT
========================= */

#boom{
    display:none;

    position:absolute;

    z-index:450;

    font-size:80px;

    pointer-events:none;

    animation:boom .55s ease-out;
}

@keyframes boom{

    0%{
        transform:scale(.3);
        opacity:0;
    }

    40%{
        transform:scale(1.25);
        opacity:1;
    }

    100%{
        transform:scale(1);
        opacity:1;
    }
}

#notification{
    position:fixed;

    z-index:1000;

    left:50%;
    bottom:25px;

    transform:translateX(-50%);

    padding:13px 24px;

    border-radius:12px;

    background:#1c291e;

    border:2px solid #49624c;

    font-weight:900;

    display:none;
}

@media(max-width:780px){

    #app{
        transform:scale(.9);
        transform-origin:top center;
    }

}
</style>
</head>


<body>

<div id="app">


<!-- =========================
     MAIN
========================= -->

<section id="mainScreen" class="screen active">

    <div class="logo">
        🪱 WORM QUEST
    </div>

    <div class="logoSub">
        먹고 · 성장하고 · 질주하라
    </div>

    <div class="mainWorm" id="mainWorm">
        🪱
    </div>

    <div class="mainStats">

        <div class="mainStat">
            🪙 <span id="mainCoins">0</span>
        </div>

        <div class="mainStat">
            🏆 <span id="mainHigh">0</span>
        </div>

    </div>

    <button
        class="mainButton startButton"
        onclick="startGame()">

        🎮 게임 시작하기

    </button>

    <br>

    <button
        class="mainButton shopOpen"
        onclick="openShop()">

        🛒 상점

    </button>

</section>


<!-- =========================
     SHOP
========================= -->

<section id="shopScreen" class="screen">

    <div class="pageTop">

        <button
            class="back"
            onclick="showScreen('mainScreen')">

            ← 메인으로

        </button>

        <div class="pageTitle">
            🛒 상점
        </div>

        <div class="shopCoin">
            🪙 <span id="shopCoins">0</span>
        </div>

    </div>


    <div class="sectionTitle">
        🪱 지렁이 외형
    </div>

    <div
        class="shopGrid"
        id="wormShop">
    </div>


    <div class="sectionTitle">
        ⚡ 스킬 변경
    </div>

    <div
        class="shopGrid"
        id="skillShop">
    </div>

</section>


<!-- =========================
     GAME
========================= -->

<section id="gameScreen" class="screen">

    <div class="gameHeader">

        <div class="scoreBox">

            점수:
            <span id="score">0</span>

            &nbsp;&nbsp;

            🪙
            <span id="gameCoins">0</span>

        </div>

        <div class="bestBox">

            🏆 최고기록:
            <span id="gameHigh">0</span>

        </div>

    </div>


    <div id="gameWrapper">

        <div id="board">


            <!-- SKILL -->

            <div id="skillBox">

                ⚡
                <span id="skillName">
                    질주
                </span>

                <br>

                <span
                    id="skillStatus"
                    class="skillReady">

                    READY

                </span>

            </div>


            <!-- QUEST -->

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


            <!-- APPLE -->

            <div id="apple">
                🍎
            </div>


            <!-- SNAKE -->

            <svg
                id="snakeSvg"
                viewBox="0 0 620 620">

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


                    <path
                        id="normalMouth"
                        d="M12,-4 Q20,0 12,4">
                    </path>


                    <g id="openMouth">

                        <ellipse
                            cx="15"
                            cy="0"
                            rx="11"
                            ry="9"
                            fill="#111">
                        </ellipse>

                        <path
                            d="M8,3 Q15,12 22,3"
                            stroke="#ff5265"
                            stroke-width="3"
                            fill="none">
                        </path>

                    </g>

                </g>

            </svg>


            <!-- BOOM -->

            <div id="boom">
                💥
            </div>


            <!-- WIND -->

            <div
                class="wind"
                id="wind1"
                style="
                    left:100px;
                    top:250px;
                    width:100px
                ">
            </div>

            <div
                class="wind"
                id="wind2"
                style="
                    left:410px;
                    top:320px;
                    width:80px
                ">
            </div>

            <div
                class="wind"
                id="wind3"
                style="
                    left:160px;
                    top:410px;
                    width:90px
                ">
            </div>


            <!-- PAUSE -->

            <div
                id="pauseOverlay"
                class="overlay">

                <div class="overlayCard">

                    <h1>
                        일시정지
                    </h1>

                    <button
                        class="pauseBtn continueBtn"
                        onclick="continueGame()">

                        ▶️ 계속하기

                    </button>

                    <button
                        class="pauseBtn restartBtn"
                        onclick="restartGame()">

                        🔄 다시하기

                    </button>

                </div>

            </div>


            <!-- DEATH -->

            <div
                id="deathOverlay"
                class="overlay">

                <div class="overlayCard">

                    <h1 class="deathTitle">
                        YOU DIE
                    </h1>

                    <h2>

                        점수:
                        <span id="finalScore">
                            0
                        </span>

                    </h2>

                    <button
                        class="deathBtn restartBtn"
                        onclick="restartGame()">

                        🔄 다시하기

                    </button>

                    <button
                        class="deathBtn mainBackBtn"
                        onclick="showScreen('mainScreen')">

                        🏠 메인으로

                    </button>

                </div>

            </div>

        </div>

    </div>

</section>


<div id="notification"></div>

</div>


<script>

/* =========================================================
   DATA
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
        color:"#e34b32",
        price:500
    },

    lightning:{
        name:"번개 지렁이",
        emoji:"⚡",
        color:"#e4c52e",
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
        color:"#df4a45",
        price:2500
    }

};


const skills = {

    dash:{
        name:"질주",
        desc:"LShift 홀드",
        price:0
    },

    turbo:{
        name:"터보 질주",
        desc:"더 빠른 질주",
        price:700
    },

    wind:{
        name:"윈드 러너",
        desc:"강력한 바람 효과",
        price:1200
    },

    flash:{
        name:"플래시",
        desc:"최고속 질주",
        price:1800
    }

};


/* =========================================================
   STORAGE
========================================================= */

let coins =
    Number(
        localStorage.getItem("wormCoins") || 0
    );

let highScore =
    Number(
        localStorage.getItem("wormHighScore") || 0
    );

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


/* =========================================================
   QUEST DATA
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
        localStorage.getItem("wormQuests") || "null"
    );


function makeInitialQuests(){

    quests = [];

    const pool = [...questPool];

    for(let i=0;i<3;i++){

        const index =
            Math.floor(
                Math.random() * pool.length
            );

        quests.push({
            ...pool[index],
            progress:0
        });

        pool.splice(index,1);
    }

    saveQuests();
}


function saveQuests(){

    localStorage.setItem(
        "wormQuests",
        JSON.stringify(quests)
    );

}


if(
    !Array.isArray(quests) ||
    quests.length !== 3
){

    makeInitialQuests();

}


/* =========================================================
   UI
========================================================= */

function updateUI(){

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


function saveEverything(){

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
        JSON.stringify(ownedWorms)
    );

    localStorage.setItem(
        "skillOwned",
        JSON.stringify(ownedSkills)
    );

    saveQuests();

    updateUI();

}


function showScreen(id){

    document
        .querySelectorAll(".screen")
        .forEach(
            screen =>
                screen.classList.remove("active")
        );

    document
        .getElementById(id)
        .classList.add("active");

    updateUI();

    if(id === "shopScreen"){
        renderShop();
    }

}


function openShop(){

    showScreen("shopScreen");

}


/* =========================================================
   SHOP
========================================================= */

function renderShop(){

    let wormHTML = "";

    Object.entries(worms).forEach(
        ([id,worm]) => {

            const owned =
                ownedWorms.includes(id);

            const equipped =
                equippedWorm === id;

            let text =
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

                <div class="shopItem">

                    <div
                        class="shopEmoji"
                        style="color:${worm.color}">

                        ${worm.emoji}

                    </div>

                    <div class="shopName">
                        ${worm.name}
                    </div>

                    <div class="shopPrice">

                        ${
                            worm.price === 0
                            ? "무료"
                            : "🪙 " + worm.price
                        }

                    </div>

                    <button
                        class="shopBtn ${cls}"
                        onclick="buyWorm('${id}')">

                        ${text}

                    </button>

                </div>

            `;

        }
    );


    document.getElementById(
        "wormShop"
    ).innerHTML = wormHTML;


    let skillHTML = "";

    Object.entries(skills).forEach(
        ([id,skill]) => {

            const owned =
                ownedSkills.includes(id);

            const equipped =
                equippedSkill === id;

            let text =
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

                <div class="shopItem">

                    <div class="shopEmoji">
                        ⚡
                    </div>

                    <div class="shopName">
                        ${skill.name}
                    </div>

                    <div class="shopDesc">
                        ${skill.desc}
                    </div>

                    <div class="shopPrice">

                        ${
                            skill.price === 0
                            ? "무료"
                            : "🪙 " + skill.price
                        }

                    </div>

                    <button
                        class="shopBtn ${cls}"
                        onclick="buySkill('${id}')">

                        ${text}

                    </button>

                </div>

            `;

        }
    );


    document.getElementById(
        "skillShop"
    ).innerHTML = skillHTML;

}


function buyWorm(id){

    const item = worms[id];

    if(ownedWorms.includes(id)){

        equippedWorm = id;

        applyWorm();

        saveEverything();

        notify(
            item.name + " 장착!"
        );

        renderShop();

        return;

    }


    if(coins < item.price){

        notify(
            "🪙 코인이 부족합니다!"
        );

        return;

    }


    coins -= item.price;

    ownedWorms.push(id);

    equippedWorm = id;

    applyWorm();

    saveEverything();

    notify(
        item.name + " 구매 완료!"
    );

    renderShop();

}


function buySkill(id){

    const item = skills[id];

    if(ownedSkills.includes(id)){

        equippedSkill = id;

        saveEverything();

        notify(
            item.name + "으로 변경!"
        );

        renderShop();

        return;

    }


    if(coins < item.price){

        notify(
            "🪙 코인이 부족합니다!"
        );

        return;

    }


    coins -= item.price;

    ownedSkills.push(id);

    equippedSkill = id;

    saveEverything();

    notify(
        item.name + " 구매 완료!"
    );

    renderShop();

}


function applyWorm(){

    const color =
        worms[equippedWorm].color;

    document.getElementById(
        "snakeBody"
    ).style.stroke = color;

    document.getElementById(
        "head"
    ).style.fill = color;

}


/* =========================================================
   NOTIFICATION
========================================================= */

let notificationTimer = null;


function notify(text){

    const box =
        document.getElementById(
            "notification"
        );

    box.textContent = text;

    box.style.display = "block";

    clearTimeout(notificationTimer);

    notificationTimer =
        setTimeout(
            () => {

                box.style.display = "none";

            },
            1800
        );

}


/* =========================================================
   GAME VARIABLES
========================================================= */

const GRID = 18;
const CELL = 34;

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
    y:8
};

let score = 0;

let gameRunning = false;
let paused = false;
let dead = false;

let lastMoveTime = 0;

let dashActive = false;
let shiftHeld = false;

let dashStartTime = 0;
let lastDashTime = -10000;


/* ★ 재시작 시 중복 루프 방지 */
let gameLoopId = null;


/* =========================================================
   START / RESTART
========================================================= */

function startGame(){

    /* 기존 게임 루프 제거 */
    if(gameLoopId !== null){

        cancelAnimationFrame(gameLoopId);

        gameLoopId = null;

    }


    showScreen("gameScreen");


    snake = [

        {x:8,y:9},
        {x:7,y:9},
        {x:6,y:9},
        {x:5,y:9},
        {x:4,y:9}

    ];


    previousSnake =
        snake.map(
            point => ({...point})
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


    dashActive = false;
    shiftHeld = false;

    lastDashTime = -10000;


    document.getElementById(
        "score"
    ).textContent = "0";


    document.getElementById(
        "pauseOverlay"
    ).classList.remove("active");


    document.getElementById(
        "deathOverlay"
    ).classList.remove("active");


    document.getElementById(
        "boom"
    ).style.display = "none";


    /*
        ★★★★★★★★★★★★★★★★★★★★★★★
        새 게임마다 퀘스트 완전 초기화
        ★★★★★★★★★★★★★★★★★★★★★★★
    */

    makeInitialQuests();


    spawnApple();


    lastMoveTime =
        performance.now();


    applyWorm();


    updateQuestUI();


    render(1);


    gameLoopId =
        requestAnimationFrame(gameLoop);

}


function restartGame(){

    startGame();

}


/* =========================================================
   APPLE
========================================================= */

function spawnApple(){

    let valid = false;

    while(!valid){

        apple = {

            x:Math.floor(
                Math.random()*GRID
            ),

            y:Math.floor(
                Math.random()*GRID
            )

        };


        valid =
            !snake.some(
                point =>
                    point.x === apple.x &&
                    point.y === apple.y
            );

    }

}


/* =========================================================
   MOVEMENT
========================================================= */

function moveSnake(){

    if(
        !gameRunning ||
        paused ||
        dead
    ){

        return;

    }


    direction =
        {...nextDirection};


    const head =
        snake[0];


    const next = {

        x:
            head.x +
            direction.x,

        y:
            head.y +
            direction.y

    };


    if(
        next.x < 0 ||
        next.x >= GRID ||
        next.y < 0 ||
        next.y >= GRID
    ){

        die(next);

        return;

    }


    /*
        자기 몸 충돌
    */

    const hitSelf =
        snake.some(
            point =>
                point.x === next.x &&
                point.y === next.y
        );


    if(hitSelf){

        die(next);

        return;

    }


    previousSnake =
        snake.map(
            point => ({...point})
        );


    snake.unshift(next);


    if(
        next.x === apple.x &&
        next.y === apple.y
    ){

        score++;


        document.getElementById(
            "score"
        ).textContent = score;


        spawnApple();


        updateQuestProgress();


    }else{

        snake.pop();

    }


    lastMoveTime =
        performance.now();

}


/* =========================================================
   SMOOTH WORM RENDER
========================================================= */

function lerp(a,b,t){

    return a + (b-a)*t;

}


function ease(t){

    return t < .5

        ? 2*t*t

        : 1-Math.pow(
            -2*t+2,
            2
        )/2;

}


/*
    몸통을 자연스럽게 연결하는
    Catmull-Rom 곡선
*/

function catmullRom(
    p0,
    p1,
    p2,
    p3,
    t
){

    const t2 = t*t;
    const t3 = t2*t;


    return {

        x:
            0.5 * (

                (2*p1.x)

                +

                (-p0.x+p2.x)*t

                +

                (
                    2*p0.x
                    -5*p1.x
                    +4*p2.x
                    -p3.x
                )*t2

                +

                (
                    -p0.x
                    +3*p1.x
                    -3*p2.x
                    +p3.x
                )*t3

            ),


        y:
            0.5 * (

                (2*p1.y)

                +

                (-p0.y+p2.y)*t

                +

                (
                    2*p0.y
                    -5*p1.y
                    +4*p2.y
                    -p3.y
                )*t2

                +

                (
                    -p0.y
                    +3*p1.y
                    -3*p2.y
                    +p3.y
                )*t3

            )

    };

}


/*
    여러 점을 부드러운 곡선으로 연결
*/

function createSmoothPath(points){

    if(points.length === 0){

        return "";

    }


    if(points.length === 1){

        return `
            M
            ${points[0].x}
            ${points[0].y}
        `;

    }


    let path =
        `M ${points[0].x} ${points[0].y}`;


    for(
        let i=0;
        i<points.length-1;
        i++
    ){

        const p0 =
            points[
                Math.max(0,i-1)
            ];

        const p1 =
            points[i];

        const p2 =
            points[i+1];

        const p3 =
            points[
                Math.min(
                    points.length-1,
                    i+2
                )
            ];


        /*
            한 칸을 여러 구간으로 나눠서
            곡선을 더 부드럽게 만듦
        */

        for(let j=1;j<=6;j++){

            const t = j/6;

            const p =
                catmullRom(
                    p0,
                    p1,
                    p2,
                    p3,
                    t
                );


            path +=
                ` L ${p.x.toFixed(2)} ${p.y.toFixed(2)}`;

        }

    }


    return path;

}


/* =========================================================
   RENDER
========================================================= */

function render(progress){

    if(snake.length === 0){

        return;

    }


    const t =
        ease(
            Math.max(
                0,
                Math.min(
                    1,
                    progress
                )
            )
        );


    /*
        각 몸통 위치를 부드럽게 보간
    */

    const points =
        snake.map(
            (point,index) => {

                const old =
                    previousSnake[index] ||
                    point;


                return {

                    x:
                        lerp(
                            old.x,
                            point.x,
                            t
                        ) * CELL + 17,

                    y:
                        lerp(
                            old.y,
                            point.y,
                            t
                        ) * CELL + 17

                };

            }
        );


    /*
        곡선 몸통
    */

    const path =
        createSmoothPath(points);


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


    /*
        머리
    */

    const head =
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
            ${head.x}
            ${head.y}
        )
        rotate(${angle})
        `
    );


    /*
        사과
    */

    const appleElement =
        document.getElementById(
            "apple"
        );


    appleElement.style.left =
        (apple.x*CELL) + "px";

    appleElement.style.top =
        (apple.y*CELL) + "px";


    /*
        사과 가까이 가면 입 벌림
    */

    const distance =
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


    if(distance <= 2){

        document.getElementById(
            "normalMouth"
        ).style.display = "none";


        document.getElementById(
            "openMouth"
        ).style.display = "block";

    }else{

        document.getElementById(
            "normalMouth"
        ).style.display = "block";


        document.getElementById(
            "openMouth"
        ).style.display = "none";

    }

}


/* =========================================================
   GAME LOOP
========================================================= */

function gameLoop(time){

    if(
        !gameRunning ||
        dead
    ){

        gameLoopId = null;

        return;

    }


    if(!paused){

        const normalSpeed = 150;


        const moveSpeed =
            dashActive
            ? getDashSpeed()
            : normalSpeed;


        const elapsed =
            time -
            lastMoveTime;


        const progress =
            Math.min(
                elapsed /
                moveSpeed,
                1
            );


        render(progress);


        if(
            elapsed >= moveSpeed
        ){

            moveSnake();

        }


        updateDash();

    }


    /*
        ★ 기존 루프와 겹치지 않게
        현재 루프 ID를 계속 저장
    */

    gameLoopId =
        requestAnimationFrame(
            gameLoop
        );

}


/* =========================================================
   DASH
========================================================= */

function getDashSpeed(){

    if(equippedSkill === "turbo")
        return 50;

    if(equippedSkill === "wind")
        return 42;

    if(equippedSkill === "flash")
        return 32;

    return 65;

}


function activateDash(){

    if(
        !gameRunning ||
        paused ||
        dead ||
        dashActive
    ){

        return;

    }


    const now =
        performance.now();


    if(
        now-lastDashTime < 10000
    ){

        return;

    }


    dashActive = true;

    dashStartTime = now;

    lastDashTime = now;


    document
        .querySelectorAll(".wind")
        .forEach(
            element =>
                element.classList.add("active")
        );

}


function updateDash(){

    const now =
        performance.now();


    /*
        SHIFT를 떼면 종료
    */

    if(
        dashActive &&
        !shiftHeld
    ){

        dashActive = false;

        stopWind();

    }


    /*
        최대 2초
    */

    if(
        dashActive &&
        now-dashStartTime >= 2000
    ){

        dashActive = false;

        stopWind();

    }


    const status =
        document.getElementById(
            "skillStatus"
        );


    const cooldown =
        10000 -
        (now-lastDashTime);


    if(
        lastDashTime < 0 ||
        cooldown <= 0
    ){

        status.textContent =
            "READY";

        status.className =
            "skillReady";

    }else if(dashActive){

        status.textContent =
            "🔥 질주 중!";

        status.className =
            "skillReady";

    }else{

        status.textContent =
            Math.ceil(
                cooldown/1000
            ) + "초";

        status.className =
            "skillCool";

    }

}


function stopWind(){

    document
        .querySelectorAll(".wind")
        .forEach(
            element =>
                element.classList.remove("active")
        );

}


/* =========================================================
   DEATH
========================================================= */

function die(position){

    dead = true;

    gameRunning = false;

    dashActive = false;

    stopWind();


    /*
        현재 애니메이션 루프 종료
    */

    if(gameLoopId !== null){

        cancelAnimationFrame(
            gameLoopId
        );

        gameLoopId = null;

    }


    if(score > highScore){

        highScore = score;

        localStorage.setItem(
            "wormHighScore",
            highScore
        );

    }


    const boom =
        document.getElementById(
            "boom"
        );


    const safeX =
        Math.max(
            0,
            Math.min(
                GRID-1,
                position.x
            )
        );


    const safeY =
        Math.max(
            0,
            Math.min(
                GRID-1,
                position.y
            )
        );


    boom.style.left =
        (safeX*CELL+255) +
        "px";


    boom.style.top =
        (safeY*CELL+170) +
        "px";


    boom.style.display =
        "block";


    setTimeout(
        () => {

            document.getElementById(
                "finalScore"
            ).textContent =
                score;


            document.getElementById(
                "deathOverlay"
            ).classList.add(
                "active"
            );


            updateUI();

        },
        550
    );

}


/* =========================================================
   PAUSE
========================================================= */

function pauseGame(){

    if(
        !gameRunning ||
        dead
    ){

        return;

    }


    paused = true;


    document.getElementById(
        "pauseOverlay"
    ).classList.add(
        "active"
    );

}


function continueGame(){

    if(dead){

        return;

    }


    paused = false;


    document.getElementById(
        "pauseOverlay"
    ).classList.remove(
        "active"
    );


    lastMoveTime =
        performance.now();


    /*
        이미 실행 중인 루프가 없을 때만 시작
    */

    if(gameLoopId === null){

        gameLoopId =
            requestAnimationFrame(
                gameLoop
            );

    }

}


/* =========================================================
   KEYBOARD
========================================================= */

document.addEventListener(
    "keydown",
    event => {


        /*
            ESC
            일시정지 / 계속하기
        */

        if(event.code === "Escape"){

            event.preventDefault();


            if(
                document
                    .getElementById(
                        "gameScreen"
                    )
                    .classList.contains(
                        "active"
                    )
            ){

                if(paused){

                    continueGame();

                }else{

                    pauseGame();

                }

            }


            return;

        }


        /*
            ★★★★★★★★★★★★★
            R = 다시하기
            ★★★★★★★★★★★★★
        */

        if(
            event.key.toLowerCase() === "r"
        ){

            event.preventDefault();


            if(
                document
                    .getElementById(
                        "gameScreen"
                    )
                    .classList.contains(
                        "active"
                    )
            ){

                restartGame();

            }


            return;

        }


        /*
            왼쪽 SHIFT = 질주
        */

        if(
            event.code === "ShiftLeft"
        ){

            event.preventDefault();


            if(!shiftHeld){

                shiftHeld = true;

                activateDash();

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


        const key =
            event.key.toLowerCase();


        /*
            W / ↑
        */

        if(

            (
                key === "w" ||
                key === "arrowup"
            )

            &&

            direction.y !== 1

        ){

            nextDirection = {
                x:0,
                y:-1
            };

        }


        /*
            S / ↓
        */

        if(

            (
                key === "s" ||
                key === "arrowdown"
            )

            &&

            direction.y !== -1

        ){

            nextDirection = {
                x:0,
                y:1
            };

        }


        /*
            A / ←
        */

        if(

            (
                key === "a" ||
                key === "arrowleft"
            )

            &&

            direction.x !== 1

        ){

            nextDirection = {
                x:-1,
                y:0
            };

        }


        /*
            D / →
        */

        if(

            (
                key === "d" ||
                key === "arrowright"
            )

            &&

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
   KEYUP
========================================================= */

document.addEventListener(
    "keyup",
    event => {

        if(
            event.code === "ShiftLeft"
        ){

            shiftHeld = false;


            if(dashActive){

                dashActive = false;

                stopWind();

            }

        }

    }
);


/* =========================================================
   QUEST SYSTEM
========================================================= */

function updateQuestProgress(){

    quests.forEach(
        quest => {


            if(
                quest.type === "apple" ||
                quest.type === "score"
            ){

                quest.progress =
                    score;

            }


            if(
                quest.type === "length"
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
                    Number(
                        quest.reward
                    ),
                    200
                );


            coins += reward;


            notify(
                "🎉 퀘스트 완료! +" +
                reward +
                " 🪙"
            );


            /*
                완료된 퀘스트와
                겹치지 않는 새 퀘스트 찾기
            */

            let available =
                questPool.filter(
                    candidate =>
                        !quests.some(
                            current =>

                                current.type ===
                                candidate.type

                                &&

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


            saveEverything();


            /*
                한 번에 하나만 완료
            */

            break;

        }

    }

}


function updateQuestUI(){

    if(
        !Array.isArray(quests) ||
        quests.length === 0
    ){

        return;

    }


    /*
        아직 완료되지 않은
        첫 번째 퀘스트 표시
    */

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


    const progress =
        Math.min(
            quest.progress,
            quest.target
        );


    document.getElementById(
        "questText"
    ).textContent =

        quest.text +
        " " +
        progress +
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
   INITIALIZE
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
