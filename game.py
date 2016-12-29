import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(index = 0), Board(index = 1) ]
        self.flash_message = "Welcome to Battleship"

    def header_letters(self):
        return "   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)])

    def arena_padding(self):
        return "      "

    def display_arena(self):
        print("\033c", end="")
        print(
            " {} ".format(self.boards[0].player_name).center(22, '-')
            +
            self.arena_padding()
            +
            " {} ".format(self.boards[1].player_name).center(22, '-')
        )

        print(self.header_letters() + self.arena_padding() + self.header_letters())
        for row_index in range(0, constants.BOARD_SIZE):
            print(
                str(row_index + 1).rjust(2) + " " + " ".join(self.boards[0].grid()[0])
                +
                self.arena_padding()
                +
                str(row_index + 1).rjust(2) + " " + " ".join(self.boards[1].grid()[0])
            )
            
        if self.flash_message != "":
            print('\n{}\n'.format(self.flash_message))
            self.flash_message = ""
        else:
            print('\n\n')

    def get_player_names(self):
        print("Enter name for Player 1")
        response = input("> ")
        self.boards[0].player_name = response
        game.display_arena()
        print("Enter name for Player 2")
        response = input("> ")
        self.boards[1].player_name = response
        game.display_arena()

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
    game.display_arena()
    game.get_player_names()

    # game.place_ships_on_board(game.boards[0])

        
