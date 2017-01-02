import logging


class BoardTest():
    
    def __init__(self):
        pass
    
    def run_tests(self):
        pass


if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game_test.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    bt = BoardTest()
    bt.run_tests()
