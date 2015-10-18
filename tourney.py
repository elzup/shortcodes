a = ["a"]
N = 1

def r(N, a, fun):
    # print(N, a)
    if N == 1:
        return a[0]
    return fun + "(" + r(N / 2, a[:N / 2], fun) + "," + r(N - N / 2, a[N / 2:], fun) + ")"

def Tourney(N, a, fun):
    return r(N, list(sum(zip(a[:N / 2], a[N / 2:]), ())) + ([a[-1]] if N % 2 else []), fun)

print(Tourney(1, ["phqg"], "won"))
print(Tourney(1, ["phqg"], "won") == 'won(phgg)')

print(Tourney(2, ["phqg",  "hume"], "won"))
print(Tourney(2, ["phqg",  "hume"], "won") == 'won(phqg,hume)')

print(Tourney(3, ["Name1","Name2","Name3"], "win"))
print(Tourney(3, ["Name1","Name2","Name3"], "win") == 'win(win(Name1,Name3),Name2)')

print(Tourney(4, ["Name1","Name2","Name3","Name4"], "won"))
print(Tourney(4, ["Name1","Name2","Name3","Name4"], "won") == "won(won(Name1,Name3),won(Name2,Name4))")

print(Tourney(8, ["Name1","Name2","Name3","Name4","Name5","Name6","Name7","Name8"], "won"))
print(Tourney(8, ["Name1","Name2","Name3","Name4","Name5","Name6","Name7","Name8"], "won") == "won(won(won(Name1,Name5),won(Name3,Name7)),won(won(Name2,Name6),won(Name4,Name8)))")


