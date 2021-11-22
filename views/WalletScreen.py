from utils.userFileHandler import readFile

youStocksMsg = 'Suas Ações'
wallet = readFile()
print(wallet['wallet'])

def showWallet():
    for stock in wallet['wallet']:
        # print('{} - Preço atual:{} | Descrição:{} | Atualizado em:{}'.format(
        #     stock['name'], stock['description'],
        #     stock['price'], stock['update_at']))
        print(stock)
def walletScreen():
    print(youStocksMsg)
    showWallet()
