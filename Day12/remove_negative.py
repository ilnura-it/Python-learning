def remove_negatives(l):
    return list(filter(lambda num: num >= 0, l))

print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,4,5]))
print(remove_negatives([50,60,70]))