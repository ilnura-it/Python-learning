# Sets

   - Sets are like formal methematical sets
   - Sets do not duplicate values
   - Elements in sets aren't ordered
   - You cannot access items in a set by index
    - Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates

### Creating/Accessing

      s = sets({1, 2, 3, 4, 5, 5, 5 }) # {1, 2, 3, 4, 5} as cannot have dulicates
      numbers = [1, 2, 3, 4, 4, 4]
      sets(numbers) #{1, 2, 3, 4}

      # Creating a new set
      s = set({1, 2, 3})
      s = {1, 4, 5}

      4 in s 
      # True

      8 in s
      # False

      s[0]
      # TypeError

### Looping

      numbers = {1, 2, 3, 4, 5}

      for number in numbers:
         print(number)

      # 1
      # 2
      # 3
      # 4
      # 5

### Methods

   - ***add*** - adds an element to a set. If the element is already in the set, the set doesn't change

         s = set([1, 2, 3])
         s.add(4)
         s # {1, 2, 3, 4}
         s.add(2)
         s # {1, 2, 3, 4}

   - ***remove*** - removes an element from the set. Returns a KeyError if the value is not found. Also ***discard*** can be used

         set1 = {1, 2, 3, 4, 5, 6}
         set1.remove(3)
         set1 # {1, 2, 4, 5, 6}

   - ***copy*** - creates a copy of the set

         s = set([1, 2, 3])

         another_s = s.copy()
         another_s # {1, 2, 3}
         another_s is s # False

   - ***clear***  - removes all contents of the set

         s = set([1, 2, 3])
         s.clear()
         s # set() 

   - ***Set Math*** - Sets have a few other mathematical methods, including: 
   - intersection (&)
   - symmetric_difference
   - union (|)

### Set Comprehension

Set comprehension is useful when converting other data types to a set

      {x**2 for x in range(10)}
      # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
      {x:x**2 for x in range(10)} # we will get dictionary

      {char.upper() for char in 'hello'}
      # {'E', 'H', 'O', 'L'} as it's a set duplication is not allowed
