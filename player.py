import logging

class Player():
    
    def __init__(self, id):
        logging.debug('Creating player with id: {}'.format(id))
        self.id = id
        self.name = 'Player {}'.format(id)

    def ask_for_name(self):
        self.name = input("What's the name of player {}? ".format(self.id))



