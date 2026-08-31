import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

st.markdown("""
<style>
header {visibility: hidden;}
.block-container {
    padding-top: 1rem;
    max-width: 950px;
}
</style>
""", unsafe_allow_html=True)

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
    background: #193d22;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

/* =========================
   전체 숲
========================= */

#container {

    width: 780px;
    height: 780px;

    margin: auto;

    position: relative;

    overflow: hidden;

    border-radius: 25px;

    background:
        radial-gradient(circle at 10% 10%, #6ca64c, transparent 20%),
        radial-gradient(circle at 90% 15%, #396f32, transparent 22%),
        radial-gradient(circle at 15% 90%, #4a8238, transparent 25%),
        radial-gradient(circle at 90% 90%, #315f2e, transparent 25%),
        #24542b;

}

/* =========================
   나무
========================= */

.tree {

    position: absolute;

    width: 115px;
    height: 115px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 25%,
            #9bd75b,
            #55943b 48%,
            #1d5128 80%
        );

    box-shadow:
        inset -10px -12px 20px rgba(0,0,0,.28),
        0 10px 15px rgba(0,0,0,.45);

}

/* =========================
   게임판
========================= */

#game {

    position: absolute;

    width: 648px;
    height: 648px;

    left: 66px;
    top: 66px;

    overflow: hidden;

    border: 18px solid #254da5;

    border-radius: 20px;

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
        inset 0 0 30px rgba(0,0,0,.22),
        0 10px 20px rgba(0,0,0,.45);

}

/* =========================
   점수
========================= */

#scoreBox {

    position: absolute;

    top: 18px;
    left: 18px;

    z-index: 100;

    background: rgba(0,0,0,.78);

    color: white;

    padding: 11px 18px;

    border-radius: 15px;

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

    justify-content: center;
    align-items: center;

    font-size: 31px;

    z-index: 40;

    animation: applePulse 1s ease-in-out infinite;

    transform-origin: center;

    filter:
        drop-shadow(0 3px 3px rgba(0,0,0,.35));

}

@keyframes applePulse {

    0% {
        transform: scale(.72);
    }

    50% {
        transform: scale(1.15);
    }

    100% {
        transform: scale(.72);
    }

}

/* =========================
   뱀 SVG
========================= */

#snakeSVG {

    position: absolute;

    width: 648px;
    height: 648px;

    left: 0;
    top: 0;

    overflow: visible;

    pointer-events: none;

}

/* 몸 그림자 */

#snakeShadow {

    fill: none;

    stroke: #17336e;

    stroke-width: 42;

    stroke-linecap: round;

    stroke-linejoin: round;

    opacity: .35;

}

/* 몸 */

#snakeBody {

    fill: none;

    stroke: #315fc9;

    stroke-width: 36;

    stroke-linecap: round;

    stroke-linejoin: round;

}

/* 몸 하이라이트 */

#snakeLight {

    fill: none;

    stroke: #739cff;

    stroke-width: 6;

    stroke-linecap: round;

    stroke-linejoin: round;

    opacity: .45;

}

/* =========================
   💥 충돌
========================= */

#crash {

    position: absolute;

    display: none;

    font-size: 78px;

    z-index: 200;

    transform: translate(-50%, -50%);

}

.shake {

    animation: shake .45s;

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
   게임오버
========================= */

#gameOver {

    position: absolute;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    width: 360px;

    padding: 25px;

    text-align: center;

    border-radius: 22px;

    background: rgba(0,0,0,.88);

    color: white;

    display: none;

    z-index: 300;

}

#gameOver h1 {
    color: #ff6257;
}

</style>
</head>

<body>

<div id="container">

    <!-- 나무 -->

    <div class="tree" style="left:-45px;top:-40px;"></div>
    <div class="tree" style="left:110px;top:-50px;"></div>
    <div class="tree" style="left:280px;top:-50px;"></div>
    <div class="tree" style="left:470px;top:-50px;"></div>
    <div class="tree" style="left:650px;top:-40px;"></div>

    <div class="tree" style="left:-60px;top:170px;"></div>
    <div class="tree" style="left:-60px;top:380px;"></div>
    <div class="tree" style="left:-60px;top:570px;"></div>

    <div class="tree" style="right:-60px;top:170px;"></div>
    <div class="tree" style="right:-60px;top:380px;"></div>
    <div class="tree" style="right:-60px;top:570px;"></div>

    <div class="tree" style="left:50px;bottom:-60px;"></div>
    <div class="tree" style="left:240px;bottom:-60px;"></div>
    <div class="tree" style="left:440px;bottom:-60px;"></div>
    <div class="tree" style="left:620px;bottom:-60px;"></div>


    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>


    <div id="game">

        <!-- 사과 -->

        <div id="food">🍎</div>


        <!-- 뱀 -->

        <svg id="snakeSVG" viewBox="0 0 648 648">

            <path id="snakeShadow"></path>

            <path id="snakeBody"></path>

            <path id="snakeLight"></path>


            <!-- =========================
                 사진 같은 뱀 얼굴
                 기본 방향: 오른쪽 →
            ========================== -->

            <g id="headGroup">

                <!-- 머리 뒤쪽 그림자 -->

                <ellipse
                    cx="0"
                    cy="3"
                    rx="27"
                    ry="23"
                    fill="#17336e"
                    opacity=".35"
                ></ellipse>


                <!-- 둥근 파란 머리 -->

                <path
                    d="
                        M -18 -20
                        Q 5 -25 20 -14
                        Q 33 0 20 14
                        Q 5 25 -18 20
                        Q -28 10 -28 0
                        Q -28 -10 -18 -20
                    "
                    fill="#315fc9"
                    stroke="#244a9f"
                    stroke-width="3"
                ></path>


                <!-- 머리 밝은 부분 -->

                <path
                    d="
                        M -17 -16
                        Q -2 -22 10 -14
                    "
                    fill="none"
                    stroke="#6f98ff"
                    stroke-width="6"
                    stroke-linecap="round"
                    opacity=".45"
                ></path>


                <!-- 사진처럼 앞으로 튀어나온 흰 눈 -->

                <circle
                    cx="4"
                    cy="-18"
                    r="10"
                    fill="#f8fbff"
                    stroke="#31528e"
                    stroke-width="2"
                ></circle>

                <circle
                    cx="4"
                    cy="18"
                    r="10"
                    fill="#f8fbff"
                    stroke="#31528e"
                    stroke-width="2"
                ></circle>


                <!-- 눈동자 -->

                <circle
                    cx="7"
                    cy="-17"
                    r="4.5"
                    fill="#18234b"
                ></circle>

                <circle
                    cx="7"
                    cy="17"
                    r="4.5"
                    fill="#18234b"
                ></circle>


                <!-- 눈 반짝임 -->

                <circle
                    cx="8"
                    cy="-19"
                    r="1.5"
                    fill="white"
                ></circle>

                <circle
                    cx="8"
                    cy="15"
                    r="1.5"
                    fill="white"
                ></circle>


                <!-- 작은 입 -->

                <path
                    d="
                        M 16 -4
                        Q 21 0 16 4
                    "
                    fill="none"
                    stroke="#173778"
                    stroke-width="2.5"
                    stroke-linecap="round"
                ></path>

            </g>

        </svg>


        <div id="crash">💥</div>

    </div>


    <div id="gameOver">

        <h1>💥 콰당!</h1>

        <h2>
            점수: <span id="finalScore">0</span>
        </h2>

        <p>R 키를 눌러 다시 시작</p>

    </div>

</div>


<script>

/* =========================
   설정
========================= */

const GRID = 34;
const COLS = 18;
const ROWS = 18;


/* =========================
   요소
========================= */

const game =
    document.getElementById("game");

const foodElement =
    document.getElementById("food");

const scoreElement =
    document.getElementById("score");

const finalScoreElement =
    document.getElementById("finalScore");

const gameOverElement =
    document.getElementById("gameOver");

const crashElement =
    document.getElementById("crash");

const snakeBody =
    document.getElementById("snakeBody");

const snakeShadow =
    document.getElementById("snakeShadow");

const snakeLight =
    document.getElementById("snakeLight");

const headGroup =
    document.getElementById("headGroup");


let snake = [];

let direction = {x: 1, y: 0};

let nextDirection = {x: 1, y: 0};

let food;

let score = 0;

let dead = false;


/* =========================
   시작 뱀
========================= */

function resetSnake() {

    snake = [

        {x: 8, y: 9},
        {x: 7, y: 9},
        {x: 6, y: 9},
        {x: 5, y: 9},
        {x: 4, y: 9}

    ];

}


/* =========================
   사과 생성
========================= */

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


/* =========================
   부드러운 몸통
========================= */

function createPath() {

    const points = [...snake]
        .reverse()
        .map(part => ({

            x: part.x * GRID + GRID / 2,
            y: part.y * GRID + GRID / 2

        }));


    if (points.length < 2) return "";


    let path =
        `M ${points[0].x} ${points[0].y}`;


    for (let i = 1; i < points.length - 1; i++) {

        const a = points[i];
        const b = points[i + 1];

        const midX =
            (a.x + b.x) / 2;

        const midY =
            (a.y + b.y) / 2;


        path +=
            ` Q ${a.x} ${a.y} ${midX} ${midY}`;

    }


    const last =
        points[points.length - 1];

    path +=
        ` L ${last.x} ${last.y}`;

    return path;

}


/* =========================
   머리 방향
========================= */

function getAngle() {

    if (direction.x === 1) return 0;

    if (direction.y === 1) return 90;

    if (direction.x === -1) return 180;

    if (direction.y === -1) return -90;

}


/* =========================
   화면
========================= */

function render() {

    const path =
        createPath();


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


    /* 머리 */

    const head =
        snake[0];


    const x =
        head.x * GRID + GRID / 2;

    const y =
        head.y * GRID + GRID / 2;


    headGroup.setAttribute(

        "transform",

        `translate(${x} ${y}) rotate(${getAngle()})`

    );


    /* 사과 */

    foodElement.style.left =
        food.x * GRID + "px";

    foodElement.style.top =
        food.y * GRID + "px";


    scoreElement.textContent =
        score;

}


/* =========================
   키보드
========================= */

document.addEventListener("keydown", e => {

    const key =
        e.key.toLowerCase();


    if (

        [
            "w", "a", "s", "d",
            "arrowup",
            "arrowdown",
            "arrowleft",
            "arrowright"
        ].includes(key)

    ) {

        e.preventDefault();

    }


    if (

        (key === "w" || key === "arrowup") &&
        direction.y !== 1

    ) {

        nextDirection = {x: 0, y: -1};

    }


    if (

        (key === "s" || key === "arrowdown") &&
        direction.y !== -1

    ) {

        nextDirection = {x: 0, y: 1};

    }


    if (

        (key === "a" || key === "arrowleft") &&
        direction.x !== 1

    ) {

        nextDirection = {x: -1, y: 0};

    }


    if (

        (key === "d" || key === "arrowright") &&
        direction.x !== -1

    ) {

        nextDirection = {x: 1, y: 0};

    }


    if (key === "r" && dead) {

        restart();

    }

});


/* =========================
   한 칸 이동
========================= */

function move() {

    if (dead) return;


    direction =
        nextDirection;


    const head =
        snake[0];


    const newHead = {

        x: head.x + direction.x,
        y: head.y + direction.y

    };


    /* 벽 */

    if (

        newHead.x < 0 ||
        newHead.x >= COLS ||
        newHead.y < 0 ||
        newHead.y >= ROWS

    ) {

        crash(head);

        return;

    }


    /* 몸 */

    if (

        snake.some(part =>

            part.x === newHead.x &&
            part.y === newHead.y

        )

    ) {

        crash(newHead);

        return;

    }


    snake.unshift(newHead);


    /* 🍎 먹음 */

    if (

        newHead.x === food.x &&
        newHead.y === food.y

    ) {

        score++;

        createFood();

    }

    else {

        snake.pop();

    }


    render();

}


/* =========================
   💥 콰당
========================= */

function crash(position) {

    dead = true;


    crashElement.style.left =
        position.x * GRID +
        GRID / 2 + "px";


    crashElement.style.top =
        position.y * GRID +
        GRID / 2 + "px";


    crashElement.style.display =
        "block";


    game.classList.add("shake");


    setTimeout(() => {

        game.classList.remove("shake");

        finalScoreElement.textContent =
            score;

        gameOverElement.style.display =
            "block";

    }, 500);

}


/* =========================
   재시작
========================= */

function restart() {

    score = 0;

    dead = false;

    direction = {x: 1, y: 0};

    nextDirection = {x: 1, y: 0};


    crashElement.style.display =
        "none";

    gameOverElement.style.display =
        "none";


    resetSnake();

    createFood();

    render();

}


/* 시작 */

resetSnake();

createFood();

render();

setInterval(move, 160);

</script>

</body>
</html>
""", height=820)
