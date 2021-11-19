from utils.userFileHandler import createUserIntoFile

userArray = []


def createNewUser():
    userNameInput = str(input('Digite o nome do novo usuário: ')).strip()
    newUser = createUserIntoFile(userNameInput)
    userArray.append(newUser)
    return newUser
