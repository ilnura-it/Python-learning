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