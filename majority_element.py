def Majority_Element(N, a):
    t = {}
    for i in a:
        if i not in t:
            t[i] = 0
        t[i] += 1
        if t[i] > N / 2:
            return i
    return -1

# from collections import Counter as c
# def Majority_Element(N, a):
#     k, v = c(a).most_common()[0]
#     return [-1, k][v > N / 2]

print(Majority_Element(9, [3, 3, 4, 2, 4, 4, 2, 4, 4]))
print(Majority_Element(5, [3, 3, 2, 2, 1]))
print(Majority_Element(7, [3, 4, 4, 3, 3, 500, 3]))

