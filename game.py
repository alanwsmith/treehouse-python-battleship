import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(), Board() ]

    def display_board(self, board):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)]))
        row_num = 1
        for row in board.grid():
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/test-run--board.txt', 
        filemode='w', 
        format='[%(levelname)s]:  %(message)s', 
        level=logging.INFO
    )
    game = Game()
    game.display_board(game.boards[0])

        
