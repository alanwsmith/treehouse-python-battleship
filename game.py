import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(index = 0), Board(index = 1) ]
        self.banners = {
            "error_duplicate_names_not_allowed": "Oops! The players can't have the same name. Try again.",
            "error_name_is_empty": "Oops! The player's name can't be empty. Try again.",
            "error_name_is_too_long": "Oops! The game can't handle names longer than 18 characters. Try again.",
            "invalid_coordinates": "Oops! {}, those were invalid coordinates. Try again.",
            "invalid_orientation": "Oops! The orientation must be either 'v' or 'h'. Try again, {}.",
            "name_set": "",
            "none": "",
            "place_ships": "{}, place your ships.",
            "welcome": "Welcome to Battleship!",
        }
        self.prompts = {
            "player_0": "What's the name of the first player?",
            "player_1": "What's the name of the second player?",
            "ship_orientation": "Do you want to place your {} (size {}) [v]ertically or [h]orizontally?", 
            "front_of_ship_coords": "Where do you want the front of your {} (size {})?",
        }

        # Place holder for items to pass to format for the banner and prompt
        self.banner_params = () 
        self.prompt_params = ()

        self.banner = 'welcome'
        self.prompt = "player_0"

        self.testing_input = []

    def get_input(self):
        if len(self.testing_input) > 0:
            return self.testing_input.pop(0)
        else:
            return input("> ")

    def header_letters(self):
        return "   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)])

    def arena_padding(self):
        return "      "

    def display_arena(self):
        print("\033c", end="")
        print("{}{}{}".format(
            self.boards[0].player_name.center(22, '-'),
            self.arena_padding(),
            self.boards[1].player_name.center(22, '-')
        ))

        print(self.header_letters() + self.arena_padding() + self.header_letters())
        for row_index in range(0, constants.BOARD_SIZE):
            print(
                str(row_index + 1).rjust(2) + " " + " ".join(self.boards[0].grid()[0]) +
                self.arena_padding() +
                str(row_index + 1).rjust(2) + " " + " ".join(self.boards[1].grid()[0])
            )

        # Assemble the banner.
        print('\n{}\n'.format(self.banners[self.banner].format(*self.banner_params)))

        # Assemble the prompt
        print(self.prompts[self.prompt].format(*self.prompt_params))

        # Clear out the banner params so they don't show next time.
        self.banner_params = ()
        self.prompt_params = ()


    def place_ships(self):
        self.banner_params = [self.boards[0].player_name]
        self.banner = "place_ships"
      
        self.prompt = "front_of_ship_coords"

        coordinates = ""
        while coordinates == "":
            self.prompt_params = ["Aircraft Carrier", 5]
            self.display_arena()
            potential_coordinates = self.get_input()
            if self.validate_coordinates(coordinates=potential_coordinates):
                coordinates = potential_coordinates
                self.banner_params = [self.boards[0].player_name]
                self.banner = "place_ships"
                self.prompt = "ship_orientation"
                orientation = ""
                while orientation == "":
                    self.prompt_params = ["Aircraft Carrier", 5]
                    self.display_arena()

                    potential_orientation = self.get_input()
                    if self.validate_orientation(potential_orientation):
                        orientation = potential_orientation
                    else:
                        self.banner_params = [self.boards[0].player_name]
                        self.banner = "invalid_orientation"

            else:
                self.banner_params = [self.boards[0].player_name]
                self.banner = "invalid_coordinates"



    def set_player_names(self):
        # Loop through the board indexes
        for num in range(0,2):
            self.banner = "welcome"
            self.prompt = "player_" + str(num)
            # Check the banner to see when a valid name if found.
            while self.banner != 'name_set':
                self.display_arena()
                self.banner = self.boards[num].set_player_name(self.get_input())
                # Prevent the same name from being used for each player
                if self.boards[0].player_name == self.boards[1].player_name:
                    # Fall back to generic name then set banner.
                    self.boards[num].set_player_name("Player {}".format(num + 1))
                    self.banner = "error_duplicate_names_not_allowed"


    def validate_coordinates(self, **kwargs):

        try:
            column = kwargs['coordinates'][0]
        except IndexError:
            logging.info("No data sent to coordinates")
            return False

        try:
            row = int(kwargs['coordinates'][1:])
        except ValueError:
            logging.info("Invalid row sent to coordinates. Must be an integer")
            return False

        if column not in constants.COORDINATE_MAP['columns']:
            logging.info("Got invalid coordinate: {}".format(kwargs['coordinates']))
            return False
        elif row not in constants.COORDINATE_MAP['rows']:
            logging.info("Got invalid coordinate: {}".format(kwargs['coordinates']))
            return False
        else:
            logging.info("Got valid coordinate: {}".format(kwargs['coordinates']))
            return True 

    def validate_orientation(self, orientation):
        if orientation == "h" or orientation == "v":
            return True
        else:
            return False


if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    game = Game()
    game.testing_input = ["Bob", "John", "a1"]
    game.set_player_names()
    game.place_ships()


