from views.showStocksInfo import stockInfoAndOptions
from messages.userMasages import systemOptionMsg
from views.WalletScreen import walletScreen
from messages.valorinvalido import invalidOption
from time import sleep


def actionChoice(userName: str = ''):
    print(f'''Olá {userName}
    ''')

    option = ''

    while option != '3':
        print(systemOptionMsg)
        option = str(input('Qual sua opção: '))
        sleep(1)

        if option == '1':
            walletScreen()
            sleep(5)
        elif option == '2':
            stockInfoAndOptions()
            sleep(3)
        elif option == '3':
            print('Finalizando...')
            sleep(1)
        else:
            invalidOption()
            sleep(1)


