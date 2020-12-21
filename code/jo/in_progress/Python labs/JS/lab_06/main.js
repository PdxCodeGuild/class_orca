
function datetime () {
    let current = new Date()
    document.getElementById('date').innerHTML = current
}

let current_time = setInterval(datetime, 1000)


/////////////////////////////////////////////////////////////////

let timer = document.getElementById('timer')
let start = document.getElementById('start')
let stop = document.getElementById('stop')
let lap = document.getElementById('lap')
let reset = document.getElementById('reset')
let laptimes = document.getElementById('laptimes')
let clear = document.getElementById('clear')


let startime = new Date()
startime.setHours(0,0,0,0)

function startTime(e) {
    let now = (startime - Date.now())
    document.getElementById('timer').innerHTML = now
    }

start.onclick = setInterval(startTime, 100)

lapcount = 1
lap.onclick = function() {
    let li = document.createElement('li')
    console.log(li)
    li.innerText = `Lap ${lapcount}: ${timer.innerText}`
    console.log(li)
    laptimes.appendChild(li)
    lapcount++
    console.log(lap)
    }

// let runningtme = setInterval(startTime, 100)


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