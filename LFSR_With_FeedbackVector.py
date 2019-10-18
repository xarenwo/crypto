#lfsr with feedback
from collections import OrderedDict
m = 8
bytes = 2 #how many of the first bytes you want as result (based on the fact that we have 8 flip flops so each row is 1 byte=8bits)
outputbytes = bytes*8
feedbackcoefficients = [1,1,0,1,1,0,0,0]
initializationvector = [1,1,1,1,1,1,1,1]


period = (2**m)-1
print('Period is {}'.format(period))
if len(feedbackcoefficients) is not m or len(initializationvector) is not m:
    print("Invalid feedback coefficients or init vector !")
    exit()

sim = OrderedDict()

for i in range(0,outputbytes):
    if i < m:
        sim[i] = (initializationvector[i]) % 2
    else:
        sim[i] = 0

for i in range(0,(outputbytes-m)):
    for j in range(0,m):
        sim[i+m] += (feedbackcoefficients[j] * sim[i+j])

sim = [int(value)%2 for key,value in sim.items()]
print(sim)
print(len(sim))
