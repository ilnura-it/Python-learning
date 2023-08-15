### User input

      name = input("Enter your name")
      print("What is your name?")
      data = input()

### Conditional statements

      if something is True:
         do something
      elif some other condition is True:
         do something
      else:
         do something

### Truthiness

In Python, all conditional checks resolve to True or False

Beside False conditional checks, other things that are naturally falsy include:
   - empty objects
   - empty strings
   - None
   - zero

### Logical Operators
   - and
   - or
   - not

### Equal

   #### "is" vs "=="

   In python, "==" and "is" are very similar comparators, however they are not the same

         a = 1
         a == 1 # True
         a is 1 # True

         a = [1, 2, 3]
         b = [1, 2, 3]
         a == b # True (check values)
         a is b # False (check space in memory, separate object in memory)


