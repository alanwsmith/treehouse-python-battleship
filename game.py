import logging

class Game():
    
    def __init__(self):
        logging.info("Initializing game")


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s]:  %(message)s', level=logging.INFO)
    game = Game()

        
