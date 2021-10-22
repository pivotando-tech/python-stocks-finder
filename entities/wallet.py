
class Wallet(object):
    ownerName = ''
    stocks = []

    def __init__(self, ownerName, stocks):
        self.ownerName = ownerName
        self.stocks = stocks
