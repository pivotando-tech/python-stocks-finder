import uuid


class User(object):
    id = uuid.uuid4()
    name = ''
    wallet = []

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


def makeUser(name, wallet):
    user = User(name, wallet)
    return user
