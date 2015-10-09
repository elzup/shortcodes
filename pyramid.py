import pprint

# pyramidMatrix = lambda N: [[min(i + 1, N - i, j + 1, N - j) for i in r(N)] for j in r(N)]
r = range
pyramidMatrix = lambda N: [[min(i + 1, N - i, j + 1, N - j) for i in r(N)] for j in r(N)]

# def pyramidMatrix(N):
#     t = range(N)
#     return [[min(i + 1, N - i, j + 1, N - j) for i in t] for j in t]

# def pyramidMatrix(N):
#     t = range(N / 2) + range(-~N / 2)[::-1]
#     return [[min(i, j) + 1 for j in t] for i in t]

# pyramidMatrix = lambda N: [[N / 2 - max(abs(N / 2 - i), abs(N / 2 - j)) for i in r(N)] for j in r(N)]

pprint.pprint(pyramidMatrix(4))
pprint.pprint(pyramidMatrix(5))
