def encrypt(text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabets[(alphabets.index(i) + key) % 26] if i != " " else " " for i in text])

def decrypt(c_text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabets[alphabets.index(i) - key] if i != " " else " "  for i in c_text])

plain_text = input("Enter Plain Text : ")
key = int(input("Enter Key: ")) % 26

cipher = encrypt(plain_text, key)

print("Cipher Text :", cipher)
print("Plain Text :", decrypt(cipher, key))