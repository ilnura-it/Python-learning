numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
print(evens)

odds = [num for num in numbers if num % 2 != 0]

[num*2 if num % 2 == 0 else num/2 for num in numbers] # [0.5, 4, 1.5, 8, 2.5, 12]

with_vowels = "This is so much fun!"

''.join(char for char in with_vowels if char not in "aeiou")

list_one = ["Elie", "Tim", "Matt"]
answer = [char[0] for char in list_one]

answer_2 =  [num for num in range(1, 101) if num % 12 == 0]

answer_3 = [char for char in "amazing" if char not in "aeoui"]

###########
