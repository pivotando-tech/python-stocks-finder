import json

from inputs.optioSaveStocks import optionSaveStocks
from utils.userFileHandler import readFile
from views.SearchStocksScreen import searchStocksScreen


def stockInfoAndOptions():
    stockSearched = searchStocksScreen()
    userInput = stockSearched['name']
    userWallet = readFile().get('wallet')
    for name in userWallet:
        parse = json.loads(name)
        stock = parse['name']
        if userInput in stock:
            print('Está ação já está salva em sua carteira')
            break
        else:
            optionSaveStocks(stockSearched)
