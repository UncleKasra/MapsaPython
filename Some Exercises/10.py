def f(a, b):
    n = range(len(a))
    c = [[0 for x in n]for x in n]
    for i in n:
        for j in n:
            for k in n:
                c[i][j] += a[i][k] * b[k][j]
    return c

a = [[1, 2], [10, 11]]
b = [[4, 5], [7, 8]]
print(f(a, b))
