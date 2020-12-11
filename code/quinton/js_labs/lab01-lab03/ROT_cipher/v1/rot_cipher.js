let english_rot = {
    a: 'n', b: 'o', c: 'p', d: 'q', e: 'r', f: 's', 
    g: 't', h: 'u', i: 'v', j: 'w', k: 'x', l: 'y',
    m: 'z', n: 'a', o: 'b', p: 'c', q: 'd', r: 'e',
    s: 'f', t: 'g', u: 'h', v: 'i', w: 'j', x: 'k', 
    y: 'l', z: 'm',
    A: 'N', B: 'O', C: 'P', D: 'Q', E: 'R', F: 'S', 
    G: 'T', H: 'U', I: 'V', J: 'W', K: 'X', L: 'Y',
    M: 'Z', N: 'A', O: 'B', P: 'C', Q: 'D', R: 'E', 
    S: 'F', T: 'G', U: 'H', V: 'I', W: 'J', X: 'K', 
    Y: 'L', Z: 'M'
};

let user_input = prompt('Enter a word or phrase to be translated');
let new_phrase = '';
let special_characters = ['!', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'];

for (let i = 0; i<user_input.length; i++) {
    if (user_input[i] === ' ') {
        new_phrase += ' ';
    } else if (special_characters.includes(user_input[i])) {
        console.log(user_input[i])
        new_phrase += user_input[i];
    } else {
    new_phrase += english_rot[user_input[i]];
    }
}
alert(new_phrase);