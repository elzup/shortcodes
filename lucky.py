import re
def LuckyNum(L, R):
    for i in range(L, R + 1):
        if all(k in '47' for k  in `i`):
            return i
    return -1




# def LuckyNum(L, R):
#     f = filter(lambda i: all(k in '47' for k in `i`), range(L, R + 1))
#     return f[0] if f else -1

print(LuckyNum(3, 77))
