var app = new Vue({
  el: '#app',
  data: {
    pendingList: [],
    completedList: [],
    textInput: '',

  },
  methods: {
    appendList: function() {
      this.pendingList.push(this.textInput) 
      // this.pendingList.push(textInput.value) 
    },
    deleteBtn: function(index) {
      this.pendingList.splice(index, 1)
    },
    checked: function(index) {
      this.completedList.push(this.textInput) 
    },
    compltedDeleteBtn: function (index) {
      this.completedList.splice(index, 1)
    }
  }
})