__author__ = 'william'

import time

if __name__ == '__main__':
    print("[ERROR]: Do not run this file. Run DoubleHog.py - this file should not be executed!")
    time.sleep(4)
    exit()


class _Getch:
    """
    Gets a single character from standard input.  Does not echo to the screen.
    """
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        # noinspection PyUnresolvedReferences
        import msvcrt

    def __call__(self):
        # noinspection PyUnresolvedReferences
        import msvcrt
        return msvcrt.getch()