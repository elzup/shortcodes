import re, ast
def correct_parentheses(s):
    try:
        t = re.sub('([)\]])', r'\1,', s)
        ast.parse(t)
        return True
    except Exception:
        return False


# def correct_parentheses(s):
#     t = '.'
#     for i in s:
#         t = t[:-1] if t[-1] + i in ['()', '[]'] else t + i
#     return t == '.'


# def correct_parentheses(s):
#     t = '.'
#     for i in s:
#         t = t[1:] if t[0] + i in '()[]' else i + t
#     return t == '.'

def correct_parentheses(s):
    t = '..'
    for i in s:
        t = i + t
        if t[:2] in ')(][':
            t = t[2:]
    return t < '._'


print(correct_parentheses('()()()()[]') == True)
print(correct_parentheses('([])') == True)
print(correct_parentheses('([)]') == False)
print(correct_parentheses('(') == False)
print(correct_parentheses('[]]') == False)
