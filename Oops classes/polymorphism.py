import time
class Car:
      #constructor of the class
      def __init__(self,name,spd):
            self.name=name
            self.speed=spd
   #abstact Method defined by convevtion only
      def spdltm(self):
            raise NotImplementedError("Subclass Must implement abstsct method")

#define class Suv inherit Car
class suv(Car):
      #redefine a method with smae name as super class
      def spdltm(self):
            time.sleep(2)
            return 'SUV',self.speed


#define class roadster inherit Car
class roadster(Car):
      #redefine a method with smae name as super class
      def spdltm(self):
            time.sleep(2)
            return 'Roadster',self.speed

#array of objetcs

cars=[suv('toyoto foruner','250km/h'),
      roadster('Audi R8 Spyder','314hm/hr'),
      suv('Nissam V8','280km/h')]
r=roadster('Toyoto Fornuter','250km/h')
print(r.name)

for i in cars:
      print('Car Name',i.name,"Top Speed Of Your ",i.spdltm())
