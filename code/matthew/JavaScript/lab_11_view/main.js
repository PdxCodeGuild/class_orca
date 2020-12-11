var app = new Vue({
  el: '#app',
  data: {
    pendingList: [],
    completedList: [],
    textInput: '',

  },
  methods: {
    appendList: function () {
      this.pendingList.push(this.textInput) 
      // this.pendingList.push(textInput.value) 
    },
    deleteBtn: function (index) {
      console.log(index)
      this.pendingList.splice(index, 1)
    },
    checked: function (index) {
      console.log(index)
      this.completedList.push(this.completedList) 
    }
  }
})