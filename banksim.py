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
    balance = float(input("Initial deposit amount: $"))            # Get the accounts intial deposit amount
    number = random.randint(100000000, 999999999)                 # Generate an account number
    aid = random.randint(1000, 5000)                              # Generate an account ID

    print()
    print(f"Congratulations on your new account {name}! Your unique account ID is: {aid}")
    print()

    account = BankAccount(name, balance, number, aid)             # Create the new bank account
    bank_accounts.update({aid: account})                          # Add the new account to bank_accounts dict


#Display menu options function
def menu_display():
    print("1. Add a new bank account")
    print("2. Make a deposit")
    print("3. Make a withdrawal")
    print("4. Quit the program")
    print()


#Print the welcome message
print("Welcome to SimBank!")
print()

#Main program loop
while quit_prog == False:

    menu_display()
    menu_option = int(input("Enter a menu option: "))
    print()

    if menu_option == 1:
          new_account()

    elif menu_option == 4:
        print("Thanks for visiting us. We hope to see you again soon")
        print("Goodbye!")
        quit_prog = True
        quit


