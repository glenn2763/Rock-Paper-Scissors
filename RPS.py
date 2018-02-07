from random import randint

print ("Welcome to RPS, a basic Rock, Paper, Scissors Python game!")
name = input("What is your name?")
print ("Ok", name, "here's how it works. When I ask, 'Rock, Paper, or Scissors' you simply enter which choice you want, then I will choose one as well and we'll see who wins. Ready?")

def play():
    #Execute game, using players input against a random input
    user_choice = input("Rock, Paper, or Scissors?")
    if user_choice.lower() == "rock":
        user_choice = 1
    elif user_choice.lower() == "paper":
        user_choice = 2
    elif user_choice.lower() == "scissors":
        user_choice = 3
    else:
        print("Make sure you spelled correctly.")
        return play()
        #ensures that players input is a choice, and re-runs the play function to offer a new input if not
    computer_choice = randint(1,3)
    if user_choice == computer_choice:
        print ("It's a tie! Try again.")
    elif user_choice == 1:
        if computer_choice == 3:
            print ("I chose Scissors, looks like you have won! Congratulations!")
        else:
            print ("I chose Paper, you have lost. Try again!")
    elif user_choice == 2:
        if computer_choice == 3:
            print ("I chose Scissors, looks like you have lost. Try again!")
        else:
            print ("I chose Rock, looks like you have won! Congratulations!")
    else:
        if computer_choice == 1:
            print ("I chose Rock, looks like you have lost. Try again!")
        else:
            print ("I chose Paper, looks like you have won! Congratulations!")
    play2 = input("Would you like to play again? Y/N")
    #runs play again if the user would like to play again
    if play2.lower() == "y":
        play()
    else:
        print ("Thanks for playing!")

play()
