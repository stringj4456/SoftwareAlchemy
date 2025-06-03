#Number guessing game. Guess a number between 1-10.

import random

found = False                           #Game condition
target = random.randint(1, 10)          #Generate a random number
num_guesses = 0                         #Number of guesses
attempts = 3                            #Number of attempts
sub_attempt = attempts                  #Count down for attempts

#Main program loop
while found == False:
    #Check number of attempts
    if num_guesses == attempts:
        print()
        print("Sorry but you've ran out of guesses.")
        print("Better luck next time!")
        exit()

    #Get the users guess
    user_guess = int(input("Enter a guess: "))
    print()

    #Increment/decrement number of guesses/attempts
    num_guesses += 1 
    sub_attempt -= 1 

    #Guess conditions
    if user_guess == target:
        print("You guessed correctly!")
        print("Nice job!")
        found = True
    else:
        print("Incorrect.")
        if sub_attempt != 0:
            print(f"You have {sub_attempt} attempts left.")
            print()
