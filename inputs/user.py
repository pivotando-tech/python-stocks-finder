from messages import userMasages
from views.WalletScreen import walletScreen


def actionChoice():
    print(userMasages.viewWalletMsg, "digite [1]")
    print(userMasages.researchStocksMsg, "digite [2]")
    # TODO: Fazer uma verificação para só permitir o user digitar 1 ou 2 [Fazer verificação numa funcao externa]
    option = int(input('Opção: '))
    if option == 1:
        walletScreen()
    else:
        print("Levar para a tela de pesquisa de ações")
