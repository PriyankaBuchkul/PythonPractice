class reactagle(object):
    def __init__(self, l,b):
        self.length = l
        self.breadth=b

    def area(self):
        return self.length*self.breadth

a = reactagle(2,3)
print("Area of Reactangle is:",a.area())
