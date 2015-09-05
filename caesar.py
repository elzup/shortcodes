Caesar_Cipher = lambda m, k: ''.join(
    chr((ord(i) - k - (65 + 32 * (i > '`')) < 0) * 26 + ord(i) - k)
        if chr(i).isalpha()
        else i
    for i in m
)

# Caesar_Cipher = lambda m, k: "".join([chr((ord(i) - k - 65 + 32 * i.islower()) % 26 + 65 + 32 * i.islower()) if i.isalpha() else i for i in m])

print(Caesar_Cipher('Ymj vznhp gwtbs Ktc ozrux tajw ymj qfed itl', 5))
