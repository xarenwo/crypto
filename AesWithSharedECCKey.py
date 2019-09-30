from collections import OrderedDict
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(str(key).encode()).digest()


    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def modInverse(a, modulus):
    a = a % modulus
    for x in range(1, modulus):
        if (a * x) % modulus == 1:
            return x
    return 1


def calculateSlope(p1, p2, alfa, modulus,mode):
    if mode is 1: #double
        x1, y1 = p1
        slope = ((3 * (x1 ** 2) + alfa) * modInverse((2 * y1), modulus)) % modulus
    else:
        x1, y1 = p1
        x2, y2 = p2
        slope = ((y2 - y1) * modInverse((x2 - x1), modulus)) % modulus
    return slope


def getX3(p1, p2, alfa, modulus,mode):
    slope = calculateSlope(p1, p2, alfa, modulus,mode)
    x1, y1 = p1
    x1 = x1 % modulus
    y1 = y1 % modulus
    x2, y2 = p2
    x2 = x2 % modulus
    y2 = y2 % modulus
    x3 = ((slope ** 2) - x1 - x2) % modulus
    return x3


def getY3(p1, p2, x3, alfa, modulus,mode):
    slope = calculateSlope(p1, p2, alfa, modulus,mode)
    x1, y1 = p1
    y3 = (slope * (x1 - x3) - y1) % modulus
    return y3


def addPoints(p1,p2,alfa,modulus):
    x = getX3(p1, p2, alfa, modulus,0)
    y = getY3(p1, p2, x, alfa, modulus,0)
    return x,y


def doublePoint(p1,p2,alfa,modulus):
    x = getX3(p1, p2, alfa, modulus,1)
    y = getY3(p1, p2, x, alfa, modulus,1)
    return x,y


def computePublicKey(alfa,modulus,privateKey,pairs):

    # Initialize some variables
    pn = 1
    pnBit = list("{0:b}".format(pn))
    keyBit = list("{0:b}".format(privateKey))
    i=1

    # Compute the operation of points on the elliptic curve
    while pnBit != keyBit:

        if keyBit[len(pnBit) - 1] == pnBit[len(pnBit) - 1] and pn != privateKey:

            lastItem = list(pairs.keys())[-1]
            dp = doublePoint(pairs[lastItem],pairs[lastItem],alfa,modulus)
            pairs[pn+pn] = dp
            pn = (pn+pn)
            pnBit = list("{0:b}".format(pn))
            i = i+1

        elif keyBit[len(pnBit) - 1] != pnBit[len(pnBit) - 1]:

            lastItem = list(pairs.keys())[-1]
            ap = addPoints(pairs[lastItem],pairs[1],alfa,modulus)
            pairs[pn+1] = ap
            pn = (pn + 1)
            pnBit = list("{0:b}".format(pn))
            i = i+1

    lastItem = list(pairs.keys())[-1]
    return pairs[lastItem]


P = (10883, 10753) # This point is the generator point of the group
alfa = 2
modulus = 101467

# example of usage
# Alice chooses private key 55
# Bob chooses private key 70

privateKeyAlice = 80
privateKeyBob = 90

publicKeyAlice = computePublicKey(alfa,modulus,privateKeyAlice,OrderedDict({1:P}))
publicKeyBob = computePublicKey(alfa,modulus,privateKeyBob,OrderedDict({1:P}))

# Now Alice and Bob exchange public keys
finalKeyAlice = computePublicKey(alfa,modulus,privateKeyAlice,OrderedDict({1:publicKeyBob}))
finalKeyBob = computePublicKey(alfa,modulus,privateKeyBob,OrderedDict({1:publicKeyAlice}))

print("Alice Public Key : {}\nBob Public Key {}".format(publicKeyAlice,publicKeyBob))
print("Alice Key : {}\nBob Key : {}".format(finalKeyAlice,finalKeyBob))
# As you can see, in the end Alice and Bob have the same key,
# that can be used for other symmetric encryption methods like AES

xAlice,yAlice = finalKeyAlice
aesAlice = AESCipher((xAlice))

encryptedsecret = aesAlice.encrypt("Hey Bob, this message is very important !")


xBob,yBob = finalKeyBob
aesBob = AESCipher((xBob))
decryptedsecret = aesBob.decrypt(encryptedsecret)

print("Bob received -> \"{}\" from Alice".format(decryptedsecret))
