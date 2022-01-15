def encrypt(text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabets[(alphabets.index(i) + key) % 26] if i != " " else " " for i in text])

def decrypt(c_text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabets[alphabets.index(i) - key] if i != " " else " "  for i in c_text])

plain_text = ""
name = input('Enter File Name to Encrypt: ')
try:
    with open(name+'.txt', 'r') as f:
        plain_text = f.read()
        print('File read Successfully!')
        print(f'Data is "{plain_text[:7]} ..."')
except FileNotFoundError:
    print('File Not Found!')
    print('Program Exiting...')
    exit()

key = int(input("Enter Key: ")) % 26

cipher = encrypt(plain_text, key)
with open(name+'.cpr', 'w') as fb:
    fb.write(cipher)
    print('File Encrypted Successfully!')
    print(f'File Saved as {name}.cpr')
    fb.close()
