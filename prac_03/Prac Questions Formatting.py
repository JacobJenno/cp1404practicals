import time

def main():
    choice = menu_display()
    menu_selection(choice)

def menu_display():
    print("")
    print("\033[4mPrac 3\033[0m")
    print("""
            1 - String Formatting 
            2 - Random Numbers 
            3 - Capitalist Conrad 
            4 - Exceptions to Complete 
            5 - Password Checker 
            6 - Files 
            7 - File Size 
            Q - Quit (ends run)
                """)
    choice = input(">>> ").upper()
    return choice

def  menu_selection(choice):
    while True:
        if choice == "1":
            string_formatting_q()
            choice = menu_display()
        elif choice == "2":
            random_numbers_q()
            choice = menu_display()
        elif choice == "3":
            capitalist_conrad_q()
            choice = menu_display()
        elif choice == "4":
            capitalist_conrad_q()
            choice = menu_display()
        elif choice == "5":
            password_checker_q()
            choice = menu_display()
        elif choice == "6":
            files_q()
            choice = menu_display()
        elif choice == "7":
            files_size_q()
            choice = menu_display()
        elif choice == "Q":
            break
        else:
            print("Not a valid choice. Insert an available option")
            time.sleep(2)
            choice = menu_display()


# String Formatting
def string_formatting_q():
    print("test")

# Random Numbers
def random_numbers_q():
    print("test")

# Capitalist Conrad
def capitalist_conrad_q():
    print("test")

# Exceptions
def exceptions_q():
    print("test")

# Password Checker
def password_checker_q():
    print("test")

# Files
def files_q():
    print("test")

# Files Size
def files_size_q():
    print("test")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
main()