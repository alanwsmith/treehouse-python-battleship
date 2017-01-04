Treehouse Battleship Python Project
===================================

My run at the Treehouse Battleship project in Python.

Notes
-----

- This was built and tested on a machine running Python 2.7.6

- The board size can be expanded up to 26 (the length of the full alphabet). Any larger would require a refactoring (and design rethinking since the current format allows for only single letter columns).




Testing Notes
-------------

Banner messages and prompts are setup as a dictionary store. Instead of trying to test the UI directly, messages are verified by the current state of the key used for each item. 


(Look into sending a list for items that need to use .format().)



TODOs
-----

- Refactor to remove 'cols' from constants.COORDINATE_MAP. Use the better named 'columns' for replacements. 




Tests to run
------------

- Each player will place their ships without the other one watching.
- After the player has entered a location the screen will be cleared and the results of the guess will be displayed on the screen.
- Players continue taking turns until one of the players guesses all of the locations on the board that opponent’s ships occupy. That player is declared the winner.
- To get full credit, you’ll need to write a minimum of three class definitions. You may write more than three though.
- The code should be clean, readable, and well organized and comply with Python PEP 8 standards.
- Refer to players using their names whenever possible.
- Under the board, prompt the user to enter one ship at a time.
- For each ship, ask if they want the ship to be oriented horizontally or vertically then ask which location on the board the first ships should be placed.
- Verify that the ships fit on the board and that they don’t overlap with any existing ships. 
- After the user places a ship, clear the screen and print the board to the screen with all of the ships that the player has placed up until that point displayed on the board using the appropriate symbols.
- After the first player has placed all their ships, clear the screen and prompt the second player, by name, to begin placing their ships.
- Clear the screen after each player has finished taking their turn. Prompt the next player, by name, that it is their turn. Prompt them to press enter to continue. This gives the previous player a chance to hand the computer to the next player so they don’t see each other’s boards.
- During play, show both the opponent's screen and the current player's screen with the appropriate markers.
- If the player enters a location that they’ve already guessed, then prompt the user for a new location after telling them why their previous guess was unacceptable.
- Continue the game until one of the players has sunk all of their opponent’s ships. Congratulate the winner with a final message. For an exceeds, display both the player’s boards on the screen.
- Error messages are detailed and include the invalid guess information.
- Display both the player’s boards on the screen showing the ship positions.
- Set names
- Place ships

- Don't allow both players to have the same name. 
- Don't allow empty names.
- Don't allow a ship to be placed so that part of it is outside the grid. 
- Make sure either 'v' or 'h' is used for ship orientation. 
- Spaces before or after the player’s input is allowed. 
- Both lower and uppercase characters are also allowed. 


