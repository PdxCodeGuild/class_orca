Vue.component('times-two', {
  props: ['nums'],
  template: `<div>
    <div v-for="num in nums">
      <div>{{ num }} times two is {{ num * 2 }}</div>
    </div>
  </div>`
})
