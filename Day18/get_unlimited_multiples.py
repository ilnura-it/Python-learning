# def get_unlimited_multiples(num = 7):
#     new_num = num
#     for i in range(1, num + 1):        
#         new_num = num * i
#         yield new_num

def get_unlimited_multiples(num = 1):
    new_num = num
    while True:
        yield new_num
        new_num += num

multiply = get_unlimited_multiples(6)
print(next(multiply))
print(next(multiply))
print(next(multiply))
print(next(multiply))
print(next(multiply))
print(next(multiply))