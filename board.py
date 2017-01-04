import constants
import logging

from ship import Ship

class Board():
    
    def __init__(self, **kwargs):
        self.index = kwargs['index']
        self.player_name = "Player {}".format(self.index + 1)
        self.grid_visibility = True
        self.ships = [] 
        self.shot_history = []
        self.load_ships()
        logging.info("Created board {}".format(self.index))

    def grid(self):
        grid = []
        for row_index in range(0, constants.BOARD_SIZE):
            row = []
            for column_index in range(0, constants.BOARD_SIZE):
                row.append(self.get_grid_key(row_index, column_index))
            grid.append(row)
        return grid 

    def grid_hidden(self):
        grid = self.grid()
        for row_index in range(0, len(grid)):
            for column_index in range(0, len(grid[row_index])):
                if grid[row_index][column_index] == "O":
                    grid[row_index][column_index] = '?'
                elif grid[row_index][column_index] == "-":
                    grid[row_index][column_index] = '?'
                elif grid[row_index][column_index] == "|":
                    grid[row_index][column_index] = '?'

        return grid

    def get_grid_key(self, row_index, column_index):
        for ship in self.ships:
            for coordinate in ship.coordinates:
                if (row_index, column_index) == coordinate:
                    if ship.orientation == 'v':
                        return '|'
                    else:
                        return '-'
        return 'O'


    def get_row_string(self, row_index):
        if self.grid_visibility:
            return " ".join(self.grid()[row_index])
        else:
            return " ".join(self.grid_hidden()[row_index])

    def last_shot(self):
        return self.shot_history[-1]

    def last_shot_status(self):
        return 'shot_missed'

    def load_ships(self):
        for ship_index in range(0, constants.SHIP_COUNT):
            ship = constants.SHIP_INFO[ship_index]
            self.ships.append(Ship(name = ship[0], size = ship[1]))


    def place_shot(self, coordinates):
        # Expects a validated set of display coordiantes. 
        # Adds the raw shot coordinates to shot_history and returns true if it's not
        # already there. Otherwise, returns false.
        column = constants.COORDINATE_MAP['columns'][coordinates[0]]
        row = constants.COORDINATE_MAP['rows'][int(coordinates[1:])]
        raw_coordinates = (row, column)
        if raw_coordinates in self.shot_history:
            logging.info("Rejected shot at {} in board {} because it's already in shot_history".format(
                         raw_coordinates,
                         self.index
                         ))
            return False
        else:
            self.shot_history.append(raw_coordinates)
            logging.info("Added shot at {} to board {}.".format(raw_coordinates, self.index))
            return True 


    def set_grid_visibility(self, mode):
        self.grid_visibility = mode


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


    def verify_coordinates_are_clear(self, coordinate_list):
        for ship in self.ships:
            for coordinate in coordinate_list:
                if coordinate in ship.coordinates:
                    return False

        return True
        

if __name__ == '__main__':

    # Run the tests if your run this file directly
    import board_test
    bt = board_test.BoardTest()
    bt.run_tests()
    print("All tests passed.")



    #board = Board(index = 0)
    #board.show()

    #for ship in board.ships:
    #    print(ship)
