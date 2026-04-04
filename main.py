from sign_in import sign_in
from log_in import log_in

class Account:

    def sign_in(self):
        sign_in()

    def log_in(self):
        log_in()

user = Account()

while True:
    selection = input("\nWould you like to log in, or sign in? (S/L): ").lower()
    if selection == "s":
        user.sign_in()
    elif selection == "l":
        user.log_in()
    else:
        print("\nEnter a valid selection.")