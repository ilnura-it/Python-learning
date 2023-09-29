users = [
   {"username": "anna", "tweets": ["I love cake", "I love cats"]},
   {"username": "samuel", "tweets": ["Some tweets", "I love cats"]},
   {"username": "bekbolot", "tweets": []},
   {"username": "asher", "tweets": []},
   {"username": "rodrigo", "tweets": ["I love go to caribbeans", "I love dogs"]},
   {"username": "john", "tweets": []}
]

sorted(users, key=lambda user: user['username'])
sorted(users, key=lambda user: len(user['tweets']), reverse = True)