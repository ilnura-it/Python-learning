# Write a function called delay which accepts a time and returns an inner function that accepts a function. When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it. Before starting the timer, delay will also print a message informing the user that there will be a delay before the decorated function gets run.

from functools import wraps
from time import sleep

def delay(val):
   def inner(fn):
      @wraps(fn)
      def wrapper(*args, **kwargs):
         if val > 0:
            print(f"Waiting {val}s before running {fn.__name__}")
            sleep(val)
         return fn(*args, **kwargs)
      return wrapper
   return inner

@delay(5)
def say_hi():
    return "hi"

print(say_hi())