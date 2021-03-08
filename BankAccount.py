
def accountTypes():
    accountType = input("Enter the accountType")
    accountType = accountType.capitalize()
    if accountType == 'Savings':
        return savingsAccount()
    if accountType == 'Current':
        return currentAccount()


def savingsAccount():
    return "Savings"


def currentAccount():
    return "Current"


if __name__ == '__main__':
    accountTypes()
