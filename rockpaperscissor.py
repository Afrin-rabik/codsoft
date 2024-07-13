import random
def play_game():
    choices=["Rock","Paper","Scissors"]
    computer_score=0
    user_score=0

    while True:
      user_choice=input("Enter your choice(R/P/S) or 'Q' to quit: ").upper()
      if user_choice=="Q":
          break


      if user_choice not in["R","P","S"]:
          print("Invalid choice.Please try again.")
          continue

      computer_choice=random.choice(choices)


      print(f"\n You chose: {user_choice}")
      print(f"Computer chose: {computer_choice}\n")


      if user_choice==computer_choice:
          print("Its a tie")
      elif (user_choice=="R" and computer_choice=="Scissors")or\
           (user_choice=="S" and computer_choice=="Paper")or\
           (user_choice=="P" and computer_choice=="Rock"):
           print("You win this round")
           user_score+=1
      else:
          print("Computer wins this round")
          computer_score+=1


      print(f"score - You:{user_score},Computer:{computer_score}\n")


    print("THANKS FOR PLAYING")
play_game()
