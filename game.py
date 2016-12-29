import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(index = 0), Board(index = 1) ]
        self.flash_message = "Welcome to Battleship"

    def display_arena(self, **kwargs):
        self.display_board(self.boards[kwargs['top_board']])
        print('')
        if kwargs['top_board'] == 0:
            self.display_board(self.boards[1])
        else:
            self.display_board(self.boards[0])

        # The flash_message only appears once and is then
        # removed. If there is no flash_message, empty
        # lines are output to maintain the spacing. 
        if self.flash_message != "":
            print('\n{}\n'.format(self.flash_message))
            self.flash_message = ""
        else:
            print('\n\n')


    def display_board(self, board):
        print(" {} ".format(board.player_name).center(22, '-'))
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)]))
        row_num = 1
        for row in board.grid():
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def place_ships_on_board(self, board):
        logging.info("Placing ships for board {}".format(board.index))
        for ship in board.ships:
            print(ship)

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/test-run--board.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )
    game = Game()
    game.display_arena(top_board = 1)
    # game.place_ships_on_board(game.boards[0])

        
