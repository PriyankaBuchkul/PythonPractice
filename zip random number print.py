a=[1,3,7]
b=[2,4,6,8]
c=[9,10,13,16,66]

l=[]
for k,v,f in zip(a,b,c):
      l.append(k)
      l.append(v)
      l.append(f)
print(l)
