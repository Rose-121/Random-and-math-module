import random

options = ["Rock","Paper","Scissors"]

user_choice = input("Choose Rock, or Scissors:")

computer_choice = random.choice(options)

print("You chose:" , user_choice)
print("Computer chose:" , computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
    
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smasses scissors! you win!")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers Rock! you win!")
    
elif user_choice == "Scissor" and computer_choice == "Paper":
    print("Scissors cuts paper!You Win!")

else:
    print("You lose!!!")
    
    