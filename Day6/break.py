while True:
   command = input("Type 'exit' to exit: ")
   if (command == "exit"):
      break

for num in range(1, 11):
   print(num)
   if num == 3:
      break

times = int(input("How many times do I have to tell you? "))

for time in range(1, times):
   print("Clean up your room!")
   if time >= 4:
      print("Do you even listen anymore?")
      break