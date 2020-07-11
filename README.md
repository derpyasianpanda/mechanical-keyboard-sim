# Mechanical Keyboard Simulator

TL:DR It just plays cool keyboard sounds lol

This is a program allows a user to play specific sounds when typing on a
keyboard. Specifically, it allows a user to test out a certain mechanical
keyboard's sounds so that a user can "test" out what a certain switch can sound
like

Confirmed to work only on Windows.
If you know of a good Python library that can play sounds cross-platform,
please tell me (or pull request :D)

## Running the program

Have Python 3.6+ installed and all the dependencies from the requirements.txt
with `pip install -r requirements.txt`

You can now open the main.py with the Python interpreter (or after opening a
terminal in the directory you can run the command `python main.py`)

You can now just follow the instructions on the screen

## How to add your own custom sounds

All you need to do is go to the sounds directory and put a folder that contains
all the sounds. The naming scheme is all lowercased and is often just the
character or key name. For more specifics, see the passage below

This program is made using the Python keyboard library. The canonical key names
can be found [here](https://github.com/boppreh/keyboard/blob/master/keyboard/_canonical_names.py)

If anyone is willing to give me a set of keyboard sounds, please contact me on
Discord at Vel0ciTy#3728. I can then upload them to this repository (If I get
enough, I might make a separate repository to house them)
