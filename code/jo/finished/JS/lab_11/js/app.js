Vue.component('additem', {
    template: `<button @click="$emit('additem')">Add Item</button>`
})

new Vue ({
    el: '#app',
    data: {
        items : [],
        item : '',
        completed : []
    },
    methods: {
        addItem: function() {
            this.items.push(this.item)
            console.log(this.item)
            console.log(this.items)
            this.item = ''
        },
        remove (item) {
            this.items.splice(this.items.indexOf(item),1)
        },
        makecomplete(item) {
            let completeitem = this.items.splice(this.items.indexOf(item),1)
            completeitem = completeitem[0]
            this.completed.push(completeitem)
        }
    }
})

// push ({item: '', id:''})


// new Vue ({
//     el: '#add',
//     data: {
//         message: ''
//     },
//     methods: {
//         additem: function () {
//             let list = document.getElementById('list')
//             list.appendChild(this.message)
//             // let input = document.getElementById('input')
//             // let li = document.createElement('li')
//             // li.innerText = input.value
//             // let list = document.getElementById('list')
//             // list.appendChild(li)
//         }
//     }
// })