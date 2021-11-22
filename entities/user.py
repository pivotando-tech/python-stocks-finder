import uuid


class User(object):
    id = ''
    name = ''
    wallet = []

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.wallet = []


def makeUser(name):
    user = User(name)
    return user
