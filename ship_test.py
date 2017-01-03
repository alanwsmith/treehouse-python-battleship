import logging

from ship import Ship


class ShipTest():

    def __init__(self):
        pass

    def assert_equal(self, a, b):
        if a != b:
            raise ValueError("Expected: {} - Got: {}".format(a, b))

    def run_tests(self):
        self.test_set_orientation()
        self.test_set_coordinates()

    def test_set_orientation(self):
        logging.info("-- Set Orientation Test --")
        ship = Ship( name = "Test Ship", size = 3)
        self.assert_equal(True, ship.set_orientation('v'))
        self.assert_equal(True, ship.set_orientation('h'))
        self.assert_equal(False, ship.set_orientation('X'))

    def test_set_coordinates(self):
        logging.info("-- Set Coordinates Test --")
        ship = Ship( name = "Test Ship", size = 3)
        self.assert_equal(True, ship.set_coordinates([(3, 1), (3, 2), (3, 3)]))
        self.assert_equal((3, 2), ship.coordinates[1])



if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/ship_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    st = ShipTest()
    st.run_tests()
    
    print("All tests passed!")

