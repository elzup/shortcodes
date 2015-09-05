def Caesar_Cipher(m, k):
    r = ''
    for i in m:
        if i.isalpha():
            t = 65 + 32 * i.islower()
            r += chr((ord(i) - k - t) % 26 + t)
        else:
            r += i
    return r

# Caesar_Cipher = lambda m, k: "".join(chr((ord(i) - k - (97 if i.islower() else 65)) % 26 + (97 if i.islower() else 65)) if i.isalpha() else i for i in m)

print(Caesar_Cipher('Ymj vznhp gwtbs Ktc ozrux tajw ymj qfed itl', 5))
