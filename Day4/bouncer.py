# ask for age
age = input("How old are you?  ")

# if age != "":
if age: # empty string means false
   age = int(age)
   if age >= 18 and age < 21:
       print("You can enter")
   elif age >= 21:
       print("yo can enter and drink")
   else:
       print("You can't come in")
else:
    print("Please enter an age")

# Another solution
# if age and (age >= 18 and age < 21):
#     print("You can enter")
# elif age and age >= 21:
#     print("yo can enter and drink")
# else:
#     print("You can't come in")