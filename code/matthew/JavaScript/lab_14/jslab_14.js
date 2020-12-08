
let pick_6 = function(){
    let ticket = []
    let counter = 0
    while (true)
    {
       if (counter < 7 ) {
           counter += 1
           var numbers = Math.floor(Math.random() * Math.floor(99)) 
           ticket.push(numbers)
        }
        else {
            return ticket
    }   
        }   
}

let winning_ticket = pick_6()
// console.log(winning_ticket)

let runFunction = function(){
    let counter = 0
    let matches = 0
    let spending = 0
    let winnings = 0
    let singleTicket = []
    
    for (let i=0; i<100000; ++i) {
        let singleTicket = pick_6()
        matches = 0
        spending += -2
        for (let i=0;  i<6; ++i)
        {
            if (singleTicket[i] === winning_ticket[i]){
                matches += 1
            }
        if (matches === 1){
            winnings += 4
            }
        else if (matches === 2){
            winnings += 7
            }
        else if (matches === 3){
            winnings +=100
            }
        else if (matches === 4){
            winnings += 5000
            }
        else if (matches === 5){
            winnings += 1000000
            }
        else if (matches === 6){
            winnings += 25000000
            }
        else {
            continue
            }
        }
    }
    let numberTicketsBought = Math.floor(spending);
    let balance = spending + winnings
    let roi = (winnings - spending) / spending
    console.log(`Winnings: ${winnings}`)
    // alert(`Winnings: ${winnings}`)
    // alert(`You bought ${numberTicketsBought} tickets for $2 each spending ${spending} and won ${winnings}`)
    // alert(`You have lost ${balance}`)
    // alert(`You have a roi of ${roi}`)

    let returnObject = {
        "winnings" : winnings,
        "numberTicketsBought" : numberTicketsBought,
        "balance" : balance,
        "roi" : roi,
    } 
    return returnObject
}


// alert(`Winnings: ${winnings}`)
// alert(`You bought ${numberTicketsBought} tickets for $2 each spending ${spending} and won ${winnings}`)
// alert(`You have lost ${balance}`)
// alert(`You have a roi of ${roi}`)


let btn = document.getElementById("btn")
let winningsDiv = document.getElementById("winnings")
let numberTicketsBoughtDiv = document.getElementById("numberTicketsBought")
let balanceDiv = document.getElementById("balance")
let roiDiv = document.getElementById("roi")


console.log(btn)

btn.addEventListener('click', function() {
    let data = runFunction()    
    console.log(data)
    winningsDiv.innerText = `you won ${data.winnings}`;
    numberTicketsBoughtDiv.innerText = `you bought ${data.numberTicketsBought} for $2 each`;
    balanceDiv.innerText = `you have lost ${data.balance}`;
    roiDiv.innerText = `your ROI is ${data.roi}`;




    // btn.style.display = "none";
    // document.body.removeChild(btn)
    let inputDiv = document.getElementById("inputDiv")
    inputDiv.removeChild(btn)

})



