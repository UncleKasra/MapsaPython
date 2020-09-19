tmp = set()

zlst = [[]]

def zir(lst, n):
    for j in lst:
        tmp.add(j)
        if n > 0:
            zir([item for item in lst if item not in list(tmp)], n-1)
        else:
            if tmp not in zlst:
                zlst.append(tmp.copy())
        tmp.remove(j)


def f(lst):
    
    for i in range(len(lst)):

        zir(lst, i)
        tmp.clear()
    return zlst



lst = [1, 2, 3, 4]
zlist = f(lst)

for k in range(len(zlist)):
    zlist[k] = list(zlist[k])



print(zlist)

