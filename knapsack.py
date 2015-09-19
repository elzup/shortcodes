
def Superincreasing_knapsack_problem(m, N, w):
    s = [0 for i in range(m + 1)]
    o = s[:]
    o[0] = 1
    r = 0
    for i in w:
        for p, v in enumerate(o):
            if v == 0:
                continue
            s[p] = 1
            k = p + i
            if k <= m:
                s[k] = 1
                r = max(r, k)
        o = s[:]
    return r

print(Superincreasing_knapsack_problem(10, 3, [5, 3, 1]))
print(Superincreasing_knapsack_problem(10, 4, [10, 5, 3, 1]))
