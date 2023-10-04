# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.

def extract_full_name(arg):
    return list(map(
            lambda x: ' '.join((x.get('first'), x.get('last'))),
            arg
        ))

# Option 2
def extract_full_name(l):
    return list(map(lambda val: f"{val['first']} {val['last']}", l))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']