from typing import List
from domino import Domino

# The ChickenFootLine class is a specialized linked list for the game.  
# It does not have to include standard linked list functions and can be custom to what you need. Add attributes or 
# methods as needed, as long as it still uses nodes and pointers to connect elements.
# Adding parameters or changing attribute names to your liking will not break any tests.
class LineNode:
   def __init__(self, domino: Domino):
      self.next = None
      self.domino = domino


class ChickenFootLine:
   # chicken_foot is the domino that branches out
   def __init__(self, chicken_foot:Domino) -> None:
      self.first = LineNode(chicken_foot)
      self.line_name = str(chicken_foot) # line_name should be a string representing the entire line in the format "7-2|2-2|2-5|5-5", where last entry is the center

   def add(self, domino: Domino):
      pass