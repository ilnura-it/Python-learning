def get(d, key):
   try:
      d[key]
   except KeyError:
      return None
   
d = {"name": "Ricky"}
d["city"] # KeyError

print(get(d, "name")) # "Ricky"
print(get(d, "city")) # None