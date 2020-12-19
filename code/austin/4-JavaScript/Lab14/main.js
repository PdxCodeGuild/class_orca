let vm = new Vue ({
    el: '#app',
    data: {
        dogs: [],
        randoDogs: [],
        matches: [],
        yourMatches: [],
        image: { url: " " },
        key: "",
        name: "",
        temparament: "",
        newList: [],
        account: 0,
        counts: [],
        noMatch: "",
    },
    
    methods: {
        loadDog: function() {
            this.matches = []
            this.newList = []
            this.results = []
            this.counts = []
            this.results = []
        
            axios({
                url: "https://api.thedogapi.com/v1/breeds",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                
            }).then(response => {
                    this.randoDogs = [];
                    this.dogs = response.data.filter(dog => dog.breed_group)
                    for (let i = 0; i < 6; i++){
                            let rand = this.dogs[Math.floor(Math.random() * this.dogs.length)];
                            this.randoDogs.push(rand);
                    }
                    console.log(this.randoDogs, "Dog array")
                    this.getMatches()
            })   
        },
        getMatches: function() {
            this.randoDogs.forEach(element => {
                this.matches[element.breed_group] ? this.matches[element.breed_group] += 1 : this.matches[element.breed_group] = 1    
            });
            this.showMatches()
        }, 
        showMatches: function() {
            console.log(this.matches, "MATCHES")
            let dogKeys= Object.keys(this.matches)
            let dogValues=Object.values(this.matches)
            console.log(dogKeys, "DOG KEYS", dogValues, "DOG VALUES")
            console.log(dogValues.length, "LENGTH")
        
            dogKeys.forEach(item => {
                if (dogValues[dogKeys.indexOf(item)] > 1) {
                    this.newList.push(item + ": " + dogValues[dogKeys.indexOf(item)])
                }  
            })

            this.counts = dogValues.filter(el => el > 1)
            this.results = this.counts.reduce(function(a, b){
                return a + b
            })

            console.log(this.newList, "NEW LIST")
            console.log(this.results)
        }
    }
})



