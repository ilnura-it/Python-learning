# Looops

   ## for loops
      for item in iterable_object:
          # do something with item

      for char in "hello":
         print(char)

   #### range() - method generate range of numbers

      range(7) - will give integers from 0 to 6 (7 numbers)
      range(1, 5) # 1, 2, 3, 4 (will exclude 5)
      range(1, 10, 2) - will give integers from 1 to 10 with step 2 # 1, 3, 5, 7, 9
      range(7, 0, -1) - will give integers from from 7 to 1 (will exclude 0)
   
   ## while loops

      while im_tired:
         do something

   while loop continuu to execute while a certain condition is truthy, and will end when they become falsy. Require more careful setup.

   *** Be careful! If condition doesn't become false at some point, your loop will continue forever! ***
