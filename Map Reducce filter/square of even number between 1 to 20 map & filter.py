#square of even number between 1 to 20 map & filter 

even = filter(lambda x:x%2==0,range(1,21))
l=list(even)

print(l)

square=map(lambda x:x**2,l)
print(list(square))
