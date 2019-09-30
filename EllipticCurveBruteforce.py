from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tkinter
matplotlib.use('TkAgg')

def modInverse(a, modd):
	a = a % modd
	for x in range(1, modd):
		if (a * x) % modd == 1:
			return x
	return 1


def calculateSlope(p1,p2,alfa,modd):
	if p1==p2:
		x1,y1 = p1
		slope = ((3*(x1**2) + alfa) * modInverse((2*y1),modd)) % modd
	else:
		x1,y1 = p1
		x2,y2 = p2
		slope = ((y2-y1) * modInverse((x2-x1),modd)) % modd
	return slope


def getX3(p1,p2,alfa,modd):
	slope = calculateSlope(p1,p2,alfa,modd)
	x1,y1 = p1
	x1 = x1%modd
	h1 = y1%modd
	x2,y2 = p2
	x2 = x2%modd
	y2 = y2%modd
	x3 = ((slope**2) - x1 - x2) % modd
	return x3


def getY3(p1,p2,x3,alfa,modd):
	slope = calculateSlope(p1,p2,alfa,modd)
	x1,y1 = p1
	y3 = (slope*(x1-x3) - y1) % modd
	return y3

# Algorithm to calculate all points on an elliptic curve
# It can be used to calculate all points for the ECC Cryptography
# Example : Given the curve y^2 = x^3 + 2*x + 2 mod 17
# The points are in a Cyclic group Zp* where p is a prime number 17
# In our case the order of the group is also prime, which means every element in the group is primitive (generator)
# Now given a generator P(5,1) and a public key (desired end point)
# We can bruteforce in order to find the private key d
# The private key is the number which the generator is multiplied by (number of # operations), in order to get our end point public key.

# coordinates of generator
x=17
y=21
# P(x,y)
pubkey=(7,13) # end point
# Modular value
Mod = 20963


x = x%Mod
y = y%Mod
Generator = (x,y)
sums = OrderedDict()


def bruteForceEC(Generator,Mod,sums,pubkey):
	sums[1] = Generator
	alfa = 2
	modd=Mod
	for i in range(2,99999999999):

		done = [x for x in sums.keys()]
		p1 = sums[i-1]
		todiv = [x for x in done if x+(i-1) == i]
		p2 = sums[todiv[0]]
		x = getX3(p1,p2,alfa,modd)
		y = getY3(p1,p2,x,alfa,modd)
		dd = list(sums.values())
		sums[i] = (x, y)
		print("Trying {} == ({},{}) \n".format(pubkey,x,y))
		if pubkey in dd or sums[i] in dd:
			break

	print("Points generated : \n")
	for key,value in sums.items():
		print("{}P -> {}".format(key,value))

	print("Order of group {}\n".format(i-1))

	print("\nPrivate key is {} \n".format(i-1))
	print("\n{} = {}*{}\n".format(pubkey,i-1,sums[1]))


bruteForceEC(Generator,Mod,sums,pubkey)


pp = [x for x in sums.values()]
xp = [x for x,y in pp]
yp = [y for x,y in pp]

xpp = np.array(xp)
ypp = np.array(yp)

line=plt.plot(xpp,ypp,'o')[0]
line.set_clip_on(False)
plt.show()
