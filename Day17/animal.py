class Animal:
   def make_sound(self, sound):
      print(f"This animal says {sound}")
   cool = True

class Cat(Animal):
   pass

blue = Cat()
print(isinstance(blue, Animal))

blue.make_sound("Meow")
print(blue.cool)
print(Cat.cool)