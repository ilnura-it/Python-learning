def divide(a,b):
   try:
      return a/b
   except:
      print("something went wrong")

#print(divide(1,0)) # something went wrong # None
#print(divide(1,2)) # 0.5

def divide_two(a,b):
   try:
      result =  a/b
   except ZeroDivisionError:
      print("don't divide by zero")
   except TypeError as err:
      print("a and b must be ints or floats")
      print(err)
   else:
      print(f"{a} divided by {b} is {result}")

print(divide_two(1,0)) # don't divide by zero # None
print(divide_two(1,2)) # 0.5
print(divide_two(1,'a'))