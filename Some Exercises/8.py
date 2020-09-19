# print(len('100'))

def f(n, d):
    r = []
    while(n > 1):
        r.append(n % 2)
        n = n // 2
    r.append(1)
    r = ''.join(map(str, r))
    b = r[::-1]

    if d > len(b):
        b = (d-len(b))*'0' + b

    return b
        
n = int(input('Enter a number: '))
d = int(input('Enter digits: '))
print(f(n, d))