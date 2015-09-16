TakingMoney = lambda _, X: ("not " if len(set(X)) < 3 else "") + 'ambiguous'

print(TakingMoney(15, [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0]))
