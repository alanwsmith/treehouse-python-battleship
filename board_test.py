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
        self.test_grid_with_ships_vertical()
        self.test_grid_with_ships_horizontal()

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

    def test_grid_with_ships_vertical(self):
        logging.info("-- Grid with Ships Test --")
        board = Board(index = 0)
        board.ships[0].set_orientation('v')
        board.ships[0].set_coordinates([(1,3), (2,3), (3,3), (4,3), (5,3)])
        self.assert_equal('O', board.grid()[0][0])
        self.assert_equal('|', board.grid()[1][3])

        for row_index in range(0, len(board.grid())):
            print(board.grid()[row_index])

    def test_grid_with_ships_horizontal(self):
        logging.info("-- Grid with Ships Horizontal Test --")
        board = Board(index = 0)
        board.ships[0].set_orientation('h')
        board.ships[0].set_coordinates([(1,3), (1,4), (1,5), (1,6), (1,7)])
        self.assert_equal('O', board.grid()[0][0])
        self.assert_equal('-', board.grid()[1][3])

        for row_index in range(0, len(board.grid())):
            print(board.grid()[row_index])


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
