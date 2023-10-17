class User:
   def __init__(self, first, last, age):
      self.first = first
      self.last = last
      self.age = age

   def full_name(self):
      return f"{self.first} {self.last}"
   
   def initials(self):
      return f"{self.first[0]}.{self.last[0]}."
   
   def likes(self, thing):
       return f"{self.first} likes {thing}"
   
   def is_senior(self):
      return self.age >= 65
   
   def birthday(self):
      self.age += 1
      return f"Happy {self.age}th, {self.first}"

user1 = User("Joe", "Smith", 48) # 
user2 = User("Blanca", "Lopez", 27) # 

# print(user1.first, user1.last)
# print(user2.first, user2.last)

# print(user2.initials())
# print(user1.initials())
# print(user1.likes("Chips"))
# print(user2.likes("Ice Cream"))
print(user1.is_senior())
print(user2.age)
print(user2.birthday())
print(user2.age)