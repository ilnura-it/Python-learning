from functools import wraps

def show_args(fn):
   @wraps(fn)
   def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
   return wrapper

@show_args
def example_function(*args, **kwargs):
    pass

# Now call the decorated function
example_function(1, 2, 3, a=1, b=2, c=3)