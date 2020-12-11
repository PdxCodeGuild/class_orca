
// add element for adding an item to the list
let addItemInput = document.getElementById("addItemInput")
let addItemButton = document.getElementById('addItemButton')
let container = document.getElementById('container')
let itemsFinishedContainer = document.getElementById('itemsFinishedContainer')

addItemButton.addEventListener('click', function() {
    let makeItem = document.createElement('p')
    makeItem.innerText = addItemInput.value
    container.appendChild(makeItem)

    // make remove button
    let removeBtn = document.createElement('button')
    removeBtn.setAttribute('type', 'button')
    removeBtn.innerText = 'x'
    container.appendChild(removeBtn)

    //make check off button
    let checkOff = document.createElement('input')
    checkOff.setAttribute('type', 'checkbox')
    container.appendChild(checkOff)

    removeBtn.addEventListener('click', function(){
        container.removeChild(removeBtn)
        container.removeChild(checkOff)
        container.removeChild(makeItem)
    })

    checkOff.addEventListener('click', function(){
        let checkedOff = document.createElement('p')

        // Item Obtained P tag
        let finishedItem = document.createElement('p')
        finishedItem.innerText = addItemInput.value
        finishedItem.style.textDecoration = 'line-through'
        container.appendChild(finishedItem)
        itemsFinishedContainer.appendChild(finishedItem)

        let FinishedcheckedOff = document.createElement('button')
        FinishedcheckedOff.innerText = 'x'
        itemsFinishedContainer.appendChild(FinishedcheckedOff)

        FinishedcheckedOff.addEventListener('click', function() {
            itemsFinishedContainer.removeChild(FinishedcheckedOff)
            itemsFinishedContainer.removeChild(finishedItem)
        })
    })


})



