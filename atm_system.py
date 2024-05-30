user_accounts = {
    5223 : 50000,
    1235 : 5000,
    1324 : 6000,
    7854 : 20000,
    8574 : 1500,
}
print('------------------------ Wellcome to Our ATM Service ------------------------')
atm_number = int(input('Enter 4 digit Pin: '))

if atm_number in user_accounts.keys():
    service_select = int(input('------------------------ Please Choose Service (1-2) ------------------------ \n 1- Balance Inquiry \n 2- Cash WithDraw \n 3- Fast Cash \n'))
    if service_select == 1:
        available_balance = user_accounts[atm_number]
        print(f'------------------------ Dear Customer, your current balance is Rs:{available_balance} ------------------------')
    elif service_select == 2:
        withdraw_amount = int(input('Please Enter Amount: '))
        if withdraw_amount <= user_accounts[atm_number]:
            user_accounts[atm_number] -= withdraw_amount
            print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        else:
             print('------------------------ Insufficient balance ------------------------')

    elif service_select == 3:
        fastCash = int(input('------------------------ Please Select Amount ------------------------ \n 1- 500 \n 2- 1000 \n 3- 1500 \n 4- 2000 \n 5- 3000 \n 6- 4000 \n 7- 5000'))
        if(fastCash == 1):
            if 500 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 500
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        elif (fastCash == 2):
            if 1000 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 1000
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        elif (fastCash == 3):
            if 1500 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 1500
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        elif (fastCash == 4):
            if 2000 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 2000
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        elif (fastCash == 5):
            if 3000 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 3000
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        elif (fastCash == 6):
            if 4000 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 4000
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
        elif (fastCash == 7):
            if 5000 <= user_accounts[atm_number]:
                user_accounts[atm_number] -= 5000
                print(f'------------------------ Please collect your cash ------------------------ \n ------------------------ Your available Balance is Rs:{user_accounts[atm_number]} ------------------------')
            else:
                print('------------------------ Insufficient balance ------------------------')
        
    else:
        print('------------------------ Invalid Input ------------------------')

else:
    print('------------------------ Your Pin is Incorrect ------------------------')

