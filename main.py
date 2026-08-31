import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

# Streamlit 기본 여백 줄이기
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 950px;
    }

    header {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center;'>🪱 지렁이 게임</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "WASD 또는 방향키로 움직이세요! 🎮"
    "</p>",
    unsafe_allow_html=True
)

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
    background: #102615;
    overflow: hidden;
    font-family: Arial, sans-serif;

    display: flex;
    justify-content: center;
    align-items: center;
}

/* 전체 게임 공간 */

#gameContainer {

    width: 820px;
    height: 820px;

    position: relative;

    border-radius: 22px;

    overflow: hidden;

    background:
        radial-gradient(circle at 10% 10%, #315f25 0%, transparent 20%),
        radial-gradient(circle at 90% 20%, #244d22 0%, transparent 20%),
        radial-gradient(circle at 20% 90%, #234d22 0%, transparent 20%),
        #173a1d;

    box-shadow:
        0 0 30px rgba(0,0,0,0.8),
        inset 0 0 50px rgba(0,0,0,0.5);

}


/* =========================
   🌲 숲 배경
========================= */

.tree {

    position: absolute;

    width: 110px;
    height: 110px;

    border-radius: 50%;

    background:
        radial-gradient(circle at 35% 30%, #75b83f, #285f29 55%, #123b1c);

    box-shadow:
        0 10px 20px rgba(0,0,0,0.45);

}

.tree::after {

    content: "";

    position: absolute;

    width: 45px;
    height: 70px;

    background: #70431f;

    left: 32px;
    top: 75px;

    border-radius: 20px;

    z-index: -1;

}


/* =========================
   🟩 게임 맵
========================= */

#game {

    position: absolute;

    width: 680px;
    height: 680px;

    left: 70px;
    top: 70px;

    background:

        linear-gradient(
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),

        linear-gradient(
            90deg,
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),

        radial-gradient(
            circle,
            rgba(90,170,55,0.35),
            transparent 60%
        ),

        #3f7f2c;

    background-size:
        68px 68px,
        68px 68px,
        100% 100%,
        100% 100%;

    border:

        6px solid #1d4b22;

    border-radius: 12px;

    box-shadow:

        inset 0 0 30px rgba(0,0,0,0.35),

        0 0 20px rgba(0,0,0,0.5);

}


/* =========================
   🌿 풀 장식
========================= */

.grass {

    position: absolute;

    color: #76b94a;

    font-size: 22px;

    pointer-events: none;

}


/* =========================
   🍎 먹이
========================= */

#food {

    position: absolute;

    font-size: 38px;

    width: 45px;
    height: 45px;

    display: flex;

    align-items: center;
    justify-content: center;

    filter:

        drop-shadow(0 5px 5px rgba(0,0,0,0.5))

        drop-shadow(0 0 8px #d6ff4b);

}


/* =========================
   🪱 지렁이
========================= */

.segment {

    position: absolute;

    width: 34px;
    height: 34px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle at 30% 25%,
            #c8ff4c,
            #82d824 40%,
            #3c8f1c 75%
        );

    border: 2px solid #286b19;

    box-shadow:

        inset -5px -6px 8px rgba(0,0,0,0.25),

        inset 4px 4px 8px rgba(255,255,255,0.3),

        0 5px 8px rgba(0,0,0,0.35);

    transform: translate(-50%, -50%);

    transition:

        left 0.08s linear,

        top 0.08s linear;

}


/* 🪱 머리 */

.head {

    width: 44px;
    height: 44px;

    z-index: 10;

}


/* 👀 눈 */

.eye {

    position: absolute;

    width: 13px;
    height: 16px;

    background: white;

    border-radius: 50%;

    top: 7px;

    box-shadow:
        0 2px 2px rgba(0,0,0,0.2);

}

.eye.left {

    left: 7px;

}

.eye.right {

    right: 7px;

}


/* 눈동자 */

.pupil {

    width: 6px;
    height: 7px;

    background: #111;

    border-radius: 50%;

    position: absolute;

    left: 4px;
    top: 6px;

}


/* =========================
   🏆 점수판
========================= */

#scoreBox {

    position: absolute;

    top: 25px;
    left: 25px;

    z-index: 30;

    background:

        rgba(5,20,8,0.88);

    border:

        2px solid rgba(110,200,70,0.4);

    border-radius: 15px;

    padding: 14px 22px;

    color: white;

    font-size: 22px;

    font-weight: bold;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.5);

}


/* ❤️ 최고점수 */

#bestBox {

    position: absolute;

    top: 25px;
    right: 25px;

    z-index: 30;

    background:

        rgba(5,20,8,0.88);

    border:

        2px solid rgba(255,220,60,0.4);

    border-radius: 15px;

    padding: 14px 22px;

    color: white;

    font-size: 20px;

    font-weight: bold;

}


/* =========================
   💀 게임오버
========================= */

#gameOver {

    position: absolute;

    left: 50%;
    top: 50%;

    transform:

        translate(-50%, -50%);

    width: 400px;

    padding: 30px;

    text-align: center;

    color: white;

    background:

        rgba(0,0,0,0.82);

    border:

        2px solid #85d94b;

    border-radius: 20px;

    z-index: 100;

    display: none;

    box-shadow:
        0 0 40px rgba(0,0,0,0.8);

}


#gameOver h1 {

    color: #ffdf4f;

    margin-top: 0;

}


#gameOver p {

    font-size: 22px;

}


/* =========================
   🎮 조작법
========================= */

#controls {

    position: absolute;

    bottom: 15px;

    left: 50%;

    transform: translateX(-50%);

    z-index: 50;

    color: white;

    background:

        rgba(0,0,0,0.75);

    padding:

        10px 25px;

    border-radius: 15px;

    font-size: 17px;

    white-space: nowrap;

}

</style>

</head>


<body>

<div id="gameContainer">


    <!-- 🌲 나무 -->

    <div class="tree" style="left:-25px; top:10px;"></div>
    <div class="tree" style="left:80px; top:-40px;"></div>
    <div class="tree" style="left:220px; top:-30px;"></div>
    <div class="tree" style="left:400px; top:-35px;"></div>
    <div class="tree" style="left:600px; top:-20px;"></div>
    <div class="tree" style="right:-35px; top:100px;"></div>
    <div class="tree" style="right:-40px; top:300px;"></div>
    <div class="tree" style="right:-30px; bottom:80px;"></div>
    <div class="tree" style="left:-40px; bottom:100px;"></div>
    <div class="tree" style="left:100px; bottom:-45px;"></div>
    <div class="tree" style="left:300px; bottom:-50px;"></div>
    <div class="tree" style="left:520px; bottom:-45px;"></div>


    <!-- 🏆 점수 -->

    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>


    <!-- ❤️ 최고점수 -->

    <div id="bestBox">
        ❤️ 최고: <span id="best">0</span>
    </div>


    <!-- 🟩 맵 -->

    <div id="game">


        <!-- 🌿 장식 -->

        <div class="grass" style="left:80px;top:100px;">🌿</div>
        <div class="grass" style="left:500px;top:120px;">☘️</div>
        <div class="grass" style="left:180px;top:430px;">🌱</div>
        <div class="grass" style="left:530px;top:500px;">☘️</div>
        <div class="grass" style="left:300px;top:200px;">🌿</div>


        <!-- 🍎 먹이 -->

        <div id="food">🍎</div>


    </div>


    <!-- 💀 게임오버 -->

    <div id="gameOver">

        <h1>💀 게임 오버!</h1>

        <p>
            최종 점수:
            <span id="finalScore">0</span>
        </p>

        <p style="font-size:17px;color:#baff7a;">
            R 키를 눌러 다시 시작!
        </p>

    </div>


    <!-- 🎮 조작법 -->

    <div id="controls">

        ⌨️ WASD 또는 방향키로 이동

    </div>


</div>


<script>


/* =========================
   ⚙️ 설정
========================= */

const game = document.getElementById("game");

const foodElement = document.getElementById("food");

const scoreElement = document.getElementById("score");

const bestElement = document.getElementById("best");

const gameOverElement =
    document.getElementById("gameOver");

const finalScoreElement =
    document.getElementById("finalScore");


const MAP_SIZE = 680;


/* =========================
   🪱 게임 데이터
========================= */

let snake = [];

let direction = { x: 1, y: 0 };

let nextDirection = { x: 1, y: 0 };

let food = { x: 450, y: 200 };

let score = 0;

let bestScore = 0;

let gameOver = false;


/* =========================
   🪱 지렁이 생성
========================= */

function createSnake() {

    document
        .querySelectorAll(".segment")
        .forEach(e => e.remove());


    snake = [];


    for (let i = 0; i < 8; i++) {

        const element =
            document.createElement("div");


        element.classList.add("segment");


        if (i === 0) {

            element.classList.add("head");


            /* 👀 눈 */

            element.innerHTML = `

                <div class="eye left">
                    <div class="pupil"></div>
                </div>

                <div class="eye right">
                    <div class="pupil"></div>
                </div>

            `;

        }


        game.appendChild(element);


        snake.push({

            x: 260 - i * 28,

            y: 350,

            element: element

        });

    }

}


/* =========================
   🍎 먹이 위치
========================= */

function createFood() {

    let valid = false;


    while (!valid) {

        food = {

            x: 40 + Math.random() * (MAP_SIZE - 80),

            y: 40 + Math.random() * (MAP_SIZE - 80)

        };


        valid = !snake.some(part => {

            const dx = part.x - food.x;

            const dy = part.y - food.y;

            return Math.sqrt(dx*dx + dy*dy) < 50;

        });

    }

}


/* =========================
   🎨 화면 업데이트
========================= */

function render() {

    snake.forEach((part, index) => {

        part.element.style.left =
            part.x + "px";

        part.element.style.top =
            part.y + "px";


        /* 머리 회전 */

        if (index === 0) {

            let angle =
                Math.atan2(
                    direction.y,
                    direction.x
                ) * 180 / Math.PI;


            part.element.style.transform =
                `translate(-50%, -50%) rotate(${angle}deg)`;

        }

    });


    foodElement.style.left =
        (food.x - 22) + "px";

    foodElement.style.top =
        (food.y - 22) + "px";


    scoreElement.textContent = score;

    bestElement.textContent = bestScore;

}


/* =========================
   🎮 부드러운 움직임
========================= */

function update() {

    if (gameOver) return;


    direction = nextDirection;


    /* 머리 이동 */

    const head = snake[0];

    const SPEED = 2.8;


    head.x += direction.x * SPEED;

    head.y += direction.y * SPEED;


    /* 💥 벽 충돌 */

    if (

        head.x < 20 ||

        head.x > MAP_SIZE - 20 ||

        head.y < 20 ||

        head.y > MAP_SIZE - 20

    ) {

        endGame();

        return;

    }


    /* 🪱 몸통이 부드럽게 따라오기 */

    for (let i = 1; i < snake.length; i++) {

        const previous = snake[i - 1];

        const current = snake[i];


        const dx =
            previous.x - current.x;

        const dy =
            previous.y - current.y;


        const distance =
            Math.sqrt(dx * dx + dy * dy);


        const targetDistance = 28;


        if (distance > targetDistance) {

            const moveDistance =
                (distance - targetDistance) * 0.35;


            current.x +=
                (dx / distance) * moveDistance;

            current.y +=
                (dy / distance) * moveDistance;

        }

    }


    /* 🍎 먹었는지 확인 */

    const foodDistance =

        Math.sqrt(

            (head.x - food.x) *
            (head.x - food.x)

            +

            (head.y - food.y) *
            (head.y - food.y)

        );


    if (foodDistance < 32) {

        score++;


        if (score > bestScore) {

            bestScore = score;

        }


        /* 몸 길어짐 */

        const tail =
            snake[snake.length - 1];


        const newSegment =
            document.createElement("div");


        newSegment.classList.add("segment");


        game.appendChild(newSegment);


        snake.push({

            x: tail.x,

            y: tail.y,

            element: newSegment

        });


        createFood();

    }


    /* 자기 몸 충돌 */

    for (let i = 5; i < snake.length; i++) {

        const part = snake[i];


        const distance =

            Math.sqrt(

                (head.x - part.x) *
                (head.x - part.x)

                +

                (head.y - part.y) *
                (head.y - part.y)

            );


        if (distance < 20) {

            endGame();

            return;

        }

    }


    render();

}


/* =========================
   💀 게임 종료
========================= */

function endGame() {

    gameOver = true;

    finalScoreElement.textContent =
        score;

    gameOverElement.style.display =
        "block";

}


/* =========================
   🔄 재시작
========================= */

function restartGame() {

    score = 0;

    gameOver = false;

    direction = { x: 1, y: 0 };

    nextDirection = { x: 1, y: 0 };


    gameOverElement.style.display =
        "none";


    createSnake();

    createFood();

    render();

}


/* =========================
   ⌨️ 키보드 조작
========================= */

document.addEventListener(
    "keydown",

    function(event) {

        const key =
            event.key.toLowerCase();


        if (

            [

                "arrowup",
                "arrowdown",
                "arrowleft",
                "arrowright",
                "w",
                "a",
                "s",
                "d"

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


        /* R 재시작 */

        if (

            key === "r"

            && gameOver

        ) {

            restartGame();

        }

    }

);


/* =========================
   🚀 시작
========================= */

createSnake();

createFood();

render();


/* 60FPS */

setInterval(
    update,
    1000 / 60
);

</script>

</body>
</html>
""", height=850)
