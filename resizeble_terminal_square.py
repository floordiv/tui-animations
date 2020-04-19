import os
from time import sleep
from platform import system
from termcolor import colored


frametime = 1 / 20  # 20 fps
cls = 'cls' if system().lower() == 'windows' else 'clear'   # cross-platform
frame_color = 'red'
bgcolor = 'blue'


def square_draw():
    while True:
        w, h = os.get_terminal_size()
        os.system(cls)
        print(colored('-' * w, frame_color, 'on_' + bgcolor))
        for _ in range(h - 3):
            print(colored('|' + ' ' * (w - 2) + '|', frame_color, 'on_' + bgcolor))
        print(colored('-' * w, frame_color, 'on_' + bgcolor))
        sleep(frametime)


if __name__ == '__main__':
    square_draw()
