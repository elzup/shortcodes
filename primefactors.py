def primefactors(n):
    k = []
    for i in range(2, n + 1):
        while n % i == 0:
            k.append(i)
            n /= i
    return "*".join(map(str, k))

print(primefactors(22))
print(primefactors(120))
print(primefactors(17194016))

def primefactors(n):
    k = []
    for i in range(2, n + 1):
        while n % i == 0:
            k.append(i)
            n /= i

