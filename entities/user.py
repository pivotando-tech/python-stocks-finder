import uuid
from inputs import createUserInput

class User(object):
    id = ''
    name = createUserInput
    wallet = []

    def __init__(self, name, wallet):
        self.id = uuid.uuid4()
        self.name = name
        self.wallet = wallet


def makeUser(name, wallet):
    user = User(name, wallet)
    return user
