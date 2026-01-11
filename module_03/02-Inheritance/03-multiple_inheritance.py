
class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f'{self.__class__.__name__}: \n{"\n".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class FalarMixin:
    def falar(self):
        return('oi, estou falando !!')

class Lobo(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, num_patas):
        # print(Ornitorrinco.__mro__)
        # print(Ornitorrinco.mro())

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, num_patas=num_patas)

lobo = Lobo(num_patas=4, cor_pelo='branco')
print(lobo)

print('###')

ornitorrinco = Ornitorrinco(num_patas=4, cor_pelo='marrom', cor_bico='laranja')
print(ornitorrinco)
print(ornitorrinco.falar())