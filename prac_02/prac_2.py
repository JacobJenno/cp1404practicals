""""""""" PRAC 2 """""""""
from random import random

def main():
    choice = menu_display()
    menu_selection(choice)

def menu_display():
    print("")
    print("\033[4mPrac 2\033[0m")
    print("""
            1 - Password activity
            2 - Temperature activity
            3 - Score activity
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
        elif choice == "3":
            score_activity()
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
""" SCORE ACTIVITY """
def score_activity():
    """Runs the password activity."""

    def score_menu():
        input_score = float(input("Enter score: "))
        return input_score

    def score_process(user_score):

        if user_score < 0 or user_score > 100:
            output = "Invalid score"
        elif 0 <= user_score < 50:
            output = "Bad"
        elif 50 <= user_score < 90:
            output = "Passable"
        else:  # 90 to 100
            output = "Excellent"

        return output

    def random_number():
        import random
        random_output = random.randint(1, 100)
        return random_output

    score = score_menu()
    print("User score: ",score," = ", score_process(score))
    if score_process(score) == "Excellent":
        print("You get a prize!")
    random_value = random_number()
    print("Random score: ", random_value, " = ", score_process(random_value))

""""""""""""""""""""""""""""""""""""""""""""""""
main()

