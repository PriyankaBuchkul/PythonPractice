#using Reduce 
import functools
l=[1,2,3,4,5]
print(functools.reduce(lambda x,y:x+y,l))

'''
fibonacci = lambda x : 1 if x <= 2 else fibonacci(x-1) + fibonacci(x-2)
print(list(fibonacci))
'''
