let game_board = document.getElementsByClassName('game_board')



class Player {

    constructor(name, token) {
        this.name = name;
        this.token = token;
    };

};

class Game {

    constructor() {
        this.board_list = [ 1,2,3,4,5,6,7,8,9 ];
    };

    game_board() {
        this.board = `
        ${this.board_list[0]}  |  ${this.board_list[1]}  |  ${this.board_list[2]}
        ${this.board_list[3]}  |  ${this.board_list[4]}  |  ${this.board_list[5]}
        ${this.board_list[6]}  |  ${this.board_list[7]}  |  ${this.board_list[8]}
        `;

        for (let i = 0; i<game_board.length; i++) {
            game_board[i].innerText = this.board_list[i]
        }


        return this.board;
    };

    move(player_move, player_token, player_name) {
        let loop = true;
        while (loop) {
            if (this.board_list.includes(player_move)) {
                player_move --;
                this.board_list[player_move] = player_token;
                break;
            } else {
                alert("Invalid entry. Try again.");
                player_move = parseInt(prompt(this.game_board() + player_name + ", enter your move."));
                loop = true;
            };   
        };
    };

    winner(token) {
        for (let i = 0; i<3; i++) {
            if (this.board_list[i]===token && this.board_list[i+1]===token && this.board_list[i+2]===token) {
                return true;
            };
        };
        for (let j=0; j<3; j++) {
            if (this.board_list[j]===token && this.board_list[j+3]===token && this.board_list[j+6]===token) {
                return true;
            };
        };
        if (this.board_list[0]===token && this.board_list[4]===token && this.board_list[8]=== token) {
            return true;
        } else if (this.board_list[2]===token && this.board_list[4]===token && this.board_list[6]=== token) {
            return true;
        } else {
            return false;
        };
    };

    is_full() {
        for (let x=0; x<9; x++) {
            if (this.board_list[x] === x+1) {
                x--;
                return false;
            };
        };
    };

};

function play_game() {

    let game = new Game();
    let player_1 = new Player('Player 1', 'X');
    let player_2 = new Player('Player 2', 'O');
    let counter = 0;
    let loop = true;
    while (loop) {
        if (counter % 2 === 0) {
        var player = player_1;
        } else {
        var player = player_2;
        };
        let user_input = parseInt(prompt(game.game_board() + "It's your turn, " + player.name));
        game.move(user_input, player.token, player.name);
        counter ++;
        let board_full = game.is_full();
        if (board_full !== false) {
            alert("Cat's game!");
            loop = false;
        }
        is_winner = game.winner(player.token);
        console.log(is_winner);
        if (is_winner === true) {
            alert(player.name + " wins!");
            loop = false;
        }; 
    };

};

play_game();
alert("Reload to play again.");