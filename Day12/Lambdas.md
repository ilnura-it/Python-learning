# Lambda

In JavaScript it called Anonymous Functions - single line function

      def square(num): return num * num
      print(square(9)) # 81

      square2 = lambda num: num * num
      print(square2(7)) # 49

      add = lambda a,b: a + b
      print(add(3,10)) # 13

      print(square2.__name__) # lambda

      lambda: print(Hello)

      cube = lambda num: num ** 3

# map

A standard function that accepts at least two arguments, a function and an "iterable". Runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure.

iterable - something that can be iterated over(lists, strings, dictionaries, sets, tuples)

      nums = [1, 2, 5, 10, 5]

      doubles = list(map(lambda x: x*2 , nums))

      people = ["Anna", "John", "Darcy", "Mike"]

      peeps = map(lambda name: name.upper(), people)
      list(peeps) # ["ANNA", "JOHN", "DARCY", "MIKE"]

      names = [
         {'first': "John", 'last': 'Steele'},
         {'first': "Anna", 'last': 'Step'},
         {'first': "Juhn", 'last': 'Sting'}
      ]

      first_names = list(map(lambda x: x['first'], names))
      print(first_names) # ["John", "Anna", "Juhn"]
 
# Filter

- There is a lambda for each value in the iterable
- Returns filter object which can be converted into other iterables
- The object contains only the values that return true to the lambda

            l = [1, 2, 3, 4]
            evens = list(filter(lambda x: x % 2 == 0, l))
            evens # [2, 4]

            names = ['austine', 'penny', 'anthony', 'angel', 'billy']
            a_names = list(filter(lambda n: n[0] == 'a', names))
            a_names # ['austine', 'anthony', 'angel']

# All

- Return True if all elements of the iterable are truthy (or if the iterable is empty)

            [char for char in 'eio' if char in 'aeiou']
            # ['e', 'i', 'o']

            all([char for char in 'eio' if char in 'aeiou'])
            # True

            nums = [2, 4, 8, 20, 21]
            all([num % 2 == 0 for num in nums])
            # False

# Any

- Return True if any element of the iterable is truthy. If the iterable is empty, return False

            any([0, 1, 2, 3]) # True even if 0 is falsy

            any([val for val in [1, 2, 3] if val > 2]) # True
            any([val for val in [1, 2, 3] if val > 5]) # False

# Generator Object (Generator Expression)

- Use a generator expression if all you're doing is iterating once. If you want to store and use the generated results, then you're probably better off with a list comprehension. (Passing to a function)

       people = ["Catherine", "Clott", "John", "Chris"]

       (name[0] == "C" for name in people)
       # <generator object <genexpr> at 0x10168f048></genexpr>>

# Sorted
 - Returns a new sorted list from the items in iterable (works on everything that iterable)

            numbers = [6, 1, 8, 2]
            sorted(numbers) # [1, 2, 6, 8]
            print(numbers) # [6, 1, 8, 2]
            numbers.sort()
            print(numbers) # [1, 2, 6, 8]

            sorted(numbers, reverse=True) # [8, 6, 2, 1]

- Can accept tuples unlike sort()

- Use with lambda

            songs = [
                  {"title": "happy birthday", "playcount": 1},
                  {"title": "Survive", "playcount": 54},
                  {"title": "Toxic", "playcount": 99},
                  {"title": "Desert Rose", "playcount": 31}
            ]
            sorted(songs, key=lambda s: s["playcount"], reverse=True) # [{'title': 'Toxic', 'playcount': 99}, {'title': 'Survive', 'playcount': 54}, {'title': 'Desert Rose', 'playcount': 31}, {'title': 'happy birthday', 'playcount': 1}]

# Max and min

- ***max*** - return the largest item in an iterable or the largest of two or more arguments

            max(3, 65, 98) 
            # 98
            min(3, 65, 98)
            # 3
            max('hello world')
            # 'w'
            min('hello world')
            # ' '

            songs = [
                  {"title": "happy birthday", "playcount": 1},
                  {"title": "Survive", "playcount": 54},
                  {"title": "Toxic", "playcount": 99},
                  {"title": "Desert Rose", "playcount": 31}
            ]
            min(songs, key=lambda s: s['playcount'])
            # {'title': 'happy birthday', 'playcount': 1}

# reversed

- return a reverse iterator

            nums = [1, 2, 3, 4]
            nums.reverse()
            nums # [4, 3, 2, 1]

            reversed(nums)
            # <list_reverseiterator object at 0X102e83eb8>
            list(reversed(nums))
            # [4, 3, 2, 1]

            for char in reversed("hello"):
                  print char
            
            # o
            # l
            # l
            # e
            # h
            #"hello"[::-1] # 'olleh'

# len

            'hello'.__len__() # behind the sceens

- In OOP we can define the type of what we want

# abs

- Returns the absolute value of a number. The argument may be an integer or a floating point number

            abs(-5) # 5
            abs(5) # 5
            abs(-3.4444) # 3.4444
            abs(3.4444) # 3.4444

# sum

- Takes an iterable and optional start.
- Returns the sum of start and the items of an iterable from left to right and returns the total
- start default is 0

            sum([1, 2, 3]) # 6
            sum([1, 2, 3], 10) # 16
            sum([1, 2, 3], -6) # 0
            sum((1.5, 2, 3.7)) # 7.2
            sum({1, 50, 100}) # 151

            sum(['hi', 'there']) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
            
            sum(['hi', 'there'], '') # TypeError: sum() can't sum strings [use ''.join(seq) instead]

# round  

- Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

            round(10.2) #10
            round(1.212121, 2) #1.21
            round(3.51234) # 4
            round(3.51234, 3) # 3.512

# zip

- Make an iterator that aggregates elements from each of the iterables.
- Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
- The iterator stops when the shortest input iterable is exhausted.

            first_zip = zip([1,2,3], [4,5,6])
            list(first_zip) # [(1, 4), (2, 5), (3, 6)]
            dict(first_zip) # {1: 4, 2: 5, 3: 6}

- zip with * for unpacking

            five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
            list(zip(*five_by_two))
            # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]



