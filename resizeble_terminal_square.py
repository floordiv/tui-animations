import os
from time import sleep
from platform import system
from threading import Thread


class data:
    resolution = [0, 0]
    frametime = 1 / 20  # 20 fps
    cls = 'cls' if system().lower() == 'windows' else 'clear'   # cross-platform


def terminal_size_listener():
    while True:
        data.resolution = os.get_terminal_size()
        sleep(data.frametime)


def square_draw():
    sleep(0.1)
    while True:
        os.system(data.cls)
        w, h = data.resolution
        print('-' * w)
        for _ in range(h - 3):
            print('|' + ' ' * (w - 2) + '|')
        print('-' * w)
        sleep(data.frametime)


if __name__ == '__main__':
    Thread(target=terminal_size_listener).start(), Thread(target=square_draw).start()
