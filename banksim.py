#This project is a bank account simulator and will include features such as adding deposits and withdrawing funds. The goal here is to learn to
#work with classes and get a grasp of OOP.

import random

bank_accounts = {}                                   # Store the bank accounts
quit_prog = False

#Bank account class
class BankAccount:
    def __init__(self, name, balance, number, aid):
        self.name = name                                          # Name of the account holder
        self.balance = balance                                    # Balance of the account
        self.number = number                                      # Account number
        self.aid = aid                                            # Account ID

    def deposit(self, deposit):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


#Create a new bank account function
def new_account():
    name = input("Name of the account holder: ")                  # Get the name of the account holder
    print()
    balance = float(input("Initial deposit amount: $"))           # Get the accounts intial deposit amount
    number = random.randint(100000000, 999999999)                 # Generate an account number
    aid = random.randint(1000, 5000)                              # Generate an account ID

    print()
    print(f"Congratulations on your new account {name}! Your unique account ID is: {aid}")

    account = BankAccount(name, balance, number, aid)             # Create the account object
    bank_accounts.update({aid: account})                          # Add the object to bank_accounts dict

#Make account withdrawal function
def make_withdrawal():
    found = False
    aid = int(input("Enter your account ID: "))                         # Get the accound ID
    print()
    
    #Search for the associated bank account
    for key in bank_accounts:
        if aid == key:                                                  # If the account is found
            print(f"Hello, {bank_accounts[aid].name}")
            print()
            amount = float(input("Enter the amount to withdraw: $"))    # Get the withdrawal amount
            print()

            bank_accounts[aid].withdraw(amount)                         # Call the withdraw method

            print(f"Successfully withdrew ${amount:.2f}")
            print()
            print(f"Your new account balance is: ${bank_accounts[aid].balance:.2f}")

            #Set the found condition and break out of the loop
            found = True
            break

    #If the account is not found
    if found == False:
        print("Could not find an associated account with that ID")

#Display menu options function
def menu_display():
    print()
    print("1. Add a new bank account")
    print("2. Make a deposit")
    print("3. Make a withdrawal")
    print("4. Quit the program")
    print()


#Print the welcome message
print("Welcome to SimBank!")

#Main program loop
while quit_prog == False:

    menu_display()
    menu_option = int(input("Enter a menu option: "))
    print()

    if menu_option == 1:
        new_account()

    elif menu_option == 3:
        make_withdrawal()

    elif menu_option == 4:
        print("Thanks for visiting us. We hope to see you again soon")
        print("Goodbye!")
        quit_prog = True
        quit


