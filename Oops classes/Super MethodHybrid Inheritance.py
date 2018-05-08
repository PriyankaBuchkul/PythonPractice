class A:
      def __init__(self):
            print("I'm From A")
class B(A):
      def __init__(self):
            print("I'm From B")
            super().__init__()

class C(A):
      def __init__(self):
            print("I'm From C")
            super().__init__()

class D(B,C):
      def __init__(self):
            print("I'm From D")
            super().__init__()

d=D()
