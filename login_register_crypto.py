
#step 1: create the flask_server.py to link all files (html, py)
#len=length of password (must be 8 or more)
#db=database
#pip install flask-bcrypt

def register():
    db = open("database.txt", "r")
    Username = input("Enter a username:")
    Password = input("Enter a password (minimum 8 characters):")
    Password1 = input("Confirm your password:")

#create a list to store all usernames and passwords. Otherwise, they will appear as plain text
    store_username = []
    store_password = []

#use for loop to split text in the database
    for i in db:
#split the username and password first
#a=column 1 for username, b=column b for password
        a,b = i.split(", ")
        b = b.strip()
        store_username.append(a)
        store_password.append(b)
#put data in a dictionary
    data = dict(zip(store_username, store_password))
    print(data)

    if Password != Password1:
        print("INCORRECT password. Please try again.")
    #call register function again (recursive function)
        register()

    else:
        if len(Password)<8:
            print("Your password is too short. Try again.")
            register()
        elif Username in store_username:
            print("Username exists already. Try another one.")
            register()
    #if all the above is false
        else:
            db = open("database.txt", "a")
    #"a" = append
    #The append() method in python adds a single item to the existing list. 
    #It doesn't return a new list of items but will modify the original list by adding the item to the end of the list.
    #for the username and password to be saved in the database.txt. Username and password will be separated by a comma.
            db.write(Username + "," + Password + "\n")
            print("Registration was successful")

register()


def login():
    Username = input("Enter your username:")
    Password = input("Enter your password:")

    if Username == True:
        print()

login()


"""
Sources:
https://www.youtube.com/watch?v=dR_cDapPWyY&t=0s
"""


