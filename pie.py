pie = lambda n: 4 * sum((-1.) ** i / (2 * i + 1) for i in range(n + 1))

# pie = lambda n: 4 * sum((1 - 2. * (i & 1)) / (2 * i + 1) for i in range(n + 1))

print(pie(10))
