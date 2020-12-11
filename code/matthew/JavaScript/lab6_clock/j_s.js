let clock = setInterval(myTimer, 1000)
let stopWatch = document.getElementById('stopWatch')

let stop = document.getElementById('stop')
let btns = document.getElementById('btns')
let lap = document.getElementById('lap')
let lapDisplay = document.getElementById('lapDisplay')

let runningWatch = false 
let interval    
let firstTime = true
let timer 
let minuets
let seconds
let counter = 0

function myTimer() {
    // console.log("sup")
    let currentTime = new Date();
    document.getElementById('clockFace').innerHTML = currentTime.toLocaleTimeString();
}

stopWatch.addEventListener('click', function(){
    if (runningWatch === true) { 
            runningWatch = false
            clearInterval(interval)
    }  
    else {
    runningWatch = true
        if (firstTime) {
            timer = new Date();
            timer.setHours(0, 0, 0, 0)
            firstTime = false
        }
        document.getElementById('displayStopWatch').innerTexs = timer
        interval = setInterval(function(){
            seconds = timer.getSeconds()   
            timer.setSeconds(seconds +1)
            minuets = timer.getMinutes()
            document.getElementById('displayStopWatch').innerText = ` ${minuets}:${seconds} `
    }, 1000)
    }
})
lap.addEventListener('click', function() {
    let lapText = document.createElement('p')
    lapText.innerText = `lap ${counter}: ${minuets}:${seconds}`
    lapDisplay.appendChild(lapText)
    counter += 1



})











    //     timer.getMilliseconds(timer.getMilliseconds() +1)
    // }, 10 )
    //     timer.getHours(timer.getHours() +1)
    // }, 3600000 )

