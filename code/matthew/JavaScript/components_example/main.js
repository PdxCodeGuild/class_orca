Vue.component('color', {
  props: ['color'],
  data: function() {
    return {
      styleObj: {
        color: this.color
      }
    } 
  },
  template: `
    <div :style="styleObj">{{ color }}</div>
  `
})

const app = new Vue({
  el: '#app',
  data: {
    text: '',
    colors: [],
  },
  methods: {
    addColor: function() {
      this.colors.push(this.text)
      this.text = ''
      console.log(this.colors)
    }
  }
})