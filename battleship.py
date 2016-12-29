import constants 
import logging
from player import Player
from ship import Ship

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

    # Using two infinite while loops here. One each for the column and the row. 
    # Each one checks for validity and starts over if the entered value isn't
    # valid. Once both are valid, the method returns. Based on the size of this
    # this mehtod, it's not an ideal way to do this. Good candidate for refactoring.

    # I didn't put break statements assuming python will take care of that. 

    # Grab the last letter for column and number for row based on board size.
    last_letter = constants.LETTERS[constants.BOARD_MAX_INDEX].upper()
    last_number = constants.BOARD_SIZE 

    while True:
        target_column = input("Which column (A-{})? ".format(last_letter)).lower()
        if target_column not in constants.COORDINATE_MAP['cols']:
            print("Oops! That wasn't a valid row. Try one more time")
            continue
        else:
            while True:
                target_row = input("Which row (1-{})? ".format(last_number)) 
                try:
                    target_row = int(target_row)
                except ValueError:
                    print("Oops! The row must be a number. Give it another shot.")
                    continue
                if target_row not in constants.COORDINATE_MAP['rows']:
                    print("Oops! '{}' is not a valid row. Give it another shot.".format(target_row))
                    continue
                else:
                    return(target_column, target_row)



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
#    ship = Ship(name = "FloatingTest", size = 5)
#    ship.place()
#    print(ship)

    main()
    pass


