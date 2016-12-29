import constants
import logging

from ship import Ship

class Board():
    
    def __init__(self):
        logging.debug("Creating new board")
        self.ships = [] 
        self.load_ships()

        pass

    def load_ships(self):
        for ship in constants.SHIP_INFO:
            self.ships.append(Ship(name = ship[0], size = ship[1]))

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

    for ship in board.ships:
        print(ship)
