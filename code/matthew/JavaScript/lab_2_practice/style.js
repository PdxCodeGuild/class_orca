let taskInput = document.getElementById('taskInput')
let taskBtn = document.getElementById('taskBtn')
let pendingContainer = document.getElementById('pendingContainer')
let completedContainer = document.getElementById('completedContainer')

taskBtn.addEventListener('click', function(){
    let pendingTask = document.createElement('p')
    pendingTask.innerText = taskInput.value
    pendingContainer.appendChild(pendingTask)
    
    let pendingCheckbox = document.createElement('input')
    pendingCheckbox.setAttribute('type', 'checkbox')
    pendingContainer.appendChild(pendingCheckbox)

    let deleteBtn = document.createElement('button')
    deleteBtn.setAttribute('type', 'button')
    deleteBtn.innerText = 'x'
    pendingContainer.appendChild(deleteBtn)

    deleteBtn.addEventListener('click', function(){
        pendingContainer.removeChild(deleteBtn)
        pendingContainer.removeChild(pendingTask)
        pendingContainer.removeChild(pendingCheckbox)
    })

    pendingCheckbox.addEventListener('click', function(){
        if (pendingCheckbox.checked) {
        let completedTask = document.createElement('p')
        completedTask.innerText = taskInput.value
        completedContainer.appendChild(completedTask)
        
        let completedDeleteBtn = document.createElement('button')
        completedDeleteBtn.setAttribute('type', 'button')
        completedDeleteBtn.innerText = 'x'
        completedContainer.appendChild(completedDeleteBtn)

        completedDeleteBtn.addEventListener('click', function(){
            completedContainer.removeChild(completedDeleteBtn)
            completedContainer.removeChild(completedTask)

        })
    }
    })



})
