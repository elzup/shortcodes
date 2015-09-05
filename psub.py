def pSub(X):
    c = 0
    for i in range(1, len(X) + 1):
        for j in range(len(X) + 1 - i):
            if r(X[j: j + i]):
                c += 1
    return c

r = lambda p: p[:-~len(p) / 2] == p[len(p) / 2:][::-1]

print(pSub('abaaac'))
