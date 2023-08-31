person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {item[0]: item[1] for item in person} 
answer2 = {k:v for k,v in person}
answer3 = dict(person)
print(answer)
print(answer2)
print(answer3)