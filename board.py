import constants
import logging

from ship import Ship

class Board():
    
    def __init__(self):
        logging.debug("Creating new board")
        self.ships = [] 
        self.load_ships()

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

    def place_ships(self):
        valid_orientations = ["v", "h"]

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


            # Get the bow coordinates

            # while True:
            #     column = input("Which column (A-{})? ".format(constants.LAST_COLUMN)).lower()
            #     if column in constants.COORDINATE_MAP['cols']:
            #         while True:
            #             row = input("Which row (1-{})? ".format(constants.LAST_ROW)) 
            #             try:
            #                 row = int(row)
            #             except ValueError:
            #                 print("Oops! The row must be a number. Try again.")
            #                 continue
            #             else:
            #                 if row in constants.COORDINATE_MAP['rows']:
            #                     self.bow = (
            #                         constants.COORDINATE_MAP['rows'][row],
            #                         constants.COORDINATE_MAP['cols'][column]
            #                     )

            #                     break
            #                 else:
            #                     print("Oops! {} is outside the grid. Give it another shot.".format(row))
            #                     continue
            #         break
            #     else:
            #         print("Oops! That wasn't a valid row. Try one more time")
            #         continue
            #     break

                

    def show(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)]))
        for row in range(0,10):
            print(str(row + 1).rjust(2), end='')
            for col in range(0, 10):
                print(" O", end='')
            print('')


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s]:  %(message)s', level=logging.INFO)
    board = Board()
    board.show()
    board.place_ships()

    for ship in board.ships:
        print(ship)
