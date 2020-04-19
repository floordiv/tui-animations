import sys
import platform
from os import system
from time import sleep
from string import ascii_letters


cls = 'cls' if platform.system().lower() == 'windows' else 'clear'  # cross-platform
timeout = 0.05
retries = 3


if len(sys.argv) > 1:
    words = list(' '.join(sys.argv[1:]))
else:
    words = list(input('Text> '))


for _ in range(retries):
    for index, letter in enumerate(words):
        system(cls)
        if letter in ascii_letters:
            print(''.join(words[:index]) + letter.upper() + ''.join(words[index + 1:]))
            sleep(timeout)

print(''.join(words))
