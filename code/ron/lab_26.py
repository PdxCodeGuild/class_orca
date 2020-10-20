
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab26
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-15-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 26: Tic-Tac-Toe

'''
#----Modules--------------------------------------------------------

import string
import math
import random

#----Dictionary/Lists-------------------------------------------------

board = [
    ["\n     ","0"," ","1"," ","2"," "],    
    ["    ","---","---","---"],
    ["  0 |"," ","|"," ","|"," ","|"],
    ["    ","---","---","---"],
    ["  1 |"," ","|"," ","|"," ","|"],
    ["    ","---","---","---"],
    ["  2 |"," ","|"," ","|"," ","|"],
    ["    ","---","---","---"],
]

#----Classes--------------------------------------------------------

class Game:
   def __init__(self, board):
      self.board = board

   def __repr__(self):
      for x in range(len(self.board)):
         print(' '.join(self.board[x]))
      # print('\n') #formatting

   def move(self, xy, player):
   # y.Line 1 index 2
      if xy == "0,0":
         self.board[2][1] = player.token
      if xy == "0,1":
         self.board[2][3] = player.token
      if xy == "0,2":
         self.board[2][5] = player.token
   # y.Line 2 index 4
      if xy == "1,0":
         self.board[4][1] = player.token
      if xy == "1,1":
         self.board[4][3] = player.token
      if xy == "1,2":
         self.board[4][5] = player.token
   # y.Line 3 index 6
      if xy == "2,0":
         self.board[6][1] = player.token
      if xy == "2,1":
         self.board[6][3] = player.token
      if xy == "2,2":
         self.board[6][5] = player.token
      self.__repr__()
      self.is_game_over(player)

   def calc_winner(self, player):
      count = 0
      # Checks y0 for win
      for y in range(2,7,2):
         if self.board[y][1] == (player.token):
            count += 1
            if count == 3:
               return(True)
      # Checks y1 for win
      count = 0
      for y in range(2,7,2):
         if self.board[y][3] == (player.token):
            count += 1
            if count == 3:
               return(True)
      # Checks y2 for win
      count = 0
      for y in range(2,7,2):
         if self.board[y][5] == (player.token):
            count += 1
            if count == 3:
               return(True)
      count = 0
      # Checks x0 for win
      for x in range(1,6,2):
         if self.board[2][x] == (player.token):
            count += 1
            if count == 3:
               return(True)
      count = 0
      # Checks x1 for win
      for x in range(1,6,2):
         if self.board[4][x] == (player.token):
            count += 1
            if count == 3:
               return(True)
      count = 0
      # Checks x2 for win
      for x in range(1,6,2):
         if self.board[6][x] == (player.token):
            count += 1
            if count == 3:
               return(True)
      count = 0
      # Checks diagnol 0,0 - 2,2 for win
      if self.board[2][1] == (player.token):
         if self.board[4][3] == (player.token):
            if self.board[6][5] == (player.token):        
               return(True)
      count = 0
      # Checks diagnol 2,0 - 0,2 for win
      if self.board[6][1] == (player.token):
         if self.board[4][3] == (player.token):
            if self.board[2][5] == (player.token):        
               return(True)

   def is_full(self):
      count = 0
      for y in range(2,7,2):
         for x in range(1,6,2):
            if self.board[y][x] in ('X', 'O'):
               count += 1
               if count == 9:
                  return True

   def is_game_over(self, player):
      win = self.calc_winner(player) 
      if win == True:
         print(f'\nCongrats {player.name} - you are a tic-tac-toe Tiger!\n')
         exit()
      if self.is_full() == True:
         print(f'\nEveryone is a loser\n')
         exit()

   def initialize(self):
      self.__repr__()

class player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

#----Main-----------------------------------------------------------

def main():

   print('''
"Catch a tiger by it's...
   Tic Tac Toe" 
      ''')

   # Start it up
   g1 = Game(board)
   p1 = player("Player 1","X")
   p2 = player("Player 2", "O")
   print((f'   {p1.name} - {p1.token}'))
   print((f'   {p2.name} - {p2.token}'))
   g1.initialize()

   # Game play
   while True:
      g1.move((input(f"\n{p1.name}, it's your turn (x,y): ")), p1)
      g1.move((input(f"\n{p2.name}, it's your turn (x,y): ")), p2)

main()





