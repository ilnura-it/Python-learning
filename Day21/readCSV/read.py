from csv import reader
with open("fighters.csv") as file:
   csv_reader = reader(file)
   #for row in csv_reader:
   #   # each row is a list
   #   print(row)
#   next(csv_reader) # moves us forward once
#   for fighter in csv_reader:
#      print(f"{fighter[0]} is from {fighter[1]}")
#
## Example where data is cast into a list
#from csv import reader
#with open("fighters.csv") as file:
#    csv_reader = reader(file)
#    data = list(csv_reader)
#    print(data)

# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row) 
        print(row['Name']) #Use keys to access data