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