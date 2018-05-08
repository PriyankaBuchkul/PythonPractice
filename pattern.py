#Various pattern Printing Programs


n=int(input("Enter The number of lines triangle:"))
'''for i in range(n,0,-1):
  print('*'*i)
'''  
#LIST COMPREHENSIO'

print('\n'.join(['*'.i for i in range(1,n+1)]))
      
