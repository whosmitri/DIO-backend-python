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

def depositar(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Valor depositado: {valor} \nSaldo atual: {saldo}')
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

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

def exibir_extrato(saldo, /, *, extrato):
    print('\n========== EXTRATO')
    if (extrato):
        print(extrato)
    else:
        print('Não foram realizadas movimentações.')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Digite seu CPF (somente números): ')
    validar_usuario = filtrar_usuario(cpf, usuarios)

    if (validar_usuario):
        print('\n Já existe um usuário com esse CPF!')
        return False
    
    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento (dd-mm-aaaa): ')
    
    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf})

    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    for user in usuarios:
        if (user['cpf'] == cpf):
            return user
        else:
            return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite seu CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if (usuario):
        print('Conta criada com sucesso!')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print('Usuário não encontrado, criação de conta encerrada')

def listar_contas(contas):
    print('========== CONTAS')
    for index, conta in enumerate(contas):
        print(f'{index} - Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}')

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = '001'

    while True:

        print(menu())
        opcao = int(input('Digite aqui: '))

        if (opcao == 1):
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif (opcao == 2):
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)


        elif (opcao == 3):
            exibir_extrato(saldo, extrato=extrato)
        
        elif (opcao == 4):
            criar_usuario(usuarios)

        elif (opcao == 5):
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if (conta):
                contas.append(conta)

        elif (opcao == 6):
            listar_contas(contas)

        elif (opcao == 0):
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()