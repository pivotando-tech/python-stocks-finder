from service.api import requestStock
from entities.stock import Stock

def searchStocksScreen():
    pesquisaAcoesMsg = input('Digite o código da ação desejada: ').strip().upper()
    teste = requestStock(pesquisaAcoesMsg)

    while teste == '':
        print('Aguarde...')
    print(teste)

    infoStockes: [Stock] = [teste]
    for stock in infoStockes:
        print('{} - Preço atual:{} | Descrição:{} | Atualizado em:{}'.format(
            stock['name'], stock['description'],
            stock['price'], stock['update_at']))
