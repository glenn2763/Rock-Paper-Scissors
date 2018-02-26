from random import randint

print ("Welcome to RPSLS, a basic Rock, Paper, Scissors, Lizard, Spock Python game!")
name = input("What is your name?")
print ("Ok", name, "here's how it works. When I ask, 'Rock, Paper, Scissors, Lizard, or Spock?'", \
        "you simply enter which choice you want, then I will choose one as well and we'll see who wins. Ready?")

rules = input("Would you like to see what beats what? Y/N")
if rules.lower() == "y":
    print ("""Rock crushes Lizard
Paper covers Rock
Scissors cuts Paper
Lizard poisons Spock
Spock smashes Scissors
Lizard eats Paper
Spock vaporizes Rock
Scissors decapitates Lizard
Paper disproves Spock
(and as it always has) Rock crushes Scissors""")

numbers_choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

streak = 0

def play(streak):
    #Execute game, using players input against a random input
    user_choice = input("Rock, Paper, Scissors, Lizard, or Spock?")
    if user_choice.lower() == "rock":
        user_choice = 1
    elif user_choice.lower() == "paper":
        user_choice = 2
    elif user_choice.lower() == "scissors":
        user_choice = 3
    elif user_choice.lower() == "lizard":
        user_choice = 4
    elif user_choice.lower() == "spock":
        user_choice = 5
    else:
        print("Make sure you spelled correctly.")
        return play()
        #Ensures that player's input is a choice, and re-runs the play function to offer a new input if not.
    computer_choice = randint(1,5)
    if user_choice == computer_choice:
        print ("It's a tie! Try again.")
        win = 2
    elif user_choice == 1:
        if computer_choice == 3 or computer_choice == 4:
            win = 1
            print ("I chose " + str(numbers_choices[computer_choice]) + ", looks like you have won! Congratulations!")
        else:
            win = 0
            print ("I chose " + str(numbers_choices[computer_choice]) + ", you have lost. Try again!")
    elif user_choice == 2:
        if computer_choice == 1 or computer_choice == 5:
            win = 1
            print ("I chose " + str(numbers_choices[computer_choice]) + ", looks like you have won! Congratulations!")
        else:
            win = 0
            print ("I chose " + str(numbers_choices[computer_choice]) + ", you have lost. Try again!")
    elif user_choice == 3:
        if computer_choice == 2 or computer_choice == 4:
            win = 1
            print ("I chose " + str(numbers_choices[computer_choice]) + ", looks like you have won! Congratulations!")
        else:
            win = 0
            print ("I chose " + str(numbers_choices[computer_choice]) + ", you have lost. Try again!")
    elif user_choice == 4:
        if computer_choice == 2 or computer_choice == 5:
            win = 1
            print ("I chose " + str(numbers_choices[computer_choice]) + ", looks like you have won! Congratulations!")
        else:
            win = 0
            print ("I chose " + str(numbers_choices[computer_choice]) + ", you have lost. Try again!")
    else:
        if computer_choice == 1 or computer_choice == 3:
            win = 1
            print ("I chose " + str(numbers_choices[computer_choice]) + ", looks like you have won! Congratulations!")
        else:
            win = 0
            print ("I chose " + str(numbers_choices[computer_choice]) + ", you have lost. Try again!")
    def win_streak(win, streak):
        if win == 1:
            streak += 1
        elif win == 0:
            streak = 0
        if streak > 0:
            print("You're on a", streak, "game win streak! See how high you can go!")
        return streak

    streak = win_streak(win, streak)

    play2 = input("Would you like to play again? Y/N")
    #runs play again if the user would like to play again
    if play2.lower() == "y":
        play(streak)
    else:
        print ("Thanks for playing!")

play(streak)
