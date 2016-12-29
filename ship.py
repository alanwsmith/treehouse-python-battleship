import constants
import logging

class Ship():
    
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.size = kwargs['size']
        self.orientation = None
        self.bow = None

        logging.debug("Initializing {} - size: {}".format(self.name, self.size)) 

    def __str__(self):
        return "Ship: {} - size: {} - orientation: {} - bow: {}".format(
            self.name, 
            self.size,
            self.orientation,
            self.bow
        )

    def set_bow(self, coordinate):
        logging.debug(coordinate)
        self.bow = coordinate

    def set_orientation(self, orientation):
        self.orientation = orientation


    def place(self):

        valid_orientations = ["v", "h"]
        
        # Figure out the orientation
        while True:
            response = input("[v]ertically or [h]orizontally? ").lower()
            if response in valid_orientations:
                self.orientation = response
                break
            else:
                print("Oops! You must enter either 'v' for vertical or 'h' for horizontal. Try again.")
                continue

        last_letter = constants.LETTERS[constants.BOARD_MAX_INDEX].upper()
        last_number = constants.BOARD_SIZE 

        # while True:
        #     target_column = input("Which column (A-{})? ".format(last_letter)).lower()
        #     if target_column not in constants.COORDINATE_MAP['cols']:
        #         print("Oops! That wasn't a valid row. Try one more time")
        #         continue
        #     else:
        #         while True:
        #             target_row = input("Which row (1-{})? ".format(last_number)) 
        #             try:
        #                 target_row = int(target_row)
        #             except ValueError:
        #                 print("Oops! The row must be a number. Give it another shot.")
        #                 continue
        #             if target_row not in constants.COORDINATE_MAP['rows']:
        #                 print("Oops! '{}' is not a valid row. Give it another shot.".format(target_row))
        #                 continue
        #             else:
        #                 return(target_column, target_row)

        # pass


if __name__ == '__main__':
    ship = Ship(name = "Test Ship", size = 5)
    ship.place()
    print(ship)


