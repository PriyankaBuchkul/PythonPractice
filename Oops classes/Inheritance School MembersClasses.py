class SchoolMember:
      def __init__(self,name,age):
            self.name=name
            self.age=age
            print('(Initialized School Members :{})'.format(self.name))
                  
      def tell(self):
            print('Name :"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
       def __init__(self,name,age,salary):
            super().__init__(name,age)
            self.salary=salary
            print('(Initialized Teacher:{})'.format(self.name))

       def tell(self):
            SchoolMember.tell(self)
            print('Salary :"{}"'.format(self.salary))

            


class Student(SchoolMember):
       def __init__(self,name,age,marks):
            SchoolMember.__init__(self,name,age)
            self.marks=marks
            print('(Initialized student:{})'.format(self.name))

       def tell(self):
            SchoolMember.tell(self)
            print('Marks:"{:d}"'.format(self.marks))

t=Teacher("Mrs Priyanka ",40,30000)
s=Student('Avinash',25,46)

            
                  

      
