# OOP

- Object oriented programming is a method of programming that attempts to model some process or thing in the world as a ***class*** or ***object***

- ***class*** - a blueprint for objects. Classes can contain methods (functions) and attributes(similar to keys in a dict)

- ***instance*** - objects that are constructed from a class blueprint that contain their class's methods and properties.

- With object oriented programming, the goal is to ***encapsulate*** your code into **logical, hierarchical groupings using classes** so that you can reason about your code at a higher level.

- **Encapsulation** - the grouping of public and private attributes and methods into a programmatic class, making **abstraction** possible.

## Creating a class

      class User:
         pass

      user1 = User()

- Classes in Python can have a special __init__ method, which gets called every time you create an instance of the class (instantiate).

class Vehicle:

   def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

- The **self** keyword refers to the current class instance. **self** must always be the first parameter to **__init__** and any methods and properties on class instances.

## Undescores

      class Person:
         def __init__(self):
         self.name = "Tony"
         self._secret = "hi"
         self.__msg = "I like coffee" 
         
         
         print(p.__msg) # AttributeError: "Person' object has no attribute '__msg'
         print(p._Person__msg) # I like coffee


      _secret - private variable that not supposed to be accessed from outside of class

      __msg

      __name__ - used for Python specific methods

