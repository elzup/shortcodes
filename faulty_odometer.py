def FaultyOdometer(k):
    n = 0
    for t in map(int, (str(k))):
        n *= 9
        if 4 < t:
            t -= 1
        n += t
    return n

print(FaultyOdometer(13))
print(FaultyOdometer(15))

