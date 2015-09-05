def water_area(a):
    s = 0
    for h in range(9):
        k = 1
        l = 0
        for j in range(len(a)):
            if h < a[j]:
                if k:
                    l = k = 0
                else:
                    s += l
                    l = 0
            else:
                l += 1
    return s


print(10, water_area([3, 0, 0, 2, 0, 4]))

print(6, water_area([2,0,3,0,4,0,1]))
print(0, water_area([0,0,6,0,0,0,0,0]))
print(9, water_area([3,0,0,0,3]))

print(10, water_area([5,0,4,0,3,0,2,0,1]))

