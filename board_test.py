import logging

from board import Board


class BoardTest():
    
    def __init__(self):
        pass

    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))
    
    def run_tests(self):
        self.test_set_player_name()
        self.test_strip_spaces_on_name()

    def test_set_player_name(self):
        logging.info("-- Set Player Name Test --")
        board = Board(index = 1)
        self.assert_equal('error_name_is_empty', board.set_player_name("")) 
        self.assert_equal('error_name_is_too_long', board.set_player_name("asdfghjkloiuytrewqe"))
        self.assert_equal('name_set', board.set_player_name("Bob"))
    
    def test_strip_spaces_on_name(self):
        logging.info("-- Strip Spaces On Name Test --")
        board = Board(index = 1)
        board.set_player_name("  Alice  ")
        self.assert_equal('Alice', board.player_name)
        


if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/board_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    bt = BoardTest()
    bt.run_tests()
