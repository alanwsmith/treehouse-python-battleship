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
        self.test_get_ship_coordinates_horizontal()
        self.test_get_ship_coordinates_vertical()
        self.test_raw_coordinates_to_display()
        self.test_get_orientation()


    def test_basic_initialization(self):
        logging.info("-- Basic Initialization Test --")
        game = Game()

        self.assert_equal(game.boards[0].player_name, "Player 1")
        self.assert_equal(game.boards[1].player_name, "Player 2")
        self.assert_equal(game.banner, "welcome")
        self.assert_equal(game.prompt, "player_0")

    def test_get_orientation(self):
        """The get_orientaiton method currently calls
        display_arena(). That should be refactored out in
        a future iteration, but for now, that causes a 
        visual output during this test. The 'print'
        call at the end is to clear the screen.
        """
        
        logging.info("-- Get Orientation Test --")
        game = Game()

        game.testing_input = ['v']
        self.assert_equal('v', game.get_orientation())
        game.testing_input = ['  V']
        self.assert_equal('v', game.get_orientation())
        print("\033c", end="")


    def test_get_ship_coordinates_horizontal(self):
        logging.info("-- Get Ship Coordinates Test --")
        game = Game()
        target_list = [ (1, 1), (1, 2), (1, 3), (1, 4), (1, 5) ]
        test_list = game.get_ship_coordinates(front_of_ship = "b2", size = 5, orientation = "h")

        self.assert_equal(len(test_list), len(target_list))

        for item_index in range(0, len(target_list)):
            self.assert_equal(target_list[item_index], test_list[item_index])


    def test_get_ship_coordinates_vertical(self):
        logging.info("-- Get Ship Coordinates Test --")
        game = Game()
        target_list = [ (4, 3), (5, 3), (6, 3), (7, 3), (8, 3) ]
        test_list = game.get_ship_coordinates(front_of_ship = "d5", size = 5, orientation = "v")
    
        self.assert_equal(len(test_list), len(target_list))
        
        for item_index in range(0, len(target_list)):
            self.assert_equal(target_list[item_index], test_list[item_index])


    def test_get_testing_input(self):
        logging.info("-- Get Testing Input Test --")
        game = Game()
        game.testing_input.append("The quick brown fox.")

        self.assert_equal(game.get_input(), "The quick brown fox.")


    def test_raw_coordinates_to_display(self):
        logging.info("-- Raw Coordinates To Display Test --")
        game = Game()

        self.assert_equal('c4', game.raw_coordinates_to_display((3, 2)))
    

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
        self.assert_equal(True, game.validate_orientation("v"))
        self.assert_equal(False, game.validate_orientation("q"))


    def test_validate_ship_stays_on_grid(self):
        logging.info("-- Validate Ship Stays On Grid Test --")
        game = Game()

        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="a1", orientation="v", size=5))
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="a1", orientation="h", size=5))
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="a9", orientation="h", size=5))
        self.assert_equal(True, game.validate_ship_stays_on_grid(front_of_ship="i1", orientation="v", size=5))
        self.assert_equal(False, game.validate_ship_stays_on_grid(front_of_ship="i1", orientation="h", size=5))
        self.assert_equal(False, game.validate_ship_stays_on_grid(front_of_ship="a9", orientation="v", size=5))



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

