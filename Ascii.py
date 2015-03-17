__author__ = 'william'

import time
import os

if __name__ == '__main__':
    print("[ERROR]: Do not run this file. Run DoubleHog.py - this file should not be executed!")
    time.sleep(4)
    exit()


def clear():
    """
    Clears the console screen using the built in commands on a operating
    system (here linux and windows)
    """
    os.system(['clear', 'cls', "^L"][os.name == 'nt'])

menuStart = """\nUse the arrow keys...\n\n\n\n\n\t\t\t  Welcome to Double Hog!!!\n
 \tDouble Hog is a fun dice game played using two six-sided dice.
 Double Hod is a variation on the dice game 'Pig' - sometimes also called 'Hog'\n\n
             _____________    _____________    _____________
            |             |  |             |  |             |
            |>Play a game<|  |  See rules  |  |    Exit     |
            |_____________|  |_____________|  |_____________|
"""

menuRules = """\nUse the arrow keys...\n\n\n\n\n\t\t\t  Welcome to Double Hog!!!\n
 \tDouble Hog is a fun dice game played using two six-sided dice.
 Double Hod is a variation on the dice game 'Pig' - sometimes also called 'Hog'\n\n
             _____________    _____________    _____________
            |             |  |             |  |             |
            | Play a game |  | >See rules< |  |    Exit     |
            |_____________|  |_____________|  |_____________|
"""

menuExit = """\nUse the arrow keys...\n\n\n\n\n\t\t\t  Welcome to Double Hog!!!\n
 \tDouble Hog is a fun dice game played using two six-sided dice.
 Double Hod is a variation on the dice game 'Pig' - sometimes also called 'Hog'\n\n
             _____________    _____________    _____________
            |             |  |             |  |             |
            | Play a game |  |  See rules  |  |   >Exit<    |
            |_____________|  |_____________|  |_____________|
"""

