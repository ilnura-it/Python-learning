msg = input("what the secret password? ").lower()
while msg != "bananas":
    print("Wrong!")
    msg = input("what the secret password? ").lower()
print("Correct")

num = 1
while num <= 10:
    print(num)
    num += 1