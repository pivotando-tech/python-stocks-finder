from inputs.searchInput import pesquisaAcoesMsg
from service.api import requestStock


def searchStocksScreen():
    teste = requestStock(pesquisaAcoesMsg)
    while teste != '':
        print('Aguarde...')
    print(teste)

