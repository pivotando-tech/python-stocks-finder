
from messages.userMasages import sistemOptionMsg
from views.SearchStocksScreen import searchStocksScreen
from views.WalletScreen import walletScreen
from messages.valorinvalido import invalidOption
from time import sleep


def actionChoice():

    option = 0

    while option != 3:
        print(sistemOptionMsg)
        option = int(input('Qual sua opção: '))
        sleep(1)

        if option == 1:
            walletScreen()
            sleep(5)
        elif option == 2:
            searchStocksScreen()
            sleep(3)
        elif option == 3:
            print('Finalizando...')
            sleep(1)
        else:
            invalidOption()
            sleep(1)


