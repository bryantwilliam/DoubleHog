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
    for i in range(3):
        print(chr(27) + "[2J")


menuStart = """\nUse the arrow keys...\n\n\n\n\n\t\t\t  Welcome to Double Hog!!!\n
 \tDouble Hog is a fun dice game played using two six-sided dice.
 Double Hod is a variation on the dice game 'Pig' - sometimes also called 'Hog'\n\n
             _____________    _____________    _____________
            |             |  |             |  |             |
            |>Play a game<|  |  See rules  |  |    Exit     |
            |_____________|  |_____________|  |_____________|
\n\n\n\n\n\n\n"""

menuRules = """\nUse the arrow keys...\n\n\n\n\n\t\t\t  Welcome to Double Hog!!!\n
 \tDouble Hog is a fun dice game played using two six-sided dice.
 Double Hod is a variation on the dice game 'Pig' - sometimes also called 'Hog'\n\n
             _____________    _____________    _____________
            |             |  |             |  |             |
            | Play a game |  | >See rules< |  |    Exit     |
            |_____________|  |_____________|  |_____________|
\n\n\n\n\n\n\n"""

menuExit = """\nUse the arrow keys...\n\n\n\n\n\t\t\t  Welcome to Double Hog!!!\n
 \tDouble Hog is a fun dice game played using two six-sided dice.
 Double Hod is a variation on the dice game 'Pig' - sometimes also called 'Hog'\n\n
             _____________    _____________    _____________
            |             |  |             |  |             |
            | Play a game |  |  See rules  |  |   >Exit<    |
            |_____________|  |_____________|  |_____________|
\n\n\n\n\n\n\n"""

# 18 lines of rules are shown at a time.
rules = ["\t\t\t\tRULES:",
         " ",
         "Players:",
         " ",
         "Usually played between 2 people.",
         "Goal:",
         "The first person to reach 100 points is the winner.",
         " ",
         "Gameplay:",
         " ",
         "On a turn, a player rolls the dice repeatedly until either:",
         "    * a single 1 is rolled",
         "    * the player chooses to hold (stop rolling)",
         "If either of the above occurs, it is the next player's turn.",
         " ",
         "Scoring:",
         " ",
         "If a player rolls:",
         "    * a single 1 - their turn ends and the total value of both dice is deducted",
         "      from their score.",
         "    * (eg if they throw a 1 and a 3, 4 is deducted from their score; 1+5 will",
         "      mean 6 is deducted from their score",
         "[NOTE: It is possible for players to have a negative score eg \"-6\"]",
         "    * double 1s - player gets 25 points",
         "    * other doubles (eg 2+2, 3+3) - player gets double points (eg 2+2 counts as",
         "      8 3+3 counts as 12; 4+4 counts as 16)",
         "    * in all other cases - the player gets the total of both dice (eg 3+4 counts",
         "      as 7 points; 2+3 counts as 5 points)",
         " ",
         "Game End:",
         " ",
         "When a player reaches a total of 100 or more points, that player is the winner,",
         "and the game ends."]
okButton = """
                                 ____________
          TIP:                  |            |
 Use the up and down arrow      |    >OK<    |
 keys to scroll up and down     |____________|
"""
