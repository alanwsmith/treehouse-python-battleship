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
        self.test_see_if_ship_was_hit()
        self.test_is_ship_sunk()


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


    def test_see_if_ship_was_hit(self):
        logging.info("-- See If Ship Was Hit Test --")
        ship = Ship(name = "Test Ship", size = 3)
        ship.set_coordinates([(3, 1), (3, 2), (3, 3)])
        miss_coordinates = (5, 6)
        hit_coordinates = (3, 2)

        self.assert_equal(False, ship.see_if_ship_was_hit(miss_coordinates))
        self.assert_equal(True , ship.see_if_ship_was_hit(hit_coordinates))
        self.assert_equal(hit_coordinates, ship.hits[0])


    def test_is_ship_sunk(self):
        logging.info("-- See If Ship Was Hit Test --")
        ship = Ship(name = "Test Ship", size = 3)
        
        # Should be false before coordinates are set
        self.assert_equal(False, ship.is_sunk())

        # Should be false if coordinates are set but not all are hit
        ship.set_coordinates([(3, 1), (3, 2), (3, 3)])
        ship.see_if_ship_was_hit((3,2))
        ship.see_if_ship_was_hit((3,3))
        self.assert_equal(False, ship.is_sunk())

        # Should be true if all coordinates are hit.
        ship.see_if_ship_was_hit((3,1))
        self.assert_equal(True, ship.is_sunk())


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

