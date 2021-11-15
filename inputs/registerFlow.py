from inputs.selectScreens import actionChoice
from messages.userMasages import forRegisterMsg, forSkipRegistrationMsg, invalidChoiceMsg
from views.createUser import createNewUser

formattedMsg = f'''
{forRegisterMsg}: [1]
{forSkipRegistrationMsg}: [2]
Sua opção: '''

def registerFlow():
    userChoice = ''

    while userChoice != '1' and userChoice != '2':
        userChoice = str(input(formattedMsg))

        if userChoice == '1':
            newUser = createNewUser()
            actionChoice(newUser.name)
        elif userChoice == '2':
            actionChoice()
        else:
            print(invalidChoiceMsg)
