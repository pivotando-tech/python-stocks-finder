from entities.user import makeUser

newUser = makeUser('Berg', [1234])
segUser = makeUser('Filipe', [4321])
print(newUser.id)
print(segUser.id)