def hexa(num):
    return hex(num)[2:].upper()
print(hexa(12345678))

hexa = lambda n: hex(n)[2:].upper()
print(hexa(12345678))

hexa = lambda n: "%X" % n
print(hexa(12345678))

hexa = "{:X}".format
print(hexa(12345678))
