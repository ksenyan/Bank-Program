import ClassAccounts
accountlist = []
balancelist = []
action = ''
wd_amt = 0
dep_amt = 0
balance = 0
while True:
    
    accountname = input('Enter your account name: ')
    originalname = accountname
    accountname = ClassAccounts.Account(accountname)
    
    if originalname in accountlist:
        spot = accountlist.index(originalname)
        print ('Your balance is: ')
        print (balancelist[spot])
        accountname.balance = balancelist[spot]  

    print('Would you like to deposit, withdrawl, or check your balance? (d, w, or b) ')

    action = input()

    while action != 'd' and action != 'w' and action != 'b':
        action = input('Enter your action: ')
        
    if action == 'd':
        dep_amt = int(input('Enter your deposit amount: '))
        accountname.deposit(dep_amt)
        
    if action == 'w':       
        wd_amt = int(input('Enter your withdrawl amount: '))
        accountname.withdrawl(wd_amt)
        
   
    if originalname in accountlist:
        balancelist[spot] = accountname.balance
    elif originalname not in accountlist:
        accountlist.append(originalname)
        balancelist.append(accountname.balance)
        
    print ('Your balance is: ')
    print (accountname.balance)
    print (accountlist)
    print (balancelist)
    
    if input('Would you like to make another transaction? y/n ') == 'y':
        print('Restarting')
        
    else:
        print('Thanks for banking.')
        break
    
