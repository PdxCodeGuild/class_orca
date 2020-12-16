new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  filters: {
  currencydecimal (value) {
    return value.toFixed(2)
  }
},
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response.data.bpi))
  }
})