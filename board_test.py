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
        self.test_set_ship_coordinates()
        self.test_set_ship_coordinates_with_conflict()
        self.test_grid_with_ships()

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

    def test_set_ship_coordinates(self):
        logging.info("-- Set Ship Coordiantes Test --")
        board = Board(index = 0)
        coordinate_list = [(1, 2), (1, 3), (1, 4)]
        self.assert_equal(True, board.verify_coordinates_are_clear(coordinate_list))

    def test_set_ship_coordinates_with_conflict(self):
        logging.info("-- Set Ship Coordiantes Test --")
        board = Board(index = 0)
        board.ships[0].coordinates = [ (1, 3), (1, 4), (1, 5)]
        coordinate_list = [(1, 2), (1, 3), (1, 4)]
        self.assert_equal(False, board.verify_coordinates_are_clear(coordinate_list))

    def test_grid_with_ships(self):
        logging.info("-- Grid with Ships Test --")
        board = Board(index = 0)
        ship = board.ships[0]
        ship.set_orientation('v')
        ship.set_coordinates([(1,3), (1,4), (1,5)])

        print(board.grid())

        self.assert_equal('O', board.grid()[0][0])
#        self.assert_equal('|', board.grid()[1][3])




if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/board_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    bt = BoardTest()
    bt.run_tests()

    print("All tests passed!")
