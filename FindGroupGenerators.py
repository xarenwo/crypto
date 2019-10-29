# You can find all generators of a small group
# If you choose a large prime number Zp the complexity will be pretty high and it will take a lot of time
# Those computations are very hard to do, that's why cryptography works in a sense, it's hard to find factors and the discrete logarithm problem



from math import gcd

group = 5743 #prime number Zp

def findFactors(x):
    factors = []
    for i in range(2, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

factors = findFactors(group-1)

def findGenerators(group,factors):
    generators = []
    banned = []
    for alfa in range(2,group):
        if gcd(alfa,group) == 1:
            for fact in factors:
                x = pow(alfa,((group-1)//fact)) % group
                if x == 1:
                    banned.append(alfa)
                if x != 1 and alfa not in generators and alfa not in banned:
                    generators.append(alfa)
    ee = []
    cc = []
    for gg in generators:
        for i in range(1, group):
            xx = (gg ** i) % group
            if xx not in ee:
                ee.append(xx)
        if len(ee) == group - 1:
            cc.append(gg)
        ee = []
    return cc

gener = findGenerators(group,factors) # pass group size and factors of the prime number

print(gener)
