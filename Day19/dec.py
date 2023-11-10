def be_polite(fn):
   def wrapper():
      print("What a pleasure to meet you!")
      fn()
      print("Have a good day")
   return wrapper

# Decorators method
@be_polite
def greet():
   print(f"My name is  Aabb")

@be_polite
def rage():
   print("I hate you")   

greet()
rage()

# How we used to use
# def greet():
#    print(f"My name is  Aabb")
# 
# def rage():
#    print("I hate you")   
# 
# greet = be_polite(greet)
# polite_rage = be_polite(rage)
# greet()
# polite_rage()