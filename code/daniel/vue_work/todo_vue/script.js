
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
    },
    computed: {
        completeItem: function (item) {
            console.log(item)
            item.completed = true
        },
        deleteItem: function (item) {

        
    },

    
})
