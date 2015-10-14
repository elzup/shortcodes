
def Untold(k, t, S, n):
    if n < 2:
        return 1
    for i in range(n - 1):
        a, b, x, y, z, M = S
        k, t = t, a * k ** 2 + b * t ** 2 + x * k + y * t + z
    return t

# def Untold(T0, T1, Numbers, n):
#     if n == 0:
#         return T0
#     if n == 1:
#         return T1
#     k = Untold(T0, T1, Numbers, n - 1)
#     t = Untold(T0, T1, Numbers, n - 2)
#     return (Numbers[0] * k ** 2 + Numbers[1] * t ** 2 + Numbers[2] * k + Numbers[3] * t + Numbers[4]) % Numbers[5]

print(Untold(1, 1, [0, 0, 1, 1, 0, 1000], 7))
# 21

