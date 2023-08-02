import textwrap
from coresptbr import cores


def menu():
    opc = '''\n
    ============ MENU ============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [nu]\tNovo usuário
    [lc]\tListar contas
    [q]\tSair
    =>'''
    return input(textwrap.dedent(opc))


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


def exibir_extrato(saldo, /, *, extrato):
    print('\n============ EXTRATO ============')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(cores.colorir('\nJá exite usuario com esse CPF!', 'vm'))
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (longradouro, num - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print(cores.colorir('Usuário criado com sucesso!', 'vd'))


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(cores.colorir('Conta criada com sucesso!', 'vd'))
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print(cores.colorir('\nUsuário não encontrado, fluxo de criação de conta encerrado!', 'vm'))


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
            '''
        print('=' * 100)
        print(textwrap.dedent(linha))


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
                numero_saques=numero_saques,
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

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print(cores.colorir('Operação inválida! Por favor selecione novamente a operação desejada.', 'vm'))


main()
