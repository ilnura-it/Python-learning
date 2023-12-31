#Write a function called only_ints which accepts a function and returns another function. The function passed to it should only be invoked if all of the arguments passed to it are integers. Otherwise the inner function should return "Please only invoke with integers."

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return f"Please only invoke with integers." 
        return fn(*args, **kwargs)
           
    return wrapper

@only_ints 
def add(x, y):
    return x + y

print(add(1, 2))
print(add("1", "5"))