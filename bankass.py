import random
print("==============================#####   WELCOME   #####===================================")


accounts = {}

def create_account(name, initial_balance):
    if initial_balance < 0:
        print("Initial balance ")
        return 
    
    account_number = str(random.randint(10000, 99999)) 
    while account_number in accounts:
        account_number = str(random.randint(10000, 99999))
    
    accounts[account_number] = {
        "name": name,
        "balance":initial_balance,
        "transactions": [("Initial deposit", initial_balance)]
    }

    print(f"Account created successfully! Your account number is {account_number}")
    return account_number

