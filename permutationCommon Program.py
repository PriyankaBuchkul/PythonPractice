def per(items):
      n=len(items)
      if n==0: yield []
      else:
            for i in range(n):
                  for cc in per(items[:i]+items[i+1:]):
                        yield [items[i]]+cc


for p in per(['r','e','d']):
      print(''.join(p))
