import constants 
import logging
from player import Player

logging.basicConfig(level=logging.INFO)


players = [ 
    Player(
        id = 1,
        ship_info = constants.SHIP_INFO 
    ), 
    Player(
        id = 2,
        ship_info = constants.SHIP_INFO 
    ) 
]


# Define the alphabet to be used for building the COORDINATE_MAP

# This map translates the coordinates that a player enters into
# the coordinates used internally to draw the board. 
COORDINATE_MAP = {
    'cols': dict(zip(constants.LETTERS[:constants.BOARD_SIZE], range(0,constants.BOARD_SIZE))),
    'rows': dict(zip(range(1, constants.BOARD_SIZE + 1), range(0, constants.BOARD_SIZE))) 
}


def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def get_player_names():
    for player in players:
        player.ask_for_name()


def print_startup_message():
    print('Starting new game for {} and {}.'.format(players[0].name, players[1].name))


def get_ship_orientation(ship):
    orientation = input("  Would you like to place your {} [v]ertically or [h]orizontally? ".format(ship.name)).lower()
    if orientation == "v" or orientation == "h":
        return orientation
    else:
        print("  That didn't work. You must choose either 'v' for vertically or 'h' for horizontally.")
        get_ship_orientation(ship)

def prompt_for_bow_coordinates(ship, board_size):
    target_column = input("Which column (A-{})? ".format(constants.LETTERS[constants.BOARD_SIZE - 1].upper())).lower()
    target_row = int(input("Which row (1-{})? ".format(constants.BOARD_SIZE)))
    if target_column in COORDINATE_MAP['cols']:
        if target_row in COORDINATE_MAP['rows']:
            return (COORDINATE_MAP['rows'][target_row], COORDINATE_MAP['cols'][target_column])
        else:
            print("Oops! '{}' is not a valid row. Give it another shot.".format(target_row))
            prompt_for_bow_coordinates(ship, board_size)
    else:
        print("Oops! '{}' is not a valid column. Give it another shot.".format(target_column))
        prompt_for_bow_coordinates(ship, board_size)

def place_ships():
    for player in players:
        print("Alright {}, it's time to place your ships!".format(player.name))
        for ship in player.ships:
            print("- {} (size {})".format(ship.name, ship.size))
            # ship.set_orientation(get_ship_orientation(ship))
            ship.set_bow(prompt_for_bow_coordinates(ship, constants.BOARD_SIZE))
            logging.debug(ship)


def main():
    logging.debug('main() started')
    # get_player_names()
    print_startup_message()
    print_board(players[0].board())    
    place_ships()


if __name__ == '__main__':
    main()
    pass


