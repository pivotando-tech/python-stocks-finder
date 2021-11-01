from entities.stock import Stock
from entities.user import User


class Wallet(object):
    ownerName: User.name = ''
    stocks: [Stock] = []

    def __init__(self, ownerName, stocks):
        self.ownerName = ownerName
        self.stocks = stocks
