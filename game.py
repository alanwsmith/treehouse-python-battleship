import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.message_key = 'welcome'
        self.boards = [ Board(index = 0), Board(index = 1) ]

    def header_letters(self):
        return "   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)])

    def arena_padding(self):
        return "      "

    def display_arena(self, **kwargs):
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
        
        if kwargs.get('flash'):
            print('\n{}\n'.format(kwargs.get('flash')))
        elif kwargs.get('error'):
            print('\nOops! {}\n'.format(kwargs.get('error')))
        else:
            print('\n\n')

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

    def get_player_name_for_board_index(self, **kwargs):
        

        self.boards[0].player_name = "Bob"
        pass


# Try abstracting the input by setting a method that always get's called for the 
# response that you can override with the test calls. That will
# keep from having to setup test code inside all the methods.


class GameTest():
    def __init__(self):
        logging.info("Initialized GameTest()")

    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))

    def run_tests(self):
        logging.info("Running tests.")
        self.test_1()
        self.test_2()

    def test_1(self):
        logging.info("-- Test 1 - Started --")
        game = Game()
        self.assert_equal(game.boards[0].player_name, "Player 1")
        self.assert_equal(game.boards[1].player_name, "Player 2")
        self.assert_equal(game.message_key, "welcome")
        logging.info("-- Test 1 - Finished --")

    def test_2(self):
        logging.info("-- Test 2 - Started --")
        game = Game()
        game.display_arena(flash="Welcome to Battleship!")
        game.get_player_name_for_board_index(board_index=0, test_value="Bob")
        self.assert_equal(game.boards[0].player_name, "Bob")
        logging.info("-- Test 2 - Finished --")
        

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/test-run--board.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    gt = GameTest()
    gt.run_tests()

    
    

    game = Game()
    game.display_arena(flash="Welcome to Battleship!")
    game.get_player_name_for_board_index(board_index=0)
#    game.get_player_names()

    # game.place_ships_on_board(game.boards[0])

        
