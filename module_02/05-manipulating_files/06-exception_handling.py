from pathlib import Path

# just:
# file = open('my_file.txt')
# return the error "FileNotFoundError"

try:
    file = open('my_file.txt')
except FileNotFoundError as exc:
    print('File not found.')
    print(exc)

ROOT_PATH = Path(__file__).parent

try:
    file = open(ROOT_PATH/'05-new_dir')
except IsADirectoryError as exc:
    print(f'This file is a directory.')
    print(exc)
except PermissionError as exc:
    print(f'The file could not be opened.')
    print(exc)
except Exception as exc:
    print(f'An error ocurred while trying to open the file: {exc}')