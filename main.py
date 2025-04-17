"""
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Caitlin's Bank")

# Add a label
welcome = tk.Label(window, text="Welcome to your bank account!")
choice1 = tk.Button(window, text="1) View account balance")
choice2 = tk.Button(window, text="2) Make a deposit")
choice3 = tk.Button(window, text="3) Create a new account")
choice4 = tk.Button(window, text="4) Delete an account")
choice5 = tk.Button(window, text="5) Modify account details")

welcome.pack()

# Add a button
choice1.pack()
choice2.pack()
choice3.pack()
choice4.pack()
choice5.pack()

# Start the Tkinter event loop
window.mainloop()

"""
import datetime

import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'bankapp', password = 'Wong2021!')

cursor = connection.cursor()

cursor.execute("DELETE FROM account")
cursor.execute("DELETE FROM balance")

addData = "INSERT INTO account(userName, password, email) VALUES ('dogs', 'ilovedogs', 'dog@gmail.com');"
cursor.execute(addData)
cursor.execute("INSERT INTO account(userName, password, email) VALUES ('LuckyDucky', 'Wong', 'lucky@gmail.com')")
cursor.execute("INSERT INTO account(userName, password, email) VALUES ('batman', 'bat', 'bat@gmail.com')")

connection.commit()



balance = 0
uName = ""
pWord = ""
email = "" 
balanceID = 3000

def viewAccount():
    cursor.execute("SELECT * FROM balance")
    print("ID      DATE      AMOUNT   DESCRIPTION")
    for item in cursor:
        print(item)



def viewAccountBalance():
    if hasAccount():
        print("----------------------")
        print("Your balance: " + str(balance))
        print("----------------------")

def deposit():
    if hasAccount():
        deposit = input("How much would you like to deposit? ")
        desc = input("What would you like to add as the description for this deposit? ")
        today = datetime.date.today()
        global balanceID
        balanceID += 1
        addDeposit = "INSERT INTO balance(idBalance, date, amount, description) VALUES (" + str(balanceID) + ", '" + today.strftime("%x") + "', " +  deposit + ", '" + desc+"')"
        cursor.execute(addDeposit)
        global balance 
        balance += int(deposit)
        viewAccountBalance()

def withdrawal():
    if hasAccount():
        withdrawal = input("How much would you like to withdraw? ")
        desc = input("What would you like to add as the description for this withdrawal? ")
        today = datetime.date.today()
        global balanceID
        balanceID += 1
        addWithdrawal = "INSERT INTO balance(idBalance, date, amount, description) VALUES (" + str(balanceID) + ", '" + today.strftime("%x") + "', -" +  withdrawal + ", '" + desc+"')"
        cursor.execute(addWithdrawal)
        global balance 
        balance -= int(withdrawal)
        viewAccountBalance()

def createAccount():
    print("\nWelcome! To create a new account, please enter the following information... ")
    global uName, pWord, email
    uName = input("New username: ")
    pWord = input("Password: ")
    email = input("Email: ")
    addUser = "INSERT INTO account(userName, password, email) VALUES ('" + uName + "', '" +pWord+"', '"+ email+"')"
    cursor.execute(addUser)
    connection.commit()
    print("You've successfully created a new account!")

def deleteAccount():
    if hasAccount():
        confirmation = input("Are you sure you want to delete your account? (y)")
        if confirmation.upper == "Y":
            print("Deleted")

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

def hasAccount():
    if uName is None:
        print("You don't have an account yet. Please choose option 4 to create an account to get started.")
        return False
    else:
        return True
    
print("Welcome to your bank account!")
while True:

    print("\nCaitlin's bank -------------")
    print("1) View account balance")
    print("2) Make a deposit")
    print("3) Make a withdrawal")
    print("4) Create a new account")
    print("5) Delete an account")
    print("6) Modify account details")
    choice = input("What would you like to do? ")

    if choice == "1":
        viewAccount()
        #connection.commit()
    elif choice == "2": 
        deposit()
        connection.commit()
    elif choice == "3": 
        withdrawal()
        connection.commit()
    elif choice == "4": 
        createAccount()
        connection.commit()
    elif choice == "5": 
        deleteAccount()
        connection.commit()
    elif choice == "6": 
        modifyAccount()
        connection.commit()

cursor.close()
connection.close()