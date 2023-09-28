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

