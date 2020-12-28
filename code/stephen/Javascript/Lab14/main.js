

let vm = new Vue({
    el: '#app',
    data: {
        deckId: '',
        cardsRemaining: '',
        playerHand: [],
        dealerHand: [],
        playerImgs: [],
        dealerImgs: [],
        dealer: {},
        playerValue: [],
        dealerValue: [],
        playerTotal: 0,
        dealerTotal: 0,
        playing: false,
        hiding: false,
        stayed: false,
        playerBusted: false,
        dealerBusted: false,
        playerWins: 0,
        dealerWins: 0,
        stopAt: 16,
        blackjack: false,
        dealerHitting: false,
        youWon: false,
        dealerWon: false,
        youTied: false,
        ties: 0,
        handEnded: false,
        
        


    },
    methods: {
        getNewDeck: function() {
            axios({
                url: 'https://deckofcardsapi.com/api/deck/new/shuffle/',
                method: 'GET',
                params: {
                    deck_count: 1,
                }
            }).then(response => {
                this.playerHand = []
                this.dealerHand = []
                this.playerImgs = []
                this.dealerImgs = []
                this.dealer = {}
                this.playerValue = []
                this.dealerValue = []
                this.playerTotal = 0
                this.dealerTotal = 0
                this.playing = false
                this.hiding = false
                this.stayed = false
                this.playerBusted = false
                this.dealerBusted = false
                this.blackjack = false
                this.youWon = false
                this.dealerWon = false
                this.youTied = false
                this.handEnded = false

                this.deckId = response.data.deck_id
                this.cardsRemaining = response.data.remaining
                // console.log(this.deckId)
                this.dealCards()
            })
        },
        dealCards: function() {
            let dealUrl = 'https://deckofcardsapi.com/api/deck/' + this.deckId + '/draw/?count=4'
            axios({
                url: dealUrl,
                method: 'GET',
                
            }).then(response => {
                // console.log(response.data)
                // console.log(response.data.cards[0].image)
                for (let i = 0; i < response.data.cards.length; i++) {
                    if (response.data.cards[i].value == "KING" || response.data.cards[i].value == "QUEEN" || response.data.cards[i].value == "JACK") {
                        response.data.cards[i].value = 10
                    }
                    if (response.data.cards[i].value == 'ACE') {
                        response.data.cards[i].value = 11
                    }
                    else {
                        response.data.cards[i].value = parseInt(response.data.cards[i].value)
                    }

                }
                this.playing = true
                this.hiding = true
                let playerCard1 = response.data.cards[0]
                this.playerHand.push(playerCard1)
                let playerCard1Img = response.data.cards[0].image
                this.playerImgs.push(playerCard1Img)
                let playerCard1Value = response.data.cards[0].value
                this.playerValue.push(playerCard1Value)
                
                
                
                let playerCard2 = response.data.cards[2]
                this.playerHand.push(playerCard2)
                let playerCard2Img = response.data.cards[2].image
                this.playerImgs.push(playerCard2Img)
                let playerCard2Value = response.data.cards[2].value
                this.playerValue.push(playerCard2Value)
                
                
                let dealerCard1 = response.data.cards[1]
                this.dealerHand.push(dealerCard1)
                let dealerCard1Img = response.data.cards[1].image
                this.dealerImgs.push(dealerCard1Img)
                let dealerCard1Value = response.data.cards[1].value
                this.dealerValue.push(dealerCard1Value)
                

                let dealerCard2 = response.data.cards[3]
                this.dealerHand.push(dealerCard2)
                let dealerCard2Img = response.data.cards[3].image
                this.dealerImgs.push(dealerCard2Img)
                let dealerCard2Value = response.data.cards[3].value
                this.dealerValue.push(dealerCard2Value)
                // console.log(this.playerValue)
                // console.log(this.dealerValue)

                this.playerTotal = this.playerValue.reduce((a, b) => a + b, 0)
                this.dealerTotal = this.dealerValue.reduce((a, b) => a + b, 0)
                // console.log(this.playerTotal)
                if (this.playerTotal == 21) {
                    this.blackjack = true
                    this.handEnded = true
                    this.playerWins++
                }
                
            })
        },
        playerHit: function() {
            let playerHitUrl = 'https://deckofcardsapi.com/api/deck/' + this.deckId + '/draw/?count=1'
            axios({
                url: playerHitUrl,
                method: 'GET',
        
            }).then(response => {
                for (let i = 0; i < response.data.cards.length; i++) {
                    if (response.data.cards[i].value == "KING" || response.data.cards[i].value == "QUEEN" || response.data.cards[i].value == "JACK") {
                        response.data.cards[i].value = 10
                    }
                    if (response.data.cards[i].value == 'ACE') {
                        response.data.cards[i].value = 11
                    }
                    else {
                        response.data.cards[i].value = parseInt(response.data.cards[i].value)
                    }

                }
                
                let playerCard3 = response.data.cards[0]
                this.playerHand.push(playerCard3)
                let playerCard3Img = response.data.cards[0].image
                this.playerImgs.push(playerCard3Img)
                let playerCard3Value = response.data.cards[0].value
                this.playerValue.push(playerCard3Value)
                
                this.playerTotal = this.playerValue.reduce((a, b) => a + b, 0)
                if (this.playerValue.includes(11) && this.playerTotal > 21) {
                    this.playerTotal = this.playerTotal - 10
                }
                if (this.playerTotal > 21) {
                    this.playerBusted = true
                    this.dealerWins++
                    this.handEnded = true
                    this.calcWinner()
                }
                // console.log(this.playerBusted)

            })
        },
        dealerHit: function() {
            let dealerHitUrl = 'https://deckofcardsapi.com/api/deck/' + this.deckId + '/draw/?count=1'
            axios({
                url: dealerHitUrl,
                method: 'GET',
        
            }).then(response => {
                for (let i = 0; i < response.data.cards.length; i++) {
                    if (response.data.cards[i].value == "KING" || response.data.cards[i].value == "QUEEN" || response.data.cards[i].value == "JACK") {
                        response.data.cards[i].value = 10
                    }
                    if (response.data.cards[i].value == 'ACE') {
                        response.data.cards[i].value = 11
                    }
                    else {
                        response.data.cards[i].value = parseInt(response.data.cards[i].value)
                    }

                }
                
                let dealerCard3 = response.data.cards[0]
                this.dealerHand.push(dealerCard3)
                let dealerCard3Img = response.data.cards[0].image
                this.dealerImgs.push(dealerCard3Img)
                let dealerCard3Value = response.data.cards[0].value
                this.dealerValue.push(dealerCard3Value)
                
                this.dealerTotal = this.dealerValue.reduce((a, b) => a + b, 0)
                if (this.dealerTotal <= 16) {
                    this.dealerHit()
                }
                
                if (this.stayed = true && this.dealerTotal > 16) {
                    this.handEnded = true
                    this.calcWinner()
                }
                this.dealerTotal = this.dealerValue.reduce((a, b) => a + b, 0)
                console.log(this.dealerTotal)
                if (this.dealerTotal > 21 && this.dealerValue.includes(11)) {
                    this.dealerTotal = this.dealerTotal - 10
                    
                } 
                if (this.dealerTotal > 16 && this.dealerTotal.includes(11) && this.playerTotal > this.dealerTotal) {
                    this.dealerTotal = this.dealerTotal - 10
                    
                }  
                if (this.dealerTotal > 21){   
                    this.dealerBusted = true
                    this.dealerHitting = false
                    this.playerWins++
                    this.handEnded = true
                    this.calcWinner()
                    console.log(this.dealerBusted)
                }
                
            })
        },
        stay: function() {
            this.hiding = false
            this.stayed = true
            console.log(this.dealerTotal)
            if (this.dealerTotal <= 16) {
                
                this.dealerHit()
                
                
                
            }
            if (this.dealerTotal > 16 && this.dealerTotal <= 21) {
                this.handEnded = true
                this.calcWinner()
            }
            // if (this.dealerTotal <= 16) {
            //     this.dealerHit()
            // }
            if (this.dealerTotal > 21){   
                this.dealerBusted = true
                this.dealerHitting = false
                this.playerWins++
                this.handEnded = true
                this.calcWinner()
                console.log(this.dealerBusted)
            }

        }, 
        calcWinner: function() {
            if (this.playerTotal > this.dealerTotal && this.dealerTotal <= 21 && this.playerTotal <= 21){
                this.playerWins++
                this.youWon = true

            }
            else if (this.playerTotal <= 21 && this.dealerTotal > 21) {
                this.youWon = true
                this.playerWins++
            }
            else if (this.playerTotal < this.dealerTotal && this.dealerTotal <= 21 && this.playerTotal <= 21){
                this.dealerWins++
                this.dealerWon = true
            }
            else if (this.playerTotal === this.dealerTotal && this.dealerTotal <= 21 && this.playerTotal <= 21 && this.handEnded){
                this.ties++
                this.youTied = true
            }
            
        }
       
    }
})