import json

def log_in():

    account_info = {}

    print("================= LOG IN ===================")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    account_info[email] = password

    with open("account_info.json", "r") as file:
        account_info = json.load(file)

    if email in account_info:
        if account_info[email] == password:
            print("\nAccount found, access granted.")
        else:
            print("Incorrect password.")
    else:
        print("Account not found.")
#