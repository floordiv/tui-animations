import os
import sys
from time import sleep
from platform import system
from termcolor import colored


cls = 'cls' if system().lower() == 'windows' else 'clear'
boardsize = 30
speed = 0.1
pause = 0.4
textcolor = 'red'


def anim(text):
    while True:
        textpos = [0, boardsize - 2]
        for _ in range(len(text) - boardsize + 3):
            w, h = os.get_terminal_size()
            horizontal_tab = ' ' * (w // 2 - boardsize // 2)
            os.system(cls)
            print('\n' * (h // 2 - 3))
            print(horizontal_tab + '-' * boardsize)
            print(horizontal_tab + '|' + colored(text[textpos[0]:textpos[1]], textcolor) + '|')
            print(horizontal_tab + '-' * boardsize)
            textpos[0] += 1
            textpos[1] += 1
            sleep(speed)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input('Text> ')

    try:
        anim(' ' * (boardsize - 2) + text + ' ' * (boardsize - 2))
    except KeyboardInterrupt:
        print('\nBye, my impatient friend')
