from entities.stock import Stock

mockStocks: [Stock] = [
    {
        'name': "Méliuz S.A.",
        'description': "Portal Virtual Para Veiculação E Divulgação de Marcas. Produtos E Outros Materiais.",
        'price': "3.31",
        'update_at': '2021-10-30'
    },
    {
        'name': "Méliuz S.A.",
        'description': "Portal Virtual Para Veiculação E Divulgação de Marcas. Produtos E Outros Materiais.",
        'price': "3.31",
        'update_at': '2021-10-30'
    },
    {
        'name': "Méliuz S.A.",
        'description': "Portal Virtual Para Veiculação E Divulgação de Marcas. Produtos E Outros Materiais.",
        'price': "3.31",
        'update_at': '2021-10-30'
    },
    {
        'name': "Méliuz S.A.",
        'description': "Portal Virtual Para Veiculação E Divulgação de Marcas. Produtos E Outros Materiais.",
        'price': "3.31",
        'update_at': '2021-10-30'
    },
    {
        'name': "Méliuz S.A.",
        'description': "Portal Virtual Para Veiculação E Divulgação de Marcas. Produtos E Outros Materiais.",
        'price': "3.31",
        'update_at': '2021-10-30'
    },
]


# TODO: bb: Verificar a melhor forma de fazer a concatenacao da string.

def showWallet():
    for stock in mockStocks:
        print(stock['name'], '- Preço atual:', stock['price'], '| Descrição: ', stock['description'],
              '| Atualizado em: ', stock['update_at'])
