#
l=[1,2,3,4]

try:
      print(l)
     # print(l[5])
     # print(s[3])
      print(l.split())
except(IndexError,NameError,AttributeError)as e:
      print(e)


'''
print(s[5])
print(l.split())
'''
