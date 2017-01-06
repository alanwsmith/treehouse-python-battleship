import constants
import logging

from board import Board

class Game():
    
    def __init__(self):
        """The initial setup that does the following:
        - Prep the boards for each player. 
        - Create `current` dictionary to store values to pass to 
          banner and prompt.
        - Set the initial banner and prompt. 
        - Create a list to assist with testing.
        """

        logging.info("Initializing game")
        self.boards = [ Board(index = 0), Board(index = 1) ]
        self.current = {}
        self.banner = 'welcome'
        self.prompt = "player_0"
        self.testing_input = []


    def arena_padding(self):
        """Responsible for setting the space between
        boards when the UI is rendered. 
        """

        return "      "


    def display_arena(self):
        """This method is responsible for rendering the UI. 
        """

        # Clear the screen.
        print("\033c", end="")

        # Output player names.
        print("{}{}{}".format(
            self.boards[0].player_name.center(22, '-'),
            self.arena_padding(),
            self.boards[1].player_name.center(22, '-')
        ))

        # Output column letters for each board.
        print(self.header_letters() + self.arena_padding() + self.header_letters())

        # Output the row numbers and data for each board.
        for row_index in range(0, constants.BOARD_SIZE):
            print('{} {}{}{} {}'.format(
                str(row_index + 1).rjust(2),
                self.boards[0].get_row_string(row_index),
                self.arena_padding(),
                str(row_index + 1).rjust(2),
                self.boards[1].get_row_string(row_index)
            ))

        # Assemble and output the banner.
        print('\n{}\n'.format(constants.BANNERS[self.banner].format(**self.current)))

        # Assemble and output the prompt.
        print(constants.PROMPTS[self.prompt].format(**self.current))

        # Clear the error
        #if 'error' in self.current:
        #    del self.current['error']


    def get_coordinates(self):
        """Requests a set of coordinates. If a 
        valid set it entered, they are returned. 
        Otherwise, the prompt is repeated until
        a valid set is provided.

        Another good refactoring would be to make the
        names of methods differentiate between 
        raw and display coordinates.
        """

        while True:
            self.display_arena()
            raw_coordinates = self.get_input()
            coordinates = raw_coordinates.strip().lower()
            if self.validate_coordinates(coordinates):
                return coordinates
            else:
                self.current['error'] = raw_coordinates.strip()
                self.banner = "invalid_coordinates"


    def get_input(self):
        """Used to gather any and all input. 
        If the testing_input list has data, it's 
        pulled from there. Otherwise, the input
        is gathered from the UI

        A nice refactoring would be to change the prompt
        when switching players to help show that only 
        hitting Enter/Return is necessary.
        """

        if len(self.testing_input) > 0:
            return self.testing_input.pop(0)
        else:
            return input("> ")


    def get_orientation(self):
        """Prompts to get a ship orientation. If a valid
        orientation is entered, it's returned. Otherwise, 
        the prompt is repeated until a valid orientation 
        is provided. 

        Input is stripped of white space and lowercased
        before passing on to the validation.

        In a future iteration, this method should be 
        refactored to return True or False instead of
        setting the banner directly.
        """

        while True:
            self.display_arena()
            raw_orientation = self.get_input()
            orientation = raw_orientation.strip().lower()
            if self.validate_orientation(orientation):
                return orientation
            else:
                self.current['error'] = raw_orientation
                self.banner = "invalid_orientation"


    def get_ship_coordinates(self, **kwargs):
        """This method takes basic parameters for a ship and returns a list
        with zero base indexed tupals of the coordinates of the spaces
        the ship takes up on the grid. It expects the front_of_ship
        to be a valid, lowercased coordinate.
        (Of course, this really should be refacotred and pushed 
        into the ship itself with the abiblity to check
        before setting.
        """

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


    def header_letters(self):
        """Helper method to render the column letters
        for the game boards.
        """
        
        return "   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + constants.BOARD_SIZE)])


    def place_ship(self, **kwargs):
        """The method loops through the ships for a given
        player/board and asks where they should be placed. 
        The prompt is done in two parts. First, coordinates
        are requested and then an orientation (vertical or
        horizontal). At each step, the inputs are validated
        and repeat requests made if necessary. Once both
        the coordinates and the orientation are validated 
        individually, a combined validation occurs to make
        sure the requested ship location fits on the board
        and doesn't overlap with other ships that have
        already been placed. 

        This method is a little long. It's a good candidate
        for refactoring if more work was going to be done
        on this project.

        Also, this method sets the individual coordinates
        that each ship occupies. Another refactoring would
        be to only set the front_of_ship and place the 
        responsibility for calculating the individual 
        coordinates on the ship itself. The current method
        works fine, it just feels like it would be better
        by moving it to the ship.

        The current behavior only checks for conflicting
        ship placement after both valid coordinates and
        and orientation is received. A UI improvement
        would be to check the coordinates as soon as
        they come in to see if they are already in
        use (i.e. it's not necessary to get the 
        orientation to identify that as a conflict).
        That's something that can go on the feature 
        road map.
        """

        # Pull the board and ship into local variables
        board = kwargs['board']
        ship = board.ships[kwargs['ship_index']]

        # Update the banner/prompt data with ship info.
        self.current['ship'] = ship.name
        self.current['size'] = ship.size

        # Make a nice UI distinction between the first
        # ship and subsequent ones.
        if kwargs['ship_index'] == 0:
            self.banner = "place_ships"
        else:
            self.banner = "place_next_ship"

        # Do the request and set loop.
        while True:
            self.prompt = "front_of_ship_coords"
            # Use target_location dict to store all the data necessary for validation
            target_location = { 'size': ship.size }
            target_location['front_of_ship'] = self.get_coordinates()
            self.prompt = "ship_orientation"
            target_location['orientation'] = self.get_orientation()
            # Make sure the requested placement stays on the grid.
            if not self.validate_ship_stays_on_grid(**target_location):
                self.current['error'] = target_location['front_of_ship']
                self.banner = "error_ship_off_grid"
                continue
            else:
                # Grab where the ship would go if it's placed.
                target_coordinates = self.get_ship_coordinates(**target_location)
                # Make sure there isn't something already there.
                if not board.verify_coordinates_are_clear(target_coordinates):
                    self.current['error'] = target_location['front_of_ship']
                    self.banner = "error_ship_collision"
                    continue
                else:
                    logging.info("Target coords: {}". format(target_coordinates))
                    # Everything looks good so update the ship with the 
                    # coordinates and orientation.
                    ship.set_coordinates(target_coordinates)
                    ship.set_orientation(target_location['orientation'])
                    break


    def place_ships(self):
        """This method jumps through the two
        players, shows/hides the boards appropriately
        and then has them place their ships.
        """
    
        self.set_active_player_id(0)
        self.boards[1].set_grid_visibility(False)

        for ship_index in range(0, len(self.boards[0].ships)):
            self.place_ship(board = self.boards[0], ship_index = ship_index)

        self.switch_players()
        
        self.boards[0].set_grid_visibility(False)
        self.boards[1].set_grid_visibility(True)
        for ship_index in range(0, len(self.boards[1].ships)):
            self.place_ship(board = self.boards[1], ship_index = ship_index)

        self.switch_players()

    def raw_coordinates_to_display(self, raw_coordinates):
        """Translates the raw coordinates used internally
        (e.g. `(3,5)`) to the display format that the players 
        and display use (e.g. `f4`).
        """

        column_letter = ""
        while column_letter == "":
            for letter, number in constants.COORDINATE_MAP['columns'].items():
                if raw_coordinates[1] == number:
                    column_letter = letter

        row_number = raw_coordinates[0] + 1

        return '{}{}'.format(column_letter, str(row_number)) 


    def set_active_player_id(self, player_id):
        """This is a helper method that allows a single call to 
        setup the active player and opponent IDs and 
        banner/prompt formatting strings.
        """

        self.active_player = player_id

        if player_id == 0:
            self.active_opponent = 1
            self.current['player'] = self.boards[0].player_name
            self.current['opponent'] = self.boards[1].player_name
        else:
            self.active_opponent = 0
            self.current['player'] = self.boards[1].player_name
            self.current['opponent'] = self.boards[0].player_name


    def set_current_player(self, board_index):
        """The original helper method for setting the
        banner/prompt formatting strings for the player and 
        opponent. In a future iteration, this should be refactored
        out in favor of using set_active_player_id().
        """

        if board_index == 0:
            self.current['player'] = self.boards[0].player_name
            self.current['opponent'] = self.boards[1].player_name
        else:
            self.current['player'] = self.boards[1].player_name
            self.current['opponent'] = self.boards[0].player_name


    def set_player_names(self):
        """The first call of the application that lets players
        input their names. Some basic sanity checking validation 
        is done to make sure the names aren't too long and 
        aren't the same.

        The method for doing the validation is by looking at
        which banner is set. This was the first approach used. 
        In a future iteration, it should be refactored to check
        against a return True or False value that majority of 
        the later methods use. 
        """
        
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

    def start_shooting(self):
        """This is the main action loop of the game where 
        players take shots at each others' boards. 

        There are two stages to each shot. First, getting
        the desired location. Second, reporting the results. 

        During the first stage, coordinates are validated. 
        Invalid entries result in an error message and a 
        prompt to try again. 

        Once valid coordinates (that haven't been used
        before) are entered, the results are displayed. 
        In this stage, the ships on both boards are 
        hidden. Only the shot locations that both players
        know (and if they are hits, misses, etc...) are 
        shown. 

        Combining the results with the hiding of the ships 
        saves one step in each turn and makes for a nicer 
        UI. 

        To facilitate the hiding, I added a '?' marker to
        the possible display output. It improves the UI by 
        making it clear when a given board is in the 
        'ships hidden' state. 
        """

        # Set the player who gets to take the first shot.
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

            if self.banner == "shot_won_game":
                break

            self.current['ship'] = opponents_board.get_name_of_ship_that_was_just_hit() 
            self.prompt = "continue"
            self.display_arena()
            self.get_input()
            self.switch_active_player_id()
            self.banner = "take_shot"

        
        self.prompt = "game_over"
        self.display_arena()
        # One last enter to pause display so it can be seen. 
        self.get_input()


    def switch_active_player_id(self):
        """Helper method to alternate which player (and
        associated data) is active. 
        """

        if self.active_player == 0:
            self.set_active_player_id(1)
        else:
            self.set_active_player_id(0)


    def switch_players(self):
        """This is a UI focused method the hides 
        the ships on both player boards and prompts 
        the active player to hand the computer to 
        the opponent. It then waits for that player 
        to hit Enter/Return to continue the game.
        """
        
        self.banner = "switch_players"
        self.prompt = "continue"
        self.boards[0].set_grid_visibility(False)
        self.boards[1].set_grid_visibility(False)
        self.display_arena()
        self.get_input()
        self.switch_active_player_id()


    def validate_coordinates(self, coordinates):
        """This method makes sure that a requested
        set of display coordinates (e.g. `f4`) is 
        in a valid format and is actually on the board. 
        
        Any scrubbing is assumed to have already been done
        since a pass of this validation means the rest of
        the application will assume the coodinates are 
        ready to go.
        """

        # Make sure there is at least one character
        try:
            column = coordinates[0]
        except IndexError:
            return False

        # Make sure a row was entered and it's a number.
        try:
            # Grab the rest of the string since numbers can
            # be two digits.
            row = int(coordinates[1:])
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
        """This method ensures that a requested orientation
        is valid. It assumes that the value to check
        has already been stripped of spaces and properly
        lower cased.
        """

        if orientation == "h" or orientation == "v":
            return True
        else:
            return False


    def validate_ship_stays_on_grid(self, **kwargs):
        """This method make sure that a requested set 
        of coordinates, orientation, and ship size will 
        actually fit on the grid.
        """

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

    autorun_items = [
        # Setup names
        "Alex", "Zelda", 
        # Place Alex's first two ships
        "B2", "v", " c2", "V", 
        # Alex enter an invalid coordiante for ship placement
        " x9", "h", 
        # Alex properly enters the their ship and flips to Zelda.
        " d2", " h", "", 
        # Zelda enters an invalid orientation and then corrects it. 
        "c6", "x",
        # Zelda corrects the orientation. 
        "h",
        # Zelda places a ship that conflicts with the first one. 
        "c6", "h", 
        # Zelda correctly places the ship. 
        "c7 ", "H", 
        # Zelda tries to place a ship that would go off the map
        "i9", "v",
        # Zelda correctly finishes placement of ships.
        "c8", "h", "",
        # Miss a few times for each player
        "c3", "", "i1", "", "h9", "", "c9", "", "f4", "", "g7", "",
        # Alex starts hitting
        "c8",
        # Pass to Zelda 
        "",
        # Zelda tries a shot that has already been taken, the corrects
        "G7", "a1", "",
        # Alex hits a new ship and Zelda hits one too.
        "d6", "", "b2", "",
        # Back and forth until Alex sinks the first ship
        "d8", "", "c2", "", "e8",
        # Pass back to Zelda
        "",
        # Back and forth until Zelda sinks a ship
        "d2", "", "c7", "", "e2", "", "d7", "", "f2",
        # Pass back to Alex
        "",
        # Keep going until Zelda sinks the Aircraft carrier 
        "e7", "", "b3", "", "c6", "", "b4", "", "e6", "", "b5", "", "f6", "", "b6", 
        # Pass back to Alex who then sinks the Aircraft carrier.
        "", "g6",
        # The continue until Alex wins
        "", "c3", "", "f7"

        # The game should end here.
    ]


    # Build auto_runs that stop at certain points.
    test_cases = {
        "invalid_coordinates": autorun_items[0:7],
        "invalid_orientation": autorun_items[0:13],
        "ships_collide": autorun_items[0:16],
        "ship_off_grid": autorun_items[0:20],
    }

    constants.SHIP_COUNT = 3
    game = Game()

    game.testing_input = autorun_items 
    # game.testing_input = test_cases["invalid_coordinates"]
    # game.testing_input = test_cases["invalid_orientation"]
    # game.testing_input = test_cases["ships_collide"]
    # game.testing_input = test_cases["ship_off_grid"]

    game.set_player_names()
    game.place_ships()
    game.start_shooting()

