from messages.userMasages import systemOptionMsg
from messages.valorinvalido import invalidOption
from utils.userFileHandler import readFile
from views.WalletScreen import showWallet
from views.showStocksInfo import stockInfoAndOptions
from time import sleep


def showAllOptions(option):
    while option != '3':
        print(systemOptionMsg)
        option = str(input('Qual sua opção: '))
        sleep(1)

        if option == '1':
            updateWallet = readFile().get('wallet')
            if len(updateWallet) != 0:
                showWallet(updateWallet)
                sleep(3)
        elif option == '2':
            stockInfoAndOptions()
            sleep(3)
        elif option == '3':
            print('Finalizando...')
            sleep(1)
        else:
            invalidOption()
            sleep(1)
