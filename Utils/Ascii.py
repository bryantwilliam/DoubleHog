__author__ = 'william'

import time
import os
import platform

if __name__ == '__main__':
    print("[ERROR]: Do not run this file. Run DoubleHog.py - this file should not be executed!")
    time.sleep(4)
    exit()


def clear():
    """
    Clears the console screen using the built in commands on a operating
    system (Linux and windows)
    This is pretty much the only comment I'm going to make because I'm extremely lazy (which is bad)
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def capStart(word):
    word = word.lower()
    letters = []
    for letter in word:
        letters.append(letter)
    letters[0] = letters[0].upper()
    word = "".join(letters)
    return word


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


def bold(msg):
    # Unfortunately bold only works on Linux (My computer is running Linux so that's why I've made this cross-platform)
    if platform.system() == "Linux":
        return u'\033[1m%s\033[0m' % msg
    else:
        return msg

# 16 lines of rules are shown at a time. Not including top line and ok button
rules = [bold("\t\t\t\t  RULES:"),
         " ",
         bold("Players:"),
         " ",
         "Usually played between 2 people.",
         bold("Goal:"),
         "The first person to reach 100 points is the winner.",
         " ",
         bold("Gameplay:"),
         " ",
         "On a turn, a player rolls the dice repeatedly until either:",
         "    * a single 1 is rolled",
         "    * the player chooses to hold (stop rolling)",
         "If either of the above occurs, it is the next player's turn.",
         " ",
         bold("Scoring:"),
         " ",
         bold("If a player rolls:"),
         "    * a single 1 - their turn ends and the total value of both dice is deducted",
         "      from their score.",
         "    * (eg if they throw a 1 and a 3, 4 is deducted from their score; 1+5 will",
         "      mean 6 is deducted from their score",
         "[NOTE: It is possible for players to have a negative score eg \"-6\"]",
         "    * double 1s - player gets 25 points",
         "    * other doubles (eg 2+2, 3+3) - player gets double points (eg 2+2 counts as",
         "      8 3+3 counts as 12; 4+4 counts as 16)",
         "    * in all other cases - the player gets the total of both dice",
         "      (eg 3+4 counts as 7 points; 2+3 counts as 5 points)",
         " ",
         bold("Game End:"),
         " ",
         "When a player reaches a total of 100 or more points, that player is the winner,",
         "and the game ends."]
okButtonRules = """
                                 ____________
          TIP:                  |            |
 Use the up and down arrow      |    >OK<    |
 keys to scroll up and down     |____________|
"""

okButtonGeneral = """
                                 ____________
                                |            |
                                |    >OK<    |
                                |____________|
"""

roleLabel_choose = """
\t _______  _______  _        _______
\t(  ____ )(  ___  )( \      (  ____ \\
\t| (    )|| (   ) || (      | (    \/
\t| (____)|| |   | || |      | (__
\t|     __)| |   | || |      |  __)     <----- Role (Press Enter)
\t| (\ (   | |   | || |      | (
\t| ) \ \__| (___) || (____/\| (____/\\
\t|/   \__/(_______)(_______/(_______/
"""
roleLabel = """
\t _______  _______  _        _______
\t(  ____ )(  ___  )( \      (  ____ \\
\t| (    )|| (   ) || (      | (    \/
\t| (____)|| |   | || |      | (__
\t|     __)| |   | || |      |  __)
\t| (\ (   | |   | || |      | (
\t| ) \ \__| (___) || (____/\| (____/\\
\t|/   \__/(_______)(_______/(_______/
"""

passLabel_choose = """
\t _______  _______  _______  _______
\t(  ____ )(  ___  )(  ____ \(  ____ \\
\t| (    )|| (   ) || (    \/| (    \/
\t| (____)|| (___) || (_____ | (_____
\t|  _____)|  ___  |(_____  )(_____  )   <----- Pass (Press Enter)
\t| (      | (   ) |      ) |      ) |
\t| )      | )   ( |/\____) |/\____) |
\t|/       |/     \|\_______)\_______)"""

passLabel = """
\t _______  _______  _______  _______
\t(  ____ )(  ___  )(  ____ \(  ____ \\
\t| (    )|| (   ) || (    \/| (    \/
\t| (____)|| (___) || (_____ | (_____
\t|  _____)|  ___  |(_____  )(_____  )
\t| (      | (   ) |      ) |      ) |
\t| )      | )   ( |/\____) |/\____) |
\t|/       |/     \|\_______)\_______)"""


def getdiceAnimation1(playerName):
    dice1 = \
        "\n\t\t\t\t\t\t  ____" + \
        "\n\t\t\t\t\t\t /\\' .\\" + \
        "\n\t\t\tOR\t\t\t/: \___\\   " + playerName + "'s turn" + \
        "\n\t\t\t\t\t\t\\' / . /" + \
        "\n\t\t\t\t\t\t \/___/"
    return dice1


def getdiceAnimation2(playerName):
    dice2 = \
        "\n\t\t\t\t\t\t  _____" + \
        "\n\t\t\t\t\t\t / .  /\\" + \
        "\n\t\t\tOR\t\t\t/____/..\\  " + playerName + "'s turn" + \
        "\n\t\t\t\t\t\t\\'  '\  /" + \
        "\n\t\t\t\t\t\t \\'__'\/"
    return dice2


rollingDice1 = """\n
                                   ______
                                  /     /\\
                                 /  '  /  \\
                                /_____/. . \\
                                \ . . \    /
                                 \ . . \  /
                                  \_____\/
"""

rollingDice2 = """\n
                                 _______.
                                | .   . |\\
                                |   .   |.\\
                                | .   . |.'|
                                |_______|.'|
                                 \ ' .   \\'|
                                  \____'__\|
"""

# 0-6
# 7-13
# 14-20
diceRoles = {1: "[     ][  o  ][     ]",
             2: "[     ][ o o ][     ]",
             3: "[  o  ][ o o ][     ]",
             4: "[ o o ][     ][ o o ]",
             5: "[ o o ][  o  ][ o o ]",
             6: "[ o o ][ o o ][ o o ]"}

score = """
                         _____
                        /  ___|
                        \ `--.  ___ ___  _ __ ___
                         `--. \/ __/ _ \| '__/ _ \\
                        /\__/ / (_| (_) | | |  __/
                        \____/ \___\___/|_|  \___|
"""

arrow = """
                  .
   .. ............;;.
    ..::::::::::::;;;;.
  . . ::::::::::::;;:'
                  :'
"""