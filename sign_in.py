import json

def sign_in():

    account_info = {}

    print("\n=================== CREATE ACCOUNT ===================")
    email = input("Enter your email: ")
    password = input("Create a strong password: ")
    print("======================================================")
    account_info[email] = password

    try:

        with open("account_info.json", "r") as file:
            account_info = json.load(file)

    except:

        account_info = {}

    account_info[email] = password

    with open("account_info.json", "w") as file:
        json.dump(account_info, file, indent=5)


    print("Account Created!")
    print("======================================================")
#