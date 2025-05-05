# Account creation

import os
import random

Account_INDEX_FILE="Account.txt"

def genarate_Account_number():
    Acc_No=(Random(100000,999999))
    while os.path.exists(f"{Acc_no}.txt"):
        Acc_No=(Random(100000,999999))
        return Acc_No

def Create_Account():
    Name=(input("Enter Account holder name :"))
    try:
        balance=float(input("Enter initial balance :"))
        if balance < 0:
            print("Initial balance cannot be negative.")
            return 
    except ValueError :
            print("Invalid Amount.")
            return

    Acc_No=genarate_Account_number()

    with open(f"{Acc_no}.txt","w") as file:
        file.write(f"{Name}\n")
        file.write(f"{balance}\n")
        file.write(f"Transaction History:\n")
        file.write(f"Account Created with balance:{balance}\n")

    with open(Account.txt,"a")as index:
        index.write(f"{Acc_no}\n")

        print("Account Created Succesfully! Account Number:{Acc_no}")


