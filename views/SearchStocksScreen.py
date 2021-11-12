from service.api import requestStock


def searchStocksScreen():
    pesquisaAcoesMsg = input('Digite o código da ação desejada: ').strip().upper()
    teste = requestStock(pesquisaAcoesMsg)

    while teste == '':
        print('Aguarde...')
    print(teste)