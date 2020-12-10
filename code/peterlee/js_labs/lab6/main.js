let timeDiv = document.getElementById("time-div");
let timeP = document.getElementById("time-p");
let btn = document.getElementById("btn");

btn.addEventListener("click", getTime);

function getTime() {
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();
    timeP.innerText = `The time is ${hours}:${minutes}:${seconds}`
}

setInterval(getTime, 1000);

