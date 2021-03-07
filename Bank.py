from Customer import *
from BankAccount import *
from Transactions import *

import uuid

BankRecordsForCustomer = {}
BankRecordsForAccountTypes = {}
CustomerPinsRecords = {}
accountNumberFromUUID = uuid.uuid4()
accountNumberFromUUID = str(accountNumberFromUUID)


def Bank():
    type(accountNumberFromUUID)
    customerInfo = Customer()
    if customerInfo:
        accountTypesInfo = accountTypes()
        if accountTypesInfo:
            BankRecordsForAccountTypes[accountNumberFromUUID] = accountTypesInfo
            BankRecordsForCustomer[accountNumberFromUUID] = customerInfo
            print("\nCustomerInformation")
            print((BankRecordsForCustomer[accountNumberFromUUID]))
            print((BankRecordsForAccountTypes[accountNumberFromUUID]))
            print(f"AccountId is: {accountNumberFromUUID}\n")
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
                    print((BankRecordsForAccountTypes[accountNumberForEnquiries])+"\n")
            except ValueError as e:
                print("Invalid pin")
            except KeyError as k:
                print("Invalid key input")
    except KeyError as k:
        print("Invalid AccountId")


if __name__ == '__main__':
    Bank()
