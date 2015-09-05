from collections import Counter as c

def yTimes(A):
    t = c(A)
    for k, v in sorted(t.items(), key=lambda x: -x[1]):
        if k != 1 and c(t.values())[v] == 1:
            return k
    return -1

print(yTimes([1,2,2,3,30,30,30]))
print(yTimes([984,984,33,22,33,22,15,33,15,15,22]))
