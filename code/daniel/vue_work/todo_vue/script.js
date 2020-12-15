let add_item = new Vue({
    el: "#todo",
    data: {
        items: [],
        item: "",
        id: 0,
    }, 
    methods: {
        addItem: function () {
            this.items.push({
                text: this.item,                
                completed: false,
                id: this.id++,
            })
            this.item = "" 
        },
        deleteItem: function (item) {
            this.items.splice(this.items.indexOf(item), 1)
        },
    },
    computed: {
        incompleteItem: function () {
            return this.items.filter(function(item) {
                return item.completed === false
            })
        },
        completeItem: function () {
            return this.items.filter(function(item) {
                return item.completed === true
            })
        }
    }
})