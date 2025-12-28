
# using read()
file = open('module_02/05-manipulating_files/03-lorem.txt')
print(file.read())
file.close()

print('\n### \n')

# using readline()
file = open('module_02/05-manipulating_files/03-lorem.txt')
print(file.readline())
file.close()

print('\n### \n')

# tip: using readline() with iterator
file = open('module_02/05-manipulating_files/03-lorem.txt')
while len(linha := file.readline()):
    print(linha)
file.close()

print('\n### \n')

# using readlines()
file = open('module_02/05-manipulating_files/03-lorem.txt')
print(file.readlines())
file.close()