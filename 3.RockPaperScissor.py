import random

#Rules Rock > Scissor, Scissor > Paper, Paper > Rock
def game():
    user = input("Rock Paper of Scissor?: ").lower().strip()
    comp = random.choice(['rock','paper','scissor'])
    
    if (user == "rock" and comp == "scissor") or (user == "scissor" and comp == "paper") or (user == "paper" and comp == "rock"):
        print("You win!")
    elif (comp == "rock" and user == "scissor") or (comp == "scissor" and user == "paper") or (comp == "paper" and user == "rock"):
        print("Computer Wins")
    elif user == comp:
        print("It's a tie!")
    else:
        print("Enter a valid input: Rock, Paper of Scissor")

game()
