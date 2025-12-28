
file = open('module_02/05-manipulating_files/04-test.txt', 'w')

file.write('escrevendo dados em um novo arquivo')

file.writelines(['\n', 'escrevendo', '\n', 'um', '\n', 'novo', '\n', 'texto'])

file.close()