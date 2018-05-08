#print all possible 4 digit numbers
  
import enchant
d=enchant.Dict("en_UK") #create dictioany for UK english
from itertools import permutations
data=['a','b','c','d','e','f','g','h','i']
print(data)

res=list(permutations(data,4)) #calcuate permutations for 4 letter combination
ip=[]
result=[]
for i in res:
      ip.append(''.join(i)) #convert list to string store in ip
for k in ip:
      if d.check(k)==True: #check the word id valid english word or not
            if k in result:
                  pass #pass if already exist in result list
            else:
                  result.append(k)
print(result)     #print Result

