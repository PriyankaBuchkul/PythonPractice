#print Pattern in python
'''
def pattern(n):
      #num=1
      for i in range(0,n):
            start=1
            for j in range(0,i+1):
                  print(start,end='')
                  start=start+1
                  #print('*')
             
            print("\r")


pattern(6)
'''

for i in range(1,10):
      for j in range(10,0,-1):
            print(str(i)+"*"*(j-i))
            break


for x in range(11,0,-1):
      print(x*' '+(11-x)* '*')
                                                                                                                                                                                                                                                                                               
