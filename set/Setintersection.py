l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,20,120,155]
'''
s1=set(l1)
s2=set(l2)

print(s1&s2)
'''

def removeCommon(set1):
    s=set{}
    for i in set1:
        if i not in s:
            s.append(i)



