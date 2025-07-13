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

    def deposit(self, amount):                                    # Deposit funds method
        self.balance += amount

    def withdraw(self, amount):                                   # Withdraw funds method
        self.balance -= amount

#User class
class User:
    def __init__(self, username, password, aid):
        self.username = username                                # Account username
        self.ph = PasswordHasher()                              # Password hasher object
        self.password = self.ph.hash(password)                  # Password hash
        self.aid = aid                                          # Account ID
    
    def verify_pass(self, attempt):                             # Check password hash method
        try:
            result = self.ph.verify(self.password, attempt)
            return result
        except VerifyMismatchError:
            return False

#Authenticate user function
def authenticate():
    found = False       # If the account is found

    #Get the username/password
    username = input("Please enter your username: ")
    print()
    plaintext = input("Please enter your password: ")
    print()

    #Loop and search for the account
    for user in bank_accounts:
        if username == user.username and user.verify_pass(plaintext):
            index = user
            found = True
            break

    return found, index     #Return the found account condition and index of the found user

#Create a new bank account function
def new_account():
    name = input("Name of the account holder: ")
    print()
    balance = float(input("Initial deposit amount: $"))
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
    auth = authenticate()       # Authenticate the user
    found = auth[0]             # Store the found account condition
    index = auth[1]             # Store the index of the found account

    #Search for the associated bank account
    if found == True:
        name = bank_accounts[index].name
        print(f"Hello, {name}")
        print()

        deposit = float(input("Enter the deposit amount: $"))       # Deposit amount
        bank_accounts[index].deposit(deposit)                       # Call the deposit method

        print()
        print(f"Successfully deposited ${deposit:.2f}")
        print()
        print(f"Your new balance is: ${bank_accounts[index].balance:.2f}")
    
    #If the account is not found
    else:
        print("Your username or password is incorrect")


#Make account withdrawal function
def make_withdrawal():
    auth = authenticate() 
    found = auth[0]
    user = auth[1]
    
    #Search for the associated bank account
    if found == True:
        name = bank_accounts[user].name
        print(f"Hello, {name}")
        print()

        withdraw = float(input("Enter the amount to withdraw: $"))          # Withdrawal amount
        bank_accounts[user].withdraw(withdraw)                              # Call withdraw method

        print()
        print(f"Successfully withdrew ${withdraw:.2f}")
        print()
        print(f"Your new account balance is: ${bank_accounts[user].balance:.2f}")

    #If the account is not found
    else:
        print("Your username or password is incorrect")


#Display account details function
def account_info():
    auth = authenticate()       # Authenticate the user
    found = auth[0]             # Store the found account condition
    user = auth[1]              # Store the index of the found account

    #Search for the associated bank account
    if found == True:
        print(f"Account Number: {bank_accounts[user].number}")
        print(f"Holder: {bank_accounts[user].name}")
        print(f"Balance: ${bank_accounts[user].balance:.2f}")
        print(f"Account ID: {bank_accounts[user].aid}")

    #If the account is not found
    else:
        print("Your username or password is incorrect")


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
