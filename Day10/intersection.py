# flesh out intersection pleaseeeee
def intersection(list1, list2):
    return [val for val in list1 if val in list2]

print(intersection([1,2,3], [2,3,4]))
print(intersection(['a','b','z'], ['x','y','z']))

# def intersection(list1, list2):
#     return [val for val in set(list1) & set(list2)]