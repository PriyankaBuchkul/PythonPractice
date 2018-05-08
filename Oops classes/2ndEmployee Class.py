class Employee:
      amt=1.04 #class variable 
      def __init__(self,first,last,id,pay): #instance method/constructor of class/class initializer method
            self.first=first
            self.last=last
            self.id=id
            self.pay=pay
      def display(self):
            print("Name is:{} {} and employee Id is {} &Pay is :{}"
                  .format(self.first,self.last,self.id,self.pay))
      def raise_amt(self):
            new_pay = self.pay * self.amt + self.pay
            print("New Pay is :",new_pay)

d = Employee("Python ","Class",2,10000)
d.display()
d.raise_amt()
print("Class Variable is:",d.amt)
print("Instance VAriables are :",d.first,d.last,d.id,d.pay)


p = Employee("Priyanka ","Pawar",2,12000)
p.display()
p.raise_amt()

print("Class Variable is:",p.amt)
print("Instance VAriables are :",p.first,p.last,p.id,p.pay)

