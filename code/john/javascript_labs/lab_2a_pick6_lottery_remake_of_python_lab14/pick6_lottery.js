// ##############################################################################
// # John Fial, PDX Code Guild, 2020-2021
// # python version: https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab14-pick6.md
// ##############################################################################


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

// # create then store the winning ticket
winning_ticket = [];
winning_ticket = pick6(winning_ticket);
console.log(`winning_ticket: ${winning_ticket}`);

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
// match_numbers(winning_ticket, test_ticket1)

// # Stored dictionary of how much money we earn with each matched number
winnings_dictionary_object = { // objects are like Python dictionaries
  // number matches : winnings in $ dollars
  // REMEMBER, IT'S AN OBJECT, CALLED WITH: winnings_dictionary_list.3 or .5 or whatever
  // person.age += 1;
  // person['age'] += 1;
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000,
};

// # Create new user balance
user_balance = 0;

// # We don't want this defined within the loop, because it'd be overwritten (unless I make a loop?)
cumulative_winnings = 0;

// # later I could make this an input...
tickets_purchased = 90;

// # Here's where we go through all the tickets purchased and change the balance
for (i=0; i<tickets_purchased; i++) {
    let ticket = []; // # Create a blank ticket and generate its ticket numbers  
    pick6(ticket);
    console.log(`testing ticket ${i} / ${tickets_purchased}, ticket #: ${ticket}`);

    matching_number_total = match_numbers(winning_ticket, ticket); // # Compare their ticket to the winning ticket, storing the number of matching numbers...

    // # ... and comparing the number to the winnings dictionary.
    user_winnings = winnings_dictionary_object[matching_number_total];

    // # Subtract ticket price, and add the user's winnings to their balance
    user_balance -= 2;
    user_balance += user_winnings

    // # Add their winnings to a total so we can tell them just how much they won in total
    cumulative_winnings += user_winnings;
};


// # The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
let expenses = tickets_purchased * 2;
let return_on_investment = ( cumulative_winnings - expenses ) / expenses;
console.log(`return_on_investment: ${return_on_investment}, expenses: $${expenses}, cumulative_winnings: $${cumulative_winnings} `)

// # **************************************** WORKING FROM HERE *******************************
// # ****************************************  TO HERE ****************************************