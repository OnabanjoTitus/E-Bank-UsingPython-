CustomerInitialDeposit = 0


def CustomerBalanceUpdater(updatedBalance):
    global CustomerInitialDeposit
    CustomerInitialDeposit = updatedBalance


def AccountStatus(Status):
    accountStatus = "Savings Account and accountBalance is " + str(Status)
    return accountStatus


def accountTypes():
    accountType = input("Enter the accountType")
    accountType = accountType.capitalize()
    if accountType == 'Savings':
        return savingsAccount()
    if accountType == 'Current':
        return currentAccount()


def savingsAccount():
    try:
        global CustomerInitialDeposit
        CustomerInitialDeposit = int(input("Enter the initial deposit"))
        CustomerBalance()
        accountStatus = CustomerInitialDeposit
        return AccountStatus(accountStatus)
    except ValueError as e:
        print("Invalid value for amount")
        print(e)


def currentAccount():
    try:
        InitialDeposit = int(input("Enter the initial deposit"))
        accountStatus = "Current Account and accountBalance is " + str(InitialDeposit)
        return accountStatus
    except ValueError as e:
        print("Invalid value for amount")
        print(e)


def CustomerBalance():
    global CustomerInitialDeposit
    return CustomerInitialDeposit


if __name__ == '__main__':
    accountTypes()
