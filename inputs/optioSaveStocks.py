from messages.userMasages import optionSaveActionsMsg
from utils.userFileHandler import updateStockInWallet


def optionSaveStocks():
    saveAction = int(input(optionSaveActionsMsg))

    print(saveAction)
    if saveAction == 1:
        print('Salvando ação...')
        updateStockInWallet(name='test', description='test', price='13,4', update_at='13/11,2021')
