var app = new Vue({
    el: '#app',
    data: {
      toDoList: [],
      textInput: '',
   },
  methods: {
    addToListBtn: function() {
      this.toDoList.push(this.textInput)
  }
}
})