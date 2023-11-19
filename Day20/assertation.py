def eat_junk(food):
   assert food in ["pizza", "ice cream", "candy", "fried butter"], "food must be a junk food!"
   return f"NOm NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))