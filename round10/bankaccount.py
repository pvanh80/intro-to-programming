# Intro to programming
# Classes and Objects
# Phan Viet Anh
# 256296


class BankAccount:

    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):

        self.__balance +=amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance-=amount
        else:
            print('Error: Insufficient Funds')

    def getBalance(self):

        return self.__balance
