def accountTypes():
    accountType = input("Enter the accountType")
    accountType = accountType.capitalize()

    if accountType == 'Savings':
        savingsAccount()
    if accountType == 'Current':
        currentAccount()


def savingsAccount():
    try:
        InitialDeposit = int(input("Enter the initial deposit"))
    except ValueError as e:
        print("Invalid value for amount")
        print(e)


def currentAccount():
    try:
        InitialDeposit = int(input("Enter the initial deposit"))
    except ValueError as e:
        print("Invalid value for amount")
        print(e)


if __name__ == '__main__':
    accountTypes()
