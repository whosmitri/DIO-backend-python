
# em python, tudo é objeto, dessa forma, funções também são objetos o que as tornam objetos da primeira classe. com isso, podemos atribuir funções ea variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures)

def add(a, b):
    return a + b

def display_result(a, b, function):
    result = function(a, b)
    print(f'The result of the operation {a} + {b} = {result}')

###

num1 = int(input('Enter a number: '))
num2 = int(input('Enter anothe number: '))

display_result(num1, num2, add)  # The result of the operation 10 + 10 = 20
