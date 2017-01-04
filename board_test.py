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
        self.test_get_row_string()
        self.test_get_row_string_with_ship_data()
        self.test_set_grid_visibility()
        self.test_place_shot()
        self.test_last_shot_status()
        self.test_last_shot_status_hit()

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

    def test_grid_with_ships_horizontal(self):
        logging.info("-- Grid with Ships Horizontal Test --")
        board = Board(index = 0)
        board.ships[0].set_orientation('h')
        board.ships[0].set_coordinates([(1,3), (1,4), (1,5), (1,6), (1,7)])
        self.assert_equal('O', board.grid()[0][0])
        self.assert_equal('-', board.grid()[1][3])

    def test_get_row_string(self):
        logging.info("-- Get Row String Test --")
        board = Board(index = 0)
        self.assert_equal(True, board.grid_visibility)
        self.assert_equal('O O O O O O O O O O', board.get_row_string(0))
        board.set_grid_visibility(False)
        self.assert_equal('? ? ? ? ? ? ? ? ? ?', board.get_row_string(0))

    def test_get_row_string_with_ship_data(self):
        logging.info("-- Get Row String With Ship Data Test --")
        # Given
        board = Board(index = 0)
        board.ships[0].set_orientation('h')
        board.ships[0].set_coordinates([(1,3), (1,4), (1,5), (1,6), (1,7)])
        board.ships[1].set_orientation('v')
        board.ships[1].set_coordinates([(3, 1), (4, 1), (5, 1), (6, 1)])
        board.shot_history = [(1, 2), (1, 3)]
        # When/Then
        self.assert_equal(True, board.grid_visibility)
        self.assert_equal('O O . * - - - - O O', board.get_row_string(1))
        self.assert_equal('O | O O O O O O O O', board.get_row_string(3))
        # When/Then
        board.set_grid_visibility(False)
        self.assert_equal('? ? . * ? ? ? ? ? ?', board.get_row_string(1))
        self.assert_equal('? ? ? ? ? ? ? ? ? ?', board.get_row_string(3))


    def test_set_grid_visibility(self):
        logging.info("-- Set Grid Visability Test --")
        board = Board(index = 0)
        self.assert_equal(True, board.grid_visibility)
        board.set_grid_visibility(False)


    def test_place_shot(self):
        logging.info("-- Place Shot Test --")
        board = Board(index = 0)
        # Send display and check for raw
        self.assert_equal(True, board.place_shot('c5'))
        self.assert_equal((4, 2), board.shot_history[-1])

        # Add another valid shot
        self.assert_equal(True, board.place_shot('d1'))
        self.assert_equal((0, 3), board.shot_history[-1])

        # Verify duplicate shots are rejected. 
        self.assert_equal(False, board.place_shot('d1'))


    def test_last_shot_status(self):
        logging.info("-- Last Shot Status Test --")
        board = Board(index = 0)
        board.ships[0].set_orientation('h')
        board.ships[0].set_coordinates([(1,3), (1,4), (1,5), (1,6), (1,7)])
        board.place_shot('c9')
        board.place_shot('e9')
        board.place_shot('b1')
        target_coordinates = (0, 1)
        self.assert_equal(target_coordinates, board.last_shot())
        self.assert_equal('shot_missed', board.last_shot_status())

    def test_last_shot_status_hit(self):
        logging.info("-- Last Shot Status Hit Test --")
        board = Board(index = 0)
        board.ships[0].set_orientation('h')
        board.ships[0].set_coordinates([(1,3), (1,4), (1,5), (1,6), (1,7)])
        board.place_shot('c9')
        board.place_shot('e9')
        board.place_shot('d2')
        target_coordinates = (1, 3)
        self.assert_equal('shot_hit', board.last_shot_status())


        # Make
        # - shot_missed
        # - shot_hit
        # - shot_sunk
        # - shot_won_game
        




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
