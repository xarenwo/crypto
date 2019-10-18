import string


def caesarEncrypt(plaintext:str,key:int):
    alphabet = string.ascii_lowercase
    plaintext = plaintext.lower()
    shifted_alph = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet,shifted_alph)
    endtext = plaintext.translate(table)
    return endtext

def caesarDecrypt(plaintext:str,key:int):
    alphabet = string.ascii_lowercase
    plaintext = plaintext.lower()
    shifted_alph = alphabet[-key:] + alphabet[:-key]
    table = str.maketrans(alphabet,shifted_alph)
    endtext = plaintext.translate(table)
    return endtext


text = 'Vuf vuf vuf i\'m a dangerous corgi'
key = 5
cipher = caesarEncrypt(text,key)
plain = caesarDecrypt(cipher,key)
print('Encrypted Cipher : {}'.format(cipher))
print('Decrypted Text : {}'.format(plain))


print('Trying to bruteforce \n')
for i in range(1,25):
    print('{} -- {}'.format(i,caesarDecrypt(cipher,i)))
