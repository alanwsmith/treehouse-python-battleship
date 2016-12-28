import logging

class Player():
    
    def __init__(self, id):
        logging.debug('Creating player with id: {}'.format(id))
        self.id = id
        self.name = 'Player {}'.format(id)

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
            

