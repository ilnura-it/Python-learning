from random import randint

player_wins = 0
computer_wins = 0

while computer_wins < 2 and computer_wins < 2:
   print(f"Player score is: {player_wins}  Computer score is: {computer_wins}")
   print("Rock...")
   print("Scissors...")
   print("Paper...\n")
   
   player1 = input("Make your move:  ").lower()
   
   rand_num = randint(0,2)
   if rand_num == 0:
      computer = "rock"
   elif rand_num == 1:
      computer = "paper"
   else:
      computer = "scissors"
   
   print(f"Computer plays {computer}\n")
   
   if player1 == computer:
       print("It's a tie")
   elif player1 == "rock":
       if computer == "scissors":
          print("Player wins!\n")
          player_wins += 1
       else:
          print("Computer wins!\n")
          computer_wins += 1
   elif player1 == "paper":
       if computer == "scissors":
          print("Computer wins!\n")
          computer_wins += 1
       else:
          print("Player wins!\n")
          player_wins += 1
   elif player1 == "scissors":
       if computer == "rock":
          print("Computer wins!\n")
          computer_wins += 1
       else:
          print("Payer wins!\n")
          player_wins += 1
   else:
       print("Something went wrong!")

if player_wins > computer_wins:
   print("Congratulations to Player!\n")
elif (computer_wins < player_wins):
   print("Congratulations to computer!\n")