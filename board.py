import constants
import logging

from ship import Ship

class Board():
    
    def __init__(self, **kwargs):
        self.index = kwargs['index']
        self.player_name = "Player {}".format(self.index + 1)
        self.ships = [] 
        self.load_ships()
        logging.info("Created board {}".format(self.index))

    def grid(self):
        grid = []
        for new_row in range(0, constants.BOARD_SIZE):
            row = []
            for column_index in range(0, constants.BOARD_SIZE):
                row.append('O')
            grid.append(row)
        return grid 


    def load_ships(self):
        for ship in constants.SHIP_INFO:
            self.ships.append(Ship(name = ship[0], size = ship[1]))

    def get_letter(self, **kargs):
        while True:
            raw_response = input(kargs['prompt'] + " ")
            if len(raw_response) == 0:
                print("Oops! You didn't make a selection. " + kargs.get('error_extension'))
                continue
            else:
                response = raw_response.strip().lower()[0]
                if response not in kargs['valid_values']:
                    print("Oops! '{}' isn't valid. ".format(raw_response) + kargs.get('error_extension'))
                    continue
                else:
                    return response

    def get_number(self, **kargs):
        while True:
            raw_response = input(kargs['prompt'] + " ").strip()
            if len(raw_response) == 0:
                print("Oops! You didn't make a selection. " + kargs.get('error_extension'))
                continue
            else:
                try:
                    response = int(raw_response)
                except ValueError:
                    print("Oops! That wasn't a number. Give it another shot.")
                    continue
                else:
                    if response not in kargs['valid_values']:
                        print("Oops! That wasn't a valid row. Try again.")
                        continue
                    else:
                        return response

    def place_ships(self):

        for ship in self.ships:

            ship.orientation = self.get_letter(
                prompt = "[v] or [h]?",
                valid_values = ['v', 'h'],
                error_extension = "You can only choose 'v' or 'h'"
            )

            column_letter_for_bow = self.get_letter(
                prompt = "What column do you want the front of the ship in (A-{})?".format(constants.LAST_COLUMN),
                valid_values = [chr(c) for c in range(ord('a'), ord('a') + constants.BOARD_SIZE)],
                error_extension = "You can only choose 'A' thru '{}'".format(constants.LAST_COLUMN)
            )

            ship.bow_column = constants.COORDINATE_MAP['columns'][column_letter_for_bow]

            row_display_letter_for_bow = self.get_number(
                prompt = "What row do you want the front of the ship in (1-{})?".format(constants.LAST_ROW),
                valid_values = [num for num in range(1, constants.BOARD_SIZE + 1)],
                error_extension = ""
            )

            ship.bow_row = constants.COORDINATE_MAP['rows'][row_display_letter_for_bow] 

    def set_player_name(self, name):
        if len(name) == 0:
            logging.info("Invalid empty player name")
            return 'error_empty_name'
        elif len(name) > 18:
            logging.info("Player name is too long")
            return 'error_name_is_too_long'
        else:
            logging.info("Set board {} player_name to {}".format(self.index, name)) 
            self.player_name = name
            return 'name_set' 
        



    def show(self):
        for row in range(0,10):
            print(str(row + 1).rjust(2), end='')
            for col in range(0, 10):
                print(" O", end='')
            print('')


if __name__ == '__main__':
    board = Board(index = 0)
    board.show()
    board.place_ships()

    for ship in board.ships:
        print(ship)
