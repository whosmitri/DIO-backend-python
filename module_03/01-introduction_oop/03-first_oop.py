
class Patins():
    def __init__(self, cor, modelo, rolamento, valor):
        self.cor = cor
        self.modelo = modelo
        self.rolamento = rolamento
        self.valor = valor

    def correr(self):
        print('correndo')

    def parar(self):
        print('patins parando')
        print('parou !!')

    # def __str__(self):
    #    return f'Patins \nCor: {self.cor} \nModelo: {self.modelo} \nRolamento{self.rolamento} \nValor: {self.valor}'

    def __str__(self):
        return f'{self.__class__.__name__}: \n{"\n".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

patins1 = Patins('branco', 'traxart revolt', 'abec-9', 799.00)
patins2 = Patins('titanium', 'traxart volt +2.0', 'abec-9', 899.00)

patins1.correr()
patins1.parar()
print(patins1.cor, patins1.modelo, patins1.rolamento, patins1.valor)
print(patins1)

print(patins2.cor, patins2.modelo, patins2.rolamento, patins2.valor)