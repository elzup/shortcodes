def is_cyclic_sorted(a):
    l = len(a)
    for i in range(l):
        b = [a[j % l] - a[-~j % l] for j in range(i, i + l - 1)]
        if abs(b[0]) == 1 and len(set(b)) == 1:
            return True
    return False
    # return b.count(b[0]) > len(a) - 2 or b.count(b[1]) > len(a) - 2

print(is_cyclic_sorted([1, 2, 3, 4]))
print(is_cyclic_sorted([1, 2, 3, 4, 0]))
print(is_cyclic_sorted([0, 1, 2, 3, 4, 5]))
print(is_cyclic_sorted([2, 4, 6, 8, 10, 0]))
print(is_cyclic_sorted([2, 3, 4, 5, 0, 1]))
print(is_cyclic_sorted([3, 4, 5, 0, 1, 2]))
print(is_cyclic_sorted([4, 5, 0, 1, 2, 3]))
print(is_cyclic_sorted([5, 0, 1, 2, 3, 4]))
print(is_cyclic_sorted([0, 1, 2, 3, 4, 5]))
# https://codefights.com/profile/elzup
