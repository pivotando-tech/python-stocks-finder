import json

from entities.stock import Stock
from entities.user import User

filePath = '.././userData.json'


def readFile():
    with open(filePath) as json_file:
        data = json.load(json_file)
        return data


def updateFile(key, data):
    with open(filePath, 'r+') as file:
        fileData = json.load(file)
        fileData[key].append(data)
        file.seek(0)
        json.dump(fileData, file, indent=4)


def updateStockInWallet(name, description, price, update_at):
    stockInfo = Stock(name=name, description=description, price=price, update_at=update_at)
    convertedObj = json.dumps(stockInfo.__dict__)

    updateFile('wallet', convertedObj)


def createUserIntoFile(userName):
    userInfo = User(name=userName)

    with open(filePath, 'r+', encoding='utf-8') as file:
        convertedObj = json.dumps(userInfo.__dict__)
        handleJson = json.loads(convertedObj)
        file.seek(0)
        file.write(json.dumps(handleJson))
        file.truncate()


createUserIntoFile('Estevão Ferreira')

# updateStockInWallet(name='test', description='test', price='13,4', update_at='13/11,2021')
