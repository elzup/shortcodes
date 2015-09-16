
def divideFactorial(X, Y):
    def divs(n):
        ds = {}
        res = {}
        m = n
        for i in range(2, n + 1):
            while m > 0 and m % i == 0:
                if i not in ds:
                    ds[i] = 0
                    res[i] = 0
                ds[i] += 1
                m /= i
        return ds, res

    k = 0
    ds, res = divs(X)

    i = 1
    while True:
        i += 1
        ms, z = divs(i)
        # for k, v in ms.iteritems():
        #     if k in res:
        #         res[k] += v
        t = True
        for k, v in ds.iteritems():
            p = i
            while v * Y > res[k] and p % k == 0:
                res[k] += 1
                p /= k
            if v * Y > res[k]:
                t = False
        if t:
            break
    return i

# print(divideFactorial(2, 2))
# print(divideFactorial(2, 3))
print(divideFactorial(1000000000, 30000))
