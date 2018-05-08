def number(f):
      def helper(x):
            if type(x)==int and x>0:
                  return f(x)
            else:
                  raise Exception("No Cant be negative")

      return helper

@number
def fact(n):
      if n==1:
            return 1
      else:
            return n*fact(n-1)

f=fact(5)
print(f)


for i in range(-4,5):
      print(fact(i))
