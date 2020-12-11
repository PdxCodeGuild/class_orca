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
    container.appendChild(removeBtn)

    let checkBtn = document.createElement('input')
    checkBtn.setAttribute('type', 'checkbox')
    container.appendChild(checkBtn)
        if (checkBtn === 2)

    removeBtn.addEventListener('click', function(){
        container.removeChild(removeBtn) 
        container.removeChild(addTask)
        container.removeChild(checkBtn)
    })



    checkBtn.addEventListener('click', function() {
        let finishedTask = document.createElement('p')
        finishedTask.innerText = inputField.value
        container2.appendChild(finishedTask)
        container2.appendChild(removeBtn)
        
        removeBtn.addEventListener('click', function(){
            container2.removeChild(removeBtn) 
            container2.removeChild(finishedTask)
    })    

    })    
  
})
