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
        self.test_validate_orientation()
        self.test_validate_ship_stays_on_grid()

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

    def test_validate_coordinates(self):
        logging.info("-- Validate Coordinates (2) Test --")
        game = Game()
        self.assert_equal(True, game.validate_coordinates("a1"))
        self.assert_equal(True, game.validate_coordinates("A1"))
        self.assert_equal(True, game.validate_coordinates(" D10 "))

        self.assert_equal(False, game.validate_coordinates(""))
        self.assert_equal(False, game.validate_coordinates("aa"))
        self.assert_equal(False, game.validate_coordinates("a"))
        self.assert_equal(False, game.validate_coordinates("q1"))
        self.assert_equal(False, game.validate_coordinates("11"))
        self.assert_equal(False, game.validate_coordinates("a30"))


    def test_validate_orientation(self):
        logging.info("-- Validate Orientation Test --")
        game = Game()
        self.assert_equal(True, game.validate_orientation("h"))
        self.assert_equal(False, game.validate_orientation("q"))
        # TODO: Test upper case and with spaces. 


    def test_validate_ship_stays_on_grid(self):
        logging.info("-- Validate Ship Stays On Grid Test --")
        game = Game()
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="a1", orientation="v", size=5))
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="a1", orientation="h", size=5))
        self.assert_equal(False, game.validate_ship_stays_on_grid(front_of_ship="a9", orientation="v", size=5))
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="a9", orientation="h", size=5))
        self.assert_equal(False, game.validate_ship_stays_on_grid(front_of_ship="i1", orientation="h", size=5))
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="i1", orientation="v", size=5))



if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    gt = GameTest()
    gt.run_tests()
    print("All tests passed!")

