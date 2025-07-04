#This project is a bank account simulator and will include features such as adding deposits and withdrawing funds. The goal here is to learn to
#work with classes and get a grasp of OOP.

import random

bank_accounts = {}                                   # Store the bank accounts

#Bank account class
class BankAccount:
    def __init__(self, name, balance, number, aid):
        self.name = name                                          # Name of the account holder
        self.balance = balance                                    # Balance of the account
        self.number = number                                      # Account number
        self.aid = aid                                            # Account ID

    def withdraw(self, amount):
        self.balance -= amount



#Create a new bank account function
def new_account():
    name = input("Name of the account holder: ")                  # Get the name of the account holder
    balance = float(input("Initial deposit amount: "))            # Get the accounts intial deposit amount
    number = random.randint(100000000, 999999999)                 # Generate an account number
    aid = random.randint(1000, 5000)                              # Generate an account ID

    print()
    print(f"Congratulations on your new account {name}! Your unique account ID is: {aid}")

    account = BankAccount(name, balance, number, aid)             # Create the new bank account
    bank_accounts.update({aid: account})                          # Add the new account to bank_accounts dict


new_account()
