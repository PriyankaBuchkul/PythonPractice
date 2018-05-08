import sys

randomList =['a',0,0.7,2]

for entry in randomList:
      try:
            print("The entry is :",entry)
            r=1/(entry)
            break
      except:
            print("Ooops!",sys.exc_info()[0],"Occured")
            print("Next Entry")
            print()
      else:
            print("This is else block")
      finally:
             print("This is finally block")

print("Reciprocal of Entry is:",entry,"is",r)

