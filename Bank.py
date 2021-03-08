from Customer import *
from BankAccount import *
from Transactions import *

import uuid

BankRecordsForCustomer = {}
BankRecordsForAccountTypes = {}
CustomerPinsRecords = {}
CustomerAccountBalance = {}

accountNumberGlobal: str


def Bank():
    accountNumberFromUUID = uuid.uuid4()
    accountNumberFromUUID = str(accountNumberFromUUID)
    global accountNumberGlobal
    accountNumberGlobal = accountNumberFromUUID
    type(accountNumberFromUUID)

    customerInfo = Customer()
    if customerInfo:
        accountTypesInfo = accountTypes()
        if accountTypesInfo:
            BankRecordsForAccountTypes[accountNumberFromUUID] = accountTypesInfo
            BankRecordsForCustomer[accountNumberFromUUID] = customerInfo
            CustomerAccountBalance[accountNumberFromUUID] = int(input("Enter Customer Initial Deposit"))
            print("\nCustomerInformation")
            print((BankRecordsForCustomer[accountNumberFromUUID]))
            print(f"AccountId is: {accountNumberFromUUID}")
            print(f"Account Type is {accountTypesInfo} and the Customer balance is"
                  f" {CustomerAccountBalance[accountNumberFromUUID]}\n")
            CustomerPinSettings()


def CustomerPinSettings():
    try:
        accountNumberForPin = input("Enter Your Customer AccountId To Set Your Pin")
        if BankRecordsForAccountTypes[accountNumberForPin]:
            try:
                setPin = int(input("Enter any  4 digits number"))
                confirmPin = int(input("Re-enter 4 digits number to confirm Pin"))
                if setPin == confirmPin:
                    CustomerPinsRecords[accountNumberForPin] = setPin
            except ValueError as e:
                print("Invalid Input")

    except KeyError as k:
        print("You Entered an Invalid accountId please Try Again")
        CustomerPinSettings()


def CustomerEnquires():
    try:
        accountNumberForEnquiries = input("\nEnter AccountID")
        if BankRecordsForAccountTypes[accountNumberForEnquiries]:
            try:
                accountPin = int(input("Enter Pin"))
                if CustomerPinsRecords[accountNumberForEnquiries] == accountPin:
                    print((BankRecordsForCustomer[accountNumberForEnquiries]))
                    print(f"Account Type is {BankRecordsForAccountTypes[accountNumberForEnquiries]} and the Customer "
                          f"balance is "
                          f" {CustomerAccountBalance[accountNumberGlobal]}\n")
            except ValueError as e:
                print("Invalid pin")
            except KeyError as k:
                print("Invalid key input")
    except KeyError as k:
        print("Invalid AccountId")


def BankTransactions():
    try:
        ReturnValue = Transactions(BankRecordsForAccountTypes, CustomerPinsRecords, CustomerAccountBalance)
        CustomerAccountBalance[ReturnValue[0]] = ReturnValue[1]
    except TypeError as e:
        print("Incorrect 1User Information")


if __name__ == '__main__':
    Bank()
