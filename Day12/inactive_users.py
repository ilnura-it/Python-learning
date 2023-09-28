users = [
   {"username": "anna", "tweets": ["I love cake", "I love cats"]},
   {"username": "samuel", "tweets": ["Some tweets", "I love cats"]},
   {"username": "bekbolot", "tweets": []},
   {"username": "asher", "tweets": []},
   {"username": "rodrigo", "tweets": ["I love go to caribbeans", "I love dogs"]},
   {"username": "john", "tweets": []}
]

#inactive_users = list(filter(lambda user: not user["tweets"], users))

inactive_users = list(map(lambda user: user["username"][0].upper() + user["username"][1::],filter(lambda value: not value["tweets"], users)))
# print(inactive_users)

# List Comprehensions option
inactive2 = [user["username"][0].upper() + user["username"][1::] for user in users if not user["tweets"]]
print(inactive2)

names = ['Lassie', 'John', 'Colt', 'Margarita']

greeting = list(map(lambda n: f"Your instructor is {n}", filter(lambda value: len(value) < 5, names)))
# print(greeting)

# List Comprehensions option
greet_compr = [f"Your instructor is {n}" for n in names if len(n) < 5]
# print(greet_compr)