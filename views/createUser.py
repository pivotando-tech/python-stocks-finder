from utils.userFileHandler import createUserIntoFile, readFile

user = readFile()

if user['name'] != '':
    userArray = [user]


def createNewUser():
    userNameInput = str(input('Digite o nome do novo usuário: ')).strip()
    newUser = createUserIntoFile(userNameInput)
    userArray.append(newUser)
    return newUser
