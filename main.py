from messages.createUserArray import createArrayUser
from messages.welcome import welcome
from inputs.user import actionChoice

welcome()

if len(createArrayUser) != 0:
    print('Não existe usuário')
else:
    actionChoice()
