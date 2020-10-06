start = float(input('what is the distance?\n>'))
input_units = input('what are the input units?\n>')
output_units = input('what are the output units?\n>')
answer = 0
final = 0

if input_units == 'ft':
    answer += start * .3048
elif input_units == 'm':
    answer += start * 1
elif input_units == 'mi':
    answer += start * 1609.34
elif input_units == 'km':
    answer += start * 1000
elif input_units == 'yd':
    answer += start * .9144
elif input_units == 'in':
    answer += start * .0254

if output_units == 'mi':
    final += answer / 1609.34
elif output_units == 'km':
    final += answer / 1000
elif output_units == 'm':
    final += answer
elif output_units == 'ft':
    final += answer / .3048
elif output_units == 'yd':
    final += answer / .9144
elif output_units == 'in':
    final += answer / .0254

print(f'{start} {input_units} is {final:.4f} {output_units}')