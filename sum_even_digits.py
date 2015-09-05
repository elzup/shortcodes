
compareSumOfDigits = lambda N: sum(i % 2 * 2 * i - i for i in map(int, N))

print(compareSumOfDigits('74'))
print(compareSumOfDigits('0000000000012345'))
print(compareSumOfDigits('01234510238401283094810230329304'))
