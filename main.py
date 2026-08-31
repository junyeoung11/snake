import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

st.markdown("""
<style>
.block-container {
    max-width: 950px;
    padding-top: 1rem;
}
header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("🪱 지렁이 게임")
st.caption("🎮 WASD 또는 방향키로 이동하세요!")

components.html("""
<!DOCTYPE html>
<html lang="ko">

<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #183b20;
    font-family: Arial, sans-serif;
    overflow: hidden;
}


/* 🌲 전체 배경 */

#container {

    width: 780px;
    height: 780px;

    margin: auto;

    position: relative;

    overflow: hidden;

    border-radius: 25px;

    background:

        radial-gradient(circle at 10% 10%, #609b42, transparent 20%),
        radial-gradient(circle at 90% 15%, #356e30, transparent 22%),
        radial-gradient(circle at 15% 90%, #4b8338, transparent 25%),
        radial-gradient(circle at 90% 90%, #315f2e, transparent 25%),

        #24542b;

    box-shadow:
        0 0 35px rgba(0,0,0,.7);
}


/* 🌳 나무 */

.tree {

    position: absolute;

    width: 115px;
    height: 115px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle at 30% 25%,
            #96d456,
            #4e9038 45%,
            #1b5028 75%
        );

    box-shadow:

        inset -10px -12px 20px rgba(0,0,0,.25),

        0 10px 15px rgba(0,0,0,.4);

}


/* 🟩 게임판 */

#game {

    position: absolute;

    width: 648px;
    height: 648px;

    left: 66px;
    top: 66px;

    border: 18px solid #254da5;

    border-radius: 20px;

    overflow: hidden;

    background:

        linear-gradient(
            90deg,
            rgba(0,0,0,.07) 1px,
            transparent 1px
        ),

        linear-gradient(
            rgba(0,0,0,.07) 1px,
            transparent 1px
        ),

        radial-gradient(
            circle at center,
            #7abb4d,
            #4e9135
        );

    background-size:
        34px 34px;

    box-shadow:

        inset 0 0 30px rgba(0,0,0,.3),

        0 8px 20px rgba(0,0,0,.5);

}


/* 🏆 점수 */

#scoreBox {

    position: absolute;

    top: 20px;
    left: 20px;

    z-index: 50;

    padding: 12px 20px;

    background: rgba(0,0,0,.78);

    border-radius: 15px;

    color: white;

    font-size: 21px;

    font-weight: bold;

}


#bestBox {

    position: absolute;

    top: 20px;
    right: 20px;

    z-index: 50;

    padding: 12px 20px;

    background: rgba(0,0,0,.78);

    border-radius: 15px;

    color: white;

    font-size: 20px;

    font-weight: bold;

}


/* 🍎 사과 */

#food {

    position: absolute;

    width: 34px;
    height: 34px;

    display: flex;

    justify-content: center;
    align-items: center;

    font-size: 31px;

    z-index: 20;

    filter:
        drop-shadow(0 4px 3px rgba(0,0,0,.4));

}


/* ===================================
   🪱 부드러운 지렁이 몸
=================================== */

#snakeSVG {

    position: absolute;

    width: 100%;
    height: 100%;

    left: 0;
    top: 0;

    pointer-events: none;

    overflow: visible;

}


/* 몸 그림자 */

#snakeShadow {

    fill: none;

    stroke: #10255a;

    stroke-width: 42;

    stroke-linecap: round;

    stroke-linejoin: round;

    opacity: .5;

}


/* 메인 몸 */

#snakeBody {

    fill: none;

    stroke: #2958c4;

    stroke-width: 36;

    stroke-linecap: round;

    stroke-linejoin: round;

}


/* 밝은 하이라이트 */

#snakeLight {

    fill: none;

    stroke: #6794ff;

    stroke-width: 8;

    stroke-linecap: round;

    stroke-linejoin: round;

    opacity: .65;

}


/* ===================================
   🪱 새 머리 디자인
=================================== */

#head {

    position: absolute;

    width: 54px;
    height: 50px;

    border-radius:

        50%
        50%
        45%
        45%;

    background:

        radial-gradient(
            ellipse at 30% 25%,

            #7fa3ff,

            #3969d3 45%,

            #183c94 80%
        );

    border:

        3px solid #173778;

    z-index: 40;

    transform:
        translate(-50%, -50%);

    box-shadow:

        inset 7px 7px 12px rgba(255,255,255,.22),

        inset -7px -8px 12px rgba(0,0,0,.25),

        0 7px 10px rgba(0,0,0,.4);

    transition:

        left .12s linear,

        top .12s linear;

}


/* 👀 눈 - 머리 위쪽에 자연스럽게 */

.eye {

    position: absolute;

    width: 20px;
    height: 23px;

    background: #f8fbff;

    border-radius: 50%;

    top: -7px;

    border:

        2px solid rgba(20,40,90,.35);

    box-shadow:

        0 2px 3px rgba(0,0,0,.25);

}


.eye.left {

    left: 7px;

}


.eye.right {

    right: 7px;

}


/* 눈동자 */

.pupil {

    position: absolute;

    width: 9px;
    height: 11px;

    background: #101b3a;

    border-radius: 50%;

    left: 5px;
    top: 7px;

}


/* 눈 반짝임 */

.pupil::after {

    content: "";

    position: absolute;

    width: 3px;
    height: 3px;

    background: white;

    border-radius: 50%;

    top: 2px;
    left: 2px;

}


/* 💥 충돌 */

#crash {

    position: absolute;

    display: none;

    font-size: 80px;

    z-index: 100;

    transform:
        translate(-50%, -50%);

}


.crashAnim {

    animation:
        boom .6s ease-out forwards;

}


@keyframes boom {

    0% {
        transform:
            translate(-50%, -50%)
            scale(.2)
            rotate(-30deg);

        opacity: 0;
    }

    45% {
        transform:
            translate(-50%, -50%)
            scale(1.5)
            rotate(20deg);

        opacity: 1;
    }

    100% {
        transform:
            translate(-50%, -50%)
            scale(1)
            rotate(0deg);

        opacity: 1;
    }

}


.shake {

    animation:
        shake .45s;

}


@keyframes shake {

    0%, 100% {
        transform: translate(0,0);
    }

    20% {
        transform: translate(-10px,5px);
    }

    40% {
        transform: translate(10px,-5px);
    }

    60% {
        transform: translate(-8px,4px);
    }

    80% {
        transform: translate(8px,-3px);
    }

}


/* 💀 게임오버 */

#gameOver {

    position: absolute;

    width: 390px;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%);

    background:
        rgba(0,0,0,.85);

    border:
        2px solid #547de5;

    border-radius: 20px;

    padding: 25px;

    text-align: center;

    color: white;

    display: none;

    z-index: 200;

}


#gameOver h1 {

    color: #ff6257;

}


#help {

    position: absolute;

    bottom: 15px;

    left: 50%;

    transform: translateX(-50%);

    background:
        rgba(0,0,0,.72);

    color: white;

    padding:
        10px 22px;

    border-radius: 15px;

    z-index: 60;

}

</style>

</head>

<body>

<div id="container">


    <!-- 🌲 나무 -->

    <div class="tree" style="left:-40px;top:-30px;"></div>
    <div class="tree" style="left:100px;top:-50px;"></div>
    <div class="tree" style="left:250px;top:-45px;"></div>
    <div class="tree" style="left:430px;top:-50px;"></div>
    <div class="tree" style="left:620px;top:-30px;"></div>

    <div class="tree" style="left:-60px;top:160px;"></div>
    <div class="tree" style="left:-60px;top:360px;"></div>
    <div class="tree" style="left:-60px;top:570px;"></div>

    <div class="tree" style="right:-60px;top:150px;"></div>
    <div class="tree" style="right:-60px;top:350px;"></div>
    <div class="tree" style="right:-60px;top:560px;"></div>

    <div class="tree" style="left:60px;bottom:-55px;"></div>
    <div class="tree" style="left:230px;bottom:-60px;"></div>
    <div class="tree" style="left:430px;bottom:-60px;"></div>
    <div class="tree" style="left:610px;bottom:-55px;"></div>


    <!-- 점수 -->

    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>

    <div id="bestBox">
        ❤️ 최고: <span id="best">0</span>
    </div>


    <!-- 게임 -->

    <div id="game">


        <div id="food">🍎</div>


        <!-- 🪱 몸 -->

        <svg id="snakeSVG">

            <path
                id="snakeShadow"
            />

            <path
                id="snakeBody"
            />

            <path
                id="snakeLight"
            />

        </svg>


        <!-- 🪱 자연스러운 얼굴 -->

        <div id="head">

            <div class="eye left">
                <div class="pupil"></div>
            </div>

            <div class="eye right">
                <div class="pupil"></div>
            </div>

        </div>


        <div id="crash">💥</div>

    </div>


    <!-- 게임오버 -->

    <div id="gameOver">

        <h1>💀 게임 오버!</h1>

        <h2>
            최종 점수:
            <span id="finalScore">0</span>
        </h2>

        <p>R 키를 눌러 다시 시작하세요!</p>

    </div>


    <div id="help">
        🎮 WASD 또는 방향키로 이동
    </div>


</div>


<script>


const GRID = 34;

const COLS = 18;
const ROWS = 18;


const game =
    document.getElementById("game");

const headElement =
    document.getElementById("head");

const foodElement =
    document.getElementById("food");

const scoreElement =
    document.getElementById("score");

const bestElement =
    document.getElementById("best");

const crashElement =
    document.getElementById("crash");

const gameOverElement =
    document.getElementById("gameOver");

const finalScoreElement =
    document.getElementById("finalScore");

const snakeBody =
    document.getElementById("snakeBody");

const snakeShadow =
    document.getElementById("snakeShadow");

const snakeLight =
    document.getElementById("snakeLight");


let snake = [];

let direction = {x: 1, y: 0};

let nextDirection = {x: 1, y: 0};

let food;

let score = 0;

let best = 0;

let gameOver = false;


/* 🪱 시작 몸 */

function resetSnake() {

    snake = [

        {x: 8, y: 9},
        {x: 7, y: 9},
        {x: 6, y: 9},
        {x: 5, y: 9},
        {x: 4, y: 9},
        {x: 3, y: 9}

    ];

}


/* 🍎 사과 하나 생성 */

function createFood() {

    let valid = false;

    while (!valid) {

        food = {

            x: Math.floor(Math.random() * COLS),

            y: Math.floor(Math.random() * ROWS)

        };


        valid = !snake.some(part =>

            part.x === food.x &&
            part.y === food.y

        );

    }

}


/* 🪱 몸을 곡선으로 그리기 */

function createSmoothPath() {

    const points =
        [...snake]
        .reverse()
        .map(part => ({

            x:
                part.x * GRID + GRID / 2,

            y:
                part.y * GRID + GRID / 2

        }));


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

        const current =
            points[i];

        const next =
            points[i + 1];


        const midX =
            (current.x + next.x) / 2;

        const midY =
            (current.y + next.y) / 2;


        path +=
            ` Q ${current.x} ${current.y}
              ${midX} ${midY}`;

    }


    const last =
        points[points.length - 1];


    path +=
        ` L ${last.x} ${last.y}`;


    return path;

}


/* 🎨 화면 */

function render() {

    const path =
        createSmoothPath();


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


    const head =
        snake[0];


    const headX =
        head.x * GRID + GRID / 2;

    const headY =
        head.y * GRID + GRID / 2;


    headElement.style.left =
        headX + "px";

    headElement.style.top =
        headY + "px";


    /* 이동 방향 */

    let angle = 0;


    if (direction.x === 1) {
        angle = 90;
    }

    else if (direction.x === -1) {
        angle = -90;
    }

    else if (direction.y === 1) {
        angle = 180;
    }

    else {
        angle = 0;
    }


    headElement.style.transform =
        `translate(-50%, -50%)
         rotate(${angle}deg)`;


    /* 🍎 */

    foodElement.style.left =
        food.x * GRID + "px";

    foodElement.style.top =
        food.y * GRID + "px";


    scoreElement.textContent =
        score;

    bestElement.textContent =
        best;

}


/* ⌨️ 조작 */

document.addEventListener(
    "keydown",

    event => {

        const key =
            event.key.toLowerCase();


        if (

            [
                "w","a","s","d",
                "arrowup",
                "arrowdown",
                "arrowleft",
                "arrowright"
            ].includes(key)

        ) {

            event.preventDefault();

        }


        if (
            (key === "w" ||
             key === "arrowup")

            && direction.y !== 1
        ) {

            nextDirection =
                {x: 0, y: -1};

        }


        if (
            (key === "s" ||
             key === "arrowdown")

            && direction.y !== -1
        ) {

            nextDirection =
                {x: 0, y: 1};

        }


        if (
            (key === "a" ||
             key === "arrowleft")

            && direction.x !== 1
        ) {

            nextDirection =
                {x: -1, y: 0};

        }


        if (
            (key === "d" ||
             key === "arrowright")

            && direction.x !== -1
        ) {

            nextDirection =
                {x: 1, y: 0};

        }


        if (
            key === "r" &&
            gameOver
        ) {

            restartGame();

        }

    }
);


/* 🪱 한 칸 이동 */

function move() {

    if (gameOver) return;


    direction =
        nextDirection;


    const head =
        snake[0];


    const newHead = {

        x:
            head.x + direction.x,

        y:
            head.y + direction.y

    };


    /* 💥 벽 */

    if (

        newHead.x < 0 ||
        newHead.x >= COLS ||

        newHead.y < 0 ||
        newHead.y >= ROWS

    ) {

        crash(head.x, head.y);

        return;

    }


    /* 💥 몸 */

    if (

        snake.some(part =>

            part.x === newHead.x &&
            part.y === newHead.y

        )

    ) {

        crash(
            newHead.x,
            newHead.y
        );

        return;

    }


    snake.unshift(newHead);


    /* 🍎 먹기 */

    if (

        newHead.x === food.x &&
        newHead.y === food.y

    ) {

        score++;


        if (score > best) {

            best = score;

        }


        /* 꼬리를 안 없애서 길어짐 */

        createFood();

    }

    else {

        snake.pop();

    }


    render();

}


/* 💥 충돌 */

function crash(x, y) {

    gameOver = true;


    crashElement.style.left =
        (x * GRID + GRID / 2) + "px";

    crashElement.style.top =
        (y * GRID + GRID / 2) + "px";


    crashElement.style.display =
        "block";


    crashElement.classList.remove(
        "crashAnim"
    );

    void crashElement.offsetWidth;

    crashElement.classList.add(
        "crashAnim"
    );


    game.classList.add("shake");


    setTimeout(() => {

        game.classList.remove("shake");

    }, 500);


    setTimeout(() => {

        finalScoreElement.textContent =
            score;

        gameOverElement.style.display =
            "block";

    }, 600);

}


/* 🔄 재시작 */

function restartGame() {

    score = 0;

    gameOver = false;

    direction =
        {x: 1, y: 0};

    nextDirection =
        {x: 1, y: 0};


    crashElement.style.display =
        "none";

    gameOverElement.style.display =
        "none";


    resetSnake();

    createFood();

    render();

}


/* 🚀 시작 */

resetSnake();

createFood();

render();


setInterval(
    move,
    160
);


</script>

</body>
</html>
""", height=820)
