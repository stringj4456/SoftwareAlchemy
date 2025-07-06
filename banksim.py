#This project is a bank account simulator and will include features such as adding deposits and withdrawing funds. The goal here is to learn to
#work with classes and get a grasp of OOP.

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import random

bank_accounts = {}                                   # Store the bank accounts
quit_prog = False                                    # Program quit condition

#Bank account class
class BankAccount:
    def __init__(self, name, balance, number, aid):
        self.name = name                                          # Name of the account holder
        self.balance = balance                                    # Balance of the account
        self.number = number                                      # Account number
        self.aid = aid                                            # Account ID

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

#User class
class User:
    def __init__(self, username, password, aid):
        self.username = username
        self.ph = PasswordHasher()
        self.password = self.ph.hash(password)
        self.aid = aid
    
    def verify_pass(self, attempt):
        try:
            return self.ph.verify(self.password, attempt)
        except VerifyMismatchError:
            return False


#Create a new bank account function
def new_account():
    name = input("Name of the account holder: ")                  # Get the name of the account holder
    print()
    balance = float(input("Initial deposit amount: $"))           # Get the accounts intial deposit amount
    number = random.randint(100000000, 999999999)                 # Generate an account number
    aid = random.randint(1000, 5000)                              # Generate an account ID

    print()
    username = input("Please enter a username: ") 
    print()
    plaintext = input("Please enter a password: ")
    user = User(username, plaintext, aid)

    print()
    print(f"Congratulations on your new account {name}! Your unique account ID is: {aid}")

    account = BankAccount(name, balance, number, aid)             # Create the account object
    bank_accounts.update({user: account})                         # Add the object to bank_accounts dict


#Make account deposit function
def make_deposit():
    found = False
    aid = int(input("Enter your account ID: "))                         # Get the account ID
    print()
    
    #Search for the associated bank account
    for key in bank_accounts:
        if aid == key:                                                  # If the account is found
            print(f"Hello, {bank_accounts[aid].name}")
            print()
            amount = float(input("Enter the amount to deposit: $"))     # Get the deposit amount
            print()

            bank_accounts[aid].deposit(amount)                          # Call the deposit method

            print(f"Successfully deposited ${amount:.2f}")
            print()
            print(f"Your current account balance is: ${bank_accounts[aid].balance:.2f}")

            #Set the found condition and break out of the loop
            found = True
            break

    #If the account is not found
    if found == False:
        print("Could not find an associated account with that ID")


#Make account withdrawal function
def make_withdrawal():
    found = False
    aid = int(input("Enter your account ID: "))                         # Get the account ID
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


#Display account details function
def account_info():
    found = False
    aid = int(input("Enter your account ID: "))                         # Get the account ID
    print()

    #Search for the associated bank account
    for key in bank_accounts:
        if aid == key:
            print(f"Account Number: {bank_accounts[aid].number}")
            print(f"Holder: {bank_accounts[aid].name}")
            print(f"Balance: ${bank_accounts[aid].balance:.2f}")
            print(f"Account ID: {bank_accounts[aid].aid}")
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
    print("4. Display account details")
    print("5. Quit the program")
    print()


#Print the welcome message
print("Welcome to SimBank!")

#Main program loop
while quit_prog == False:

    menu_display()                                          # Display menu options
    menu_option = int(input("Enter a menu option: "))       # Get the users menu choice
    print()

    #Create a new bank account
    if menu_option == 1:
        new_account()

    #Make an account deposit
    elif menu_option == 2:
        make_deposit()
    
    #Make an account withdrawal
    elif menu_option == 3:
        make_withdrawal()
    
    #Display account details
    elif menu_option == 4:
        account_info()

    #Quit the program
    elif menu_option == 5:
        print("Thanks for visiting us. We hope to see you again soon")
        print("Goodbye!")
        quit_prog = True
        quit
