```python
import streamlit as st
import streamlit.components.v1 as components
import random
import json

# =========================================================
# Streamlit 설정
# =========================================================

st.set_page_config(
    page_title="WORM QUEST",
    page_icon="🪱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# Session State
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "main"

if "coins" not in st.session_state:
    st.session_state.coins = 0

if "high_score" not in st.session_state:
    st.session_state.high_score = 0

if "owned_worms" not in st.session_state:
    st.session_state.owned_worms = ["basic"]

if "equipped_worm" not in st.session_state:
    st.session_state.equipped_worm = "basic"


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #101810;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    padding-top: 1rem;
    max-width: 950px;
}

.main-title {
    text-align: center;
    color: white;
    font-size: 70px;
    font-weight: 900;
    margin-top: 40px;
}

.sub-title {
    text-align: center;
    color: #9eb69e;
    font-size: 20px;
    margin-bottom: 35px;
}

.stat-box {
    background: #1b261d;
    border: 1px solid #344737;
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

.shop-card {
    background: #1b261d;
    border: 2px solid #344737;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    color: white;
    margin-bottom: 15px;
}

.worm-big {
    font-size: 75px;
    text-align: center;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 메인 화면
# =========================================================

def main_page():

    st.markdown(
        '<div class="main-title">🪱 WORM QUEST</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">먹고 · 성장하고 · 질주하라</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"""
            <div class="stat-box">
                🪙 {st.session_state.coins}
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="stat-box">
                🏆 {st.session_state.high_score}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "🎮 게임 시작하기",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.page = "game"
            st.rerun()

    with c2:
        if st.button(
            "🛒 상점",
            use_container_width=True
        ):
            st.session_state.page = "shop"
            st.rerun()

    st.markdown(
        '<div class="worm-big">🪱</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 상점
# =========================================================

WORMS = {
    "basic": {
        "name": "기본 지렁이",
        "emoji": "🪱",
        "price": 0,
        "skill": "기본 질주"
    },
    "fire": {
        "name": "화염 지렁이",
        "emoji": "🔥",
        "price": 500,
        "skill": "화염 질주"
    },
    "lightning": {
        "name": "번개 지렁이",
        "emoji": "⚡",
        "price": 1000,
        "skill": "번개 질주"
    },
    "ghost": {
        "name": "유령 지렁이",
        "emoji": "👻",
        "price": 2000,
        "skill": "유령화"
    },
    "rainbow": {
        "name": "무지개 지렁이",
        "emoji": "🌈",
        "price": 3000,
        "skill": "무지개 질주"
    }
}


def shop_page():

    top1, top2 = st.columns([3, 1])

    with top1:
        st.title("🛒 지렁이 상점")

    with top2:
        st.markdown(
            f"""
            <div class="stat-box">
                🪙 {st.session_state.coins}
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("← 메인으로"):
        st.session_state.page = "main"
        st.rerun()

    st.divider()

    cols = st.columns(2)

    for index, (worm_id, worm) in enumerate(WORMS.items()):

        with cols[index % 2]:

            owned = worm_id in st.session_state.owned_worms
            equipped = (
                worm_id ==
                st.session_state.equipped_worm
            )

            status = (
                "✅ 장착 중"
                if equipped
                else
                "⚡ 장착"
                if owned
                else
                f"🪙 {worm['price']} 구매"
            )

            st.markdown(
                f"""
                <div class="shop-card">

                    <div style="font-size:65px;">
                        {worm['emoji']}
                    </div>

                    <h3>
                        {worm['name']}
                    </h3>

                    <p>
                        ⚡ {worm['skill']}
                    </p>

                    <p>
                        가격: 🪙 {worm['price']}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                status,
                key=f"worm_{worm_id}",
                use_container_width=True
            ):

                if equipped:
                    pass

                elif owned:

                    st.session_state.equipped_worm = worm_id
                    st.rerun()

                else:

                    if (
                        st.session_state.coins
                        >= worm["price"]
                    ):

                        st.session_state.coins -= \
                            worm["price"]

                        st.session_state.owned_worms.append(
                            worm_id
                        )

                        st.session_state.equipped_worm = \
                            worm_id

                        st.rerun()

                    else:
                        st.error("🪙 코인이 부족합니다!")


# =========================================================
# 게임
# =========================================================

def game_page():

    if st.button("← 메인으로"):
        st.session_state.page = "main"
        st.rerun()

    worm_id = st.session_state.equipped_worm
    worm = WORMS[worm_id]

    game_html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

* {{
    box-sizing:border-box;
    user-select:none;
}}

body {{
    margin:0;
    background:#101810;
    font-family:Arial,sans-serif;
    overflow:hidden;
}}

#game {{
    width:650px;
    height:720px;
    margin:auto;
    position:relative;
}}

#board {{
    width:612px;
    height:612px;
    position:absolute;
    top:60px;
    left:19px;

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
        #9dcc4a;

    background-size:34px 34px;

    border:10px solid #214ba0;
    border-radius:20px;

    overflow:hidden;
}}

#snake {{
    position:absolute;
    width:612px;
    height:612px;
    left:0;
    top:0;
    pointer-events:none;
}}

#body {{
    fill:none;
    stroke:{worm["color"] if "color" in worm else "#315fc9"};
    stroke-width:31;
    stroke-linecap:round;
    stroke-linejoin:round;
}}

#light {{
    fill:none;
    stroke:#8fb0ff;
    stroke-width:5;
    stroke-linecap:round;
}}

#head {{
    fill:{worm["color"] if "color" in worm else "#315fc9"};
}}

#mouth {{
    stroke:#111;
    stroke-width:4;
    fill:none;
}}

#openMouth {{
    display:none;
}}

#apple {{
    position:absolute;
    width:34px;
    height:34px;
    font-size:30px;
    z-index:20;
    animation:pulse .8s infinite;
}}

@keyframes pulse {{
    0% {{transform:scale(.8);}}
    50% {{transform:scale(1.15);}}
    100% {{transform:scale(.8);}}
}}

#info {{
    position:absolute;
    top:5px;
    left:20px;
    color:white;
    font-weight:bold;
    font-size:18px;
}}

#high {{
    position:absolute;
    top:5px;
    right:20px;
    color:#ffd84d;
    font-weight:bold;
}}

#quest {{
    position:absolute;
    top:40px;
    right:20px;
    width:160px;
    padding:9px;

    color:white;
    background:rgba(0,0,0,.75);
    border-radius:10px;

    font-size:11px;
    z-index:100;
}}

#skill {{
    position:absolute;
    top:40px;
    left:20px;
    color:white;
    background:rgba(0,0,0,.75);
    border-radius:10px;
    padding:7px 10px;
    font-size:12px;
}}

#pause,
#gameover {{
    display:none;

    position:absolute;

    left:50%;
    top:50%;

    transform:translate(-50%,-50%);

    width:430px;

    padding:35px;

    background:rgba(0,0,0,.96);

    border-radius:25px;

    color:white;

    text-align:center;

    z-index:500;
}}

#pause h1,
#gameover h1 {{
    font-size:52px;
}}

.pauseBtn {{
    width:270px;
    height:55px;
    margin:7px;

    border:0;
    border-radius:13px;

    color:white;
    font-size:19px;
    font-weight:bold;
}}

#continue {{
    background:#477fe5;
}}

#restart {{
    background:#43b96a;
}}

#gameover h1 {{
    color:#ff4040;
}}

#boom {{
    display:none;

    position:absolute;

    font-size:70px;

    z-index:300;
}}

</style>

</head>

<body>

<div id="game">

    <div id="info">
        점수: <span id="score">0</span>
        &nbsp;&nbsp;
        🪙 <span id="coins">0</span>
    </div>

    <div id="high">
        🏆 최고기록: <span id="highScore">0</span>
    </div>

    <div id="skill">
        ⚡ {worm["skill"]}
        <br>
        <span id="skillStatus">READY</span>
    </div>

    <div id="quest">
        <b style="color:#ffd84d;">📜 QUEST</b>
        <div id="questText">
            🍎 사과 먹기 0/5
        </div>
    </div>

    <div id="board">

        <div id="apple">🍎</div>

        <svg id="snake" viewBox="0 0 612 612">

            <path id="body"></path>

            <path id="light"></path>

            <g id="headGroup">

                <circle
                    id="head"
                    cx="0"
                    cy="0"
                    r="18">
                </circle>

                <circle
                    cx="7"
                    cy="-12"
                    r="7"
                    fill="white">
                </circle>

                <circle
                    cx="7"
                    cy="12"
                    r="7"
                    fill="white">
                </circle>

                <circle
                    cx="9"
                    cy="-12"
                    r="3"
                    fill="black">
                </circle>

                <circle
                    cx="9"
                    cy="12"
                    r="3"
                    fill="black">
                </circle>

                <path
                    id="mouth"
                    d="M12,-4 Q20,0 12,4">
                </path>

                <g id="openMouth">

                    <ellipse
                        cx="14"
                        cy="0"
                        rx="9"
                        ry="7"
                        fill="#111">
                    </ellipse>

                    <path
                        d="M10,3 Q14,9 18,3"
                        stroke="#ff4c62"
                        stroke-width="3"
                        fill="none">
                    </path>

                </g>

            </g>

        </svg>

        <div id="boom">💥</div>

        <div id="pause">

            <h1>일시정지</h1>

            <button
                class="pauseBtn"
                id="continue">
                ▶️ 계속하기
            </button>

            <button
                class="pauseBtn"
                id="restart">
                🔄 다시하기
            </button>

        </div>

        <div id="gameover">

            <h1>YOU DIE</h1>

            <h2>
                점수:
                <span id="finalScore">0</span>
            </h2>

            <button
                class="pauseBtn"
                id="restart2">
                🔄 다시하기
            </button>

        </div>

    </div>

</div>


<script>

const GRID = 34;
const SIZE = 18;

let snake;
let oldSnake;

let direction;
let nextDirection;

let apple;

let score = 0;

let dead = false;
let paused = false;

let lastMove = performance.now();

let shiftHeld = false;
let dash = false;

let dashStart = 0;
let lastDash = -10000;

const DASH_TIME = 2000;
const DASH_COOLDOWN = 10000;


/* =========================================
   시작
========================================= */

function startGame() {{

    snake = [
        {{x:8,y:9}},
        {{x:7,y:9}},
        {{x:6,y:9}},
        {{x:5,y:9}},
        {{x:4,y:9}}
    ];

    oldSnake =
        snake.map(p => ({{...p}}));

    direction = {{x:1,y:0}};
    nextDirection = {{x:1,y:0}};

    score = 0;

    dead = false;
    paused = false;

    document.getElementById(
        "pause"
    ).style.display="none";

    document.getElementById(
        "gameover"
    ).style.display="none";

    document.getElementById(
        "boom"
    ).style.display="none";

    spawnApple();

    lastMove = performance.now();

    requestAnimationFrame(loop);
}}


/* =========================================
   사과
========================================= */

function spawnApple(){{

    do {{

        apple = {{
            x:Math.floor(Math.random()*SIZE),
            y:Math.floor(Math.random()*SIZE)
        }};

    }}while(
        snake.some(
            p =>
                p.x===apple.x &&
                p.y===apple.y
        )
    );
}}


/* =========================================
   이동
========================================= */

function moveSnake(){{

    if(dead || paused) return;

    direction = nextDirection;

    const head = snake[0];

    const next = {{
        x:head.x+direction.x,
        y:head.y+direction.y
    }};

    if(
        next.x<0 ||
        next.x>=SIZE ||
        next.y<0 ||
        next.y>=SIZE
    ){{

        die(next);
        return;
    }}

    if(
        snake.some(
            p =>
                p.x===next.x &&
                p.y===next.y
        )
    ){{

        die(next);
        return;
    }}

    oldSnake =
        snake.map(p => ({{...p}}));

    snake.unshift(next);

    if(
        next.x===apple.x &&
        next.y===apple.y
    ){{

        score++;

        spawnApple();

        document.getElementById(
            "score"
        ).textContent=score;

        updateQuest();

    }}else{{

        snake.pop();
    }}

    lastMove=performance.now();
}}


/* =========================================
   부드러운 렌더링
========================================= */

function lerp(a,b,t){{

    return a+(b-a)*t;
}}


function render(progress){{

    const points =
        snake.map(
            (p,i)=>{{

                const old =
                    oldSnake[i] || p;

                return {{
                    x:lerp(old.x,p.x,progress),
                    y:lerp(old.y,p.y,progress)
                }};
            }}
        );

    if(points.length<2) return;

    let path =
        "M "+
        (
            points[points.length-1].x*GRID+17
        )+
        " "+
        (
            points[points.length-1].y*GRID+17
        );

    for(
        let i=points.length-2;
        i>=0;
        i--
    ){{

        path +=
            " L "+
            (
                points[i].x*GRID+17
            )+
            " "+
            (
                points[i].y*GRID+17
            );
    }}

    document.getElementById(
        "body"
    ).setAttribute("d",path);

    document.getElementById(
        "light"
    ).setAttribute("d",path);


    const head = points[0];

    let angle=0;

    if(direction.x===1) angle=0;
    if(direction.y===1) angle=90;
    if(direction.x===-1) angle=180;
    if(direction.y===-1) angle=-90;

    document.getElementById(
        "headGroup"
    ).setAttribute(
        "transform",
        `translate(${{head.x*GRID+17}}
        ${{head.y*GRID+17}})
        rotate(${{angle}})`
    );


    document.getElementById(
        "apple"
    ).style.left =
        apple.x*GRID+"px";

    document.getElementById(
        "apple"
    ).style.top =
        apple.y*GRID+"px";


    const dist =
        Math.max(
            Math.abs(
                snake[0].x-apple.x
            ),
            Math.abs(
                snake[0].y-apple.y
            )
        );


    if(dist<=2){{

        document.getElementById(
            "mouth"
        ).style.display="none";

        document.getElementById(
            "openMouth"
        ).style.display="block";

    }}else{{

        document.getElementById(
            "mouth"
        ).style.display="block";

        document.getElementById(
            "openMouth"
        ).style.display="none";
    }}
}}


/* =========================================
   게임 루프
========================================= */

function loop(time){{

    if(dead) return;

    if(!paused){{

        let speed =
            dash ? 65 : 160;

        let progress =
            Math.min(
                (time-lastMove)/speed,
                1
            );

        progress =
            progress<.5
            ? 2*progress*progress
            : 1-
              Math.pow(
                  -2*progress+2,
                  2
              )/2;

        render(progress);

        if(
            time-lastMove>=speed
        ){{
            moveSnake();
        }}

        updateSkill();

        requestAnimationFrame(loop);
    }}
}}


/* =========================================
   질주
========================================= */

function activateDash(){{

    if(dead || paused || dash)
        return;

    const now =
        performance.now();

    if(
        now-lastDash<DASH_COOLDOWN
    )
        return;

    dash=true;

    lastDash=now;

    dashStart=now;
}}


function updateSkill(){{

    const now =
        performance.now();

    const status =
        document.getElementById(
            "skillStatus"
        );

    if(dash){{

        if(
            now-dashStart>=DASH_TIME
        ){{
            dash=false;
        }}else{{

            status.textContent =
                "🔥 질주 중";
            return;
        }}
    }}

    const remaining =
        DASH_COOLDOWN-
        (now-lastDash);

    if(
        lastDash<0 ||
        remaining<=0
    ){{
        status.textContent="READY";
    }}else{{
        status.textContent =
            Math.ceil(
                remaining/1000
            )+
            "초";
    }}
}}


/* =========================================
   죽음
========================================= */

function die(pos){{

    dead=true;
    dash=false;

    const boom =
        document.getElementById("boom");

    boom.style.left =
        pos.x*GRID+"px";

    boom.style.top =
        pos.y*GRID+"px";

    boom.style.display="block";

    setTimeout(
        ()=>{{

            document.getElementById(
                "finalScore"
            ).textContent=score;

            document.getElementById(
                "gameover"
            ).style.display="block";

        }},
        500
    );
}}


/* =========================================
   퀘스트
========================================= */

function updateQuest(){{

    let progress =
        Math.min(score,5);

    document.getElementById(
        "questText"
    ).textContent =
        "🍎 사과 먹기 "+
        progress+
        "/5";

    if(score>=5){{

        document.getElementById(
            "questText"
        ).textContent =
            "🎉 완료! +80 🪙";
    }}
}}


/* =========================================
   키보드
========================================= */

document.addEventListener(
    "keydown",
    e => {{

        const key =
            e.key.toLowerCase();


        /* ESC */

        if(e.code==="Escape"){{

            e.preventDefault();

            if(dead) return;

            paused=!paused;

            document.getElementById(
                "pause"
            ).style.display =
                paused
                ? "block"
                : "none";

            if(!paused){{
                lastMove=performance.now();
                requestAnimationFrame(loop);
            }}

            return;
        }}


        /* LEFT SHIFT */

        if(e.code==="ShiftLeft"){{

            e.preventDefault();

            shiftHeld=true;

            activateDash();

            return;
        }}


        if(paused || dead)
            return;


        if(
            (key==="w" ||
             key==="arrowup") &&
            direction.y!==1
        ){{
            nextDirection={{x:0,y:-1}};
        }}

        if(
            (key==="s" ||
             key==="arrowdown") &&
            direction.y!==-1
        ){{
            nextDirection={{x:0,y:1}};
        }}

        if(
            (key==="a" ||
             key==="arrowleft") &&
            direction.x!==1
        ){{
            nextDirection={{x:-1,y:0}};
        }}

        if(
            (key==="d" ||
             key==="arrowright") &&
            direction.x!==-1
        ){{
            nextDirection={{x:1,y:0}};
        }}
    }}
);


document.addEventListener(
    "keyup",
    e => {{

        if(e.code==="ShiftLeft"){{

            shiftHeld=false;

            dash=false;
        }}
    }}
);


/* =========================================
   버튼
========================================= */

document.getElementById(
    "continue"
).onclick=()=>{{

    paused=false;

    document.getElementById(
        "pause"
    ).style.display="none";

    lastMove=performance.now();

    requestAnimationFrame(loop);
}};


document.getElementById(
    "restart"
).onclick=()=>{{
    startGame();
}};


document.getElementById(
    "restart2"
).onclick=()=>{{
    startGame();
}};


startGame();

</script>

</body>

</html>
"""

    components.html(
        game_html,
        height=750,
        scrolling=False
    )


# =========================================================
# 페이지 실행
# =========================================================

if st.session_state.page == "main":

    main_page()

elif st.session_state.page == "shop":

    shop_page()

elif st.session_state.page == "game":

    game_page()
```
