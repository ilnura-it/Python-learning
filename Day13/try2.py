# try:
#    number = int(input('please enter a number: '))
# except:
#    print("That is not a number")
# else:
#    print("I'm in the ELSE")
# finally:
#    print("Runs no matter what")

while True:
   try:
      number = int(input('please enter a number: '))
   except ValueError:
      print("That is not a number")
   else:
      print("I'm in the ELSE")
      break
   finally:
      print("Runs no matter what")

print("rest of game code")