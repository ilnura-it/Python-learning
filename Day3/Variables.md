## Variables

   Variables should be assigned before they can be used.

      x = 100
      num_of_cats = 100
      cat_name = "Kitty"

### Variables names Restrictions

   1. Variables must start with a letter or underscore
   2. The rest of name must consist of lowercase letters letters, numbers, underscore
   3. Names are case-sensitive

### Naming conventions

   1. snake_case
   2. lowercase
   3. Constant can be UPPERCASE
   4. UpperCamelCase refers to a class
   5. Variables that start and end with underscore are supposed to be private or left alone

## Data types

   ***Data Type*** | ***Description*** |
   | :---         | :--- |
   | bool | True or False |
   | int | integer  |
   | str | string |
   | list | an ordered dequence of values of other types |
   | dict | a collection of key: values |
  
### Dynamic typing

   Dynamic typing means that variables can change types readily

### The Special Value **NONE**

   It's a version of ***null*** in Python

      child # will give error
      child = None
      type(child) # class 'NoneType'

### String Escape Characters

   - \n - new line

         new_line = "hi \nthere"

   - \ - backslash

         str = "this is a backslash: \\"
 
   - to keep quoates

         str = 'he said \"ha ha\"'

### String concatenation

### Formatting Strings

      guess = 8
      print(f"your guess of {guess} was incorrect")

## Converting Data Types

      decimal = 12.83759387593
      integer = int(decimal) # 12

      my_list = [1, 2, 3]
      my_list_str = str(my_list) # "[1, 2, 3]"