from time import sleep

from utils.userFileHandler import createUserIntoFile, readFile
userArray = []
user = readFile()
test = createUserIntoFile('provisory')

if user['name'] != '':
    userArray.append(test)


def createNewUser():
    userNameInput = str(input('Digite o nome do novo usuário: ')).strip()
    newUser = createUserIntoFile(userNameInput)
    userArray.append(newUser)
    return newUser
