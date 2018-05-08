class Vehicle:
      def general_usage(self):#instance Method
            print("General Use:Transporattion")
class Car(Vehicle):
      def __init__(self):
            print("I'm Car")
            self.wheels=4
            self.has_roof=True

      def specific_usage(self):
            self.general_usage()
            print("Specific Usage:Commute to work.Vacation with family")
class MotorCycle(Vehicle):
      def __init__(self):
            print("I'm MOtor Cycle")
            self.wheels=2
            self.has_roof=False
      def specific_usage(self):
            self.general_usage()
            print("Specifi8-c Usage:Road Trip Racing")
      
c=Car()
c.specific_usage()
d=MotorCycle()
d.specific_usage()
