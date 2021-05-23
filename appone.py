name = input ("what is your username? \n")
allowedUsers = ['David','Mike','Love']
allowedPassword = ['111','222','passwordLove']
restart=('Y')
balance = 100
import datetime
currentTime = datetime.datetime.now()


if(name in allowedUsers):
    password = input ("Your password? \n")
    userId = allowedUsers.index(name)

    if (password == allowedPassword [userId]):
        print ('Welcome %s' % name + '!' + ' current Date and Time is %s' % currentTime)
        print ('These are the available options:')
        print ('1. withdrawal')
        print ('2. Cash Deposit')
        print ('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        if selectedOption == 1:
            print ('You selected %s' %selectedOption)
            withdrawal = int(input('How much would you like to withdraw?: '))
            print ('Please take your cash')
            restart = input('Would You you like to perform another transaction? Y/N : ')
            if restart in ('N'):
                print('Thank You')
            else:
                print ('These are the available options:')
                print ('1. withdrawal')
                print ('2. Cash Deposit')
                print ('3. Complaint')

                selectedOption = int(input('Please select an option:'))
            
        
         
        elif selectedOption == 2:
            print ('you selected %s' %selectedOption)
            CashDeposit = float(input('\nHow much would you like to deposit?: '))
            balance = balance + CashDeposit
            print ('\nYour Balance is now =', balance)
            restart = input('Would You you like to perform another transaction? Y/N : ')
            if restart in ('N'):
                print('Thank You')
            else:
                print ('These are the available options:')
                print ('1. withdrawal')
                print ('2. Cash Deposit')
                print ('3. Complaint')

                selectedOption = int(input('Please select an option:'))
            
            
        elif (selectedOption == 3):
            print ('you selected %s' %selectedOption)
            Issue = input('What issue would you like to report?: ')
            print ('Thank you for contacting us')
            restart = input('Would You you like to perform another transaction? Y/N : ')
            if restart in ('N'):
                print('Thank You')
            else:
                print ('These are the available options:')
                print ('1. withdrawal')
                print ('2. Cash Deposit')
                print ('3. Complaint')

                selectedOption = int(input('Please select an option:'))

     
            
        else:
            print ('Invalid option selected, please try again')

    else:
        print ('Password incorrect, please try again')
else:
    print('Name not found, please try again')

