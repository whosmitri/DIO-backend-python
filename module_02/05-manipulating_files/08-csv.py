import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

'''
try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['04', 'Miguel'])
        escritor.writerow(['02', 'Dmitri'])
except IOError as exc:
    print('Error opening file.')
    print(exc)
'''

'''
try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for i, row in enumerate(leitor):
            if (i == 0):
                continue
            print(f'ID: {row[COLUNA_ID]}')
            print(f'Nome: {row[COLUNA_NOME]}')
except IOError as exc:
    print('Error opening file.')
    print(exc)
'''


try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for row in leitor:
            print(f'ID: {row['id']}')
            print(f'Nome: {row['nome']}')
except IOError as exc:
    print('Error opening file.')
    print(exc)
