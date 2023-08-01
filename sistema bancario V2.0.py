import textwrap
from coresptbr import cores

def menu():
    menu = '''\n
    ============ MENU ============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    =>'''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print(cores.colorir('Deposósito realizado com sucesso!', 'vd'))
    else:
        print(cores.colorir('Operação falhou! O valor informado é inválido.', 'vm'))
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(cores.colorir('\n Operação falhou! Você não tem saldo suficiente.', 'vm'))

    elif excedeu_limite:
        print(cores.colorir('\n Operação falhou! O valor do saque excede o limite.', 'vm'))

    elif excedeu_saques:
        print(cores.colorir('\n Operação falhou! Número máximo de saques excedido. , vm'))

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print(cores.colorir('\nSaque realizado com sucesso!', 'vd'))

    else:
        print(cores.colorir('\nOperação falhou! O valor informado é inválido.', 'vm'))

    return saldo, extrato

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: R$'))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: R$'))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
