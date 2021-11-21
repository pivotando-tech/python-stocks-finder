from service.api import requestStock
from entities.stock import Stock

def searchStocksScreen():
    pesquisaAcoesMsg = input('Digite o código da ação desejada: ').strip().upper()
    teste = requestStock(pesquisaAcoesMsg)

    while teste == '':
        print('Aguarde...')



    infoStockes: [Stock] = [teste]
    for stock in infoStockes:
        print('{} - Preço atual:{} | Atualizado em:{}\nDescrição:{}...\n'.format(
            stock['results'][pesquisaAcoesMsg]['name'], stock['results'][pesquisaAcoesMsg]['price'],
            stock['results'][pesquisaAcoesMsg]['updated_at'], stock['results'][pesquisaAcoesMsg]['description'][:100]))
