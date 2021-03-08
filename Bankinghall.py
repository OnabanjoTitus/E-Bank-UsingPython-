from Bank import *


def BankingHall():
    try:
        userInput = int(input("Enter 1 to open an account\nEnter 2 For Customer Enquires\nEnter 3 For "
                              "Transactions\nAnd 4 To Exit Bank"))
        while userInput != 4:
            if userInput == 1:
                Bank()
            if userInput == 2:
                CustomerEnquires()
            if userInput == 3:
                BankTransactions()
            userInput = int(input("Enter 1 to open an account\nEnter 2 For Customer Enquires\nEnter 3 For "
                                  "Transactions\nAnd 4 To Exit Bank"))
    except ValueError as e:
        print("Invalid User Input")
        BankingHall()
    print("Exiting Bank!!!!")


if __name__ == '__main__':
    BankingHall()
