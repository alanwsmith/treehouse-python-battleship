import logging

class Ship():
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.size = kwargs.get('size')
        logging.debug("Initializing {} - size: {}".format(self.name, self.size)) 

    def __str__(self):
        return "Ship type: {} - size: {}".format(self.name, self.size)



