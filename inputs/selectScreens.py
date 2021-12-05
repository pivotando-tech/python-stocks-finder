from utils.userFileHandler import readFile
from views.allUserOptions import showAllOptions
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

        showAllOptions(option)
    else:

        while option != '2':
            print(systemOptionMsgWithOutStock)
            option = str(input('Qual sua opção: '))
            sleep(1)

            if option == '1':
                stockInfoAndOptions()
                sleep(3)
                updateWallet = readFile().get('wallet')

                if len(updateWallet) != 0:
                    showAllOptions(option)

            elif option == '2':
                print('Finalizando...')
                sleep(1)
            else:
                invalidOption()
                sleep(1)
