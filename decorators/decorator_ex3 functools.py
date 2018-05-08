from functools import wraps


def mydecorator(f):
      @wraps(f)
      def wrapped(*args,**kwargs):
            print("Before decorated function")
            r=f(*args,**kwargs)
            print("after decorated function")
            return r
      return wrapped

@mydecorator
def myfunc(myarg):
      print("myfunction",myarg)
      return "return value"

r=myfunc('dsscs')
print(r)
            
            
