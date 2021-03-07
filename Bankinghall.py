from Bank import *


def BankingHall():
    try:
        userInput = int(input("Enter 1 to open an account\nEnter 2 For Customer Enquires\nAnd 3 to exit Bank"))
        while userInput != 3:
            if userInput == 1:
                Bank()
            if userInput == 2:
                CustomerEnquires()
            if userInput == 4:
                BankTransactions()
            userInput = int(input("Enter 1 to open an account\nEnter 2 For Customer Enquires\nAnd 3 to exit Bank"))
    except ValueError as e:
        print("Invalid User Input")
        BankingHall()
    print("Exiting Bank!!!!")


if __name__ == '__main__':
    BankingHall()
