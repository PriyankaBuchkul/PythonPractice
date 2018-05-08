print("=======================Using Keys==========================")
def char_count(s):
    dict = {}
    for n in s:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_count('the quick brown fox jumps over the lazy dog'))

print("==========================Using get==============================")

s="The quick brown fox jumps over the laz dog"
d={}
for i  in s:
      d[i]=d.get(i,0)+1

print(d)

print("Print Word COunt In a dictionary:====================>")
s1="The quick brown fox jumps over the laz dog"
d1={}
for i in s1.split():
      d1[i]=d1.get(i,0)+1

print(d1)

