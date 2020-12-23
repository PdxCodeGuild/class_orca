var app = new Vue({
    el: '#app',
    data: {
        listItems: [],
        textField: '',
    },
    methods: {
        addBtn: function() {
            this.listItems.push(this.textField)
        }
    }
})