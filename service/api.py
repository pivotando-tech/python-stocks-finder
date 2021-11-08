import requests
from requests.exceptions import HTTPError
from service import strings

def requestStock(symbol: str):
    try:
        getStockInfo = requests.get(strings.baseUrl, params={'symbol': symbol})
        getStockInfo.raise_for_status()
        response = getStockInfo.json()

        return response

    except HTTPError as http_err:
        print(f'Http error: {http_err}')
    except Exception as err:
        print(f'Unexpected error: {err}')
