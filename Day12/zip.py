midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate':78}

grades = [pair for pair in zip(midterms, finals)]
max_grades = [max(pair) for pair in zip(midterms, finals)]
final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}

# print(grades) # [(80, 98), (91, 89), (78, 53)]
# print(max_grades) # [98, 91, 78]
# 
# print(final_grades) # {'dan': 98, 'ang': 91, 'kate': 78}

# option 2

scores = map(
   lambda pair: max(pair), 
   zip(midterms, finals)
)

print(list(scores))

final_scores = dict(
   zip(
      students,
      map(
         lambda pair: max(pair), 
         zip(midterms, finals)
      )
   )
)
print(final_scores) # {'dan': 98, 'ang': 91, 'kate': 78}