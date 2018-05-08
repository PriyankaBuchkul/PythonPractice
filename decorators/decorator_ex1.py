import time
def our_decorators(func):
      def function_wrapper(x):
            print("Before calling "+func.__name__)
            time.sleep(2)
            func(x)
            print("after calling "+func.__name__)
            time.sleep(2)
      return function_wrapper

def foo(a):
      print("hi, foo has been called with "+str(a))


f=our_decorators(foo)
f(8)
            
