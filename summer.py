# Summer = lambda n: `bin(n)`.count('1')
Summer = lambda n: bin(n).count('1')

#     a = 0
#     while n != 0:
#         a += n & 1
#         n >>= 1
#     return a

n = 15
print(n, Summer(n))
