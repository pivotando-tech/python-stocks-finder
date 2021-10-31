from messages.criarArrayUsuario import userCarteiraInvest
from messages.welcome import welcome
from inputs.user import actionChoice

welcome()

if len(userCarteiraInvest) == 0:
    print('Não existe usuário')
else:
    actionChoice()
