new Vue ({
    el: '#app',
    data: {
        items: [],
        item : ''
    },
    methods: {
        additem() {
            this.items.push(this.item)
            this.item = ''
        }
    }
})




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