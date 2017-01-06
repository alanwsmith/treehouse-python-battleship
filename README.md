Treehouse Battleship Python Project
===================================

My run at the Treehouse Battleship project in Python.

Running 
-------

- This project was built and runs on Python 3. 

- Start the game with: `python3 battleship.py`

Notes
-----

- I added a '?' symbol that's used to cover unknown parts of opponents boards. I think it makes for a better user interface.

- I decided to display the boards side-by-side instead of on top of each other. I think keeping each player's board in the same place throughout the game improves the user interface.

- I setup a simple test framework. It's used in the `board_test.py`, `game_test.py`, and `ship_test.py` files.

- Running the `board.py` and `ship.py` files will call their corresponding `_test.py` files. 

- Running `game.py` directly will do an automatic play-through of a game that's used for manual acceptance testing. 

- The automatic run in `game.py` can be altered by uncommenting the `game.testing_input = test_cases["ship_off_grid"]` type lines. This will stop the automatic playback at various checkpoints. 

- There are some other notes inside comments (especially in the `game.py` file) that explain more of my though processes. These include identifying lots of places where I'd refactor the code if this project was going to go further.
