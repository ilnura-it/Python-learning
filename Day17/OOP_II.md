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

## Polymorphism

A key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph).

While a formal definition of polymorphism is more difficult, here are two important practical applications:

1. The same class method works in a similar way for different classes

         Cat.speak() # meow
         Dog.speak() # woof
         Human.speak() #yeah

2. The same operation works for different kinds of objects

         sample_list = [1, 2, 3]
         sample_tuple = (1, 2, 3)
         sample_string = "awesome"

         len(simple_list)
         len(simple_tuple)
         len(simple_string)

## Special __magic__ methods

      8 + 2 # 10
      "8" + "2" # 82

   The **+** operator is shorthand for a special method called **__add__()** that gets called on the first operand