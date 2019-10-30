# with this algorithm you can find the d private key knowing e and phi totient
# this helps you avoid extended euclidean algorithm and just bruteforce d for k 1->totient
# formula is d=(k*totientPhi+1)/e
# if d*e mod phi == 1 then d is the key


phi = 3120
e = 17
for i in range(1,phi):
    d = (i*phi+1)/e % phi
    res = d*e % phi
    if res == 1 and d % 1 == 0:
        print('k -> {}\ne -> {} \nd -> {}'.format(i,e,d))
        break
