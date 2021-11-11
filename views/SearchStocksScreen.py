from service.api import requestStock
from inputs.optioSaveAction import OptionSaveAction


def searchStocksScreen():
    pesquisaAcoesMsg = input('Digite o código da ação desejada: ').strip().upper()
    teste = requestStock(pesquisaAcoesMsg)
    saveAction = ''
    while teste == '':
        print('Aguarde...')
    print(teste)
