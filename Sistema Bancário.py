print('-=' * 10)
print(f'{"BANCO BRASUL":^20}')
print('-=' * 10)

menu = '''
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0

while True:

    opcao = int(input(menu))

    if opcao == 1:

        deposito = float(input('Digite o valor do deposito: R$'))

        if deposito > 0:
            saldo += deposito
            extrato += f'Deposito: R${deposito:.2f}\n'

        else:
            print('Operação invalida! valor o valor informado é invalido.')

    elif opcao == 2:

        if numero_saques < 3:

            saque = float(input('Digite o valor que deseja sacar: R$'))

            if saque <= limite and saque <= saldo:
                extrato += f'Saque: R${saque:.2f}\n'
                numero_saques += 1
                saldo -= saque

            elif saque > limite:
                print('Operação invalida! você excedeu o limite de saque.')

            else:
                print('Operação invalida! saldo insuficiente.')

        elif numero_saques >= 3:
            print(f'Operaçao invalida! número maximo de saques excedido.')

    elif opcao == 3:
        print(f'\n{"=" * 15} EXTRATO {"=" * 15}')
        print('Não foram realizadas movimentações.\n' if not extrato else extrato)
        print(f'Saldo: R${saldo}')
        print('=' * 39)
    elif opcao == 4:
        break

    else:
        print('Opção invalida! por favor selecione a opção novamente. ')
