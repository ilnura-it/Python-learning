from functools import wraps

def log_function_data(fn):
   @wraps(fn)
   def wrapper(*args, **kwargs):
      print(f"you are about to call {fn.__name__}")
      print(f"Here's the documentation: {fn.__doc__}")
      return fn(*args, **kwargs)
   return wrapper

@log_function_data
def add(x, y):
   """ADS two numbers together"""
   return x + y

print(add.__doc__)
print(add.__name__)
help(add)


# def log_function_data(fn):
#    def wrapper(*args, **kwargs):
#       print(f"you are about to call {fn.__name__}")
#       print(f"Here's the documentation: {fn.__doc__}")
#       return fn(*args, **kwargs)
#    return wrapper
# 
# @log_function_data
# def add(x, y):
#    return x + y

print(add(10, 30))