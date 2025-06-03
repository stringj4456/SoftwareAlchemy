#Number guessing game. Guess a number between 1-10. Simple implementation

import random

found = False                           #Game condition
target = random.randint(1, 10)          #Generate a random number
num_guesses = 0                         #Number of guesses

#Main program loop
while found == False:
    print()
    user_guess = int(input("Enter a guess: "))   #Get the users guess
    print()

    if user_guess == target:                     #If the guess is correct
        print("You guessed correctly!")
        found = True
    else:                                        #If the guess is wrong
        print("Incorrect.")

    num_guesses += 1                             #Increment guess count
    print()
    print(f"Number of guesses: {num_guesses}")

