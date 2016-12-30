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
        self.test_2()

    def test_basic_initialization(self):
        logging.info("-- Basic Initialization Test --")
        game = Game()
        self.assert_equal(game.boards[0].player_name, "Player 1")
        self.assert_equal(game.boards[1].player_name, "Player 2")
        self.assert_equal(game.message_key, "welcome")

    def test_2(self):
        logging.info("-- Test 2 - Started --")
        game = Game()
        game.display_arena()
        game.get_player_name_for_board(board_index=0, test_value="Bob")
        self.assert_equal(game.boards[0].player_name, "Bob")

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    gt = GameTest()
    gt.run_tests()
