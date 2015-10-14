import re
def RomanNumerals(s):
    nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    if not re.search("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", s):
        return -1
    ints = [1000, 500, 100, 50, 10, 5, 1]
    places = []
    for c in s:
        if not c in nums:
            return -1
    for i in range(len(s)):
        c = s[i]
        value = ints[nums.index(c)]
        try:
            nextvalue = ints[nums.index(s[i +1])]
            if nextvalue > value:
                value *= -1
        except IndexError:
            pass
        places.append(value)
    return sum(places)

print(RomanNumerals("MMXV"))
print(RomanNumerals("IV"))
print(RomanNumerals("VI"))
print(RomanNumerals("VIV"))
