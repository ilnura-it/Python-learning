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

- *append* - takes one argument and add to the end of the list

            data = [1, 2, 3, 4]
            data.append(5)
            # [1, 2, 3, 4, 5]

            data.append(6, 7, 8) # DOES NOT WORK!
            
            data.append([6, 7, 8]) 
            #[1, 2, 3, 4, 5, [6, 7, 8]]

- *extend* - to add more than one item to the end of the list

            data.extend([6, 7, 8])
            # #[1, 2, 3, 4, 5, 6, 7, 8]

- *insert* - insert an item at a given position

            data = [1, 2, 3, 4]
            data.insert(2, "Hi!")
            # [1, 2, "Hi!", 3, 4]

            data.insert(-1, "end!")
            # [1, 2, "Hi!", 3, "end!", 4]

            data.insert(len(data), "Last")
            # [1, 2, "Hi!", 3, "end!", 4, "Last"]

#### Removing from a LIST

- *clear* - clear all items

            data = [1, 2, 3, 4]
            data.clear()
            # []

- *pop* - remove an item at the given position, without index removes&returns last item

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

- *remove* - remove the first item from the list whose value is x

            data = [1, 2, 3, 4, 4, 4]
            data.remove(2)
            print(data) # [1, 3, 4, 4, 4]

            data.remove(4)
            print(data) # [1, 3, 4, 4] - will remove only one 4 (when you are unsure wheather the item in the list or not)

- *index* - find an index of the specified item

            data = [5, 5, 6, 7, 5, 8, 8, 9, 10]
            data.index(6) # 2
            data.index(7) # 3
            data.index(5) # 0 - gives index of first item 
            data.index(5, 2) # 4  - we give an item and idex to start. So, it misses first two 5s

- *count* - returns the number of times an element is in the list

            data = [5, 5, 6, 7, 5, 8, 8, 9, 10]
            data.count(6) # 1
            data.count(5) # 3
            data.count(20) # 0

- *reverse* - reverse the elements of the list(in-place)

            data = [1, 2, 3, 4]
            data.reverse()
            print(data) # [4, 3, 2, 1]

- *sort* - sort the items of the list

            data = [6, 2, 3, 5, 1, 4]
            data.sort()
            print(data) # [1, 2, 3, 4, 5, 6]

- *join* - it's a string method but it's used to convert list to string

            words = ["Coding", "Is", "fun"]
            ' '.join(words) # "Coding Is fun"

            name = ['Mr', 'Steele']
            '. '.join(name) # 'Mr. Steele'

### Slicing

Make new lists using slices of the old list!

            some_list[start:end:step]

- *start* Parameter

            data = [1, 2, 3, 4]
            data[1:] # [2, 3, 4]
            data[3:] # [4]

   we can use negative number to slice from the end

            data = [1, 2, 3, 4]
            data[-1:] # [4]
            data[-3] # [2, 3, 4]

- *end* Parameter (exclusive)

            data = [1, 2, 3, 4]
            data[:2] # [1, 2]
            data[:4] # [1, 2, 3, 4] as index 4 doesn'e exist
            data[1:3] # [2, 3]
            data[0:3] == data[:3]

- *step* Parameter

            data = [1, 2, 3, 4, 5, 6]
            data[1::2] # [2, 4, 6]
            data[::2] #[1, 3, 5]

    with negative numbers, reverse the order

##### Slice with Strings

            string = "this is fun"
            string[::-1] #"nuf si siht" - reverse the string

### Modifying portions of lists

            numbers = [1, 2, 3, 4, 5]
            numbers[1:3] = ['a', 'b', 'c']

            print(numbers) # [1, 'a', 'b', 'c', 4, 5]

### Swapping Values

            names = ["James", "Anna"]
            names[0], names[1] = names[1], names[0]
            print(names) # ["Anna", "James"]

### Nested Lists

            nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            nested_list[0][1] # 2
            nested_list[-1][0] # 7

            for l in nested_list:
                  for val in l:
                        print(val)
