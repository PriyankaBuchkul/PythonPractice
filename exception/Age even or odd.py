#age

def age_getter(age):
      if age < 0:
            raise ValueError ('Only positive intergerd allowed')
      if age %2 == 0:
            print("Age is Even")
      else:
            print("Age is Odd")

while True:
      n=int(input("Enter any age :"))
      if n=="d":
            break
      else:
            try:
                  age_getter(n)
            except ValueError as e:
                  print(e)

'''
age = int(input("Enter the Age :"))
try:
      if age%2==0:
            print("Even")
except ValueError as e:
      print("Not Even")
      print('"%s" odd:%s'.format(age,e))


print("Age is {} ".format(age))
'''
