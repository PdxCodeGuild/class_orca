//Get current time
function currentTime() {
    let date = new Date(); 
    let hour = date.getHours();
    let min = date.getMinutes();
    let sec = date.getSeconds();
    hour = addZero(hour);
    min = addZero(min);
    sec = addZero(sec);

    //Change to 12-hour format
    if (hour > 12) {
        hour -= 12;
    } if (hour == 0) {
        hour = 12;
    }
    let morning;
    if (hour >=12) {
        morning = "AM"
    } else {
        morning = "PM"
    }
    document.getElementById("clock").innerText = hour + ":" + min + ":" + sec + " " + morning; 
    let lapse = setTimeout(function(){ currentTime() }, 1000); 
}

function addZero(z) {
    if (z < 10) {
        return "0" + z;
    }
    else {
        return z;
    }
}

currentTime();


let display = document.getElementById("stopwatch")
let time;
let tInterval;

//Set stopwatch value
function sWatch() {
    display.innerText = "00" + ":" + "00" + ":" + "00" 
    time = new Date();
    let hour = time.getHours();
    let min = time.getMinutes();
    let sec = time.getSeconds();

    let startBtn = document.getElementById("start-btn");
    startBtn.addEventListener('click', function() {
        time = new Date();
        time.setHours(0,0,0,0);
        let update = setInterval(updateTimer, 1000);
        hour + ":" + min + ":" + sec
    });

    let resetBtn = document.getElementById("reset-btn");
    resetBtn.addEventListener('click', function() {
        clearInterval(tInterval);
        time = new Date();
        time.setHours(0,0,0,0);
        display.innerText = "clear"
    });

}

function updateTimer(z) {
    time.setSeconds(time.getSeconds() +1)
    let hour = time.getHours();
    let min = time.getMinutes();
    let sec = time.getSeconds();
    hour = addZero(hour);
    min = addZero(min);
    sec = addZero(sec);
    display.innerText = hour + ":" + min + ":" + sec
}

sWatch();