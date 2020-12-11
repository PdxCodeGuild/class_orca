


setInterval( function theTime (){
console.log("it's running")
    let now = new Date()
    let check = now.toLocaleTimeString()
    console.log(check)
    // let h = now.getHours()
    // let m = now.getMinutes()
    // let s = now.getSeconds()
    let clock = document.getElementById("clock")
    clock.innerText = `The time is: ${check}`
    
}, 1000)

