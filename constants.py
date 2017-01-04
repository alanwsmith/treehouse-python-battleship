
# The board is square. This value sets both the width and the height.
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

SHIP_COUNT = 3

# The list of ships in the game. 
SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


# Define the alphabet to be used for building the COORDINATE_MAP
# Only the number defined by BOARD_SIZE are used. The full
# alphabet is here to accommodate boards up to 26x26.
LETTERS = "abcdefghijklmnopqrstuvwxyz"


# This map translates the coordinates that a player enters into
# the coordinates used internally to draw the board. 

# TODO: Remove 'cols' and use the full 'columns' name.
COORDINATE_MAP = {
    'cols': dict(zip(LETTERS[:BOARD_SIZE], range(0,BOARD_SIZE))),
    'columns': dict(zip(LETTERS[:BOARD_SIZE], range(0,BOARD_SIZE))),
    'rows': dict(zip(range(1, BOARD_SIZE + 1), range(0, BOARD_SIZE))) 
}


# User facing values for the last column letter and row number.
LAST_COLUMN = LETTERS[BOARD_MAX_INDEX].upper()
LAST_ROW = BOARD_SIZE 
