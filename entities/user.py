import uuid


class User(object):
    id = ''
    name = ''
    wallet = []

    def __init__(self, name, wallet):
        self.id = uuid.uuid4()
        self.name = name
        self.wallet = wallet


def makeUser(name, wallet):
    user = User(name, wallet)
    return user
