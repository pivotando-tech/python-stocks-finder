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


def showWallet():
    for stock in mockStocks:
        print('{} - Preço atual:{} | Descrição:{} | Atualizado em:{}'.format(
            stock['name'], stock['description'],
            stock['price'], stock['update_at']))