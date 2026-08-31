import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🪱 지렁이 게임",
    page_icon="🪱",
    layout="centered"
)

st.title("🪱 지렁이 게임")
st.caption("🎮 WASD 또는 방향키로 움직이세요!")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        background: #111;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    }

    canvas {
        background: #181818;
        border: 3px solid #4CAF50;
        border-radius: 15px;
        box-shadow: 0 0 30px rgba(76, 175, 80, 0.5);
    }
</style>
</head>

<body>

<canvas id="game" width="700" height="500"></canvas>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const gridSize = 20;

let snake = [
    {x: 300, y: 240},
    {x: 280, y: 240},
    {x: 260, y: 240}
];

let direction = {x: 20, y: 0};
let nextDirection = {x: 20, y: 0};

let score = 0;
let gameOver = false;

let food = {
    x: Math.floor(Math.random() * 35) * gridSize,
    y: Math.floor(Math.random() * 25) * gridSize
};


// 🍎 먹이 생성
function createFood() {

    let newFood;

    do {
        newFood = {
            x: Math.floor(Math.random() * 35) * gridSize,
            y: Math.floor(Math.random() * 25) * gridSize
        };
    } while (
        snake.some(
            part => part.x === newFood.x &&
                    part.y === newFood.y
        )
    );

    return newFood;
}


// ⌨️ 키보드 조작
document.addEventListener("keydown", function(event) {

    const key = event.key.toLowerCase();

    if (
        ["arrowup", "arrowdown", "arrowleft", "arrowright",
         "w", "a", "s", "d"].includes(key)
    ) {
        event.preventDefault();
    }


    // 🔼 위
    if (key === "arrowup" || key === "w") {

        if (direction.y !== 20) {
            nextDirection = {x: 0, y: -20};
        }

    }

    // 🔽 아래
    if (key === "arrowdown" || key === "s") {

        if (direction.y !== -20) {
            nextDirection = {x: 0, y: 20};
        }

    }

    // ◀️ 왼쪽
    if (key === "arrowleft" || key === "a") {

        if (direction.x !== 20) {
            nextDirection = {x: -20, y: 0};
        }

    }

    // ▶️ 오른쪽
    if (key === "arrowright" || key === "d") {

        if (direction.x !== -20) {
            nextDirection = {x: 20, y: 0};
        }

    }

    // 🔄 다시 시작
    if (key === "r" && gameOver) {
        restartGame();
    }

});


// 🪱 게임 업데이트
function update() {

    if (gameOver) return;

    direction = nextDirection;

    const head = {
        x: snake[0].x + direction.x,
        y: snake[0].y + direction.y
    };


    // 💥 벽 충돌
    if (
        head.x < 0 ||
        head.x >= canvas.width ||
        head.y < 0 ||
        head.y >= canvas.height
    ) {
        gameOver = true;
        return;
    }


    // 💥 자기 몸 충돌
    if (
        snake.some(
            part => part.x === head.x &&
                    part.y === head.y
        )
    ) {
        gameOver = true;
        return;
    }


    snake.unshift(head);


    // 🍎 먹이 먹기
    if (head.x === food.x && head.y === food.y) {

        score++;

        food = createFood();

    } else {

        snake.pop();

    }

}


// 🎨 화면 그리기
function draw() {

    // 배경
    ctx.fillStyle = "#181818";
    ctx.fillRect(0, 0, canvas.width, canvas.height);


    // 격자
    ctx.strokeStyle = "#222";
    ctx.lineWidth = 1;

    for (let x = 0; x < canvas.width; x += gridSize) {

        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();

    }

    for (let y = 0; y < canvas.height; y += gridSize) {

        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();

    }


    // 🍎 먹이
    ctx.font = "20px Arial";
    ctx.fillText("🍎", food.x, food.y + 18);


    // 🪱 지렁이
    snake.forEach((part, index) => {

        ctx.fillStyle =
            index === 0 ? "#5CFF72" : "#28A745";

        ctx.beginPath();

        ctx.roundRect(
            part.x + 1,
            part.y + 1,
            gridSize - 2,
            gridSize - 2,
            6
        );

        ctx.fill();

    });


    // 👀 눈
    const head = snake[0];

    ctx.fillStyle = "white";

    ctx.beginPath();
    ctx.arc(head.x + 6, head.y + 6, 3, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(head.x + 14, head.y + 6, 3, 0, Math.PI * 2);
    ctx.fill();


    // 🏆 점수
    ctx.fillStyle = "white";
    ctx.font = "bold 22px Arial";
    ctx.fillText("🏆 SCORE: " + score, 15, 30);


    // 💀 게임오버
    if (gameOver) {

        ctx.fillStyle = "rgba(0,0,0,0.7)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = "#ff4d4d";
        ctx.font = "bold 50px Arial";
        ctx.textAlign = "center";

        ctx.fillText(
            "GAME OVER 💀",
            canvas.width / 2,
            canvas.height / 2 - 40
        );

        ctx.fillStyle = "white";
        ctx.font = "25px Arial";

        ctx.fillText(
            "최종 점수: " + score,
            canvas.width / 2,
            canvas.height / 2 + 10
        );

        ctx.fillStyle = "#FFD700";
        ctx.font = "20px Arial";

        ctx.fillText(
            "R키를 눌러 다시 시작",
            canvas.width / 2,
            canvas.height / 2 + 60
        );

        ctx.textAlign = "left";

    }

}


// 🔄 게임 재시작
function restartGame() {

    snake = [
        {x: 300, y: 240},
        {x: 280, y: 240},
        {x: 260, y: 240}
    ];

    direction = {x: 20, y: 0};
    nextDirection = {x: 20, y: 0};

    score = 0;

    food = createFood();

    gameOver = false;

}


// 🎮 게임 루프
setInterval(function() {

    update();
    draw();

}, 120);

</script>

</body>
</html>
""", height=550)
