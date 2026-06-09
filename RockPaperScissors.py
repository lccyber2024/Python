import random
import time

#clear the screen
random_choice = random.choice(['rock', 'paper', 'scissors'])
print("\033[H\033[J", end="")

#computer_choice = 'scissors'
user_choice = 'scissors'

if computer_choice == user_choice:
    print("It's a tie!")
elif (computer_choice == 'rock' and user_choice == 'scissors') or \
     (computer_choice == 'paper' and user_choice == 'rock') or \
     (computer_choice == 'scissors' and user_choice == 'paper'):
    print("Computer wins!")
else:
    print("You win!")   