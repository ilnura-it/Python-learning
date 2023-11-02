class GrumpyDict(dict):
   def __repr__(self):
      print("NONE OF YOUR BUSINESS")
      return super().__repr__()
   
   def __missing__(self, key):
      print(f"YOU WANT {key}? WELL IT AINT HERE")

   def __setitem__(self, key, value):
      print("You want to change the dictionary")
      super().__setitem__(key, value)

d = GrumpyDict({"name": "Yoko", "city": "New York"})
print(d) #NONE OF YOUR BUSINESS #{'name': 'Yoko', 'city': 'New York'}
d['city']  = "SF"

print(d) # {'name': 'Yoko', 'city': 'SF'}