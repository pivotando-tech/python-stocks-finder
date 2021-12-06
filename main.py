from inputs.registerFlow import registerFlow
from utils.userFileHandler import readFile
from messages.welcome import welcome
from messages.userMasages import wantsToRegisterNewUserMsg
from inputs.selectScreens import actionChoice

welcome()

user = readFile()


if user['name'] == 'provisory':
    print(wantsToRegisterNewUserMsg)
    registerFlow()

else:
    actionChoice(userName=user['name'])


# todo: [FILIPE] - make async function to write data before check if user exists