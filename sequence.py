# sequence = lambda k, y, z: [k * x - y for x in range(1, z + 1)]
# sequence = lambda k, y, z: range(k - y, (k - y) + k * z, k)
sequence = lambda k, y, z: range(k - y, k - y + k * z, k)


print(sequence(1, 4, 8))
print(sequence(1, 8, 10))
print(sequence(5, 5, 7))
