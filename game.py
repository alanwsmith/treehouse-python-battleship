import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(), Board() ]

    def display_board(self, board):
        board.show()
        pass






if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s]:  %(message)s', level=logging.INFO)
    game = Game()
    game.display_board(game.boards[0])

        
