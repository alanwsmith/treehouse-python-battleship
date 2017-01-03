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
        return "{}\n- size: {}\n- orientation: {} \n- bow_column: {}\n- bow_row: {}".format(
            self.name, 
            self.size,
            self.orientation,
            self.bow_column,
            self.bow_row
        )

    def set_bow(self, coordinate):
        logging.debug(coordinate)
        self.bow = coordinate

    def set_orientation(self, orientation):
        self.orientation = orientation


if __name__ == '__main__':
    ship = Ship(name = "Test Ship", size = 5)
    ship.place()
    print(ship)


