import constants
import logging

from game import Game


class Battleship():

    def run(self):
        constants.SHIP_COUNT = 5
        game = Game()
        game.set_player_names()
        game.place_ships()
        game.start_shooting()


if __name__ == '__main__':
    """This is where the game gets
    kicked off.
    """
    logging.basicConfig(filename='logs/game.txt', filemode='w',
                        format='[%(levelname).1s]: %(message)s',
                        level=logging.INFO)
    battleship = Battleship()
    battleship.run()
