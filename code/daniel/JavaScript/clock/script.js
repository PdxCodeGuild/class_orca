// let clock = document.getElementById("clock_display")
let hour_digit = document.getElementById("hour")
let minute_digit = document.getElementById("minute")
let second_digit = document.getElementById("second")


function get_time() {

    let time = new Date()

    let hour = time.getHours()
    let minute = time.getMinutes()
    let second = time.getSeconds()

    hour_digit.innerText = hour
    minute_digit.innerText = minute
    second_digit.innerText = second

    setInterval(function() {
        get_time()
    }, 1000)
}

get_time()

// setInterval(function() {
//     location.reload()
// }, 3000)