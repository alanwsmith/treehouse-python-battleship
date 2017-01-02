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
            "welcome": "Welcome to Battleship!",
        }
        self.prompts = {
            "player_1": "What's the name of the first player?"
        }

        self.banner = 'welcome'
        self.prompt = "player_1"

        self.testing_input = []

    def get_input(self):
        if self.testing_input:
            if len(self.testing_input) > 0:
                return self.testing_input.pop(0)
            else:
                return input("> ")
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

    def get_player_names(self):
        for board_index in range(0,2):
            while True:
                print("Enter name for Player {}".format(board_index + 1))
                response = input("> ").strip()
                if len(response) == 0:
                    self.display_arena(error="You didn't enter a name. Try again.")
                    continue
                elif len(response) > 18:
                    self.display_arena(error="That name is to long for the game. Try one less than 18 letters.")
                elif self.boards[0].player_name == response:
                    self.display_arena(error="Players can't have the same name. Try again.")
                    continue
                else:
                    self.boards[board_index].player_name = response
                    self.display_arena()
                    break

    def place_ships_on_board(self, board):
        logging.info("Placing ships for board {}".format(board.index))
        for ship in board.ships:
            print(ship)

    def get_player_name_for_board(self, **kwargs):
        
        self.boards[0].player_name = "Bob"
        pass

    def set_player_names(self):
        while self.banner != 'name_set':
            self.banner = self.boards[0].set_player_name(self.get_input())
            self.display_arena()
        pass 


if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    game = Game()
    game.display_arena()
    game.set_player_names()
    game.display_arena()

