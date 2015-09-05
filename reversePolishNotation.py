# def toPostFixExpression(e):
#     p = lambda c: (c in '*/%') * 2 + (c in '+-')
#     s = []
#     h = []
#     for c in e:
#         if c == ')':
#             while h[-1] != '(':
#                 s += [h[-1]]
#                 h = h[:-1]
#             h = h[:-1]
#         elif c.isdigit():
#             s += [c]
#         elif h and p(h[-1]) >= p(c) and c != '(':
#             s += [h[-1]]
#             h[-1] = c
#         else:
#             h += [c]
#     return s + h[::-1]

def toPostFixExpression(e):
    p = lambda c: (c in '*/%') * 2 + (c in '+-')
    s = []
    h = []
    for c in e:
        if c == ')':
            while h[-1] != '(':
                s += [h[-1]]
                h = h[:-1]
            h = h[:-1]
        elif c.isdigit():
            s += [c]
        elif h and p(h[-1]) >= p(c) and c != '(':
            s += [h[-1]]
            h[-1] = c
        else:
            h += [c]
    return s + h[::-1]

print(toPostFixExpression('3*4'))
print(toPostFixExpression('3*4+5*6'))
print(toPostFixExpression('3*(4+5)*6'))
print(toPostFixExpression(["20","+","3","*","(","5","*","4",")"]))
print(toPostFixExpression("10*(5+3%2*(3+3)/4)"))
print(toPostFixExpression("3*4/5"))

