# Functions

- A process for executing a task
- It can accept input and return an output
- Useful for executing similar procedures over and over


### Function Structure

   ***def name_of_function ():
       # block of code***

      def say_hi():
         print('Hi!')

      say_hi()
      # Hi

### Parameters
     
      def multiplu(a, b):
         return a * b

      def multiplu(a, b):
         return a + b
### Return in Functions

      def square_of_7():
          return 7**2

### Default parameters

Anything can be as Default Parameter: functions, lists, dictionaries, strings, booleans

      def exponent(num, power=2):
         return num ** power

      print(exponent(2,3)) # 8
      print(exponent(3)) # 9 as power=2
      print(exponent(7)) # 49
