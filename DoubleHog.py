__author__ = 'william'

import platform

import time
import sys
import random
import threading
# Was going to use threads for animation but it seems like it won't work since getch() creates a thread
# that continually creates blank lines then delete them and that messes up text output in another thread.
# I'll keep this import here just incase I do something with it later and also to remind myself

import Ascii

import Getch
import Enums


if sys.version_info[0] == 2:
    def input(text):
        # noinspection PyUnresolvedReferences
        return raw_input(text)

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
turnStates = Enums.enum(ROLE_CHOOSE=Ascii.roleLabel_choose, ROLE=Ascii.roleLabel, PASS_CHOOSE=Ascii.passLabel_choose,
                        PASS=Ascii.passLabel)


def startGame():
    Ascii.clear()
    print("\n\n\t\t\tAwesome! Lets get started then...")
    while True:
        try:
            amountPlayers = int(input("\n How many players will you be playing with? (2-4 are the limits): "))
            if amountPlayers not in [2, 3, 4]:
                raise ValueError
        except ValueError:
            for i in range(3):
                Ascii.clear()
                print(" Error! You did not enter a valid number! (2-4 are the limits)")
                time.sleep(1)
            Ascii.clear()
        else:
            break
    players = []
    players.append(input("\n\n\t Ok cool! We got " + str(amountPlayers) + " players. So what's your name? "))

    for player in range(amountPlayers - 1):
        if len(players) == 1:
            players.append(input("\n\n\t Ok " + players[0] + " and your friend's name? "))
        else:
            players.append(input("\n\n\t Great! And your other friend's name? "))

    time.sleep(1)

    message = "\n\n\tGreat! so we have "

    # Shuffled so the order at which they role dice is random.
    random.shuffle(players)
    for index in range(len(players)):
        if index == len(players) - 1:
            if not len(players) == 2:
                message += "and finally " + players[index]
            else:
                message += "and " + players[index]
        else:
            if not (len(players) == 2 or index == len(players) - 2):
                message += players[index] + ", "
            else:
                message += players[index] + " "
    print(message + "\n\t(Please forgive me if I mis-pronounced your name. I'm only a robot!)")

    time.sleep(3)

    for i in range(2):
        Ascii.clear()

        print(Ascii.roleLabel + Ascii.getdiceAnimation1(players[0]) + Ascii.passLabel)

        time.sleep(1)

        Ascii.clear()
        print(Ascii.roleLabel + Ascii.getdiceAnimation2(players[0]) + Ascii.passLabel)

        time.sleep(1)

    roleState = turnStates.ROLE_CHOOSE
    passState = turnStates.PASS

    Ascii.clear()
    print(roleState + Ascii.getdiceAnimation1(players[0]) + passState)

    getch = Getch._Getch()
    while True:
        Ascii.clear()
        print(roleState + Ascii.getdiceAnimation1(players[0]) + passState)
        key = ord(getch())
        if key == DOWN_KEY:
            if roleState == turnStates.ROLE_CHOOSE:
                roleState = turnStates.ROLE
                passState = turnStates.PASS_CHOOSE
        elif key == UP_KEY:
            if passState == turnStates.PASS_CHOOSE:
                roleState = turnStates.ROLE_CHOOSE
                passState = turnStates.PASS
        elif key == ENTER_KEY:
            if passState == turnStates.PASS_CHOOSE:
                passRound()
                break
            elif roleState == turnStates.ROLE_CHOOSE:
                roleRound()
                break
                # TODO:
                # add up down, enter button
                # have a look at "Other friend" and "," error.
                # Create game logic.


def passRound():
    Ascii.clear()


def roleRound():
    Ascii.clear()
    dice1 = random.randrange(1, 6)
    dice2 = random.randrange(1, 6)
    for i in range(3):
        print("\n\n\n\n\t\t\t\t  Rolling...")
        print(Ascii.rollingDice1)
        time.sleep(1)
        Ascii.clear()
        print("\n\n\n\n\t\t\t\t  Rolling...")
        print(Ascii.rollingDice2)
        time.sleep(1)
        Ascii.clear()

    diceAni1 = Ascii.diceRoles.get(dice1)
    diceAni2 = Ascii.diceRoles.get(dice2)
    print("\n\n\n\n\n\n\n\n\t\t\t\t" + diceAni1[0:7] + "\t" + diceAni2[0:7])
    print("\t\t\t\t" + diceAni1[7:14] + "\t" + diceAni2[7:14])
    print("\t\t\t\t" + diceAni1[14:] + "\t" + diceAni2[14:])

    youRolledMsg = "\n\n\t\t\tYou rolled "
    if dice1 == dice2:
        youRolledMsg += "2 " + str(dice1) + "'s"
    else:
        youRolledMsg += "a " + str(dice1) + " and a " + str(dice2)
    print(youRolledMsg)

    if dice1 == 1 or dice2 == 1:
        if dice1 == dice2:
            # Double 1s
            pass
        if dice1 != dice2:
            # Single 1
            pass

    print("\n\n\t\t\tYou rolled a " + str(dice1) + " and a " + str(dice2))


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