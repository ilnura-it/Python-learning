nums = [1, 2, 3]

nums2 = [x*10 for x in nums] # manipulate each time in a list

print(nums2)

# Without comprehension
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)

# With comprehension

numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

############

name = 'ilnura'
name_upper = [char.uppper() for char in name]
print(name_upper)

##############
friends = ['ashley', 'matt', 'michael']
friends_upper = [friend[0].upper() + friend[1:] for friend in friends]
print(friends_upper)

##############

[num * 10 for num in range(1, 6)] # [10, 20, 30, 40, 50]

###############

[bool(val) for val in [0, [], '']] # [False, False, False] as empty string, empty list and 0 always False

###############
number = [1, 2, 3, 4, 5]

string_list = [str(num) for num in numbers]

print(string_list)