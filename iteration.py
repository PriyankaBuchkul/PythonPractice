s="Python is good language"
l=s.split()

for i in l:
      print(i,id(i))
print("@"*20)

it=iter(l)
for i in range(len(l)+2):
      print(next(it),id(next(it)))
      
