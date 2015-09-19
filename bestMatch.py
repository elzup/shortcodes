def BestMAtch(N, a, b):
    t = [abs(j - k) for j, k in zip(a, b)]
    return N + ~t[::-1].index(min(t))

# def BestMAtch(N, a, b):
#     for v1, v2 in zip(a, b):
#         t.append(abs(v1 - v2))
#     return N - t[::-1].index(min(t)) - 1


print(BestMAtch(2, [6, 4], [1, 2]))
print(BestMAtch(6, [1, 1, 2, 4, 3, 5], [3, 7, 4, 6, 5, 8]))

