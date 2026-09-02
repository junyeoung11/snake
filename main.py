import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

st.markdown("""
<style>
header {visibility:hidden;}
.block-container {
    padding-top:1rem;
    max-width:950px;
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing:border-box;
}

body {
    margin:0;
    background:#193d22;
    font-family:Arial,sans-serif;
    overflow:hidden;
}

#container {
    width:780px;
    height:780px;
    margin:auto;
    position:relative;
    overflow:hidden;
    border-radius:25px;

    background:
        radial-gradient(circle at 10% 10%,#6ca64c,transparent 20%),
        radial-gradient(circle at 90% 15%,#396f32,transparent 22%),
        radial-gradient(circle at 15% 90%,#4a8238,transparent 25%),
        radial-gradient(circle at 90% 90%,#315f2e,transparent 25%),
        #24542b;
}

.tree {
    position:absolute;
    width:115px;
    height:115px;
    border-radius:50%;

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

#game {
    position:absolute;
    width:648px;
    height:648px;
    left:66px;
    top:66px;
    overflow:hidden;

    border:18px solid #254da5;
    border-radius:20px;

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
        inset 0 0 30px rgba(0,0,0,.22),
        0 10px 20px rgba(0,0,0,.45);
}

#scoreBox,
#highScoreBox {
    position:absolute;
    top:18px;
    z-index:100;

    background:rgba(0,0,0,.78);
    color:white;

    padding:11px 18px;
    border-radius:15px;

    font-size:20px;
    font-weight:bold;
}

#scoreBox {
    left:18px;
}

#highScoreBox {
    right:18px;
}

#food {
    position:absolute;
    width:34px;
    height:34px;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:31px;
    z-index:40;

    animation:applePulse 1s ease-in-out infinite;
    transform-origin:center;

    filter:drop-shadow(0 3px 3px rgba(0,0,0,.35));
}

@keyframes applePulse {
    0% {transform:scale(.72);}
    50% {transform:scale(1.15);}
    100% {transform:scale(.72);}
}

#snakeSVG {
    position:absolute;
    width:648px;
    height:648px;
    left:0;
    top:0;
    overflow:visible;
    pointer-events:none;
}

#snakeShadow {
    fill:none;
    stroke:#17336e;
    stroke-width:42;
    stroke-linecap:round;
    stroke-linejoin:round;
    opacity:.35;
}

#snakeBody {
    fill:none;
    stroke:#315fc9;
    stroke-width:36;
    stroke-linecap:round;
    stroke-linejoin:round;
}

#snakeLight {
    fill:none;
    stroke:#739cff;
    stroke-width:6;
    stroke-linecap:round;
    stroke-linejoin:round;
    opacity:.45;
}

/* =========================
   뱀 얼굴
========================= */

#headGroup {
    transition:transform .03s linear;
}

#mouthClosed,
#mouthOpen {
    fill:none;
    stroke:#173778;
    stroke-width:2.8;
    stroke-linecap:round;
}

#mouthOpen {
    display:none;
}

#crash {
    position:absolute;
    display:none;

    font-size:65px;
    font-weight:900;

    color:white;

    z-index:200;

    transform:translate(-50%,-50%);

    text-shadow:
        4px 4px 0 #111,
        -2px -2px 0 #111,
        2px -2px 0 #111,
        -2px 2px 0 #111;
}

.shake {
    animation:shake .45s;
}

@keyframes shake {
    0%,100% {
        transform:translate(0,0);
    }

    20% {
        transform:translate(-10px,5px);
    }

    40% {
        transform:translate(10px,-5px);
    }

    60% {
        transform:translate(-8px,4px);
    }

    80% {
        transform:translate(8px,-3px);
    }
}

/* =========================
   오버레이
========================= */

.overlay {
    position:absolute;

    left:50%;
    top:50%;

    transform:translate(-50%,-50%);

    width:430px;

    padding:35px 30px;

    text-align:center;

    border-radius:25px;

    background:rgba(0,0,0,.92);

    color:white;

    z-index:500;

    display:none;

    box-shadow:
        0 15px 40px rgba(0,0,0,.5);
}

.overlay h1 {
    margin:0 0 30px;

    font-size:64px;

    font-weight:900;
}

.menuButton {
    display:block;

    width:270px;
    height:62px;

    margin:10px auto;

    border:none;

    border-radius:16px;

    font-size:23px;

    font-weight:bold;

    cursor:pointer;

    transition:.12s;
}

.menuButton:hover {
    transform:scale(1.04);
    filter:brightness(1.12);
}

.menuButton:active {
    transform:scale(.97);
}

#continueButton {
    background:#4f8cff;
    color:white;
}

#restartButton,
#gameOverRestart {
    background:#48b96b;
    color:white;
}

#gameOver h1 {
    color:#ff4242;
}

#gameOver h2 {
    font-size:28px;
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


    <!-- 점수 -->
    <div id="scoreBox">
        🏆 점수: <span id="score">0</span>
    </div>

    <!-- 최고기록 -->
    <div id="highScoreBox">
        👑 최고기록: <span id="highScore">0</span>
    </div>


    <div id="game">

        <div id="food">🍎</div>


        <svg id="snakeSVG" viewBox="0 0 648 648">

            <path id="snakeShadow"></path>
            <path id="snakeBody"></path>
            <path id="snakeLight"></path>


            <!-- 뱀 머리 -->

            <g id="headGroup">

                <ellipse
                    cx="0"
                    cy="3"
                    rx="27"
                    ry="23"
                    fill="#17336e"
                    opacity=".35">
                </ellipse>


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
                    stroke-width="3">
                </path>


                <path
                    d="
                    M -17 -16
                    Q -2 -22 10 -14
                    "
                    fill="none"
                    stroke="#6f98ff"
                    stroke-width="6"
                    stroke-linecap="round"
                    opacity=".45">
                </path>


                <!-- 눈 -->

                <circle
                    cx="4"
                    cy="-18"
                    r="10"
                    fill="#f8fbff"
                    stroke="#31528e"
                    stroke-width="2">
                </circle>

                <circle
                    cx="4"
                    cy="18"
                    r="10"
                    fill="#f8fbff"
                    stroke="#31528e"
                    stroke-width="2">
                </circle>


                <circle
                    cx="7"
                    cy="-17"
                    r="4.5"
                    fill="#18234b">
                </circle>

                <circle
                    cx="7"
                    cy="17"
                    r="4.5"
                    fill="#18234b">
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


                <!-- 닫힌 입 -->

                <path
                    id="mouthClosed"
                    d="M 16 -4 Q 21 0 16 4">
                </path>


                <!-- 벌어진 입 -->

                <path
                    id="mouthOpen"
                    d="
                    M 14 -5
                    Q 23 -3 21 2
                    Q 19 8 13 6
                    "
                    fill="#111">
                </path>

            </g>

        </svg>


        <div id="crash">YOU DIE</div>

    </div>


    <!-- 일시정지 -->

    <div id="pauseOverlay" class="overlay">

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


    <!-- 게임오버 -->

    <div id="gameOver" class="overlay">

        <h1>YOU DIE</h1>

        <h2>
            점수:
            <span id="finalScore">0</span>
        </h2>

        <h2>
            👑 최고기록:
            <span id="gameOverHighScore">0</span>
        </h2>

        <button
            id="gameOverRestart"
            class="menuButton">
            🔄 다시하기
        </button>

        <p>R 키를 눌러 다시 시작</p>

    </div>

</div>


<script>

const GRID = 34;
const COLS = 18;
const ROWS = 18;

const MOVE_TIME = 160;


/* =========================
   요소
========================= */

const game =
    document.getElementById("game");

const foodElement =
    document.getElementById("food");

const scoreElement =
    document.getElementById("score");

const highScoreElement =
    document.getElementById("highScore");

const finalScoreElement =
    document.getElementById("finalScore");

const gameOverHighScoreElement =
    document.getElementById("gameOverHighScore");

const gameOverElement =
    document.getElementById("gameOver");

const pauseOverlay =
    document.getElementById("pauseOverlay");

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

const mouthClosed =
    document.getElementById("mouthClosed");

const mouthOpen =
    document.getElementById("mouthOpen");

const continueButton =
    document.getElementById("continueButton");

const restartButton =
    document.getElementById("restartButton");

const gameOverRestart =
    document.getElementById("gameOverRestart");


/* =========================
   변수
========================= */

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

let food;

let score = 0;

let dead = false;

let paused = false;

let lastMoveTime =
    performance.now();

let animationFrame = null;


/* =========================
   최고기록
========================= */

let highScore =
    Number(
        localStorage.getItem(
            "wormHighScore"
        ) || 0
    );

highScoreElement.textContent =
    highScore;


/* =========================
   뱀 초기화
========================= */

function resetSnake() {

    snake = [
        {x:8,y:9},
        {x:7,y:9},
        {x:6,y:9},
        {x:5,y:9},
        {x:4,y:9}
    ];

    previousSnake =
        snake.map(part => ({
            x:part.x,
            y:part.y
        }));
}


/* =========================
   사과 생성
========================= */

function createFood() {

    let valid = false;

    while (!valid) {

        food = {
            x:Math.floor(
                Math.random() * COLS
            ),

            y:Math.floor(
                Math.random() * ROWS
            )
        };

        valid =
            !snake.some(part =>
                part.x === food.x &&
                part.y === food.y
            );
    }
}


/* =========================
   거리 계산
========================= */

function foodDistance() {

    const head = snake[0];

    /*
        격자 기준 거리.
        예:
        바로 옆 = 1칸
        대각선 = 1칸
        두 칸 떨어짐 = 2칸
    */

    return Math.max(
        Math.abs(head.x - food.x),
        Math.abs(head.y - food.y)
    );
}


/* =========================
   입 벌리기
========================= */

function updateMouth() {

    const distance =
        foodDistance();

    /*
        사과와 2칸 이내면 입을 벌림
    */

    if (distance <= 2) {

        mouthClosed.style.display =
            "none";

        mouthOpen.style.display =
            "block";

    } else {

        mouthClosed.style.display =
            "block";

        mouthOpen.style.display =
            "none";
    }
}


/* =========================
   보간
========================= */

function lerp(a,b,t) {
    return a + (b-a) * t;
}


function getAnimatedSnake(progress) {

    return snake.map(
        (part,index) => {

            const oldPart =
                previousSnake[index] ||
                part;

            return {
                x:lerp(
                    oldPart.x,
                    part.x,
                    progress
                ),

                y:lerp(
                    oldPart.y,
                    part.y,
                    progress
                )
            };
        }
    );
}


/* =========================
   몸통
========================= */

function createPath(animatedSnake) {

    const points =
        [...animatedSnake]
        .reverse()
        .map(part => ({
            x:
                part.x * GRID +
                GRID / 2,

            y:
                part.y * GRID +
                GRID / 2
        }));


    if (points.length < 2) {
        return "";
    }


    let path =
        `M ${points[0].x} ${points[0].y}`;


    for (
        let i=1;
        i<points.length-1;
        i++
    ) {

        const a =
            points[i];

        const b =
            points[i+1];

        const midX =
            (a.x+b.x)/2;

        const midY =
            (a.y+b.y)/2;

        path +=
            ` Q ${a.x} ${a.y} ${midX} ${midY}`;
    }


    const last =
        points[points.length-1];

    path +=
        ` L ${last.x} ${last.y}`;

    return path;
}


/* =========================
   머리 방향
========================= */

function getAngle() {

    if (direction.x === 1)
        return 0;

    if (direction.y === 1)
        return 90;

    if (direction.x === -1)
        return 180;

    if (direction.y === -1)
        return -90;

    return 0;
}


/* =========================
   렌더
========================= */

function render(progress=1) {

    const animatedSnake =
        getAnimatedSnake(progress);


    const path =
        createPath(animatedSnake);


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
        animatedSnake[0];


    const x =
        head.x * GRID +
        GRID / 2;

    const y =
        head.y * GRID +
        GRID / 2;


    headGroup.setAttribute(
        "transform",
        `translate(${x} ${y}) rotate(${getAngle()})`
    );


    foodElement.style.left =
        food.x * GRID + "px";

    foodElement.style.top =
        food.y * GRID + "px";


    scoreElement.textContent =
        score;

    highScoreElement.textContent =
        highScore;


    updateMouth();
}


/* =========================
   애니메이션
========================= */

function animate(time) {

    if (dead || paused) {
        return;
    }


    const progress =
        Math.min(
            (time-lastMoveTime) /
            MOVE_TIME,
            1
        );


    const eased =
        progress < .5
        ? 2 * progress * progress
        : 1 - Math.pow(
            -2 * progress + 2,
            2
        ) / 2;


    render(eased);


    animationFrame =
        requestAnimationFrame(
            animate
        );
}


/* =========================
   이동
========================= */

function move() {

    if (dead || paused) {
        return;
    }


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


    previousSnake =
        snake.map(part => ({
            x:part.x,
            y:part.y
        }));


    snake.unshift(newHead);


    /* 사과 */

    if (
        newHead.x === food.x &&
        newHead.y === food.y
    ) {

        score++;


        if (score > highScore) {

            highScore =
                score;

            localStorage.setItem(
                "wormHighScore",
                highScore
            );
        }


        createFood();

    } else {

        snake.pop();
    }


    lastMoveTime =
        performance.now();


    render(0);
}


/* =========================
   YOU DIE
========================= */

function crash(position) {

    dead = true;


    crashElement.style.left =
        position.x * GRID +
        GRID / 2 +
        "px";


    crashElement.style.top =
        position.y * GRID +
        GRID / 2 +
        "px";


    crashElement.style.display =
        "block";


    game.classList.add("shake");


    setTimeout(() => {

        game.classList.remove(
            "shake"
        );


        finalScoreElement.textContent =
            score;

        gameOverHighScoreElement.textContent =
            highScore;

        gameOverElement.style.display =
            "block";

    },500);
}


/* =========================
   일시정지
========================= */

function pauseGame() {

    if (dead || paused) {
        return;
    }


    const now =
        performance.now();


    const progress =
        Math.min(
            (now-lastMoveTime) /
            MOVE_TIME,
            1
        );


    const eased =
        progress < .5
        ? 2 * progress * progress
        : 1 - Math.pow(
            -2 * progress + 2,
            2
        ) / 2;


    render(eased);


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


/* =========================
   계속하기
========================= */

function resumeGame() {

    if (dead) {
        return;
    }


    paused = false;


    pauseOverlay.style.display =
        "none";


    lastMoveTime =
        performance.now();


    animationFrame =
        requestAnimationFrame(
            animate
        );
}


/* =========================
   다시하기
========================= */

function restart() {

    score = 0;

    dead = false;

    paused = false;


    direction = {
        x:1,
        y:0
    };

    nextDirection = {
        x:1,
        y:0
    };


    crashElement.style.display =
        "none";


    gameOverElement.style.display =
        "none";


    pauseOverlay.style.display =
        "none";


    resetSnake();

    createFood();


    lastMoveTime =
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


/* =========================
   버튼
========================= */

continueButton.addEventListener(
    "click",
    resumeGame
);

restartButton.addEventListener(
    "click",
    restart
);

gameOverRestart.addEventListener(
    "click",
    restart
);


/* =========================
   키보드
========================= */

document.addEventListener(
    "keydown",
    function(e) {

        const key =
            e.key.toLowerCase();


        /* ESC */

        if (key === "escape") {

            e.preventDefault();


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


        /* 일시정지 중 */

        if (paused) {
            return;
        }


        /* 위 */

        if (
            (key === "w" ||
             key === "arrowup") &&
            direction.y !== 1
        ) {

            nextDirection = {
                x:0,
                y:-1
            };
        }


        /* 아래 */

        if (
            (key === "s" ||
             key === "arrowdown") &&
            direction.y !== -1
        ) {

            nextDirection = {
                x:0,
                y:1
            };
        }


        /* 왼쪽 */

        if (
            (key === "a" ||
             key === "arrowleft") &&
            direction.x !== 1
        ) {

            nextDirection = {
                x:-1,
                y:0
            };
        }


        /* 오른쪽 */

        if (
            (key === "d" ||
             key === "arrowright") &&
            direction.x !== -1
        ) {

            nextDirection = {
                x:1,
                y:0
            };
        }

    }
);


/* =========================
   시작
========================= */

resetSnake();

createFood();

render(1);

animationFrame =
    requestAnimationFrame(
        animate
    );


setInterval(
    move,
    MOVE_TIME
);

</script>

</body>
</html>
""", height=820)
