#This project is a bank account simulator and will include features such as adding deposits and withdrawing funds. The goal here is to learn to
#work with classes and get a grasp of OOP.

class BankAccount:
    def __init__(self, holder):
        self.holder = holder

name = input("Enter the name of the account holder: ")
new_acc = BankAccount(name)
print(new_acc.holder)

