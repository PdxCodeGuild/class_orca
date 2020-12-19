let vm = new Vue ({
    el: '#app',
    data: {
        dogs: [],
        randoDogs: [],
        matches: [],
        yourMatches: [],
        image: { url: " "},
        searchTerm: "",
        key: "",
        name: "",
        temparament: "",
    },
    
    methods: {
        loadDog: function() {
            axios({
                url: "https://api.thedogapi.com/v1/breeds",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                
            }).then(response => {
                    this.randoDogs = [];
                    this.dogs = response.data.filter(dog => dog.breed_group)
                    for (let i = 0; i < 5; i++){
                            let rand = this.dogs[Math.floor(Math.random() * this.dogs.length)];
                            this.randoDogs.push(rand);
                    }
                    console.log(this.randoDogs, "Dog array")
                    this.getMatches()
                    this.showMatches()
            })   
        },
        getMatches: function() {
            this.randoDogs.forEach(element => {
                this.matches[element.breed_group] ? this.matches[element.breed_group] += 1 : this.matches[element.breed_group] = 1    
            });
        }, 
        showMatches: function() {
            console.log(this.matches, "MATCHES")
            for (i = 0; i < this.matches.length; i++){
                for (j = 0; j < this.matches.length; j++){
                    if (this.matches[i][j] > 1) {
                        yourMatches.push(this.matches[i][j])
                    }
                } 
            }
            console.log(this.yourMatches, "YOUR MATCHES")
        }
    }
})



