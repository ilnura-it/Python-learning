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

### List Methods

#### Adding to a LIST

- append - takes one argument and add to the end of the list

            data = [1, 2, 3, 4]
            data.append(5)
            # [1, 2, 3, 4, 5]

            data.append(6, 7, 8) # DOES NOT WORK!
            
            data.append([6, 7, 8]) 
            #[1, 2, 3, 4, 5, [6, 7, 8]]

- extend - to add more than one item to the end of the list

            data.extend([6, 7, 8])
            # #[1, 2, 3, 4, 5, 6, 7, 8]

- insert - insert an item at a given position

            data = [1, 2, 3, 4]
            data.insert(2, "Hi!")
            # [1, 2, "Hi!", 3, 4]

            data.insert(-1, "end!")
            # [1, 2, "Hi!", 3, "end!", 4]

            data.insert(len(data), "Last")
            # [1, 2, "Hi!", 3, "end!", 4, "Last"]

#### Removing from a LIST

- clear - clear all items

            data = [1, 2, 3, 4]
            data.clear()
            # []

- pop - remove an item at the given position, without index removes&returns last item

             data = [1, 2, 3, 4]
             data.pop()
             4
             print(data) # [1, 2, 3]

             last_item = data.pop()
             print(last_item) # 3

             data = [1, 2, 3, 4]
             data.pop(1)
             2
             print(data) # [1, 3, 4]

- remove - remove the first item from the list whose value is x

            data = [1, 2, 3, 4, 4, 4]
            data.remove(2)
            print(data) # [1, 3, 4, 4, 4]

            data.remove(4)
            print(data) # [1, 3, 4, 4] - will remove only one 4 (when you are unsure wheather the item in the list or not)