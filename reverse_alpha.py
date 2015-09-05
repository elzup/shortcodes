HackIt = lambda k: ''.join(
  [
    chr(155 - ord(i) + 64 * ('Z' < i)),
    i
  ][i < 'A']
  for i in k)

# HackIt = lambda k: ''.join(
#   chr(
#     [
#       155 - i + 64 * (90 < i),
#       i
#     ][i < 65])
#   for i in map(ord, k))

print(HackIt('Xlwv Urtsgh'))
