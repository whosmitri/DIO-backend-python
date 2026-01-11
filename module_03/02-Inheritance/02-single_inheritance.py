
class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('ligando motor...')

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado=False):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'sim, ' if self.carregado else 'não'} estou carregado')

###

moto = Motocicleta('vermelho', 'DMT-2402', 2)
moto.ligar_motor()

caminhao = Caminhao('amarelo', 'abc-1234', 8, carregado=True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)