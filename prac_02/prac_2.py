""""""""" PRAC 2 """""""""

def main():
    choice = menu_display()
    menu_selection(choice)

def menu_display():
    print("\033[4mPrac 2\033[0m")
    print("""
            1 - Password activity
            2 - Temperature activity
            Q - Quit (ends run)
                """)
    choice = input(">>> ").upper()
    return choice

def  menu_selection(choice):
    while True:
        if choice == "1":
            password_activity()
            choice = menu_display()
        elif choice == "2":
            temperature_activity()
            choice = menu_display()
        else: break


""""""""""""""""""""""""""""""""""""""""""""""""
""" PASSWORD ACTIVITY """
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
""""""""""""""""""""""""""""""""""""""""""""""""
""" TEMPERATURE ACTIVITY """
def temperature_activity():
    """Runs the password activity."""

    def temperature_menu():
        #Creates temperature menu
        print("\033[4mTemperature Converter\033[0m")
        temp_menu = """
        C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius
        Q - Quit """
        print(temp_menu)
        print(" ")

        choice = input("Menu Option >>> ").upper()

        return choice

    def temp_choice_maker(choice):
        while choice != "Q":
            if choice == "C":
                celsius_to_fahrenheit()
                choice = input("Menu Option >>> ").upper()
            elif choice == "F":
                fahrenheit_to_celsius()
                choice = input("Menu Option >>> ").upper()
            else:
                print("Invalid option, try C,F or Q")
                choice = input("Menu Option >>> ").upper()

        print("Thank you.")
        print(" ")

    def celsius_to_fahrenheit():
        while True:
            try:
                celsius = float(input("Celsius: "))
                fahrenheit = celsius * 9.0 / 5 + 32
                print(f"Result: {fahrenheit:.2f} F")
                break
            except ValueError:
                print("Invalid option, input a number")

    def fahrenheit_to_celsius():
        while True:
            try:
                fahrenheit = float(input("Fahrenheit: "))
                celsius = 5 / 9 * (fahrenheit - 32)
                print(f"Result: {celsius:.2f} C")
                break
            except ValueError:
                print("Invalid option, input a number")

    user_choice = temperature_menu()
    temp_choice_maker(user_choice)

""""""""""""""""""""""""""""""""""""""""""""""""
main()

