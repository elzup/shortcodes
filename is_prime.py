f = lambda n: (n > 1) * all(n % i for i in range(2, n))
# f = lambda n: all(n % i for i in range(2, n)) & (n >> 1)
# f = lambda n: all(n % i for i in range(2, n)) * n >> 1

for i in range(100):
    print(str(i) + ": " + str(f(i)))
