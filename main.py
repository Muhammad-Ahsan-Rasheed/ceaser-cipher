from string import ascii_lowercase

def encrypt(text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabets[(alphabets.index(i) + key) % 26] if i in ascii_lowercase else i for i in text])

def decrypt(c_text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabets[alphabets.index(i) - key] if i in ascii_lowercase else i  for i in c_text])

def filing(in_name, key):
    plain_text = ''

    try:
        with open(in_name, 'r') as f:
            plain_text = f.read()
            print('File read Successfully!')
            print(f'Data is "{plain_text[:7]} ..."')
    except FileNotFoundError:
        print('File Not Found!')
        print('Program Exiting...')
        exit()
    cipher = encrypt(plain_text, key)
    
    out_file_name = name.split('.')[0]+'.cpr'
    with open(out_file_name, 'w') as fb:
        fb.write(cipher)
        print('File Encrypted Successfully!')
        print(f'File Saved as {out_file_name}')
        fb.close()

if __name__ == '__main__':
    name = input('Enter File Name (with extension e.g file.txt) to Encrypt: ')
    key = int(input("Enter Key: ")) % 26

    filing(name, key)
