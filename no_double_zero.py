# -*- coding: utf-8 -*-
import time
start = time.time()

# for n in range(1, 20):
#     c = 0
#     for j in range(2 ** n):
#         if all(j >> k & 1 or j >> (k - 1) & 1 for k in range(1, n)):
#             c += 1
#     print(n, c)

def OnesandZeros(n):
    a = p = 1
    for k in range(n):
        a, p = a + p, a
    return a

for i in range(1, 10):
    print(i, OnesandZeros(i))
    print("")

# output: it is fibonachi
print(str(time.time() - start) + "ms")
