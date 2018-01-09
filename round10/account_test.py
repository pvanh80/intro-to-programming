# Intro to programming
# Classes and Objects
# Phan Viet Anh
# 256296

import bankaccount


def main():

    start_bal = float(input('Enter your starting balance: '))

    savings = bankaccount.BankAccount(start_bal)

    pay = float(input('How much did you pay for this week? '))

    savings.deposit(pay)

    print('Your account balance is $', format(savings.getBalance(), '.2f'), sep='')

    cash = float(input('How much would you like to withdraw? '))

    print('I will withdraw from the account ')

    savings.withdraw(cash)

    print('Your account balance is $', format(savings.getBalance(), '.2f'), sep='')

main()
