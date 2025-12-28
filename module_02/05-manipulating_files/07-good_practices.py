from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/'lorem.txt', 'r') as file:
        print(file.read())
except IOError as exc:
    print('Error opening file.')
    print(exc)

'''
try:
    with open(ROOT_PATH/'07-utf8_file.txt', 'w', encoding='utf8') as file:
        file.write('Learning to manipulate files using Python')
except IOError as exc:
    print('Error opening file.')
    print(exc)
'''

try:
    with open(ROOT_PATH/'07-utf8_file.txt', 'r', encoding='ascii') as file:
        print(file.read())
except IOError as exc:
    print('Error opening file.')
    print(exc)
except UnicodeDecodeError as exc:
    print(exc)
