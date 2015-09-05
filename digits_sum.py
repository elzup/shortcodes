def Digital_sum(arg1):
    def k(n):
        return n if n < 10 else k(sum(map(int, (`n`))))
    return k(arg1)



Digital_sum = k = lambda n: n if n < 10 else k(sum(map(int, (`n`))))
Digital_sum = lambda n: 9 - -n % 9
for i in range(1000):
    print(i, 9 - -i % 9, Digital_sum(i))
