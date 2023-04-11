# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date:  10/03/2022
# Description:  Take an integer input from the user, and then have them (or someone else) guess the number

print("Enter the integer for the player to guess.")
num_to_guess = int(input())
right_guess = False
num_of_guesses = 0

print("Enter your guess.")
while not right_guess:
    num_of_guesses += 1
    guess = int(input())
    if guess == num_to_guess and num_of_guesses == 1:
        print("You guessed it in 1 try.")
        right_guess = True
    elif guess < num_to_guess:
        print("Too low - try again:")
    elif guess > num_to_guess:
        print("Too high - try again:")
    else:
        print(f"You guessed it in {num_of_guesses} tries.")
        right_guess = True
