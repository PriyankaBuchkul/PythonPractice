import functools
print(functools.reduce(lambda a,b:a if(a>b) else b,[22,44,11,33,68]))
