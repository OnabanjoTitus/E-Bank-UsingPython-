def Customer():
    firstName = input("Enter customer first name")
    otherNames = input("Enter Customer OtherName")
    lastName = input("Enter customer last name")
    phoneNumber = input("Enter customer phoneNumber")
    email = input("Enter customer email address")
    customer = "firstName: " + firstName + "\notherName: " + otherNames + "\nlastName: " + lastName + "\nPhoneNumber: " + phoneNumber + "\nE-mail: " + email

    return customer


if __name__ == '__main__':
    Customer()
