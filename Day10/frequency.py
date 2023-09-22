def frequency(list, val):
    return list.count(val)

def multiply_even_numbers(list):
    total = 1
    list2 = [num for num in list if num % 2 == 0]
    for num in list2:
        total *= num
    return total

# def multiply_even_numbers(lst):
#     total = 1
#     for val in lst:
#         if val % 2 == 0:
#             total = total * val
#     return total

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(str):
    return str[0].upper() + str[1:]

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(list):
    return [val for val in list if val]