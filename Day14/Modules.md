# Modules

- Modules used to keep Python files small
- Reuse code across multiple files by importing
- A module is just a Python file!

## Built-in Modules

      import random
      random.choice(['apple', 'orange', 'banana', 'pear'])
      random.shuffle(['apple', 'orange', 'banana', 'pear'])
      random.randint(1, 100)

      import random as rand
      rand.shuffle(['apple', 'orange', 'banana', 'pear'])

### Importing Parts of a Module

- The ***from*** keyword lets you import parts of a module
- Handy rule of thumb: only import what you need!

      from random import choice, randint

      randint(1, 100)
      choice(['apple', 'orange', 'banana', 'pear'])

      from random import choice as pick, randint as magic

      magic(1, 100)
      pick(['apple', 'orange', 'banana', 'pear'])

## Custom Modules

- You can **import** from your own code too
- The syntax is the same as before
- import from the name of the Python file
- Can be used when code will be used in more than one place
- For organising long files 

***file1***

      def fn():
         return "Hello"

      def other_fn():
         return "Bye"

***file2***

      import file1

      file1.fn() # Hello
      file1.other_fn() # Bye

- With **(import random)**, you need to specify random. before the function name.
- With **(from random import * )**, you can use functions directly without the random. prefix.

## External Modules

- Built-in modules come with Python
- External modules are dowmloaded from the internet
- You can download external modules using **pip**

      python3 -m pip install NAME_OF_PACKAGE

      python3 -m pip install autopep8 # To clean Up the code
      autopep8 --in-place exercise.py
      autopep8 --in-place -a -a exercise.py # double aggressive

      python3 -m pip install pyfiglet
      import pyfiglet
      help(pyfiglet)
