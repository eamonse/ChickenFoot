import csv
import random
from typing import Dict, List, Tuple
from domino import Domino
from linked_list import ChickenFootLine, LineNode
from random import randrange
import copy

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
        self.num_players = num_players
        self.max_pips = max_pips
        self.player = 0

        self.hand_list = None
        #overall list of the hand
        self.restricted_list:List[ChickenFootLine] = []
        #the hand list restricted by the start of the game
        self.all_list:List[ChickenFootLine] = []
        #all of the hands in one list
        self.open_list:List[ChickenFootLine] = []
        #the open list when theres no restrictions

    # Starts a game of dominos using the starting double number
    # starting_pips: the number of pips for the starting double domino (e.g. 7 would be passed for a 7-7 in the center)
    # dominos_dealt: a list of starting hand for all players, where each hand is a list of Domino objects.  
    def start_game(self, starting_pips:int, dominos_dealt: List[List[Domino]] = None) -> None:
        self.hand_list = dominos_dealt
        domino = Domino(starting_pips, starting_pips)
        domino.set_open_value(starting_pips)
        #initialize

        for x in range(6):
            line = ChickenFootLine(LineNode(domino))
            self.restricted_list.append(line)
            self.all_list.append(line)
        #for each of the branhes,  create a new chicken foot line and append that to the lists

    # Finds and returns a list of PossibleMove objects representing possible moves that the current player can make
    # based on tiles in their hand and what is open on the board (see object definition above) 
    def find_moves(self) -> List[PossibleMove]:
        move_list:List[PossibleMove] = []
        hand = self.hand_list[self.player]
        #grab the hand of the current player
        if self.restricted_list:
            for card in hand:
                for restricted in self.restricted_list:
                    if card.contains_val(restricted.first.domino.open_value):
                        move_list.append(PossibleMove(restricted, restricted.line_name, card))
        else:
            for card in hand:
                for open in self.open_list:
                    if card.contains_val(open.first.domino.open_value):
                        move_list.append(PossibleMove(open,open.line_name,card))

        return move_list


    
    # Draws the specified domino from the pile into the current player's hand
    # domino: the domino that the user picked from the pile.  
    def draw_domino(self, domino:Domino = None) -> Domino:
        self.hand_list[self.player].append(domino)
    
    # Place specified domino on the head of the place linked list
    # domino: the domino to place
    # place: a linked list of dominos on a path on the board
    def place_domino(self, domino:Domino, place) -> None:
        if domino.is_double == False:
            node = LineNode(domino)
            #gotta figure out how to sort this domino since its not a double it has to slap onto a branch

           
            if place in self.open_list:
                self.open_list.remove(place)
            if place in self.all_list:
                self.all_list.remove(place)
            if place in self.restricted_list:
                self.restricted_list.remove(place)

            place.add(node)
            self.all_list.append(place)
            self.open_list.append(place)
        else:
            #if it is a double
            node = LineNode(domino)

            if place in self.restricted_list:
                self.restricted_list.remove(place)
            if place in self.open_list:
                self.open_list.remove(place)
            if place in self.all_list:
                self.all_list.remove(place)

            place.add(node)
            #throw it in and start up some new branches
            for x in range(3):
                copy = copy.deepcopy(place)
                self.restricted_list.append(copy)
                self.all_list.append(copy)
        self.hand_list[self.player].remove(domino)
            
            

    # Moves on to the next player
    def end_turn(self) -> None:
        if self.player < self.num_players-1:
            self.player = self.player + 1
        else:
            self.player = 0

    # Return a list of strings that represent all paths on the board (same string as the target_line_name), 
    # with the center double of the board as the last one. Paths are represented with hyphens between numbers on a single domino, 
    # and | between dominos.  e.g. A path on a board with a double 12 in the center looks like this: 
    # "7-2|2-2|2-5|5-6|6-6|6-1|1-12|12-12"
    def get_board_paths(self) -> List[str]:
        path_list = []
        for path in self.all_list:
            path_list.append(path.line_name)
        return path_list
