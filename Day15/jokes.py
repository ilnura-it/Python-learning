import requests
import pyfiglet
import random
from colorama import init
from termcolor import colored

init()

header = pyfiglet.figlet_format("Dad Joke 3000")
header = colored(header, color="cyan")
print(header)

url = "https://icanhazdadjoke.com/search"
item = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
   url, 
   headers={"Accept": "application/json"},
   params={"term": item}
).json()

total_jokes = response["total_jokes"]
res = response["results"]
# result = [i["joke"] for i in res]

if total_jokes == 1:
   print(f"I've got one joke about {item}. Here it is:")
   print(res[0]["joke"])
elif total_jokes > 1:
   print(f"I've got {total_jokes} jokes about {item}. Here is one:")
   print(random.choice(res)["joke"])
else:
   print(f"Sorry, I don't have any jokes about {item}. Plese try again")