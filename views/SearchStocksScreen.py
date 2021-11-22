from service.api import requestStock


def searchStocksScreen():
    pesquisaAcoesMsg = input('Digite o código da ação desejada: ').strip().upper()
    stock = requestStock(pesquisaAcoesMsg)

    while stock == '':
        print('Aguarde...')
    print(stock)
    formattedStock = stock['results'][pesquisaAcoesMsg]
    return formattedStock
