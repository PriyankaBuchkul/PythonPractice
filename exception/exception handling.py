def f(x):
      return g(x)

def g(x):
      if x<0:raise ValueError("I can't cope with the negative number here.")
      else:return 5

try:
      print(f(-3))
except ValueError as e:
      print(e)
      
      
