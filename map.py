def square(x):
	return x*x

l=list(map(square,[1,2,3,4]))

#print(l)

def mul(y):
      return y*4
l3=list(map(mul,[1,2,3,4]))
#print(l3)

def add(p):
	return p+p

l1=list(map(add,[1,2,3,4]))
#print(l1)



func=[square,mul,add]
for i in range(5):
      m=map(lambda x:x(i),func)
      print(list(m))
