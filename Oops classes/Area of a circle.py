import math  
class Circle:
      def __init__(self,r,pi=3.14):
            self.r=r
            self.pi=pi
            

      def circle_area(self):
            a=self.pi*self.r**2
            print("Area of a circle is:",a)

p=Circle(2)
p.circle_area()
   
