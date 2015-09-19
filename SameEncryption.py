e = lambda s: s[0] + `sum(map(int, `len(s) - 2`))` + s[-1]
SameEncryption = lambda f, s: ["NO", "YES"][e(f) == e(s)]

print(SameEncryption("abc", "abc"))
