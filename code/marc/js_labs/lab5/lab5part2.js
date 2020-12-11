let start = document.getElementById("start")
let stop = document.getElementById("stop")
let reset = document.getElementById("reset")
let lap = document.getElementById("lap")
let lreset = document.getElementById("lreset")
let time = 0


 let start_stop = function(y=0){
    if (y===0){
    console.log("where we need to be")
    time= new Date()
    let starttime = time.setHours(0,0,0,0)
    } else {
        time = y
    }
    
    let sw= setInterval(function (){
    //    start.onclick = () => start_stop()
       let mili= time.getMilliseconds()
       time.setMilliseconds(mili+10)
       sec = time.getSeconds()
       min = time.getMinutes()
       hours= time.getHours()
       theMoment = `${hours}:${min}:${sec}:${mili}`
    //    console.log(starttime)
       let stopwatch = document.getElementById("stop_watch")
       stopwatch.innerText = theMoment
       stop.onclick = ()=> clearInterval(sw)
       lap.onclick = ()=> lapcount(theMoment) 
       reset.onclick = () => start_stop(0)
       lreset.onclick = ()=> lapreset()
       start.onclick = () => start_stop(time)
    }, 10)
    
}
let lapcount = function (theMoment) {
    lapcounter = document.getElementById("laptime")
    lapnumber = document.createElement("li")
    lapnumber.innerText = theMoment
    lapcounter.appendChild(lapnumber)
}

let lapreset = function (){
    let laplist = document.getElementById("laptime")
    // var node= document.getElementById("parent");
    laplist.querySelectorAll('*').forEach(n => n.remove());
        
}
start.addEventListener("click", ()=>start_stop(time))