def my_multiple(x, y):
    a = 0
    i = x
    while(i != 0):
        a += y
        if i > 0:
            i -= 1
        else:
            i += 1

    if ((y > 0) and (x < 0)) or ((y < 0) and (x < 0)) :
        a = -a

    return a



c = input('Enter two numbers (with space between): ')
x, y = (int(i) for i in c.split())
print(my_multiple(x, y))

