from messages.userMasages import optioSaveActionsMsg
from inputs.selectScreens import actionChoice
from views.SearchStocksScreen import searchStocksScreen


def optionSaveStocks():
    saveAction = int(input(optioSaveActionsMsg))
    if saveAction == 1:
        print('Salvar ação!!')
    else:
        searchStocksScreen()
