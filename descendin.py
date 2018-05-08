'''
def descending(num):
      s=str(num)
      a=sorted(s)[::-1]
      print(a)
      print(int(''.join(a)))


descending(9641816)

'''

def descending(num):
      return int(''.join(sorted(str(num),reverse=True)))

print(descending(814256479))
