# OOP

## Objectives

## Inheritance

 - A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).
 - In Python, inheritance works by passing the parent class as an argument to the definition of a child class:

         class Animal:
            def make_sound(self, sound):
               print(sound)

            cool = True

         class Cat(Animal):
            pass

         gandalf = Cat()
         print(isinstance(gandalf, Animal)) # True
         print(isinstance(gandalf, Cat)) # True
         gandalf.make_sound("meow") # meow
         gandalf.cool # True

### Mltiple inheritance

**Method Resolution Order(MRO)** - whenever you create a class, Python sets a Method Resolution Order, or MRO, for hat class, which is the order in which Python will look for methods on instances of that class.

You can programmatically reference the MRO three ways:
- **_mro_** attribute on the class
- use the **mro()** method on the class
- use the builtin help(cls) method