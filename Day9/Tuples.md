# Tuples

   Tuples - an ordered collection or grouping of items. ***But it is immutable!***

   - Tuples are faster than lists
   - It makes your code safer
   - Valid keys in a dictionary

      numbers = (1, 2, 3, 4)

      alphabet - ('a', 'b', 'c', 'd')
      type(alphabet) # class 'tuple'
      alphabet.append('e') # Error
      alphabet[0] # 'a'
      alphabet[0] = 'A' # Error

      locations = {
         (36.674, 39.697): "Tokyo Office",
         (40.7123, 74.0020): "New York Office",
         (37.0923, 122.3846): San Francisco Office"
      }

      cat = {"name": "Kitty", "age": 0.5, "favourite_toy": "chapstick"}
      cat.items() # dict_items([('name', 'Kitty'), ('age', 0.5), ('favourite_toy', 'chapstick')])

### Creating and Accessing

   Creating using ***()*** or the ***tuple*** function

   Accessing is just like a list!

### Looping

   We can use a ***for*** and ***while*** loop to iterate over a tuple just like a list

   names = ('Abba', 'Scorpions', 'U2')

   for name in names:
      print(name)

      # Abba
      # Scorpions
      # U2

   i = len(names) - 1
   while i >= 0:
      print(names[i])
      i -= 1

### Methods

   - ***count*** - returns the number of times a value appears in a tuple

         x = (1, 2, 3, 3, 3)
         x.count(1) # 1
         x.count(3) # 3

   - ***index*** - returns the index at which a value is found in a tuple

         t = (1, 2, 3, 3, 3)
         t.index(1) # 0
         t.index(5) # ValueError
         t.index(3) # 2 - only the first matching index


