#self keyword, class variables
class demo:
      a=10  #class variable
      def fun(self):
            print("this is fun variable :")
            b=29   #function variable,instance Variable
            print("B is :",b)



d=demo()  #object of a class/instance of a class
d.fun()# function Call
