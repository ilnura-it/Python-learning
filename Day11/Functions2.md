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

## Parameter Ordering

1. parameters
2. *args
3. default parameters
4. **kwargs

        def display_info(a, b, *args, instructor="Colt", **kwargs):
            return [a, b, args, instructor, kwargs]

        print(display_info(1, 2, 3, last_name="Steele", job="Instructor")) 
        # [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]

## Using * as an Argument: Argument Unpacking

We can use * as an argument to a function to "unpack" values

    def sum_all_values(*args):
        print(args)
        total = 0
        for num in args:
            total += num
        print(total)

    nums = [1, 2, 3, 4, 5, 6]
    sum_all_values(nums) # ([1, 2, 3, 4, 5, 6],)
    # Error
    sum_all_values(*nums) # (1, 2, 3, 4, 5, 6)
    # 21

## Using ** as an Argument: Dictionary Unpacking

    def display_names(first, second):
        print(f"{first} says hello to {second}")

    names = {"first": "Colt", "second": "Rusty"}

    display_names(first="Charlie", second="Sue") # Charlie says hello to Sue

    display_names(names) # Error
    display_names(**names) # Colt says hello to Rusty