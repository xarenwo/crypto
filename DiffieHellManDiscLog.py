import random

def findOrder(num,mod):
    ss = []
    for i in range(1,mod):
        s = (num**i) % mod
        if s not in ss:
            ss.append(s)
    return len(ss)

def findGenerators(mod):
    gen = []
    for i in range(1,mod):
        if findOrder(i,mod) == mod-1:
            gen.append(i)
    return gen


p = 419 # large prime number

generators = findGenerators(p)
alfa=random.choice(generators) # alfa is a generator of group Zp
alln = [x for x in range(1,p) if x%2 ==0]
a = random.choice(alln) # private key, better if even number
b = random.choice(alln) # private key, better if even number

print('Private Key for Alice is {} \nPrivate Key for Bob is {}'.format(a,b))
print('We have public the set (alfa,p) = ({},{})'.format(alfa,p))
print('Computing public keys ...')
kpubAlice = alfa**a % p
kpubBob = alfa**b % p

print('Exchanged public keys... \nPublic key of Alice is {} \nPublic key for Bob is {}'.format(kpubAlice,kpubBob))
finalAlice = kpubBob**a % p
finalBob = kpubAlice**b % p
print('Alice computes final key as {}'.format(finalAlice))
print('Bob computes final key as {}'.format(finalBob))
print('Both bob and Alice have same key {}'.format(finalBob))
print('\nBob and Alice can now use the key for encrypting with a symmetric algorithm like AES')
print('\nIn order for Oscar to attack this, he needs to solve the Discrete logarithm problem\n'
      'which means he needs to find a=log(alfa)A mod p or b=log(alfa)B mod p\n'
      'then he knows private keys a and b, and he can compute B^a= alfa^(ab) which is the final key used for aws\n'
      'unfortunately the DL(Discrete Log or Diffie Hellman) problem a=log(alfa)A mod p is a very hard problem if p is large enough.')
