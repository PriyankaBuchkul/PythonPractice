'''d={'id':[],'Name':[],'Age':[],'salary':[]}
a=int(input("How many entries you want??"))
for i in range(a):
      for j in d:
            s=input("Enter Value for {}: ".format(j))
            if s not in d[j]:
                  d[j].append(s)

print(d)'''


d={'id':[],'Name':[],'age':[],'salary':[]}
a=int(input("How many entries you want??"))
for i in range(a):
      for j in d:
            if j=='id':
                  d[j].append(int(input("Enter Interger Value for {}: ".format(j)))
            elif j=='age':
                  d[j].append(int(input("Enter Interger Value for {}: ".format(j)))
            elif j=='salary':
                  d[j].append(int(input("Enter Interger Value for {}: ".format(j)))
            else :
                  print()
                                          
            
                              
                              

print(d)
                  

