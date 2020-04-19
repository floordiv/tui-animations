import os
import sys
from time import sleep
from platform import system

config = {
    'move_speed': 0.05,
    'cls': 'cls' if system().lower() == 'windows' else 'clear',
    'direction': 'left',
    'bubble': True,
    'halign': True,
    'use_terminal_width': True,
    'default_field_len': 20,
    'collision_retries': 3,
    'infinity_loop': False,
    'flags': ['--bubble', '--use-terminal-width', '--halign'],
}


def anim(text):
    w, h = (config['default_field_len'], 0)

    if config['use_terminal_width']:
        w, h = os.get_terminal_size()
        h //= 2
        h -= 3

    start_coord = ((w - 2) - len(text), 0)
    left_space, right_space = start_coord if config['direction'] == 'left' else start_coord[::-1]

    try:
        for _ in range(w - 1 - len(text)):
            os.system(config['cls'])

            if config['halign']:
                print('\n' * h)

            print('-' * w)
            print('|' + ' ' * left_space + text + ' ' * right_space + '|')
            print('-' * w)

            if config['direction'] == 'left':
                left_space -= 1
                right_space += 1
            else:
                left_space += 1
                right_space -= 1

            sleep(config['move_speed'])
    except KeyboardInterrupt:
        print('\nOkay, my impatient friend')
        exit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        config['bubble'] = '--bubble' in sys.argv
        config['use_terminal_width'] = '--use-terminal-width' in sys.argv
        config['halign'] = '--halign' in sys.argv

        argv = list(filter(lambda flag: flag not in config['flags'], sys.argv))

        args_indexes = []

        for arg, var in [('--speed', 'move_speed'),
                         ('--first-position', 'direction'),
                         ('--hits', 'collision_retries'),
                         ('--field-len', 'default_field_len')]:
            if arg in argv:
                try:
                    arg_index = argv.index(arg)
                    config[var] = argv[arg_index + 1]

                    args_indexes += [arg_index]
                except IndexError:
                    print('[ERROR] Missing argument\'s value:', arg)

        if len(args_indexes) == 0:
            text = ' '.join(argv)
        else:
            text = ' '.join(argv[1:min(args_indexes)])

    else:
        text = input('Text> ')

    if config['collision_retries'] == 'inf':
        config['infinity_loop'] = True
        config['collision_retries'] = 2

    # convert these variables to int, because if they're given threw arguments, their type is string
    config['move_speed'], config['default_field_len'], config['collision_retries'] = \
        (float(config['move_speed']), int(config['default_field_len']), int(config['collision_retries']))

    if not config['bubble']:
        anim(text)
    else:
        if not config['infinity_loop']:
            for i in range(config['collision_retries']):
                anim(text)
                config['direction'] = 'right' if config['direction'] == 'left' else 'left'  # change direction
        else:
            while True:
                anim(text)
                config['direction'] = 'right' if config['direction'] == 'left' else 'left'  # change direction

