
admin_id=(input("Enter the admin ID: "))
cus_ID=0
account_number=20020


print("==============================#####   WELCOME   #####===================================")

while admin_id == "1001":
    print("=== Bank Menu ===" )
    print("1.Create customer")
    print("2.Create Account")
    print("3.Deposit money")
    print("4.Check balance")
    print("5.Transaction History ")
    print("6.Exit")
    print("***********")

    Choice=input("choose an option from [1-6]: ")
    if Choice == "1":
        Cus_name=(input("Enter the customer Name: "))
        Cus_pswrd=(input("Enter the customer Password: "))
        Balance=(input("Enter your Initfical Balance: "))
        print("Account created successfully!")
        

    if Choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        print("Deposit done" , Balance)

    if choice == "2":
        Accounts = {}

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



    if Choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        print("Deposit done" , Balance)















































































































