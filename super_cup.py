def SuperCup(s):
    a, b = "zamalek", "alahly"
    for c in s:
        if a[0] == c:
            a = a[1:]
        if b[0] == c:
            b = b[1:]
        if a == "":
            return "win"
        if b == "":
            return "loss"

print(SuperCup('zaqlaqmaqlehkly'))
