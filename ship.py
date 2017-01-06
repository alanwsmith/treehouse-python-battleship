import logging


class Ship():

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.size = kwargs['size']
        self.orientation = None
        self.coordinates = []
        self.hits = []

        logging.debug(
            "Initializing {} - size: {}".format(self.name, self.size))

    def is_sunk(self):
        """Identify if the ship is sunk by comparing the
        number of hits to the size of the ship.
        """

        if len(self.hits) == self.size:
            return True
        else:
            return False

    def set_bow(self, coordinate):
        logging.debug(coordinate)
        self.bow = coordinate

    def set_coordinates(self, coordinates):
        # This is just to set via a method. It assumes
        # a valid list is passed that has already been
        # checked to make sure it doesn't conflict with
        # other ships.
        self.coordinates = coordinates
        return True

    def set_orientation(self, orientation):
        """This method just sets the orientation
        for the ship. It does a sanity check
        to make sure the value is either a 'v'
        or an 'h' first. (The value should already
        have been validated, but this felt like
        a natural place to enfore it as well.

        A potential refactore is to remove the redundante
        checks in other classess/objects and do all
        the validation here.
        """

        if orientation == 'v' or orientation == 'h':
            self.orientation = orientation
            return True
        else:
            return False

    def see_if_ship_was_hit(self, coordinate):
        """Check to see if a set of coordinates is a hit
        on the ship. If it is, add it to the list of
        hits.

        Since the other methods should prevent the same
        shot from being duplicated there is no
        check here to avoid duplication.

        The reason to keep up directly with the hits it
        to know when the ship is sunk.
        """

        if coordinate in self.coordinates:
            self.hits.append(coordinate)
            return True
        else:
            return False


if __name__ == '__main__':
    import ship_test
    st = ship_test.ShipTest()
    st.run_tests()
    print("All tests passed!")
