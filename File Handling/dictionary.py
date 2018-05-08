d={'id':[],'Name':[],'age':[],'salary':[]}
a=int(input("How many Entries:"))
for i in range(a):
      for j in d:
            if j=='id':
                  d[j].append(int(input("ENter Interger value for {}:".format(j))))
            elif j=='age':
                  d[j].append(int(input("ENter  value for {}:".format(j))))
            elif j=='salary':
                  d[j].append(float(input("ENter  value for {}:".format(j))))
            else:
                  d[j].append((input("ENter  value for {}:".format(j))))
print(d)
f=open("dict_data.txt",'w')
for i in d:
      f.write("The {} is {},{} is {},{} is {} and {} is {}\n".format(i,d[i],i,d[i],i,d[i],i,d[i]))
f.close()
s=open("dict_data.txt",'r')
for i in s.readlines():
      print(i)
s.close()
            
            
