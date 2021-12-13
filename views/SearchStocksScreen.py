from service.api import requestStock


def searchStocksScreen():
    pesquisaAcoesMsg = input('Digite o código da ação desejada: ').strip().upper()
    stock = requestStock(pesquisaAcoesMsg)

    while stock == '':
        print('Aguarde...')
    formattedStock = stock['results'][pesquisaAcoesMsg]


    print(f'''{'-' * 60}
    Name: {formattedStock['name']}
    Price: R$ {formattedStock['price']}
    Description: {formattedStock['description'][:90]}...
    Last Update: {formattedStock['updated_at']}
            ''')
    return formattedStock
