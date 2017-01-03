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

    def set_player_name(self, name):
        stripped_name = name.strip()
        if len(stripped_name) == 0:
            logging.info("Invalid empty player name")
            return 'error_name_is_empty'
        elif len(stripped_name) > 18:
            logging.info("Player name is too long")
            return 'error_name_is_too_long'
        else:
            logging.info("Set board {} player_name to {}".format(self.index, name)) 
            self.player_name = stripped_name
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

    for ship in board.ships:
        print(ship)
