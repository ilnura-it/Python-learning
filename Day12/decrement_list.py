def decrement_list(arr):
    return list(map(lambda x: x - 1, arr))

print(decrement_list([1,2,3])) # [0,1,2]
print(decrement_list([20,14,11])) # [19,13,10]