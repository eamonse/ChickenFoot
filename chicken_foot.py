import csv
import random
from typing import Dict, List, Tuple
from domino import Domino
from linked_list import ChickenFootLine, LineNode
from random import randrange

# Do not modify; this is used by the tests
class PossibleMove:
    def __init__(self, target_line: ChickenFootLine, target_line_name:str, domino:Domino) -> None:
        self.target_line = target_line
        self.target_line_name = target_line_name
        self.domino = domino

# Chicken Foot Dominos
# *************************************
# See OneNote for game information
# 
# Instructions
# 1) Implement/Customize the ChickenFootLine class on linked_list.py. This is a specialized linked list for the game.  
#    It does not have to include standard linked list functions and can be custom to what you need. Add attributes or 
#    methods as needed, as long as it still uses nodes and pointers to connect elements.
#
# 2) Customize the Domino class to meet your needs (suggested helpers are stubbed; add methods and attributes that will help you)
#
# 3) Implement the ChickenFoot class to run a game of chicken foot, using ChickenFootLine
# 
# Extension: Use Pygame or Tkinter to create an interactive UI for the game that calls the APIs
# You will likely need to modify these APIs with the following: 
# a) start_game: Generate a "chicken yard" with all the dominos with all combinations up to max_pips
# b) start_game: If dominos_dealt is None, pick a random 7 dominos for each player from the "chicken yard"
# c) draw_domino: If domino is None, draw a random tile from the chicken yard you generated in (a). End the 
# game if there are no more tiles
# d) Add an API to calculate the score of each player.  Score is the sum of pips on remaining tiles in hand (lowest is best) 

class ChickenFoot:

    # num_players: the number of players playing the game
    # max_pips: the largest number of pips (dots) on a side of a domino
    def __init__(self, num_players: int, max_pips: int) -> None:
        pass

    # Starts a game of dominos using the starting double number
    # starting_pips: the number of pips for the starting double domino (e.g. 7 would be passed for a 7-7 in the center)
    # dominos_dealt: a list of starting hand for all players, where each hand is a list of Domino objects.  
    def start_game(self, starting_pips:int, dominos_dealt: List[List[Domino]] = None) -> None:
        pass

    # Finds and returns a list of PossibleMove objects representing possible moves that the current player can make
    # based on tiles in their hand and what is open on the board (see object definition above) 
    def find_moves(self) -> List[PossibleMove]:
        pass
    
    # Draws the specified domino from the pile into the current player's hand
    # domino: the domino that the user picked from the pile.  
    def draw_domino(self, domino:Domino = None) -> Domino:
        pass
    
    # Place specified domino on the head of the place linked list
    # domino: the domino to place
    # place: a linked list of dominos on a path on the board
    def place_domino(self, domino:Domino, place) -> None:
        pass

    # Moves on to the next player
    def end_turn(self) -> None:
        pass

    # Return a list of strings that represent all paths on the board (same string as the target_line_name), 
    # with the center double of the board as the last one. Paths are represented with hyphens between numbers on a single domino, 
    # and | between dominos.  e.g. A path on a board with a double 12 in the center looks like this: 
    # "7-2|2-2|2-5|5-6|6-6|6-1|1-12|12-12"
    def get_board_paths(self) -> List[str]:
        pass