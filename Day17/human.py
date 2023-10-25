class Human:
   def __init__(self, first, last, age):
      self.first = first
      self.last = last
      
      if age >= 0:
         self._age = age # for internal  use 
      else:
         self._age = 0

   def get_age(self):
      return self._age
   
   def set_age(self, new_age):
      if new_age >= 0:
         self._age = new_age # for internal  use 
      else:
         self._age = 0


jane = Human("Jane", "Bill", -50)
# print(jane.age)
print(jane.get_age())
# jane.age = -100
jane.set_age(45)
print(jane.get_age())