def is_all_strings(iter):
    return all([type(x) == str for x in iter])

print(is_all_strings(['a', 'b', 'c'])) # True
print(is_all_strings([2,'a', 'b', 'c'])) # False
print(is_all_strings(('hello', 'goodbye'))) # True