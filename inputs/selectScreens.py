from utils.userFileHandler import readFile
from views.showStocksInfo import stockInfoAndOptions
from messages.userMasages import systemOptionMsg, systemOptionMsgWithOutStock
from views.WalletScreen import walletScreen
from messages.valorinvalido import invalidOption
from time import sleep


def actionChoice(userName: str = ''):
    print(f'''Olá {userName}
    ''')

    option = ''

    infoWallet = readFile().get('wallet')
    if len(infoWallet) != 0:


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

    else:
        while option != '2':
            print(systemOptionMsgWithOutStock)
            option = str(input('Qual sua opção: '))
            sleep(1)

            if option == '1':
                stockInfoAndOptions()
                sleep(3)
            elif option == '2':
                print('Finalizando...')
                sleep(1)
            else:
                invalidOption()
                sleep(1)
