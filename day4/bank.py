#Build a banking system which has the following functionalities :: 
# 2.1 Add account for a new user 
# 2.2 Add money to the account
# 2.3 Withdraw money from the account 
# 2.4 Display balance for a particular user


user_name = input('Enter username')
function= ' '
Account = {
        'a':10000,'b':20
    }
while(function != '0'):
    function = input('Enter the required operation: \n 1 Add account for a new user \n 2 Add money to the account \n 3 Withdraw money from the account \n 4 Display balance for a particular user \n Press 0 to EXIT')

    

    def add_account(username):
        Account[username] = 0
        print('Account added successfully')
        print(Account)

    def add_money(username):
        print(username)
        print(Account)
        if(username in Account):
            amt = float(input('Enter a valid amount'))
            Account[username] += amt
            print('Amount added succesfully')
        else:
            print('Invalid User')

    def withdraw_money(username):
        print(Account)
        if(username in Account):
            w_amt = float(input('Enter a valid amount'))
            if(w_amt > Account[username]):
                print('Insufficient balance')
            else:
                Account[user_name] -= w_amt
                print('Amount withdrawn successfully')
        else:
            print('Invalid User')
    def display_balance(username):
        print('Balance : ' +str(Account[username])) 

    if function == '1':
        add_account(user_name)
    elif function == '2':
        add_money(user_name)
    elif function == '3':
        withdraw_money(user_name)
    elif function == '4':
        display_balance(user_name)
    else:
        print('Wrong input')

