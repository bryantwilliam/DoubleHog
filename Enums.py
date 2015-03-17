__author__ = 'william'

import time

if __name__ == '__main__':
    print("[ERROR]: Do not run this file. Run DoubleHog.py - this file should not be executed!")
    time.sleep(4)
    exit()

def enum(**enums):
    return type('Enum', (), enums)