#Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. The function passed to it should only be invoked if there are fewer than three positional arguments passed to it. Otherwise, the inner function should return "Too many arguments!"

from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args):
        num_args = len(args)
        if num_args < 3:
            return fn(*args)
        else:
            return f"Too many arguments!"
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

# print(add_all(1))
print(add_all(1, 2, 3))