from inputs.optioSaveStocks import optionSaveStocks
from views.SearchStocksScreen import searchStocksScreen


def stockInfoAndOptions():
    stockSearched = searchStocksScreen()
    optionSaveStocks(stockSearched)
