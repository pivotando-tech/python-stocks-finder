from entities.user import User

userArray = []


def createNewUser():
    userNameInput = str(input('Digite o nome do novo usuário: ')).strip()
    newUser = User(name=userNameInput, wallet=[])
    userArray.append(newUser)
    return newUser
