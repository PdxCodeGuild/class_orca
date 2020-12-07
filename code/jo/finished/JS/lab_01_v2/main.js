// number averager

let add_btn = document.getElementById("add_btn");
let avg_btn = document.getElementById("avg_btn");
let num = document.getElementById("num");
let average = document.getElementById('average');
let li = document.createElement('li');
let num_list = [];
let total = 0;
let avg = 0;

add_btn.addEventListener('click', function(e) {
    num_list.push(num.value);
    num.value = ''
});

num.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        num_list.push(num.value);
        num.value = ''
    };
});

avg_btn.addEventListener('click', function() {
    num_list.forEach(function (i) {
        total += (+i)
    });
    avg += total / num_list.length;
    console.log(total);
    console.log(num_list.length);
    li.innerText = (`The average of [${num_list}] is ${avg}`);
    average.appendChild(li);        
});
