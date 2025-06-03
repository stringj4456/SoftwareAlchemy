#Number guessing game. Guess a number between 1-10. Simple implementation

import random

found = False                           #Game condition
target = random.randint(1, 10)          #Generate a random number

#Main program loop
while found == False:
    print()
    guess = int(input("Enter a guess: "))   #Get the users guess
    print()

    if guess == target:                     #If the guess is correct
        print("You guessed correctly!")
        found = True
    else:                                   #If the guess is wrong
        print("Incorrect.")

