
def main():
    """Function docstring"""
    # statements...

def get_password():
    global password
    password = input("Enter a password: ")

    while len(password) < min_length:
        print("Password is too short.")
        password = input("Enter a password: ")

def password_hidden():
    print("*" * len(password))

min_length = 8
get_password()
password_hidden()

main()

