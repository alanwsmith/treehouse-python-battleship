import logging

from ship import Ship

class Player():

    def __init__(self, **kwargs):
        logging.debug("Initialiing Player")
        self.id = kwargs.get('id')
        self.name = 'Player {}'.format(self.id)
        self.ships = []
        logging.debug("  ID: {}".format(self.id))

        for ship in kwargs.get('ship_info'):
            self.ships.append(Ship(name = ship[0], size = ship[1]))
            

    def ask_for_name(self):
        self.name = input("What's the name of player {}? ".format(self.id))

    def board(self):
        output_board = []
        for col in range(10):
            row = []
            for num in range(10):
                row.append('O')
            output_board.append(row)

        return output_board 

