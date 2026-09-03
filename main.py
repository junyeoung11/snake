

```python
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

components.html(r"""
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


/* =========================
   점수
========================= */

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


/* =========================
   질주 UI
========================= */

#dashBox {
    position:absolute;

    left:50%;
    top:18px;

    transform:translateX(-50%);

    z-index:110;

    background:rgba(0,0,0,.78);

    color:white;

    padding:10px 18px;

    border-radius:15px;

    font-size:17px;

    font-weight:bold;

    white-space:nowrap;
}

#dashStatus {
    color:#6eff91;
}


/* =========================
   사과
========================= */

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

    filter:drop-shadow(
        0 3px 3px rgba(0,0,0,.35)
    );
}

@keyframes applePulse {

    0% {
        transform:scale(.72);
    }

    50% {
        transform:scale(1.15);
    }

    100% {
        transform:scale(.72);
    }
}


/* =========================
   뱀
========================= */

#snakeSVG {
    position:absolute;

    width:648px;
    height:648px;

    left:0;
    top:0;

    overflow:visible;

    pointer-events:none;

    z-index:30;
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
   머리
========================= */

#headGroup {
    transition:transform .04s linear;
}


/* 닫힌 입 */

#mouthClosed {
    fill:none;

    stroke:#102b63;

    stroke-width:3;

    stroke-linecap:round;
}


/* 벌어진 입 */

#mouthOpenGroup {
    display:none;
}

#openMouth {
    fill:#111;

    stroke:#081535;

    stroke-width:2;
}

#tongue {
    fill:#ff4b55;

    stroke:#b51f2c;

    stroke-width:1.5;
}

.tooth {
    fill:white;

    stroke:#cfd7e5;

    stroke-width:1;
}


/* =========================
   질주 바람
========================= */

#windLayer {
    display:none;
}

.wind {
    fill:none;

    stroke:white;

    stroke-width:4;

    stroke-linecap:round;

    opacity:0;
}

.dashActive #windLayer {
    display:block;
}

.dashActive .wind1 {
    animation:windMove .28s infinite;
}

.dashActive .wind2 {
    animation:windMove .38s infinite .08s;
}

.dashActive .wind3 {
    animation:windMove .32s infinite .15s;
}

.dashActive .wind4 {
    animation:windMove .42s infinite .05s;
}

@keyframes windMove {

    0% {
        opacity:0;

        transform:
            translateX(18px)
            scaleX(.4);
    }

    30% {
        opacity:.8;
    }

    100% {
        opacity:0;

        transform:
            translateX(-35px)
            scaleX(1.3);
    }
}


/* =========================
   질주 잔상
========================= */

#dashTrail {
    display:none;

    fill:none;

    stroke:#b7d6ff;

    stroke-width:9;

    stroke-linecap:round;

    opacity:.4;

    stroke-dasharray:15 15;
}

.dashing #dashTrail {
    display:block;

    animation:
        trailMove .25s linear infinite;
}

@keyframes trailMove {

    from {
        stroke-dashoffset:0;
    }

    to {
        stroke-dashoffset:-30;
    }
}


/* =========================
   충돌
========================= */

#crash {
    position:absolute;

    display:none;

    font-size:78px;

    z-index:300;

    transform:
        translate(-50%,-50%);

    filter:
        drop-shadow(
            0 4px 4px rgba(0,0,0,.5)
        );

    animation:
        crashPop .45s ease-out;
}

@keyframes crashPop {

    0% {
        transform:
            translate(-50%,-50%)
            scale(.2)
            rotate(-20deg);
    }

    60% {
        transform:
            translate(-50%,-50%)
            scale(1.25)
            rotate(8deg);
    }

    100% {
        transform:
            translate(-50%,-50%)
            scale(1)
            rotate(0deg);
    }
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
   일시정지 / 게임오버
========================= */

.overlay {
    position:absolute;

    left:50%;
    top:50%;

    transform:
        translate(-50%,-50%);

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


/* =========================
   질주 시작 효과
========================= */

#game.dashFlash::after {
    content:"";

    position:absolute;

    inset:0;

    pointer-events:none;

    background:
        radial-gradient(
            circle,
            transparent 45%,
            rgba(255,255,255,.15)
        );

    animation:
        dashFlash .18s;
}

@keyframes dashFlash {

    from {
        opacity:1;
    }

    to {
        opacity:0;
    }
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
        🏆 점수:
        <span id="score">0</span>
    </div>


    <!-- 최고기록 -->

    <div id="highScoreBox">
        👑 최고기록:
        <span id="highScore">0</span>
    </div>


    <!-- 질주 상태 -->

    <div id="dashBox">
        ⚡ 질주:
        <span id="dashStatus">준비</span>
    </div>


    <div id="game">

        <!-- 사과 -->

        <div id="food">🍎</div>


        <svg
            id="snakeSVG"
            viewBox="0 0 648 648"
        >

            <path id="snakeShadow"></path>

            <path id="snakeBody"></path>

            <path id="snakeLight"></path>


            <!-- 질주 잔상 -->

            <path id="dashTrail"></path>


            <!-- 바람 -->

            <g id="windLayer">

                <path
                    class="wind wind1"
                    d="M 0 -12 Q -30 -20 -55 -12">
                </path>

                <path
                    class="wind wind2"
                    d="M 0 0 Q -38 -5 -68 5">
                </path>

                <path
                    class="wind wind3"
                    d="M 0 12 Q -30 20 -58 14">
                </path>

                <path
                    class="wind wind4"
                    d="M -5 22 Q -35 28 -50 25">
                </path>

            </g>


            <!-- 머리 -->

            <g id="headGroup">

                <ellipse
                    cx="0"
                    cy="4"
                    rx="28"
                    ry="24"
                    fill="#17336e"
                    opacity=".35">
                </ellipse>


                <path
                    d="
                    M -18 -21
                    Q 4 -28 21 -15
                    Q 34 0 21 15
                    Q 4 28 -18 21
                    Q -30 11 -30 0
                    Q -30 -11 -18 -21
                    "

                    fill="#315fc9"
                    stroke="#244a9f"
                    stroke-width="3">
                </path>


                <path
                    d="M -17 -17 Q -2 -23 10 -15"
                    fill="none"
                    stroke="#6f98ff"
                    stroke-width="6"
                    stroke-linecap="round"
                    opacity=".5">
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
                    d="M 16 -5 Q 23 0 16 5">
                </path>


                <!-- 벌어진 입 -->

                <g id="mouthOpenGroup">

                    <path
                        id="openMouth"
                        d="
                        M 12 -8
                        Q 25 -9 27 0
                        Q 25 9 12 8
                        Q 17 0 12 -8
                        ">
                    </path>


                    <path
                        id="tongue"
                        d="
                        M 16 3
                        Q 21 0 25 3
                        Q 21 10 16 6
                        Z
                        ">
                    </path>


                    <path
                        class="tooth"
                        d="M 16 -7 L 19 -2 L 22 -7 Z">
                    </path>

                    <path
                        class="tooth"
                        d="M 22 -7 L 25 -2 L 27 -6 Z">
                    </path>

                    <path
                        class="tooth"
                        d="M 17 7 L 20 3 L 22 8 Z">
                    </path>

                </g>

            </g>

        </svg>


        <!-- 충돌 -->

        <div id="crash">💥</div>

    </div>


    <!-- =====================
         일시정지
    ====================== -->

    <div
        id="pauseOverlay"
        class="overlay"
    >

        <h1>일시정지</h1>

        <button
            id="continueButton"
            class="menuButton"
        >
            ▶️ 계속하기
        </button>

        <button
            id="restartButton"
            class="menuButton"
        >
            🔄 다시하기
        </button>

    </div>


    <!-- =====================
         게임오버
    ====================== -->

    <div
        id="gameOver"
        class="overlay"
    >

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
            class="menuButton"
        >
            🔄 다시하기
        </button>

        <p>R 키를 눌러 다시 시작</p>

    </div>

</div>


<script>

/* =========================
   게임 설정
========================= */

const GRID = 34;

const COLS = 18;

const ROWS = 18;


/* 일반 속도 */

const NORMAL_MOVE_TIME = 160;


/* 질주 속도 */

const DASH_MOVE_TIME = 65;


/* 최대 질주 시간 */

const DASH_DURATION = 2000;


/* 쿨타임 */

const DASH_COOLDOWN = 10000;


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

const dashStatus =
    document.getElementById("dashStatus");

const finalScoreElement =
    document.getElementById("finalScore");

const gameOverHighScoreElement =
    document.getElementById(
        "gameOverHighScore"
    );

const gameOverElement =
    document.getElementById(
        "gameOver"
    );

const pauseOverlay =
    document.getElementById(
        "pauseOverlay"
    );

const crashElement =
    document.getElementById(
        "crash"
    );

const snakeBody =
    document.getElementById(
        "snakeBody"
    );

const snakeShadow =
    document.getElementById(
        "snakeShadow"
    );

const snakeLight =
    document.getElementById(
        "snakeLight"
    );

const dashTrail =
    document.getElementById(
        "dashTrail"
    );

const headGroup =
    document.getElementById(
        "headGroup"
    );

const mouthClosed =
    document.getElementById(
        "mouthClosed"
    );

const mouthOpenGroup =
    document.getElementById(
        "mouthOpenGroup"
    );

const continueButton =
    document.getElementById(
        "continueButton"
    );

const restartButton =
    document.getElementById(
        "restartButton"
    );

const gameOverRestart =
    document.getElementById(
        "gameOverRestart"
    );


/* =========================
   게임 변수
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

let food = {
    x:10,
    y:9
};

let score = 0;

let dead = false;

let paused = false;


/* =========================
   질주 변수
========================= */

let dashing = false;


/*
   질주가 끝나는 시간
*/

let dashEndTime = 0;


/*
   마지막으로 질주를 시작한 시간
*/

let lastDashTime = -Infinity;


/*
   LShift가 현재 눌려 있는지
*/

let shiftHeld = false;


/* =========================
   이동 시간
========================= */

function getMoveTime() {

    if (dashing) {
        return DASH_MOVE_TIME;
    }

    return NORMAL_MOVE_TIME;
}


/* =========================
   애니메이션
========================= */

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

            x:
                Math.floor(
                    Math.random() * COLS
                ),

            y:
                Math.floor(
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
   사과 거리
========================= */

function foodDistance() {

    const head = snake[0];

    return Math.max(

        Math.abs(
            head.x - food.x
        ),

        Math.abs(
            head.y - food.y
        )
    );
}


/* =========================
   입
========================= */

function updateMouth() {

    if (dead) {
        return;
    }


    if (foodDistance() <= 2) {

        mouthClosed.style.display =
            "none";

        mouthOpenGroup.style.display =
            "block";

    } else {

        mouthClosed.style.display =
            "block";

        mouthOpenGroup.style.display =
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

                x:
                    lerp(
                        oldPart.x,
                        part.x,
                        progress
                    ),

                y:
                    lerp(
                        oldPart.y,
                        part.y,
                        progress
                    )
            };
        }
    );
}


/* =========================
   몸통 경로
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
   화면 그리기
========================= */

function render(progress=1) {

    const animatedSnake =
        getAnimatedSnake(progress);


    const path =
        createPath(
            animatedSnake
        );


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
   질주 UI
========================= */

function updateDashUI() {

    const now =
        performance.now();


    if (dashing) {

        const remaining =
            Math.max(
                0,
                dashEndTime - now
            );


        dashStatus.textContent =
            "🔥 질주 " +
            (
                remaining / 1000
            ).toFixed(1) +
            "초";


        dashStatus.style.color =
            "#ffcc4d";

        return;
    }


    const elapsed =
        now - lastDashTime;


    if (
        lastDashTime === -Infinity ||
        elapsed >= DASH_COOLDOWN
    ) {

        dashStatus.textContent =
            "준비 ⚡";

        dashStatus.style.color =
            "#6eff91";

    } else {

        const remaining =
            Math.ceil(
                (
                    DASH_COOLDOWN -
                    elapsed
                ) / 1000
            );


        dashStatus.textContent =
            "쿨타임 " +
            remaining +
            "초";

        dashStatus.style.color =
            "#ff7777";
    }
}


/* =========================
   애니메이션
========================= */

function animate(time) {

    if (dead || paused) {
        return;
    }


    /*
       2초가 지나면
       자동으로 질주 종료
    */

    if (
        dashing &&
        time >= dashEndTime
    ) {

        stopDash();
    }


    const moveTime =
        getMoveTime();


    const progress =
        Math.min(
            (
                time -
                lastMoveTime
            ) / moveTime,
            1
        );


    const eased =
        progress < .5

        ? 2 * progress * progress

        : 1 -
          Math.pow(
              -2 * progress + 2,
              2
          ) / 2;


    render(eased);

    updateDashUI();


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
            head.x +
            direction.x,

        y:
            head.y +
            direction.y
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


    previousSnake =
        snake.map(part => ({
            x:part.x,
            y:part.y
        }));


    snake.unshift(
        newHead
    );


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
   질주 시작
========================= */

function startDash() {

    if (
        dead ||
        paused ||
        dashing
    ) {
        return;
    }


    const now =
        performance.now();


    /*
       쿨타임 검사
    */

    if (
        now - lastDashTime <
        DASH_COOLDOWN
    ) {

        return;
    }


    dashing = true;


    lastDashTime =
        now;


    dashEndTime =
        now + DASH_DURATION;


    game.classList.add(
        "dashing"
    );

    game.classList.add(
        "dashActive"
    );

    game.classList.add(
        "dashFlash"
    );


    setTimeout(() => {

        game.classList.remove(
            "dashFlash"
        );

    },180);


    lastMoveTime =
        now;


    updateDashUI();
}


/* =========================
   질주 종료
========================= */

function stopDash() {

    if (!dashing) {
        return;
    }


    dashing = false;


    game.classList.remove(
        "dashing"
    );

    game.classList.remove(
        "dashActive"
    );


    lastMoveTime =
        performance.now();


    updateDashUI();
}


/* =========================
   충돌
========================= */

function crash(position) {

    dead = true;


    stopDash();


    mouthClosed.style.display =
        "block";

    mouthOpenGroup.style.display =
        "none";


    crashElement.textContent =
        "💥";


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


    game.classList.add(
        "shake"
    );


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

            (
                now -
                lastMoveTime
            ) /
            getMoveTime(),

            1
        );


    render(progress);


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


    /*
       일시정지 중에는
       질주 시간이 지나지 않도록
       다시 기준점을 잡음
    */

    if (dashing) {

        /*
           일시정지 상태에서
           Shift가 눌려 있었다면
           남은 질주 시간을 유지
        */

        const remaining =
            Math.max(
                0,
                dashEndTime -
                performance.now()
            );

        dashEndTime =
            performance.now() +
            remaining;
    }


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

    dashing = false;

    shiftHeld = false;

    lastDashTime = -Infinity;


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


    game.classList.remove(
        "dashing"
    );

    game.classList.remove(
        "dashActive"
    );


    resetSnake();

    createFood();


    lastMoveTime =
        performance.now();


    render(1);

    updateDashUI();


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


        /* =====================
           LSHIFT 누름
        ====================== */

        if (
            e.code === "ShiftLeft"
        ) {

            e.preventDefault();


            /*
               이미 누르고 있다면
               다시 발동하지 않음
            */

            if (!shiftHeld) {

                shiftHeld = true;

                startDash();
            }


            return;
        }


        /* =====================
           ESC
        ====================== */

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


        /* =====================
           R
        ====================== */

        if (
            key === "r" &&
            dead
        ) {

            restart();

            return;
        }


        if (paused) {
            return;
        }


        /* =====================
           방향키
        ====================== */

        if (

            (
                key === "w" ||
                key === "arrowup"
            )

            &&

            direction.y !== 1

        ) {

            nextDirection = {
                x:0,
                y:-1
            };
        }


        if (

            (
                key === "s" ||
                key === "arrowdown"
            )

            &&

            direction.y !== -1

        ) {

            nextDirection = {
                x:0,
                y:1
            };
        }


        if (

            (
                key === "a" ||
                key === "arrowleft"
            )

            &&

            direction.x !== 1

        ) {

            nextDirection = {
                x:-1,
                y:0
            };
        }


        if (

            (
                key === "d" ||
                key === "arrowright"
            )

            &&

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
   LShift 떼기
========================= */

document.addEventListener(
    "keyup",
    function(e) {

        if (
            e.code === "ShiftLeft"
        ) {

            shiftHeld = false;


            /*
               핵심:
               Shift를 떼는 순간
               질주 즉시 종료
            */

            if (dashing) {

                stopDash();
            }
        }

    }
);


/* =========================
   창을 벗어나도
   Shift가 풀리도록 처리
========================= */

window.addEventListener(
    "blur",
    function() {

        shiftHeld = false;


        if (dashing) {

            stopDash();
        }
    }
);


/* =========================
   시작
========================= */

resetSnake();

createFood();

render(1);

updateDashUI();


animationFrame =
    requestAnimationFrame(
        animate
    );


/*
   15ms마다 이동 체크
*/

setInterval(
    function() {

        if (dead || paused) {
            return;
        }


        const now =
            performance.now();


        const interval =
            getMoveTime();


        if (
            now - lastMoveTime >=
            interval
        ) {

            move();
        }

    },
    15
);

</script>

</body>
</html>
""", height=820)
```
