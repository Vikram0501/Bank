#! /usr/bin/Python3.9
import sys
import os.path
import getpass

def hash(sString):
    sHash = ""
    Total = 0
    for i in range(0, len(sString)):
        Total = Total +ord(sString[i])

    for i in range(0, len(sString)):
        sHash = sHash + chr(Total % ord(sString[i]))
    return sHash

def DisplayInfo():
    print("\nName: \t".expandtabs(16) + Name)
    print("Surname: \t" + Surname)
    print("Balance: \tR{:.2f}".format(Balance))

Username = input("Enter your username: ")
Password = getpass.getpass(prompt = "Enter your password: ", stream = None)
Valid = False

with open("hash.txt", "rt") as f:
    sLine = f.read()
    UserHash = sLine[0 : sLine.find("\n")]
    sLine = sLine[sLine.find("\n")+1 : len(sLine)]
    PassHash = sLine
    f.close()

if (UserHash == hash(Username)) and (PassHash == hash(Password)):
    Valid = True

if Valid != True :
    print("\nAccess denied")
    quit()

print("\nAccess granted")

with open("decrypt.py") as f:
    exec(f.read())

with open("bank.txt") as f:
    Bank = f.read()
Name = Bank[0 : Bank.find(",")]
Bank = Bank[Bank.find(",")+1 : len(Bank)]
Surname = Bank[0 : Bank.find(",")]
Bank = Bank[Bank.find(",")+1 : len(Bank)]
Balance = float(Bank)

DisplayInfo()

while Valid == True: 
    Choice = input("Do you want to deposit or withdraw(D/W): ")

    if Choice == "D":
        Deposit = float(input("How much would you like to depost: "))
        Balance = Balance + Deposit
        with open("bank.txt", "wt") as f:
            f.write(Name + "," + Surname + "," + str(Balance))
        DisplayInfo()
    else:
        if Choice == "W":
            Withdrawal = float(input("How much would you like to withdraw: "))
            Balance = Balance - Withdrawal
            with open("bank.txt", "wt") as f:
                f.write(Name + "," + Surname + "," + str(Balance))
            DisplayInfo()
        else:
            if Choice == "exit":
                with open("encrypt.py") as f:
                    exec(f.read())
                Valid = False


