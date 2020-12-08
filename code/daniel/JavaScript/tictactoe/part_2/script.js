// Golbal Variables
let play_btn = document.getElementById("play")
let game_board = document.getElementById("game_board")
let player_1
let player_2 
let game
let play_square
let game_play = [ '','','', '','','', '','','' ] 
let counter = 0

// buttons \\ 
play_btn.addEventListener('click', generate_players)

function generate_players() {
    let name_1 = prompt("Player 1, enter your name.")
    player_1 = new Player(name_1, "X")
    let name_2 = prompt("Player 2, enter your name.") 
    player_2 = new Player(name_2, "O") 
    console.log(player_1, player_2)
    play_btn.remove()
    game = new Game()
    game.generate_game_board()
}

class Player {
    constructor(name, token) {
        this.name = name;
        this.token = token;
    };
};

class Game {
    constructor() {}
    generate_game_board() {
        play_square = document.createElement("div")
        play_square.id = "game_grid"
        for (let i=0; i<9; i++) {
            let box = document.createElement("p")
            box.id = "piece"
            let index = document.createElement("button")
            index.class = "piece_button"
            index.addEventListener('click', this.player_move)
            index.addEventListener('click', this.check_win)
            index.addEventListener('click', this.check_cats)
            index.id = i
            index.innerText = '' 
            box.appendChild(index)
            play_square.appendChild(box)
        }
        game_board.appendChild(play_square)
    }
    player_move(event) {
        let id = event.target.id
        let move = document.getElementById(event.target.id) 
        if (move.innerText === ''){
            if (counter % 2 === 0) {
                counter ++
                move.innerText = "X"
                game_play[id] = "X"
            } else {
                counter ++
                move.innerText = "O"
                game_play[id] = "O"
            }
        }
    }
    check_win(event) {
        let play_again = document.createElement("button")
        play_again.innerText = "Play again?"
        play_again.addEventListener('click', function(event) {location.reload()})
        let move = document.getElementById(event.target.id)
        let token = move.innerText
        for (let i = 0; i<3; i+=3) {
            if (game_play[i]===token && game_play[i+1]===token && game_play[i+2]===token) {
                console.log(token)
                if (token === "X") {
                    play_square.innerText = `${player_1.name} won!`
                    game_board.appendChild(play_again)
                } else {
                    play_square.innerText = `${player_2.name} won!`
                    play_square.appendChild(play_again)
                }
            };
        };
        for (let j=0; j<3; j+=3) {
            if (game_play[j]===token && game_play[j+3]===token && game_play[j+6]===token) {
                if (token === "X") {
                    play_square.innerText = `${player_1.name} won!`
                } else {
                    play_square.innerText = `${player_2.name} won!`
                }
            };
        };
        if (game_play[0]===token && game_play[4]===token && game_play[8]=== token) {
            if (token === "X") {
                play_square.innerText = `${player_1.name} won!`
            } else {
                play_square.innerText = `${player_2.name} won!`
            }
        } else if (game_play[2]===token && game_play[4]===token && game_play[6]=== token) {
            if (token === "X") {
                play_square.innerText = `${player_1.name} won!`
            } else {
                play_square.innerText = `${player_2.name} won!`
            }
        } else {
            return false;
        };
    }
    check_cats() {
        let num_str = game_play.toString()
        if (num_str.length === 17) {
            play_square.innerText = "Cat's game!"

        }
    }
}