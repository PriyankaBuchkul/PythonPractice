stack=['Wake Up','dress Up','have a coffee','have breakfast','go to office']

def view():
      for x in range(len(stack)):
            print(stack[x])

def push():
      item=input("Enter item to add:")
      if item.isdigit():
            stack.append(int(item))
      else:
            stack.append(item)

def pop():
      if len(stack)>0:
            item=stack.pop(-1)
            print("You Just poped out :",item)
      else:
            print("Can't pop from empty stack ,please insert something before pop :-(")

while True:
      print(" ")
      print("Python Implementation Of Stack ")
      print("#######################"*2)
      print(" 1. View  ")
      print(" 2. Push ")
      print(" 3. pop ")
      print("#######################"*2)
      choice=int(input("Please ENter your choice :"))

      if choice==1:
            view()
      elif choice==2:
            push()
      elif choice==3:
            pop()
      else:
            print("You Entered wrong choice")
            break
