import logging
from player import Player

logging.basicConfig(level=logging.DEBUG)

SHIP_INFO = [
    ("Aircraft Carrier", 5),
#    ("Battleship", 4),
#    ("Submarine", 3),
#    ("Cruiser", 3),
#    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


players = [ 
    Player(
        id = 1,
        ship_info = SHIP_INFO 
    ), 
    Player(
        id = 2,
        ship_info = SHIP_INFO 
    ) 
]


def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


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
    target_column = input("Which column (A-J)? ").lower()
    target_row = input("Which row (1-10)? ")
    
    return (3,5)


def place_ships():
    for player in players:
        print("Alright {}, it's time to place your ships!".format(player.name))
        for ship in player.ships:
            print("- {} (size {})".format(ship.name, ship.size))
            # ship.set_orientation(get_ship_orientation(ship))
            # ship.set_bow(prompt_for_bow_coordinates(ship, BOARD_SIZE))
            logging.debug(ship)


def main():
    logging.debug('main() started')
    # get_player_names()
    print_startup_message()
    print_board(players[0].board())    
    place_ships()


if __name__ == '__main__':
    main()


