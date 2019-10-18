def xxor(x, y):
  a = int(x)
  b = int(y)
  return (a & ~b) | (~a & b)


s1 = list('0101101') # our key (the tricky part is getting a strong key that both parties agree on)
x1 = "{0:b}".format(ord('A')) # the message

def streamEncrypt(x,s):
    y=[]
    for i in range(0,len(x)):
        res = xxor(int(s[i]),int(x[i]))
        y.append(res)
    ystr = ''.join([str(x) for x in y])
    return ystr

cipher = streamEncrypt(x1,s1)
print(cipher)
print(streamEncrypt(cipher,s1))
