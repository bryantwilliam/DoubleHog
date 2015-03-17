__author__ = 'william'

import Ascii
import Getch
import platform
import Enums

if platform.system() == "Windows":
    ENTER_KEY = 13
    LEFT_KEY = 75
    RIGHT_KEY = 77
    UP_KEY = 72
    DOWN_KEY = 80

elif platform.system() == "Linux":
    ENTER_KEY = 13
    LEFT_KEY = 68
    RIGHT_KEY = 67
    UP_KEY = 65
    DOWN_KEY = 66

menuStates = Enums.enum(START=Ascii.menuStart, RULES=Ascii.menuRules, EXIT=Ascii.menuExit)


def startGame():
    pass
    # TODO:
    # Create game.

def displayRules():
    rules = Ascii.rules
    min = 1
    max = 17
    changed = True

    getch = Getch._Getch()
    while True:
        if changed:
            Ascii.clear()
            print(rules[0])
            for lineNumber in range(min, max):
                print(rules[lineNumber])
            print(Ascii.okButtonRules)
            changed = False
        key = ord(getch())
        if key == ENTER_KEY:
            init()
            break
        elif key == DOWN_KEY or key == RIGHT_KEY:
            if max != len(rules):
                min += 1
                max += 1
                changed = True
        elif key == UP_KEY or key == LEFT_KEY:
            if min != 1:
                min -= 1
                max -= 1
                changed = True


def init():
    getch = Getch._Getch()
    currentState = menuStates.START
    Ascii.clear()
    print(Ascii.menuStart)

    while True:
        key = ord(getch())
        if key == ENTER_KEY and currentState == menuStates.START:
            startGame()
            break

        elif key == ENTER_KEY and currentState == menuStates.EXIT:
            exit()
            break

        elif key == ENTER_KEY and currentState == menuStates.RULES:
            displayRules()
            break
        else:
            states = [menuStates.START, menuStates.RULES, menuStates.EXIT]
            if key == LEFT_KEY:
                if states.index(currentState) == 0:
                    currentState = states[2]
                else:
                    currentState = states[states.index(currentState) - 1]
            elif key == RIGHT_KEY:
                if states.index(currentState) == 2:
                    currentState = states[0]

                else:
                    currentState = states[states.index(currentState) + 1]
            Ascii.clear()
            print(currentState)


# if the file is the main file then start the program
if __name__ == '__main__':
    init()