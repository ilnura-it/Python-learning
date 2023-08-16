print("Rock...")
print("Scissors...")
print("Paper...")

player1 = input("Player 1, make your move:  ")
computer = input("Player 2, make your move:  ")

if player1 == "rock" and computer == "scissors":
    print("player 1 wins")
elif player1 == "rock" and computer == "paper":
    print("player 2 wins")
elif player1 == "paper" and computer == "rock":
   print("player 1 wins")
elif player1 == "paper" and computer == "scissors":
    print("player 2 wins")
elif player1 == "scissors" and computer == "rock":
    print("player 2 wins")
elif player1 == "scissors" and computer == "paper":
    print("player 1 wins")
elif player1 == computer :
    print("It's a tie")
else:
    print("Something went wrong!")

