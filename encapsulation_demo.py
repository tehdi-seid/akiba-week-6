from tkinter import constants


class BankAccount:
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self.account_holder = account_holder

    def withdraw(self, amount):
        if amount > self.__balance:
            print("insufficient balance")

            return
        self.__balance -= amount

    def deposit(self, amount):

        self.__balance += amount
    def get_balance(self):
        return self.__balance


account = BankAccount(100, "tehdi seid")


account.withdraw(1000)
account.deposit(100)
print(account.get_balance())

# ANSWER FOR QUESTIONS

# encapsulation is just control how the datas can be accessed or modified
# we use private to protect sensitive datas from being accessed outside the class
# name mangling is a situation that python changes the name of attribute or methods that start with double underscore (__)
#

# public naming convension is an attribute or method that can be accessed outside the class
# protected is an attribute or method that can be accessed by the child classes but not outside the class
# private is  an attribute or method that can be accessed only inside the class not anywhere


# encapsulation is the way we protect the data and control access but abstraction is about hiding the implementation detail
