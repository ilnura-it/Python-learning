import requests
import pyfiglet 

f = pyfiglet.figlet_format("Dad Joke 3000", font="slant")
print(f)

url = "https://icanhazdadjoke.com/search"

item = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(
   url, 
   headers={"Accept": "application/json"},
   params={"term": item}
)

data = response.json()
result = data["results"]
result2 = [i["joke"] for i in result]

if len(result) < 1:
   print(f"Sorry, I don't have any jokes about {item}. Plese try again")
elif len(result) == 1:
   print(f"I've got one joke about {item}. Here it is:")
   print(result2[0])
elif len(result) > 1:
   print(f"I've got {len(result)} jokes about {item}. Here is one:")
   print(result2[0])
