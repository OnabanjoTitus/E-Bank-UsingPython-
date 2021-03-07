CustomerInitialDeposit = 0


def accountTypes():
    accountType = input("Enter the accountType")
    accountType = accountType.capitalize()

    if accountType == 'Savings':
        return savingsAccount()
    if accountType == 'Current':
        return currentAccount()


def savingsAccount():
    try:
        InitialDeposit = int(input("Enter the initial deposit"))
        global CustomerInitialDeposit
        CustomerInitialDeposit = InitialDeposit
        CustomerBalance()
        accountStatus = "Savings Account and accountBalance is " + str(CustomerInitialDeposit)
        return accountStatus
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
    return CustomerInitialDeposit


def CustomerBalanceUpdater(updatedBalance):
    global CustomerInitialDeposit
    CustomerInitialDeposit = updatedBalance


if __name__ == '__main__':
    accountTypes()
