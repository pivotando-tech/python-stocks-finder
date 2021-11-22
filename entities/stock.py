class Stock(object):
    name = ''
    description = ''
    price = ''
    updated_at = ''

    def __init__(self, name, description, price, update_at):
        self.name = name
        self.description = description
        self.price = price
        self.update_at = update_at
