#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    r_list = list(range(1, 50))
    return [num for num in r_list if num % 2 == 0]

print(generate_evens()) 