import constants
import logging

class Ship():
    
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.size = kwargs['size']
        self.orientation = None
        self.bow = None

        self.bow_column = None
        self.bow_row = None

        self.coordinates = []

        logging.debug("Initializing {} - size: {}".format(self.name, self.size)) 

    def __str__(self):
        return "{}\n- size: {}\n- orientation: {} \n- bow_column: {}\n- bow_row: {}\n- coordinates: {}".format(
            self.name, 
            self.size,
            self.orientation,
            self.bow_column,
            self.bow_row,
            self.coordinates,
        )

    def set_bow(self, coordinate):
        logging.debug(coordinate)
        self.bow = coordinate

    def set_coordinates(self, coordinates):
        # This is just to set via a method. It assumes
        # a valid list is passed that has already been
        # checked to make sure it doesn't conflict with 
        # other ships.
        self.coordinates = coordinates
        return True

    def set_orientation(self, orientation):
        if orientation == 'v' or orientation == 'h':
            self.orientation = orientation
            return True
        else:
            return False


if __name__ == '__main__':
    ship = Ship(name = "Test Ship", size = 5)
    print(ship)


