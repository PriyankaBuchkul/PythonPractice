d1={'name':'priya','age':24}
d2={'name':'Mayur','age':15}
d3={'name':'priyanka','age':23}
d4={'name':'priti','age':21}


d=[d1,d2,d3,d4]


def check(ch):
      for entry in d:
            if entry['name']==ch:
                  return("found")
      return("Not Found ")



while True:
      ch=input("Enter Your Name:")
      if ch=='stop':
            break
      print(check(ch))





