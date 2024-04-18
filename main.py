import keyboard as kbd

dct = {}

try:
    with open('saves.txt', 'r') as file:
        print('Сохранения были найдены!')
        for string in file:
            temp_lst = string.split('_')
            key, value = temp_lst[0], int(temp_lst[1])
            dct[key] = value

except FileNotFoundError:
    with open('saves.txt', 'w') as file:
        print('Сохранения не найдены! Выставляем по умолчанию ( •̀ ω •́ )y')
        dct = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '0': 0,
            'space': 0,
            'enter': 0,
            'tab': 0,
            'alt': 0,
            'ctrl': 0,
            'shift': 0,
            'backspace': 0,
            'right alt': 0,
            'right ctrl': 0,
            'right shift': 0,
            'esc': 0,
            'f1': 0,
            'f2': 0,
            'f3': 0,
            'f4': 0,
            'f5': 0,
            'f6': 0,
            'f7': 0,
            'f8': 0,
            'f9': 0,
            'f10': 0,
            'f11': 0,
            'f12': 0,
            'caps lock': 0,
            '[': 0,
            ']': 0,
            ';': 0,
            "'": 0,
            ',': 0,
            '.': 0,
            '/': 0,
            '-': 0,
            '=': 0,
            '`': 0,
            'left windows': 0,
            'insert': 0,
            'home': 0,
            'page up': 0,
            'delete': 0,
            'end': 0,
            'page down': 0,
            'print screen': 0,
            'scroll lock': 0,  # SL
            'pause': 0,  # PB
            'up': 0,  # arrow
            'left': 0,  # arrow
            'down': 0,  # arrow
            'right': 0  # arrow
        }


def onPress(key):
    name = key.name

    if name == 'й':
        dct['q'] += 1

    elif name == 'ц':
        dct['w'] += 1

    elif name == 'у':
        dct['e'] += 1

    elif name == 'к':
        dct['r'] += 1

    elif name == 'е':
        dct['t'] += 1

    elif name == 'н':
        dct['y'] += 1

    elif name == 'г':
        dct['u'] += 1

    elif name == 'ш':
        dct['i'] += 1

    elif name == 'щ':
        dct['o'] += 1

    elif name == 'з':
        dct['p'] += 1

    elif name == 'х':
        dct['['] += 1

    elif name == 'ъ':
        dct[']'] += 1

    elif name == 'ф':
        dct['a'] += 1

    elif name == 'ы':
        dct['s'] += 1

    elif name == 'в':
        dct['d'] += 1

    elif name == 'а':
        dct['f'] += 1

    elif name == 'п':
        dct['g'] += 1

    elif name == 'р':
        dct['h'] += 1

    elif name == 'о':
        dct['j'] += 1

    elif name == 'л':
        dct['k'] += 1

    elif name == 'д':
        dct['l'] += 1

    elif name == 'ж':
        dct[';'] += 1

    elif name == 'э':
        dct["'"] += 1

    elif name == 'я':
        dct['z'] += 1

    elif name == 'ч':
        dct['x'] += 1

    elif name == 'с':
        dct['c'] += 1

    elif name == 'м':
        dct['v'] += 1

    elif name == 'и':
        dct['b'] += 1

    elif name == 'т':
        dct['n'] += 1

    elif name == 'ь':
        dct['m'] += 1

    elif name == 'б':
        dct[','] += 1

    elif name == 'ю':
        dct['.'] += 1

    elif name == '.':
        dct['/'] += 1

    elif name == 'ё':
        dct['`'] += 1

    else:
        dct[name] += 1


def printDictionary(dct):
    for key, value in dct.items():
        print(f"{key}: {value}")


print('Ведётся запись...\n')

kbd.on_press(onPress)

kbd.wait('esc')

printDictionary(dct)

with open('options.txt', 'w') as file:
    print('\nСохранение! Пожалуйста, подождите (_　_)。゜zｚＺ')

    for key, value in dct.items():
        file.write(f'{key}_{value}\n')

    print('Сохранения были успешно сохранены!(✿◡‿◡)')