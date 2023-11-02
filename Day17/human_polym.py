from copy import copy

class Human:
   def __init__(self, first, last, age):
      self.first = first
      self.last = last
      self.age = age

   def __repr__(self):
      return f"Human named {self.first} {self.last}"
   
   def __len__(self):
      return self.age
   
   def __add__(self, other):
      if isinstance(other, Human):
         return Human(first = "Newborn", last = self.last, age = 0)
      return "You can't add that"
   
   def __mul__(self, other):
      if isinstance(other, int):
         return [copy(self) for i in range(other)]
      return "You are multiplying Humans"
   
j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
#print(j)
#print(len(j))

#print(j + k) # Human named Newborn Larsen
#print(j + 2) # You can't add that
#print(j * 2) # You are multiplying Humans

#triplets = j * 3
#triplets[1].first = "Jessica"
#print(triplets) # [Human named Jessica Larsen, Human named Jessica Larsen, Human named Jessica Larsen]
#
#print(triplets) # [Human named Jenny Larsen, Human named Jessica Larsen, Human named Jenny Larsen]

triplets = (k + j) * 3
print(triplets) # [Human named Newborn Jones, Human named Newborn Jones, Human named Newborn Jones]