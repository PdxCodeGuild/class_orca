const clock = document.getElementById('clock')

document.body.style.display = "flex"
document.body.style.justifyContent = "center"
document.body.style.alignContent = "center"
clock.style.margin = "auto"
clock.style.border = "1px solid black"
clock.style.height = "200px"
clock.style.width = "750px"
clock.style.marginTop = "32vh"
document.body.style.fontSize = "160px"

function timeNow() {
    var date = new Date()
    var hour = date.getHours()
    var minutes = date.getMinutes()
    var seconds = date.getSeconds()
    var mili = date.getMilliseconds()
    hour = zeros(hour)
    minutes = zeros(minutes)
    seconds = zeros(seconds)
    clock.style.color = "blue"
    clock.innerHTML = hour + " : " + minutes + " : " + seconds 
    var y = setTimeout(function(){ timeNow() }, 1000)
}

function zeros(x) {
    if (x < 10) {
        return "0" + x
    } else {
        return x
    }
}
timeNow()