let start = prompt('what is the distance?')
let input = prompt('what are the input units? (ft, m, mi, km, yd, in)')
let output = prompt('what are the output units? (ft, m, mi, km, yd, in)')
let answer = 0
let final = 0

if (input == 'ft') {
    answer += start * .3048
} else if (input == 'm') {
    answer += start * 1
} else if (input == 'mi') {
    answer += start * 1609.34
} else if (input == 'km') {
    answer += start * 1000
} else if (input == 'yd') {
    answer += start * .9144
} else if (input == 'in') {
    answer += start * .0254
}
if (output == 'mi') {
    final += answer / 1609.34
} else if (output == 'km') {
    final += answer / 1000
} else if (output == 'm') {
    final += answer
} else if (output == 'ft') {
    final += answer / .3048
} else if (output == 'yd') {
    final += answer / .9144
} else if (output == 'in') {
    final += answer / .0254
}
alert(start + input + ' is ' + final + output)