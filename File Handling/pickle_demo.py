import pickle
#import pickle as pk
'''s={'a':10,'b':20,'c':30}
w=pk.dumps(s)
print(w)
w=s
l=pickle.load(s)
print(l)
'''

'''
d={1:22,3:34,2:'hello'}
f=open('python.txt','wb')
pickle.dump(d,f)  #for conversion of object to byte code //serilization
f.close()
'''

f=open('python.txt','rb')
s=pickle.load(f)#Deserilization
print(s)
