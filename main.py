import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Worm Quest",
    page_icon="🪱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
header, footer {visibility:hidden;}
.block-container {padding:0 !important; max-width:1000px;}
[data-testid="stAppViewContainer"] {background:#0c1c10;}
</style>
""", unsafe_allow_html=True)

HTML = r
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#102615;font-family:Arial,"Noto Sans KR",sans-serif;color:#fff}
button{font-family:inherit;cursor:pointer;border:0}
#app{width:820px;height:880px;margin:auto;position:relative;overflow:hidden;border-radius:28px;background:
radial-gradient(circle at 5% 5%,#6e9f45 0 6%,transparent 18%),
radial-gradient(circle at 95% 10%,#3f7535 0 8%,transparent 20%),
radial-gradient(circle at 5% 92%,#477e38 0 8%,transparent 20%),
radial-gradient(circle at 94% 90%,#315e31 0 9%,transparent 22%),#214d2b}
.screen{position:absolute;inset:0;display:none}.screen.active{display:block}
.tree{position:absolute;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle at 32% 25%,#a5d95d,#5d963e 48%,#214c28 85%);box-shadow:inset -12px -15px 20px #0005,0 10px 18px #0006}
#main{padding-top:58px;text-align:center}
.logo{font-size:62px;font-weight:1000;text-shadow:0 5px #17321e}
.subtitle{color:#bfd3bf;margin-top:5px}
.preview{font-size:125px;margin:30px auto 12px;animation:float 1.5s ease-in-out infinite}
@keyframes float{50%{transform:translateY(-12px) rotate(3deg)}}
.stats{display:flex;justify-content:center;gap:12px;margin:10px 0 25px}.stat{background:#0006;border:1px solid #fff2;padding:12px 25px;border-radius:14px;font-weight:900}.coin{color:#ffd84d}
.mainBtn{width:390px;height:62px;margin:8px;border-radius:15px;color:#fff;font-size:21px;font-weight:900}.start{background:#315fc9;box-shadow:0 5px #1d3b7e}.shop{background:#744dc4;box-shadow:0 5px #4b3081}
#shop{padding:25px 35px}.top{display:flex;align-items:center;justify-content:space-between}.back{background:#354139;color:#fff;padding:11px 18px;border-radius:10px;font-weight:900}.title{font-size:40px;font-weight:1000}.shopCoin{color:#ffd84d;font-size:20px;font-weight:900}.section{font-size:23px;font-weight:900;margin:18px 0 10px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:11px}.item{background:#0005;border:1px solid #fff2;border-radius:15px;padding:12px;text-align:center}.emoji{font-size:48px;height:62px;display:flex;align-items:center;justify-content:center}.name{font-weight:900}.price{color:#ffd84d;margin:6px}.item button{width:100%;height:36px;border-radius:8px;background:#315fc9;color:#fff;font-weight:900}.item button.owned{background:#39784b}.item button.equipped{background:#a87927}
#gameScreen{padding-top:4px}.header{height:58px;display:flex;justify-content:space-between;align-items:center;padding:0 25px;font-weight:900}.high{color:#ffd84d}
#gameArea{width:680px;height:680px;margin:auto;position:relative}
#board{position:absolute;inset:0;border:16px solid #254da5;border-radius:23px;overflow:hidden;background:
radial-gradient(circle at 12% 16%,#77a94c 0 3px,transparent 4px),
radial-gradient(circle at 27% 72%,#245d31 0 5px,transparent 6px),
radial-gradient(circle at 72% 25%,#8bb64d 0 4px,transparent 5px),
radial-gradient(circle at 88% 80%,#245d31 0 5px,transparent 6px),
linear-gradient(135deg,#3f7934,#72a544 35%,#396e32 70%,#568d38);background-size:120px 140px,170px 180px,150px 160px,200px 190px,100% 100%;box-shadow:inset 0 0 45px #0004,0 12px 25px #0007}
.hud{position:absolute;z-index:50;background:#000c;padding:8px 13px;border-radius:11px;font-weight:900}.score{left:14px;top:12px}.highbox{right:14px;top:12px;color:#ffd84d}.dash{left:50%;top:12px;transform:translateX(-50%);font-size:14px}.ready{color:#6eff91}.cool{color:#ff7777}
#quest{position:absolute;right:14px;bottom:14px;z-index:50;width:190px;background:#000c;border:1px solid #fff2;border-radius:11px;padding:9px 11px;font-size:12px}.qtitle{color:#ffd84d;font-weight:900;margin-bottom:4px}.qreward{color:#ffd84d;margin-top:3px}
#food{position:absolute;z-index:40;font-size:31px;width:34px;height:34px;display:flex;align-items:center;justify-content:center;animation:pulse .65s ease-in-out infinite}@keyframes pulse{50%{transform:scale(1.14)}}
#svg{position:absolute;inset:0;width:648px;height:648px;z-index:30;overflow:visible;pointer-events:none}
.path{fill:none;stroke-width:36;stroke-linecap:round;stroke-linejoin:round}.shadow{stroke:#18386f55;stroke-width:46}.light{stroke:#fff5;stroke-width:5}.trail{stroke:#dcecff88;stroke-width:8;stroke-dasharray:13 13}
#head{transform-origin:center;transform-box:fill-box}.eye{fill:#fff}.pupil{fill:#172044}
#closed{fill:none;stroke:#112c64;stroke-width:3;stroke-linecap:round}#open{display:none}.mouth{fill:#101010;stroke:#071535;stroke-width:2}.tongue{fill:#ff4b55}.tooth{fill:#fff}
.dashing .trail{animation:trail .2s linear infinite}@keyframes trail{to{stroke-dashoffset:-26px}}
.wind{display:none;fill:none;stroke:#fff;stroke-width:4;stroke-linecap:round}.dashing .wind{display:block}.w1{animation:wind .3s infinite}.w2{animation:wind .36s .08s infinite}.w3{animation:wind .42s .15s infinite}@keyframes wind{0%{opacity:0;transform:translateX(30px)}30%{opacity:.8}100%{opacity:0;transform:translateX(-40px)}}
#crash{display:none;position:absolute;z-index:200;font-size:82px;transform:translate(-50%,-50%);animation:pop .45s}@keyframes pop{50%{transform:translate(-50%,-50%) scale(1.25)}}
.shake{animation:shake .4s}@keyframes shake{20%{transform:translate(-8px,4px)}40%{transform:translate(8px,-4px)}60%{transform:translate(-6px,3px)}80%{transform:translate(6px,-3px)}}
.overlay{position:absolute;inset:0;z-index:300;background:#000d;display:none;align-items:center;justify-content:center}.card{width:440px;background:#111a13;border:2px solid #3e5041;border-radius:24px;padding:38px;text-align:center;box-shadow:0 20px 50px #000a}.card h1{font-size:62px;margin:0 0 25px;font-weight:1000}.ob{display:block;width:280px;height:58px;margin:11px auto;border-radius:13px;color:#fff;font-size:20px;font-weight:900}.continue{background:#315fc9}.restart{background:#3d8b51}.home{background:#444c45}.die{color:#ff4545}
#notice{display:none;position:absolute;z-index:500;left:50%;bottom:18px;transform:translateX(-50%);background:#152119;border:2px solid #47604b;border-radius:11px;padding:11px 18px;font-weight:900}
</style>
</head>
<body>
<div id="app">
<div class="tree" style="left:-55px;top:-50px"></div><div class="tree" style="left:150px;top:-65px"></div><div class="tree" style="left:360px;top:-55px"></div><div class="tree" style="right:-55px;top:-45px"></div><div class="tree" style="right:-65px;top:220px"></div><div class="tree" style="left:-65px;top:470px"></div>

<section id="main" class="screen active">
<div class="logo">🪱 WORM QUEST</div><div class="subtitle">숲속에서 살아남아라</div>
<div class="preview" id="preview">🪱</div>
<div class="stats"><div class="stat">🪙 <span id="mainCoins">0</span></div><div class="stat">🏆 <span id="mainHigh">0</span></div></div>
<button class="mainBtn start" onclick="startGame()">🎮 게임 시작하기</button><br>
<button class="mainBtn shop" onclick="openShop()">🛒 상점</button>
</section>

<section id="shop" class="screen">
<div class="top"><button class="back" onclick="show('main')">← 메인으로</button><div class="title">🛒 상점</div><div class="shopCoin">🪙 <span id="shopCoins">0</span></div></div>
<div class="section">🪱 지렁이 외형</div><div id="wormGrid" class="grid"></div>
<div class="section">⚡ 스킬 변경</div><div id="skillGrid" class="grid"></div>
</section>

<section id="gameScreen" class="screen">
<div class="header"><div>🍎 점수: <span id="hScore">0</span>　🪙 <span id="gCoins">0</span></div><div class="high">🏆 최고기록: <span id="hHigh">0</span></div></div>
<div id="gameArea">
<div id="board">
<div id="scoreBox" class="hud score">🍎 <span id="score">0</span></div>
<div id="highBox" class="hud highbox">🏆 <span id="high">0</span></div>
<div id="dashBox" class="hud dash">⚡ 질주: <span id="dashStatus" class="ready">준비</span></div>
<div id="quest"><div class="qtitle">📜 QUEST</div><div id="qtext">-</div><div class="qreward">🪙 보상: <span id="qreward">0</span></div></div>
<div id="food">🍎</div>
<svg id="svg" viewBox="0 0 648 648">
<path id="shadow" class="path shadow"></path><path id="body" class="path"></path><path id="light" class="path light"></path><path id="trail" class="path trail"></path>
<g class="wind"><path class="wind w1" d="M5 20 Q-30 5 -65 15"></path><path class="wind w2" d="M0 0 Q-40 -10 -80 0"></path><path class="wind w3" d="M5 -20 Q-30 -5 -65 -15"></path></g>
<g id="head">
<path d="M-18-21Q4-28 21-15Q34 0 21 15Q4 28-18 21Q-30 11-30 0Q-30-11-18-21Z" id="headFill" fill="#315fc9" stroke="#244a9f" stroke-width="3"></path>
<circle class="eye" cx="4" cy="-18" r="10"></circle><circle class="eye" cx="4" cy="18" r="10"></circle><circle class="pupil" cx="7" cy="-17" r="4.5"></circle><circle class="pupil" cx="7" cy="17" r="4.5"></circle>
<path id="closed" d="M16-5Q23 0 16 5"></path>
<g id="open"><path class="mouth" d="M12-9Q25-12 29 0Q25 12 12 9Q17 0 12-9Z"></path><path class="tongue" d="M15 3Q21 0 26 4Q22 12 16 7Z"></path><path class="tooth" d="M16-8L20-2L23-8Z"></path><path class="tooth" d="M22-8L25-2L28-7Z"></path></g>
</g></svg>
<div id="crash">💥</div>

<div id="pause" class="overlay"><div class="card"><h1>일시정지</h1><button class="ob continue" onclick="resumeGame()">▶️ 계속하기</button><button class="ob restart" onclick="restart()">🔄 다시하기</button></div></div>
<div id="over" class="overlay"><div class="card"><h1 class="die">YOU DIE</h1><h2>점수: <span id="final">0</span></h2><h2>🏆 최고기록: <span id="finalHigh">0</span></h2><button class="ob restart" onclick="restart()">🔄 다시하기</button><button class="ob home" onclick="home()">🏠 메인으로</button></div></div>
</div></div>
</section>
<div id="notice"></div>
</div>

<script>
const GRID=36,COLS=18,ROWS=18,NORMAL=155,DASH_DURATION=2000,COOLDOWN=10000;

const worms={
basic:{name:"기본 지렁이",emoji:"🪱",color:"#315fc9",price:0},
fire:{name:"화염 지렁이",emoji:"🔥",color:"#e94a32",price:500},
lightning:{name:"번개 지렁이",emoji:"⚡",color:"#e7ca36",price:1000},
ghost:{name:"유령 지렁이",emoji:"👻",color:"#a879e8",price:1500},
rainbow:{name:"무지개 지렁이",emoji:"🌈",color:"#e35db7",price:2000},
dragon:{name:"용 지렁이",emoji:"🐉",color:"#df4b45",price:2500}
};

const skills={
dash:{name:"질주",price:0,speed:65},
turbo:{name:"터보 질주",price:700,speed:50},
wind:{name:"윈드 러너",price:1200,speed:42},
flash:{name:"플래시",price:1800,speed:32}
};

const pool=[
{type:"apple",text:"🍎 사과 먹기",target:5,reward:80},
{type:"apple",text:"🍎 사과 먹기",target:10,reward:150},
{type:"apple",text:"🍎 사과 먹기",target:15,reward:200},
{type:"score",text:"🏆 점수 달성",target:10,reward:100},
{type:"score",text:"🏆 점수 달성",target:20,reward:180},
{type:"score",text:"🏆 점수 달성",target:30,reward:200},
{type:"length",text:"🪱 몸 길이 늘리기",target:8,reward:100},
{type:"length",text:"🪱 몸 길이 늘리기",target:12,reward:150},
{type:"length",text:"🪱 몸 길이 늘리기",target:18,reward:200}
];

let coins=Number(localStorage.getItem("wqCoins")||0);
let highScore=Number(localStorage.getItem("wqHigh")||0);
let equippedWorm=localStorage.getItem("wqWorm")||"basic";
let equippedSkill=localStorage.getItem("wqSkill")||"dash";
let ownedWorms=JSON.parse(localStorage.getItem("wqWorms")||'["basic"]');
let ownedSkills=JSON.parse(localStorage.getItem("wqSkills")||'["dash"]');
let quests=JSON.parse(localStorage.getItem("wqQuests")||"null");

if(!Array.isArray(quests)||quests.length!==3) newQuests();

let snake=[],previous=[],food={x:10,y:9};
let direction={x:1,y:0},nextDirection={x:1,y:0};
let score=0,dead=false,paused=false,running=false;
let dashing=false,shiftHeld=false,dashEnd=0,lastDash=-Infinity;
let lastMove=0,raf=0;

const $=id=>document.getElementById(id);

function save(){
localStorage.setItem("wqCoins",coins);
localStorage.setItem("wqHigh",highScore);
localStorage.setItem("wqWorm",equippedWorm);
localStorage.setItem("wqSkill",equippedSkill);
localStorage.setItem("wqWorms",JSON.stringify(ownedWorms));
localStorage.setItem("wqSkills",JSON.stringify(ownedSkills));
localStorage.setItem("wqQuests",JSON.stringify(quests));
updateUI();
}

function updateUI(){
$("mainCoins").textContent=coins;
$("shopCoins").textContent=coins;
$("mainHigh").textContent=highScore;
$("gCoins").textContent=coins;
$("hHigh").textContent=highScore;
$("high").textContent=highScore;
$("preview").textContent=worms[equippedWorm].emoji;
}

function show(id){
document.querySelectorAll(".screen").forEach(x=>x.classList.remove("active"));
$(id).classList.add("active");
updateUI();
}

function openShop(){renderShop();show("shop");}

function notify(t){
const n=$("notice");n.textContent=t;n.style.display="block";
clearTimeout(window.nt);window.nt=setTimeout(()=>n.style.display="none",1800);
}

function renderShop(){
let wh="";
Object.entries(worms).forEach(([id,x])=>{
const owned=ownedWorms.includes(id),eq=equippedWorm===id;
wh+=`<div class="item"><div class="emoji">${x.emoji}</div><div class="name">${x.name}</div><div class="price">${x.price?`🪙 ${x.price}`:"무료"}</div><button class="${eq?"equipped":owned?"owned":""}" onclick="buyWorm('${id}')">${eq?"장착 중":owned?"장착하기":"구매"}</button></div>`;
});
$("wormGrid").innerHTML=wh;

let sh="";
Object.entries(skills).forEach(([id,x])=>{
const owned=ownedSkills.includes(id),eq=equippedSkill===id;
sh+=`<div class="item"><div class="emoji">⚡</div><div class="name">${x.name}</div><div class="price">${x.price?`🪙 ${x.price}`:"무료"}</div><button class="${eq?"equipped":owned?"owned":""}" onclick="buySkill('${id}')">${eq?"사용 중":owned?"변경하기":"구매"}</button></div>`;
});
$("skillGrid").innerHTML=sh;
}

function buyWorm(id){
const x=worms[id];
if(ownedWorms.includes(id)){equippedWorm=id;applyWorm();save();renderShop();notify(x.name+" 장착!");return;}
if(coins<x.price){notify("🪙 코인이 부족합니다!");return;}
coins-=x.price;ownedWorms.push(id);equippedWorm=id;applyWorm();save();renderShop();notify(x.name+" 구매 완료!");
}

function buySkill(id){
const x=skills[id];
if(ownedSkills.includes(id)){equippedSkill=id;save();renderShop();notify(x.name+"으로 변경!");return;}
if(coins<x.price){notify("🪙 코인이 부족합니다!");return;}
coins-=x.price;ownedSkills.push(id);equippedSkill=id;save();renderShop();notify(x.name+" 구매 완료!");
}

function applyWorm(){
const c=worms[equippedWorm].color;
$("body").style.stroke=c;
$("headFill").style.fill=c;
}

function newQuests(){
const arr=[...pool];quests=[];
for(let i=0;i<3;i++){const n=Math.floor(Math.random()*arr.length);quests.push({...arr[n],progress:0});arr.splice(n,1);}
save();
}

function updateQuestUI(){
let q=quests.find(x=>x.progress<x.target)||quests[0];
$("qtext").textContent=`${q.text} ${Math.min(q.progress,q.target)}/${q.target}`;
$("qreward").textContent=Math.min(q.reward,200);
}

function questProgress(){
quests.forEach(q=>{
if(q.type==="apple"||q.type==="score")q.progress=score;
if(q.type==="length")q.progress=snake.length;
});
for(let i=0;i<quests.length;i++){
if(quests[i].progress>=quests[i].target){
const reward=Math.min(quests[i].reward,200);
coins+=reward;
notify(`🎉 퀘스트 완료! +${reward} 🪙`);
const candidates=pool.filter(p=>!quests.some(q=>q.type===p.type&&q.target===p.target));
const r=(candidates.length?candidates:pool)[Math.floor(Math.random()*(candidates.length?candidates:pool).length)];
quests[i]={...r,progress:0};
break;
}}
save();updateQuestUI();
}

function resetSnake(){
snake=[{x:7,y:9},{x:6,y:9},{x:5,y:9},{x:4,y:9},{x:3,y:9}];
previous=snake.map(p=>({...p}));
}

function createFood(){
do{food={x:Math.floor(Math.random()*COLS),y:Math.floor(Math.random()*ROWS)}}while(snake.some(p=>p.x===food.x&&p.y===food.y));
}

function distanceToFood(){
const h=snake[0];return Math.max(Math.abs(h.x-food.x),Math.abs(h.y-food.y));
}

function updateMouth(){
const near=distanceToFood()<=2;
$("closed").style.display=near?"none":"block";
$("open").style.display=near?"block":"none";
}

function lerp(a,b,t){return a+(b-a)*t}
function ease(t){return t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2}

function animated(progress){
const t=ease(Math.max(0,Math.min(1,progress)));
return snake.map((p,i)=>{const o=previous[i]||p;return{x:lerp(o.x,p.x,t),y:lerp(o.y,p.y,t)}})
}

function pathFor(parts){
if(parts.length<2)return"";
const pts=[...parts].reverse().map(p=>({x:p.x*GRID+18,y:p.y*GRID+18}));
let d=`M ${pts[0].x} ${pts[0].y}`;
for(let i=1;i<pts.length-1;i++){
const a=pts[i],b=pts[i+1],mx=(a.x+b.x)/2,my=(a.y+b.y)/2;
d+=` Q ${a.x} ${a.y} ${mx} ${my}`;
}
const z=pts[pts.length-1];d+=` L ${z.x} ${z.y}`;return d;
}

function angle(){
if(direction.x===1)return 0;
if(direction.y===1)return 90;
if(direction.x===-1)return 180;
return -90;
}

function render(progress=1){
const a=animated(progress),d=pathFor(a);
$("body").setAttribute("d",d);$("shadow").setAttribute("d",d);$("light").setAttribute("d",d);$("trail").setAttribute("d",d);
const h=a[0],x=h.x*GRID+18,y=h.y*GRID+18;
$("head").setAttribute("transform",`translate(${x} ${y}) rotate(${angle()})`);
$("food").style.left=(food.x*GRID+7)+"px";$("food").style.top=(food.y*GRID+7)+"px";
$("score").textContent=score;$("hScore").textContent=score;updateMouth();
}

function move(){
if(dead||paused||!running)return;
direction={...nextDirection};
const h=snake[0],nh={x:h.x+direction.x,y:h.y+direction.y};
if(nh.x<0||nh.x>=COLS||nh.y<0||nh.y>=ROWS||snake.some(p=>p.x===nh.x&&p.y===nh.y)){crash(nh);return;}
previous=snake.map(p=>({...p}));
snake.unshift(nh);
if(nh.x===food.x&&nh.y===food.y){score++;if(score>highScore)highScore=score;createFood();questProgress();}else snake.pop();
lastMove=performance.now();render(0);
}

function moveTime(){return dashing?skills[equippedSkill].speed:NORMAL}

function loop(t){
if(!running||paused||dead)return;
if(dashing&&t>=dashEnd)stopDash();
const mt=moveTime();
if(t-lastMove>=mt)move();
render(Math.min((t-lastMove)/mt,1));
dashUI();
raf=requestAnimationFrame(loop);
}

function startGame(){
show("gameScreen");score=0;dead=false;paused=false;running=true;dashing=false;shiftHeld=false;lastDash=-Infinity;
direction={x:1,y:0};nextDirection={x:1,y:0};$("pause").style.display="none";$("over").style.display="none";$("crash").style.display="none";
resetSnake();createFood();lastMove=performance.now();applyWorm();updateQuestUI();render(1);cancelAnimationFrame(raf);raf=requestAnimationFrame(loop);
}

function restart(){startGame()}

function pauseGame(){
if(!running||dead||paused)return;
paused=true;cancelAnimationFrame(raf);raf=0;$("pause").style.display="flex";
}

function resumeGame(){
if(dead)return;
paused=false;$("pause").style.display="none";lastMove=performance.now();raf=requestAnimationFrame(loop);
}

function home(){
running=false;paused=false;dashing=false;shiftHeld=false;$("pause").style.display="none";$("over").style.display="none";show("main");
}

function startDash(){
if(!running||paused||dead||dashing)return;
const now=performance.now();
if(now-lastDash<COOLDOWN)return;
dashing=true;lastDash=now;dashEnd=now+DASH_DURATION;$("board").classList.add("dashing");lastMove=now;
}

function stopDash(){dashing=false;$("board").classList.remove("dashing")}

function dashUI(){
const now=performance.now();
if(dashing){$("dashStatus").textContent=`🔥 ${Math.max(0,(dashEnd-now)/1000).toFixed(1)}초`;$("dashStatus").className="cool";return}
if(lastDash===-Infinity||now-lastDash>=COOLDOWN){$("dashStatus").textContent="준비";$("dashStatus").className="ready"}
else{$("dashStatus").textContent=`쿨타임 ${Math.ceil((COOLDOWN-(now-lastDash))/1000)}초`;$("dashStatus").className="cool"}
}

function crash(p){
dead=true;running=false;stopDash();$("crash").style.left=(p.x*GRID+18)+"px";$("crash").style.top=(p.y*GRID+18)+"px";$("crash").style.display="block";$("board").classList.add("shake");
if(score>highScore)highScore=score;
setTimeout(()=>{$("board").classList.remove("shake");$("final").textContent=score;$("finalHigh").textContent=highScore;$("over").style.display="flex";save()},450);
}

window.addEventListener("keydown",e=>{
const k=e.key.toLowerCase();
if(e.code==="Escape"){
e.preventDefault();
if($("gameScreen").classList.contains("active"))paused?resumeGame():pauseGame();
return;
}
if(e.code==="ShiftLeft"){
e.preventDefault();
if(!shiftHeld){shiftHeld=true;startDash()}
return;
}
if(!running||paused||dead)return;
if((k==="w"||k==="arrowup")&&direction.y!==1)nextDirection={x:0,y:-1};
else if((k==="s"||k==="arrowdown")&&direction.y!==-1)nextDirection={x:0,y:1};
else if((k==="a"||k==="arrowleft")&&direction.x!==1)nextDirection={x:-1,y:0};
else if((k==="d"||k==="arrowright")&&direction.x!==-1)nextDirection={x:1,y:0};
});

window.addEventListener("keyup",e=>{
if(e.code==="ShiftLeft"){shiftHeld=false;if(dashing)stopDash()}
});

window.addEventListener("blur",()=>{shiftHeld=false;if(dashing)stopDash()});

updateUI();renderShop();applyWorm();updateQuestUI();
</script>
</body>
</html>


components.html(HTML, height=900, scrolling=False)
