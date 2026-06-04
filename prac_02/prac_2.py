
def main():
    """Function docstring"""
    # statements...

min_length = 8

def get_password():
    global password
    password = input("Enter a password: ")

    while len(password) < min_length:
        print("Password is too short.")
        password = input("Enter a password: ")

get_password()


def password_hidden():
    print("*" * len(password))

password_hidden()

main()

