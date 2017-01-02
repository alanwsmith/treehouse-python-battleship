import constants
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
        self.test_get_testing_input()
        self.test_validate_coordinates()

    def test_basic_initialization(self):
        logging.info("-- Basic Initialization Test --")
        game = Game()
        self.assert_equal(game.boards[0].player_name, "Player 1")
        self.assert_equal(game.boards[1].player_name, "Player 2")
        self.assert_equal(game.banner, "welcome")
        self.assert_equal(game.prompt, "player_0")

    def test_get_testing_input(self):
        logging.info("-- Get Testing Input Test --")
        game = Game()
        game.testing_input.append("The quick brown fox.")
        self.assert_equal(game.get_input(), "The quick brown fox.")

    def test_validate_coordinates(self, **kwargs):
        logging.info("-- Get Valid Coordinates Test --")
        game = Game()
        self.assert_equal(False, game.validate_coordinates(coordinates = ""))
        self.assert_equal(False, game.validate_coordinates(coordinates = "aa"))
        self.assert_equal(False, game.validate_coordinates(coordinates = "q1"))
        self.assert_equal(False, game.validate_coordinates(coordinates = "a30"))
        self.assert_equal(True, game.validate_coordinates(coordinates = "a1"))




if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    gt = GameTest()
    gt.run_tests()
