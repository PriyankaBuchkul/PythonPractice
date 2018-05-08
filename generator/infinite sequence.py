def ints():
      i=1
      while True:
            yield i
            i+=1

print()i
def square():
      for i in ints():
            yield i*i

def demo(n,seq):
      r=[]
      it=iter(seq)
      try:
            for i in range(n):
                  r.append(it.__next__())
      except StopIteration:
            print("Ended")
      return r

print(demo(5,square()))
            
