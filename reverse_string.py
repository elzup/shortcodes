import re
reverse_string = lambda s: re.sub('[^a-zA-Z]', '', s[::-1])
# reverse_string=lambdas:re.sub('[^a-zA-Z]','',s[::-1])

reverse_string = lambda s: ''.join(c if c.isalpha() else '' for c in s)
# reverse_string=lambdas:''.join(cifc.isalpha()else''forcins)

reverse_string = lambda s: filter(str.isalpha, s)[::-1]
# reverse_string=lambdas:filter(str.isalpha,s)[::-1]

print(reverse_string('abc*d?4ef3g'))
print(reverse_string('krishan'))

