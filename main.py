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
    max-width: 1000px;
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🪱 지렁이 게임")
st.caption("🎮 WASD 또는 방향키로 움직이세요!")

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
    background: #163b1d;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

/* 🌲 전체 숲 */

#container {
    width: 820px;
    height: 820px;
    margin: auto;
    position: relative;
    overflow: hidden;
    border-radius: 25px;

    background:
        radial-gradient(circle at 10% 10%, #477c32, transparent 20%),
        radial-gradient(circle at 90% 20%, #285d29, transparent 25%),
        radial-gradient(circle at 20% 90%, #356f2e, transparent 25%),
        #1d4b27;

    box-shadow:
        0 0 35px rgba(0,0,0,.8);
}


/* 🌳 나무 */

.tree {
    position: absolute;
    width: 120px;
    height: 120px;

    border-radius: 50%;

    background:
        radial-gradient(circle at 35% 30%,
        #82c94c,
        #367a2e 55%,
        #173e20);

    box-shadow:
        0 10px 20px rgba(0,0,0,.5);

    z-index: 1;
}


/* 🟩 게임 맵 */

#game {

    position: absolute;

    width: 680px;
    height: 680px;

    left: 70px;
    top: 70px;

    border-radius: 12px;

    overflow: hidden;

    border: 18px solid #244fa3;

    background:

        linear-gradient(
            90deg,
            rgba(0,0,0,.08) 1px,
            transparent 1px
        ),

        linear-gradient(
            rgba(0,0,0,.08) 1px,
            transparent 1px
        ),

        #6aaa3b;

    background-size:
        34px 34px;

    box-shadow:

        inset 0 0 30px rgba(0,0,0,.3),

        0 0 20px rgba(0,0,0,.5);

    z-index: 5;
}


/* 🍎 사과 */

#food {

    position: absolute;

    width: 34px;
    height: 34px;

    font-size: 30px;

    display: flex;
    align-items: center;
    justify-content: center;

    z-index: 10;

    filter:
        drop-shadow(0 4px 3px rgba(0,0,0,.4));
}


/* 🪱 몸통 */

.segment {

    position: absolute;

    width: 34px;
    height: 34px;

    border-radius: 12px;

    background:

        linear-gradient(
            135deg,
            #557fe5,
            #254aa8
        );

    border:

        2px solid #183782;

    box-shadow:

        inset 4px 4px 8px rgba(255,255,255,.2),

        inset -4px -4px 8px rgba(0,0,0,.25),

        0 4px 6px rgba(0,0,0,.3);

    transition:

        left .12s ease,

        top .12s ease;

}


/* 🪱 머리 */

.head {

    width: 42px;
    height: 42px;

    border-radius: 50%;

    z-index: 20;

}


/* 👀 눈 */

.eye {

    position: absolute;

    width: 14px;
    height: 17px;

    background: white;

    border-radius: 50%;

    top: 6px;

}


.eye.left {
    left: 6px;
}


.eye.right {
    right: 6px;
}


.pupil {

    position: absolute;

    width: 7px;
    height: 8px;

    background: #111;

    border-radius: 50%;

    left: 4px;
    top: 6px;

}


/* 🏆 점수 */

#scoreBox {

    position: absolute;

    top: 20px;
    left: 20px;

    z-index: 50;

    color: white;

    background:
        rgba(0,0,0,.8);

    border-radius: 15px;

    padding: 12px 20px;

    font-size: 22px;

    font-weight: bold;

}


/* 💥 충돌 효과 */

#crash {

    position: absolute;

    font-size: 75px;

    display: none;

    z-index: 100;

    animation: crash .6s ease;

}


@keyframes crash {

    0% {
        transform: scale(.2) rotate(0deg);
        opacity: 0;
    }

    50% {
        transform: scale(1.5) rotate(20deg);
        opacity: 1;
    }

    100% {
        transform: scale(1) rotate(-10deg);
        opacity: 1;
    }

}


/* 💀 게임오버 */

#gameOver {

    position: absolute;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%);

    width: 400px;

    padding: 30px;

    background:
        rgba(0,0,0,.82);

    border:
        2px solid #547ee0;

    border-radius: 20px;

    color: white;

    text-align: center;

    display: none;

    z-index: 200;

}


#gameOver h1 {
    color: #ff5d50;
}


</style>
</head>


<body>

<div id="container">

    <!-- 🌲 나무 -->

    <div class="tree" style="left:-30px;top:-30px;"></div>
    <div class="tree" style="left:120px;top:-50px;"></div>
    <div class="tree" style="left:300px;top:-50px;"></div>
    <div class="tree" style="left:500px;top:-50px;"></div>
    <div class="tree" style="right:-30px;top:-20px;"></div>

    <div class="tree" style="left:-60px;top:200px;"></div>
    <div class="tree" style="right:-60px;top:180px;"></div>

    <div class="tree" style="left:-60px;bottom:100px;"></div>
    <div class="tree" style="right:-60px;bottom:100px;"></div>

    <div class="tree" style="left:100px;bottom:-60px;"></div>
    <div class="tree" style="left:300px;bottom:-60px;"></div>
    <div class="tree" style="left:500px;bottom:-60px;"></div>


    <!-- 🏆 -->

    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>


    <!-- 🟩 게임 -->

    <div id="game">

        <!-- 🍎 사과 -->
        <div id="food">🍎</div>

        <!-- 💥 충돌 -->
        <div id="crash">💥</div>

    </div>


    <!-- 💀 -->

    <div id="gameOver">

        <h1>💀 게임 오버!</h1>

        <h2>
            최종 점수:
            <span id="finalScore">0</span>
        </h2>

        <p>R 키를 눌러 다시 시작하세요!</p>

    </div>

</div>


<script>


/* =========================
   ⚙️ 설정
========================= */

const game =
    document.getElementById("game");

const foodElement =
    document.getElementById("food");

const crashElement =
    document.getElementById("crash");

const scoreElement =
    document.getElementById("score");

const gameOverElement =
    document.getElementById("gameOver");

const finalScoreElement =
    document.getElementById("finalScore");


const GRID = 34;

/* 벽 두께 제외 실제 맵 */

const MAP = 646;


/* =========================
   🎮 변수
========================= */

let snake = [];

let direction =
    {x: 1, y: 0};

let nextDirection =
    {x: 1, y: 0};

let food;

let score = 0;

let gameOver = false;


/* =========================
   🪱 생성
========================= */

function createSnake() {

    document
        .querySelectorAll(".segment")
        .forEach(e => e.remove());


    snake = [];


    for (let i = 0; i < 4; i++) {

        const element =
            document.createElement("div");


        element.classList.add("segment");


        if (i === 0) {

            element.classList.add("head");

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

            x: 272 - i * GRID,

            y: 272,

            element: element

        });

    }

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
                    Math.random() * 18
                ) * GRID,

            y:
                Math.floor(
                    Math.random() * 18
                ) * GRID

        };


        valid = !snake.some(part =>
            part.x === food.x &&
            part.y === food.y
        );

    }


    foodElement.style.left =
        food.x + "px";

    foodElement.style.top =
        food.y + "px";

}


/* =========================
   🎨 그리기
========================= */

function render() {

    snake.forEach(part => {

        part.element.style.left =
            part.x + "px";

        part.element.style.top =
            part.y + "px";

    });


    scoreElement.textContent =
        score;

}


/* =========================
   ⌨️ 키보드
========================= */

document.addEventListener(
    "keydown",

    function(event) {

        const key =
            event.key.toLowerCase();


        if (
            ["w","a","s","d",
            "arrowup","arrowdown",
            "arrowleft","arrowright"]
            .includes(key)
        ) {

            event.preventDefault();

        }


        if (
            (key === "w" ||
            key === "arrowup")

            && direction.y !== 1
        ) {

            nextDirection =
                {x:0,y:-1};

        }


        if (
            (key === "s" ||
            key === "arrowdown")

            && direction.y !== -1
        ) {

            nextDirection =
                {x:0,y:1};

        }


        if (
            (key === "a" ||
            key === "arrowleft")

            && direction.x !== 1
        ) {

            nextDirection =
                {x:-1,y:0};

        }


        if (
            (key === "d" ||
            key === "arrowright")

            && direction.x !== -1
        ) {

            nextDirection =
                {x:1,y:0};

        }


        if (
            key === "r" &&
            gameOver
        ) {

            restart();

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


    const head = snake[0];


    const newHead = {

        x:
            head.x +
            direction.x * GRID,

        y:
            head.y +
            direction.y * GRID

    };


    /* 💥 벽 충돌 */

    if (

        newHead.x < 0 ||

        newHead.x >= MAP ||

        newHead.y < 0 ||

        newHead.y >= MAP

    ) {

        crash(
            head.x,
            head.y
        );

        return;

    }


    /* 💥 자기 몸 충돌 */

    if (

        snake.some(
            part =>

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


    /* 머리 이동 */

    const tail =
        snake.pop();


    tail.x =
        newHead.x;

    tail.y =
        newHead.y;


    snake.unshift(tail);


    /* 🍎 사과 먹기 */

    if (

        newHead.x === food.x &&
        newHead.y === food.y

    ) {

        score++;


        /* 몸 하나 추가 */

        const last =
            snake[snake.length - 1];


        const element =
            document.createElement("div");


        element.classList.add("segment");


        game.appendChild(element);


        snake.push({

            x:last.x,
            y:last.y,
            element:element

        });


        /* 새 사과 1개 */

        createFood();

    }


    render();

}


/* =========================
   💥 콰당
========================= */

function crash(x, y) {

    gameOver = true;


    crashElement.style.left =
        (x - 20) + "px";

    crashElement.style.top =
        (y - 20) + "px";


    crashElement.style.display =
        "block";


    setTimeout(() => {

        finalScoreElement.textContent =
            score;

        gameOverElement.style.display =
            "block";

    }, 500);

}


/* =========================
   🔄 재시작
========================= */

function restart() {

    score = 0;

    gameOver = false;

    direction =
        {x:1,y:0};

    nextDirection =
        {x:1,y:0};


    crashElement.style.display =
        "none";

    gameOverElement.style.display =
        "none";


    createSnake();

    createFood();

    render();

}


/* =========================
   🚀 시작
========================= */

createSnake();

createFood();

render();


/* ⏱️ 이동 속도 */

setInterval(
    move,
    170
);


</script>

</body>
</html>
""", height=850)
