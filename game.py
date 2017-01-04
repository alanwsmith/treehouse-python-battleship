import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        logging.info("Initializing game")
        self.boards = [ Board(index = 0), Board(index = 1) ]

        # This is used to hold text strings to disply in the banner and prompts. 
        self.current = {}

        # Set the initial banner and prompt.
        self.banner = 'welcome'
        self.prompt = "player_0"

        # This is only used for testing. Makes jumping to different points easy. 
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
            print('{} {}{}{} {}'.format(
                str(row_index + 1).rjust(2),
                self.boards[0].get_row_string(row_index),
                self.arena_padding(),
                str(row_index + 1).rjust(2),
                self.boards[1].get_row_string(row_index)
            ))

        # Assemble the banner.
        print('\n{}\n'.format(constants.BANNERS[self.banner].format(**self.current)))

        # Assemble the prompt
        print(constants.PROMPTS[self.prompt].format(**self.current))


    # Use this to make it easy to keep up with player/boards
    # A next refactoring step would be to make everything use
    # this and the related switch_active_player_id() method.
    def set_active_player_id(self, player_id):
        self.active_player = player_id
        if player_id == 0:
            self.active_opponent = 1
            self.current['player'] = self.boards[0].player_name
            self.current['opponent'] = self.boards[1].player_name
        else:
            self.active_opponent = 0
            self.current['player'] = self.boards[1].player_name
            self.current['opponent'] = self.boards[0].player_name

    def switch_active_player_id(self):
        if self.active_player == 0:
            self.set_active_player_id(1)
        else:
            self.set_active_player_id(0)


    def start_shooting(self):

        self.set_active_player_id(0)

        self.banner = "take_shot"
        while True:
            self.prompt = "get_shot_coordinates"
            self.display_arena()
            player_board = self.boards[self.active_player] 
            opponents_board = self.boards[self.active_opponent]
            player_board.set_grid_visibility(True)

            while not opponents_board.place_shot(self.get_coordinates()):
                self.banner = "already_shot_there"
                continue
             
            player_board.set_grid_visibility(False)
            self.current['last_shot'] = self.raw_coordinates_to_display(opponents_board.last_shot())
            self.banner = opponents_board.last_shot_status()
            self.prompt = "continue"
            self.display_arena()
            self.get_input()
            self.switch_active_player_id()
            self.banner = "take_shot"

    def place_ships(self):
        self.set_current_player(0)
        self.boards[1].set_grid_visibility(False)
        for ship_index in range(0, len(self.boards[0].ships)):
            self.place_ship(board = self.boards[0], ship_index = ship_index)

        self.switch_players()
        self.set_current_player(1)

        self.boards[0].set_grid_visibility(False)
        self.boards[1].set_grid_visibility(True)
        for ship_index in range(0, len(self.boards[1].ships)):
            self.place_ship(board = self.boards[1], ship_index = ship_index)

        self.switch_players()


    def place_ship(self, **kwargs):
        board = kwargs['board']
        ship = board.ships[kwargs['ship_index']]
        self.current['ship'] = ship.name
        self.current['size'] = ship.size
        if kwargs['ship_index'] == 0:
            self.banner = "place_ships"
        else:
            self.banner = "place_next_ship"

        while True:
            self.prompt = "front_of_ship_coords"
            target_location = { 'size': ship.size }
            target_location['front_of_ship'] = self.get_coordinates()
            self.prompt = "ship_orientation"
            target_location['orientation'] = self.get_orientation()
            if not self.validate_ship_stays_on_grid(**target_location):
                self.banner = "error_ship_off_grid"
                continue
            else:
                target_coordinates = self.get_ship_coordinates(**target_location)
                if not board.verify_coordinates_are_clear(target_coordinates):
                    self.banner = "error_ship_collision"
                    continue
                else:
                    logging.info("Target coords: {}". format(target_coordinates))
                    ship.set_coordinates(target_coordinates)
                    ship.set_orientation(target_location['orientation'])
                    break

        
    def get_coordinates(self):
        while True:
            self.display_arena()
            coordinates = self.get_input()
            if self.validate_coordinates(coordinates):
                return coordinates
            else:
                self.banner = "invalid_coordinates"


    def get_ship_coordinates(self, **kwargs):
        # This method takes basic parameters for a ship and returns a list
        # with zero base indexed tupals of the coordinates of the spaces
        # the ship takes up on the grid. It expects the front_of_ship
        # to be a valid, lowercased coordinate.
        # (Of course, this really should be refacotred and pushed 
        # into the ship itself with the abiblity to check
        # before setting.

        raw_column = kwargs['front_of_ship'][0] 
        raw_row = int(kwargs['front_of_ship'][1:])

        column = constants.COORDINATE_MAP['columns'][raw_column]
        row = constants.COORDINATE_MAP['rows'][raw_row]

        coordinates = []
        
        if kwargs['orientation'] == "h":
            for column_index in range(column, (column + kwargs['size'])):
                coordinates.append((row, column_index))
        else:
            for row_index in range(row, (row + kwargs['size'])):
                coordinates.append((row_index, column))
         
        return coordinates 

    def get_orientation(self):
        while True:
            self.display_arena()
            orientation = self.get_input()
            if self.validate_orientation(orientation):
                return orientation
            else:
                self.banner = "invalid_orientation"

    def raw_coordinates_to_display(self, raw_coordinates):
        column_letter = ""
        while column_letter == "":
            for letter, number in constants.COORDINATE_MAP['columns'].items():
                if raw_coordinates[1] == number:
                    column_letter = letter
        row_number = raw_coordinates[0] + 1
        return '{}{}'.format(column_letter, str(row_number)) 


    def set_current_player(self, board_index):
        if board_index == 0:
            self.current['player'] = self.boards[0].player_name
            self.current['opponent'] = self.boards[1].player_name
        else:
            self.current['player'] = self.boards[1].player_name
            self.current['opponent'] = self.boards[0].player_name


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


    def switch_players(self):
        # This method of for hiding both boards
        # and prompting to give the computer to the other
        # player.
        self.banner = "switch_players"
        self.prompt = "continue"
        self.boards[0].set_grid_visibility(False)
        self.boards[1].set_grid_visibility(False)
        self.display_arena()
        self.get_input()


    def validate_coordinates(self, coordinates):

        # Scrub the input
        prepped_coordinates = coordinates.strip().lower()

        # Try to grab the column 
        try:
            column = prepped_coordinates[0]
        except IndexError:
            return False

        # Make sure there is a row and it's a number.
        try:
            row = int(prepped_coordinates[1:])
        except ValueError:
            return False
        
        # Verify the column and row are both valid.
        if column not in constants.COORDINATE_MAP['columns']:
            return False
        elif row not in constants.COORDINATE_MAP['rows']:
            return False
        else:
            return True 


    def validate_orientation(self, orientation):
        if orientation == "h" or orientation == "v":
            return True
        else:
            return False


    def validate_ship_stays_on_grid(self, **kwargs):
        # Pull in the number for the column and the row as an integer.
        column_number = constants.COORDINATE_MAP['columns'][kwargs['front_of_ship'][0]]
        row = int(kwargs['front_of_ship'][1:])

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

    constants.SHIP_COUNT = 3
    game = Game()
    game.testing_input = ["Bob", "John"]
    game.testing_input = ["Bob", "John", "b3", "v", "d2", "h", "i6", "v", "", "a1", "v", "b1", "v", "c1", "v", ""]
    # This is where shots start being fired.
    game.testing_input.extend(["a1", "", "a1", ""])
    game.set_player_names()
    game.place_ships()
    game.set_current_player(0)
    game.start_shooting()

