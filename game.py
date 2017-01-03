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
            "error_ship_off_grid": "Oops! That won't fit on the grid. Try again.",
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

    def set_ui(self, **kwargs):
        self.banners['custom'] = kwargs['banner']
        self.prompts['custom'] = kwargs['prompt']
        self.banner = 'custom'
        self.prompt = 'custom'

    def place_ships_2(self):
        self.set_ui(banner="Place ships", prompt="First ship")
        self.display_arena()
        self.get_coordinates()


    def get_coordinates(self):
        while True:
            coordinates = self.get_input()
            if self.validate_coordinates_2(coordinates):
                print("Got valid coordinates")
                break


    def place_ships(self):

        player_id = 0
        board = self.boards[player_id]
        
        for ship_index in range(0, len(board.ships)):
            ship = board.ships[ship_index]
            self.banner_params = [board.player_name]
            self.banner = "place_ships"
            coordinates = ""
            while coordinates == "":
                self.prompt = "front_of_ship_coords"
                self.prompt_params = [ship.name, ship.size]
                self.display_arena()
                potential_coordinates = self.get_input()
                if self.validate_coordinates(coordinates=potential_coordinates):
                    coordinates = potential_coordinates
                    self.banner_params = [board.player_name]
                    self.banner = "place_ships"
                    self.prompt = "ship_orientation"
                    orientation = ""
                    while orientation == "":
                        self.prompt_params = [ship.name, ship.size]
                        self.display_arena()

                        potential_orientation = self.get_input()
                        if self.validate_orientation(potential_orientation):
                            orientation = potential_orientation

                            if not self.validate_ship_stays_on_grid(
                                coordinates = coordinates,
                                orientation = orientation,
                                size = ship.size):

                                self.banner = "error_ship_off_grid"
                                coordinates = ""
                                orientation = ""


                        else:
                            self.banner_params = [board.player_name]
                            self.banner = "invalid_orientation"

                else:
                    self.banner_params = [board.player_name]
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

    def validate_coordinates_2(self, coordinates):

        # Scrub the input
        prepped_coordinates = coordinates.strip().lower()

        # Try to grab the column or bail out.
        try:
            column = prepped_coordinates[0]
        except IndexError:
            return False

        # Make sure there is a row and it's a number.
        try:
            row = int(prepped_coordinates[1:])
        except ValueError:
            return False
        
        if column not in constants.COORDINATE_MAP['columns']:
            return False
        elif row not in constants.COORDINATE_MAP['rows']:
            return False
        else:
            return True 

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


    def validate_ship_stays_on_grid(self, **kwargs):
        # Pull in the number for the column and the row as an integer.
        column_number = constants.COORDINATE_MAP['columns'][kwargs['coordinates'][0]]
        row = int(kwargs['coordinates'][1:])

        # Run the checks (which assume the coordinate has already been validated)
        if kwargs['orientation'] == 'v' and (row + kwargs['size']) > constants.BOARD_SIZE:
            return False
        elif kwargs['orientation'] == 'h' and (column_number + kwargs['size']) > constants.BOARD_SIZE:
            return False
        else:
            return True

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/game.txt', 
        filemode='w', 
        format='[%(levelname).1s]: %(message)s', 
        level=logging.INFO
    )

    game = Game()
    game.testing_input = ["Bob", "John"]
    game.set_player_names()
    # game.place_ships()

    game.place_ships_2()


