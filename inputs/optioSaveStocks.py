from messages.userMasages import optioSaveActionsMsg


def optionSaveStocks():
    saveAction = int(input(optioSaveActionsMsg))

    print(saveAction)
    if saveAction == 1:
        print('Salvando ação...')
