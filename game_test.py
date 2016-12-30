import logging

from game import Game

class GameTest():
    def __init__(self):
        logging.info("Initialized GameTest()")

    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))

    def run_tests(self):
        logging.info("Running tests.")
        self.test_basic_initialization()
        self.test_get_player_name_for_board()

    def test_basic_initialization(self):
        logging.info("-- Basic Initialization Test --")
        game = Game()
        game.activate_testing()
        self.assert_equal(game.boards[0].player_name, "Player 1")
        self.assert_equal(game.boards[1].player_name, "Player 2")
        self.assert_equal(game.banner, "welcome")
        self.assert_equal(game.prompt, "player_1")

    def test_get_player_name_for_board(self):
        logging.info("-- Set Player Name Test --")
        game = Game()
        game.activate_testing()
        game.display_arena()
        game.get_player_name_for_board(board=0)


        #self.assert_equal(game.boards[0].player_name, "Bob")

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    gt = GameTest()
    gt.run_tests()
