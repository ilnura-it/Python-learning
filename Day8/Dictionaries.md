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