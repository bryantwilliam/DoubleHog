__author__ = 'william'

import time
import os

#Error message if user executes the wrong file.
if __name__ == '__main__':
    print("[ERROR]: Do not run this file. Run main.py - this file should not be executed!")
    time.sleep(4)
    exit()

#Clear function
def clear():
    """
    Clears the console screen using the built in commands on a operating
    system (here linux and windows)
    """
    os.system(['clear','cls', "^L"][os.name == 'nt'])

menuStart = """\nUse the arrow keys...\n\n\n\n\n\n\n\n
     _____________    _____________    _____________
    |             |  |             |  |             |
    |>Play a game<|  |  See rules  |  |    Exit     |
    |_____________|  |_____________|  |_____________|
"""

menuRules = """\nUse the arrow keys...\n\n\n\n\n\n\n\n
     _____________    _____________    _____________
    |             |  |             |  |             |
    | Play a game |  | >See rules< |  |    Exit     |
    |_____________|  |_____________|  |_____________|
"""

menuExit = """\nUse the arrow keys...\n\n\n\n\n\n\n\n
     _____________    _____________    _____________
    |             |  |             |  |             |
    | Play a game |  |  See rules  |  |   >Exit<    |
    |_____________|  |_____________|  |_____________|
"""

