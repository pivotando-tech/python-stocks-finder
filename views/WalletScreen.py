import json

from utils.userFileHandler import readFile

youStocksMsg = 'Suas Ações'
userInfo = readFile()
wallet = userInfo['wallet']


def showWallet():

    for stock in wallet:
        parse = json.loads(stock)
        data = {
            'name': parse['name'],
            'price': parse['price'],
            'description': parse['description'],
            'update_at': parse['update_at']
        }
        print(f'''{'-' * 60}
Name: {data['name']}
Price: R$ {data['price']}
Description: {data['description'][:90]}...
Last Update: {data['update_at']}
        ''')


def walletScreen():
    print(youStocksMsg)
    showWallet()
