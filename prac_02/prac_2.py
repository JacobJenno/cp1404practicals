
def main():
    password = get_password()
    password_hidden(password)

def get_password():
    min_length = 8
    password = input("Enter a password: ")

    while len(password) < min_length:
        print("Password is too short.")
        password = input("Enter a password: ")

    return password

def password_hidden(password):
    print("*" * len(password))

main()

