print("Rock...")
print("Scissors...")
print("Paper...")

player1 = input("Player 1, make your move:  ")
print("***NO CHEATING!\n" * 20)
computer = input("Player 2, make your move:  ")

if player1 == computer:
    print("It's a tie")
elif player1 == "rock":
    if computer == "scissors":
       print("player 1 wins!")
    elif computer == "paper":
       print("player 2 wins!")
elif player1 == "paper":
    if computer == "scissors":
       print("player 2 wins!")
    elif computer == "rock":
       print("player 1 wins!")
elif player1 == "scissors":
    if computer == "rock":
       print("player 2 wins!")
    elif computer == "paper":
       print("player 1 wins!")
else:
    print("Something went wrong!")
