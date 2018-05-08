def fun(exp):
      for i in exp:
            yield i**2


g=fun(iter(range(10)))

print(g.__next__())
print(g.__next__())
print(g.__next__())

print(list(g))
