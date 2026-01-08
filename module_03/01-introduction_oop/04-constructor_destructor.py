
class Cachorro():
    def __init__(self, nome):
        print('iniciando...')
        self.nome = nome
    
    def falar(self):
        print('auau')
    
    def __del__(self):
        print('Destruindo a instância')


c = Cachorro('choi')
c.falar()

print('omg hi')

del c

print('omg hi')
print('omg hi')
print('omg hi')
