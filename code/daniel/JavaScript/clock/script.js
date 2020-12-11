let clock = document.getElementById("clock_display")
// let hour_digit = document.createElement("p")
// let minute_digit = document.createElement("p")
// let second_digit = document.createElement("p")
// clock.append(hour_digit, minute_digit, second)

function get_time() {
    let time = new Date()

    let hour = time.getHours()

    let minute = time.getMinutes()

    let second = time.getSeconds()
    
    clock.innerText = `${hour}:${minute}:${second}`

    setInterval(function() {
        get_time()
    }, 1000)
}

get_time()

// // Global variables
// let digits = document.getElementById("digits")
// let hour_digits = document.getElementById("hour_digits")
// let minute_digits = document.getElementById("minute_digits")
// let second_digits = document.getElementById("second_digits")

// function get_time () {
//     for (let i=0; i<24; i++) {
//         let hour_digit = document.createElement("p")
//         hour_digit.innerHTML = i
//         if (time('hour') === i) {
//             hour_digit.style.backgroundColor = "black"
//             hour_digit.style.color = "white"
//         } else {
//             hour_digit.style.backgroundColor = "white"
//             hour_digit.style.color = "black"
//         }
//         hour_digit.className = "hour_digit"
//         hour_digits.appendChild(hour_digit)
//     } 

//     for (let i=0; i<60; i++) {
//         let minute_digit = document.createElement("p")
//         minute_digit.innerHTML = i
//         if (time('minute') === i) {
//             minute_digit.style.backgroundColor = "black"
//             minute_digit.style.color = "white"
//         } else {
//             minute_digit.style.backgroundColor = "white"
//             minute_digit.style.color = "black"
//         }
//         minute_digit.className = "minute_digit"
//         minute_digits.appendChild(minute_digit)
//     } 

//     for (let i=0; i<60; i++) {
//         let second_digit = document.createElement("p")
//         second_digit.innerHTML = i
//         if (time('second') === i) {
//             second_digit.style.backgroundColor = "black"
//             second_digit.style.color = "white"
//         } else {
//             second_digit.style.backgroundColor = "white"
//             second_digit.style.color = "black"
//         }
//         second_digit.className = "second_digit"
//         second_digits.appendChild(second_digit)
//     }
// }
// // Time
// function time (whos_asking) {
//     let time = new Date()
//     if (whos_asking === "hour") {
//         let hours = time.getHours()
//         return hours
//     } else if (whos_asking === "minute") {
//         let minutes = time.getMinutes()
//         return minutes
//     } else if (whos_asking === "second") {
//         let seconds = time.getSeconds()
//         return seconds
//     }
//     console.log(`${hours}:${minutes}.${seconds}`)
// }

// // let clock = setInterval(function() {
// //     get_time()
// // }, 1000)
// get_time()