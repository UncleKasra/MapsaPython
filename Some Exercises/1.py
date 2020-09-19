def kmm(a, b):
    return a*b/bmm(a, b)

def bmm(a, b):
    if a < b:
        a, b = b, a

    while b!=0:
        tmp = a % b
        a = b
        b = tmp

    return a

c = input('Enter two natural numbers (with space between): ')

a, b = (int(i) for i in c.split())

print(kmm(a, b))
