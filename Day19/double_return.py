from functools import wraps

def double_return(fn):
   @wraps(fn)
   def wrapper(*args):
      return [fn(*args), fn(*args)]
   return wrapper

@double_return
def greet(name):
   return f"Hi, I'm {name}"

@double_return
def add(x, y):
   return x + y

print(add(1, 3))
print(greet("tony"))