import logging

class Ship():
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.size = kwargs.get('size')
        self.orientation = None
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


