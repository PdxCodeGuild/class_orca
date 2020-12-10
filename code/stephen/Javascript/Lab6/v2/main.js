const clock = document.getElementById('clock')
const btns = document.getElementById('btns')
const start = document.getElementById('start')
const stop = document.getElementById('stop')
const lap = document.getElementById('lap')
const laps = document.getElementById('laps')
const lapsList = document.getElementById('lapsList')
const main = document.getElementById('main')

document.body.style.display = "flex"
document.body.style.justifyContent = "center"
document.body.style.alignContent = "center"
clock.style.margin = "auto"
clock.style.border = "1px solid black"
clock.style.height = "250px"
clock.style.width = "750px"
clock.style.marginTop = "32vh"
document.body.style.fontSize = "100px"

// function timeNow() {
//     var date = new Date()
//     var hour = date.getHours()
//     var minutes = date.getMinutes()
//     var seconds = date.getSeconds()
//     var mili = date.getMilliseconds()
//     hour = zeros(hour)
//     minutes = zeros(minutes)
//     seconds = zeros(seconds)
//     clock.innerHTML = hour + " : " + minutes + " : " + seconds + " : " + mili
//     var y = setTimeout(function(){ 
//         timeNow() 
//     }, 1)
// }
let stopwatch_running = false
let stopdate = new Date()
function update_stopwatch() {
    startdate = new Date();
    startseconds = startdate.getSeconds();
    startseconds += 1;
    startdate.setHours(0,0,0,0);
    startdate.setSeconds(startseconds);
    clock.innerText = `${startdate.getHours()}:${startdate.getMinutes()}:${startdate.getSeconds()}`;
}


start.addEventListener("click", function() {
    if (stopwatch_running == false) {
        stopwatch_running = true;
        stopdate = new Date();
        stopdate.setHours(0,0,0,0);
        let stopwatch_interval = window.setInterval(update_stopwatch,1000);
        
       
        
        
       
        stop.addEventListener("click", function() {
            clearInterval(stopwatch_interval);
            
            lapsList.innerText = "";
            stopwatch_running = false;
        })

       
        lap.addEventListener("click", function() {
            let lap_item = document.createElement("li");
            lap_item.innerText = `${stopdate.getHours()}:${stopdate.getMinutes()}:${stopdate.getSeconds()}`;
            lapsList.append(lap_item);
        })
    }
})
function zeros(x) {
    if (x < 10) {
        return "0" + x
    } else {
        return x
    }
}
// timeNow()
update_stopwatch()