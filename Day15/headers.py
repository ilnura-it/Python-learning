import requests
url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})

response = requests.get(url, headers={"Accept": "application/json"})

# print(response.text) but if we do type(response.text) it gives us string

data = response.json()
print(type(data)) # <class 'dict'>, now we have access to the data

print(data["joke"])