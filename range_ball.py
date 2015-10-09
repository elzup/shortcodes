import operator

def range_ball(a):
    return 0 if a == 1 else reduce(lambda b, c: b * -~c, range(1, a - 1), 1)

for i in range(1, 10):
    print(i, range_ball(i))

# 1: 0
# 2: 1
# 3: 2
# 4: 
