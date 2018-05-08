class Person:
      def getGender(self):
            return ""
class Male(Person):
      def getGender(self):
            return "male"
class Female(Person):
      def getGender(self):
            return "female"


a= Male()
f= Female()
print (a.getGender())
print (f.getGender())
print(dir(a))
