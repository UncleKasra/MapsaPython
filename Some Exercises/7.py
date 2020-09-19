import random

def f():
    w = 0
    r = random.randint(1, 30)
    for i in range(1, 6):
        g = int(input('guess a number: '))
        if g == r:
            w = 1
            break
    if w == 1:
        print('You win!')
    else:
        print('gameOver')

f()