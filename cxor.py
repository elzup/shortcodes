distancesum = lambda n, a: sum(
        abs(a[i] - a[j])
        for i in range(n)
        for j in range(i + 1, n)
        ) % 10000007

print(distancesum(3, [-3, 4, -3]))
