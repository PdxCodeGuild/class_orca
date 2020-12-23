
function datetime () {
    let current = new Date()
    document.getElementById('date').innerHTML = current
}

let current_time = setInterval(datetime, 1000)


/////////////////////////////////////////////////////////////////

let timer = document.getElementById('timer')
let startbutton = document.getElementById('start')
let stopbutton = document.getElementById('stop')
let lapbutton = document.getElementById('lap')
let resetbutton = document.getElementById('reset')
let laptimes = document.getElementById('laptimes')

let time = 1000000000

function millitostring(time) {
    let diffinHrs = time / 3600000
    let hours = Math.floor(diffinHrs)
    let diffinMin = (diffinHrs - hours) * 60
    let minutes = Math.floor(diffinMin)
    let diffinSec = (diffinMin - minutes) * 60
    let seconds = Math.floor(diffinSec)
    let diffinMS = (diffinSec - seconds) * 100
    let milliseconds = Math.floor(diffinMS)

    return `${hours}:${minutes}:${seconds}:${milliseconds}`
}

startbutton.addEventListener('click', start)
stopbutton.addEventListener('click', stop)
resetbutton.addEventListener('click', reset)

let elapsedTime = 0

function start(){
    startTime = Date.now() - elapsedTime
    timerInterval = setInterval(function printTime(){
        elapsedTime = Date.now() - startTime
        document.getElementById('timer').innerHTML = millitostring(elapsedTime)
    },100)
}

function stop(){
    clearInterval(timerInterval)
}

function reset() {
    clearInterval(timerInterval)
    elapsedTime = 0
    document.getElementById('timer').innerHTML = elapsedTime
    var ul = document.getElementById('laptimes')
    while(ul.firstChild) ul.removeChild(ul.firstChild)
}

lapcount = 1
lap.onclick = function() {
    let li = document.createElement('li')
    li.innerText = `Lap ${lapcount}: ${timer.innerText}`
    laptimes.appendChild(li)
    lapcount++
    }

// let startime = new Date()
// startime.setHours(0,0,0,0)

// function startTime(e) {
//     let now = Date.now()
//     // let now = (startime - Date.now())
//     document.getElementById('timer').innerHTML = now
//     // console.log(now)
//     // console.log(startime)
//     }

// start.onclick = setInterval(startTime, 100)


///////////////////////////////sorta working
// timer.innerHTML = 0

// start.onclick = function() {
//     let interval = setInterval(function() {
//         timer.innerText++
//     }, 1000)
// }

// lapcount = 1
// lap.onclick = function() {
//     let li = document.createElement('li')
//     console.log(li)
//     li.innerText = `Lap ${lapcount}: ${timer.innerText}`
//     console.log(li)
//     laptimes.appendChild(li)
//     lapcount++
//     console.log(lap)
//     }
///////////////////////////////////


// function startTime () {
//     let newtime = document.createElement('p')
//     timer.appendChild(newtime)
//     let current = new Date()
//     newtime.innerHTML = document.getElementById('p').innerHTML = current.toLocaleTimeString()
// }

// let timertime = setInterval(startTime, 1000)








// var startTimer = setInterval(myTimer, 1000),
// timerElement = document.getElementById("timer"),
// buttonElement = document.getElementById("myButton");

// function myTimer(){
// var current = new Date();
// timerElement.innerHTML = current.toLocaleTimeString();
// }

// function toggle(){
// if (startTimer) {
//     clearInterval(startTimer);
//     startTimer = null;
//     buttonElement.innerHTML = "Start";
// } else {
//     buttonElement.innerHTML = "Stop";
//     startTimer = setInterval(myTimer, 1000);
// }
// }