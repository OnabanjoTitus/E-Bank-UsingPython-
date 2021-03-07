from Bank import *


def Transactions():
    try:
        TransactionType = int(input("Enter 1 for Withdrawal\nEnter 2 for Deposit\nEnter 3 for Transfer"))
        if TransactionType == 1:
            try:
                AccountNumber = input("Enter Customer AccountId")
                if BankRecordsForAccountTypes[AccountNumber]:
                    try:
                        AccountPin = int(input("Enter Customer Pin"))
                        if CustomerPinsRecords[AccountNumber] == AccountPin:
                            Amount = int(input("Enter Amount To withdraw"))
                            print(BankRecordsForAccountTypes[AccountNumber])

                    except ValueError as v:
                        print("Invalid Pin")
            except KeyError as k:
                print("Invalid User Detail")
    except ValueError as v:
        print("Invalid User Input")
