


def Fraction(a, b):
    k = a + b
    while b:
        a, b = b, a % b
    return k / a

print(Fraction(2, 4))
