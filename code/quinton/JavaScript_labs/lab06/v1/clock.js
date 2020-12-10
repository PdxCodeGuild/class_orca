clock = document.getElementById('clock');
let hour_p = document.getElementById('hour');
let minute_p = document.getElementById('minute');
let second_p = document.getElementById('second');


function startClock() {
    let now = new Date();
    let hour = now.getHours();
    let minute = now.getMinutes();
    let second = now.getSeconds();
    minute = checkTime(minute);
    second = checkTime(second);
    hour_p.innerText = hour +':';
    minute_p.innerText = minute + ':';
    second_p.innerText = second;
    let time = setTimeout(startClock);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};
    return i;
}

startClock()