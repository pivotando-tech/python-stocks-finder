from messages.userMasages import optioSaveActionsMsg
from views.SearchStocksScreen import searchStocksScreen


def optionSaveStocks():
    saveAction = int(input(optioSaveActionsMsg))

    print(saveAction)
    if saveAction == 1:
        print('Salvar ação!!')
    else:
        searchStocksScreen()
