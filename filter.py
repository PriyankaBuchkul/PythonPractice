print("EVEN NUMBER")
l=list(range(10,100))
f=filter(lambda x:x%2==0,l)
print(list(f))


print("Removes < 0 elements")
l1=list(range(-5,6))
f1=filter(lambda x:x>0,l1)
print(list(f1))



a=[1,2,3,4,5]
b=[2,3,4,8,6,7]

l3=filter(lambda x:x in a,b)
print(list(l3))



