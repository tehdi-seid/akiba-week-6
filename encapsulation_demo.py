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