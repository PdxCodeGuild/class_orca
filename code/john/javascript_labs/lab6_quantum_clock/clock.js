const div_clock = document.getElementById('clock');






// var minutes = 1000 * 60;
// var hours = minutes * 60;
// var days = hours * 24;
// var years = days * 365;
// var d = new Date();
// var t = d.getTime();
// var y = Math.round(t / years); 

// My code before searching the web:
let clock_as_p = document.createElement('p');

div_clock.appendChild(clock_as_p);
current_time = new Date();
clock_as_p.innerText = current_time;

let interval = setInterval(function() {
    // console.log(i);
    current_time = new Date();
    console.log(`updating time: ${current_time}`);
    clock_as_p.innerText = current_time;
}, 1000);
// END my code

// / / / / / / / / / / / / / / / / / 
// HTML IDs USED:
    // div id='container'
    // button class="btn"
    // div id='clock'
    // div id='to-do-list'
// / / / / / / / / / / / / / / / / /

// ##############################################################################
// # John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
// https://github.com/PdxCodeGuild/class_orca/blob/main/4%20JavaScript/labs/lab04-todo.md
// ##############################################################################
