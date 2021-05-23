# register
# --first name, last name, password, email
# --generate user account

# login
# --account number and password

# bank operations

# initializing the system
import random
import validation
import database
from getpass import getpass

account_number_from_user = None


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have an account with us?: 1 (Yes) 2 (No) \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected an invalid option")
        init()


def login():
    print("======= Login =========")

    global account_number_from_user

    account_number_from_user = input("What is your account number?\n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("what is your password? \n")

        user = database.authenticate_user(account_number_from_user, password)

        if user:
            database.login_auth_session(account_number_from_user, user)
            bank_operation(user)

        print("Invalid account or password")
        login()

    else:
        print("Account number invalid. Please check that you entered exactly 10 digits")
        init()


def register():
    print("******* Register ******")

    email = input("What is your email address?:\n")
    first_name = input("What is your first name?:\n")
    last_name = input("What is your last name?:\n")
    password = getpass("Create a password for yourself \n")
    # Initial_deposit = input("How much would you be depositing today?\n")

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Congrats! Your account has been created!")
        print("== === ===== ===== === ==")
        print("Your account number is: %s" % account_number)
        print("Please make sure to keep it safe")
        print("== === ===== ===== === ==")

        login()

    else:
        print("something went wrong, please try again")
        register()


def bank_operation(user):
    print("welcome %s %s" % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit "))
    if selected_option == 1:

        deposit_operation(user)
    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    print("Withdrawal")
    current_balance = int(get_current_balance(user))
    withdrawal_amount = int(input("Enter amount to Withdraw: "))
    if withdrawal_amount > current_balance:
        print ("Your withrawal amount is greater than your current balance")
        withdrawal_amount = int(input("Enter amount to Withdraw: "))
    else:
        current_balance -= withdrawal_amount
        set_current_balance(user, str(current_balance))
    
    if database.update(account_number_from_user, user):
        print ("Your new acount balance is {}".format(current_balance))
        bank_operation(user)
    else:
        print ("Transaction not successful")
        bank_operation(user)


def deposit_operation(user):
    print("Deposit Operations")
#    print("your current balance is:", user[4])
    current_balance = int(get_current_balance(user))
    deposit_amount = int(input("Enter amount to be Deposited: \n"))
    current_balance += deposit_amount
    set_current_balance(user, str(current_balance))


    if database.update(account_number_from_user, user):
        print ("Your new acount balance is {}".format(current_balance))
        bank_operation(user)
    else:
        print ("Transaction not successful")
        bank_operation(user)



# get current balance
# get amount to deposit
# add deposit amount to current balance
# update the user file with the current balance
# display the current balance


def generate_account_number():
    return random.randrange(1111111111, 9999999999)



def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    
    login()


init()
