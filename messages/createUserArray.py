from entities.user import User

createArrayUser = []


def createNewUser():
    userNameInput = str(input('Digite o nome do novo usuário: ')).strip().upper()
    newUser = User(name=userNameInput, wallet=[])
    createArrayUser.append(newUser)
