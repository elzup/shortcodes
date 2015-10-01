sumofprimenumbers = lambda n, a: sum(
        (i > 1) * all(i % j for j in range(2, i)) * sum(map(int, list(`i`)))
        for i in a)
# return sum(f(i) * sum(map(int, list(`i`))) for i in a)

print(sumofprimenumbers(3, [11, 21, 54]))
print(sumofprimenumbers(4, [22, 7, 121, 17]))
