
BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

SHIP_INFO = [
    ("Aircraft Carrier", 5),
#    ("Battleship", 4),
#    ("Submarine", 3),
#    ("Cruiser", 3),
#    ("Patrol Boat", 2)
]


# Define the alphabet to be used for building the COORDINATE_MAP
LETTERS = "abcdefghijklmnopqrstuvwxyz"


# This map translates the coordinates that a player enters into
# the coordinates used internally to draw the board. 
COORDINATE_MAP = {
    'cols': dict(zip(LETTERS[:BOARD_SIZE], range(0,BOARD_SIZE))),
    'rows': dict(zip(range(1, BOARD_SIZE + 1), range(0, BOARD_SIZE))) 
}

