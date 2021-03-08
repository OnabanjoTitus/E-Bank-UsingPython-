def Transactions(BankRecordsForAccountTypes, CustomerPinsRecords, CustomerAccountBalance):
    try:
        TransactionType = int(input("Enter 1 for Withdrawal\nEnter 2 for Deposit\nEnter 3 for Transfer"))
        if TransactionType == 1:
            try:
                AccountNumberForSender = input("Enter Customer AccountId")
                if BankRecordsForAccountTypes[AccountNumberForSender]:
                    try:
                        AccountPin = int(input("Enter Customer Pin"))
                        if CustomerPinsRecords[AccountNumberForSender] == AccountPin:
                            Amount = int(input("Enter Amount To withdraw"))
                            if Amount < CustomerAccountBalance[AccountNumberForSender]:
                                CustomerAccountBalance[AccountNumberForSender] = CustomerAccountBalance[
                                                                                     AccountNumberForSender] - Amount
                                ReturnValue = AccountNumberForSender, CustomerAccountBalance[AccountNumberForSender]
                                return ReturnValue
                            else:
                                print("Insufficient Fund")
                                ReturnValue = AccountNumberForSender, CustomerAccountBalance[AccountNumberForSender]
                                return ReturnValue
                    except ValueError as v:
                        print("Invalid Pin")
            except KeyError as k:
                print("Invalid User Detail")
        if TransactionType == 2:
            try:
                AccountNumberForSender = input("Enter Customer AccountId")
                if BankRecordsForAccountTypes[AccountNumberForSender]:
                    try:
                        Amount = int(input("Enter Amount To Deposit"))
                        if Amount > 0:
                            CustomerAccountBalance[AccountNumberForSender] = CustomerAccountBalance[
                                                                                 AccountNumberForSender] + Amount
                            ReturnValue = AccountNumberForSender, CustomerAccountBalance[AccountNumberForSender]
                            return ReturnValue
                        else:
                            print("Insufficient Fund")
                            ReturnValue = AccountNumberForSender, CustomerAccountBalance[AccountNumberForSender]
                            return ReturnValue
                    except ValueError as v:
                        print("Invalid Pin")
            except KeyError as k:
                print("Invalid User Detail")
        if TransactionType == 3:
            try:
                AccountNumberForSender = input("Enter Sender Bank AccountId")
                if BankRecordsForAccountTypes[AccountNumberForSender]:
                    try:
                        AccountPin = int(input("Insert AccountPin"))
                        if CustomerPinsRecords[AccountNumberForSender] == AccountPin:
                            print(CustomerAccountBalance[AccountNumberForSender])
                            Amount = int(input("Enter the Amount You Want To Transfer"))
                            if 0 <= Amount < CustomerAccountBalance[AccountNumberForSender]:
                                AccountNumberForReceiver = input("Enter Receiver AccountId")
                                if BankRecordsForAccountTypes[AccountNumberForReceiver]:
                                    CustomerAccountBalance[AccountNumberForSender] = CustomerAccountBalance[
                                                                                         AccountNumberForSender] - Amount
                                    ReturnValue1 = AccountNumberForSender, CustomerAccountBalance[
                                        AccountNumberForSender]
                                    CustomerAccountBalance[AccountNumberForReceiver] = \
                                        CustomerAccountBalance[AccountNumberForReceiver] + Amount
                                    ReturnValue2 = AccountNumberForReceiver, \
                                                   CustomerAccountBalance[AccountNumberForReceiver]
                                    print(CustomerAccountBalance[AccountNumberForReceiver])
                                    print(CustomerAccountBalance[AccountNumberForSender])
                                    ReturnValues = ReturnValue1, ReturnValue2
                                    return ReturnValues
                    except ValueError as v:
                        print("Invalid Pin")
            except KeyError as k:
                print("Invalid User Detail")
    except ValueError as v:
        print("Invalid User Input")
