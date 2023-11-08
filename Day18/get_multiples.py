def get_multiples(num = 1, count = 10):
   next_num = num
   while count > 0:
      yield next_num
      count -= 1
      next_num = next_num + num

evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))

