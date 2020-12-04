



// title.innerHTML = "<strong><em>Hello World</strong></em>";

let title = document.getElementById("title")

let div = document.createElement("div");
div.style.width = "400px";
div.style.height = "400px";
div.style.border = "1px solid black";

document.body.appendChild(div);

title.appendChild(div)

title.innerHTML = "<p>paragraph</p>";


div = document.getElementById("js")
div.style.backgroundColor = "red";

console.log(div)


