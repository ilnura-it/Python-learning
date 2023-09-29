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