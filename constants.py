
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

# Setup the text for each banner and prompt key
BANNERS = {
    "already_shot_there": "Oops! You already shot there. Try again, {player}.",
    "error_duplicate_names_not_allowed": "Oops! The players can't have the same name. Try again.",
    "error_name_is_empty": "Oops! The player's name can't be empty. Try again.",
    "error_name_is_too_long": "Oops! The game can't handle names longer than 18 characters. Try again.",
    "error_ship_collision": "Oops! That would collidate with another ship. Try again, {player}",
    "error_ship_off_grid": "Oops! That won't fit on the grid. Try again, {player}.",
    "invalid_coordinates": "Oops! Those were invalid coordinates. Try again, {player}.",
    "invalid_orientation": "Oops! The orientation must be either 'v' or 'h'. Try again, {player}.",
    "name_set": "",
    "none": "",
    "place_ships": "Alright, {player}. Time to place your ships.",
    "place_next_ship": "Place your next ship, {player}",
    "shot_hit": "{player} hit at '{last_shot}' - All ships hidden - Pass the computer to {opponent}.",
    "shot_missed": "{player} missed at '{last_shot}' - All ships hidden - Pass the computer to {opponent}.",
    "switch_players": "{player} - Your turn is over. Hand the computer over to {opponent}.",
    "take_shot": "{player} your ships are visible. The ships of your opponent {opponent} are hidden.",
    "welcome": "Welcome to Battleship!",
}

PROMPTS = {
    "player_0": "What's the name of the first player?",
    "player_1": "What's the name of the second player?",
    "ship_orientation": "Do you want to place your {ship} (size {size}) [v]ertically or [h]orizontally?", 
    "front_of_ship_coords": "Where do you want the front of your {ship} (size {size})?",
    "get_shot_coordinates": "What coordinates do you want to shoot at?",
    "continue": "{opponent}, hit Enter/Return when you're ready to continue.",
}
