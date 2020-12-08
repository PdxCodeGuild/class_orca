// ##############################################################################
// # John Fial, PDX Code Guild, 2020-2021
// # python version: https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab14-pick6.md
// ##############################################################################
// REMEMBER TO ALWAYS END LINES WITH ; SEMICOLONS;


function getRandomInt_strip_zeroes(max) {
    // from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random  
    random_number = Math.random();
    random_int_with_zeroes = Math.floor(random_number * Math.floor(max));

    while (random_int_with_zeroes === 0) { // if it's 0, redo it, then return number, otherwise keep trying
      random_number = Math.random();
      random_int_with_zeroes = Math.floor(random_number * Math.floor(max));
    };
    return random_int_with_zeroes;
    // };
};
  
winning_ticket = [];

// # Define a function to pick 6 numbers between 1-99 and store them in a simple list:
function pick6(ticket_name) {
    // console.log('pick6() FUNCTION START');
    for (let i=0; i<6; i++) {; //remember that starting at 0, i<6 is SIX numbers
      let temp_number = getRandomInt_strip_zeroes(99);
      ticket_name[i] = temp_number;
      // console.log(`temp_number: ${temp_number} inserted at [i] ${i}, and ticket_name now: ${ticket_name} `);
    };
    // console.log(`ticket_name: ${ticket_name}`);
    // console.log('pick6() FUNCTION END');
    return ticket_name
};

function generate_winning() {    
    if ( winning_ticket == '' ) { // i thought [] would work, but apperently JS wants a '' for an empty array!
         winning_ticket = pick6(winning_ticket);
         console.log(winning_ticket);
         let winning_ticket_text = document.createElement("h4");
         winning_ticket_text.innerText = `Winning ticket: [${winning_ticket}]`;
         winning_ticket_html.appendChild(winning_ticket_text);
    } // good example of where NOT to put a semicolon!
    else {
        alert('There can be only One Ring To Ru----err, One Ticket!');
    };
 };

// make some test tickets
test_ticket1 = [28,3,5,6,7,8];
test_ticket2 = [37,71,69,28,67,96];

// # making the function to match how many numbers
function match_numbers(winning_ticket, ticket) {
    let matching_number_total = 0;
    // console.log(`testing ticket: ${ticket} vs. winning_ticket: ${winning_ticket}`);
    for (let i=0; i<6; i++) {
        if ( ticket[i] === winning_ticket[i] ) {
        matching_number_total += 1;
        };
        // console.log(`matching_number_total: ${matching_number_total} for i:${i} `);
    };
    return matching_number_total;
};


function main(user_balance=0, tickets_purchased=1000){ // MAIN FUNCTION START

        // # Stored dictionary of how much money we earn with each matched number
        winnings_dictionary_object = { // objects are like Python dictionaries
            // REMEMBER, IT'S AN OBJECT, CALLED WITH: winnings_dictionary_list.3 or .5 or whatever   // person.age += 1;   // person['age'] += 1;
            // number matches : winnings in $ dollars
            0:0,
            1:4,
            2:7,
            3:100,
            4:50000,
            5:1000000,
            6:25000000,
        };

        // # Create new user balance
        // user_balance = 0;

        // # We don't want this defined within the loop, because it'd be overwritten (unless I make a loop?)
        cumulative_winnings = 0;

        // # later I could make this an input...
        // tickets_purchased = 10000;

        // # Here's where we go through all the tickets purchased and change the balance
        for (i=0; i<tickets_purchased; i++) {
            let ticket = []; // # Create a blank ticket and generate its ticket numbers  
            pick6(ticket);
            // console.log(`testing ticket ${i} / ${tickets_purchased}, ticket #: ${ticket}`);

            matching_number_total = match_numbers(winning_ticket, ticket); // # Compare their ticket to the winning ticket, storing the number of matching numbers...

            // # ... and comparing the number to the winnings dictionary.
            user_winnings = winnings_dictionary_object[matching_number_total];

            // # Subtract ticket price, and add the user's winnings to their balance
            user_balance -= 2;
            user_balance += user_winnings

            // # Add their winnings to a total so we can tell them just how much they won in total
            cumulative_winnings += user_winnings;};

        // # The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
        let expenses = tickets_purchased * 2;
        let return_on_investment = ( cumulative_winnings - expenses ) / expenses;
        // console.log(`Congratulations, you won a total of $${cumulative_winnings}! However, we suppose you shouldn't celebrate so quickly, because buying ${tickets_purchased} tickets cost you a total of $${expenses}. Therefore, your net balance is $${user_balance}, making your return on investment: ${return_on_investment}! Thanks for giving the lottery your hard earned money!`);
        
        let p_text = document.createElement("p");
        p_text.innerText = `Congratulations, you won a total of $${cumulative_winnings}! However, we suppose you shouldn't celebrate so quickly, because buying ${tickets_purchased} tickets cost you a total of $${expenses}. Therefore, your net balance is $${user_balance}, making your return on investment: ${return_on_investment}! Thanks for giving the lottery your hard earned money!`;
        results.appendChild(p_text);

}; // MAIN FUNCTION END

let button_play = document.getElementById("button_play");
let field_tickets_purchased = document.getElementById("field_tickets_purchased");
let field_starting_balance = document.getElementById("field_starting_balance");
let button_play_again = document.getElementById("button_play_again");

// # **************************************** WORKING FROM HERE *******************************

    // HTML IDs USED:
        // <button id="button_generate">
        // <p id="winning_ticket_html"> */
        // <p id="results"> */
        // <input id="field_tickets_purchased" type="text" placeholder="Number of tickets purchased:">
        // <input id="field_starting_balance" type="text" placeholder="Starting Balance:"> */

function verify_integer (input) {
    // console.log(typeof(input))
    console.log(`parseInt(input) ::: ${parseInt(input)}`)

    if (input === '') {
        console.log('empty input!, returing as undefined');
        return;
    }
    else if (isNaN(input)) {
        console.log('seems to be a non-number');
        alert('must be a number!')
    }
    else {
        // console.log(`typeof(input) WAS: ${typeof(input)}`);
        input = parseInt(input);
        // console.log(`typeof(input) is NOW: ${typeof(input)}`);
        console.log(typeof(input))
        return input
    };
};


button_play.addEventListener('click', function(e) { // Uncaught TypeError: Cannot read property 'addEventListener' of null at pick6_lottery.js:141
    // console.log("clicked button!")

    tickets_purchased = verify_integer(field_tickets_purchased.value)
    // console.log(`tickets_purchased is now ${tickets_purchased}`)
    user_balance =  verify_integer(field_starting_balance.value)
    // console.log(`user_balance is now ${user_balance}`)

    main(user_balance, tickets_purchased);
    // ;sending empty string
    // console.log(`field_tickets_purchased.value is ${field_tickets_purchased.value}`);
    // console.log(`field_starting_balance.value is ${field_starting_balance.value}`);
});

// # ****************************************  TO HERE ****************************************

generate_winning()

button_play_again.addEventListener('click', function(e) {
    location.reload();
});