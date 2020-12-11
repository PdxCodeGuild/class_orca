let input = document.getElementById('input')
let add = document.getElementById('add')
let list = document.getElementById('list')
let edit = document.getElementById('edit')
let finished = document.getElementById('finished')

function addItem(e){
    let li = document.createElement('li')
    li.innerText = `${input.value}`
    li.setAttribute('id', input.value)
    li.setAttribute('class', 'item')

    let complete = document.createElement('button')
    complete.setAttribute('id', 'complete')
    complete.innerText = 'Complete'
    complete.addEventListener('click', function(e){
        finished.appendChild(li)
    })
    let remove = document.createElement('button')
    remove.setAttribute('id', 'remove')
    remove.innerText = 'Remove item'
    remove.addEventListener('click', function(e){
        list.removeChild(li)
    })
    li.appendChild(complete)
    li.appendChild(remove)

    list.appendChild(li)    
    input.value = ''
}

add.addEventListener('click', addItem)
input.addEventListener('keypress', function(e){
    if (e.key === 'Enter'){
        addItem()
    }
})