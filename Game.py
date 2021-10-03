import random
def Game(Computer, You):
    if Computer==You:
        return None
    elif Computer=='s':
        if You=='p':
            return True
        if You=='sc':
            return False
    elif Computer=='p':
        if You=='s':
            return False
        if You=='sc':
            return True
    elif Computer=='sc':
        if You=='s':
            return True
        if You=='p':
            return False
print('Computer turn Stone(s), Paper(p), Scissor(sc)')
randno=random.randint(1,3)
if randno==1:
    Computer='s'
elif randno==2:
    Computer='p'
elif randno==3:
    Computer='sc'
You=input('Your turn Stone(s), Paper(p), Scissor(sc)\n')
a=Game(Computer,You)
print(f'computer chose {Computer}')
print(f'you chose {You}')
if a==None:
    print('Game is tie')
elif a:
    print('Congratulations! You Win')
else:
    print('You Lost')

