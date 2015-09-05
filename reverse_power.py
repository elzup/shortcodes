# def power(X):
#     for i in range(2, X + 1):
#         k = X
#         s = 0
#         while k % i == 0:
#             s += 1
#             k /= i
#         if k == 1:
#             return i, s

def power(X):
    for i in range(2, X + 1):
        k = X
        s = 0
        while k % i == 0:
            s += 1
            k /= i
        if k == 1:
            return i, s

print(power(27))
print(power(1024))
print(power(5 ** 5))
print(power(6 ** 8))
print(power(7))
