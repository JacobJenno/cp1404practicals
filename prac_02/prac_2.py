def main():
    password_activity()

def password_activity():
    """Runs the password activity."""

    def get_password():
        min_length = 8
        password = input("Enter a password: ")

        while len(password) < min_length:
            print("Password is too short.")
            password = input("Enter a password: ")

        return password

    def password_hidden(password):
        print("*" * len(password))

    user_password = get_password()
    password_hidden(user_password)

main()

