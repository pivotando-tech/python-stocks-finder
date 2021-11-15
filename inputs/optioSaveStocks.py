from messages.userMasages import optionSaveActionsMsg


def optionSaveStocks():
    saveAction = int(input(optionSaveActionsMsg))

    print(saveAction)
    if saveAction == 1:
        print('Salvando ação...')
