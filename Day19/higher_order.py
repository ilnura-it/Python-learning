def sum(n, func):
   total = 0
   for num in range(1, n+1):
      total += func(num)
   return total

def square(x):
   return x*x

def cube(x):
   return x*x*x

print(sum(3, square)) # 14
# 1 2 3
# 1 4 9 = 14

print(sum(3, cube)) # 36
