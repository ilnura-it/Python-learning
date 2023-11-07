# Iterators

**Iterator** - an object that can be iterated upon. An object which returns data, one element at a time when next() is called on it

**Iterable** - an object which will return an iterator when iter() is called on it.

         nums = [1, 2, 3, 4, 5]
         next(nums)
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         TypeError: 'list' object is not an iterator
         it = iter(nums)
         next(it)
         1
         next(it)
         2
         next(it)
         3
         next(it)
         4
         next(it)
         5
         next(it)
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         StopIteration

# Generators

- Generators are iterators
- Generators can be created with generator functions
- Generator functions use the yield keyword; can yield multiple times; when invoked, returns a generator
- Generators can be created with generator expressions

      def count_up_to(max):
        count = 1
        while count <= max:
          yield count
          count += 1

      count_up_to(5) # <generator object count_up_to at 0x00000210FED98380>

      counter = count_up_to(5)
      next(counter)
      # 1
      next(counter)
      # 2
      next(counter)
      # 3
      next(counter)
      # 4


