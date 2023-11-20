## Why test?

- Reduce bugs in existing code
- Ensure bugs that are fixed stay fixed
- Ebsure that new features don't break old ones
- Ensure that cleaning up code doesn't introduce new bugs
- Makes development more fun

## Test Driven Development

- Development begins by writing tests
- Once tests are written, write code to make tests pass
- Once tests pass, a feature is considered complete

## Red, Green, Refactor

1. Red - Write a test that fails
2. Green - Write the minimal amount of code necessary to make the tests pass
3. Refactor - Clean up the code, while ensuring that tests still pass

## Assertions

- We can make simple assertionswith the **assert** keyword
- **assert** accepts an expression
- Returns ***None*** if the expression is truthy
- Raises an AssertionError if the expression is falsy
- Accepts an optional error message as a second argument

         def add_positive_numbers(x, y):
            assert x > 0 and y > 0, "Both numbers must be positive"
            return x + y

         add_positive_numbers(1, 1) # 2
         add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive

- If a Python files is run with the flag -O, assertions will not be evaluated!

## Doctests

         def add(x, y):
         """ add together x and y

         >>> add(1, 2)
         3

         >>> add(8, "hi")
         Traceback (most recent call last):
           ...
         TypeError: unsupported operand type(s) +: 'int' and 'str'
         """
 ### Issues with doctests

 - Syntax is a little strange
 - Clutters up our function code
 - Lack many features of larger testing tools
 - Tests can be brittle

 ## Unittest

 ### Unit testing:

 - Test smallest parts of an application in isolation (e.g. units)
 - Good candidates for unit testing: individual classes, modules, or functions
 - Bad candidates for unit testing: an entire application, dependencies across several classes or modules

 ### unittest

 - Python comes with a built-in module called unittest
 - You can write unit tests encapsulaed as classes that inherit from unittest .TestCase
 - This inheritance gives you access to many assertion helpers that let you test the behavior of your functions
 - You can run tests by calling unittest.main()