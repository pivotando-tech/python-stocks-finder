from messages import userMasages
from views.SearchStocksScreen import searchStocksScreen
from views.WalletScreen import walletScreen
from messages.valorinvalido import invalidOption


def actionChoice():

    print(userMasages.viewWalletMsg, "digite [1]")
    print(userMasages.researchStocksMsg, "digite [2]")

    option = 0

    while option != 1 and option != 2:
        option = int(input('Opção: '))

        if option == 1:
            walletScreen()
        elif option == 2:
            searchStocksScreen()
        else:
            invalidOption()

