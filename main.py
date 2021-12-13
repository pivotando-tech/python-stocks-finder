from inputs.registerFlow import registerFlow
from utils.userFileHandler import readFile
from views.createUser import userArray
from messages.welcome import welcome
from messages.userMasages import wantsToRegisterNewUserMsg
from inputs.selectScreens import actionChoice

welcome()

if len(userArray) == 0:
    print(wantsToRegisterNewUserMsg)

    registerFlow()

else:
    user = readFile()

    actionChoice(userName=user['name'])
