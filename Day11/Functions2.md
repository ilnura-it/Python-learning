# Functions

### *args

- ****args*** - a special operator we can pass to functions. Gather remaining arguments as a tuple. This is just a parameter - you can call it whatever you want.

      def sum_all_nums(num1, num2, num3):
          return num1 + num2 + num3

- We have limitanions in number of arguments

      def sum_all_nums(*args):
          print(args)

      print(sum_all_nums(4,6,9,7,3)) # (4, 6, 9, 7, 3) - tuple
      print(sum_all_nums(4,6)) # (4, 6) - tuple

- We need to iterate through the tuple

      def sum_all_nums(*args):
          total = 0
          for num in args:
               total += num
          return total

      print(sum_all_nums(4,6,9,7,3)) # 33
      print(sum_all_nums(4,6)) # 10

- We can also add more arguments

      def sum_all_nums(num1, *args):
          print(num1)
          total = 0
          for num in args:
               total += num
          return total

      print(sum_all_nums(4,6,9,7,3)) 
      # 4
      # 29
      print(sum_all_nums(4,6)) 
      # 4
      # 6

### **kwargs

- *****kwargs*** - a special operator we can pass to functions
- Gathers remaining keyword arguments as a dictionary
- This is just a parameter - you can call it whatever you want!

