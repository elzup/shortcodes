PowersOfTwo = lambda M: z(M, 2 ** (len(bin(M)) - 3))

z = lambda N, k: N / 2 + 1 if k < 3 else sum(z(N - t * k, k / 2) for t in range(N / k + 1))

for i in range(1, 100):
    print('--' + str(i))
    print(PowersOfTwo(i))
    print('')
