cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

your_cards = []
count = 0

# function that gets the user input 
def user_input ():
  #ask the user for a card
  card = input('enter card1 ie.(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, or k): ')
  #check to see if car is in the provided list 
  if card in ['j', 'q', 'k']:
    #set the card ten
    card = 10
    #put the card in my cards
    your_cards.append(card)

  elif card in cards:
    card = int(card)
    your_cards.append(card)
  else:
    print('enter a valid card')
    user_input()  

def count_card ():
  total = 0
  for x in your_cards:
    total += x

  if total < 17:
    advise = 'hit'
  elif total >= 17 and total < 21:
    advise = 'stay'
  elif total > 21:
    advise = 'busted'
  else:
    advise = 'Blackjack'
  return advise


while count < 3:
  count += 1
  user_input()

  if count == 3:
    print(count_card())

