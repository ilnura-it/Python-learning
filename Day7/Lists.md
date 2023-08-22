## LISTS
   - It's a collection og grouping of items

         tasks = ["Install Python", "Learn Python", 'Take a break"]

         ________

         first_task = "Install Python"
         second_task = "Learn Python"
         third_task = "Take a break"

         tasks = [first_task, second_task, third_task]

         demo_list = ['a', 1, 1.55, True]

   
   - *len*  - builtin function to know how many items in the list

         len(demo_list) # 4

   - *list(range(1,5))* - builtin function to make a list of numbers

         tasks = list(range(1, 4))
         tasks # [1, 2, 3]

### Accessing Values in a List

      friends = ["Ashley", "Matt", "Michael"]

   - lists ALWAYS start counting at zero. First element lives at index 0

         print(friends[0] # "Ashley')

   - you can use a negative number to index backwards

         print(friends[-1]) # "Michael"
         print(friends[-3]) # "Ashley"
         print(friends[-4]) # IndexError

### Check if a value is in a List

   - *in* builtin function

         "Ashley" in friends # True
         "Colt" in friends # False

### Iterating over Lists

   - for loop

         numbers = [1, 2, 3, 4]

         for number in numbers:
            print(number)
            # 1
            # 2
            # 3
            # 4

   - while loop

         numbers = [1, 2, 3, 4]
         i = 0
         
         while i < len(numbers):
         print(numbers[i])
         i += 1
         # 1
         # 2
         # 3
         # 4
