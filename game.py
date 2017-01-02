import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(index = 0), Board(index = 1) ]
        self.banners = {
            "error_name_is_empty": "Oops! The player's name can't be empty. Try again.",
            "error_name_is_too_long": "Oops! The game can't handle names longer than 18 characters. Try again.",
            "name_set": "",
            "none": "",
            "welcome": "Welcome to Battleship!",
        }
        self.prompts = {
            "player_1": "What's the name of the first player?",
            "player_2": "What's the name of the second player?",
        }

        self.banner = 'welcome'
        self.prompt = "player_1"

        self.testing_input = []

    def get_input(self):
        if len(self.testing_input) > 0:
            return self.testing_input.pop(0)
        else:
            return input("> ")

    def header_letters(self):
        return "   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)])

    def arena_padding(self):
        return "      "

    def display_arena(self):
        print("\033c", end="")
        print(
            " {} ".format(self.boards[0].player_name).center(22, '-') +
            self.arena_padding() +
            " {} ".format(self.boards[1].player_name).center(22, '-')
        )

        print(self.header_letters() + self.arena_padding() + self.header_letters())
        for row_index in range(0, constants.BOARD_SIZE):
            print(
                str(row_index + 1).rjust(2) + " " + " ".join(self.boards[0].grid()[0]) +
                self.arena_padding() +
                str(row_index + 1).rjust(2) + " " + " ".join(self.boards[1].grid()[0])
            )

        print('\n{}\n'.format(self.banners[self.banner]))
        print(self.prompts[self.prompt])

    def place_ships_on_board(self, board):
        logging.info("Placing ships for board {}".format(board.index))
        for ship in board.ships:
            print(ship)

    def set_player_names(self):
        while self.banner != 'name_set':
            self.display_arena()
            self.banner = self.boards[0].set_player_name(self.get_input())
        self.banner = "none"
        self.prompt = "player_2"
        while self.banner != 'name_set':
            self.display_arena()
            self.banner = self.boards[1].set_player_name(self.get_input())



if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    game = Game()
    game.set_player_names()
    game.display_arena()

