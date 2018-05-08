class Encapsulation_ex:
      def __init__(self):
            self.a="Public" #Public Within Class
            self._b="Private" #private instance Varible
            self.__c="Protected" #protected instance Varible
            self.___d-="Super Private" #Super Protected instance Varible
            self.____e="Testing"
f=Encapsulation_ex()

print(f.a)
print(f._b)
print(f.__c)
print(f.___d)


