class person:
      def __init__(self,first,last):
            self.firstnm=first
            self.lastnm=last

      def name(self):
            return self.firstnm+" "+self.lastnm

class Employee(person):#derived class
      #DRY: Dont Repeat Yourself
      def __init__(self,first,last,staffnum):
            person.__init__(self,first,last)
            self.staffnumber=staffnum

      def GetEmployee(self):
            return self.name()+" , "+self.staffnumber

y=Employee("Homer","Simpson","1007")#Object of a class
print(y.GetEmployee())
