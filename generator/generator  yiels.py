def fun():
      print("Beginning.....!")
      for i in range(3):
            print("Before yielding  :",i)
            yield i
            print("After yielding   :",i)
      print("Its Ended")

f=fun()
print(f.__next__())

print(f.__next__())

print(f.__next__())

print(f.__next__())

            
