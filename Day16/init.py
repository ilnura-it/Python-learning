class User:
   def __init__(self, first, last, age):
      self.first = first
      self.last = last
      self.age = age

user1 = User("Joe", "Smith", 48) # 
user2 = User("Blanca", "Lopez", 27) # 

print(user1.first, user1.last)
print(user2.first, user2.last)