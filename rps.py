"""
Rock paper scissors project, I'm not going to look anything up. I'm just trying
out what I think I can do. I'm familiar with the idea it uses randomly 
generated numbers, but I don't know how to use that.
"""
import random
#First, we need to make a choice that our computer will make.
def computer_choice():
    choice = random.randint(1,3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    

# Second, we need to make some variables for what our player chooses.
# Making sure this is in a while loop so it asks again when you tie.
# Now, we just make a function to compare the values and see who won.

def compare():
    if player_choice == "rock":
        if comp_choice == "rock":
            return "It was a tie! Go again."

        elif comp_choice == "paper":
            return "You lose!"
        
        elif comp_choice == "scissors":
            return "You win!"
    if player_choice == "paper":
        if comp_choice == "paper":
            return "It was a tie! Go again."

        elif comp_choice == "scissors":
            return "You lose!"
        
        elif comp_choice == "paper":
            return "You win!"
    if player_choice == "scissors":
        if comp_choice == "scissors":
            return "It was a tie! Go again."

        elif comp_choice == "rock":
            return "You lose!"
        
        elif comp_choice == "paper":
            return "You win!"


while True:
    player_choice = input("Rock/Paper/Scissors: ").lower()
    player_choice_validity == False
    while player_choice_validity != True:
        if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            player_choice_validity = False
            player_choice = input("Rock/Paper/Scissors: ").lower()
        else:
            player_choice_validity = True
    comp_choice = computer_choice()
    result = compare()
    if result == "You win!":
        print(result)
        break
    elif result == "You lose!":
        again = input("You lose! Go again?(Y/N) ").lower()
        if again == "n":
            break
        elif again == "y":
            pass