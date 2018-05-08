def simple_decorator(decorator):
      def new_decorator(f):
            g= decorator(f)
            g.__name__=f.__name__
            g.__doc__=f.__doc__
            g.__dict__.update(f.__dict__)
            return g

      new_decorator.__name__= decorator.__name__
      new_decorator.__doc__=decorator.__doc__
      new_decorator.__dict__.update(decorator.__dict__)
      return new_decorator

@simple_decorator
def my_simple_logging_decorator(func):
      def you_will_never_use_this_name(*args,**kwargs):
            print("Calling {}".format(func.__name__))
            return func(*args,**kwargs)
      return you_will_never_use_this_name

@my_simple_logging_decorator
def double(x):
      'doubles a number'
      return 2 * x

assert double.__name__ =='double' #assert is used in test cases
assert double.__doc__ =='doubles a number'
print(double(50))

   
      
