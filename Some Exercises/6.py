def f(le, he):
    print((he-1)*' ' + le*'*')

    for i in range(2, he):
        print((he-i)*' ' + '*' + (le-2)*' ' + '*')

    print(le*'*')

le = int(input('Enter length: '))
he = int(input('Enter heigth: '))
f(le, he)