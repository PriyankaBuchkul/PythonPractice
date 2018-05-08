#positional Arguments
print("===================== Positional Argumants==================")
def add(a,b):
      return(a+b)
print(add(2,5))
print("=====================Keyworded Argumants==================")
#keyworded Argumnets
def add1(a,b=3):
      return a+b
print(add1(3))

print("=====================arbitary Positional Argumants==================")
#arbitary Positional Argumants
def demo(*args):
      for i in args:
            print(i,end=' ')
t=(10,23,45)
demo(t)
print("=====================arbitary keyworded Argumants==================")   
def test(fargs,*args,**kwargs):
      print("formal argumant is :",fargs)
      for i in args:
            print("args Is :",i)
      for  k in kwargs:
                  print("KEYWORD  ARGS are:%s:%s"%(k,kwargs[k]))

test(10,2,3,4,5,6,a=10,b=20,c=100,d=300)
