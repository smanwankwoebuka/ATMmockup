import random
database ={
   'Ebuka':'passwordEbuka',
    'Stephen':'passwordStephen',
    'John':'passwordJohn'
   
}

def init():
     isValidOptionSelected= False
     print('welcome to bankSwift')

     while isValidOptionSelected== False:

         haveAccount=int(input('Do you have an account with us: 1 (Yes)  2 (No)\n'))

         if (haveAccount ==1):
             isValidOptionSelected= True
             login()
         elif (haveAccount ==2):
             isValidOptionSelected= True
             register()
         else:
             print('you have selected invalid option')
        
def login():
    #login function here
    print('log in to your account')
    while isLoginSuccessful=False:
        accountNumberFromUser=int(input('what is your account number?\n'))
        password=input('what is your password?\n')

        for accountNumber, userDetails in database.items():
            if(accountNumber== accountNumberFromUser):
                if(userDetails[3]==password):
                    isloginSuccessful =True
         print('invalid account or password')
     bankOperation()

        


def bankOperations():

    from datetime import datetime
    date = datetime.now()
    print(date)
    
    print('These are the available options:\n')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    
    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        print('How much would you like to withdraw')
        Amount_withdraw = input('Enter the amount here: \n')
        print('please, take your cash')
        bankOperations()
                
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        print('How much would you like to deposit?')
        Amount_input = int(input('Enter the amount here: \n'))
        balance = 0.00
        Amount_deposit = Amount_input + balance
        print('Your current balance is %s' % Amount_deposit)
        bankOperations()
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        print('What issue will you like to report?')
        issue=input('Enter the issue here:\n')
        print('Thank you for contacting us')
        bankOperations()

    elif(selectedOption == 4):
        exit()   
    else:
        print('Invalid Option selected, please try again')


def generationAccountNumber():
    
    #print('Generating account number')
    return random.randrange(1111111111,9999999999)

def register():
    print('*******Register*******')
    email:input('what is your email address?\n')
    first_name=input('what is your first name?\n')
    last_name=input('what is your last name?\n')
    password = input('create password\n')
    accountnumber= generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]
    return database
    print('registration successful!')
    login()
    

#print("Welcome, what would you like to do?")
#print("1. Login")
#print("2. Register")
#print('3. Generate Account Number')
#actionSelect = int(input("Select an option \n"))

#if(actionSelect == 1):
#   isLoginSuccessful = False

#    while isLoginSuccessful == False:
#        isLoginSuccessful = login()

#    bankOperations()

#elif(actionSelect == 3):
#    print(generationAccountNumber())
    
#else:
#    print('Login failed, username or password incorrect')


print(init())

    
