# Define speak below:
def speak(str="dog"):
    if str == "pig":
        return "oink"
    elif str == "duck":
        return "quack"
    elif str == "cat":
        return "meow"
    elif str == "dog":
        return "woof"
    else:
        return "?"

#Solution 2   
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"