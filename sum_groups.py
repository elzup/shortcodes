
def SumGroups(a):
    while 1:
        b = []
        p = 3
        for v in a:
            t = v % 2
            if p == t:
                b[-1] += t
                continue
            b += [t]
            p = t
        if a == b:
            break
        a = b
    return len(a)

print(SumGroups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]))
print(SumGroups([2,1,2,2,6,5,0,2,0,3,3,3,9,2]))

