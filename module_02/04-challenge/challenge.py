import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class ContaIterador():
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f'''\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        '''
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''

class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (tipo_transacao is None) or (transacao['tipo'].lower() == tipo_transacao.lower()):
                yield transacao
    
    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao['data'], '%d-%m-%Y %H:%M:%S').date()
            if (data_atual == data_transacao):
                transacoes.append(transacao)
        return transacoes

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope

def menu():

    menu = """\n
    ============ MENU ============
    [0] Sair
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta Corrente
    [6] Listar Contas
    ==============================
    """
    return menu


def filtrar_cliente(cpf, usuarios):
    for user in usuarios:
        if (user['cpf'] == cpf):
            return user
        else:
            return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\nCliente não possui conta!')
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

@log_transacao
def depositar(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Valor depositado: {valor} \nSaldo atual: {saldo}')
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

@log_transacao
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f'Valor sacado: {valor} \nSaldo atual: {saldo}')

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

@log_transacao
def exibir_extrato(saldo, /, *, extrato):
    print('\n========== EXTRATO')
    if (extrato):
        print(extrato)
    else:
        print('Não foram realizadas movimentações.')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')

@log_transacao
def criar_cliente(usuarios):
    cpf = input('Digite seu CPF (somente números): ')
    validar_usuario = filtrar_cliente(cpf, usuarios)

    if (validar_usuario):
        print('\n Já existe um usuário com esse CPF!')
        return False
    
    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento (dd-mm-aaaa): ')
    
    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf})

    print('Usuário criado com sucesso!')

@log_transacao
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite seu CPF (somente números): ')
    usuario = filtrar_cliente(cpf, usuarios)

    if (usuario):
        print('Conta criada com sucesso!')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print('Usuário não encontrado, criação de conta encerrada')

def listar_contas(contas):
    print('========== CONTAS')
    for index, conta in enumerate(contas):
        print(f'{index} - Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}')

def main():

    clientes = []
    contas = []

    while True:

        print(menu())
        opcao = int(input('Digite aqui: '))

        if (opcao == 1):
            depositar(clientes)

        elif (opcao == 2):
            sacar(clientes)

        elif (opcao == 3):
            exibir_extrato(clientes)
        
        elif (opcao == 4):
            criar_cliente(clientes)

        elif (opcao == 5):
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif (opcao == 6):
            listar_contas(contas)

        elif (opcao == 0):
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()