# Dictionaties

   A data structure that consists of key value pairs

      cat = {
         "name": "Kitty",
         "age": 0.5,
         "isCute": True
      }

      cat2 = dict(name="blue", age=1)

### Accessing Individual Values

     
      instructor = {
         "name": "Instructor",
         "own_dog": True,
         "num_courses": 4,
         "favourite_languages": "Python"
      }

      instructor["name"] # "Instructor"
      instructor["thing"] # KeyError

### Iterating Dictionaries

Accessing All Values in a Dictionary, use ***.values()***

      for value in instrucot.values():
         print(value)

      for key, value in instructor.items():
         print(f"key is {key} and value is {value}")

### Check if a dictionary has a key

      "name" in instructor # True
      "awesome" in instructor # False

### Check if a dictionary has a value

      4 in instructor.values() # True
      "name in instructor.values() # False

## Dictionary Methods

   - ***clear*** - clear all the keys and values in dictionary

         d = dict(a=1,b=2,c=3)
         d.clear() # {}

   - ***copy*** - make a copy of a dictionary

         c = d.copy()
         c # {'a':1, 'b':2, 'c':3}

   - ***fromkeys*** - creates key-value pairs from comma separated values. Usually used to create default dictionaries.

         {}.fromkeys("a", "b") # {'a': 'b'}
         {}.fromkeys(["email"], "unknown") # {'email': 'unknown'}
         {}.fromkeys("a", [1,2,3,4,5]) # {'a':[1,2,3,4,5]}
         new_user = {}
         new_user.fromkeys(range(1,10), 'unknown') #{1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown'}

   - ***get*** - retrieves a key in an object and return None instead of a KeyError if the key does not exist

         d = dict(a=1,b=2,c=3)
         d['a'] # 1
         d.get('a') # 1
         d.get('no_key') # None
         d['no_key'] #KeyError

         instructor.get('name') # "Instructor"