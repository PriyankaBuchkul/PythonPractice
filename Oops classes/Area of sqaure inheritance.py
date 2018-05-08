class Shape:
      def __init__(self):
            print("")
      def area(self):
            return 0

class Square(Shape):
      def __init__(self,l):
            self.length=l
      def area(self):
            return self.length*self.length

s=Square(3)
print(s.area())
