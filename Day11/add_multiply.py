def add_and_multiply_nums(a, b, c):
    print(a + b * c)

data = dict(a=1, b=2, c=3)

# add_and_multiply_nums(data) # TypeError: add_and_multiply_nums() missing 2 required positional arguments: 'b' and 'c'

add_and_multiply_nums(**data) # 7

def add_and_multiply_nums_kwargs(a, b, c, **kwargs):
    print(a + b * c)
    print("Other Stuff....")
    print(kwargs)

data = dict(a=1, b=2, c=3, d=55, name="Tony")
add_and_multiply_nums_kwargs(**data)
# 7
# Other Stuff....
# {'d': 55, 'name': 'Tony'}

add_and_multiply_nums_kwargs(**data, cat="blue")
# 7
# Other Stuff....
# {'d': 55, 'name': 'Tony', 'cat': 'blue'}