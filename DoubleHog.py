__author__ = 'william'

import Ascii
import Getch
import platform
import Enums
import time
import sys
import random
import threading

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

class DiceAnimation(threading.Thread):
    def __init__(self, runTime=0, playerName="null", passLabel=Ascii.roleLabel_choose, roleLabel=Ascii.passLabel):
        super(DiceAnimation, self).__init__()
        self._stop = threading.Event()
        self.runTime = runTime
        self.roleLabel = Ascii.roleLabel_choose
        self.passLabel = Ascii.passLabel
        self.playerName = playerName
        self.roleLabel = roleLabel
        self.passLabel = passLabel

    def stop(self):
        self._stop.set()

    def isStopped(self):
        return self._stop.isSet()

    def createAnimation(self):
        Ascii.clear()
        print(self.roleLabel + Ascii.getdiceAnimation1(self.playerName) + self.passLabel)
        time.sleep(1)
        Ascii.clear()
        print(self.roleLabel + Ascii.getdiceAnimation2(self.playerName) + self.passLabel)
        time.sleep(1)

    def run(self):
        if self.runTime == 0:
            while True:
                self.createAnimation()
        elif self.runTime > 0:
            for i in range(self.runTime):
                self.createAnimation()
            self.stop()
        else:
            self.stop()
            raise Exception()

    def getLabels(self):
        return [self.roleLabel, self.passLabel]

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
        if len(players) == 2:
            players.append(input("\n\n\t Ok " + players[0] + " and your friend's name? " ))
        else:
            players.append(input("\n\n\t Great! And your other friend's name? " ))

    time.sleep(1)

    message = "\n\n\tGreat! so we have "

    # Shuffled so the order at which they role dice is random.
    random.shuffle(players)
    for player in players:
        if players.index(player) == len(players) - 1:
            message += "and finally " + player
        else:
            message += player + ", "
    print(message + "\n\t(Please forgive me if I mis-pronounced your name. I'm only a robot!)")

    time.sleep(2)

    Ascii.clear()

    Animation = DiceAnimation(0, players[0], Ascii.passLabel, Ascii.roleLabel_choose)
    Animation.start()
    # Animation.stop()


    # TODO:
    # add up down, enter button
    # have a look at "Other friend" and "," error.
    # Create game logic.


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