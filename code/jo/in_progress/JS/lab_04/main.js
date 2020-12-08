let input = document.getElementById('input')
let add = document.getElementById('add')
let list = document.getElementById('list')
let edit = document.getElementById('edit')

function addItem(e) {
    let li = document.createElement('li')

    let radios = document.createElement('form')

    let complete = document.createElement('input')
    let label_c = document.createElement('label')
    complete.setAttribute('id', 'complete')
    complete.setAttribute('name', 'choice')
    complete.setAttribute('type', 'radio')
    label_c.setAttribute('for', 'complete')
    label_c.innerText = ("complete")

    let remove = document.createElement('input')
    let label_r = document.createElement('label')
    remove.setAttribute('id', 'remove')
    remove.setAttribute('name', 'choice')
    remove.setAttribute('type', 'radio')
    label_r.setAttribute('for', 'remove')
    label_r.innerText = ('remove')

    radios.innerText = `${input.value}`
    radios.appendChild(complete)
    radios.appendChild(label_c)
    radios.appendChild(remove)
    radios.appendChild(label_r)
    
    li.setAttribute('id', input.value)
    li.setAttribute('class', 'item')

    li.appendChild(radios)
    list.appendChild(li)
}



function Update(e) {
    

}




add.addEventListener('click', addItem)

edit.addEventListener('click', Update)