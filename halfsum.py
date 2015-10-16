HalfSum = lambda A: sum(A) / 3
# HalfSum = lambda A: sum((sum(A) == i * 3) * i for i in A)

print(HalfSum([1, 2, 3, 4, 5]))
