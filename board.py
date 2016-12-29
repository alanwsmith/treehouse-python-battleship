import constants
import logging


class Board():
    
    def __init__(self):
        logging.debug("Creating new board")
        pass


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s]:  %(message)s', level=logging.DEBUG)
    board = Board()

