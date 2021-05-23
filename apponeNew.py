from typing import Any, Union

balance = 100
import datetime

currentTime = datetime.datetime.now()
restart = 'Y'

database_user_account = {
    "David": "111",
    "Mike": "222",
    "Love": "333"
}


def init():
    print("Welcome to BankPHP")

    have_account = int(input("Do you have an account with us?: 1 (Yes) 2 (No) \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        print(register())
    else:
        print("You have selected an invalid option")
        init()


def login():
    print("======= Welcome to Account Login =========")
    name = input("what is your username? \n")
    password = input("Please enter your password? \n")
    if name in database_user_account and password == database_user_account[name]:
        print('Welcome %s' % name + '!' + ' current Date and Time is %s' % currentTime)
        print(bank_operations())
    else:
        print("Invalid account or password. Please try again")
        login()


def bank_operations():
    selected_option = int(
        input("What would you like to do? (1) Withdrawal (2) Cash Deposit (3) Complaint (4) Logout \n"))
    if selected_option == 1:
        withdrawal()
    elif selected_option == 2:
        cash_deposit()
    elif selected_option == 3:
        complaint()
    elif selected_option == 4:
        print('Thank you for your business')
        exit()
    else:
        print("invalid option selected")
        print(bank_operations())


def register():
    print("##### Please Register For an Account ******")

    name = input("Please choose a name?:\n")
    password = input("Create your password:\n")

    database_user_account[name] = [name, password]
    print("Congrats! Your account has been created!")
    print("== === ===== ===== === ==")
    print("Your name is: %s" % name)
    print("== === ===== ===== === ==")
    login()


def withdrawal():
    print("Withdrawal")
    int(input('How much would you like to withdraw?: '))
    print('Please take your cash')
    restart = input('Would You you like to perform another transaction? Y/N : ')
    if restart in 'N':
        print('Thank you for your business!')
    else:
        print(bank_operations())


def cash_deposit(balance=100):
    print("Cash Deposit")
    Deposit = float(input('\nHow much would you like to deposit?: '))
    balance = balance + Deposit
    print('\nYour New Balance is %s', balance)
    restart = input('Would You you like to perform another transaction? Y/N : ')
    if restart in 'N':
        print('Thank you for your business')
    else:
        print(bank_operations())


def complaint():
    print("Complaint")
    issue = input('What issue would you like to report?: ')
    print('Thank you for contacting us')
    restart = input('Would You you like to perform another transaction? Y/N : ')
    if restart in 'N':
        print('Thank you for your business')
    else:
        print(bank_operations())


init()
