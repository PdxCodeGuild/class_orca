
let add_item = new Vue({
    el: "#app",
    data: {
        items: [], 
        completed_items: []
    },
    methods: {
        addItem: function () {
            this.items.push(item)
        },
        completeItem: function () {
            this.completed_items.push(item)
        },
        deleteItem: function () {
            this.items.remove(item)
        }
    }
})
