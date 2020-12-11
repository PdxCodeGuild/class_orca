let container = document.getElementById('container')
let container2 = document.getElementById('container2')
let inputField = document.getElementById('inputField')
let btn = document.getElementById('btn')


btn.addEventListener('click', function() {
    let addTask = document.createElement('p')
    addTask.innerText = inputField.value
    container.appendChild(addTask)

    let removeBtn = document.createElement('button')
    removeBtn.setAttribute('type', 'button')
    removeBtn.innerText = 'x'
    removeBtn.style.backgroundColor = 'wheat'
    container.appendChild(removeBtn)

    let checkBtn = document.createElement('input')
    checkBtn.setAttribute('type', 'checkbox')
    container.appendChild(checkBtn)


    removeBtn.addEventListener('click', function(){
        container.removeChild(removeBtn) 
        container.removeChild(addTask)
        container.removeChild(checkBtn)
    })

    checkBtn.addEventListener('click', function(){
        if (checkBtn.checked) {
            let finishedTask = document.createElement('p')
            finishedTask.innerText = inputField.value
            finishedTask.style.textDecoration = 'line-through', 
            finishedTask.style.textDecorationColor = 'red'
            container2.appendChild(finishedTask)

 
            let removeBtn2 = document.createElement('button')
            removeBtn2.setAttribute('type', 'button')
            removeBtn2.innerText = 'x'
            removeBtn2.style.backgroundColor = 'wheat'
            container2.appendChild(removeBtn2)

            removeBtn2.addEventListener('click', function(){
                container2.removeChild(removeBtn2) 
                container2.removeChild(finishedTask)
        })
    }
    })    
})
