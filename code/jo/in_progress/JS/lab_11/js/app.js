Vue.component('add-item', {
    data: function() {
        return {
            items : [],
            item : '',
            completed : []
        }
    },
    template: `
        <div>
            <input type='text' placeholder='item' @keyup.enter="additem" v-model='item'>
            <button @click='additem'>Add Item</button>
        </div>
    `,
    methods: {
        additem: function() {
            this.items.push(this.item)

            this.item = ''

    }
}
})

new Vue ({
    el: '#app',
    data: {
        items : [],
        item : '',
        completed : []
    },
    methods: {
        additem: function() {
            this.items.push()
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