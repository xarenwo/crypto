import string

ciphertext = 'bsaspp kkuosr'
key = 'rsidpy dkawoa'

x = []
for i in range(0,len(ciphertext)):
    if ciphertext[i] is not ' ':
        x.append((ord(ciphertext[i]) - ord(key[i])) % 26)
    else:
        x.append(' ')
alphabet = string.ascii_letters

xout = ''.join([alphabet[xo] if xo is not ' ' else ' ' for xo in x])
print(xout)
