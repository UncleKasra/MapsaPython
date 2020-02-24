
s=[]

def hanoi(n, a, b, c):
    if n == 1:
        s.append(a + ' -> ' + c)
    else:
        hanoi(n-1, a, c, b)
        s.append(a + ' -> ' + c)
        hanoi(n-1, b, a, c)
    

n = int(input('Enter number of disks: '))
a = input('Enter the name of rod that disks are in it now: ')
c = input('Enter the name of rod that disks should go to it: ')
b = input('Enter the name of helper rod: ')

hanoi(n, a, b, c)
# print(s)
print("\n".join(s))