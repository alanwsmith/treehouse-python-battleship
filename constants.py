
BOARD_SIZE = 10

# The game uses zero based indexes. 
# BOARD_MAX_INDEX is set to make it easy to find the end of the board. 
BOARD_MAX_INDEX = BOARD_SIZE - 1

# These are the markers used in the board display.
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

