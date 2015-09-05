from itertools import permutations as p
permutation = lambda n, v: list(p(v))[n - 1]

print(permutation(1, [1, 2, 3]))
print(permutation(4, [1, 2, 3]))
