import json

youStocksMsg = 'Suas Ações'


def showWallet(userWallet):
    for stock in userWallet:
        parse = json.loads(stock)
        data = {
            'name': parse['name'],
            'price': parse['price'],
            'description': parse['description'],
            'update_at': parse['update_at']
        }
        print(f'''{'-' * 60}
Suas Ações: 
Name: {data['name']}
Price: R$ {data['price']}
Description: {data['description'][:90]}...
Last Update: {data['update_at']}
        ''')
