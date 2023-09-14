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
      cat.items()
      # dict_items([('name', 'Kitty'), ('age', 0.5), ('favourite_toy', 'chapstick')])

### Creating and Accessing

   Creating using ***()*** or the ***tuple*** function

   Accessing is just like a list!
  