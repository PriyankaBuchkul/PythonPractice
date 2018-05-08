class InputString:
      def __init__(self):
            self.str=" "

      def getstring(self):
            self.str=input("Enter The String :")

      def printstring(self):
            print(self.str.upper())

      def test(self):
            print("I'm In Test Method")

p=InputString()
p.getstring()
p.printstring()
            
p.test()
