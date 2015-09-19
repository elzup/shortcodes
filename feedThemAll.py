import math as m

feedThemAllC = lambda n: int(m.ceil(m.sqrt(8 * n - 7) / 2 - .5))

def feedThemAll(n):
    i = 0
    k = 1
    while 1:
        k += i
        if k >= n:
            return i
        i += 1

for i in range(1, 10):
    # print(int(m.ceil(m.sqrt(8 * i - 7) / 2 + 0.5 - 1)))
    print(i)
    print(" " + str(feedThemAll(i)))
    print(" " + str(feedThemAllC(i)))
    print()
