
import datetime

import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'bankapp', password = 'Wong2021!')

cursor = connection.cursor()


uName = ""
pWord = ""
email = "" 
balanceID = 3000

def viewAccount():
    global uName
    cursor.execute("SELECT idBalance, date, amount, description FROM balance WHERE username = '" + uName + "'")
    print("ID      DATE      AMOUNT   DESCRIPTION")
    for item in cursor:
        print(item)



def viewAccountBalance():
    if hasAccount():
        print("----------------------")
        balance = 0
        cursor.execute("SELECT amount FROM balance WHERE username = '" + uName + "'")
        for item in cursor:
            balance += float(item[0]) 
        print("\033[92mYour balance: $" + str(balance) + "\033[0m")  # Cyan
        print("----------------------")

def deposit():
    if hasAccount():
        deposit = input("How much would you like to deposit? ")
        desc = input("What would you like to add as the description for this deposit? ")
        today = datetime.date.today()
        global balanceID
        global uName
        balanceID += 1
        addDeposit = """
            INSERT INTO balance(idBalance, date, amount, description, username)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (balanceID, today.strftime("%x"), deposit, desc, uName)
        cursor.execute(addDeposit, values)
        viewAccountBalance()

def withdrawal():
    if hasAccount():
        withdrawal = input("How much would you like to withdraw? ")
        desc = input("What would you like to add as the description for this withdrawal? ")
        today = datetime.date.today()
        global balanceID
        balanceID += 1
        addWithdrawal = """
            INSERT INTO balance(idBalance, date, amount, description, username)
            VALUES (%s, %s, %s, %s, %s)
        """
        amount = -float(withdrawal)
        values = (balanceID, today.strftime("%x"), amount, desc, uName)
        cursor.execute(addWithdrawal, values)
        viewAccountBalance()

def createAccount():
    print("\nWelcome! To create a new account, please enter the following information... ")
    global uName, pWord, email
    uName = input("New username: ")
    pWord = input("Password: ")
    email = input("Email: ")
    cursor2 = connection.cursor()
    cursor2.execute("SELECT * FROM account WHERE userName = %s", (uName, ))
    rows = cursor.fetchall()
    print(rows)
    if len(rows) == 0:
        print("Setting up a new account...")
        addUser = "INSERT INTO account(userName, password, email) VALUES ('" + uName + "', '" +pWord+"', '"+ email+"')"
        cursor.execute(addUser)
        connection.commit()
        print("You've successfully created a new account!")
    else:
        print("There is already an existing account with that username. Choose a new one or sign in to that account.")
        choice = input("Create account [c] or log in [l]? ")
        if choice == "c":
            createAccount()
        elif choice == "l":
            logIn()

def deleteAccount():
    if hasAccount():
        confirmation = input("Are you sure you want to delete your account? You will not be able to undo this process and all of your money will be donated to the bank. (y) ")
        if confirmation == "y":
            global uName, pWord, email
            cursor.execute("DELETE FROM account WHERE userName = %s AND password = %s AND email = %s", (uName, pWord, email))
            connection.commit()
            uName = ""
            pWord = ""
            email = ""
            print("Successfully removed your account")

def logIn():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    global uName, pWord, email
    cursor.execute("SELECT userName, password, email FROM account WHERE userName = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        uName, pWord, email = result
        print("Successfully signed into " + uName + "'s account")
    else:
        print("That didn't seem to work.")
        # handle case where login failed



def modifyAccount():
    if hasAccount():
        global uName
        global pWord
        global email
        print("Username: " + uName)
        # for i in pWord:
        #     password += "*"
        print("Password: " + pWord)
        print("Email: " + email)
        choice = input("What would you like to modify? ")
        if choice == "u":
            uName = input("Enter a new username: ")  #immediately changes the global variable... change
            mail = input("Enter your email to authorize this action: ")
            cursor.execute("UPDATE account SET userName = '" + uName + "' WHERE email = '" + mail + "' AND password = '" + pWord + "'")
            connection.commit()
            print("Username changed successfully! ")
        elif choice == "p":
            pWord1 = input("Enter a new password: ")
            pWord2 = input("Retype your password: ")
            if pWord1 == pWord2:
                pWord = pWord1
                name = input("Enter your username to authorize this action: ")
                cursor.execute("UPDATE account SET password = '" + pWord + "' WHERE email = '" + email + "' AND username = '" + name + "'")
                connection.commit()                
                print("Password changed successfully!")
            else:
                print("Not the same password... password not changed")
        elif choice == "e":
            email = input("Enter a new backup email account to link your bank account to: ")             #immediately changes the global variable... change
            passWord = input("Enter your password to authorize this action: ")
            cursor.execute("UPDATE account SET email = '" + email + "' WHERE password = '" + passWord + "' AND username = '" + uName + "'")
            connection.commit()
            print("Email changed successfully! ")

def hasAccount():
    if uName is None:
        print("You don't have an account yet. Please choose option 4 to create an account to get started.")
        return False
    else:
        return True
def startingPage():
    print("\nWelcome!")
    print("\nCaitlin's bank -------------")
    print("1) Create a new account")
    print("2) Log in to existing account")
    print("3) Leave")
    choice = input("What would you like to do? ")

    if choice == "1": 
        createAccount()
    elif choice == "2": 
        logIn()
    elif choice == "3":
        print("Thanks for visiting!")
    else:
        print("I didn't quite catch that. Please enter a number from above...")
        logIn()


startingPage()
while True:
    print("\nCaitlin's bank -------------")
    print("1) View account balance")
    print("2) Make a deposit")
    print("3) Make a withdrawal")
    print("4) Delete an account")
    print("5) Modify account details")
    print("6) Leave")
    print("7) Back to sign in")
    choice = input("What would you like to do? ")

    if choice == "1":
        viewAccount()
    elif choice == "2": 
        deposit()
        connection.commit()
    elif choice == "3": 
        withdrawal()
        connection.commit()
    elif choice == "4": 
        deleteAccount()
    elif choice == "5": 
        modifyAccount()
        connection.commit()
    elif choice == "6":
        break
    elif choice == "7":
        startingPage()
    else:
        print("I didn't quite catch that. Please enter a number from above...")


cursor.close()
connection.close()