from masagens import userMasages


def actionChoice():
    print(userMasages.viewWalletMsg, "digite [1]")
    print(userMasages.researchStocksMsg, "digite [2]")
    option = int(input('Opção: '))
    if option == 1:
        print("levar para a tela de visualizar carteira")
    else:
        print("Levar para a tela de pesquisa de ações")

