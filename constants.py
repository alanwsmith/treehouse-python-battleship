
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
    'cols': dict(zip(LETTERS[:BOARD_SIZE], range(0, BOARD_SIZE))),
    'columns': dict(zip(LETTERS[:BOARD_SIZE], range(0, BOARD_SIZE))),
    'rows': dict(zip(range(1, BOARD_SIZE + 1), range(0, BOARD_SIZE)))
}


# User facing values for the last column letter and row number.
LAST_COLUMN = LETTERS[BOARD_MAX_INDEX].upper()
LAST_ROW = BOARD_SIZE

# Setup the text for each banner and prompt key

# I know some of these are longer than pep8 likes, but they are easier to
# deal with that way.

BANNERS = {
    "already_shot_there": "Oops! You already shot at '{error}'. Try again, {player}.",
    "error_duplicate_names_not_allowed": "Oops! The players can't have the same name. Try again.",
    "error_name_is_empty": "Oops! The player's name can't be empty. Try again.",
    "error_name_is_too_long": "Oops! The game can't handle names longer than 18 characters. Try again.",
    "error_ship_collision": "Oops! Starting at '{error}' would collidate with another ship. Try again, {player}.",
    "error_ship_off_grid": "Oops! Starting at '{error}' won't fit on the grid. Try again, {player}.",
    "invalid_coordinates": "Oops! The coordinates '{error}' are invalid. Try again, {player}.",
    "invalid_orientation": "Oops! The orientation '{error}' is invalid. It must be either 'v' or 'h'. Try again, {player}.",
    "name_set": "",
    "none": "",
    "place_next_ship": "Place your next ship, {player}",
    "place_ships": "Alright, {player}. Time to place your ships.",
    "shot_hit": "{player} shot at '{last_shot}' and HIT! ~ (Hiding ships) ~ Pass computer to {opponent}.",
    "shot_missed": "{player} shot at '{last_shot}' and MISSED! ~ (Hiding ships) ~ Pass computer to {opponent}.",
    "shot_sunk": "{player} HIT '{last_shot}' and sunk the {ship}! ~ Pass computer to {opponent}.",
    "shot_won_game": "{player} HIT '{last_shot}' and sunk the {ship}! ~ That was the last one! ~ {player} won!",
    "switch_players": "{player} - Your turn is over ~ (Hiding ships) ~ Pass the computer to {opponent}.",
    "take_shot": "{player}, your ships are visible. The ships of your opponent ({opponent}) are hidden.",
    "welcome": "Welcome to Battleship!"}

PROMPTS = {
    "continue": "{opponent}, hit Enter/Return when you're ready to continue.",
    "front_of_ship_coords": "Where do you want the front of your {ship} (size {size})?",
    "game_over": "Thanks for playing Battleship! (Press Enter/Return to quit.)",
    "get_shot_coordinates": "Where do you want to shoot (e.g. 'h6')?",
    "player_0": "What's the name of the first player?",
    "player_1": "What's the name of the second player?",
    "ship_orientation": "Do you want to place your {ship} (size {size}) [v]ertically or [h]orizontally?"
}
