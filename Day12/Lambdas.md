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
