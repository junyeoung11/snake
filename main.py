import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

st.title("🪱 숲속 지렁이 게임")
st.caption("WASD 또는 방향키로 움직이세요!")

components.html("""
<!DOCTYPE html>
<html>
<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #183d22;
    font-family: Arial, sans-serif;
}


/* =========================
   전체 게임
========================= */

#container {

    width: 780px;
    height: 780px;

    margin: auto;

    position: relative;

    overflow: hidden;

    border-radius: 25px;

    background:
        radial-gradient(circle at 10% 10%, #6da64c, transparent 20%),
        radial-gradient(circle at 90% 10%, #396d32, transparent 22%),
        radial-gradient(circle at 10% 90%, #467d38, transparent 22%),
        radial-gradient(circle at 90% 90%, #315e2c, transparent 22%),
        #24562d;

}


/* =========================
   나무
========================= */

.tree {

    position: absolute;

    width: 110px;
    height: 110px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 25%,
            #9bd65b,
            #55933c 48%,
            #214f2a 80%
        );

    box-shadow:
        inset -10px -12px 20px rgba(0,0,0,.3),
        0 8px 15px rgba(0,0,0,.4);

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

    border: 18px solid #264da5;

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

        radial-gradient(
            circle,
            #83bf52,
            #57963a
        );

    background-size: 34px 34px;

    box-shadow:
        inset 0 0 30px rgba(0,0,0,.3),
        0 10px 20px rgba(0,0,0,.45);

}


/* =========================
   점수
========================= */

#scoreBox {

    position: absolute;

    top: 15px;
    left: 15px;

    z-index: 100;

    background: rgba(0,0,0,.75);

    color: white;

    padding: 10px 16px;

    border-radius: 14px;

    font-weight: bold;

}


/* =========================
   사과
========================= */

#food {

    position: absolute;

    width: 34px;
    height: 34px;

    font-size: 30px;

    display: flex;

    align-items: center;
    justify-content: center;

    z-index: 30;

}


/* =========================
   지렁이 SVG
========================= */

#snakeSVG {

    position: absolute;

    width: 648px;
    height: 648px;

    overflow: visible;

    pointer-events: none;

}


/* 몸 그림자 */

#snakeShadow {

    fill: none;

    stroke: #13295c;

    stroke-width: 42;

    stroke-linecap: round;

    stroke-linejoin: round;

    opacity: .4;

}


/* 몸통 */

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

    stroke: #6f98ff;

    stroke-width: 7;

    stroke-linecap: round;

    stroke-linejoin: round;

    opacity: .55;

}


/* =========================
   콰당
========================= */

#crash {

    position: absolute;

    display: none;

    font-size: 75px;

    z-index: 200;

    transform: translate(-50%, -50%);

}


.shake {

    animation: shake .4s;

}

@keyframes shake {

    0%, 100% {
        transform: translate(0);
    }

    25% {
        transform: translate(-10px, 5px);
    }

    50% {
        transform: translate(10px, -5px);
    }

    75% {
        transform: translate(-8px, 3px);
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

    border-radius: 20px;

    background: rgba(0,0,0,.88);

    color: white;

    display: none;

    z-index: 300;

}

</style>

</head>

<body>


<div id="container">


    <!-- 나무 -->

    <div class="tree" style="left:-40px; top:-40px;"></div>
    <div class="tree" style="left:110px; top:-45px;"></div>
    <div class="tree" style="left:280px; top:-45px;"></div>
    <div class="tree" style="left:480px; top:-45px;"></div>
    <div class="tree" style="left:650px; top:-40px;"></div>

    <div class="tree" style="left:-60px; top:180px;"></div>
    <div class="tree" style="left:-60px; top:400px;"></div>

    <div class="tree" style="right:-60px; top:180px;"></div>
    <div class="tree" style="right:-60px; top:400px;"></div>

    <div class="tree" style="left:50px; bottom:-60px;"></div>
    <div class="tree" style="left:250px; bottom:-60px;"></div>
    <div class="tree" style="left:450px; bottom:-60px;"></div>
    <div class="tree" style="left:630px; bottom:-60px;"></div>


    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>


    <div id="game">


        <!-- 사과 -->

        <div id="food">🍎</div>


        <!-- 지렁이 -->

        <svg id="snakeSVG"
             viewBox="0 0 648 648">


            <!-- 몸 -->

            <path id="snakeShadow"></path>

            <path id="snakeBody"></path>

            <path id="snakeLight"></path>


            <!-- =====================
                 머리
                 사진처럼 눈이 위로 튀어나옴
            ====================== -->

            <g id="headGroup">


                <!-- 머리 그림자 -->

                <ellipse
                    cx="0"
                    cy="0"
                    rx="27"
                    ry="22"
                    fill="#173778"
                    opacity=".45"
                    transform="translate(3,4)"
                />


                <!-- 파란 머리 -->

                <ellipse
                    id="headShape"

                    cx="0"
                    cy="0"

                    rx="27"
                    ry="22"

                    fill="#315fc9"

                    stroke="#173778"

                    stroke-width="3"
                />


                <!-- 머리 하이라이트 -->

                <ellipse

                    cx="-6"
                    cy="-6"

                    rx="12"
                    ry="7"

                    fill="#6f98ff"

                    opacity=".35"
                />


                <!-- 왼쪽 눈 -->

                <ellipse
                    id="eyeLeft"

                    cx="7"
                    cy="-20"

                    rx="9"
                    ry="12"

                    fill="white"

                    stroke="#1b336d"

                    stroke-width="2"
                />


                <!-- 오른쪽 눈 -->

                <ellipse
                    id="eyeRight"

                    cx="19"
                    cy="-15"

                    rx="9"
                    ry="12"

                    fill="white"

                    stroke="#1b336d"

                    stroke-width="2"
                />


                <!-- 눈동자 -->

                <circle
                    id="pupilLeft"
                    cx="9"
                    cy="-19"
                    r="4.5"
                    fill="#142044"
                />


                <circle
                    id="pupilRight"
                    cx="21"
                    cy="-14"
                    r="4.5"
                    fill="#142044"
                />


                <!-- 작은 웃는 입 -->

                <path

                    d="M 5 9 Q 13 15 21 9"

                    fill="none"

                    stroke="#18336f"

                    stroke-width="2.5"

                    stroke-linecap="round"

                />


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
   시작 지렁이
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
   부드러운 몸통 경로
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

    /*
    SVG 기본 머리 방향 → 오른쪽
    */

    if (direction.x === 1) return 0;

    if (direction.y === 1) return 90;

    if (direction.x === -1) return 180;

    if (direction.y === -1) return -90;

}


/* =========================
   화면 그리기
========================= */

function render() {


    const path =
        createPath();


    snakeBody.setAttribute("d", path);

    snakeShadow.setAttribute("d", path);

    snakeLight.setAttribute("d", path);


    /* 머리 위치 */

    const head =
        snake[0];


    const x =
        head.x * GRID + GRID / 2;

    const y =
        head.y * GRID + GRID / 2;


    const angle =
        getAngle();


    /*
    ⭐ 머리와 눈 전체를 같이 회전
    */

    headGroup.setAttribute(

        "transform",

        `translate(${x} ${y}) rotate(${angle})`

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

document.addEventListener(
    "keydown",

    e => {

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
            (key === "w" || key === "arrowup")
            && direction.y !== 1
        ) {

            nextDirection = {x: 0, y: -1};

        }


        if (
            (key === "s" || key === "arrowdown")
            && direction.y !== -1
        ) {

            nextDirection = {x: 0, y: 1};

        }


        if (
            (key === "a" || key === "arrowleft")
            && direction.x !== 1
        ) {

            nextDirection = {x: -1, y: 0};

        }


        if (
            (key === "d" || key === "arrowright")
            && direction.x !== -1
        ) {

            nextDirection = {x: 1, y: 0};

        }


        if (key === "r" && dead) {

            restart();

        }

    }
);


/* =========================
   이동
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


    /* 벽 충돌 */

    if (

        newHead.x < 0 ||

        newHead.x >= COLS ||

        newHead.y < 0 ||

        newHead.y >= ROWS

    ) {

        crash(head);

        return;

    }


    /* 몸 충돌 */

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


    /* 사과 */

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
   콰당
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


setInterval(
    move,
    160
);


</script>

</body>
</html>
""", height=800)
