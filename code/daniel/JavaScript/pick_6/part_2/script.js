let btn = document.getElementById("pick6")
let container = document.getElementById("container")
let global_matches = 0
let play_again = document.getElementById("play_again")

btn.addEventListener('click', main)
play_again.addEventListener('click', function() {
    location.reload()
})

function pick6() {
    let nums = [];
    for (let x=0; x<6; x++) {
        nums.push(Math.floor(Math.random() * 100));
    };
    return nums;
};

function compare_tix(winning_nums, nums) {
    let matches = 0;
    for (let x=0; x<6; x++) {
        if (winning_nums[x] === nums[x]) {
            matches ++;
            global_matches ++
        };
    };
    return matches;
};

function winning_total(x) {
    let points_list = [0, 1, 7, 100, 50000, 1000000, 25000000];
    return points_list[x];
};

function main() {
    // To draw numbers
    let winning_numbers = document.createElement("p")
    let winning_nums = pick6()
    let read_numbers = winning_nums.join(" ")
    winning_numbers.innerText = "The winning numbers are: "+read_numbers
    container.appendChild(winning_numbers)

    // User interaction
    let numbers = document.createElement("p")
    container.appendChild(numbers)

    // Calculate winnings
    let winnings = 0
    let counter = 0;
    while (counter <= 100000) {
        winnings -= 2;
        counter ++;
        let nums = pick6();
        let matches = compare_tix(winning_nums, nums)
        winnings += winning_total(matches)
    };

    // Print results
    let results = document.createElement("h2")
    results.innerText = `Out of 100,000 attempts, there were ${global_matches} matching numbers.\n
                        Your total winnings are: $${winnings}.`
    container.appendChild(results)
    play_again.style.display = "block"
}

