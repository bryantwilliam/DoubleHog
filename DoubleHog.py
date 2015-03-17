#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     An RPG (Roll playing game) where you wake up in a room and have
#              to figure out text based puzzles to escape.
#              The whole game will be done in a terminal (Shell) and will be
#              completely text and ascii code. This will be the main file.
#
# Author:      William Bryant
#
# Created:     15/12/2013
# Copyright:   (c) William Bryant 2013
#-------------------------------------------------------------------------------

import time
import Ascii
import Getch
from enum import Enum
import platform

if platform.system() == "Windows":
    ENTER_KEY = 13
    LEFT_KEY = 75
    RIGHT_KEY = 77
elif platform.system() == "Linux":
    ENTER_KEY = 13
    LEFT_KEY = 68
    RIGHT_KEY = 67



class menuState(Enum):
    start = Ascii.menuStart
    rules = Ascii.menuRules
    exit = Ascii.menuExit


def getNewState(key, currentState):
    states = [menuState.start, menuState.rules, menuState.exit]
    states.index(currentState)
    if key == LEFT_KEY:
        if states.index(currentState) == 0:
            return states[2]
        else:
            return states[states.index(currentState) - 1]
    elif key == RIGHT_KEY:
        if states.index(currentState) == 2:
            return states[0]

        else:
            return states[states.index(currentState) + 1]
    else:
        return currentState
#This is a small text based gui with the ability to change option with arrow
#keys which players can choose to start/exit the game


def init():
    getch = Getch._Getch()
    currentState = menuState.start
    print(Ascii.menuStart)

    pressedEnter = False
    while pressedEnter == False:
        key = ord(getch())
        if key == ENTER_KEY and currentState == menuState.start:
            #start()
            pressedEnter = True

        elif key == ENTER_KEY and currentState == menuState.exit:
            exit()
            pressedEnter = True

        elif key == ENTER_KEY and currentState == menuState.rules:
            #rules()
            pressedEnter = True
        else:
            currentState = getNewState(key, currentState)
            print(currentState.value)



#if the file is the main file then start the program
if __name__ == '__main__':
    init()