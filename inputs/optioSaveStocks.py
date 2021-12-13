from messages.userMasages import optionSaveActionsMsg
from utils.userFileHandler import updateStockInWallet


def optionSaveStocks(stockInfo):
    saveAction = int(input(optionSaveActionsMsg))

    print(saveAction)

    if saveAction == 1:
        print('Salvando ação...')
        updateStockInWallet(
            name=stockInfo['name'],
            description=stockInfo['description'],
            price=stockInfo['price'],
            update_at=stockInfo['updated_at']
        )



