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
st.caption("WASD 또는 방향키로 이동하세요! 🎮")

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
    background: #17351c;
    font-family: Arial, sans-serif;
    overflow: hidden;
}


/* =========================
   🌲 전체 숲
========================= */

#container {

    width: 780px;
    height: 780px;

    margin: auto;

    position: relative;

    overflow: hidden;

    border-radius: 25px;

    background:

        radial-gradient(circle at 10% 10%, #5a963d, transparent 20%),
        radial-gradient(circle at 90% 15%, #396f32, transparent 22%),
        radial-gradient(circle at 15% 90%, #467f36, transparent 25%),
        radial-gradient(circle at 90% 90%, #315f2d, transparent 25%),

        #245128;

    box-shadow:
        0 0 35px rgba(0,0,0,.7);

}


/* =========================
   🌳 나무
========================= */

.tree {

    position: absolute;

    width: 110px;
    height: 110px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle at 30% 25%,
            #91cf52,
            #4d8c36 45%,
            #1d5428 75%
        );

    box-shadow:

        inset -10px -12px 20px rgba(0,0,0,.25),

        0 10px 15px rgba(0,0,0,.4);

}


.tree::after {

    content: "";

    position: absolute;

    width: 30px;
    height: 55px;

    background: #70421f;

    border-radius: 15px;

    left: 40px;
    top: 85px;

    z-index: -1;

}


/* =========================
   🟩 게임 맵
========================= */

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
            #79b94b,
            #4f9134
        );

    background-size:
        34px 34px;

    box-shadow:

        inset 0 0 30px rgba(0,0,0,.3),

        0 8px 20px rgba(0,0,0,.5);

}


/* =========================
   🏆 점수
========================= */

#scoreBox {

    position: absolute;

    top: 20px;
    left: 20px;

    z-index: 50;

    padding: 12px 20px;

    background: rgba(0,0,0,.78);

    border: 2px solid rgba(100,180,255,.5);

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

    border: 2px solid rgba(255,220,80,.5);

    border-radius: 15px;

    color: white;

    font-size: 20px;

    font-weight: bold;

}


/* =========================
   🍎 사과
========================= */

#food {

    position: absolute;

    width: 34px;
    height: 34px;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 31px;

    z-index: 20;

    filter:

        drop-shadow(0 4px 3px rgba(0,0,0,.4));

}


/* =========================
   🪱 SVG 몸통
========================= */

#snakeSVG {

    position: absolute;

    inset: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;

    overflow: visible;

}


/* =========================
   🪱 머리
========================= */

#head {

    position: absolute;

    width: 44px;
    height: 44px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle at 30% 25%,
            #7198ff,
            #315fc5 50%,
            #183b91
        );

    border: 3px solid #173779;

    z-index: 30;

    transform:
        translate(-50%, -50%);

    box-shadow:

        inset 6px 6px 10px rgba(255,255,255,.25),

        inset -6px -7px 10px rgba(0,0,0,.25),

        0 5px 8px rgba(0,0,0,.4);

    transition:

        left .12s linear,

        top .12s linear;

}


/* 👀 눈 */

.eye {

    position: absolute;

    width: 15px;
    height: 18px;

    background: white;

    border-radius: 50%;

    top: 5px;

    box-shadow:
        0 2px 3px rgba(0,0,0,.3);

}


.eye.left {
    left: 6px;
}

.eye.right {
    right: 6px;
}


/* 👁 눈동자 */

.pupil {

    position: absolute;

    width: 7px;
    height: 8px;

    border-radius: 50%;

    background: #111;

    left: 4px;
    top: 6px;

}


/* =========================
   💥 충돌
========================= */

#crash {

    position: absolute;

    display: none;

    font-size: 80px;

    z-index: 100;

    transform: translate(-50%, -50%);

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

    40% {
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


/* =========================
   💀 게임 오버
========================= */

#gameOver {

    position: absolute;

    width: 390px;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%);

    background:
        rgba(0,0,0,.83);

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
        rgba(0,0,0,.7);

    color: white;

    padding:
        10px 22px;

    border-radius: 15px;

    z-index: 60;

}


</style>

</head>


<body>

<div id="container" tabindex="0">


    <!-- 🌲 숲 -->

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


    <!-- 🏆 점수 -->

    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>


    <div id="bestBox">
        ❤️ 최고: <span id="best">0</span>
    </div>


    <!-- 🟩 게임판 -->

    <div id="game">


        <!-- 🍎 사과 -->

        <div id="food">🍎</div>


        <!-- 🪱 부드러운 몸 -->

        <svg id="snakeSVG">

            <!-- 그림자 -->

            <path
                id="snakeShadow"
                fill="none"
                stroke="#142d66"
                stroke-width="34"
                stroke-linecap="round"
                stroke-linejoin="round"
                opacity=".55"
            />

            <!-- 몸통 -->

            <path
                id="snakeBody"
                fill="none"
                stroke="#2859c9"
                stroke-width="28"
                stroke-linecap="round"
                stroke-linejoin="round"
            />

            <!-- 몸통 하이라이트 -->

            <path
                id="snakeLight"
                fill="none"
                stroke="#5f8cff"
                stroke-width="7"
                stroke-linecap="round"
                stroke-linejoin="round"
                opacity=".55"
            />

        </svg>


        <!-- 🪱 머리 -->

        <div id="head">

            <div class="eye left">
                <div class="pupil"></div>
            </div>

            <div class="eye right">
                <div class="pupil"></div>
            </div>

        </div>


        <!-- 💥 -->

        <div id="crash">💥</div>


    </div>


    <!-- 💀 게임오버 -->

    <div id="gameOver">

        <h1>💀 게임 오버!</h1>

        <h2>
            최종 점수:
            <span id="finalScore">0</span>
        </h2>

        <p>
            R 키를 눌러 다시 시작하세요!
        </p>

    </div>


    <div id="help">
        🎮 WASD 또는 방향키로 이동
    </div>


</div>


<script>


/* =========================
   ⚙️ 게임 설정
========================= */

const GRID = 34;

const COLS = 18;
const ROWS = 18;

const SIZE = GRID * COLS;


/* =========================
   HTML 요소
========================= */

const container =
    document.getElementById("container");

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


/* =========================
   🎮 게임 데이터
========================= */

let snake = [];

let direction = { x: 1, y: 0 };

let nextDirection = { x: 1, y: 0 };

let food = { x: 12, y: 8 };

let score = 0;

let best = 0;

let gameOver = false;


/* =========================
   🪱 시작
========================= */

function resetSnake() {

    snake = [

        { x: 8, y: 9 },
        { x: 7, y: 9 },
        { x: 6, y: 9 },
        { x: 5, y: 9 },
        { x: 4, y: 9 },
        { x: 3, y: 9 }

    ];

}


/* =========================
   🍎 사과 생성
========================= */

function createFood() {

    let valid = false;

    while (!valid) {

        food = {

            x:
                Math.floor(
                    Math.random() * COLS
                ),

            y:
                Math.floor(
                    Math.random() * ROWS
                )

        };

        valid = !snake.some(part =>

            part.x === food.x &&
            part.y === food.y

        );

    }

}


/* =========================
   🪱 부드러운 몸 SVG
========================= */

function createSmoothPath() {

    /*
    snake 배열은
    머리 → 꼬리 순서

    SVG는 꼬리 → 머리로 그린다
    */

    const points =
        [...snake].reverse().map(part => ({

            x:
                part.x * GRID + GRID / 2,

            y:
                part.y * GRID + GRID / 2

        }));


    if (points.length < 2) return "";


    let path =
        `M ${points[0].x} ${points[0].y}`;


    /*
    점과 점 사이를
    곡선으로 연결
    */

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


/* =========================
   🎨 화면 업데이트
========================= */

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


    /* 🪱 머리 */

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


    /* 방향에 따라 머리 회전 */

    let angle = 0;


    if (direction.x === 1) {
        angle = 90;
    }

    else if (direction.x === -1) {
        angle = -90;
    }

    else if (direction.y === -1) {
        angle = 0;
    }

    else if (direction.y === 1) {
        angle = 180;
    }


    headElement.style.transform =
        `translate(-50%, -50%) rotate(${angle}deg)`;


    /* 🍎 사과 */

    foodElement.style.left =
        food.x * GRID + "px";

    foodElement.style.top =
        food.y * GRID + "px";


    scoreElement.textContent =
        score;

    bestElement.textContent =
        best;

}


/* =========================
   ⌨️ 조작
========================= */

document.addEventListener(
    "keydown",

    event => {

        const key =
            event.key.toLowerCase();


        if (

            [
                "w", "a", "s", "d",
                "arrowup",
                "arrowdown",
                "arrowleft",
                "arrowright"
            ].includes(key)

        ) {

            event.preventDefault();

        }


        /* 위 */

        if (

            (key === "w" ||
             key === "arrowup")

            && direction.y !== 1

        ) {

            nextDirection =
                { x: 0, y: -1 };

        }


        /* 아래 */

        if (

            (key === "s" ||
             key === "arrowdown")

            && direction.y !== -1

        ) {

            nextDirection =
                { x: 0, y: 1 };

        }


        /* 왼쪽 */

        if (

            (key === "a" ||
             key === "arrowleft")

            && direction.x !== 1

        ) {

            nextDirection =
                { x: -1, y: 0 };

        }


        /* 오른쪽 */

        if (

            (key === "d" ||
             key === "arrowright")

            && direction.x !== -1

        ) {

            nextDirection =
                { x: 1, y: 0 };

        }


        /* 🔄 재시작 */

        if (
            key === "r" &&
            gameOver
        ) {

            restartGame();

        }

    }
);


/* =========================
   🪱 한 칸 이동
========================= */

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


    /* 💥 벽 충돌 */

    if (

        newHead.x < 0 ||
        newHead.x >= COLS ||

        newHead.y < 0 ||
        newHead.y >= ROWS

    ) {

        crash(
            head.x,
            head.y
        );

        return;

    }


    /* 💥 자기 몸 충돌 */

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


    /* 새 머리 추가 */

    snake.unshift(newHead);


    /* 🍎 사과 먹음 */

    if (

        newHead.x === food.x &&
        newHead.y === food.y

    ) {

        score++;

        if (score > best) {
            best = score;
        }


        /* 꼬리를 안 지움 = 몸 길어짐 */

        createFood();

    }

    else {

        /* 일반 이동 */

        snake.pop();

    }


    render();

}


/* =========================
   💥 콰당!
========================= */

function crash(x, y) {

    gameOver = true;


    const crashX =
        x * GRID + GRID / 2;

    const crashY =
        y * GRID + GRID / 2;


    crashElement.style.left =
        crashX + "px";

    crashElement.style.top =
        crashY + "px";


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


/* =========================
   🔄 재시작
========================= */

function restartGame() {

    score = 0;

    gameOver = false;

    direction =
        { x: 1, y: 0 };

    nextDirection =
        { x: 1, y: 0 };


    crashElement.style.display =
        "none";

    gameOverElement.style.display =
        "none";


    resetSnake();

    createFood();

    render();

}


/* =========================
   🚀 게임 시작
========================= */

resetSnake();

createFood();

render();


/*
   ⏱️ 0.16초마다
   정확히 한 칸 이동
*/

setInterval(
    move,
    160
);


/* 클릭하면 키보드 포커스 */

container.addEventListener(
    "click",

    () => {
        container.focus();
    }
);


</script>

</body>
</html>
""", height=820)
