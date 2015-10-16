
def subarraysearch(a, s):
    return all(i in a.lower() for i in s.lower())

# subarraysearch = lambda a, s: all(i in a.lower() for i in s.lower())

print(subarraysearch("ABCdefgh", "bCf"))
print(subarraysearch("ABCdefgh", "i"))
