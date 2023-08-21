import random

random_number = random.randint(1, 10)
print(random_number)

user_number = int(input("Enter your guess:  "))

while user_number != random_number:
   if user_number < random_number:
       print("Your number is lower! Try again!")
       user_number = int(input("Enter your guess:  "))
   elif user_number > random_number:
       print("Your number is higher! Try again!")
       user_number = int(input("Enter your guess:  "))
print("You won!")