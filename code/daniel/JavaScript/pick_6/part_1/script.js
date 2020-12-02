function pick6() {
    let nums = [];
    for (let x=0; x<6; x++) {
        nums.push(Math.floor(Math.random() * 100));
    };
    return nums;
};

function compare_tix(winning, drawn) {
    let matches = 0;
    for (let x=0; x<6; x++) {
        if (winning[x] === drawn[x]) {
            matches ++;
        };
    };
    return matches;
};

function winning_total(x) {
    let points_list = [0, 1, 7, 100, 50000, 1000000, 25000000];
    return points_list[x];
};

function main() {
    let winning_nums = pick6();
    let net_winnings = 0;
    let counter = 0;
    while (counter <= 100000) {
        net_winnings -= 2;
        counter ++;
        let gambler_nums = pick6();
        let matching_nums = compare_tix(winning_nums, gambler_nums);
        let winnings = winning_total(matching_nums);
        net_winnings += winnings;
    };
    alert("You're net winnings are $" + Math.round(net_winnings) + ".");
    let roi = net_winnings/(counter*2);
    alert("Your ROI is " + Math.round(roi * 1000)/1000 + ".");
};

main()