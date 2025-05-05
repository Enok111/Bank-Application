import random

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance):
        if initial_balance < 0:
            print("Initial balance must be non-negative.")
            return None
        
        account_number = str(random.randint(10000, 99999))  # Auto-generated account number
        while account_number in self.accounts:
            account_number = str(random.randint(10000, 99999))
        
        self.accounts[account_number] = {
            "name": name,
            "balance": initial_balance,
            "transactions": [("Initial deposit", initial_balance)]
        }
        
        print(f"Account created successfully! Your account number is {account_number}")
        return account_number

    def deposit_money(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transactions"].append(("Deposit", amount))
            print(f"Deposit successful! New balance: {self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                self.accounts[account_number]["transactions"].append(("Withdrawal", amount))
                print(f"Withdrawal successful! New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account Balance: {self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def transaction_history(self, account_number):
        if account_number in self.accounts:
            print(f"Transaction History for {account_number}:")
            for transaction in self.accounts[account_number]["transactions"]:
                print(f"{transaction[0]} - Amount: {transaction[1]}")
        else:
            print("Account not found.")

def main():
    bank = BankSystem()

    while True:
        print("\nBank System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit_money(account_number, amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw_money(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == "5":
            account_number = input("Enter account number: ")
            bank.transaction_history(account_number)
        elif choice == "6":
            print("Exiting Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
