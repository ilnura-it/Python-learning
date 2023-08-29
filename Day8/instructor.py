instructor = {
   "name": "Instructor",
   "own_dog": True,
   "num_courses": 4,
   "favourite_languages": "Python"
}
print(instructor) # {'name': 'Instructor', 'own_dog': True, 'num_courses': 4, 'favourite_languages': 'Python'}

print(instructor.items())

print(instructor.values()) # dict_values(['Instructor', True, 4, 'Python'])
print(instructor.keys())

for value in instructor.values():
   print(value)

for v in instructor.keys():
   print(v)

for key, value in instructor.items():
   print(f"key is {key} and value is {value}")