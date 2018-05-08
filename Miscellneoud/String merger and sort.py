
#[{}]===>  set(str)-->list<== sorted
def longest(a,b):
      return (''.join(sorted(set(a)|set(b))))
##      a=set(a)|set(b)
##      print(a)
##      s=sorted(a)
##      print(' '.join(s))

print(longest('xyaabbbccccdefww','xxxxyyyyabklmopdg'))
