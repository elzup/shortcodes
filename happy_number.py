import time
start = time.time()

l = lambda n: sum(map(lambda e: e * e, map(int, str(n))))
def HappyNumbers(m):
    c = [1]
    cli = []
    wli = []
    for a in range(2, m + 1):
        n = a
        li = []
        while n not in li:
            li += [n]
            n = l(n)
            if n == 1 or n in cli:
                cli = list(set(li + cli))
                c += [a]
                break
        wli = list(set(li + wli))
    return c

print(HappyNumbers(2000))
print(HappyNumbers(10))
print(str(time.time() - start) + "ms")
