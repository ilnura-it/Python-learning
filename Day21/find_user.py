from csv import reader

def find_users(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader): 
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
               print(index)
        print(f"{first_name} {last_name} not found")   

find_users("a", "b")