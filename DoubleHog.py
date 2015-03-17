__author__ = 'william'

import Ascii
import Getch
import platform
import Enums

if platform.system() == "Windows":
    ENTER_KEY = 13
    LEFT_KEY = 75
    RIGHT_KEY = 77
elif platform.system() == "Linux":
    ENTER_KEY = 13
    LEFT_KEY = 68
    RIGHT_KEY = 67

menuStates = Enums.enum(START=Ascii.menuStart, RULES=Ascii.menuRules, EXIT=Ascii.menuExit)

def getNewState(key, currentState):
    states = [menuStates.START, menuStates.RULES, menuStates.EXIT]
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
    currentState = menuStates.START
    print(Ascii.menuStart)

    pressedEnter = False
    while pressedEnter == False:
        key = ord(getch())
        if key == ENTER_KEY and currentState == menuStates.START:
            #start()
            pressedEnter = True

        elif key == ENTER_KEY and currentState == menuStates.EXIT:
            exit()
            pressedEnter = True

        elif key == ENTER_KEY and currentState == menuStates.RULES:
            #rules()
            pressedEnter = True
        else:
            currentState = getNewState(key, currentState)
            Ascii.clear()
            print(currentState)



#if the file is the main file then start the program
if __name__ == '__main__':
    init()