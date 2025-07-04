#This project is a bank account simulator and will include features such as adding deposits and withdrawing funds. The goal here is to learn to
#work with classes and get a grasp of OOP.

import random

#Bank account class
class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name 
        self.number = number
        self.balance = balance

#Create a new bank account function
def new_account():
    name = input("Enter the name of the account holder: ")                  # Get the name of the account holder
    balance = float(input("Enter the initial deposit amount: "))            # Get the accounts intial deposit amount
    number = random.randint(100000000, 999999999)                           # Generate an account number

    print()
    print(f"Congratulations on your new account {name}! Your account number is: {number}")
    account = BankAccount(name, number, balance)

new_account()

