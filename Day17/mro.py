class A:
   def do_something(self):
      print("Method defined In: A")

class B(A):
   def do_something(self):
      print("Method defined In: B")
      super().do_something()

class C(A):
   def do_something(self):
      print("Method defined In: C")
      super().do_something()

class D(B,C):
   def do_something(self):
      print("Method defined In: D")
      super().do_something()

#print(D.__mro__)
#print(D.mro())
thing = D()
thing.do_something()