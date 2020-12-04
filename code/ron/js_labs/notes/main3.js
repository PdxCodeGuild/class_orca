

let p = document.getElementsByTagName("p");

let red = document.getElementsByClassName("red"); // red in this class in this case (an html collection)
                                                    // the elements of red are maniputable
let title = document.getElementById("title");

title.innerText = "Hello World innertext"

title.innerHTML = "Hello World innerHTML"


// for (let i=0; i<red.length; i++) {
//     red[i].innerText = "why is this text not red we'll have to fix that"
//     red[i].style.backgroundColor = "red";
//     red[i].style.color = "white"
//     red[i].style.border = "1px solid black"
// }





