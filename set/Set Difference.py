x={'a','b','c','d','e'}
y={'b','c'}
z={'c','d'}
'''
d=x-y
e=x-d
print(e)#c b
for i in e:
      if i in e:
            print(i)

#print(e)
'''
l=set()
for i in x:
      for j in y:
            for k in z:
                  if i==j==k and i not in l and k not in l:
                        l.add(i)
print(l)
