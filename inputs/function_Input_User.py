from views.WalletScreen import walletScreen
from messages.erroOption import invalidOption


def opcaoUser():
    while option != 1 and option != 2:
        option = int(input('Opção: '))

        if option == 1:
            walletScreen()
        elif option == 2:
            print("Levar para a tela de pesquisa de ações")
        else:
            invalidOption()




