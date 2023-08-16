# import random
from random import randint

player1 = input("Player 1, make your move:  ").lower()

rand_num = randint(0,2)
if rand_num == 0:
   computer = "rock"
elif rand_num == 1:
   computer = "paper"
else:
   computer = "scissors"

print(f"Computer plays {computer}")
print("\n")

if player1 == computer:
    print("It's a tie")
elif player1 == "rock":
    if computer == "scissors":
       print("player 1 wins!")
    else:
       print("Computer wins!")
elif player1 == "paper":
    if computer == "scissors":
       print("Computer wins!")
    else:
       print("player 1 wins!")
elif player1 == "scissors":
    if computer == "rock":
       print("Computer wins!")
    else:
       print("player 1 wins!")
else:
    print("Something went wrong!")