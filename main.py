## import game parts

from piece import Piece
from dice import Dice
# from player import 
from board import Board

## initiate game structure

my_board = Board()
my_dice = Dice()
my_pieces = {}

for team in 'ABCD':
    for i in range(4):
        my_pieces[f'team{team}{i}'] = Piece(team, i)



